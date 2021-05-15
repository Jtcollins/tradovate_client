# openapi_client.AccountingApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_dependents**](AccountingApi.md#account_dependents) | **GET** /account/deps | 
[**account_find**](AccountingApi.md#account_find) | **GET** /account/find | 
[**account_item**](AccountingApi.md#account_item) | **GET** /account/item | 
[**account_items**](AccountingApi.md#account_items) | **GET** /account/items | 
[**account_l_dependents**](AccountingApi.md#account_l_dependents) | **GET** /account/ldeps | 
[**account_list**](AccountingApi.md#account_list) | **GET** /account/list | 
[**account_suggest**](AccountingApi.md#account_suggest) | **GET** /account/suggest | 
[**cash_balance_dependents**](AccountingApi.md#cash_balance_dependents) | **GET** /cashBalance/deps | 
[**cash_balance_item**](AccountingApi.md#cash_balance_item) | **GET** /cashBalance/item | 
[**cash_balance_items**](AccountingApi.md#cash_balance_items) | **GET** /cashBalance/items | 
[**cash_balance_l_dependents**](AccountingApi.md#cash_balance_l_dependents) | **GET** /cashBalance/ldeps | 
[**cash_balance_list**](AccountingApi.md#cash_balance_list) | **GET** /cashBalance/list | 
[**cash_balance_log_dependents**](AccountingApi.md#cash_balance_log_dependents) | **GET** /cashBalanceLog/deps | 
[**cash_balance_log_item**](AccountingApi.md#cash_balance_log_item) | **GET** /cashBalanceLog/item | 
[**cash_balance_log_items**](AccountingApi.md#cash_balance_log_items) | **GET** /cashBalanceLog/items | 
[**cash_balance_log_l_dependents**](AccountingApi.md#cash_balance_log_l_dependents) | **GET** /cashBalanceLog/ldeps | 
[**get_cash_balance_snapshot**](AccountingApi.md#get_cash_balance_snapshot) | **POST** /cashBalance/getcashbalancesnapshot | 
[**margin_snapshot_dependents**](AccountingApi.md#margin_snapshot_dependents) | **GET** /marginSnapshot/deps | 
[**margin_snapshot_item**](AccountingApi.md#margin_snapshot_item) | **GET** /marginSnapshot/item | 
[**margin_snapshot_items**](AccountingApi.md#margin_snapshot_items) | **GET** /marginSnapshot/items | 
[**margin_snapshot_l_dependents**](AccountingApi.md#margin_snapshot_l_dependents) | **GET** /marginSnapshot/ldeps | 
[**margin_snapshot_list**](AccountingApi.md#margin_snapshot_list) | **GET** /marginSnapshot/list | 
[**trading_permission_dependents**](AccountingApi.md#trading_permission_dependents) | **GET** /tradingPermission/deps | 
[**trading_permission_item**](AccountingApi.md#trading_permission_item) | **GET** /tradingPermission/item | 
[**trading_permission_items**](AccountingApi.md#trading_permission_items) | **GET** /tradingPermission/items | 
[**trading_permission_l_dependents**](AccountingApi.md#trading_permission_l_dependents) | **GET** /tradingPermission/ldeps | 
[**trading_permission_list**](AccountingApi.md#trading_permission_list) | **GET** /tradingPermission/list | 


# **account_dependents**
> [Account] account_dependents(masterid)



Retrieves all entities of Account type related to User entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterid = 1 # int | id of User entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity |

### Return type

[**[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_find**
> Account account_find(name)



Retrieves an entity of Account type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Account**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_item**
> Account account_item(id)



Retrieves an entity of Account type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Account**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_items**
> [Account] account_items(ids)



Retrieves multiple entities of Account type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_l_dependents**
> [Account] account_l_dependents(masterids)



Retrieves all entities of Account type related to multiple entities of User type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of User entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of User entities |

### Return type

[**[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_list**
> [Account] account_list()



Retrieves all entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.account_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_suggest**
> [Account] account_suggest(t, l)



Retrieves entities of Account type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.account import Account
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
    api_instance = accounting_api.AccountingApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->account_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_dependents**
> [CashBalance] cash_balance_dependents(masterid)



Retrieves all entities of CashBalance type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance import CashBalance
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_item**
> CashBalance cash_balance_item(id)



Retrieves an entity of CashBalance type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance import CashBalance
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
    api_instance = accounting_api.AccountingApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**CashBalance**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_items**
> [CashBalance] cash_balance_items(ids)



Retrieves multiple entities of CashBalance type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance import CashBalance
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
    api_instance = accounting_api.AccountingApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_l_dependents**
> [CashBalance] cash_balance_l_dependents(masterids)



Retrieves all entities of CashBalance type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance import CashBalance
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_list**
> [CashBalance] cash_balance_list()



Retrieves all entities of CashBalance type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance import CashBalance
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
    api_instance = accounting_api.AccountingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.cash_balance_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_dependents**
> [CashBalanceLog] cash_balance_log_dependents(masterid)



Retrieves all entities of CashBalanceLog type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance_log import CashBalanceLog
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_log_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_log_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[CashBalanceLog]**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalanceLog |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_item**
> CashBalanceLog cash_balance_log_item(id)



Retrieves an entity of CashBalanceLog type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance_log import CashBalanceLog
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
    api_instance = accounting_api.AccountingApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_log_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_log_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**CashBalanceLog**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalanceLog |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_items**
> [CashBalanceLog] cash_balance_log_items(ids)



Retrieves multiple entities of CashBalanceLog type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance_log import CashBalanceLog
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
    api_instance = accounting_api.AccountingApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_log_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_log_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[CashBalanceLog]**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalanceLog |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_l_dependents**
> [CashBalanceLog] cash_balance_log_l_dependents(masterids)



Retrieves all entities of CashBalanceLog type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance_log import CashBalanceLog
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cash_balance_log_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->cash_balance_log_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[CashBalanceLog]**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalanceLog |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_balance_snapshot**
> CashBalanceSnapshot get_cash_balance_snapshot(get_cash_balance_snapshot)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.cash_balance_snapshot import CashBalanceSnapshot
from openapi_client.model.get_cash_balance_snapshot import GetCashBalanceSnapshot
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
    api_instance = accounting_api.AccountingApi(api_client)
    get_cash_balance_snapshot = GetCashBalanceSnapshot(
        account_id=0,
    ) # GetCashBalanceSnapshot | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cash_balance_snapshot(get_cash_balance_snapshot)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->get_cash_balance_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cash_balance_snapshot** | [**GetCashBalanceSnapshot**](GetCashBalanceSnapshot.md)|  |

### Return type

[**CashBalanceSnapshot**](CashBalanceSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CashBalanceSnapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_dependents**
> [MarginSnapshot] margin_snapshot_dependents(masterid)



Retrieves all entities of MarginSnapshot type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.margin_snapshot import MarginSnapshot
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.margin_snapshot_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->margin_snapshot_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarginSnapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_item**
> MarginSnapshot margin_snapshot_item(id)



Retrieves an entity of MarginSnapshot type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.margin_snapshot import MarginSnapshot
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
    api_instance = accounting_api.AccountingApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.margin_snapshot_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->margin_snapshot_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**MarginSnapshot**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarginSnapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_items**
> [MarginSnapshot] margin_snapshot_items(ids)



Retrieves multiple entities of MarginSnapshot type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.margin_snapshot import MarginSnapshot
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
    api_instance = accounting_api.AccountingApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.margin_snapshot_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->margin_snapshot_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarginSnapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_l_dependents**
> [MarginSnapshot] margin_snapshot_l_dependents(masterids)



Retrieves all entities of MarginSnapshot type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.margin_snapshot import MarginSnapshot
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.margin_snapshot_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->margin_snapshot_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarginSnapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_list**
> [MarginSnapshot] margin_snapshot_list()



Retrieves all entities of MarginSnapshot type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.margin_snapshot import MarginSnapshot
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
    api_instance = accounting_api.AccountingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.margin_snapshot_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->margin_snapshot_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarginSnapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_dependents**
> [TradingPermission] trading_permission_dependents(masterid)



Retrieves all entities of TradingPermission type related to User entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.trading_permission import TradingPermission
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterid = 1 # int | id of User entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trading_permission_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->trading_permission_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity |

### Return type

[**[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradingPermission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_item**
> TradingPermission trading_permission_item(id)



Retrieves an entity of TradingPermission type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.trading_permission import TradingPermission
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
    api_instance = accounting_api.AccountingApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trading_permission_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->trading_permission_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**TradingPermission**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradingPermission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_items**
> [TradingPermission] trading_permission_items(ids)



Retrieves multiple entities of TradingPermission type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.trading_permission import TradingPermission
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
    api_instance = accounting_api.AccountingApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trading_permission_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->trading_permission_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradingPermission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_l_dependents**
> [TradingPermission] trading_permission_l_dependents(masterids)



Retrieves all entities of TradingPermission type related to multiple entities of User type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.trading_permission import TradingPermission
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
    api_instance = accounting_api.AccountingApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of User entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trading_permission_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->trading_permission_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of User entities |

### Return type

[**[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradingPermission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_list**
> [TradingPermission] trading_permission_list()



Retrieves all entities of TradingPermission type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import accounting_api
from openapi_client.model.trading_permission import TradingPermission
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
    api_instance = accounting_api.AccountingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.trading_permission_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountingApi->trading_permission_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradingPermission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

