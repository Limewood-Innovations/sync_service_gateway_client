# sync_service_gateway_client.PortalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portal_bp_update_portal_bp_update_post**](PortalApi.md#add_portal_bp_update_portal_bp_update_post) | **POST** /portal_bp_update | Add Portal Bp Update
[**get_portal_bp_update_portal_bp_update_get**](PortalApi.md#get_portal_bp_update_portal_bp_update_get) | **GET** /portal_bp_update | Get Portal Bp Update


# **add_portal_bp_update_portal_bp_update_post**
> ApiResponse add_portal_bp_update_portal_bp_update_post(portal_bp_update_create)

Add Portal Bp Update

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.api_response import ApiResponse
from sync_service_gateway_client.models.portal_bp_update_create import PortalBPUpdateCreate
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
    api_instance = sync_service_gateway_client.PortalApi(api_client)
    portal_bp_update_create = sync_service_gateway_client.PortalBPUpdateCreate() # PortalBPUpdateCreate | 

    try:
        # Add Portal Bp Update
        api_response = api_instance.add_portal_bp_update_portal_bp_update_post(portal_bp_update_create)
        print("The response of PortalApi->add_portal_bp_update_portal_bp_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalApi->add_portal_bp_update_portal_bp_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_bp_update_create** | [**PortalBPUpdateCreate**](PortalBPUpdateCreate.md)|  | 

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

# **get_portal_bp_update_portal_bp_update_get**
> List[PortalBPUpdate] get_portal_bp_update_portal_bp_update_get()

Get Portal Bp Update

### Example


```python
import sync_service_gateway_client
from sync_service_gateway_client.models.portal_bp_update import PortalBPUpdate
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
    api_instance = sync_service_gateway_client.PortalApi(api_client)

    try:
        # Get Portal Bp Update
        api_response = api_instance.get_portal_bp_update_portal_bp_update_get()
        print("The response of PortalApi->get_portal_bp_update_portal_bp_update_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalApi->get_portal_bp_update_portal_bp_update_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortalBPUpdate]**](PortalBPUpdate.md)

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

