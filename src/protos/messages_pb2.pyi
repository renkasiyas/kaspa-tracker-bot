from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

import rpc_pb2 as _rpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class KaspadRequest(_message.Message):
    __slots__ = (
        "id",
        "getCurrentNetworkRequest",
        "submitBlockRequest",
        "getBlockTemplateRequest",
        "notifyBlockAddedRequest",
        "getPeerAddressesRequest",
        "GetSinkRequest",
        "getMempoolEntryRequest",
        "getConnectedPeerInfoRequest",
        "addPeerRequest",
        "submitTransactionRequest",
        "notifyVirtualChainChangedRequest",
        "getBlockRequest",
        "getSubnetworkRequest",
        "getVirtualChainFromBlockRequest",
        "getBlocksRequest",
        "getBlockCountRequest",
        "getBlockDagInfoRequest",
        "resolveFinalityConflictRequest",
        "notifyFinalityConflictRequest",
        "getMempoolEntriesRequest",
        "shutdownRequest",
        "getHeadersRequest",
        "notifyUtxosChangedRequest",
        "getUtxosByAddressesRequest",
        "getSinkBlueScoreRequest",
        "notifySinkBlueScoreChangedRequest",
        "banRequest",
        "unbanRequest",
        "getInfoRequest",
        "stopNotifyingUtxosChangedRequest",
        "notifyPruningPointUtxoSetOverrideRequest",
        "stopNotifyingPruningPointUtxoSetOverrideRequest",
        "estimateNetworkHashesPerSecondRequest",
        "notifyVirtualDaaScoreChangedRequest",
        "getBalanceByAddressRequest",
        "getBalancesByAddressesRequest",
        "notifyNewBlockTemplateRequest",
        "getMempoolEntriesByAddressesRequest",
        "getCoinSupplyRequest",
        "pingRequest",
        "getMetricsRequest",
        "getServerInfoRequest",
        "getSyncStatusRequest",
        "getDaaScoreTimestampEstimateRequest",
        "submitTransactionReplacementRequest",
        "getConnectionsRequest",
        "getSystemInfoRequest",
        "getFeeEstimateRequest",
        "getFeeEstimateExperimentalRequest",
        "getCurrentBlockColorRequest",
        "GetUtxoReturnAddressRequest",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    GETCURRENTNETWORKREQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBMITBLOCKREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKTEMPLATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYBLOCKADDEDREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETPEERADDRESSESREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSINKREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETMEMPOOLENTRYREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETCONNECTEDPEERINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    ADDPEERREQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBMITTRANSACTIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYVIRTUALCHAINCHANGEDREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSUBNETWORKREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETVIRTUALCHAINFROMBLOCKREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKSREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKCOUNTREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKDAGINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    RESOLVEFINALITYCONFLICTREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYFINALITYCONFLICTREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETMEMPOOLENTRIESREQUEST_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWNREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETHEADERSREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYUTXOSCHANGEDREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETUTXOSBYADDRESSESREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSINKBLUESCOREREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYSINKBLUESCORECHANGEDREQUEST_FIELD_NUMBER: _ClassVar[int]
    BANREQUEST_FIELD_NUMBER: _ClassVar[int]
    UNBANREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    STOPNOTIFYINGUTXOSCHANGEDREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYPRUNINGPOINTUTXOSETOVERRIDEREQUEST_FIELD_NUMBER: _ClassVar[int]
    STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDEREQUEST_FIELD_NUMBER: _ClassVar[int]
    ESTIMATENETWORKHASHESPERSECONDREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYVIRTUALDAASCORECHANGEDREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBALANCEBYADDRESSREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETBALANCESBYADDRESSESREQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFYNEWBLOCKTEMPLATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETMEMPOOLENTRIESBYADDRESSESREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETCOINSUPPLYREQUEST_FIELD_NUMBER: _ClassVar[int]
    PINGREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETMETRICSREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSERVERINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSYNCSTATUSREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETDAASCORETIMESTAMPESTIMATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBMITTRANSACTIONREPLACEMENTREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETCONNECTIONSREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSYSTEMINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETFEEESTIMATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETFEEESTIMATEEXPERIMENTALREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETCURRENTBLOCKCOLORREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETUTXORETURNADDRESSREQUEST_FIELD_NUMBER: _ClassVar[int]
    id: int
    getCurrentNetworkRequest: _rpc_pb2.GetCurrentNetworkRequestMessage
    submitBlockRequest: _rpc_pb2.SubmitBlockRequestMessage
    getBlockTemplateRequest: _rpc_pb2.GetBlockTemplateRequestMessage
    notifyBlockAddedRequest: _rpc_pb2.NotifyBlockAddedRequestMessage
    getPeerAddressesRequest: _rpc_pb2.GetPeerAddressesRequestMessage
    GetSinkRequest: _rpc_pb2.GetSinkRequestMessage
    getMempoolEntryRequest: _rpc_pb2.GetMempoolEntryRequestMessage
    getConnectedPeerInfoRequest: _rpc_pb2.GetConnectedPeerInfoRequestMessage
    addPeerRequest: _rpc_pb2.AddPeerRequestMessage
    submitTransactionRequest: _rpc_pb2.SubmitTransactionRequestMessage
    notifyVirtualChainChangedRequest: _rpc_pb2.NotifyVirtualChainChangedRequestMessage
    getBlockRequest: _rpc_pb2.GetBlockRequestMessage
    getSubnetworkRequest: _rpc_pb2.GetSubnetworkRequestMessage
    getVirtualChainFromBlockRequest: _rpc_pb2.GetVirtualChainFromBlockRequestMessage
    getBlocksRequest: _rpc_pb2.GetBlocksRequestMessage
    getBlockCountRequest: _rpc_pb2.GetBlockCountRequestMessage
    getBlockDagInfoRequest: _rpc_pb2.GetBlockDagInfoRequestMessage
    resolveFinalityConflictRequest: _rpc_pb2.ResolveFinalityConflictRequestMessage
    notifyFinalityConflictRequest: _rpc_pb2.NotifyFinalityConflictRequestMessage
    getMempoolEntriesRequest: _rpc_pb2.GetMempoolEntriesRequestMessage
    shutdownRequest: _rpc_pb2.ShutdownRequestMessage
    getHeadersRequest: _rpc_pb2.GetHeadersRequestMessage
    notifyUtxosChangedRequest: _rpc_pb2.NotifyUtxosChangedRequestMessage
    getUtxosByAddressesRequest: _rpc_pb2.GetUtxosByAddressesRequestMessage
    getSinkBlueScoreRequest: _rpc_pb2.GetSinkBlueScoreRequestMessage
    notifySinkBlueScoreChangedRequest: _rpc_pb2.NotifySinkBlueScoreChangedRequestMessage
    banRequest: _rpc_pb2.BanRequestMessage
    unbanRequest: _rpc_pb2.UnbanRequestMessage
    getInfoRequest: _rpc_pb2.GetInfoRequestMessage
    stopNotifyingUtxosChangedRequest: _rpc_pb2.StopNotifyingUtxosChangedRequestMessage
    notifyPruningPointUtxoSetOverrideRequest: (
        _rpc_pb2.NotifyPruningPointUtxoSetOverrideRequestMessage
    )
    stopNotifyingPruningPointUtxoSetOverrideRequest: (
        _rpc_pb2.StopNotifyingPruningPointUtxoSetOverrideRequestMessage
    )
    estimateNetworkHashesPerSecondRequest: _rpc_pb2.EstimateNetworkHashesPerSecondRequestMessage
    notifyVirtualDaaScoreChangedRequest: _rpc_pb2.NotifyVirtualDaaScoreChangedRequestMessage
    getBalanceByAddressRequest: _rpc_pb2.GetBalanceByAddressRequestMessage
    getBalancesByAddressesRequest: _rpc_pb2.GetBalancesByAddressesRequestMessage
    notifyNewBlockTemplateRequest: _rpc_pb2.NotifyNewBlockTemplateRequestMessage
    getMempoolEntriesByAddressesRequest: _rpc_pb2.GetMempoolEntriesByAddressesRequestMessage
    getCoinSupplyRequest: _rpc_pb2.GetCoinSupplyRequestMessage
    pingRequest: _rpc_pb2.PingRequestMessage
    getMetricsRequest: _rpc_pb2.GetMetricsRequestMessage
    getServerInfoRequest: _rpc_pb2.GetServerInfoRequestMessage
    getSyncStatusRequest: _rpc_pb2.GetSyncStatusRequestMessage
    getDaaScoreTimestampEstimateRequest: _rpc_pb2.GetDaaScoreTimestampEstimateRequestMessage
    submitTransactionReplacementRequest: _rpc_pb2.SubmitTransactionReplacementRequestMessage
    getConnectionsRequest: _rpc_pb2.GetConnectionsRequestMessage
    getSystemInfoRequest: _rpc_pb2.GetSystemInfoRequestMessage
    getFeeEstimateRequest: _rpc_pb2.GetFeeEstimateRequestMessage
    getFeeEstimateExperimentalRequest: _rpc_pb2.GetFeeEstimateExperimentalRequestMessage
    getCurrentBlockColorRequest: _rpc_pb2.GetCurrentBlockColorRequestMessage
    GetUtxoReturnAddressRequest: _rpc_pb2.GetUtxoReturnAddressRequestMessage
    def __init__(
        self,
        id: _Optional[int] = ...,
        getCurrentNetworkRequest: _Optional[
            _Union[_rpc_pb2.GetCurrentNetworkRequestMessage, _Mapping]
        ] = ...,
        submitBlockRequest: _Optional[_Union[_rpc_pb2.SubmitBlockRequestMessage, _Mapping]] = ...,
        getBlockTemplateRequest: _Optional[
            _Union[_rpc_pb2.GetBlockTemplateRequestMessage, _Mapping]
        ] = ...,
        notifyBlockAddedRequest: _Optional[
            _Union[_rpc_pb2.NotifyBlockAddedRequestMessage, _Mapping]
        ] = ...,
        getPeerAddressesRequest: _Optional[
            _Union[_rpc_pb2.GetPeerAddressesRequestMessage, _Mapping]
        ] = ...,
        GetSinkRequest: _Optional[_Union[_rpc_pb2.GetSinkRequestMessage, _Mapping]] = ...,
        getMempoolEntryRequest: _Optional[
            _Union[_rpc_pb2.GetMempoolEntryRequestMessage, _Mapping]
        ] = ...,
        getConnectedPeerInfoRequest: _Optional[
            _Union[_rpc_pb2.GetConnectedPeerInfoRequestMessage, _Mapping]
        ] = ...,
        addPeerRequest: _Optional[_Union[_rpc_pb2.AddPeerRequestMessage, _Mapping]] = ...,
        submitTransactionRequest: _Optional[
            _Union[_rpc_pb2.SubmitTransactionRequestMessage, _Mapping]
        ] = ...,
        notifyVirtualChainChangedRequest: _Optional[
            _Union[_rpc_pb2.NotifyVirtualChainChangedRequestMessage, _Mapping]
        ] = ...,
        getBlockRequest: _Optional[_Union[_rpc_pb2.GetBlockRequestMessage, _Mapping]] = ...,
        getSubnetworkRequest: _Optional[
            _Union[_rpc_pb2.GetSubnetworkRequestMessage, _Mapping]
        ] = ...,
        getVirtualChainFromBlockRequest: _Optional[
            _Union[_rpc_pb2.GetVirtualChainFromBlockRequestMessage, _Mapping]
        ] = ...,
        getBlocksRequest: _Optional[_Union[_rpc_pb2.GetBlocksRequestMessage, _Mapping]] = ...,
        getBlockCountRequest: _Optional[
            _Union[_rpc_pb2.GetBlockCountRequestMessage, _Mapping]
        ] = ...,
        getBlockDagInfoRequest: _Optional[
            _Union[_rpc_pb2.GetBlockDagInfoRequestMessage, _Mapping]
        ] = ...,
        resolveFinalityConflictRequest: _Optional[
            _Union[_rpc_pb2.ResolveFinalityConflictRequestMessage, _Mapping]
        ] = ...,
        notifyFinalityConflictRequest: _Optional[
            _Union[_rpc_pb2.NotifyFinalityConflictRequestMessage, _Mapping]
        ] = ...,
        getMempoolEntriesRequest: _Optional[
            _Union[_rpc_pb2.GetMempoolEntriesRequestMessage, _Mapping]
        ] = ...,
        shutdownRequest: _Optional[_Union[_rpc_pb2.ShutdownRequestMessage, _Mapping]] = ...,
        getHeadersRequest: _Optional[_Union[_rpc_pb2.GetHeadersRequestMessage, _Mapping]] = ...,
        notifyUtxosChangedRequest: _Optional[
            _Union[_rpc_pb2.NotifyUtxosChangedRequestMessage, _Mapping]
        ] = ...,
        getUtxosByAddressesRequest: _Optional[
            _Union[_rpc_pb2.GetUtxosByAddressesRequestMessage, _Mapping]
        ] = ...,
        getSinkBlueScoreRequest: _Optional[
            _Union[_rpc_pb2.GetSinkBlueScoreRequestMessage, _Mapping]
        ] = ...,
        notifySinkBlueScoreChangedRequest: _Optional[
            _Union[_rpc_pb2.NotifySinkBlueScoreChangedRequestMessage, _Mapping]
        ] = ...,
        banRequest: _Optional[_Union[_rpc_pb2.BanRequestMessage, _Mapping]] = ...,
        unbanRequest: _Optional[_Union[_rpc_pb2.UnbanRequestMessage, _Mapping]] = ...,
        getInfoRequest: _Optional[_Union[_rpc_pb2.GetInfoRequestMessage, _Mapping]] = ...,
        stopNotifyingUtxosChangedRequest: _Optional[
            _Union[_rpc_pb2.StopNotifyingUtxosChangedRequestMessage, _Mapping]
        ] = ...,
        notifyPruningPointUtxoSetOverrideRequest: _Optional[
            _Union[_rpc_pb2.NotifyPruningPointUtxoSetOverrideRequestMessage, _Mapping]
        ] = ...,
        stopNotifyingPruningPointUtxoSetOverrideRequest: _Optional[
            _Union[_rpc_pb2.StopNotifyingPruningPointUtxoSetOverrideRequestMessage, _Mapping]
        ] = ...,
        estimateNetworkHashesPerSecondRequest: _Optional[
            _Union[_rpc_pb2.EstimateNetworkHashesPerSecondRequestMessage, _Mapping]
        ] = ...,
        notifyVirtualDaaScoreChangedRequest: _Optional[
            _Union[_rpc_pb2.NotifyVirtualDaaScoreChangedRequestMessage, _Mapping]
        ] = ...,
        getBalanceByAddressRequest: _Optional[
            _Union[_rpc_pb2.GetBalanceByAddressRequestMessage, _Mapping]
        ] = ...,
        getBalancesByAddressesRequest: _Optional[
            _Union[_rpc_pb2.GetBalancesByAddressesRequestMessage, _Mapping]
        ] = ...,
        notifyNewBlockTemplateRequest: _Optional[
            _Union[_rpc_pb2.NotifyNewBlockTemplateRequestMessage, _Mapping]
        ] = ...,
        getMempoolEntriesByAddressesRequest: _Optional[
            _Union[_rpc_pb2.GetMempoolEntriesByAddressesRequestMessage, _Mapping]
        ] = ...,
        getCoinSupplyRequest: _Optional[
            _Union[_rpc_pb2.GetCoinSupplyRequestMessage, _Mapping]
        ] = ...,
        pingRequest: _Optional[_Union[_rpc_pb2.PingRequestMessage, _Mapping]] = ...,
        getMetricsRequest: _Optional[_Union[_rpc_pb2.GetMetricsRequestMessage, _Mapping]] = ...,
        getServerInfoRequest: _Optional[
            _Union[_rpc_pb2.GetServerInfoRequestMessage, _Mapping]
        ] = ...,
        getSyncStatusRequest: _Optional[
            _Union[_rpc_pb2.GetSyncStatusRequestMessage, _Mapping]
        ] = ...,
        getDaaScoreTimestampEstimateRequest: _Optional[
            _Union[_rpc_pb2.GetDaaScoreTimestampEstimateRequestMessage, _Mapping]
        ] = ...,
        submitTransactionReplacementRequest: _Optional[
            _Union[_rpc_pb2.SubmitTransactionReplacementRequestMessage, _Mapping]
        ] = ...,
        getConnectionsRequest: _Optional[
            _Union[_rpc_pb2.GetConnectionsRequestMessage, _Mapping]
        ] = ...,
        getSystemInfoRequest: _Optional[
            _Union[_rpc_pb2.GetSystemInfoRequestMessage, _Mapping]
        ] = ...,
        getFeeEstimateRequest: _Optional[
            _Union[_rpc_pb2.GetFeeEstimateRequestMessage, _Mapping]
        ] = ...,
        getFeeEstimateExperimentalRequest: _Optional[
            _Union[_rpc_pb2.GetFeeEstimateExperimentalRequestMessage, _Mapping]
        ] = ...,
        getCurrentBlockColorRequest: _Optional[
            _Union[_rpc_pb2.GetCurrentBlockColorRequestMessage, _Mapping]
        ] = ...,
        GetUtxoReturnAddressRequest: _Optional[
            _Union[_rpc_pb2.GetUtxoReturnAddressRequestMessage, _Mapping]
        ] = ...,
    ) -> None: ...

class KaspadResponse(_message.Message):
    __slots__ = (
        "id",
        "getCurrentNetworkResponse",
        "submitBlockResponse",
        "getBlockTemplateResponse",
        "notifyBlockAddedResponse",
        "blockAddedNotification",
        "getPeerAddressesResponse",
        "GetSinkResponse",
        "getMempoolEntryResponse",
        "getConnectedPeerInfoResponse",
        "addPeerResponse",
        "submitTransactionResponse",
        "notifyVirtualChainChangedResponse",
        "virtualChainChangedNotification",
        "getBlockResponse",
        "getSubnetworkResponse",
        "getVirtualChainFromBlockResponse",
        "getBlocksResponse",
        "getBlockCountResponse",
        "getBlockDagInfoResponse",
        "resolveFinalityConflictResponse",
        "notifyFinalityConflictResponse",
        "finalityConflictNotification",
        "finalityConflictResolvedNotification",
        "getMempoolEntriesResponse",
        "shutdownResponse",
        "getHeadersResponse",
        "notifyUtxosChangedResponse",
        "utxosChangedNotification",
        "getUtxosByAddressesResponse",
        "getSinkBlueScoreResponse",
        "notifySinkBlueScoreChangedResponse",
        "sinkBlueScoreChangedNotification",
        "banResponse",
        "unbanResponse",
        "getInfoResponse",
        "stopNotifyingUtxosChangedResponse",
        "notifyPruningPointUtxoSetOverrideResponse",
        "pruningPointUtxoSetOverrideNotification",
        "stopNotifyingPruningPointUtxoSetOverrideResponse",
        "estimateNetworkHashesPerSecondResponse",
        "notifyVirtualDaaScoreChangedResponse",
        "virtualDaaScoreChangedNotification",
        "getBalanceByAddressResponse",
        "getBalancesByAddressesResponse",
        "notifyNewBlockTemplateResponse",
        "newBlockTemplateNotification",
        "getMempoolEntriesByAddressesResponse",
        "getCoinSupplyResponse",
        "pingResponse",
        "getMetricsResponse",
        "getServerInfoResponse",
        "getSyncStatusResponse",
        "getDaaScoreTimestampEstimateResponse",
        "submitTransactionReplacementResponse",
        "getConnectionsResponse",
        "getSystemInfoResponse",
        "getFeeEstimateResponse",
        "getFeeEstimateExperimentalResponse",
        "getCurrentBlockColorResponse",
        "GetUtxoReturnAddressResponse",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    GETCURRENTNETWORKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBMITBLOCKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKTEMPLATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYBLOCKADDEDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BLOCKADDEDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    GETPEERADDRESSESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSINKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETMEMPOOLENTRYRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETCONNECTEDPEERINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    ADDPEERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTRANSACTIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYVIRTUALCHAINCHANGEDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    VIRTUALCHAINCHANGEDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSUBNETWORKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETVIRTUALCHAINFROMBLOCKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKCOUNTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETBLOCKDAGINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESOLVEFINALITYCONFLICTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYFINALITYCONFLICTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    FINALITYCONFLICTNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    FINALITYCONFLICTRESOLVEDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    GETMEMPOOLENTRIESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWNRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETHEADERSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYUTXOSCHANGEDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    UTXOSCHANGEDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    GETUTXOSBYADDRESSESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSINKBLUESCORERESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYSINKBLUESCORECHANGEDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SINKBLUESCORECHANGEDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    BANRESPONSE_FIELD_NUMBER: _ClassVar[int]
    UNBANRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    STOPNOTIFYINGUTXOSCHANGEDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYPRUNINGPOINTUTXOSETOVERRIDERESPONSE_FIELD_NUMBER: _ClassVar[int]
    PRUNINGPOINTUTXOSETOVERRIDENOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDERESPONSE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATENETWORKHASHESPERSECONDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYVIRTUALDAASCORECHANGEDRESPONSE_FIELD_NUMBER: _ClassVar[int]
    VIRTUALDAASCORECHANGEDNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    GETBALANCEBYADDRESSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETBALANCESBYADDRESSESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOTIFYNEWBLOCKTEMPLATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEWBLOCKTEMPLATENOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    GETMEMPOOLENTRIESBYADDRESSESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETCOINSUPPLYRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PINGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETMETRICSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSERVERINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSYNCSTATUSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETDAASCORETIMESTAMPESTIMATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTRANSACTIONREPLACEMENTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETCONNECTIONSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETSYSTEMINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETFEEESTIMATERESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETFEEESTIMATEEXPERIMENTALRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETCURRENTBLOCKCOLORRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETUTXORETURNADDRESSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    id: int
    getCurrentNetworkResponse: _rpc_pb2.GetCurrentNetworkResponseMessage
    submitBlockResponse: _rpc_pb2.SubmitBlockResponseMessage
    getBlockTemplateResponse: _rpc_pb2.GetBlockTemplateResponseMessage
    notifyBlockAddedResponse: _rpc_pb2.NotifyBlockAddedResponseMessage
    blockAddedNotification: _rpc_pb2.BlockAddedNotificationMessage
    getPeerAddressesResponse: _rpc_pb2.GetPeerAddressesResponseMessage
    GetSinkResponse: _rpc_pb2.GetSinkResponseMessage
    getMempoolEntryResponse: _rpc_pb2.GetMempoolEntryResponseMessage
    getConnectedPeerInfoResponse: _rpc_pb2.GetConnectedPeerInfoResponseMessage
    addPeerResponse: _rpc_pb2.AddPeerResponseMessage
    submitTransactionResponse: _rpc_pb2.SubmitTransactionResponseMessage
    notifyVirtualChainChangedResponse: _rpc_pb2.NotifyVirtualChainChangedResponseMessage
    virtualChainChangedNotification: _rpc_pb2.VirtualChainChangedNotificationMessage
    getBlockResponse: _rpc_pb2.GetBlockResponseMessage
    getSubnetworkResponse: _rpc_pb2.GetSubnetworkResponseMessage
    getVirtualChainFromBlockResponse: _rpc_pb2.GetVirtualChainFromBlockResponseMessage
    getBlocksResponse: _rpc_pb2.GetBlocksResponseMessage
    getBlockCountResponse: _rpc_pb2.GetBlockCountResponseMessage
    getBlockDagInfoResponse: _rpc_pb2.GetBlockDagInfoResponseMessage
    resolveFinalityConflictResponse: _rpc_pb2.ResolveFinalityConflictResponseMessage
    notifyFinalityConflictResponse: _rpc_pb2.NotifyFinalityConflictResponseMessage
    finalityConflictNotification: _rpc_pb2.FinalityConflictNotificationMessage
    finalityConflictResolvedNotification: _rpc_pb2.FinalityConflictResolvedNotificationMessage
    getMempoolEntriesResponse: _rpc_pb2.GetMempoolEntriesResponseMessage
    shutdownResponse: _rpc_pb2.ShutdownResponseMessage
    getHeadersResponse: _rpc_pb2.GetHeadersResponseMessage
    notifyUtxosChangedResponse: _rpc_pb2.NotifyUtxosChangedResponseMessage
    utxosChangedNotification: _rpc_pb2.UtxosChangedNotificationMessage
    getUtxosByAddressesResponse: _rpc_pb2.GetUtxosByAddressesResponseMessage
    getSinkBlueScoreResponse: _rpc_pb2.GetSinkBlueScoreResponseMessage
    notifySinkBlueScoreChangedResponse: _rpc_pb2.NotifySinkBlueScoreChangedResponseMessage
    sinkBlueScoreChangedNotification: _rpc_pb2.SinkBlueScoreChangedNotificationMessage
    banResponse: _rpc_pb2.BanResponseMessage
    unbanResponse: _rpc_pb2.UnbanResponseMessage
    getInfoResponse: _rpc_pb2.GetInfoResponseMessage
    stopNotifyingUtxosChangedResponse: _rpc_pb2.StopNotifyingUtxosChangedResponseMessage
    notifyPruningPointUtxoSetOverrideResponse: (
        _rpc_pb2.NotifyPruningPointUtxoSetOverrideResponseMessage
    )
    pruningPointUtxoSetOverrideNotification: _rpc_pb2.PruningPointUtxoSetOverrideNotificationMessage
    stopNotifyingPruningPointUtxoSetOverrideResponse: (
        _rpc_pb2.StopNotifyingPruningPointUtxoSetOverrideResponseMessage
    )
    estimateNetworkHashesPerSecondResponse: _rpc_pb2.EstimateNetworkHashesPerSecondResponseMessage
    notifyVirtualDaaScoreChangedResponse: _rpc_pb2.NotifyVirtualDaaScoreChangedResponseMessage
    virtualDaaScoreChangedNotification: _rpc_pb2.VirtualDaaScoreChangedNotificationMessage
    getBalanceByAddressResponse: _rpc_pb2.GetBalanceByAddressResponseMessage
    getBalancesByAddressesResponse: _rpc_pb2.GetBalancesByAddressesResponseMessage
    notifyNewBlockTemplateResponse: _rpc_pb2.NotifyNewBlockTemplateResponseMessage
    newBlockTemplateNotification: _rpc_pb2.NewBlockTemplateNotificationMessage
    getMempoolEntriesByAddressesResponse: _rpc_pb2.GetMempoolEntriesByAddressesResponseMessage
    getCoinSupplyResponse: _rpc_pb2.GetCoinSupplyResponseMessage
    pingResponse: _rpc_pb2.PingResponseMessage
    getMetricsResponse: _rpc_pb2.GetMetricsResponseMessage
    getServerInfoResponse: _rpc_pb2.GetServerInfoResponseMessage
    getSyncStatusResponse: _rpc_pb2.GetSyncStatusResponseMessage
    getDaaScoreTimestampEstimateResponse: _rpc_pb2.GetDaaScoreTimestampEstimateResponseMessage
    submitTransactionReplacementResponse: _rpc_pb2.SubmitTransactionReplacementResponseMessage
    getConnectionsResponse: _rpc_pb2.GetConnectionsResponseMessage
    getSystemInfoResponse: _rpc_pb2.GetSystemInfoResponseMessage
    getFeeEstimateResponse: _rpc_pb2.GetFeeEstimateResponseMessage
    getFeeEstimateExperimentalResponse: _rpc_pb2.GetFeeEstimateExperimentalResponseMessage
    getCurrentBlockColorResponse: _rpc_pb2.GetCurrentBlockColorResponseMessage
    GetUtxoReturnAddressResponse: _rpc_pb2.GetUtxoReturnAddressResponseMessage
    def __init__(
        self,
        id: _Optional[int] = ...,
        getCurrentNetworkResponse: _Optional[
            _Union[_rpc_pb2.GetCurrentNetworkResponseMessage, _Mapping]
        ] = ...,
        submitBlockResponse: _Optional[_Union[_rpc_pb2.SubmitBlockResponseMessage, _Mapping]] = ...,
        getBlockTemplateResponse: _Optional[
            _Union[_rpc_pb2.GetBlockTemplateResponseMessage, _Mapping]
        ] = ...,
        notifyBlockAddedResponse: _Optional[
            _Union[_rpc_pb2.NotifyBlockAddedResponseMessage, _Mapping]
        ] = ...,
        blockAddedNotification: _Optional[
            _Union[_rpc_pb2.BlockAddedNotificationMessage, _Mapping]
        ] = ...,
        getPeerAddressesResponse: _Optional[
            _Union[_rpc_pb2.GetPeerAddressesResponseMessage, _Mapping]
        ] = ...,
        GetSinkResponse: _Optional[_Union[_rpc_pb2.GetSinkResponseMessage, _Mapping]] = ...,
        getMempoolEntryResponse: _Optional[
            _Union[_rpc_pb2.GetMempoolEntryResponseMessage, _Mapping]
        ] = ...,
        getConnectedPeerInfoResponse: _Optional[
            _Union[_rpc_pb2.GetConnectedPeerInfoResponseMessage, _Mapping]
        ] = ...,
        addPeerResponse: _Optional[_Union[_rpc_pb2.AddPeerResponseMessage, _Mapping]] = ...,
        submitTransactionResponse: _Optional[
            _Union[_rpc_pb2.SubmitTransactionResponseMessage, _Mapping]
        ] = ...,
        notifyVirtualChainChangedResponse: _Optional[
            _Union[_rpc_pb2.NotifyVirtualChainChangedResponseMessage, _Mapping]
        ] = ...,
        virtualChainChangedNotification: _Optional[
            _Union[_rpc_pb2.VirtualChainChangedNotificationMessage, _Mapping]
        ] = ...,
        getBlockResponse: _Optional[_Union[_rpc_pb2.GetBlockResponseMessage, _Mapping]] = ...,
        getSubnetworkResponse: _Optional[
            _Union[_rpc_pb2.GetSubnetworkResponseMessage, _Mapping]
        ] = ...,
        getVirtualChainFromBlockResponse: _Optional[
            _Union[_rpc_pb2.GetVirtualChainFromBlockResponseMessage, _Mapping]
        ] = ...,
        getBlocksResponse: _Optional[_Union[_rpc_pb2.GetBlocksResponseMessage, _Mapping]] = ...,
        getBlockCountResponse: _Optional[
            _Union[_rpc_pb2.GetBlockCountResponseMessage, _Mapping]
        ] = ...,
        getBlockDagInfoResponse: _Optional[
            _Union[_rpc_pb2.GetBlockDagInfoResponseMessage, _Mapping]
        ] = ...,
        resolveFinalityConflictResponse: _Optional[
            _Union[_rpc_pb2.ResolveFinalityConflictResponseMessage, _Mapping]
        ] = ...,
        notifyFinalityConflictResponse: _Optional[
            _Union[_rpc_pb2.NotifyFinalityConflictResponseMessage, _Mapping]
        ] = ...,
        finalityConflictNotification: _Optional[
            _Union[_rpc_pb2.FinalityConflictNotificationMessage, _Mapping]
        ] = ...,
        finalityConflictResolvedNotification: _Optional[
            _Union[_rpc_pb2.FinalityConflictResolvedNotificationMessage, _Mapping]
        ] = ...,
        getMempoolEntriesResponse: _Optional[
            _Union[_rpc_pb2.GetMempoolEntriesResponseMessage, _Mapping]
        ] = ...,
        shutdownResponse: _Optional[_Union[_rpc_pb2.ShutdownResponseMessage, _Mapping]] = ...,
        getHeadersResponse: _Optional[_Union[_rpc_pb2.GetHeadersResponseMessage, _Mapping]] = ...,
        notifyUtxosChangedResponse: _Optional[
            _Union[_rpc_pb2.NotifyUtxosChangedResponseMessage, _Mapping]
        ] = ...,
        utxosChangedNotification: _Optional[
            _Union[_rpc_pb2.UtxosChangedNotificationMessage, _Mapping]
        ] = ...,
        getUtxosByAddressesResponse: _Optional[
            _Union[_rpc_pb2.GetUtxosByAddressesResponseMessage, _Mapping]
        ] = ...,
        getSinkBlueScoreResponse: _Optional[
            _Union[_rpc_pb2.GetSinkBlueScoreResponseMessage, _Mapping]
        ] = ...,
        notifySinkBlueScoreChangedResponse: _Optional[
            _Union[_rpc_pb2.NotifySinkBlueScoreChangedResponseMessage, _Mapping]
        ] = ...,
        sinkBlueScoreChangedNotification: _Optional[
            _Union[_rpc_pb2.SinkBlueScoreChangedNotificationMessage, _Mapping]
        ] = ...,
        banResponse: _Optional[_Union[_rpc_pb2.BanResponseMessage, _Mapping]] = ...,
        unbanResponse: _Optional[_Union[_rpc_pb2.UnbanResponseMessage, _Mapping]] = ...,
        getInfoResponse: _Optional[_Union[_rpc_pb2.GetInfoResponseMessage, _Mapping]] = ...,
        stopNotifyingUtxosChangedResponse: _Optional[
            _Union[_rpc_pb2.StopNotifyingUtxosChangedResponseMessage, _Mapping]
        ] = ...,
        notifyPruningPointUtxoSetOverrideResponse: _Optional[
            _Union[_rpc_pb2.NotifyPruningPointUtxoSetOverrideResponseMessage, _Mapping]
        ] = ...,
        pruningPointUtxoSetOverrideNotification: _Optional[
            _Union[_rpc_pb2.PruningPointUtxoSetOverrideNotificationMessage, _Mapping]
        ] = ...,
        stopNotifyingPruningPointUtxoSetOverrideResponse: _Optional[
            _Union[_rpc_pb2.StopNotifyingPruningPointUtxoSetOverrideResponseMessage, _Mapping]
        ] = ...,
        estimateNetworkHashesPerSecondResponse: _Optional[
            _Union[_rpc_pb2.EstimateNetworkHashesPerSecondResponseMessage, _Mapping]
        ] = ...,
        notifyVirtualDaaScoreChangedResponse: _Optional[
            _Union[_rpc_pb2.NotifyVirtualDaaScoreChangedResponseMessage, _Mapping]
        ] = ...,
        virtualDaaScoreChangedNotification: _Optional[
            _Union[_rpc_pb2.VirtualDaaScoreChangedNotificationMessage, _Mapping]
        ] = ...,
        getBalanceByAddressResponse: _Optional[
            _Union[_rpc_pb2.GetBalanceByAddressResponseMessage, _Mapping]
        ] = ...,
        getBalancesByAddressesResponse: _Optional[
            _Union[_rpc_pb2.GetBalancesByAddressesResponseMessage, _Mapping]
        ] = ...,
        notifyNewBlockTemplateResponse: _Optional[
            _Union[_rpc_pb2.NotifyNewBlockTemplateResponseMessage, _Mapping]
        ] = ...,
        newBlockTemplateNotification: _Optional[
            _Union[_rpc_pb2.NewBlockTemplateNotificationMessage, _Mapping]
        ] = ...,
        getMempoolEntriesByAddressesResponse: _Optional[
            _Union[_rpc_pb2.GetMempoolEntriesByAddressesResponseMessage, _Mapping]
        ] = ...,
        getCoinSupplyResponse: _Optional[
            _Union[_rpc_pb2.GetCoinSupplyResponseMessage, _Mapping]
        ] = ...,
        pingResponse: _Optional[_Union[_rpc_pb2.PingResponseMessage, _Mapping]] = ...,
        getMetricsResponse: _Optional[_Union[_rpc_pb2.GetMetricsResponseMessage, _Mapping]] = ...,
        getServerInfoResponse: _Optional[
            _Union[_rpc_pb2.GetServerInfoResponseMessage, _Mapping]
        ] = ...,
        getSyncStatusResponse: _Optional[
            _Union[_rpc_pb2.GetSyncStatusResponseMessage, _Mapping]
        ] = ...,
        getDaaScoreTimestampEstimateResponse: _Optional[
            _Union[_rpc_pb2.GetDaaScoreTimestampEstimateResponseMessage, _Mapping]
        ] = ...,
        submitTransactionReplacementResponse: _Optional[
            _Union[_rpc_pb2.SubmitTransactionReplacementResponseMessage, _Mapping]
        ] = ...,
        getConnectionsResponse: _Optional[
            _Union[_rpc_pb2.GetConnectionsResponseMessage, _Mapping]
        ] = ...,
        getSystemInfoResponse: _Optional[
            _Union[_rpc_pb2.GetSystemInfoResponseMessage, _Mapping]
        ] = ...,
        getFeeEstimateResponse: _Optional[
            _Union[_rpc_pb2.GetFeeEstimateResponseMessage, _Mapping]
        ] = ...,
        getFeeEstimateExperimentalResponse: _Optional[
            _Union[_rpc_pb2.GetFeeEstimateExperimentalResponseMessage, _Mapping]
        ] = ...,
        getCurrentBlockColorResponse: _Optional[
            _Union[_rpc_pb2.GetCurrentBlockColorResponseMessage, _Mapping]
        ] = ...,
        GetUtxoReturnAddressResponse: _Optional[
            _Union[_rpc_pb2.GetUtxoReturnAddressResponseMessage, _Mapping]
        ] = ...,
    ) -> None: ...
