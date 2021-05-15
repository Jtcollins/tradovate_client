# openapi_client.ContractLibraryApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_dependents**](ContractLibraryApi.md#contract_dependents) | **GET** /contract/deps | 
[**contract_find**](ContractLibraryApi.md#contract_find) | **GET** /contract/find | 
[**contract_group_find**](ContractLibraryApi.md#contract_group_find) | **GET** /contractGroup/find | 
[**contract_group_item**](ContractLibraryApi.md#contract_group_item) | **GET** /contractGroup/item | 
[**contract_group_items**](ContractLibraryApi.md#contract_group_items) | **GET** /contractGroup/items | 
[**contract_group_list**](ContractLibraryApi.md#contract_group_list) | **GET** /contractGroup/list | 
[**contract_group_suggest**](ContractLibraryApi.md#contract_group_suggest) | **GET** /contractGroup/suggest | 
[**contract_item**](ContractLibraryApi.md#contract_item) | **GET** /contract/item | 
[**contract_items**](ContractLibraryApi.md#contract_items) | **GET** /contract/items | 
[**contract_l_dependents**](ContractLibraryApi.md#contract_l_dependents) | **GET** /contract/ldeps | 
[**contract_maturity_dependents**](ContractLibraryApi.md#contract_maturity_dependents) | **GET** /contractMaturity/deps | 
[**contract_maturity_item**](ContractLibraryApi.md#contract_maturity_item) | **GET** /contractMaturity/item | 
[**contract_maturity_items**](ContractLibraryApi.md#contract_maturity_items) | **GET** /contractMaturity/items | 
[**contract_maturity_l_dependents**](ContractLibraryApi.md#contract_maturity_l_dependents) | **GET** /contractMaturity/ldeps | 
[**contract_suggest**](ContractLibraryApi.md#contract_suggest) | **GET** /contract/suggest | 
[**currency_find**](ContractLibraryApi.md#currency_find) | **GET** /currency/find | 
[**currency_item**](ContractLibraryApi.md#currency_item) | **GET** /currency/item | 
[**currency_items**](ContractLibraryApi.md#currency_items) | **GET** /currency/items | 
[**currency_list**](ContractLibraryApi.md#currency_list) | **GET** /currency/list | 
[**currency_rate_dependents**](ContractLibraryApi.md#currency_rate_dependents) | **GET** /currencyRate/deps | 
[**currency_rate_item**](ContractLibraryApi.md#currency_rate_item) | **GET** /currencyRate/item | 
[**currency_rate_items**](ContractLibraryApi.md#currency_rate_items) | **GET** /currencyRate/items | 
[**currency_rate_l_dependents**](ContractLibraryApi.md#currency_rate_l_dependents) | **GET** /currencyRate/ldeps | 
[**currency_rate_list**](ContractLibraryApi.md#currency_rate_list) | **GET** /currencyRate/list | 
[**currency_suggest**](ContractLibraryApi.md#currency_suggest) | **GET** /currency/suggest | 
[**exchange_find**](ContractLibraryApi.md#exchange_find) | **GET** /exchange/find | 
[**exchange_item**](ContractLibraryApi.md#exchange_item) | **GET** /exchange/item | 
[**exchange_items**](ContractLibraryApi.md#exchange_items) | **GET** /exchange/items | 
[**exchange_list**](ContractLibraryApi.md#exchange_list) | **GET** /exchange/list | 
[**exchange_suggest**](ContractLibraryApi.md#exchange_suggest) | **GET** /exchange/suggest | 
[**get_product_fee_params**](ContractLibraryApi.md#get_product_fee_params) | **POST** /contract/getproductfeeparams | 
[**product_dependents**](ContractLibraryApi.md#product_dependents) | **GET** /product/deps | 
[**product_find**](ContractLibraryApi.md#product_find) | **GET** /product/find | 
[**product_item**](ContractLibraryApi.md#product_item) | **GET** /product/item | 
[**product_items**](ContractLibraryApi.md#product_items) | **GET** /product/items | 
[**product_l_dependents**](ContractLibraryApi.md#product_l_dependents) | **GET** /product/ldeps | 
[**product_list**](ContractLibraryApi.md#product_list) | **GET** /product/list | 
[**product_session_dependents**](ContractLibraryApi.md#product_session_dependents) | **GET** /productSession/deps | 
[**product_session_item**](ContractLibraryApi.md#product_session_item) | **GET** /productSession/item | 
[**product_session_items**](ContractLibraryApi.md#product_session_items) | **GET** /productSession/items | 
[**product_session_l_dependents**](ContractLibraryApi.md#product_session_l_dependents) | **GET** /productSession/ldeps | 
[**product_suggest**](ContractLibraryApi.md#product_suggest) | **GET** /product/suggest | 
[**roll_contract**](ContractLibraryApi.md#roll_contract) | **POST** /contract/rollcontract | 
[**spread_definition_item**](ContractLibraryApi.md#spread_definition_item) | **GET** /spreadDefinition/item | 
[**spread_definition_items**](ContractLibraryApi.md#spread_definition_items) | **GET** /spreadDefinition/items | 


# **contract_dependents**
> [Contract] contract_dependents(masterid)



Retrieves all entities of Contract type related to ContractMaturity entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract import Contract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterid = 1 # int | id of ContractMaturity entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of ContractMaturity entity |

### Return type

[**[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_find**
> Contract contract_find(name)



Retrieves an entity of Contract type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract import Contract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Contract**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_find**
> ContractGroup contract_group_find(name)



Retrieves an entity of ContractGroup type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_group import ContractGroup
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_group_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_group_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**ContractGroup**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_item**
> ContractGroup contract_group_item(id)



Retrieves an entity of ContractGroup type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_group import ContractGroup
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_group_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_group_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ContractGroup**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_items**
> [ContractGroup] contract_group_items(ids)



Retrieves multiple entities of ContractGroup type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_group import ContractGroup
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_group_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_group_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ContractGroup]**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_list**
> [ContractGroup] contract_group_list()



Retrieves all entities of ContractGroup type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_group import ContractGroup
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.contract_group_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ContractGroup]**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_suggest**
> [ContractGroup] contract_group_suggest(t, l)



Retrieves entities of ContractGroup type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_group import ContractGroup
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_group_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_group_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[ContractGroup]**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_item**
> Contract contract_item(id)



Retrieves an entity of Contract type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract import Contract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Contract**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_items**
> [Contract] contract_items(ids)



Retrieves multiple entities of Contract type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract import Contract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_l_dependents**
> [Contract] contract_l_dependents(masterids)



Retrieves all entities of Contract type related to multiple entities of ContractMaturity type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract import Contract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of ContractMaturity entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of ContractMaturity entities |

### Return type

[**[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_dependents**
> [ContractMaturity] contract_maturity_dependents(masterid)



Retrieves all entities of ContractMaturity type related to Product entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_maturity import ContractMaturity
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterid = 1 # int | id of Product entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_maturity_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_maturity_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Product entity |

### Return type

[**[ContractMaturity]**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMaturity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_item**
> ContractMaturity contract_maturity_item(id)



Retrieves an entity of ContractMaturity type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_maturity import ContractMaturity
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_maturity_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_maturity_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ContractMaturity**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMaturity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_items**
> [ContractMaturity] contract_maturity_items(ids)



Retrieves multiple entities of ContractMaturity type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_maturity import ContractMaturity
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_maturity_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_maturity_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ContractMaturity]**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMaturity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_l_dependents**
> [ContractMaturity] contract_maturity_l_dependents(masterids)



Retrieves all entities of ContractMaturity type related to multiple entities of Product type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract_maturity import ContractMaturity
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Product entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_maturity_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_maturity_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Product entities |

### Return type

[**[ContractMaturity]**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContractMaturity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_suggest**
> [Contract] contract_suggest(t, l)



Retrieves entities of Contract type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.contract import Contract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contract_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->contract_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_find**
> Currency currency_find(name)



Retrieves an entity of Currency type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency import Currency
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Currency**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_item**
> Currency currency_item(id)



Retrieves an entity of Currency type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency import Currency
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Currency**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_items**
> [Currency] currency_items(ids)



Retrieves multiple entities of Currency type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency import Currency
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Currency]**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_list**
> [Currency] currency_list()



Retrieves all entities of Currency type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency import Currency
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.currency_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Currency]**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_dependents**
> [CurrencyRate] currency_rate_dependents(masterid)



Retrieves all entities of CurrencyRate type related to Currency entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency_rate import CurrencyRate
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterid = 1 # int | id of Currency entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_rate_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_rate_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Currency entity |

### Return type

[**[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrencyRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_item**
> CurrencyRate currency_rate_item(id)



Retrieves an entity of CurrencyRate type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency_rate import CurrencyRate
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_rate_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**CurrencyRate**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrencyRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_items**
> [CurrencyRate] currency_rate_items(ids)



Retrieves multiple entities of CurrencyRate type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency_rate import CurrencyRate
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_rate_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_rate_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrencyRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_l_dependents**
> [CurrencyRate] currency_rate_l_dependents(masterids)



Retrieves all entities of CurrencyRate type related to multiple entities of Currency type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency_rate import CurrencyRate
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Currency entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_rate_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_rate_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Currency entities |

### Return type

[**[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrencyRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_list**
> [CurrencyRate] currency_rate_list()



Retrieves all entities of CurrencyRate type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency_rate import CurrencyRate
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.currency_rate_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_rate_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrencyRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_suggest**
> [Currency] currency_suggest(t, l)



Retrieves entities of Currency type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.currency import Currency
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.currency_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->currency_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[Currency]**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_find**
> Exchange exchange_find(name)



Retrieves an entity of Exchange type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.exchange import Exchange
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.exchange_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->exchange_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Exchange**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exchange |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_item**
> Exchange exchange_item(id)



Retrieves an entity of Exchange type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.exchange import Exchange
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.exchange_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->exchange_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Exchange**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exchange |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_items**
> [Exchange] exchange_items(ids)



Retrieves multiple entities of Exchange type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.exchange import Exchange
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.exchange_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->exchange_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Exchange]**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exchange |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_list**
> [Exchange] exchange_list()



Retrieves all entities of Exchange type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.exchange import Exchange
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.exchange_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->exchange_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Exchange]**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exchange |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_suggest**
> [Exchange] exchange_suggest(t, l)



Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.exchange import Exchange
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.exchange_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->exchange_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[Exchange]**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exchange |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_fee_params**
> ProductFeeParamsResponse get_product_fee_params(get_product_fee_params)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product_fee_params_response import ProductFeeParamsResponse
from openapi_client.model.get_product_fee_params import GetProductFeeParams
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    get_product_fee_params = GetProductFeeParams(
        product_ids=[
            1,
        ],
    ) # GetProductFeeParams | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_product_fee_params(get_product_fee_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->get_product_fee_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_product_fee_params** | [**GetProductFeeParams**](GetProductFeeParams.md)|  |

### Return type

[**ProductFeeParamsResponse**](ProductFeeParamsResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductFeeParamsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_dependents**
> [Product] product_dependents(masterid)



Retrieves all entities of Product type related to Exchange entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterid = 1 # int | id of Exchange entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Exchange entity |

### Return type

[**[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_find**
> Product product_find(name)



Retrieves an entity of Product type by its name

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_find(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Product**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_item**
> Product product_item(id)



Retrieves an entity of Product type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Product**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_items**
> [Product] product_items(ids)



Retrieves multiple entities of Product type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_l_dependents**
> [Product] product_l_dependents(masterids)



Retrieves all entities of Product type related to multiple entities of Exchange type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Exchange entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Exchange entities |

### Return type

[**[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list**
> [Product] product_list()



Retrieves all entities of Product type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.product_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_dependents**
> [ProductSession] product_session_dependents(masterid)



Retrieves all entities of ProductSession type related to Product entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product_session import ProductSession
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterid = 1 # int | id of Product entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_session_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_session_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Product entity |

### Return type

[**[ProductSession]**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductSession |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_item**
> ProductSession product_session_item(id)



Retrieves an entity of ProductSession type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product_session import ProductSession
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_session_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_session_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ProductSession**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductSession |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_items**
> [ProductSession] product_session_items(ids)



Retrieves multiple entities of ProductSession type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product_session import ProductSession
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_session_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_session_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ProductSession]**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductSession |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_l_dependents**
> [ProductSession] product_session_l_dependents(masterids)



Retrieves all entities of ProductSession type related to multiple entities of Product type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product_session import ProductSession
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Product entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_session_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_session_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Product entities |

### Return type

[**[ProductSession]**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProductSession |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_suggest**
> [Product] product_suggest(t, l)



Retrieves entities of Product type filtered by an occurrence of a text in one of its fields

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.product import Product
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    t = "t_example" # str | Text
    l = 1 # int | Max number of entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.product_suggest(t, l)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->product_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text |
 **l** | **int**| Max number of entities |

### Return type

[**[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roll_contract**
> RollContractResponse roll_contract(roll_contract)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.roll_contract_response import RollContractResponse
from openapi_client.model.roll_contract import RollContract
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    roll_contract = RollContract(
        name="name_example",
        forward=True,
        if_expired=True,
    ) # RollContract | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.roll_contract(roll_contract)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->roll_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roll_contract** | [**RollContract**](RollContract.md)|  |

### Return type

[**RollContractResponse**](RollContractResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RollContractResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spread_definition_item**
> SpreadDefinition spread_definition_item(id)



Retrieves an entity of SpreadDefinition type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.spread_definition import SpreadDefinition
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.spread_definition_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->spread_definition_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**SpreadDefinition**](SpreadDefinition.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SpreadDefinition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spread_definition_items**
> [SpreadDefinition] spread_definition_items(ids)



Retrieves multiple entities of SpreadDefinition type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import contract_library_api
from openapi_client.model.spread_definition import SpreadDefinition
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
    api_instance = contract_library_api.ContractLibraryApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.spread_definition_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractLibraryApi->spread_definition_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[SpreadDefinition]**](SpreadDefinition.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SpreadDefinition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

