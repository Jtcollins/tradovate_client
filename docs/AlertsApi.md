# openapi_client.AlertsApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_alert_signal_dependents**](AlertsApi.md#admin_alert_signal_dependents) | **GET** /adminAlertSignal/deps | 
[**admin_alert_signal_item**](AlertsApi.md#admin_alert_signal_item) | **GET** /adminAlertSignal/item | 
[**admin_alert_signal_items**](AlertsApi.md#admin_alert_signal_items) | **GET** /adminAlertSignal/items | 
[**admin_alert_signal_l_dependents**](AlertsApi.md#admin_alert_signal_l_dependents) | **GET** /adminAlertSignal/ldeps | 
[**admin_alert_signal_list**](AlertsApi.md#admin_alert_signal_list) | **GET** /adminAlertSignal/list | 
[**alert_dependents**](AlertsApi.md#alert_dependents) | **GET** /alert/deps | 
[**alert_item**](AlertsApi.md#alert_item) | **GET** /alert/item | 
[**alert_items**](AlertsApi.md#alert_items) | **GET** /alert/items | 
[**alert_l_dependents**](AlertsApi.md#alert_l_dependents) | **GET** /alert/ldeps | 
[**alert_list**](AlertsApi.md#alert_list) | **GET** /alert/list | 
[**alert_signal_dependents**](AlertsApi.md#alert_signal_dependents) | **GET** /alertSignal/deps | 
[**alert_signal_item**](AlertsApi.md#alert_signal_item) | **GET** /alertSignal/item | 
[**alert_signal_items**](AlertsApi.md#alert_signal_items) | **GET** /alertSignal/items | 
[**alert_signal_l_dependents**](AlertsApi.md#alert_signal_l_dependents) | **GET** /alertSignal/ldeps | 
[**alert_signal_list**](AlertsApi.md#alert_signal_list) | **GET** /alertSignal/list | 
[**complete_alert_signal**](AlertsApi.md#complete_alert_signal) | **POST** /adminAlertSignal/completealertsignal | 
[**create_alert**](AlertsApi.md#create_alert) | **POST** /alert/createalert | 
[**delete_alert**](AlertsApi.md#delete_alert) | **POST** /alert/deletealert | 
[**dismiss_alert**](AlertsApi.md#dismiss_alert) | **POST** /alert/dismissalert | 
[**mark_read_alert_signal**](AlertsApi.md#mark_read_alert_signal) | **POST** /alert/markreadalertsignal | 
[**modify_alert**](AlertsApi.md#modify_alert) | **POST** /alert/modifyalert | 
[**reset_alert**](AlertsApi.md#reset_alert) | **POST** /alert/resetalert | 
[**take_alert_signal_ownership**](AlertsApi.md#take_alert_signal_ownership) | **POST** /adminAlertSignal/takealertsignalownership | 


# **admin_alert_signal_dependents**
> [AdminAlertSignal] admin_alert_signal_dependents(masterid)



Retrieves all entities of AdminAlertSignal type related to AdminAlert entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal import AdminAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    masterid = 1 # int | id of AdminAlert entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_alert_signal_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->admin_alert_signal_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of AdminAlert entity |

### Return type

[**[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_item**
> AdminAlertSignal admin_alert_signal_item(id)



Retrieves an entity of AdminAlertSignal type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal import AdminAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_alert_signal_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->admin_alert_signal_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**AdminAlertSignal**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_items**
> [AdminAlertSignal] admin_alert_signal_items(ids)



Retrieves multiple entities of AdminAlertSignal type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal import AdminAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_alert_signal_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->admin_alert_signal_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_l_dependents**
> [AdminAlertSignal] admin_alert_signal_l_dependents(masterids)



Retrieves all entities of AdminAlertSignal type related to multiple entities of AdminAlert type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal import AdminAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of AdminAlert entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_alert_signal_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->admin_alert_signal_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of AdminAlert entities |

### Return type

[**[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_list**
> [AdminAlertSignal] admin_alert_signal_list()



Retrieves all entities of AdminAlertSignal type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal import AdminAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.admin_alert_signal_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->admin_alert_signal_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_dependents**
> [Alert] alert_dependents(masterid)



Retrieves all entities of Alert type related to User entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert import Alert
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
    api_instance = alerts_api.AlertsApi(api_client)
    masterid = 1 # int | id of User entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity |

### Return type

[**[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_item**
> Alert alert_item(id)



Retrieves an entity of Alert type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert import Alert
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
    api_instance = alerts_api.AlertsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Alert**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_items**
> [Alert] alert_items(ids)



Retrieves multiple entities of Alert type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert import Alert
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
    api_instance = alerts_api.AlertsApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_l_dependents**
> [Alert] alert_l_dependents(masterids)



Retrieves all entities of Alert type related to multiple entities of User type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert import Alert
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
    api_instance = alerts_api.AlertsApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of User entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of User entities |

### Return type

[**[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_list**
> [Alert] alert_list()



Retrieves all entities of Alert type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert import Alert
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
    api_instance = alerts_api.AlertsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.alert_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_dependents**
> [AlertSignal] alert_signal_dependents(masterid)



Retrieves all entities of AlertSignal type related to Alert entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_signal import AlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    masterid = 1 # int | id of Alert entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_signal_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_signal_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Alert entity |

### Return type

[**[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_item**
> AlertSignal alert_signal_item(id)



Retrieves an entity of AlertSignal type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_signal import AlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_signal_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_signal_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**AlertSignal**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_items**
> [AlertSignal] alert_signal_items(ids)



Retrieves multiple entities of AlertSignal type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_signal import AlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_signal_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_signal_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_l_dependents**
> [AlertSignal] alert_signal_l_dependents(masterids)



Retrieves all entities of AlertSignal type related to multiple entities of Alert type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_signal import AlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Alert entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.alert_signal_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_signal_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Alert entities |

### Return type

[**[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_list**
> [AlertSignal] alert_signal_list()



Retrieves all entities of AlertSignal type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_signal import AlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.alert_signal_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alert_signal_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertSignal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_alert_signal**
> AdminAlertSignalResponse complete_alert_signal(complete_alert_signal)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal_response import AdminAlertSignalResponse
from openapi_client.model.complete_alert_signal import CompleteAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    complete_alert_signal = CompleteAlertSignal(
        admin_alert_signal_id=0,
    ) # CompleteAlertSignal | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.complete_alert_signal(complete_alert_signal)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->complete_alert_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complete_alert_signal** | [**CompleteAlertSignal**](CompleteAlertSignal.md)|  |

### Return type

[**AdminAlertSignalResponse**](AdminAlertSignalResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignalResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert**
> AlertResponse create_alert(create_alert)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_response import AlertResponse
from openapi_client.model.create_alert import CreateAlert
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
    api_instance = alerts_api.AlertsApi(api_client)
    create_alert = CreateAlert(
        expression="expression_example",
        valid_until=dateutil_parser('1970-01-01T00:00:00.00Z'),
        trigger_limits=0,
        message="message_example",
    ) # CreateAlert | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_alert(create_alert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert** | [**CreateAlert**](CreateAlert.md)|  |

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> AlertResponse delete_alert(delete_alert)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_response import AlertResponse
from openapi_client.model.delete_alert import DeleteAlert
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
    api_instance = alerts_api.AlertsApi(api_client)
    delete_alert = DeleteAlert(
        alert_id=0,
    ) # DeleteAlert | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_alert(delete_alert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_alert** | [**DeleteAlert**](DeleteAlert.md)|  |

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dismiss_alert**
> AlertResponse dismiss_alert(dismiss_alert)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_response import AlertResponse
from openapi_client.model.dismiss_alert import DismissAlert
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
    api_instance = alerts_api.AlertsApi(api_client)
    dismiss_alert = DismissAlert(
        alert_id=0,
    ) # DismissAlert | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dismiss_alert(dismiss_alert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->dismiss_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dismiss_alert** | [**DismissAlert**](DismissAlert.md)|  |

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_read_alert_signal**
> AlertResponse mark_read_alert_signal(mark_read_alert_signal)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_response import AlertResponse
from openapi_client.model.mark_read_alert_signal import MarkReadAlertSignal
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
    api_instance = alerts_api.AlertsApi(api_client)
    mark_read_alert_signal = MarkReadAlertSignal(
        alert_id=0,
        alert_signal_id=0,
    ) # MarkReadAlertSignal | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_read_alert_signal(mark_read_alert_signal)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->mark_read_alert_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_read_alert_signal** | [**MarkReadAlertSignal**](MarkReadAlertSignal.md)|  |

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_alert**
> AlertResponse modify_alert(modify_alert)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_response import AlertResponse
from openapi_client.model.modify_alert import ModifyAlert
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
    api_instance = alerts_api.AlertsApi(api_client)
    modify_alert = ModifyAlert(
        alert_id=0,
        expression="expression_example",
        valid_until=dateutil_parser('1970-01-01T00:00:00.00Z'),
        trigger_limits=0,
        message="message_example",
    ) # ModifyAlert | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.modify_alert(modify_alert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->modify_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_alert** | [**ModifyAlert**](ModifyAlert.md)|  |

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_alert**
> AlertResponse reset_alert(reset_alert)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.alert_response import AlertResponse
from openapi_client.model.reset_alert import ResetAlert
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
    api_instance = alerts_api.AlertsApi(api_client)
    reset_alert = ResetAlert(
        alert_id=0,
    ) # ResetAlert | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reset_alert(reset_alert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->reset_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_alert** | [**ResetAlert**](ResetAlert.md)|  |

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **take_alert_signal_ownership**
> AdminAlertSignalResponse take_alert_signal_ownership(take_alert_signal_ownership)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.admin_alert_signal_response import AdminAlertSignalResponse
from openapi_client.model.take_alert_signal_ownership import TakeAlertSignalOwnership
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
    api_instance = alerts_api.AlertsApi(api_client)
    take_alert_signal_ownership = TakeAlertSignalOwnership(
        admin_alert_signal_id=0,
    ) # TakeAlertSignalOwnership | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.take_alert_signal_ownership(take_alert_signal_ownership)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->take_alert_signal_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take_alert_signal_ownership** | [**TakeAlertSignalOwnership**](TakeAlertSignalOwnership.md)|  |

### Return type

[**AdminAlertSignalResponse**](AdminAlertSignalResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdminAlertSignalResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

