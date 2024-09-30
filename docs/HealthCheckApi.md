# sync_service_api_gateway.HealthCheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_pong**](HealthCheckApi.md#health_check_pong) | **GET** /ping | Pong


# **health_check_pong**
> object health_check_pong()

Pong

### Example


```python
import sync_service_api_gateway
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.HealthCheckApi(api_client)

    try:
        # Pong
        api_response = api_instance.health_check_pong()
        print("The response of HealthCheckApi->health_check_pong:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthCheckApi->health_check_pong: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

