# sync_service_gateway_client.IHNotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ihclose_ihclose_post**](IHNotificationsApi.md#add_ihclose_ihclose_post) | **POST** /ihclose | Add Ihclose
[**add_ihcreate_ihcreate_post**](IHNotificationsApi.md#add_ihcreate_ihcreate_post) | **POST** /ihcreate | Add Ihcreate
[**get_ihclose_ihclose_get**](IHNotificationsApi.md#get_ihclose_ihclose_get) | **GET** /ihclose | Get Ihclose
[**get_ihcreate_by_id_ihcreate_transaction_id_get**](IHNotificationsApi.md#get_ihcreate_by_id_ihcreate_transaction_id_get) | **GET** /ihcreate/{transaction_id} | Get Ihcreate By Id
[**get_ihcreate_ihcreate_get**](IHNotificationsApi.md#get_ihcreate_ihcreate_get) | **GET** /ihcreate | get ihcreate


# **add_ihclose_ihclose_post**
> ApiResponse add_ihclose_ihclose_post(ih_close_create)

Add Ihclose

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.api_response import ApiResponse
from sync_service_gateway_client.models.ih_close_create import IHCloseCreate
from sync_service_gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_gateway_client.IHNotificationsApi(api_client)
    ih_close_create = sync_service_gateway_client.IHCloseCreate() # IHCloseCreate | 

    try:
        # Add Ihclose
        api_response = api_instance.add_ihclose_ihclose_post(ih_close_create)
        print("The response of IHNotificationsApi->add_ihclose_ihclose_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationsApi->add_ihclose_ihclose_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ih_close_create** | [**IHCloseCreate**](IHCloseCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ihcreate_ihcreate_post**
> ApiResponse add_ihcreate_ihcreate_post(ih_create_create)

Add Ihcreate

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.api_response import ApiResponse
from sync_service_gateway_client.models.ih_create_create import IHCreateCreate
from sync_service_gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_gateway_client.IHNotificationsApi(api_client)
    ih_create_create = sync_service_gateway_client.IHCreateCreate() # IHCreateCreate | 

    try:
        # Add Ihcreate
        api_response = api_instance.add_ihcreate_ihcreate_post(ih_create_create)
        print("The response of IHNotificationsApi->add_ihcreate_ihcreate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationsApi->add_ihcreate_ihcreate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ih_create_create** | [**IHCreateCreate**](IHCreateCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ihclose_ihclose_get**
> List[IHClose] get_ihclose_ihclose_get()

Get Ihclose

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.ih_close import IHClose
from sync_service_gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_gateway_client.IHNotificationsApi(api_client)

    try:
        # Get Ihclose
        api_response = api_instance.get_ihclose_ihclose_get()
        print("The response of IHNotificationsApi->get_ihclose_ihclose_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationsApi->get_ihclose_ihclose_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IHClose]**](IHClose.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ihcreate_by_id_ihcreate_transaction_id_get**
> IHCreate get_ihcreate_by_id_ihcreate_transaction_id_get(transaction_id)

Get Ihcreate By Id

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.ih_create import IHCreate
from sync_service_gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_gateway_client.IHNotificationsApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Ihcreate By Id
        api_response = api_instance.get_ihcreate_by_id_ihcreate_transaction_id_get(transaction_id)
        print("The response of IHNotificationsApi->get_ihcreate_by_id_ihcreate_transaction_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationsApi->get_ihcreate_by_id_ihcreate_transaction_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**IHCreate**](IHCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ihcreate_ihcreate_get**
> List[IHCreate] get_ihcreate_ihcreate_get()

get ihcreate

description

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.ih_create import IHCreate
from sync_service_gateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_gateway_client.IHNotificationsApi(api_client)

    try:
        # get ihcreate
        api_response = api_instance.get_ihcreate_ihcreate_get()
        print("The response of IHNotificationsApi->get_ihcreate_ihcreate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationsApi->get_ihcreate_ihcreate_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IHCreate]**](IHCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

