# openapi_client.RisksApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_margin_dependents**](RisksApi.md#contract_margin_dependents) | **GET** /contractMargin/deps | 
[**contract_margin_item**](RisksApi.md#contract_margin_item) | **GET** /contractMargin/item | 
[**contract_margin_items**](RisksApi.md#contract_margin_items) | **GET** /contractMargin/items | 
[**contract_margin_l_dependents**](RisksApi.md#contract_margin_l_dependents) | **GET** /contractMargin/ldeps | 
[**delete_user_account_position_limit**](RisksApi.md#delete_user_account_position_limit) | **POST** /userAccountPositionLimit/deleteuseraccountpositionlimit | 
[**delete_user_account_risk_parameter**](RisksApi.md#delete_user_account_risk_parameter) | **POST** /userAccountPositionLimit/deleteuseraccountriskparameter | 
[**product_margin_dependents**](RisksApi.md#product_margin_dependents) | **GET** /productMargin/deps | 
[**product_margin_item**](RisksApi.md#product_margin_item) | **GET** /productMargin/item | 
[**product_margin_items**](RisksApi.md#product_margin_items) | **GET** /productMargin/items | 
[**product_margin_l_dependents**](RisksApi.md#product_margin_l_dependents) | **GET** /productMargin/ldeps | 
[**product_margin_list**](RisksApi.md#product_margin_list) | **GET** /productMargin/list | 
[**user_account_auto_liq_create**](RisksApi.md#user_account_auto_liq_create) | **POST** /userAccountAutoLiq/create | 
[**user_account_auto_liq_dependents**](RisksApi.md#user_account_auto_liq_dependents) | **GET** /userAccountAutoLiq/deps | 
[**user_account_auto_liq_item**](RisksApi.md#user_account_auto_liq_item) | **GET** /userAccountAutoLiq/item | 
[**user_account_auto_liq_items**](RisksApi.md#user_account_auto_liq_items) | **GET** /userAccountAutoLiq/items | 
[**user_account_auto_liq_l_dependents**](RisksApi.md#user_account_auto_liq_l_dependents) | **GET** /userAccountAutoLiq/ldeps | 
[**user_account_auto_liq_list**](RisksApi.md#user_account_auto_liq_list) | **GET** /userAccountAutoLiq/list | 
[**user_account_auto_liq_update**](RisksApi.md#user_account_auto_liq_update) | **POST** /userAccountAutoLiq/update | 
[**user_account_position_limit_create**](RisksApi.md#user_account_position_limit_create) | **POST** /userAccountPositionLimit/create | 
[**user_account_position_limit_dependents**](RisksApi.md#user_account_position_limit_dependents) | **GET** /userAccountPositionLimit/deps | 
[**user_account_position_limit_item**](RisksApi.md#user_account_position_limit_item) | **GET** /userAccountPositionLimit/item | 
[**user_account_position_limit_items**](RisksApi.md#user_account_position_limit_items) | **GET** /userAccountPositionLimit/items | 
[**user_account_position_limit_l_dependents**](RisksApi.md#user_account_position_limit_l_dependents) | **GET** /userAccountPositionLimit/ldeps | 
[**user_account_position_limit_update**](RisksApi.md#user_account_position_limit_update) | **POST** /userAccountPositionLimit/update | 
[**user_account_risk_parameter_create**](RisksApi.md#user_account_risk_parameter_create) | **POST** /userAccountRiskParameter/create | 
[**user_account_risk_parameter_dependents**](RisksApi.md#user_account_risk_parameter_dependents) | **GET** /userAccountRiskParameter/deps | 
[**user_account_risk_parameter_item**](RisksApi.md#user_account_risk_parameter_item) | **GET** /userAccountRiskParameter/item | 
[**user_account_risk_parameter_items**](RisksApi.md#user_account_risk_parameter_items) | **GET** /userAccountRiskParameter/items | 
[**user_account_risk_parameter_l_dependents**](RisksApi.md#user_account_risk_parameter_l_dependents) | **GET** /userAccountRiskParameter/ldeps | 
[**user_account_risk_parameter_update**](RisksApi.md#user_account_risk_parameter_update) | **POST** /userAccountRiskParameter/update | 


# **contract_margin_dependents**
> [ContractMargin] contract_margin_dependents(masterid)



Retrieves all entities of ContractMargin type related to Contract entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.contract_margin import ContractMargin
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
    api_instance = risks_api.RisksApi(api_client)
    masterid = 1 # int | id of Contract entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_margin_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->contract_margin_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Contract entity |

### Return type

[**[ContractMargin]**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_item**
> ContractMargin contract_margin_item(id)



Retrieves an entity of ContractMargin type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.contract_margin import ContractMargin
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
    api_instance = risks_api.RisksApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_margin_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->contract_margin_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ContractMargin**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_items**
> [ContractMargin] contract_margin_items(ids)



Retrieves multiple entities of ContractMargin type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.contract_margin import ContractMargin
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
    api_instance = risks_api.RisksApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_margin_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->contract_margin_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ContractMargin]**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_l_dependents**
> [ContractMargin] contract_margin_l_dependents(masterids)



Retrieves all entities of ContractMargin type related to multiple entities of Contract type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.contract_margin import ContractMargin
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
    api_instance = risks_api.RisksApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Contract entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_margin_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->contract_margin_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Contract entities |

### Return type

[**[ContractMargin]**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_account_position_limit**
> DeleteResultResponse delete_user_account_position_limit(delete_user_account_position_limit)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.delete_result_response import DeleteResultResponse
from openapi_client.model.delete_user_account_position_limit import DeleteUserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    delete_user_account_position_limit = DeleteUserAccountPositionLimit(
        user_account_position_limit_id=0,
    ) # DeleteUserAccountPositionLimit | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_user_account_position_limit(delete_user_account_position_limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->delete_user_account_position_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_account_position_limit** | [**DeleteUserAccountPositionLimit**](DeleteUserAccountPositionLimit.md)|  |

### Return type

[**DeleteResultResponse**](DeleteResultResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteResultResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_account_risk_parameter**
> DeleteResultResponse delete_user_account_risk_parameter(delete_user_account_risk_parameter)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.delete_user_account_risk_parameter import DeleteUserAccountRiskParameter
from openapi_client.model.delete_result_response import DeleteResultResponse
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
    api_instance = risks_api.RisksApi(api_client)
    delete_user_account_risk_parameter = DeleteUserAccountRiskParameter(
        user_account_risk_parameter_id=0,
    ) # DeleteUserAccountRiskParameter | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_user_account_risk_parameter(delete_user_account_risk_parameter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->delete_user_account_risk_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_account_risk_parameter** | [**DeleteUserAccountRiskParameter**](DeleteUserAccountRiskParameter.md)|  |

### Return type

[**DeleteResultResponse**](DeleteResultResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteResultResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_dependents**
> [ProductMargin] product_margin_dependents(masterid)



Retrieves all entities of ProductMargin type related to Product entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.product_margin import ProductMargin
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
    api_instance = risks_api.RisksApi(api_client)
    masterid = 1 # int | id of Product entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_margin_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->product_margin_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Product entity |

### Return type

[**[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_item**
> ProductMargin product_margin_item(id)



Retrieves an entity of ProductMargin type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.product_margin import ProductMargin
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
    api_instance = risks_api.RisksApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_margin_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->product_margin_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ProductMargin**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_items**
> [ProductMargin] product_margin_items(ids)



Retrieves multiple entities of ProductMargin type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.product_margin import ProductMargin
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
    api_instance = risks_api.RisksApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_margin_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->product_margin_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_l_dependents**
> [ProductMargin] product_margin_l_dependents(masterids)



Retrieves all entities of ProductMargin type related to multiple entities of Product type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.product_margin import ProductMargin
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
    api_instance = risks_api.RisksApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Product entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_margin_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->product_margin_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Product entities |

### Return type

[**[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_list**
> [ProductMargin] product_margin_list()



Retrieves all entities of ProductMargin type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.product_margin import ProductMargin
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
    api_instance = risks_api.RisksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.product_margin_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->product_margin_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductMargin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_create**
> UserAccountAutoLiq user_account_auto_liq_create(user_account_auto_liq)



Creates a new entity of UserAccountAutoLiq

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)
    user_account_auto_liq = UserAccountAutoLiq(
        id=1,
        changes_locked=True,
        margin_percentage_alert=3.14,
        daily_loss_percentage_alert=3.14,
        daily_loss_alert=3.14,
        margin_percentage_liq_only=3.14,
        daily_loss_percentage_liq_only=3.14,
        daily_loss_liq_only=3.14,
        margin_percentage_auto_liq=3.14,
        daily_loss_percentage_auto_liq=3.14,
        daily_loss_auto_liq=3.14,
        weekly_loss_auto_liq=3.14,
        flatten_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        trailing_max_drawdown=3.14,
        trailing_max_drawdown_limit=3.14,
        daily_profit_auto_liq=3.14,
        weekly_profit_auto_liq=3.14,
    ) # UserAccountAutoLiq | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_auto_liq_create(user_account_auto_liq)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_account_auto_liq** | [**UserAccountAutoLiq**](UserAccountAutoLiq.md)|  |

### Return type

[**UserAccountAutoLiq**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_dependents**
> [UserAccountAutoLiq] user_account_auto_liq_dependents(masterid)



Retrieves all entities of UserAccountAutoLiq type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_auto_liq_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_item**
> UserAccountAutoLiq user_account_auto_liq_item(id)



Retrieves an entity of UserAccountAutoLiq type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_auto_liq_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**UserAccountAutoLiq**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_items**
> [UserAccountAutoLiq] user_account_auto_liq_items(ids)



Retrieves multiple entities of UserAccountAutoLiq type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_auto_liq_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_l_dependents**
> [UserAccountAutoLiq] user_account_auto_liq_l_dependents(masterids)



Retrieves all entities of UserAccountAutoLiq type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_auto_liq_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_list**
> [UserAccountAutoLiq] user_account_auto_liq_list()



Retrieves all entities of UserAccountAutoLiq type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.user_account_auto_liq_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_update**
> UserAccountAutoLiq user_account_auto_liq_update(user_account_auto_liq)



Updates an existing entity of UserAccountAutoLiq

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_auto_liq import UserAccountAutoLiq
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
    api_instance = risks_api.RisksApi(api_client)
    user_account_auto_liq = UserAccountAutoLiq(
        id=1,
        changes_locked=True,
        margin_percentage_alert=3.14,
        daily_loss_percentage_alert=3.14,
        daily_loss_alert=3.14,
        margin_percentage_liq_only=3.14,
        daily_loss_percentage_liq_only=3.14,
        daily_loss_liq_only=3.14,
        margin_percentage_auto_liq=3.14,
        daily_loss_percentage_auto_liq=3.14,
        daily_loss_auto_liq=3.14,
        weekly_loss_auto_liq=3.14,
        flatten_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        trailing_max_drawdown=3.14,
        trailing_max_drawdown_limit=3.14,
        daily_profit_auto_liq=3.14,
        weekly_profit_auto_liq=3.14,
    ) # UserAccountAutoLiq | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_auto_liq_update(user_account_auto_liq)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_auto_liq_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_account_auto_liq** | [**UserAccountAutoLiq**](UserAccountAutoLiq.md)|  |

### Return type

[**UserAccountAutoLiq**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountAutoLiq |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_create**
> UserAccountPositionLimit user_account_position_limit_create(user_account_position_limit)



Creates a new entity of UserAccountPositionLimit

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_position_limit import UserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    user_account_position_limit = UserAccountPositionLimit(
        id=1,
        contract_id=0,
        product_id=0,
        exchange_id=0,
        product_type="CommonStock",
        risk_discount_contract_group_id=0,
        product_verification_status="Inactive",
        contract_group_id=0,
        active=True,
        risk_time_period_id=0,
        total_by="Contract",
        short_limit=0,
        long_limit=0,
        exposed_limit=0,
        description="description_example",
        account_id=0,
    ) # UserAccountPositionLimit | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_position_limit_create(user_account_position_limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_position_limit_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_account_position_limit** | [**UserAccountPositionLimit**](UserAccountPositionLimit.md)|  |

### Return type

[**UserAccountPositionLimit**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountPositionLimit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_dependents**
> [UserAccountPositionLimit] user_account_position_limit_dependents(masterid)



Retrieves all entities of UserAccountPositionLimit type related to Account entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_position_limit import UserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    masterid = 1 # int | id of Account entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_position_limit_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_position_limit_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity |

### Return type

[**[UserAccountPositionLimit]**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountPositionLimit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_item**
> UserAccountPositionLimit user_account_position_limit_item(id)



Retrieves an entity of UserAccountPositionLimit type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_position_limit import UserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_position_limit_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_position_limit_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**UserAccountPositionLimit**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountPositionLimit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_items**
> [UserAccountPositionLimit] user_account_position_limit_items(ids)



Retrieves multiple entities of UserAccountPositionLimit type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_position_limit import UserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_position_limit_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_position_limit_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[UserAccountPositionLimit]**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountPositionLimit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_l_dependents**
> [UserAccountPositionLimit] user_account_position_limit_l_dependents(masterids)



Retrieves all entities of UserAccountPositionLimit type related to multiple entities of Account type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_position_limit import UserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Account entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_position_limit_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_position_limit_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Account entities |

### Return type

[**[UserAccountPositionLimit]**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountPositionLimit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_update**
> UserAccountPositionLimit user_account_position_limit_update(user_account_position_limit)



Updates an existing entity of UserAccountPositionLimit

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_position_limit import UserAccountPositionLimit
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
    api_instance = risks_api.RisksApi(api_client)
    user_account_position_limit = UserAccountPositionLimit(
        id=1,
        contract_id=0,
        product_id=0,
        exchange_id=0,
        product_type="CommonStock",
        risk_discount_contract_group_id=0,
        product_verification_status="Inactive",
        contract_group_id=0,
        active=True,
        risk_time_period_id=0,
        total_by="Contract",
        short_limit=0,
        long_limit=0,
        exposed_limit=0,
        description="description_example",
        account_id=0,
    ) # UserAccountPositionLimit | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_position_limit_update(user_account_position_limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_position_limit_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_account_position_limit** | [**UserAccountPositionLimit**](UserAccountPositionLimit.md)|  |

### Return type

[**UserAccountPositionLimit**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountPositionLimit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_create**
> UserAccountRiskParameter user_account_risk_parameter_create(user_account_risk_parameter)



Creates a new entity of UserAccountRiskParameter

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_risk_parameter import UserAccountRiskParameter
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
    api_instance = risks_api.RisksApi(api_client)
    user_account_risk_parameter = UserAccountRiskParameter(
        id=1,
        contract_id=0,
        product_id=0,
        exchange_id=0,
        product_type="CommonStock",
        risk_discount_contract_group_id=0,
        product_verification_status="Inactive",
        contract_group_id=0,
        max_opening_order_qty=0,
        max_closing_order_qty=0,
        max_back_month=0,
        pre_expiration_days=1,
        margin_percentage=3.14,
        margin_dollar_value=3.14,
        hard_limit=True,
        user_account_position_limit_id=0,
    ) # UserAccountRiskParameter | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_risk_parameter_create(user_account_risk_parameter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_risk_parameter_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_account_risk_parameter** | [**UserAccountRiskParameter**](UserAccountRiskParameter.md)|  |

### Return type

[**UserAccountRiskParameter**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountRiskParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_dependents**
> [UserAccountRiskParameter] user_account_risk_parameter_dependents(masterid)



Retrieves all entities of UserAccountRiskParameter type related to UserAccountPositionLimit entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_risk_parameter import UserAccountRiskParameter
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
    api_instance = risks_api.RisksApi(api_client)
    masterid = 1 # int | id of UserAccountPositionLimit entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_risk_parameter_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_risk_parameter_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of UserAccountPositionLimit entity |

### Return type

[**[UserAccountRiskParameter]**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountRiskParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_item**
> UserAccountRiskParameter user_account_risk_parameter_item(id)



Retrieves an entity of UserAccountRiskParameter type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_risk_parameter import UserAccountRiskParameter
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
    api_instance = risks_api.RisksApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_risk_parameter_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_risk_parameter_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**UserAccountRiskParameter**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountRiskParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_items**
> [UserAccountRiskParameter] user_account_risk_parameter_items(ids)



Retrieves multiple entities of UserAccountRiskParameter type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_risk_parameter import UserAccountRiskParameter
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
    api_instance = risks_api.RisksApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_risk_parameter_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_risk_parameter_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[UserAccountRiskParameter]**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountRiskParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_l_dependents**
> [UserAccountRiskParameter] user_account_risk_parameter_l_dependents(masterids)



Retrieves all entities of UserAccountRiskParameter type related to multiple entities of UserAccountPositionLimit type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_risk_parameter import UserAccountRiskParameter
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
    api_instance = risks_api.RisksApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of UserAccountPositionLimit entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_risk_parameter_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_risk_parameter_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of UserAccountPositionLimit entities |

### Return type

[**[UserAccountRiskParameter]**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountRiskParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_update**
> UserAccountRiskParameter user_account_risk_parameter_update(user_account_risk_parameter)



Updates an existing entity of UserAccountRiskParameter

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import risks_api
from openapi_client.model.user_account_risk_parameter import UserAccountRiskParameter
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
    api_instance = risks_api.RisksApi(api_client)
    user_account_risk_parameter = UserAccountRiskParameter(
        id=1,
        contract_id=0,
        product_id=0,
        exchange_id=0,
        product_type="CommonStock",
        risk_discount_contract_group_id=0,
        product_verification_status="Inactive",
        contract_group_id=0,
        max_opening_order_qty=0,
        max_closing_order_qty=0,
        max_back_month=0,
        pre_expiration_days=1,
        margin_percentage=3.14,
        margin_dollar_value=3.14,
        hard_limit=True,
        user_account_position_limit_id=0,
    ) # UserAccountRiskParameter | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_account_risk_parameter_update(user_account_risk_parameter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RisksApi->user_account_risk_parameter_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_account_risk_parameter** | [**UserAccountRiskParameter**](UserAccountRiskParameter.md)|  |

### Return type

[**UserAccountRiskParameter**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserAccountRiskParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

