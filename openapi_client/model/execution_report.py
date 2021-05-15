"""
    Tradovate API

    Tradovate API provides an access to the complete set of robust Tradovate functionality.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.trade_date import TradeDate
    globals()['TradeDate'] = TradeDate


class ExecutionReport(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('exec_type',): {
            'CANCELED': "Canceled",
            'COMPLETED': "Completed",
            'DONEFORDAY': "DoneForDay",
            'EXPIRED': "Expired",
            'NEW': "New",
            'ORDERSTATUS': "OrderStatus",
            'PENDINGCANCEL': "PendingCancel",
            'PENDINGNEW': "PendingNew",
            'PENDINGREPLACE': "PendingReplace",
            'REJECTED': "Rejected",
            'REPLACED': "Replaced",
            'STOPPED': "Stopped",
            'SUSPENDED': "Suspended",
            'TRADE': "Trade",
            'TRADECANCEL': "TradeCancel",
            'TRADECORRECT': "TradeCorrect",
        },
        ('action',): {
            'BUY': "Buy",
            'SELL': "Sell",
        },
        ('ord_status',): {
            'CANCELED': "Canceled",
            'COMPLETED': "Completed",
            'EXPIRED': "Expired",
            'FILLED': "Filled",
            'PENDINGCANCEL': "PendingCancel",
            'PENDINGNEW': "PendingNew",
            'PENDINGREPLACE': "PendingReplace",
            'REJECTED': "Rejected",
            'SUSPENDED': "Suspended",
            'UNKNOWN': "Unknown",
            'WORKING': "Working",
        },
        ('reject_reason',): {
            'ACCOUNTCLOSED': "AccountClosed",
            'ADVANCEDTRAILINGSTOPUNSUPPORTED': "AdvancedTrailingStopUnsupported",
            'ANOTHERCOMMANDPENDING': "AnotherCommandPending",
            'BACKMONTHPROHIBITED': "BackMonthProhibited",
            'EXECUTIONPROVIDERNOTCONFIGURED': "ExecutionProviderNotConfigured",
            'EXECUTIONPROVIDERUNAVAILABLE': "ExecutionProviderUnavailable",
            'INVALIDCONTRACT': "InvalidContract",
            'INVALIDPRICE': "InvalidPrice",
            'LIQUIDATIONONLY': "LiquidationOnly",
            'LIQUIDATIONONLYBEFOREEXPIRATION': "LiquidationOnlyBeforeExpiration",
            'MAXORDERQTYISNOTSPECIFIED': "MaxOrderQtyIsNotSpecified",
            'MAXORDERQTYLIMITREACHED': "MaxOrderQtyLimitReached",
            'MAXPOSLIMITMISCONFIGURED': "MaxPosLimitMisconfigured",
            'MAXPOSLIMITREACHED': "MaxPosLimitReached",
            'MAXTOTALPOSLIMITREACHED': "MaxTotalPosLimitReached",
            'MULTIPLEACCOUNTPLANREQUIRED': "MultipleAccountPlanRequired",
            'NOQUOTE': "NoQuote",
            'NOTENOUGHLIQUIDITY': "NotEnoughLiquidity",
            'OTHEREXECUTIONRELATED': "OtherExecutionRelated",
            'PARENTREJECTED': "ParentRejected",
            'RISKCHECKTIMEOUT': "RiskCheckTimeout",
            'SESSIONCLOSED': "SessionClosed",
            'SUCCESS': "Success",
            'TOOLATE': "TooLate",
            'TRADINGLOCKED': "TradingLocked",
            'TRAILINGSTOPNONORDERQTYMODIFY': "TrailingStopNonOrderQtyModify",
            'UNAUTHORIZED': "Unauthorized",
            'UNKNOWNREASON': "UnknownReason",
            'UNSUPPORTED': "Unsupported",
        },
    }

    validations = {
        ('command_id',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('name',): {
            'max_length': 64,
        },
        ('account_id',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('contract_id',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('order_id',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('exec_ref_id',): {
            'max_length': 64,
        },
        ('text',): {
            'max_length': 8192,
        },
        ('exchange_order_id',): {
            'max_length': 64,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'command_id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'account_id': (int,),  # noqa: E501
            'contract_id': (int,),  # noqa: E501
            'timestamp': (datetime,),  # noqa: E501
            'order_id': (int,),  # noqa: E501
            'exec_type': (str,),  # noqa: E501
            'action': (str,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'trade_date': (TradeDate,),  # noqa: E501
            'exec_ref_id': (str,),  # noqa: E501
            'ord_status': (str,),  # noqa: E501
            'cum_qty': (int,),  # noqa: E501
            'avg_px': (float,),  # noqa: E501
            'last_qty': (int,),  # noqa: E501
            'last_px': (float,),  # noqa: E501
            'reject_reason': (str,),  # noqa: E501
            'text': (str,),  # noqa: E501
            'exchange_order_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'command_id': 'commandId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'account_id': 'accountId',  # noqa: E501
        'contract_id': 'contractId',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'order_id': 'orderId',  # noqa: E501
        'exec_type': 'execType',  # noqa: E501
        'action': 'action',  # noqa: E501
        'id': 'id',  # noqa: E501
        'trade_date': 'tradeDate',  # noqa: E501
        'exec_ref_id': 'execRefId',  # noqa: E501
        'ord_status': 'ordStatus',  # noqa: E501
        'cum_qty': 'cumQty',  # noqa: E501
        'avg_px': 'avgPx',  # noqa: E501
        'last_qty': 'lastQty',  # noqa: E501
        'last_px': 'lastPx',  # noqa: E501
        'reject_reason': 'rejectReason',  # noqa: E501
        'text': 'text',  # noqa: E501
        'exchange_order_id': 'exchangeOrderId',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, command_id, name, account_id, contract_id, timestamp, order_id, exec_type, action, *args, **kwargs):  # noqa: E501
        """ExecutionReport - a model defined in OpenAPI

        Args:
            command_id (int):
            name (str):
            account_id (int):
            contract_id (int):
            timestamp (datetime):
            order_id (int):
            exec_type (str): Canceled, Completed, DoneForDay, Expired, New, OrderStatus, PendingCancel, PendingNew, PendingReplace, Rejected, Replaced, Stopped, Suspended, Trade, TradeCancel, TradeCorrect
            action (str): Buy, Sell

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): [optional]  # noqa: E501
            trade_date (TradeDate): [optional]  # noqa: E501
            exec_ref_id (str): [optional]  # noqa: E501
            ord_status (str): Canceled, Completed, Expired, Filled, PendingCancel, PendingNew, PendingReplace, Rejected, Suspended, Unknown, Working. [optional]  # noqa: E501
            cum_qty (int): [optional]  # noqa: E501
            avg_px (float): [optional]  # noqa: E501
            last_qty (int): [optional]  # noqa: E501
            last_px (float): [optional]  # noqa: E501
            reject_reason (str): AccountClosed, AdvancedTrailingStopUnsupported, AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable, InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified, MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached, MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected, RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized, UnknownReason, Unsupported. [optional]  # noqa: E501
            text (str): [optional]  # noqa: E501
            exchange_order_id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.command_id = command_id
        self.name = name
        self.account_id = account_id
        self.contract_id = contract_id
        self.timestamp = timestamp
        self.order_id = order_id
        self.exec_type = exec_type
        self.action = action
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
