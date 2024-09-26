# sync_service_gateway_client.MahnstufeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mahnstufe_mahnstufe_post**](MahnstufeApi.md#add_mahnstufe_mahnstufe_post) | **POST** /mahnstufe | Add Mahnstufe
[**get_mahnstufe_mahnstufe_get**](MahnstufeApi.md#get_mahnstufe_mahnstufe_get) | **GET** /mahnstufe | Get Mahnstufe


# **add_mahnstufe_mahnstufe_post**
> ApiResponse add_mahnstufe_mahnstufe_post(mahnstufe_create)

Add Mahnstufe

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.api_response import ApiResponse
from sync_service_gateway_client.models.mahnstufe_create import MahnstufeCreate
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
    api_instance = sync_service_gateway_client.MahnstufeApi(api_client)
    mahnstufe_create = sync_service_gateway_client.MahnstufeCreate() # MahnstufeCreate | 

    try:
        # Add Mahnstufe
        api_response = api_instance.add_mahnstufe_mahnstufe_post(mahnstufe_create)
        print("The response of MahnstufeApi->add_mahnstufe_mahnstufe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MahnstufeApi->add_mahnstufe_mahnstufe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mahnstufe_create** | [**MahnstufeCreate**](MahnstufeCreate.md)|  | 

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

# **get_mahnstufe_mahnstufe_get**
> List[Mahnstufe] get_mahnstufe_mahnstufe_get()

Get Mahnstufe

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.mahnstufe import Mahnstufe
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
    api_instance = sync_service_gateway_client.MahnstufeApi(api_client)

    try:
        # Get Mahnstufe
        api_response = api_instance.get_mahnstufe_mahnstufe_get()
        print("The response of MahnstufeApi->get_mahnstufe_mahnstufe_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MahnstufeApi->get_mahnstufe_mahnstufe_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Mahnstufe]**](Mahnstufe.md)

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

