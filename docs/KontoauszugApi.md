# sync_service_gateway_client.KontoauszugApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kontoauszug_kontoauszug_post**](KontoauszugApi.md#add_kontoauszug_kontoauszug_post) | **POST** /kontoauszug | Add Kontoauszug
[**get_kontoauszug_kontoauszug_get**](KontoauszugApi.md#get_kontoauszug_kontoauszug_get) | **GET** /kontoauszug | Get Kontoauszug


# **add_kontoauszug_kontoauszug_post**
> ApiResponse add_kontoauszug_kontoauszug_post(kontoauszug_create)

Add Kontoauszug

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.api_response import ApiResponse
from sync_service_gateway_client.models.kontoauszug_create import KontoauszugCreate
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
    api_instance = sync_service_gateway_client.KontoauszugApi(api_client)
    kontoauszug_create = sync_service_gateway_client.KontoauszugCreate() # KontoauszugCreate | 

    try:
        # Add Kontoauszug
        api_response = api_instance.add_kontoauszug_kontoauszug_post(kontoauszug_create)
        print("The response of KontoauszugApi->add_kontoauszug_kontoauszug_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KontoauszugApi->add_kontoauszug_kontoauszug_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kontoauszug_create** | [**KontoauszugCreate**](KontoauszugCreate.md)|  | 

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

# **get_kontoauszug_kontoauszug_get**
> List[Kontoauszug] get_kontoauszug_kontoauszug_get()

Get Kontoauszug

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.kontoauszug import Kontoauszug
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
    api_instance = sync_service_gateway_client.KontoauszugApi(api_client)

    try:
        # Get Kontoauszug
        api_response = api_instance.get_kontoauszug_kontoauszug_get()
        print("The response of KontoauszugApi->get_kontoauszug_kontoauszug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KontoauszugApi->get_kontoauszug_kontoauszug_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Kontoauszug]**](Kontoauszug.md)

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

