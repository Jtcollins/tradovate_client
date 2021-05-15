# CashBalanceLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**timestamp** | **datetime** |  | 
**trade_date** | [**TradeDate**](TradeDate.md) |  | 
**currency_id** | **int** |  | 
**amount** | **float** |  | 
**cash_change_type** | **str** | AutomaticReconciliation, BrokerageFee, CancelledPairedTrade, ClearingFee, Commission, DeskFee, EntitlementSubscription, ExchangeFee, FundTransaction, FundTransactionFee, IPFee, LiquidationFee, ManualAdjustment, MarketDataSubscription, NewSession, NfaFee, OptionsTrade, OrderRoutingFee, TradePaired, TradovateSubscription | 
**delta** | **float** |  | 
**id** | **int** |  | [optional] 
**realized_pn_l** | **float** |  | [optional] 
**week_realized_pn_l** | **float** |  | [optional] 
**fill_pair_id** | **int** |  | [optional] 
**fill_id** | **int** |  | [optional] 
**fund_transaction_id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


