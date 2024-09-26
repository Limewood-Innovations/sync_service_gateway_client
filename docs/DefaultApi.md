# sync_service_gateway_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pong_ping_get**](DefaultApi.md#pong_ping_get) | **GET** /ping | Pong


# **pong_ping_get**
> ApiResponse pong_ping_get()

Pong

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.api_response import ApiResponse
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
    api_instance = sync_service_gateway_client.DefaultApi(api_client)

    try:
        # Pong
        api_response = api_instance.pong_ping_get()
        print("The response of DefaultApi->pong_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pong_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

