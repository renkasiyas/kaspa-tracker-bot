# ABOUTME: Kaspa gRPC client for real-time address monitoring using MessageStream
# ABOUTME: All communication via bidirectional MessageStream on mainnet.kasanova.io:16110

import asyncio
import logging
from typing import Any, Callable, Dict, Optional

import grpc

from ..protos import messages_pb2, messages_pb2_grpc, rpc_pb2

logger = logging.getLogger(__name__)


class KaspaGrpcClient:
    """gRPC client for Kaspa real-time monitoring."""

    def __init__(self, endpoint: str = "mainnet.kasanova.io:16110"):
        self.endpoint = endpoint
        self.channel: Optional[grpc.aio.Channel] = None
        self.stub = None
        self.connected = False
        self.subscriptions = set()
        self.callback = None
        self.request_queue = asyncio.Queue()
        self.response_futures = {}
        self.request_id = 0
        self.stream_task = None

    async def connect(self) -> bool:
        """Connect to Kaspa node via gRPC."""
        try:
            # Create channel with keepalive options
            self.channel = grpc.aio.insecure_channel(
                self.endpoint,
                options=[
                    ("grpc.keepalive_time_ms", 10000),
                    ("grpc.keepalive_timeout_ms", 5000),
                    ("grpc.keepalive_permit_without_calls", True),
                    ("grpc.http2.max_pings_without_data", 0),
                ],
            )

            # Create RPC stub
            self.stub = messages_pb2_grpc.RPCStub(self.channel)

            # Start message stream
            self.connected = True  # Set connected first so request_stream doesn't exit
            self.stream_task = asyncio.create_task(self._run_message_stream())

            # Test connection with GetInfo
            await asyncio.sleep(0.5)  # Let stream start

            request = messages_pb2.KaspadRequest()
            self.request_id += 1
            request.id = self.request_id
            request.getInfoRequest.CopyFrom(rpc_pb2.GetInfoRequestMessage())

            future = asyncio.Future()
            self.response_futures[self.request_id] = future
            await self.request_queue.put(request)

            try:
                response = await asyncio.wait_for(future, timeout=5)
                if response.HasField("getInfoResponse"):
                    info = response.getInfoResponse
                    logger.info(f"✅ Connected to Kaspa gRPC node at {self.endpoint}")
                    logger.info(f"   Server version: {info.serverVersion}")
                    logger.info(f"   Is synced: {info.isSynced}")
                    logger.info(f"   Is UTXO indexed: {info.isUtxoIndexed}")
                    return True
            except asyncio.TimeoutError:
                logger.error("Connection test timeout")
                self.connected = False
                return False

        except Exception as e:
            logger.error(f"Failed to connect to Kaspa node: {e}")
            self.connected = False
            return False

    async def disconnect(self):
        """Disconnect from Kaspa node."""
        self.connected = False
        if self.stream_task:
            self.stream_task.cancel()
            try:
                await self.stream_task
            except asyncio.CancelledError:
                pass
        if self.channel:
            await self.channel.close()
            self.channel = None
            self.stub = None

    async def get_balance(self, address: str) -> Optional[Dict[str, Any]]:
        """Get balance for an address via gRPC."""
        if not self.connected:
            await self.connect()

        try:
            request = messages_pb2.KaspadRequest()
            self.request_id += 1
            request.id = self.request_id
            request.getBalanceByAddressRequest.CopyFrom(
                rpc_pb2.GetBalanceByAddressRequestMessage(address=address)
            )

            future = asyncio.Future()
            self.response_futures[self.request_id] = future
            await self.request_queue.put(request)

            response = await asyncio.wait_for(future, timeout=5)
            if response.HasField("getBalanceByAddressResponse"):
                balance_resp = response.getBalanceByAddressResponse
                return {
                    "balance": balance_resp.balance,
                    "address": address,
                    "balance_kas": balance_resp.balance / 100_000_000,
                }

        except asyncio.TimeoutError:
            logger.error(f"Timeout getting balance for {address}")
        except Exception as e:
            logger.error(f"Failed to get balance for {address}: {e}")
        return None

    async def subscribe_to_address(self, address: str, callback: Callable) -> bool:
        """Subscribe to UTXO changes for an address."""
        if not self.connected:
            await self.connect()

        try:
            self.callback = callback

            # Check if already subscribed to this address
            if address in self.subscriptions:
                logger.info(f"Already subscribed to address: {address}")
                return True

            self.subscriptions.add(address)

            # Only subscribe to DAA score changes once (for the first address)
            if len(self.subscriptions) == 1:
                # Subscribe to DAA score changes (for new blocks)
                request = messages_pb2.KaspadRequest()
                self.request_id += 1
                request.id = self.request_id
                request.notifyVirtualDaaScoreChangedRequest.CopyFrom(
                    rpc_pb2.NotifyVirtualDaaScoreChangedRequestMessage()
                )

                future = asyncio.Future()
                self.response_futures[self.request_id] = future
                await self.request_queue.put(request)

                # Wait for confirmation
                response = await asyncio.wait_for(future, timeout=5)
                if not response.HasField("notifyVirtualDaaScoreChangedResponse"):
                    logger.error("Failed to subscribe to DAA score changes")
                    self.subscriptions.remove(address)
                    return False

            # Subscribe to UTXO changes for this specific address
            request = messages_pb2.KaspadRequest()
            self.request_id += 1
            request.id = self.request_id
            request.notifyUtxosChangedRequest.CopyFrom(
                rpc_pb2.NotifyUtxosChangedRequestMessage(addresses=[address])
            )

            future = asyncio.Future()
            self.response_futures[self.request_id] = future
            await self.request_queue.put(request)

            response = await asyncio.wait_for(future, timeout=5)
            if response.HasField("notifyUtxosChangedResponse"):
                logger.info(f"✅ Subscribed to changes for address: {address}")
                return True
            else:
                logger.error("Failed to subscribe to UTXO changes")
                self.subscriptions.remove(address)
                return False

        except Exception as e:
            logger.error(f"Failed to subscribe to {address}: {e}")
            if address in self.subscriptions:
                self.subscriptions.remove(address)
            return False

    async def unsubscribe_from_address(self, address: str) -> bool:
        """Unsubscribe from UTXO changes for an address."""
        if address in self.subscriptions:
            self.subscriptions.remove(address)
            logger.info(f"Unsubscribed from address: {address}")
            return True
        return False

    async def _run_message_stream(self):
        """Run the bidirectional message stream."""
        try:
            # Create request iterator
            request_iter = self._create_request_stream()

            # Start message stream
            response_stream = self.stub.MessageStream(request_iter)

            # Process responses
            async for response in response_stream:
                await self._handle_response(response)

        except grpc.aio.AioRpcError as e:
            if e.code() != grpc.StatusCode.CANCELLED:
                logger.error(f"Stream error: {e}")
        except Exception as e:
            logger.error(f"Error in message stream: {e}")

    async def _create_request_stream(self):
        """Create request stream."""
        while self.connected or not self.request_queue.empty():
            try:
                # Get request from queue with timeout
                request = await asyncio.wait_for(self.request_queue.get(), timeout=1.0)
                yield request
            except asyncio.TimeoutError:
                # No requests, continue loop
                continue
            except Exception as e:
                logger.error(f"Error in request stream: {e}")
                break

    async def _handle_response(self, response):
        """Handle response from message stream."""
        try:
            # Check if response is None
            if response is None:
                return

            # Check if this is a response to a request
            if hasattr(response, "id") and response.id > 0 and response.id in self.response_futures:
                future = self.response_futures.pop(response.id)
                future.set_result(response)
                return

            # Handle notifications (no request ID)
            if response.HasField("utxosChangedNotification"):
                notification = response.utxosChangedNotification

                for utxo in notification.added:
                    if utxo.address in self.subscriptions and self.callback:
                        tx_id = "unknown"
                        index = 0
                        if utxo.outpoint:
                            # transactionId could be bytes or string
                            if utxo.outpoint.transactionId:
                                tx_id = (
                                    utxo.outpoint.transactionId.hex()
                                    if hasattr(utxo.outpoint.transactionId, "hex")
                                    else str(utxo.outpoint.transactionId)
                                )
                            index = utxo.outpoint.index

                        await self.callback(
                            "utxo_added",
                            utxo.address,
                            {
                                "amount": utxo.utxoEntry.amount if utxo.utxoEntry else 0,
                                "amount_kas": (
                                    (utxo.utxoEntry.amount / 100_000_000) if utxo.utxoEntry else 0
                                ),
                                "tx_id": tx_id,
                                "index": index,
                            },
                        )

                for utxo in notification.removed:
                    if utxo.address in self.subscriptions and self.callback:
                        tx_id = "unknown"
                        index = 0
                        if utxo.outpoint:
                            # transactionId could be bytes or string
                            if utxo.outpoint.transactionId:
                                tx_id = (
                                    utxo.outpoint.transactionId.hex()
                                    if hasattr(utxo.outpoint.transactionId, "hex")
                                    else str(utxo.outpoint.transactionId)
                                )
                            index = utxo.outpoint.index

                        await self.callback(
                            "utxo_removed", utxo.address, {"tx_id": tx_id, "index": index}
                        )

            elif response.HasField("virtualDaaScoreChangedNotification"):
                notification = response.virtualDaaScoreChangedNotification
                if self.callback:
                    await self.callback(
                        "new_block", None, {"virtual_daa_score": notification.virtualDaaScore}
                    )

        except Exception as e:
            import traceback

            logger.error(f"Error handling response: {e}")
            logger.error(f"Traceback: {traceback.format_exc()}")
