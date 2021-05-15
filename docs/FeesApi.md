# openapi_client.FeesApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_data_subscription_exchange_scope_find**](FeesApi.md#market_data_subscription_exchange_scope_find) | **GET** /marketDataSubscriptionExchangeScope/find | 
[**market_data_subscription_exchange_scope_item**](FeesApi.md#market_data_subscription_exchange_scope_item) | **GET** /marketDataSubscriptionExchangeScope/item | 
[**market_data_subscription_exchange_scope_items**](FeesApi.md#market_data_subscription_exchange_scope_items) | **GET** /marketDataSubscriptionExchangeScope/items | 
[**market_data_subscription_exchange_scope_list**](FeesApi.md#market_data_subscription_exchange_scope_list) | **GET** /marketDataSubscriptionExchangeScope/list | 
[**market_data_subscription_exchange_scope_suggest**](FeesApi.md#market_data_subscription_exchange_scope_suggest) | **GET** /marketDataSubscriptionExchangeScope/suggest | 
[**market_data_subscription_plan_find**](FeesApi.md#market_data_subscription_plan_find) | **GET** /marketDataSubscriptionPlan/find | 
[**market_data_subscription_plan_item**](FeesApi.md#market_data_subscription_plan_item) | **GET** /marketDataSubscriptionPlan/item | 
[**market_data_subscription_plan_items**](FeesApi.md#market_data_subscription_plan_items) | **GET** /marketDataSubscriptionPlan/items | 
[**market_data_subscription_plan_list**](FeesApi.md#market_data_subscription_plan_list) | **GET** /marketDataSubscriptionPlan/list | 
[**market_data_subscription_plan_suggest**](FeesApi.md#market_data_subscription_plan_suggest) | **GET** /marketDataSubscriptionPlan/suggest | 
[**tradovate_subscription_plan_find**](FeesApi.md#tradovate_subscription_plan_find) | **GET** /tradovateSubscriptionPlan/find | 
[**tradovate_subscription_plan_item**](FeesApi.md#tradovate_subscription_plan_item) | **GET** /tradovateSubscriptionPlan/item | 
[**tradovate_subscription_plan_items**](FeesApi.md#tradovate_subscription_plan_items) | **GET** /tradovateSubscriptionPlan/items | 
[**tradovate_subscription_plan_list**](FeesApi.md#tradovate_subscription_plan_list) | **GET** /tradovateSubscriptionPlan/list | 
[**tradovate_subscription_plan_suggest**](FeesApi.md#tradovate_subscription_plan_suggest) | **GET** /tradovateSubscriptionPlan/suggest | 


# **market_data_subscription_exchange_scope_find**
> MarketDataSubscriptionExchangeScope market_data_subscription_exchange_scope_find(name)



Retrieves an entity of MarketDataSubscriptionExchangeScope type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_exchange_scope import MarketDataSubscriptionExchangeScope
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
    api_instance = fees_api.FeesApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_exchange_scope_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_exchange_scope_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**MarketDataSubscriptionExchangeScope**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionExchangeScope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_item**
> MarketDataSubscriptionExchangeScope market_data_subscription_exchange_scope_item(id)



Retrieves an entity of MarketDataSubscriptionExchangeScope type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_exchange_scope import MarketDataSubscriptionExchangeScope
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
    api_instance = fees_api.FeesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_exchange_scope_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_exchange_scope_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**MarketDataSubscriptionExchangeScope**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionExchangeScope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_items**
> [MarketDataSubscriptionExchangeScope] market_data_subscription_exchange_scope_items(ids)



Retrieves multiple entities of MarketDataSubscriptionExchangeScope type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_exchange_scope import MarketDataSubscriptionExchangeScope
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
    api_instance = fees_api.FeesApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_exchange_scope_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_exchange_scope_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[MarketDataSubscriptionExchangeScope]**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionExchangeScope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_list**
> [MarketDataSubscriptionExchangeScope] market_data_subscription_exchange_scope_list()



Retrieves all entities of MarketDataSubscriptionExchangeScope type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_exchange_scope import MarketDataSubscriptionExchangeScope
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
    api_instance = fees_api.FeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.market_data_subscription_exchange_scope_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_exchange_scope_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[MarketDataSubscriptionExchangeScope]**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionExchangeScope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_suggest**
> [MarketDataSubscriptionExchangeScope] market_data_subscription_exchange_scope_suggest(t, l)



Retrieves entities of MarketDataSubscriptionExchangeScope type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_exchange_scope import MarketDataSubscriptionExchangeScope
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
    api_instance = fees_api.FeesApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_exchange_scope_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_exchange_scope_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[MarketDataSubscriptionExchangeScope]**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionExchangeScope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_find**
> MarketDataSubscriptionPlan market_data_subscription_plan_find(name)



Retrieves an entity of MarketDataSubscriptionPlan type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_plan import MarketDataSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_plan_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_plan_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**MarketDataSubscriptionPlan**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_item**
> MarketDataSubscriptionPlan market_data_subscription_plan_item(id)



Retrieves an entity of MarketDataSubscriptionPlan type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_plan import MarketDataSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_plan_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_plan_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**MarketDataSubscriptionPlan**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_items**
> [MarketDataSubscriptionPlan] market_data_subscription_plan_items(ids)



Retrieves multiple entities of MarketDataSubscriptionPlan type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_plan import MarketDataSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_plan_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_plan_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[MarketDataSubscriptionPlan]**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_list**
> [MarketDataSubscriptionPlan] market_data_subscription_plan_list()



Retrieves all entities of MarketDataSubscriptionPlan type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_plan import MarketDataSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.market_data_subscription_plan_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_plan_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[MarketDataSubscriptionPlan]**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_suggest**
> [MarketDataSubscriptionPlan] market_data_subscription_plan_suggest(t, l)



Retrieves entities of MarketDataSubscriptionPlan type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.market_data_subscription_plan import MarketDataSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.market_data_subscription_plan_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->market_data_subscription_plan_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[MarketDataSubscriptionPlan]**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketDataSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_find**
> TradovateSubscriptionPlan tradovate_subscription_plan_find(name)



Retrieves an entity of TradovateSubscriptionPlan type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.tradovate_subscription_plan import TradovateSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tradovate_subscription_plan_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->tradovate_subscription_plan_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**TradovateSubscriptionPlan**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradovateSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_item**
> TradovateSubscriptionPlan tradovate_subscription_plan_item(id)



Retrieves an entity of TradovateSubscriptionPlan type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.tradovate_subscription_plan import TradovateSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tradovate_subscription_plan_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->tradovate_subscription_plan_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**TradovateSubscriptionPlan**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradovateSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_items**
> [TradovateSubscriptionPlan] tradovate_subscription_plan_items(ids)



Retrieves multiple entities of TradovateSubscriptionPlan type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.tradovate_subscription_plan import TradovateSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tradovate_subscription_plan_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->tradovate_subscription_plan_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[TradovateSubscriptionPlan]**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradovateSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_list**
> [TradovateSubscriptionPlan] tradovate_subscription_plan_list()



Retrieves all entities of TradovateSubscriptionPlan type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.tradovate_subscription_plan import TradovateSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.tradovate_subscription_plan_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->tradovate_subscription_plan_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[TradovateSubscriptionPlan]**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradovateSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_suggest**
> [TradovateSubscriptionPlan] tradovate_subscription_plan_suggest(t, l)



Retrieves entities of TradovateSubscriptionPlan type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import fees_api
from openapi_client.model.tradovate_subscription_plan import TradovateSubscriptionPlan
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
    api_instance = fees_api.FeesApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tradovate_subscription_plan_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeesApi->tradovate_subscription_plan_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[TradovateSubscriptionPlan]**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TradovateSubscriptionPlan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

