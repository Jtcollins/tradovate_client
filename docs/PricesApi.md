# openapi_client.PricesApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_speed**](PricesApi.md#change_speed) | **POST** /replay/changespeed | 
[**check_replay_session**](PricesApi.md#check_replay_session) | **POST** /replay/checkreplaysession | 
[**initialize_clock**](PricesApi.md#initialize_clock) | **POST** /replay/initializeclock | 


# **change_speed**
> SimpleResponse change_speed(change_speed)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import prices_api
from openapi_client.model.change_speed import ChangeSpeed
from openapi_client.model.simple_response import SimpleResponse
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
    api_instance = prices_api.PricesApi(api_client)
    change_speed = ChangeSpeed(
        speed=0,
    ) # ChangeSpeed | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.change_speed(change_speed)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PricesApi->change_speed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_speed** | [**ChangeSpeed**](ChangeSpeed.md)|  |

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SimpleResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_replay_session**
> CheckReplaySessionResponse check_replay_session(check_replay_session)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import prices_api
from openapi_client.model.check_replay_session_response import CheckReplaySessionResponse
from openapi_client.model.check_replay_session import CheckReplaySession
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
    api_instance = prices_api.PricesApi(api_client)
    check_replay_session = CheckReplaySession(
        start_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CheckReplaySession | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.check_replay_session(check_replay_session)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PricesApi->check_replay_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_replay_session** | [**CheckReplaySession**](CheckReplaySession.md)|  |

### Return type

[**CheckReplaySessionResponse**](CheckReplaySessionResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CheckReplaySessionResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_clock**
> SimpleResponse initialize_clock(initialize_clock)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import prices_api
from openapi_client.model.initialize_clock import InitializeClock
from openapi_client.model.simple_response import SimpleResponse
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
    api_instance = prices_api.PricesApi(api_client)
    initialize_clock = InitializeClock(
        start_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        speed=0,
        initial_balance=3.14,
    ) # InitializeClock | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.initialize_clock(initialize_clock)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PricesApi->initialize_clock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initialize_clock** | [**InitializeClock**](InitializeClock.md)|  |

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SimpleResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

