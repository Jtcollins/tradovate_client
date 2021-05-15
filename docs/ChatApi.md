# openapi_client.ChatApi

All URIs are relative to *https://demo-api-d.tradovate.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_dependents**](ChatApi.md#chat_dependents) | **GET** /chat/deps | 
[**chat_item**](ChatApi.md#chat_item) | **GET** /chat/item | 
[**chat_items**](ChatApi.md#chat_items) | **GET** /chat/items | 
[**chat_l_dependents**](ChatApi.md#chat_l_dependents) | **GET** /chat/ldeps | 
[**chat_list**](ChatApi.md#chat_list) | **GET** /chat/list | 
[**chat_message_dependents**](ChatApi.md#chat_message_dependents) | **GET** /chatMessage/deps | 
[**chat_message_item**](ChatApi.md#chat_message_item) | **GET** /chatMessage/item | 
[**chat_message_items**](ChatApi.md#chat_message_items) | **GET** /chatMessage/items | 
[**chat_message_l_dependents**](ChatApi.md#chat_message_l_dependents) | **GET** /chatMessage/ldeps | 
[**close_chat**](ChatApi.md#close_chat) | **POST** /chat/closechat | 
[**mark_as_read_chat_message**](ChatApi.md#mark_as_read_chat_message) | **POST** /chat/markasreadchatmessage | 
[**post_chat_message**](ChatApi.md#post_chat_message) | **POST** /chat/postchatmessage | 


# **chat_dependents**
> [Chat] chat_dependents(masterid)



Retrieves all entities of Chat type related to User entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat import Chat
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
    api_instance = chat_api.ChatApi(api_client)
    masterid = 1 # int | id of User entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity |

### Return type

[**[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_item**
> Chat chat_item(id)



Retrieves an entity of Chat type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat import Chat
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
    api_instance = chat_api.ChatApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Chat**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_items**
> [Chat] chat_items(ids)



Retrieves multiple entities of Chat type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat import Chat
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
    api_instance = chat_api.ChatApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_l_dependents**
> [Chat] chat_l_dependents(masterids)



Retrieves all entities of Chat type related to multiple entities of User type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat import Chat
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
    api_instance = chat_api.ChatApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of User entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of User entities |

### Return type

[**[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_list**
> [Chat] chat_list()



Retrieves all entities of Chat type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat import Chat
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
    api_instance = chat_api.ChatApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.chat_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_dependents**
> [ChatMessage] chat_message_dependents(masterid)



Retrieves all entities of ChatMessage type related to Chat entity

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat_message import ChatMessage
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
    api_instance = chat_api.ChatApi(api_client)
    masterid = 1 # int | id of Chat entity

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_message_dependents(masterid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_message_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Chat entity |

### Return type

[**[ChatMessage]**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatMessage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_item**
> ChatMessage chat_message_item(id)



Retrieves an entity of ChatMessage type by its id

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat_message import ChatMessage
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
    api_instance = chat_api.ChatApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_message_item(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_message_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ChatMessage**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatMessage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_items**
> [ChatMessage] chat_message_items(ids)



Retrieves multiple entities of ChatMessage type by its ids

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat_message import ChatMessage
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
    api_instance = chat_api.ChatApi(api_client)
    ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_message_items(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_message_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**|  |

### Return type

[**[ChatMessage]**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatMessage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_l_dependents**
> [ChatMessage] chat_message_l_dependents(masterids)



Retrieves all entities of ChatMessage type related to multiple entities of Chat type

### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.chat_message import ChatMessage
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
    api_instance = chat_api.ChatApi(api_client)
    masterids = [
        1,
    ] # [int] | ids of Chat entities

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chat_message_l_dependents(masterids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->chat_message_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | **[int]**| ids of Chat entities |

### Return type

[**[ChatMessage]**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatMessage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_chat**
> ChatResponse close_chat(close_chat)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.close_chat import CloseChat
from openapi_client.model.chat_response import ChatResponse
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
    api_instance = chat_api.ChatApi(api_client)
    close_chat = CloseChat(
        chat_id=0,
    ) # CloseChat | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.close_chat(close_chat)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->close_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_chat** | [**CloseChat**](CloseChat.md)|  |

### Return type

[**ChatResponse**](ChatResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_read_chat_message**
> ChatMessageResponse mark_as_read_chat_message(mark_as_read_chat_message)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.mark_as_read_chat_message import MarkAsReadChatMessage
from openapi_client.model.chat_message_response import ChatMessageResponse
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
    api_instance = chat_api.ChatApi(api_client)
    mark_as_read_chat_message = MarkAsReadChatMessage(
        chat_message_id=0,
    ) # MarkAsReadChatMessage | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_as_read_chat_message(mark_as_read_chat_message)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->mark_as_read_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_as_read_chat_message** | [**MarkAsReadChatMessage**](MarkAsReadChatMessage.md)|  |

### Return type

[**ChatMessageResponse**](ChatMessageResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatMessageResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_chat_message**
> ChatMessageResponse post_chat_message(post_chat_message)



### Example

* Bearer Authentication (bearer_access_token):
```python
import time
import openapi_client
from openapi_client.api import chat_api
from openapi_client.model.post_chat_message import PostChatMessage
from openapi_client.model.chat_message_response import ChatMessageResponse
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
    api_instance = chat_api.ChatApi(api_client)
    post_chat_message = PostChatMessage(
        user_id=0,
        category="Support",
        text="text_example",
    ) # PostChatMessage | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_chat_message(post_chat_message)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChatApi->post_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_chat_message** | [**PostChatMessage**](PostChatMessage.md)|  |

### Return type

[**ChatMessageResponse**](ChatMessageResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChatMessageResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

