# ExecutionReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_id** | **int** |  | 
**name** | **str** |  | 
**account_id** | **int** |  | 
**contract_id** | **int** |  | 
**timestamp** | **datetime** |  | 
**order_id** | **int** |  | 
**exec_type** | **str** | Canceled, Completed, DoneForDay, Expired, New, OrderStatus, PendingCancel, PendingNew, PendingReplace, Rejected, Replaced, Stopped, Suspended, Trade, TradeCancel, TradeCorrect | 
**action** | **str** | Buy, Sell | 
**id** | **int** |  | [optional] 
**trade_date** | [**TradeDate**](TradeDate.md) |  | [optional] 
**exec_ref_id** | **str** |  | [optional] 
**ord_status** | **str** | Canceled, Completed, Expired, Filled, PendingCancel, PendingNew, PendingReplace, Rejected, Suspended, Unknown, Working | [optional] 
**cum_qty** | **int** |  | [optional] 
**avg_px** | **float** |  | [optional] 
**last_qty** | **int** |  | [optional] 
**last_px** | **float** |  | [optional] 
**reject_reason** | **str** | AccountClosed, AdvancedTrailingStopUnsupported, AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable, InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified, MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached, MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected, RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized, UnknownReason, Unsupported | [optional] 
**text** | **str** |  | [optional] 
**exchange_order_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


