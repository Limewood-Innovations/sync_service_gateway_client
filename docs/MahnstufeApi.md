# swagger_client.MahnstufeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mahnstufe_mahnstufe_post**](MahnstufeApi.md#add_mahnstufe_mahnstufe_post) | **POST** /mahnstufe | Add Mahnstufe
[**get_mahnstufe_mahnstufe_get**](MahnstufeApi.md#get_mahnstufe_mahnstufe_get) | **GET** /mahnstufe | Get Mahnstufe

# **add_mahnstufe_mahnstufe_post**
> ApiResponse add_mahnstufe_mahnstufe_post(body)

Add Mahnstufe

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MahnstufeApi()
body = swagger_client.MahnstufeCreate() # MahnstufeCreate | 

try:
    # Add Mahnstufe
    api_response = api_instance.add_mahnstufe_mahnstufe_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MahnstufeApi->add_mahnstufe_mahnstufe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MahnstufeCreate**](MahnstufeCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mahnstufe_mahnstufe_get**
> list[Mahnstufe] get_mahnstufe_mahnstufe_get()

Get Mahnstufe

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MahnstufeApi()

try:
    # Get Mahnstufe
    api_response = api_instance.get_mahnstufe_mahnstufe_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MahnstufeApi->get_mahnstufe_mahnstufe_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Mahnstufe]**](Mahnstufe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

