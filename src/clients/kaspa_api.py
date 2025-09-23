# ABOUTME: Kaspa REST API client for fetching address data, UTXOs, and transactions
# ABOUTME: Uses api.kaspa.org for comprehensive blockchain data

import asyncio
import logging
from typing import Any, Dict, List, Optional

import httpx

logger = logging.getLogger(__name__)


class KaspaAPI:
    """REST API client for Kaspa blockchain data."""

    def __init__(self, base_url: str = "https://api.kaspa.org"):
        self.base_url = base_url
        self.client: Optional[httpx.AsyncClient] = None

    async def _ensure_client(self):
        """Ensure httpx client exists."""
        if self.client is None:
            self.client = httpx.AsyncClient()

    async def close(self):
        """Close the client."""
        if self.client:
            await self.client.aclose()
            self.client = None

    async def get_address_info(self, address: str) -> Optional[Dict[str, Any]]:
        """Get comprehensive address information."""
        await self._ensure_client()

        try:
            url = f"{self.base_url}/addresses/{address}"
            response = await self.client.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Failed to get address info: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"Error fetching address info: {e}")
            return None

    async def get_balance(self, address: str) -> Optional[Dict[str, Any]]:
        """Get balance for an address."""
        await self._ensure_client()

        try:
            url = f"{self.base_url}/addresses/{address}/balance"
            response = await self.client.get(url)
            if response.status_code == 200:
                data = response.json()
                return {
                    "balance": data.get("balance", 0),
                    "balance_kas": data.get("balance", 0) / 100_000_000,
                    "address": address,
                }
            else:
                logger.error(f"Failed to get balance: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            return None

    async def get_utxos(self, address: str) -> Optional[List[Dict[str, Any]]]:
        """Get UTXOs for an address."""
        await self._ensure_client()

        try:
            url = f"{self.base_url}/addresses/{address}/utxos"
            response = await self.client.get(url)
            if response.status_code == 200:
                data = response.json()
                utxos = []
                for utxo in data:
                    # Amount is nested in utxoEntry.amount as a string
                    utxo_entry = utxo.get("utxoEntry", {})
                    amount = int(utxo_entry.get("amount", "0"))

                    utxos.append(
                        {
                            "amount": amount,
                            "amount_kas": amount / 100_000_000,
                            "tx_id": utxo.get("transactionId", ""),
                            "index": utxo.get("index", 0),
                            "script": utxo_entry.get("scriptPublicKey", {}).get(
                                "scriptPublicKey", ""
                            ),
                            "block_time": utxo_entry.get("blockDaaScore", 0),
                        }
                    )
                return utxos
            else:
                logger.error(f"Failed to get UTXOs: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"Error fetching UTXOs: {e}")
            return None

    async def get_transactions(
        self, address: str, limit: int = 50
    ) -> Optional[List[Dict[str, Any]]]:
        """Get recent transactions for an address."""
        await self._ensure_client()

        try:
            url = f"{self.base_url}/addresses/{address}/full-transactions"
            params = {"limit": limit}
            response = await self.client.get(url, params=params)
            if response.status_code == 200:
                raw_txs = response.json()
                # Process and simplify the transaction data
                transactions = []
                for tx in raw_txs:
                    # Determine if this is incoming or outgoing for the address
                    is_incoming = False
                    is_outgoing = False
                    amount = 0

                    # Check outputs for incoming
                    for output in tx.get("outputs", []):
                        if output.get("script_public_key_address") == address:
                            is_incoming = True
                            amount += output.get("amount", 0)

                    # Check inputs for outgoing (would need previous tx data for full accuracy)
                    # For now, if address appears only in outputs, it's incoming
                    tx_type = "incoming" if is_incoming else "outgoing"

                    transactions.append(
                        {
                            "transaction_id": tx.get("transaction_id", ""),
                            "transaction_type": tx_type,
                            "amount": amount,
                            "timestamp": tx.get("block_time", 0),
                            "block_hash": tx.get("accepting_block_hash", ""),
                        }
                    )
                return transactions
            else:
                logger.error(f"Failed to get transactions: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"Error fetching transactions: {e}")
            return None

    async def get_transaction(self, tx_id: str) -> Optional[Dict[str, Any]]:
        """Get details of a specific transaction."""
        await self._ensure_client()

        try:
            url = f"{self.base_url}/transactions/{tx_id}"
            response = await self.client.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Failed to get transaction: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"Error fetching transaction: {e}")
            return None
