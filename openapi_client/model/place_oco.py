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
    from openapi_client.model.restrained_order_version import RestrainedOrderVersion
    globals()['RestrainedOrderVersion'] = RestrainedOrderVersion


class PlaceOCO(ModelNormal):
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
        ('action',): {
            'BUY': "Buy",
            'SELL': "Sell",
        },
        ('order_type',): {
            'LIMIT': "Limit",
            'MIT': "MIT",
            'MARKET': "Market",
            'QTS': "QTS",
            'STOP': "Stop",
            'STOPLIMIT': "StopLimit",
            'TRAILINGSTOP': "TrailingStop",
            'TRAILINGSTOPLIMIT': "TrailingStopLimit",
        },
        ('time_in_force',): {
            'DAY': "Day",
            'FOK': "FOK",
            'GTC': "GTC",
            'GTD': "GTD",
            'IOC': "IOC",
        },
    }

    validations = {
        ('symbol',): {
            'max_length': 64,
        },
        ('order_qty',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('account_spec',): {
            'max_length': 64,
        },
        ('account_id',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('cl_ord_id',): {
            'max_length': 64,
        },
        ('max_show',): {
            'exclusive_minimum''inclusive_minimum': 0,
        },
        ('text',): {
            'max_length': 64,
        },
        ('custom_tag50',): {
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
            'action': (str,),  # noqa: E501
            'symbol': (str,),  # noqa: E501
            'order_qty': (int,),  # noqa: E501
            'order_type': (str,),  # noqa: E501
            'other': (RestrainedOrderVersion,),  # noqa: E501
            'account_spec': (str,),  # noqa: E501
            'account_id': (int,),  # noqa: E501
            'cl_ord_id': (str,),  # noqa: E501
            'price': (float,),  # noqa: E501
            'stop_price': (float,),  # noqa: E501
            'max_show': (int,),  # noqa: E501
            'peg_difference': (float,),  # noqa: E501
            'time_in_force': (str,),  # noqa: E501
            'expire_time': (datetime,),  # noqa: E501
            'text': (str,),  # noqa: E501
            'activation_time': (datetime,),  # noqa: E501
            'custom_tag50': (str,),  # noqa: E501
            'is_automated': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action': 'action',  # noqa: E501
        'symbol': 'symbol',  # noqa: E501
        'order_qty': 'orderQty',  # noqa: E501
        'order_type': 'orderType',  # noqa: E501
        'other': 'other',  # noqa: E501
        'account_spec': 'accountSpec',  # noqa: E501
        'account_id': 'accountId',  # noqa: E501
        'cl_ord_id': 'clOrdId',  # noqa: E501
        'price': 'price',  # noqa: E501
        'stop_price': 'stopPrice',  # noqa: E501
        'max_show': 'maxShow',  # noqa: E501
        'peg_difference': 'pegDifference',  # noqa: E501
        'time_in_force': 'timeInForce',  # noqa: E501
        'expire_time': 'expireTime',  # noqa: E501
        'text': 'text',  # noqa: E501
        'activation_time': 'activationTime',  # noqa: E501
        'custom_tag50': 'customTag50',  # noqa: E501
        'is_automated': 'isAutomated',  # noqa: E501
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
    def __init__(self, action, symbol, order_qty, order_type, other, *args, **kwargs):  # noqa: E501
        """PlaceOCO - a model defined in OpenAPI

        Args:
            action (str): Buy, Sell
            symbol (str):
            order_qty (int):
            order_type (str): Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit
            other (RestrainedOrderVersion):

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
            account_spec (str): [optional]  # noqa: E501
            account_id (int): [optional]  # noqa: E501
            cl_ord_id (str): [optional]  # noqa: E501
            price (float): [optional]  # noqa: E501
            stop_price (float): [optional]  # noqa: E501
            max_show (int): [optional]  # noqa: E501
            peg_difference (float): [optional]  # noqa: E501
            time_in_force (str): Day, FOK, GTC, GTD, IOC. [optional]  # noqa: E501
            expire_time (datetime): [optional]  # noqa: E501
            text (str): [optional]  # noqa: E501
            activation_time (datetime): [optional]  # noqa: E501
            custom_tag50 (str): [optional]  # noqa: E501
            is_automated (bool): [optional]  # noqa: E501
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

        self.action = action
        self.symbol = symbol
        self.order_qty = order_qty
        self.order_type = order_type
        self.other = other
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
