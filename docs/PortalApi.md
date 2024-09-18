# swagger_client.PortalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portal_bp_update_portal_bp_update_post**](PortalApi.md#add_portal_bp_update_portal_bp_update_post) | **POST** /portal_bp_update | Add Portal Bp Update
[**get_portal_bp_update_portal_bp_update_get**](PortalApi.md#get_portal_bp_update_portal_bp_update_get) | **GET** /portal_bp_update | Get Portal Bp Update

# **add_portal_bp_update_portal_bp_update_post**
> ApiResponse add_portal_bp_update_portal_bp_update_post(body)

Add Portal Bp Update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortalApi()
body = swagger_client.PortalBPUpdateCreate() # PortalBPUpdateCreate | 

try:
    # Add Portal Bp Update
    api_response = api_instance.add_portal_bp_update_portal_bp_update_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->add_portal_bp_update_portal_bp_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalBPUpdateCreate**](PortalBPUpdateCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_bp_update_portal_bp_update_get**
> list[PortalBPUpdate] get_portal_bp_update_portal_bp_update_get()

Get Portal Bp Update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortalApi()

try:
    # Get Portal Bp Update
    api_response = api_instance.get_portal_bp_update_portal_bp_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->get_portal_bp_update_portal_bp_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortalBPUpdate]**](PortalBPUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

