# swagger_client.KontoauszugApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kontoauszug_kontoauszug_post**](KontoauszugApi.md#add_kontoauszug_kontoauszug_post) | **POST** /kontoauszug | Add Kontoauszug
[**get_kontoauszug_kontoauszug_get**](KontoauszugApi.md#get_kontoauszug_kontoauszug_get) | **GET** /kontoauszug | Get Kontoauszug

# **add_kontoauszug_kontoauszug_post**
> ApiResponse add_kontoauszug_kontoauszug_post(body)

Add Kontoauszug

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KontoauszugApi()
body = swagger_client.KontoauszugCreate() # KontoauszugCreate | 

try:
    # Add Kontoauszug
    api_response = api_instance.add_kontoauszug_kontoauszug_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KontoauszugApi->add_kontoauszug_kontoauszug_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KontoauszugCreate**](KontoauszugCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kontoauszug_kontoauszug_get**
> object get_kontoauszug_kontoauszug_get()

Get Kontoauszug

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KontoauszugApi()

try:
    # Get Kontoauszug
    api_response = api_instance.get_kontoauszug_kontoauszug_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KontoauszugApi->get_kontoauszug_kontoauszug_get: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

