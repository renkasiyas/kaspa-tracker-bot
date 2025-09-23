from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class RpcNotifyCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFY_START: _ClassVar[RpcNotifyCommand]
    NOTIFY_STOP: _ClassVar[RpcNotifyCommand]

NOTIFY_START: RpcNotifyCommand
NOTIFY_STOP: RpcNotifyCommand

class RPCError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RpcBlock(_message.Message):
    __slots__ = ("header", "transactions", "verboseData")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    VERBOSEDATA_FIELD_NUMBER: _ClassVar[int]
    header: RpcBlockHeader
    transactions: _containers.RepeatedCompositeFieldContainer[RpcTransaction]
    verboseData: RpcBlockVerboseData
    def __init__(
        self,
        header: _Optional[_Union[RpcBlockHeader, _Mapping]] = ...,
        transactions: _Optional[_Iterable[_Union[RpcTransaction, _Mapping]]] = ...,
        verboseData: _Optional[_Union[RpcBlockVerboseData, _Mapping]] = ...,
    ) -> None: ...

class RpcBlockHeader(_message.Message):
    __slots__ = (
        "version",
        "parents",
        "hashMerkleRoot",
        "acceptedIdMerkleRoot",
        "utxoCommitment",
        "timestamp",
        "bits",
        "nonce",
        "daaScore",
        "blueWork",
        "pruningPoint",
        "blueScore",
    )
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    HASHMERKLEROOT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTEDIDMERKLEROOT_FIELD_NUMBER: _ClassVar[int]
    UTXOCOMMITMENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BITS_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    DAASCORE_FIELD_NUMBER: _ClassVar[int]
    BLUEWORK_FIELD_NUMBER: _ClassVar[int]
    PRUNINGPOINT_FIELD_NUMBER: _ClassVar[int]
    BLUESCORE_FIELD_NUMBER: _ClassVar[int]
    version: int
    parents: _containers.RepeatedCompositeFieldContainer[RpcBlockLevelParents]
    hashMerkleRoot: str
    acceptedIdMerkleRoot: str
    utxoCommitment: str
    timestamp: int
    bits: int
    nonce: int
    daaScore: int
    blueWork: str
    pruningPoint: str
    blueScore: int
    def __init__(
        self,
        version: _Optional[int] = ...,
        parents: _Optional[_Iterable[_Union[RpcBlockLevelParents, _Mapping]]] = ...,
        hashMerkleRoot: _Optional[str] = ...,
        acceptedIdMerkleRoot: _Optional[str] = ...,
        utxoCommitment: _Optional[str] = ...,
        timestamp: _Optional[int] = ...,
        bits: _Optional[int] = ...,
        nonce: _Optional[int] = ...,
        daaScore: _Optional[int] = ...,
        blueWork: _Optional[str] = ...,
        pruningPoint: _Optional[str] = ...,
        blueScore: _Optional[int] = ...,
    ) -> None: ...

class RpcBlockLevelParents(_message.Message):
    __slots__ = ("parentHashes",)
    PARENTHASHES_FIELD_NUMBER: _ClassVar[int]
    parentHashes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parentHashes: _Optional[_Iterable[str]] = ...) -> None: ...

class RpcBlockVerboseData(_message.Message):
    __slots__ = (
        "hash",
        "difficulty",
        "selectedParentHash",
        "transactionIds",
        "isHeaderOnly",
        "blueScore",
        "childrenHashes",
        "mergeSetBluesHashes",
        "mergeSetRedsHashes",
        "isChainBlock",
    )
    HASH_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    SELECTEDPARENTHASH_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONIDS_FIELD_NUMBER: _ClassVar[int]
    ISHEADERONLY_FIELD_NUMBER: _ClassVar[int]
    BLUESCORE_FIELD_NUMBER: _ClassVar[int]
    CHILDRENHASHES_FIELD_NUMBER: _ClassVar[int]
    MERGESETBLUESHASHES_FIELD_NUMBER: _ClassVar[int]
    MERGESETREDSHASHES_FIELD_NUMBER: _ClassVar[int]
    ISCHAINBLOCK_FIELD_NUMBER: _ClassVar[int]
    hash: str
    difficulty: float
    selectedParentHash: str
    transactionIds: _containers.RepeatedScalarFieldContainer[str]
    isHeaderOnly: bool
    blueScore: int
    childrenHashes: _containers.RepeatedScalarFieldContainer[str]
    mergeSetBluesHashes: _containers.RepeatedScalarFieldContainer[str]
    mergeSetRedsHashes: _containers.RepeatedScalarFieldContainer[str]
    isChainBlock: bool
    def __init__(
        self,
        hash: _Optional[str] = ...,
        difficulty: _Optional[float] = ...,
        selectedParentHash: _Optional[str] = ...,
        transactionIds: _Optional[_Iterable[str]] = ...,
        isHeaderOnly: bool = ...,
        blueScore: _Optional[int] = ...,
        childrenHashes: _Optional[_Iterable[str]] = ...,
        mergeSetBluesHashes: _Optional[_Iterable[str]] = ...,
        mergeSetRedsHashes: _Optional[_Iterable[str]] = ...,
        isChainBlock: bool = ...,
    ) -> None: ...

class RpcTransaction(_message.Message):
    __slots__ = (
        "version",
        "inputs",
        "outputs",
        "lockTime",
        "subnetworkId",
        "gas",
        "payload",
        "verboseData",
        "mass",
    )
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    LOCKTIME_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORKID_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERBOSEDATA_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    version: int
    inputs: _containers.RepeatedCompositeFieldContainer[RpcTransactionInput]
    outputs: _containers.RepeatedCompositeFieldContainer[RpcTransactionOutput]
    lockTime: int
    subnetworkId: str
    gas: int
    payload: str
    verboseData: RpcTransactionVerboseData
    mass: int
    def __init__(
        self,
        version: _Optional[int] = ...,
        inputs: _Optional[_Iterable[_Union[RpcTransactionInput, _Mapping]]] = ...,
        outputs: _Optional[_Iterable[_Union[RpcTransactionOutput, _Mapping]]] = ...,
        lockTime: _Optional[int] = ...,
        subnetworkId: _Optional[str] = ...,
        gas: _Optional[int] = ...,
        payload: _Optional[str] = ...,
        verboseData: _Optional[_Union[RpcTransactionVerboseData, _Mapping]] = ...,
        mass: _Optional[int] = ...,
    ) -> None: ...

class RpcTransactionInput(_message.Message):
    __slots__ = ("previousOutpoint", "signatureScript", "sequence", "sigOpCount", "verboseData")
    PREVIOUSOUTPOINT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURESCRIPT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SIGOPCOUNT_FIELD_NUMBER: _ClassVar[int]
    VERBOSEDATA_FIELD_NUMBER: _ClassVar[int]
    previousOutpoint: RpcOutpoint
    signatureScript: str
    sequence: int
    sigOpCount: int
    verboseData: RpcTransactionInputVerboseData
    def __init__(
        self,
        previousOutpoint: _Optional[_Union[RpcOutpoint, _Mapping]] = ...,
        signatureScript: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        sigOpCount: _Optional[int] = ...,
        verboseData: _Optional[_Union[RpcTransactionInputVerboseData, _Mapping]] = ...,
    ) -> None: ...

class RpcScriptPublicKey(_message.Message):
    __slots__ = ("version", "scriptPublicKey")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRIPTPUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    version: int
    scriptPublicKey: str
    def __init__(
        self, version: _Optional[int] = ..., scriptPublicKey: _Optional[str] = ...
    ) -> None: ...

class RpcTransactionOutput(_message.Message):
    __slots__ = ("amount", "scriptPublicKey", "verboseData")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SCRIPTPUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    VERBOSEDATA_FIELD_NUMBER: _ClassVar[int]
    amount: int
    scriptPublicKey: RpcScriptPublicKey
    verboseData: RpcTransactionOutputVerboseData
    def __init__(
        self,
        amount: _Optional[int] = ...,
        scriptPublicKey: _Optional[_Union[RpcScriptPublicKey, _Mapping]] = ...,
        verboseData: _Optional[_Union[RpcTransactionOutputVerboseData, _Mapping]] = ...,
    ) -> None: ...

class RpcOutpoint(_message.Message):
    __slots__ = ("transactionId", "index")
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    transactionId: str
    index: int
    def __init__(
        self, transactionId: _Optional[str] = ..., index: _Optional[int] = ...
    ) -> None: ...

class RpcUtxoEntry(_message.Message):
    __slots__ = ("amount", "scriptPublicKey", "blockDaaScore", "isCoinbase")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SCRIPTPUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    BLOCKDAASCORE_FIELD_NUMBER: _ClassVar[int]
    ISCOINBASE_FIELD_NUMBER: _ClassVar[int]
    amount: int
    scriptPublicKey: RpcScriptPublicKey
    blockDaaScore: int
    isCoinbase: bool
    def __init__(
        self,
        amount: _Optional[int] = ...,
        scriptPublicKey: _Optional[_Union[RpcScriptPublicKey, _Mapping]] = ...,
        blockDaaScore: _Optional[int] = ...,
        isCoinbase: bool = ...,
    ) -> None: ...

class RpcTransactionVerboseData(_message.Message):
    __slots__ = ("transactionId", "hash", "computeMass", "blockHash", "blockTime")
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    COMPUTEMASS_FIELD_NUMBER: _ClassVar[int]
    BLOCKHASH_FIELD_NUMBER: _ClassVar[int]
    BLOCKTIME_FIELD_NUMBER: _ClassVar[int]
    transactionId: str
    hash: str
    computeMass: int
    blockHash: str
    blockTime: int
    def __init__(
        self,
        transactionId: _Optional[str] = ...,
        hash: _Optional[str] = ...,
        computeMass: _Optional[int] = ...,
        blockHash: _Optional[str] = ...,
        blockTime: _Optional[int] = ...,
    ) -> None: ...

class RpcTransactionInputVerboseData(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RpcTransactionOutputVerboseData(_message.Message):
    __slots__ = ("scriptPublicKeyType", "scriptPublicKeyAddress")
    SCRIPTPUBLICKEYTYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIPTPUBLICKEYADDRESS_FIELD_NUMBER: _ClassVar[int]
    scriptPublicKeyType: str
    scriptPublicKeyAddress: str
    def __init__(
        self,
        scriptPublicKeyType: _Optional[str] = ...,
        scriptPublicKeyAddress: _Optional[str] = ...,
    ) -> None: ...

class GetCurrentNetworkRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentNetworkResponseMessage(_message.Message):
    __slots__ = ("currentNetwork", "error")
    CURRENTNETWORK_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    currentNetwork: str
    error: RPCError
    def __init__(
        self,
        currentNetwork: _Optional[str] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class SubmitBlockRequestMessage(_message.Message):
    __slots__ = ("block", "allowNonDAABlocks")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    ALLOWNONDAABLOCKS_FIELD_NUMBER: _ClassVar[int]
    block: RpcBlock
    allowNonDAABlocks: bool
    def __init__(
        self, block: _Optional[_Union[RpcBlock, _Mapping]] = ..., allowNonDAABlocks: bool = ...
    ) -> None: ...

class SubmitBlockResponseMessage(_message.Message):
    __slots__ = ("rejectReason", "error")

    class RejectReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SubmitBlockResponseMessage.RejectReason]
        BLOCK_INVALID: _ClassVar[SubmitBlockResponseMessage.RejectReason]
        IS_IN_IBD: _ClassVar[SubmitBlockResponseMessage.RejectReason]

    NONE: SubmitBlockResponseMessage.RejectReason
    BLOCK_INVALID: SubmitBlockResponseMessage.RejectReason
    IS_IN_IBD: SubmitBlockResponseMessage.RejectReason
    REJECTREASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    rejectReason: SubmitBlockResponseMessage.RejectReason
    error: RPCError
    def __init__(
        self,
        rejectReason: _Optional[_Union[SubmitBlockResponseMessage.RejectReason, str]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetBlockTemplateRequestMessage(_message.Message):
    __slots__ = ("payAddress", "extraData")
    PAYADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTRADATA_FIELD_NUMBER: _ClassVar[int]
    payAddress: str
    extraData: str
    def __init__(
        self, payAddress: _Optional[str] = ..., extraData: _Optional[str] = ...
    ) -> None: ...

class GetBlockTemplateResponseMessage(_message.Message):
    __slots__ = ("block", "isSynced", "error")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    ISSYNCED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    block: RpcBlock
    isSynced: bool
    error: RPCError
    def __init__(
        self,
        block: _Optional[_Union[RpcBlock, _Mapping]] = ...,
        isSynced: bool = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class NotifyBlockAddedRequestMessage(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: RpcNotifyCommand
    def __init__(self, command: _Optional[_Union[RpcNotifyCommand, str]] = ...) -> None: ...

class NotifyBlockAddedResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class BlockAddedNotificationMessage(_message.Message):
    __slots__ = ("block",)
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: RpcBlock
    def __init__(self, block: _Optional[_Union[RpcBlock, _Mapping]] = ...) -> None: ...

class GetPeerAddressesRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPeerAddressesResponseMessage(_message.Message):
    __slots__ = ("addresses", "bannedAddresses", "error")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    BANNEDADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[GetPeerAddressesKnownAddressMessage]
    bannedAddresses: _containers.RepeatedCompositeFieldContainer[
        GetPeerAddressesKnownAddressMessage
    ]
    error: RPCError
    def __init__(
        self,
        addresses: _Optional[
            _Iterable[_Union[GetPeerAddressesKnownAddressMessage, _Mapping]]
        ] = ...,
        bannedAddresses: _Optional[
            _Iterable[_Union[GetPeerAddressesKnownAddressMessage, _Mapping]]
        ] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetPeerAddressesKnownAddressMessage(_message.Message):
    __slots__ = ("Addr",)
    ADDR_FIELD_NUMBER: _ClassVar[int]
    Addr: str
    def __init__(self, Addr: _Optional[str] = ...) -> None: ...

class GetSinkRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSinkResponseMessage(_message.Message):
    __slots__ = ("sink", "error")
    SINK_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sink: str
    error: RPCError
    def __init__(
        self, sink: _Optional[str] = ..., error: _Optional[_Union[RPCError, _Mapping]] = ...
    ) -> None: ...

class GetMempoolEntryRequestMessage(_message.Message):
    __slots__ = ("txId", "includeOrphanPool", "filterTransactionPool")
    TXID_FIELD_NUMBER: _ClassVar[int]
    INCLUDEORPHANPOOL_FIELD_NUMBER: _ClassVar[int]
    FILTERTRANSACTIONPOOL_FIELD_NUMBER: _ClassVar[int]
    txId: str
    includeOrphanPool: bool
    filterTransactionPool: bool
    def __init__(
        self,
        txId: _Optional[str] = ...,
        includeOrphanPool: bool = ...,
        filterTransactionPool: bool = ...,
    ) -> None: ...

class GetMempoolEntryResponseMessage(_message.Message):
    __slots__ = ("entry", "error")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entry: RpcMempoolEntry
    error: RPCError
    def __init__(
        self,
        entry: _Optional[_Union[RpcMempoolEntry, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetMempoolEntriesRequestMessage(_message.Message):
    __slots__ = ("includeOrphanPool", "filterTransactionPool")
    INCLUDEORPHANPOOL_FIELD_NUMBER: _ClassVar[int]
    FILTERTRANSACTIONPOOL_FIELD_NUMBER: _ClassVar[int]
    includeOrphanPool: bool
    filterTransactionPool: bool
    def __init__(
        self, includeOrphanPool: bool = ..., filterTransactionPool: bool = ...
    ) -> None: ...

class GetMempoolEntriesResponseMessage(_message.Message):
    __slots__ = ("entries", "error")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RpcMempoolEntry]
    error: RPCError
    def __init__(
        self,
        entries: _Optional[_Iterable[_Union[RpcMempoolEntry, _Mapping]]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class RpcMempoolEntry(_message.Message):
    __slots__ = ("fee", "transaction", "isOrphan")
    FEE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    ISORPHAN_FIELD_NUMBER: _ClassVar[int]
    fee: int
    transaction: RpcTransaction
    isOrphan: bool
    def __init__(
        self,
        fee: _Optional[int] = ...,
        transaction: _Optional[_Union[RpcTransaction, _Mapping]] = ...,
        isOrphan: bool = ...,
    ) -> None: ...

class GetConnectedPeerInfoRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConnectedPeerInfoResponseMessage(_message.Message):
    __slots__ = ("infos", "error")
    INFOS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[GetConnectedPeerInfoMessage]
    error: RPCError
    def __init__(
        self,
        infos: _Optional[_Iterable[_Union[GetConnectedPeerInfoMessage, _Mapping]]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetConnectedPeerInfoMessage(_message.Message):
    __slots__ = (
        "id",
        "address",
        "lastPingDuration",
        "isOutbound",
        "timeOffset",
        "userAgent",
        "advertisedProtocolVersion",
        "timeConnected",
        "isIbdPeer",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LASTPINGDURATION_FIELD_NUMBER: _ClassVar[int]
    ISOUTBOUND_FIELD_NUMBER: _ClassVar[int]
    TIMEOFFSET_FIELD_NUMBER: _ClassVar[int]
    USERAGENT_FIELD_NUMBER: _ClassVar[int]
    ADVERTISEDPROTOCOLVERSION_FIELD_NUMBER: _ClassVar[int]
    TIMECONNECTED_FIELD_NUMBER: _ClassVar[int]
    ISIBDPEER_FIELD_NUMBER: _ClassVar[int]
    id: str
    address: str
    lastPingDuration: int
    isOutbound: bool
    timeOffset: int
    userAgent: str
    advertisedProtocolVersion: int
    timeConnected: int
    isIbdPeer: bool
    def __init__(
        self,
        id: _Optional[str] = ...,
        address: _Optional[str] = ...,
        lastPingDuration: _Optional[int] = ...,
        isOutbound: bool = ...,
        timeOffset: _Optional[int] = ...,
        userAgent: _Optional[str] = ...,
        advertisedProtocolVersion: _Optional[int] = ...,
        timeConnected: _Optional[int] = ...,
        isIbdPeer: bool = ...,
    ) -> None: ...

class AddPeerRequestMessage(_message.Message):
    __slots__ = ("address", "isPermanent")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ISPERMANENT_FIELD_NUMBER: _ClassVar[int]
    address: str
    isPermanent: bool
    def __init__(self, address: _Optional[str] = ..., isPermanent: bool = ...) -> None: ...

class AddPeerResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class SubmitTransactionRequestMessage(_message.Message):
    __slots__ = ("transaction", "allowOrphan")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWORPHAN_FIELD_NUMBER: _ClassVar[int]
    transaction: RpcTransaction
    allowOrphan: bool
    def __init__(
        self,
        transaction: _Optional[_Union[RpcTransaction, _Mapping]] = ...,
        allowOrphan: bool = ...,
    ) -> None: ...

class SubmitTransactionResponseMessage(_message.Message):
    __slots__ = ("transactionId", "error")
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transactionId: str
    error: RPCError
    def __init__(
        self,
        transactionId: _Optional[str] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class SubmitTransactionReplacementRequestMessage(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: RpcTransaction
    def __init__(self, transaction: _Optional[_Union[RpcTransaction, _Mapping]] = ...) -> None: ...

class SubmitTransactionReplacementResponseMessage(_message.Message):
    __slots__ = ("transactionId", "replacedTransaction", "error")
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    REPLACEDTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transactionId: str
    replacedTransaction: RpcTransaction
    error: RPCError
    def __init__(
        self,
        transactionId: _Optional[str] = ...,
        replacedTransaction: _Optional[_Union[RpcTransaction, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class NotifyVirtualChainChangedRequestMessage(_message.Message):
    __slots__ = ("includeAcceptedTransactionIds", "command")
    INCLUDEACCEPTEDTRANSACTIONIDS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    includeAcceptedTransactionIds: bool
    command: RpcNotifyCommand
    def __init__(
        self,
        includeAcceptedTransactionIds: bool = ...,
        command: _Optional[_Union[RpcNotifyCommand, str]] = ...,
    ) -> None: ...

class NotifyVirtualChainChangedResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class VirtualChainChangedNotificationMessage(_message.Message):
    __slots__ = ("removedChainBlockHashes", "addedChainBlockHashes", "acceptedTransactionIds")
    REMOVEDCHAINBLOCKHASHES_FIELD_NUMBER: _ClassVar[int]
    ADDEDCHAINBLOCKHASHES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTEDTRANSACTIONIDS_FIELD_NUMBER: _ClassVar[int]
    removedChainBlockHashes: _containers.RepeatedScalarFieldContainer[str]
    addedChainBlockHashes: _containers.RepeatedScalarFieldContainer[str]
    acceptedTransactionIds: _containers.RepeatedCompositeFieldContainer[RpcAcceptedTransactionIds]
    def __init__(
        self,
        removedChainBlockHashes: _Optional[_Iterable[str]] = ...,
        addedChainBlockHashes: _Optional[_Iterable[str]] = ...,
        acceptedTransactionIds: _Optional[
            _Iterable[_Union[RpcAcceptedTransactionIds, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetBlockRequestMessage(_message.Message):
    __slots__ = ("hash", "includeTransactions")
    HASH_FIELD_NUMBER: _ClassVar[int]
    INCLUDETRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    hash: str
    includeTransactions: bool
    def __init__(self, hash: _Optional[str] = ..., includeTransactions: bool = ...) -> None: ...

class GetBlockResponseMessage(_message.Message):
    __slots__ = ("block", "error")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    block: RpcBlock
    error: RPCError
    def __init__(
        self,
        block: _Optional[_Union[RpcBlock, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetSubnetworkRequestMessage(_message.Message):
    __slots__ = ("subnetworkId",)
    SUBNETWORKID_FIELD_NUMBER: _ClassVar[int]
    subnetworkId: str
    def __init__(self, subnetworkId: _Optional[str] = ...) -> None: ...

class GetSubnetworkResponseMessage(_message.Message):
    __slots__ = ("gasLimit", "error")
    GASLIMIT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    gasLimit: int
    error: RPCError
    def __init__(
        self, gasLimit: _Optional[int] = ..., error: _Optional[_Union[RPCError, _Mapping]] = ...
    ) -> None: ...

class GetVirtualChainFromBlockRequestMessage(_message.Message):
    __slots__ = ("startHash", "includeAcceptedTransactionIds", "minConfirmationCount")
    STARTHASH_FIELD_NUMBER: _ClassVar[int]
    INCLUDEACCEPTEDTRANSACTIONIDS_FIELD_NUMBER: _ClassVar[int]
    MINCONFIRMATIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    startHash: str
    includeAcceptedTransactionIds: bool
    minConfirmationCount: int
    def __init__(
        self,
        startHash: _Optional[str] = ...,
        includeAcceptedTransactionIds: bool = ...,
        minConfirmationCount: _Optional[int] = ...,
    ) -> None: ...

class RpcAcceptedTransactionIds(_message.Message):
    __slots__ = ("acceptingBlockHash", "acceptedTransactionIds")
    ACCEPTINGBLOCKHASH_FIELD_NUMBER: _ClassVar[int]
    ACCEPTEDTRANSACTIONIDS_FIELD_NUMBER: _ClassVar[int]
    acceptingBlockHash: str
    acceptedTransactionIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        acceptingBlockHash: _Optional[str] = ...,
        acceptedTransactionIds: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class GetVirtualChainFromBlockResponseMessage(_message.Message):
    __slots__ = (
        "removedChainBlockHashes",
        "addedChainBlockHashes",
        "acceptedTransactionIds",
        "error",
    )
    REMOVEDCHAINBLOCKHASHES_FIELD_NUMBER: _ClassVar[int]
    ADDEDCHAINBLOCKHASHES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTEDTRANSACTIONIDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    removedChainBlockHashes: _containers.RepeatedScalarFieldContainer[str]
    addedChainBlockHashes: _containers.RepeatedScalarFieldContainer[str]
    acceptedTransactionIds: _containers.RepeatedCompositeFieldContainer[RpcAcceptedTransactionIds]
    error: RPCError
    def __init__(
        self,
        removedChainBlockHashes: _Optional[_Iterable[str]] = ...,
        addedChainBlockHashes: _Optional[_Iterable[str]] = ...,
        acceptedTransactionIds: _Optional[
            _Iterable[_Union[RpcAcceptedTransactionIds, _Mapping]]
        ] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetBlocksRequestMessage(_message.Message):
    __slots__ = ("lowHash", "includeBlocks", "includeTransactions")
    LOWHASH_FIELD_NUMBER: _ClassVar[int]
    INCLUDEBLOCKS_FIELD_NUMBER: _ClassVar[int]
    INCLUDETRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    lowHash: str
    includeBlocks: bool
    includeTransactions: bool
    def __init__(
        self,
        lowHash: _Optional[str] = ...,
        includeBlocks: bool = ...,
        includeTransactions: bool = ...,
    ) -> None: ...

class GetBlocksResponseMessage(_message.Message):
    __slots__ = ("blockHashes", "blocks", "error")
    BLOCKHASHES_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    blockHashes: _containers.RepeatedScalarFieldContainer[str]
    blocks: _containers.RepeatedCompositeFieldContainer[RpcBlock]
    error: RPCError
    def __init__(
        self,
        blockHashes: _Optional[_Iterable[str]] = ...,
        blocks: _Optional[_Iterable[_Union[RpcBlock, _Mapping]]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetBlockCountRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBlockCountResponseMessage(_message.Message):
    __slots__ = ("blockCount", "headerCount", "error")
    BLOCKCOUNT_FIELD_NUMBER: _ClassVar[int]
    HEADERCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    blockCount: int
    headerCount: int
    error: RPCError
    def __init__(
        self,
        blockCount: _Optional[int] = ...,
        headerCount: _Optional[int] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetBlockDagInfoRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBlockDagInfoResponseMessage(_message.Message):
    __slots__ = (
        "networkName",
        "blockCount",
        "headerCount",
        "tipHashes",
        "difficulty",
        "pastMedianTime",
        "virtualParentHashes",
        "pruningPointHash",
        "virtualDaaScore",
        "sink",
        "error",
    )
    NETWORKNAME_FIELD_NUMBER: _ClassVar[int]
    BLOCKCOUNT_FIELD_NUMBER: _ClassVar[int]
    HEADERCOUNT_FIELD_NUMBER: _ClassVar[int]
    TIPHASHES_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    PASTMEDIANTIME_FIELD_NUMBER: _ClassVar[int]
    VIRTUALPARENTHASHES_FIELD_NUMBER: _ClassVar[int]
    PRUNINGPOINTHASH_FIELD_NUMBER: _ClassVar[int]
    VIRTUALDAASCORE_FIELD_NUMBER: _ClassVar[int]
    SINK_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    networkName: str
    blockCount: int
    headerCount: int
    tipHashes: _containers.RepeatedScalarFieldContainer[str]
    difficulty: float
    pastMedianTime: int
    virtualParentHashes: _containers.RepeatedScalarFieldContainer[str]
    pruningPointHash: str
    virtualDaaScore: int
    sink: str
    error: RPCError
    def __init__(
        self,
        networkName: _Optional[str] = ...,
        blockCount: _Optional[int] = ...,
        headerCount: _Optional[int] = ...,
        tipHashes: _Optional[_Iterable[str]] = ...,
        difficulty: _Optional[float] = ...,
        pastMedianTime: _Optional[int] = ...,
        virtualParentHashes: _Optional[_Iterable[str]] = ...,
        pruningPointHash: _Optional[str] = ...,
        virtualDaaScore: _Optional[int] = ...,
        sink: _Optional[str] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class ResolveFinalityConflictRequestMessage(_message.Message):
    __slots__ = ("finalityBlockHash",)
    FINALITYBLOCKHASH_FIELD_NUMBER: _ClassVar[int]
    finalityBlockHash: str
    def __init__(self, finalityBlockHash: _Optional[str] = ...) -> None: ...

class ResolveFinalityConflictResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class NotifyFinalityConflictRequestMessage(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: RpcNotifyCommand
    def __init__(self, command: _Optional[_Union[RpcNotifyCommand, str]] = ...) -> None: ...

class NotifyFinalityConflictResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class FinalityConflictNotificationMessage(_message.Message):
    __slots__ = ("violatingBlockHash",)
    VIOLATINGBLOCKHASH_FIELD_NUMBER: _ClassVar[int]
    violatingBlockHash: str
    def __init__(self, violatingBlockHash: _Optional[str] = ...) -> None: ...

class FinalityConflictResolvedNotificationMessage(_message.Message):
    __slots__ = ("finalityBlockHash",)
    FINALITYBLOCKHASH_FIELD_NUMBER: _ClassVar[int]
    finalityBlockHash: str
    def __init__(self, finalityBlockHash: _Optional[str] = ...) -> None: ...

class ShutdownRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShutdownResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class GetHeadersRequestMessage(_message.Message):
    __slots__ = ("startHash", "limit", "isAscending")
    STARTHASH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ISASCENDING_FIELD_NUMBER: _ClassVar[int]
    startHash: str
    limit: int
    isAscending: bool
    def __init__(
        self, startHash: _Optional[str] = ..., limit: _Optional[int] = ..., isAscending: bool = ...
    ) -> None: ...

class GetHeadersResponseMessage(_message.Message):
    __slots__ = ("headers", "error")
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    headers: _containers.RepeatedScalarFieldContainer[str]
    error: RPCError
    def __init__(
        self,
        headers: _Optional[_Iterable[str]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class NotifyUtxosChangedRequestMessage(_message.Message):
    __slots__ = ("addresses", "command")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    command: RpcNotifyCommand
    def __init__(
        self,
        addresses: _Optional[_Iterable[str]] = ...,
        command: _Optional[_Union[RpcNotifyCommand, str]] = ...,
    ) -> None: ...

class NotifyUtxosChangedResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class UtxosChangedNotificationMessage(_message.Message):
    __slots__ = ("added", "removed")
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    added: _containers.RepeatedCompositeFieldContainer[RpcUtxosByAddressesEntry]
    removed: _containers.RepeatedCompositeFieldContainer[RpcUtxosByAddressesEntry]
    def __init__(
        self,
        added: _Optional[_Iterable[_Union[RpcUtxosByAddressesEntry, _Mapping]]] = ...,
        removed: _Optional[_Iterable[_Union[RpcUtxosByAddressesEntry, _Mapping]]] = ...,
    ) -> None: ...

class RpcUtxosByAddressesEntry(_message.Message):
    __slots__ = ("address", "outpoint", "utxoEntry")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OUTPOINT_FIELD_NUMBER: _ClassVar[int]
    UTXOENTRY_FIELD_NUMBER: _ClassVar[int]
    address: str
    outpoint: RpcOutpoint
    utxoEntry: RpcUtxoEntry
    def __init__(
        self,
        address: _Optional[str] = ...,
        outpoint: _Optional[_Union[RpcOutpoint, _Mapping]] = ...,
        utxoEntry: _Optional[_Union[RpcUtxoEntry, _Mapping]] = ...,
    ) -> None: ...

class StopNotifyingUtxosChangedRequestMessage(_message.Message):
    __slots__ = ("addresses",)
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class StopNotifyingUtxosChangedResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class GetUtxosByAddressesRequestMessage(_message.Message):
    __slots__ = ("addresses",)
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUtxosByAddressesResponseMessage(_message.Message):
    __slots__ = ("entries", "error")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RpcUtxosByAddressesEntry]
    error: RPCError
    def __init__(
        self,
        entries: _Optional[_Iterable[_Union[RpcUtxosByAddressesEntry, _Mapping]]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetBalanceByAddressRequestMessage(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class GetBalanceByAddressResponseMessage(_message.Message):
    __slots__ = ("balance", "error")
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    balance: int
    error: RPCError
    def __init__(
        self, balance: _Optional[int] = ..., error: _Optional[_Union[RPCError, _Mapping]] = ...
    ) -> None: ...

class GetBalancesByAddressesRequestMessage(_message.Message):
    __slots__ = ("addresses",)
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class RpcBalancesByAddressesEntry(_message.Message):
    __slots__ = ("address", "balance", "error")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    address: str
    balance: int
    error: RPCError
    def __init__(
        self,
        address: _Optional[str] = ...,
        balance: _Optional[int] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetBalancesByAddressesResponseMessage(_message.Message):
    __slots__ = ("entries", "error")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RpcBalancesByAddressesEntry]
    error: RPCError
    def __init__(
        self,
        entries: _Optional[_Iterable[_Union[RpcBalancesByAddressesEntry, _Mapping]]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetSinkBlueScoreRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSinkBlueScoreResponseMessage(_message.Message):
    __slots__ = ("blueScore", "error")
    BLUESCORE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    blueScore: int
    error: RPCError
    def __init__(
        self, blueScore: _Optional[int] = ..., error: _Optional[_Union[RPCError, _Mapping]] = ...
    ) -> None: ...

class NotifySinkBlueScoreChangedRequestMessage(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: RpcNotifyCommand
    def __init__(self, command: _Optional[_Union[RpcNotifyCommand, str]] = ...) -> None: ...

class NotifySinkBlueScoreChangedResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class SinkBlueScoreChangedNotificationMessage(_message.Message):
    __slots__ = ("sinkBlueScore",)
    SINKBLUESCORE_FIELD_NUMBER: _ClassVar[int]
    sinkBlueScore: int
    def __init__(self, sinkBlueScore: _Optional[int] = ...) -> None: ...

class NotifyVirtualDaaScoreChangedRequestMessage(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: RpcNotifyCommand
    def __init__(self, command: _Optional[_Union[RpcNotifyCommand, str]] = ...) -> None: ...

class NotifyVirtualDaaScoreChangedResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class VirtualDaaScoreChangedNotificationMessage(_message.Message):
    __slots__ = ("virtualDaaScore",)
    VIRTUALDAASCORE_FIELD_NUMBER: _ClassVar[int]
    virtualDaaScore: int
    def __init__(self, virtualDaaScore: _Optional[int] = ...) -> None: ...

class NotifyPruningPointUtxoSetOverrideRequestMessage(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: RpcNotifyCommand
    def __init__(self, command: _Optional[_Union[RpcNotifyCommand, str]] = ...) -> None: ...

class NotifyPruningPointUtxoSetOverrideResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class PruningPointUtxoSetOverrideNotificationMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopNotifyingPruningPointUtxoSetOverrideRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopNotifyingPruningPointUtxoSetOverrideResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class BanRequestMessage(_message.Message):
    __slots__ = ("ip",)
    IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    def __init__(self, ip: _Optional[str] = ...) -> None: ...

class BanResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class UnbanRequestMessage(_message.Message):
    __slots__ = ("ip",)
    IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    def __init__(self, ip: _Optional[str] = ...) -> None: ...

class UnbanResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class GetInfoRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInfoResponseMessage(_message.Message):
    __slots__ = (
        "p2pId",
        "mempoolSize",
        "serverVersion",
        "isUtxoIndexed",
        "isSynced",
        "hasNotifyCommand",
        "hasMessageId",
        "error",
    )
    P2PID_FIELD_NUMBER: _ClassVar[int]
    MEMPOOLSIZE_FIELD_NUMBER: _ClassVar[int]
    SERVERVERSION_FIELD_NUMBER: _ClassVar[int]
    ISUTXOINDEXED_FIELD_NUMBER: _ClassVar[int]
    ISSYNCED_FIELD_NUMBER: _ClassVar[int]
    HASNOTIFYCOMMAND_FIELD_NUMBER: _ClassVar[int]
    HASMESSAGEID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    p2pId: str
    mempoolSize: int
    serverVersion: str
    isUtxoIndexed: bool
    isSynced: bool
    hasNotifyCommand: bool
    hasMessageId: bool
    error: RPCError
    def __init__(
        self,
        p2pId: _Optional[str] = ...,
        mempoolSize: _Optional[int] = ...,
        serverVersion: _Optional[str] = ...,
        isUtxoIndexed: bool = ...,
        isSynced: bool = ...,
        hasNotifyCommand: bool = ...,
        hasMessageId: bool = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class EstimateNetworkHashesPerSecondRequestMessage(_message.Message):
    __slots__ = ("windowSize", "startHash")
    WINDOWSIZE_FIELD_NUMBER: _ClassVar[int]
    STARTHASH_FIELD_NUMBER: _ClassVar[int]
    windowSize: int
    startHash: str
    def __init__(
        self, windowSize: _Optional[int] = ..., startHash: _Optional[str] = ...
    ) -> None: ...

class EstimateNetworkHashesPerSecondResponseMessage(_message.Message):
    __slots__ = ("networkHashesPerSecond", "error")
    NETWORKHASHESPERSECOND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    networkHashesPerSecond: int
    error: RPCError
    def __init__(
        self,
        networkHashesPerSecond: _Optional[int] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class NotifyNewBlockTemplateRequestMessage(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: RpcNotifyCommand
    def __init__(self, command: _Optional[_Union[RpcNotifyCommand, str]] = ...) -> None: ...

class NotifyNewBlockTemplateResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class NewBlockTemplateNotificationMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RpcMempoolEntryByAddress(_message.Message):
    __slots__ = ("address", "sending", "receiving")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SENDING_FIELD_NUMBER: _ClassVar[int]
    RECEIVING_FIELD_NUMBER: _ClassVar[int]
    address: str
    sending: _containers.RepeatedCompositeFieldContainer[RpcMempoolEntry]
    receiving: _containers.RepeatedCompositeFieldContainer[RpcMempoolEntry]
    def __init__(
        self,
        address: _Optional[str] = ...,
        sending: _Optional[_Iterable[_Union[RpcMempoolEntry, _Mapping]]] = ...,
        receiving: _Optional[_Iterable[_Union[RpcMempoolEntry, _Mapping]]] = ...,
    ) -> None: ...

class GetMempoolEntriesByAddressesRequestMessage(_message.Message):
    __slots__ = ("addresses", "includeOrphanPool", "filterTransactionPool")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    INCLUDEORPHANPOOL_FIELD_NUMBER: _ClassVar[int]
    FILTERTRANSACTIONPOOL_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    includeOrphanPool: bool
    filterTransactionPool: bool
    def __init__(
        self,
        addresses: _Optional[_Iterable[str]] = ...,
        includeOrphanPool: bool = ...,
        filterTransactionPool: bool = ...,
    ) -> None: ...

class GetMempoolEntriesByAddressesResponseMessage(_message.Message):
    __slots__ = ("entries", "error")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RpcMempoolEntryByAddress]
    error: RPCError
    def __init__(
        self,
        entries: _Optional[_Iterable[_Union[RpcMempoolEntryByAddress, _Mapping]]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetCoinSupplyRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCoinSupplyResponseMessage(_message.Message):
    __slots__ = ("maxSompi", "circulatingSompi", "error")
    MAXSOMPI_FIELD_NUMBER: _ClassVar[int]
    CIRCULATINGSOMPI_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    maxSompi: int
    circulatingSompi: int
    error: RPCError
    def __init__(
        self,
        maxSompi: _Optional[int] = ...,
        circulatingSompi: _Optional[int] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class PingRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponseMessage(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: RPCError
    def __init__(self, error: _Optional[_Union[RPCError, _Mapping]] = ...) -> None: ...

class ProcessMetrics(_message.Message):
    __slots__ = (
        "residentSetSize",
        "virtualMemorySize",
        "coreNum",
        "cpuUsage",
        "fdNum",
        "diskIoReadBytes",
        "diskIoWriteBytes",
        "diskIoReadPerSec",
        "diskIoWritePerSec",
    )
    RESIDENTSETSIZE_FIELD_NUMBER: _ClassVar[int]
    VIRTUALMEMORYSIZE_FIELD_NUMBER: _ClassVar[int]
    CORENUM_FIELD_NUMBER: _ClassVar[int]
    CPUUSAGE_FIELD_NUMBER: _ClassVar[int]
    FDNUM_FIELD_NUMBER: _ClassVar[int]
    DISKIOREADBYTES_FIELD_NUMBER: _ClassVar[int]
    DISKIOWRITEBYTES_FIELD_NUMBER: _ClassVar[int]
    DISKIOREADPERSEC_FIELD_NUMBER: _ClassVar[int]
    DISKIOWRITEPERSEC_FIELD_NUMBER: _ClassVar[int]
    residentSetSize: int
    virtualMemorySize: int
    coreNum: int
    cpuUsage: float
    fdNum: int
    diskIoReadBytes: int
    diskIoWriteBytes: int
    diskIoReadPerSec: float
    diskIoWritePerSec: float
    def __init__(
        self,
        residentSetSize: _Optional[int] = ...,
        virtualMemorySize: _Optional[int] = ...,
        coreNum: _Optional[int] = ...,
        cpuUsage: _Optional[float] = ...,
        fdNum: _Optional[int] = ...,
        diskIoReadBytes: _Optional[int] = ...,
        diskIoWriteBytes: _Optional[int] = ...,
        diskIoReadPerSec: _Optional[float] = ...,
        diskIoWritePerSec: _Optional[float] = ...,
    ) -> None: ...

class ConnectionMetrics(_message.Message):
    __slots__ = (
        "borshLiveConnections",
        "borshConnectionAttempts",
        "borshHandshakeFailures",
        "jsonLiveConnections",
        "jsonConnectionAttempts",
        "jsonHandshakeFailures",
        "activePeers",
    )
    BORSHLIVECONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    BORSHCONNECTIONATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    BORSHHANDSHAKEFAILURES_FIELD_NUMBER: _ClassVar[int]
    JSONLIVECONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    JSONCONNECTIONATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    JSONHANDSHAKEFAILURES_FIELD_NUMBER: _ClassVar[int]
    ACTIVEPEERS_FIELD_NUMBER: _ClassVar[int]
    borshLiveConnections: int
    borshConnectionAttempts: int
    borshHandshakeFailures: int
    jsonLiveConnections: int
    jsonConnectionAttempts: int
    jsonHandshakeFailures: int
    activePeers: int
    def __init__(
        self,
        borshLiveConnections: _Optional[int] = ...,
        borshConnectionAttempts: _Optional[int] = ...,
        borshHandshakeFailures: _Optional[int] = ...,
        jsonLiveConnections: _Optional[int] = ...,
        jsonConnectionAttempts: _Optional[int] = ...,
        jsonHandshakeFailures: _Optional[int] = ...,
        activePeers: _Optional[int] = ...,
    ) -> None: ...

class BandwidthMetrics(_message.Message):
    __slots__ = (
        "borshBytesTx",
        "borshBytesRx",
        "jsonBytesTx",
        "jsonBytesRx",
        "grpcP2pBytesTx",
        "grpcP2pBytesRx",
        "grpcUserBytesTx",
        "grpcUserBytesRx",
    )
    BORSHBYTESTX_FIELD_NUMBER: _ClassVar[int]
    BORSHBYTESRX_FIELD_NUMBER: _ClassVar[int]
    JSONBYTESTX_FIELD_NUMBER: _ClassVar[int]
    JSONBYTESRX_FIELD_NUMBER: _ClassVar[int]
    GRPCP2PBYTESTX_FIELD_NUMBER: _ClassVar[int]
    GRPCP2PBYTESRX_FIELD_NUMBER: _ClassVar[int]
    GRPCUSERBYTESTX_FIELD_NUMBER: _ClassVar[int]
    GRPCUSERBYTESRX_FIELD_NUMBER: _ClassVar[int]
    borshBytesTx: int
    borshBytesRx: int
    jsonBytesTx: int
    jsonBytesRx: int
    grpcP2pBytesTx: int
    grpcP2pBytesRx: int
    grpcUserBytesTx: int
    grpcUserBytesRx: int
    def __init__(
        self,
        borshBytesTx: _Optional[int] = ...,
        borshBytesRx: _Optional[int] = ...,
        jsonBytesTx: _Optional[int] = ...,
        jsonBytesRx: _Optional[int] = ...,
        grpcP2pBytesTx: _Optional[int] = ...,
        grpcP2pBytesRx: _Optional[int] = ...,
        grpcUserBytesTx: _Optional[int] = ...,
        grpcUserBytesRx: _Optional[int] = ...,
    ) -> None: ...

class ConsensusMetrics(_message.Message):
    __slots__ = (
        "blocksSubmitted",
        "headerCounts",
        "depCounts",
        "bodyCounts",
        "txsCounts",
        "chainBlockCounts",
        "massCounts",
        "blockCount",
        "headerCount",
        "mempoolSize",
        "tipHashesCount",
        "difficulty",
        "pastMedianTime",
        "virtualParentHashesCount",
        "virtualDaaScore",
    )
    BLOCKSSUBMITTED_FIELD_NUMBER: _ClassVar[int]
    HEADERCOUNTS_FIELD_NUMBER: _ClassVar[int]
    DEPCOUNTS_FIELD_NUMBER: _ClassVar[int]
    BODYCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TXSCOUNTS_FIELD_NUMBER: _ClassVar[int]
    CHAINBLOCKCOUNTS_FIELD_NUMBER: _ClassVar[int]
    MASSCOUNTS_FIELD_NUMBER: _ClassVar[int]
    BLOCKCOUNT_FIELD_NUMBER: _ClassVar[int]
    HEADERCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEMPOOLSIZE_FIELD_NUMBER: _ClassVar[int]
    TIPHASHESCOUNT_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    PASTMEDIANTIME_FIELD_NUMBER: _ClassVar[int]
    VIRTUALPARENTHASHESCOUNT_FIELD_NUMBER: _ClassVar[int]
    VIRTUALDAASCORE_FIELD_NUMBER: _ClassVar[int]
    blocksSubmitted: int
    headerCounts: int
    depCounts: int
    bodyCounts: int
    txsCounts: int
    chainBlockCounts: int
    massCounts: int
    blockCount: int
    headerCount: int
    mempoolSize: int
    tipHashesCount: int
    difficulty: float
    pastMedianTime: int
    virtualParentHashesCount: int
    virtualDaaScore: int
    def __init__(
        self,
        blocksSubmitted: _Optional[int] = ...,
        headerCounts: _Optional[int] = ...,
        depCounts: _Optional[int] = ...,
        bodyCounts: _Optional[int] = ...,
        txsCounts: _Optional[int] = ...,
        chainBlockCounts: _Optional[int] = ...,
        massCounts: _Optional[int] = ...,
        blockCount: _Optional[int] = ...,
        headerCount: _Optional[int] = ...,
        mempoolSize: _Optional[int] = ...,
        tipHashesCount: _Optional[int] = ...,
        difficulty: _Optional[float] = ...,
        pastMedianTime: _Optional[int] = ...,
        virtualParentHashesCount: _Optional[int] = ...,
        virtualDaaScore: _Optional[int] = ...,
    ) -> None: ...

class StorageMetrics(_message.Message):
    __slots__ = ("storageSizeBytes",)
    STORAGESIZEBYTES_FIELD_NUMBER: _ClassVar[int]
    storageSizeBytes: int
    def __init__(self, storageSizeBytes: _Optional[int] = ...) -> None: ...

class GetConnectionsRequestMessage(_message.Message):
    __slots__ = ("includeProfileData",)
    INCLUDEPROFILEDATA_FIELD_NUMBER: _ClassVar[int]
    includeProfileData: bool
    def __init__(self, includeProfileData: bool = ...) -> None: ...

class ConnectionsProfileData(_message.Message):
    __slots__ = ("cpuUsage", "memoryUsage")
    CPUUSAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORYUSAGE_FIELD_NUMBER: _ClassVar[int]
    cpuUsage: float
    memoryUsage: int
    def __init__(
        self, cpuUsage: _Optional[float] = ..., memoryUsage: _Optional[int] = ...
    ) -> None: ...

class GetConnectionsResponseMessage(_message.Message):
    __slots__ = ("clients", "peers", "profileData", "error")
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    PEERS_FIELD_NUMBER: _ClassVar[int]
    PROFILEDATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    clients: int
    peers: int
    profileData: ConnectionsProfileData
    error: RPCError
    def __init__(
        self,
        clients: _Optional[int] = ...,
        peers: _Optional[int] = ...,
        profileData: _Optional[_Union[ConnectionsProfileData, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetSystemInfoRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemInfoResponseMessage(_message.Message):
    __slots__ = (
        "version",
        "systemId",
        "gitHash",
        "coreNum",
        "totalMemory",
        "fdLimit",
        "proxySocketLimitPerCpuCore",
        "error",
    )
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEMID_FIELD_NUMBER: _ClassVar[int]
    GITHASH_FIELD_NUMBER: _ClassVar[int]
    CORENUM_FIELD_NUMBER: _ClassVar[int]
    TOTALMEMORY_FIELD_NUMBER: _ClassVar[int]
    FDLIMIT_FIELD_NUMBER: _ClassVar[int]
    PROXYSOCKETLIMITPERCPUCORE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    version: str
    systemId: str
    gitHash: str
    coreNum: int
    totalMemory: int
    fdLimit: int
    proxySocketLimitPerCpuCore: int
    error: RPCError
    def __init__(
        self,
        version: _Optional[str] = ...,
        systemId: _Optional[str] = ...,
        gitHash: _Optional[str] = ...,
        coreNum: _Optional[int] = ...,
        totalMemory: _Optional[int] = ...,
        fdLimit: _Optional[int] = ...,
        proxySocketLimitPerCpuCore: _Optional[int] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetMetricsRequestMessage(_message.Message):
    __slots__ = (
        "processMetrics",
        "connectionMetrics",
        "bandwidthMetrics",
        "consensusMetrics",
        "storageMetrics",
        "customMetrics",
    )
    PROCESSMETRICS_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMETRICS_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTHMETRICS_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSMETRICS_FIELD_NUMBER: _ClassVar[int]
    STORAGEMETRICS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMETRICS_FIELD_NUMBER: _ClassVar[int]
    processMetrics: bool
    connectionMetrics: bool
    bandwidthMetrics: bool
    consensusMetrics: bool
    storageMetrics: bool
    customMetrics: bool
    def __init__(
        self,
        processMetrics: bool = ...,
        connectionMetrics: bool = ...,
        bandwidthMetrics: bool = ...,
        consensusMetrics: bool = ...,
        storageMetrics: bool = ...,
        customMetrics: bool = ...,
    ) -> None: ...

class GetMetricsResponseMessage(_message.Message):
    __slots__ = (
        "serverTime",
        "processMetrics",
        "connectionMetrics",
        "bandwidthMetrics",
        "consensusMetrics",
        "storageMetrics",
        "error",
    )
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    PROCESSMETRICS_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMETRICS_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTHMETRICS_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSMETRICS_FIELD_NUMBER: _ClassVar[int]
    STORAGEMETRICS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    serverTime: int
    processMetrics: ProcessMetrics
    connectionMetrics: ConnectionMetrics
    bandwidthMetrics: BandwidthMetrics
    consensusMetrics: ConsensusMetrics
    storageMetrics: StorageMetrics
    error: RPCError
    def __init__(
        self,
        serverTime: _Optional[int] = ...,
        processMetrics: _Optional[_Union[ProcessMetrics, _Mapping]] = ...,
        connectionMetrics: _Optional[_Union[ConnectionMetrics, _Mapping]] = ...,
        bandwidthMetrics: _Optional[_Union[BandwidthMetrics, _Mapping]] = ...,
        consensusMetrics: _Optional[_Union[ConsensusMetrics, _Mapping]] = ...,
        storageMetrics: _Optional[_Union[StorageMetrics, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetServerInfoRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetServerInfoResponseMessage(_message.Message):
    __slots__ = (
        "rpcApiVersion",
        "rpcApiRevision",
        "serverVersion",
        "networkId",
        "hasUtxoIndex",
        "isSynced",
        "virtualDaaScore",
        "error",
    )
    RPCAPIVERSION_FIELD_NUMBER: _ClassVar[int]
    RPCAPIREVISION_FIELD_NUMBER: _ClassVar[int]
    SERVERVERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORKID_FIELD_NUMBER: _ClassVar[int]
    HASUTXOINDEX_FIELD_NUMBER: _ClassVar[int]
    ISSYNCED_FIELD_NUMBER: _ClassVar[int]
    VIRTUALDAASCORE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    rpcApiVersion: int
    rpcApiRevision: int
    serverVersion: str
    networkId: str
    hasUtxoIndex: bool
    isSynced: bool
    virtualDaaScore: int
    error: RPCError
    def __init__(
        self,
        rpcApiVersion: _Optional[int] = ...,
        rpcApiRevision: _Optional[int] = ...,
        serverVersion: _Optional[str] = ...,
        networkId: _Optional[str] = ...,
        hasUtxoIndex: bool = ...,
        isSynced: bool = ...,
        virtualDaaScore: _Optional[int] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetSyncStatusRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSyncStatusResponseMessage(_message.Message):
    __slots__ = ("isSynced", "error")
    ISSYNCED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    isSynced: bool
    error: RPCError
    def __init__(
        self, isSynced: bool = ..., error: _Optional[_Union[RPCError, _Mapping]] = ...
    ) -> None: ...

class GetDaaScoreTimestampEstimateRequestMessage(_message.Message):
    __slots__ = ("daaScores",)
    DAASCORES_FIELD_NUMBER: _ClassVar[int]
    daaScores: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, daaScores: _Optional[_Iterable[int]] = ...) -> None: ...

class GetDaaScoreTimestampEstimateResponseMessage(_message.Message):
    __slots__ = ("timestamps", "error")
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    timestamps: _containers.RepeatedScalarFieldContainer[int]
    error: RPCError
    def __init__(
        self,
        timestamps: _Optional[_Iterable[int]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class RpcFeerateBucket(_message.Message):
    __slots__ = ("feerate", "estimatedSeconds")
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATEDSECONDS_FIELD_NUMBER: _ClassVar[int]
    feerate: float
    estimatedSeconds: float
    def __init__(
        self, feerate: _Optional[float] = ..., estimatedSeconds: _Optional[float] = ...
    ) -> None: ...

class RpcFeeEstimate(_message.Message):
    __slots__ = ("priorityBucket", "normalBuckets", "lowBuckets")
    PRIORITYBUCKET_FIELD_NUMBER: _ClassVar[int]
    NORMALBUCKETS_FIELD_NUMBER: _ClassVar[int]
    LOWBUCKETS_FIELD_NUMBER: _ClassVar[int]
    priorityBucket: RpcFeerateBucket
    normalBuckets: _containers.RepeatedCompositeFieldContainer[RpcFeerateBucket]
    lowBuckets: _containers.RepeatedCompositeFieldContainer[RpcFeerateBucket]
    def __init__(
        self,
        priorityBucket: _Optional[_Union[RpcFeerateBucket, _Mapping]] = ...,
        normalBuckets: _Optional[_Iterable[_Union[RpcFeerateBucket, _Mapping]]] = ...,
        lowBuckets: _Optional[_Iterable[_Union[RpcFeerateBucket, _Mapping]]] = ...,
    ) -> None: ...

class RpcFeeEstimateVerboseExperimentalData(_message.Message):
    __slots__ = (
        "mempoolReadyTransactionsCount",
        "mempoolReadyTransactionsTotalMass",
        "networkMassPerSecond",
        "nextBlockTemplateFeerateMin",
        "nextBlockTemplateFeerateMedian",
        "nextBlockTemplateFeerateMax",
    )
    MEMPOOLREADYTRANSACTIONSCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEMPOOLREADYTRANSACTIONSTOTALMASS_FIELD_NUMBER: _ClassVar[int]
    NETWORKMASSPERSECOND_FIELD_NUMBER: _ClassVar[int]
    NEXTBLOCKTEMPLATEFEERATEMIN_FIELD_NUMBER: _ClassVar[int]
    NEXTBLOCKTEMPLATEFEERATEMEDIAN_FIELD_NUMBER: _ClassVar[int]
    NEXTBLOCKTEMPLATEFEERATEMAX_FIELD_NUMBER: _ClassVar[int]
    mempoolReadyTransactionsCount: int
    mempoolReadyTransactionsTotalMass: int
    networkMassPerSecond: int
    nextBlockTemplateFeerateMin: float
    nextBlockTemplateFeerateMedian: float
    nextBlockTemplateFeerateMax: float
    def __init__(
        self,
        mempoolReadyTransactionsCount: _Optional[int] = ...,
        mempoolReadyTransactionsTotalMass: _Optional[int] = ...,
        networkMassPerSecond: _Optional[int] = ...,
        nextBlockTemplateFeerateMin: _Optional[float] = ...,
        nextBlockTemplateFeerateMedian: _Optional[float] = ...,
        nextBlockTemplateFeerateMax: _Optional[float] = ...,
    ) -> None: ...

class GetFeeEstimateRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFeeEstimateResponseMessage(_message.Message):
    __slots__ = ("estimate", "error")
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    estimate: RpcFeeEstimate
    error: RPCError
    def __init__(
        self,
        estimate: _Optional[_Union[RpcFeeEstimate, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetFeeEstimateExperimentalRequestMessage(_message.Message):
    __slots__ = ("verbose",)
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    verbose: bool
    def __init__(self, verbose: bool = ...) -> None: ...

class GetFeeEstimateExperimentalResponseMessage(_message.Message):
    __slots__ = ("estimate", "verbose", "error")
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    estimate: RpcFeeEstimate
    verbose: RpcFeeEstimateVerboseExperimentalData
    error: RPCError
    def __init__(
        self,
        estimate: _Optional[_Union[RpcFeeEstimate, _Mapping]] = ...,
        verbose: _Optional[_Union[RpcFeeEstimateVerboseExperimentalData, _Mapping]] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...

class GetCurrentBlockColorRequestMessage(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class GetCurrentBlockColorResponseMessage(_message.Message):
    __slots__ = ("blue", "error")
    BLUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    blue: bool
    error: RPCError
    def __init__(
        self, blue: bool = ..., error: _Optional[_Union[RPCError, _Mapping]] = ...
    ) -> None: ...

class GetUtxoReturnAddressRequestMessage(_message.Message):
    __slots__ = ("txid", "accepting_block_daa_score")
    TXID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTING_BLOCK_DAA_SCORE_FIELD_NUMBER: _ClassVar[int]
    txid: str
    accepting_block_daa_score: int
    def __init__(
        self, txid: _Optional[str] = ..., accepting_block_daa_score: _Optional[int] = ...
    ) -> None: ...

class GetUtxoReturnAddressResponseMessage(_message.Message):
    __slots__ = ("return_address", "error")
    RETURN_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    return_address: str
    error: RPCError
    def __init__(
        self,
        return_address: _Optional[str] = ...,
        error: _Optional[_Union[RPCError, _Mapping]] = ...,
    ) -> None: ...
