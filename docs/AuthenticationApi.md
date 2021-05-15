# openapi_client.AuthenticationApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token_request**](AuthenticationApi.md#access_token_request) | **POST** /auth/accesstokenrequest | 
[**me**](AuthenticationApi.md#me) | **GET** /auth/me | 
[**o_auth_token**](AuthenticationApi.md#o_auth_token) | **POST** /auth/oauthtoken | 
[**renew_access_token**](AuthenticationApi.md#renew_access_token) | **GET** /auth/renewaccesstoken | 


# **access_token_request**
> AccessTokenResponse access_token_request(access_token_request)



### Example

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.access_token_request import AccessTokenRequest
from openapi_client.model.access_token_response import AccessTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    access_token_request = AccessTokenRequest(
        name="name_example",
        password="password_example",
        app_id="app_id_example",
        app_version="app_version_example",
        device_id="device_id_example",
        cid="cid_example",
        sec="sec_example",
    ) # AccessTokenRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.access_token_request(access_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->access_token_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)|  |

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AccessTokenResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> OAuthMeResponse me()



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.o_auth_me_response import OAuthMeResponse
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.me()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthMeResponse**](OAuthMeResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuthMeResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth_token**
> OAuthTokenResponse o_auth_token(o_auth_token)



### Example

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.o_auth_token import OAuthToken
from openapi_client.model.o_auth_token_response import OAuthTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api-d.tradovate.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo-api-d.tradovate.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    o_auth_token = OAuthToken(
        grant_type="grant_type_example",
        code="code_example",
        redirect_uri="redirect_uri_example",
        client_id="client_id_example",
        client_secret="client_secret_example",
        http_auth="http_auth_example",
    ) # OAuthToken | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.o_auth_token(o_auth_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->o_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_token** | [**OAuthToken**](OAuthToken.md)|  |

### Return type

[**OAuthTokenResponse**](OAuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuthTokenResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_access_token**
> AccessTokenResponse renew_access_token()



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.access_token_response import AccessTokenResponse
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.renew_access_token()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->renew_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AccessTokenResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

