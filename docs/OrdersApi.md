# openapi_client.OrdersApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrdersApi.md#cancel_order) | **POST** /order/cancelorder | 
[**command_dependents**](OrdersApi.md#command_dependents) | **GET** /command/deps | 
[**command_item**](OrdersApi.md#command_item) | **GET** /command/item | 
[**command_items**](OrdersApi.md#command_items) | **GET** /command/items | 
[**command_l_dependents**](OrdersApi.md#command_l_dependents) | **GET** /command/ldeps | 
[**command_list**](OrdersApi.md#command_list) | **GET** /command/list | 
[**command_report_dependents**](OrdersApi.md#command_report_dependents) | **GET** /commandReport/deps | 
[**command_report_item**](OrdersApi.md#command_report_item) | **GET** /commandReport/item | 
[**command_report_items**](OrdersApi.md#command_report_items) | **GET** /commandReport/items | 
[**command_report_l_dependents**](OrdersApi.md#command_report_l_dependents) | **GET** /commandReport/ldeps | 
[**command_report_list**](OrdersApi.md#command_report_list) | **GET** /commandReport/list | 
[**execution_report_dependents**](OrdersApi.md#execution_report_dependents) | **GET** /executionReport/deps | 
[**execution_report_find**](OrdersApi.md#execution_report_find) | **GET** /executionReport/find | 
[**execution_report_item**](OrdersApi.md#execution_report_item) | **GET** /executionReport/item | 
[**execution_report_items**](OrdersApi.md#execution_report_items) | **GET** /executionReport/items | 
[**execution_report_l_dependents**](OrdersApi.md#execution_report_l_dependents) | **GET** /executionReport/ldeps | 
[**execution_report_list**](OrdersApi.md#execution_report_list) | **GET** /executionReport/list | 
[**execution_report_suggest**](OrdersApi.md#execution_report_suggest) | **GET** /executionReport/suggest | 
[**fill_dependents**](OrdersApi.md#fill_dependents) | **GET** /fill/deps | 
[**fill_fee_dependents**](OrdersApi.md#fill_fee_dependents) | **GET** /fillFee/deps | 
[**fill_fee_item**](OrdersApi.md#fill_fee_item) | **GET** /fillFee/item | 
[**fill_fee_items**](OrdersApi.md#fill_fee_items) | **GET** /fillFee/items | 
[**fill_fee_l_dependents**](OrdersApi.md#fill_fee_l_dependents) | **GET** /fillFee/ldeps | 
[**fill_fee_list**](OrdersApi.md#fill_fee_list) | **GET** /fillFee/list | 
[**fill_item**](OrdersApi.md#fill_item) | **GET** /fill/item | 
[**fill_items**](OrdersApi.md#fill_items) | **GET** /fill/items | 
[**fill_l_dependents**](OrdersApi.md#fill_l_dependents) | **GET** /fill/ldeps | 
[**fill_list**](OrdersApi.md#fill_list) | **GET** /fill/list | 
[**interrupt_order_strategy**](OrdersApi.md#interrupt_order_strategy) | **POST** /orderStrategy/interruptorderstrategy | 
[**liquidate_position**](OrdersApi.md#liquidate_position) | **POST** /order/liquidateposition | 
[**modify_order**](OrdersApi.md#modify_order) | **POST** /order/modifyorder | 
[**modify_order_strategy**](OrdersApi.md#modify_order_strategy) | **POST** /orderStrategy/modifyorderstrategy | 
[**order_dependents**](OrdersApi.md#order_dependents) | **GET** /order/deps | 
[**order_item**](OrdersApi.md#order_item) | **GET** /order/item | 
[**order_items**](OrdersApi.md#order_items) | **GET** /order/items | 
[**order_l_dependents**](OrdersApi.md#order_l_dependents) | **GET** /order/ldeps | 
[**order_list**](OrdersApi.md#order_list) | **GET** /order/list | 
[**order_strategy_dependents**](OrdersApi.md#order_strategy_dependents) | **GET** /orderStrategy/deps | 
[**order_strategy_item**](OrdersApi.md#order_strategy_item) | **GET** /orderStrategy/item | 
[**order_strategy_items**](OrdersApi.md#order_strategy_items) | **GET** /orderStrategy/items | 
[**order_strategy_l_dependents**](OrdersApi.md#order_strategy_l_dependents) | **GET** /orderStrategy/ldeps | 
[**order_strategy_link_dependents**](OrdersApi.md#order_strategy_link_dependents) | **GET** /orderStrategyLink/deps | 
[**order_strategy_link_item**](OrdersApi.md#order_strategy_link_item) | **GET** /orderStrategyLink/item | 
[**order_strategy_link_items**](OrdersApi.md#order_strategy_link_items) | **GET** /orderStrategyLink/items | 
[**order_strategy_link_l_dependents**](OrdersApi.md#order_strategy_link_l_dependents) | **GET** /orderStrategyLink/ldeps | 
[**order_strategy_link_list**](OrdersApi.md#order_strategy_link_list) | **GET** /orderStrategyLink/list | 
[**order_strategy_list**](OrdersApi.md#order_strategy_list) | **GET** /orderStrategy/list | 
[**order_version_dependents**](OrdersApi.md#order_version_dependents) | **GET** /orderVersion/deps | 
[**order_version_item**](OrdersApi.md#order_version_item) | **GET** /orderVersion/item | 
[**order_version_items**](OrdersApi.md#order_version_items) | **GET** /orderVersion/items | 
[**order_version_l_dependents**](OrdersApi.md#order_version_l_dependents) | **GET** /orderVersion/ldeps | 
[**order_version_list**](OrdersApi.md#order_version_list) | **GET** /orderVersion/list | 
[**place_oco**](OrdersApi.md#place_oco) | **POST** /order/placeoco | 
[**place_order**](OrdersApi.md#place_order) | **POST** /order/placeorder | 
[**place_oso**](OrdersApi.md#place_oso) | **POST** /order/placeoso | 
[**start_order_strategy**](OrdersApi.md#start_order_strategy) | **POST** /orderStrategy/startorderstrategy | 


# **cancel_order**
> CommandResult cancel_order(cancel_order)



 ## Make a request to cancel an order.

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_result import CommandResult
from openapi_client.model.cancel_order import CancelOrder
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    cancel_order = CancelOrder(
        order_id=0,
        cl_ord_id="cl_ord_id_example",
        activation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        custom_tag50="custom_tag50_example",
        is_automated=True,
    ) # CancelOrder | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cancel_order(cancel_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_order** | [**CancelOrder**](CancelOrder.md)|  |

### Return type

[**CommandResult**](CommandResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_dependents**
> [Command] command_dependents(masterid)



Retrieves all entities of Command type related to Order entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command import Command
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Order entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Order entity |

### Return type

[**[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_item**
> Command command_item(id)



Retrieves an entity of Command type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command import Command
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Command**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_items**
> [Command] command_items(ids)



Retrieves multiple entities of Command type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command import Command
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_l_dependents**
> [Command] command_l_dependents(masterids)



Retrieves all entities of Command type related to multiple entities of Order type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command import Command
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Order entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Order entities |

### Return type

[**[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_list**
> [Command] command_list()



Retrieves all entities of Command type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command import Command
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.command_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Command |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_dependents**
> [CommandReport] command_report_dependents(masterid)



Retrieves all entities of CommandReport type related to Command entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_report import CommandReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Command entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_report_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_report_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Command entity |

### Return type

[**[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_item**
> CommandReport command_report_item(id)



Retrieves an entity of CommandReport type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_report import CommandReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_report_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_report_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**CommandReport**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_items**
> [CommandReport] command_report_items(ids)



Retrieves multiple entities of CommandReport type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_report import CommandReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_report_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_report_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_l_dependents**
> [CommandReport] command_report_l_dependents(masterids)



Retrieves all entities of CommandReport type related to multiple entities of Command type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_report import CommandReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Command entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.command_report_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_report_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Command entities |

### Return type

[**[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_list**
> [CommandReport] command_report_list()



Retrieves all entities of CommandReport type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_report import CommandReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.command_report_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->command_report_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_dependents**
> [ExecutionReport] execution_report_dependents(masterid)



Retrieves all entities of ExecutionReport type related to Command entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Command entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execution_report_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Command entity |

### Return type

[**[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_find**
> ExecutionReport execution_report_find(name)



Retrieves an entity of ExecutionReport type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execution_report_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**ExecutionReport**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_item**
> ExecutionReport execution_report_item(id)



Retrieves an entity of ExecutionReport type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execution_report_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionReport**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_items**
> [ExecutionReport] execution_report_items(ids)



Retrieves multiple entities of ExecutionReport type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execution_report_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_l_dependents**
> [ExecutionReport] execution_report_l_dependents(masterids)



Retrieves all entities of ExecutionReport type related to multiple entities of Command type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Command entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execution_report_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Command entities |

### Return type

[**[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_list**
> [ExecutionReport] execution_report_list()



Retrieves all entities of ExecutionReport type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.execution_report_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_suggest**
> [ExecutionReport] execution_report_suggest(t, l)



Retrieves entities of ExecutionReport type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.execution_report import ExecutionReport
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execution_report_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->execution_report_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExecutionReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_dependents**
> [Fill] fill_dependents(masterid)



Retrieves all entities of Fill type related to Order entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill import Fill
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Order entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Order entity |

### Return type

[**[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_dependents**
> [FillFee] fill_fee_dependents(masterid)



Retrieves all entities of FillFee type related to Fill entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill_fee import FillFee
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Fill entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_fee_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_fee_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Fill entity |

### Return type

[**[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FillFee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_item**
> FillFee fill_fee_item(id)



Retrieves an entity of FillFee type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill_fee import FillFee
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_fee_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_fee_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**FillFee**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FillFee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_items**
> [FillFee] fill_fee_items(ids)



Retrieves multiple entities of FillFee type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill_fee import FillFee
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_fee_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_fee_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FillFee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_l_dependents**
> [FillFee] fill_fee_l_dependents(masterids)



Retrieves all entities of FillFee type related to multiple entities of Fill type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill_fee import FillFee
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Fill entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_fee_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_fee_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Fill entities |

### Return type

[**[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FillFee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_list**
> [FillFee] fill_fee_list()



Retrieves all entities of FillFee type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill_fee import FillFee
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.fill_fee_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_fee_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FillFee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_item**
> Fill fill_item(id)



Retrieves an entity of Fill type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill import Fill
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Fill**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_items**
> [Fill] fill_items(ids)



Retrieves multiple entities of Fill type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill import Fill
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_l_dependents**
> [Fill] fill_l_dependents(masterids)



Retrieves all entities of Fill type related to multiple entities of Order type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill import Fill
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Order entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fill_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Order entities |

### Return type

[**[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_list**
> [Fill] fill_list()



Retrieves all entities of Fill type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.fill import Fill
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.fill_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->fill_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interrupt_order_strategy**
> OrderStrategyStatusResponse interrupt_order_strategy(interrupt_order_strategy)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.interrupt_order_strategy import InterruptOrderStrategy
from openapi_client.model.order_strategy_status_response import OrderStrategyStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    interrupt_order_strategy = InterruptOrderStrategy(
        order_strategy_id=0,
    ) # InterruptOrderStrategy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.interrupt_order_strategy(interrupt_order_strategy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->interrupt_order_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interrupt_order_strategy** | [**InterruptOrderStrategy**](InterruptOrderStrategy.md)|  |

### Return type

[**OrderStrategyStatusResponse**](OrderStrategyStatusResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyStatusResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidate_position**
> PlaceOrderResult liquidate_position(liquidate_position)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.liquidate_position import LiquidatePosition
from openapi_client.model.place_order_result import PlaceOrderResult
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    liquidate_position = LiquidatePosition(
        account_id=0,
        contract_id=0,
        admin=True,
        custom_tag50="custom_tag50_example",
    ) # LiquidatePosition | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.liquidate_position(liquidate_position)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->liquidate_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liquidate_position** | [**LiquidatePosition**](LiquidatePosition.md)|  |

### Return type

[**PlaceOrderResult**](PlaceOrderResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PlaceOrderResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_order**
> CommandResult modify_order(modify_order)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.command_result import CommandResult
from openapi_client.model.modify_order import ModifyOrder
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    modify_order = ModifyOrder(
        order_id=0,
        cl_ord_id="cl_ord_id_example",
        order_qty=0,
        order_type="Limit",
        price=3.14,
        stop_price=3.14,
        max_show=0,
        peg_difference=3.14,
        time_in_force="Day",
        expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        text="text_example",
        activation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        custom_tag50="custom_tag50_example",
        is_automated=True,
    ) # ModifyOrder | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.modify_order(modify_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_order** | [**ModifyOrder**](ModifyOrder.md)|  |

### Return type

[**CommandResult**](CommandResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommandResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_order_strategy**
> OrderStrategyStatusResponse modify_order_strategy(modify_order_strategy)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_status_response import OrderStrategyStatusResponse
from openapi_client.model.modify_order_strategy import ModifyOrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    modify_order_strategy = ModifyOrderStrategy(
        order_strategy_id=0,
        command="command_example",
        custom_tag50="custom_tag50_example",
    ) # ModifyOrderStrategy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.modify_order_strategy(modify_order_strategy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->modify_order_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_order_strategy** | [**ModifyOrderStrategy**](ModifyOrderStrategy.md)|  |

### Return type

[**OrderStrategyStatusResponse**](OrderStrategyStatusResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyStatusResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_dependents**
> [Order] order_dependents(masterid)



Retrieves all entities of Order type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_item**
> Order order_item(id)



Retrieves an entity of Order type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Order**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_items**
> [Order] order_items(ids)



Retrieves multiple entities of Order type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_l_dependents**
> [Order] order_l_dependents(masterids)



Retrieves all entities of Order type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_list**
> [Order] order_list()



Retrieves all entities of Order type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order import Order
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.order_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_dependents**
> [OrderStrategy] order_strategy_dependents(masterid)



Retrieves all entities of OrderStrategy type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy import OrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_item**
> OrderStrategy order_strategy_item(id)



Retrieves an entity of OrderStrategy type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy import OrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**OrderStrategy**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_items**
> [OrderStrategy] order_strategy_items(ids)



Retrieves multiple entities of OrderStrategy type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy import OrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_l_dependents**
> [OrderStrategy] order_strategy_l_dependents(masterids)



Retrieves all entities of OrderStrategy type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy import OrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_dependents**
> [OrderStrategyLink] order_strategy_link_dependents(masterid)



Retrieves all entities of OrderStrategyLink type related to OrderStrategy entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_link import OrderStrategyLink
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of OrderStrategy entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_link_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_link_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of OrderStrategy entity |

### Return type

[**[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_item**
> OrderStrategyLink order_strategy_link_item(id)



Retrieves an entity of OrderStrategyLink type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_link import OrderStrategyLink
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_link_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_link_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**OrderStrategyLink**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_items**
> [OrderStrategyLink] order_strategy_link_items(ids)



Retrieves multiple entities of OrderStrategyLink type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_link import OrderStrategyLink
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_link_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_link_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_l_dependents**
> [OrderStrategyLink] order_strategy_link_l_dependents(masterids)



Retrieves all entities of OrderStrategyLink type related to multiple entities of OrderStrategy type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_link import OrderStrategyLink
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of OrderStrategy entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_strategy_link_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_link_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of OrderStrategy entities |

### Return type

[**[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_list**
> [OrderStrategyLink] order_strategy_link_list()



Retrieves all entities of OrderStrategyLink type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_link import OrderStrategyLink
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.order_strategy_link_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_link_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_list**
> [OrderStrategy] order_strategy_list()



Retrieves all entities of OrderStrategy type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy import OrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.order_strategy_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_strategy_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_dependents**
> [OrderVersion] order_version_dependents(masterid)



Retrieves all entities of OrderVersion type related to Order entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_version import OrderVersion
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterid = 1 # int | id of Order entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_version_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_version_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Order entity |

### Return type

[**[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_item**
> OrderVersion order_version_item(id)



Retrieves an entity of OrderVersion type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_version import OrderVersion
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_version_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_version_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**OrderVersion**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_items**
> [OrderVersion] order_version_items(ids)



Retrieves multiple entities of OrderVersion type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_version import OrderVersion
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_version_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_version_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_l_dependents**
> [OrderVersion] order_version_l_dependents(masterids)



Retrieves all entities of OrderVersion type related to multiple entities of Order type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_version import OrderVersion
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Order entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.order_version_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_version_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Order entities |

### Return type

[**[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_list**
> [OrderVersion] order_version_list()



Retrieves all entities of OrderVersion type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_version import OrderVersion
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.order_version_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->order_version_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_oco**
> PlaceOcoResult place_oco(place_oco)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.place_oco import PlaceOCO
from openapi_client.model.place_oco_result import PlaceOcoResult
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    place_oco = PlaceOCO(
        account_spec="account_spec_example",
        account_id=0,
        cl_ord_id="cl_ord_id_example",
        action="Buy",
        symbol="symbol_example",
        order_qty=0,
        order_type="Limit",
        price=3.14,
        stop_price=3.14,
        max_show=0,
        peg_difference=3.14,
        time_in_force="Day",
        expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        text="text_example",
        activation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        custom_tag50="custom_tag50_example",
        is_automated=True,
        other=RestrainedOrderVersion(
            action="Buy",
            cl_ord_id="cl_ord_id_example",
            order_type="Limit",
            price=3.14,
            stop_price=3.14,
            max_show=0,
            peg_difference=3.14,
            time_in_force="Day",
            expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            text="text_example",
        ),
    ) # PlaceOCO | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.place_oco(place_oco)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->place_oco: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_oco** | [**PlaceOCO**](PlaceOCO.md)|  |

### Return type

[**PlaceOcoResult**](PlaceOcoResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PlaceOcoResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> PlaceOrderResult place_order(place_order)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.place_order_result import PlaceOrderResult
from openapi_client.model.place_order import PlaceOrder
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    place_order = PlaceOrder(
        account_spec="account_spec_example",
        account_id=0,
        cl_ord_id="cl_ord_id_example",
        action="Buy",
        symbol="symbol_example",
        order_qty=0,
        order_type="Limit",
        price=3.14,
        stop_price=3.14,
        max_show=0,
        peg_difference=3.14,
        time_in_force="Day",
        expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        text="text_example",
        activation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        custom_tag50="custom_tag50_example",
        is_automated=True,
    ) # PlaceOrder | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.place_order(place_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->place_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_order** | [**PlaceOrder**](PlaceOrder.md)|  |

### Return type

[**PlaceOrderResult**](PlaceOrderResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PlaceOrderResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_oso**
> PlaceOsoResult place_oso(place_oso)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.place_oso_result import PlaceOsoResult
from openapi_client.model.place_oso import PlaceOSO
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    place_oso = PlaceOSO(
        account_spec="account_spec_example",
        account_id=0,
        cl_ord_id="cl_ord_id_example",
        action="Buy",
        symbol="symbol_example",
        order_qty=0,
        order_type="Limit",
        price=3.14,
        stop_price=3.14,
        max_show=0,
        peg_difference=3.14,
        time_in_force="Day",
        expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        text="text_example",
        activation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        custom_tag50="custom_tag50_example",
        is_automated=True,
        bracket1=RestrainedOrderVersion(
            action="Buy",
            cl_ord_id="cl_ord_id_example",
            order_type="Limit",
            price=3.14,
            stop_price=3.14,
            max_show=0,
            peg_difference=3.14,
            time_in_force="Day",
            expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            text="text_example",
        ),
        bracket2=RestrainedOrderVersion(
            action="Buy",
            cl_ord_id="cl_ord_id_example",
            order_type="Limit",
            price=3.14,
            stop_price=3.14,
            max_show=0,
            peg_difference=3.14,
            time_in_force="Day",
            expire_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            text="text_example",
        ),
    ) # PlaceOSO | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.place_oso(place_oso)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->place_oso: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_oso** | [**PlaceOSO**](PlaceOSO.md)|  |

### Return type

[**PlaceOsoResult**](PlaceOsoResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PlaceOsoResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_order_strategy**
> OrderStrategyStatusResponse start_order_strategy(start_order_strategy)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order_strategy_status_response import OrderStrategyStatusResponse
from openapi_client.model.start_order_strategy import StartOrderStrategy
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_access_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    start_order_strategy = StartOrderStrategy(
        account_id=0,
        account_spec="account_spec_example",
        symbol="symbol_example",
        order_strategy_type_id=0,
        action="Buy",
        params="params_example",
        uuid="uuid_example",
        custom_tag50="custom_tag50_example",
    ) # StartOrderStrategy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_order_strategy(start_order_strategy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->start_order_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_order_strategy** | [**StartOrderStrategy**](StartOrderStrategy.md)|  |

### Return type

[**OrderStrategyStatusResponse**](OrderStrategyStatusResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStrategyStatusResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

