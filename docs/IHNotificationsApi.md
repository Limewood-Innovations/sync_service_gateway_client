# swagger_client.IHNotificationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ihclose_ihclose_post**](IHNotificationsApi.md#add_ihclose_ihclose_post) | **POST** /ihclose | Add Ihclose
[**add_ihcreate_ihcreate_post**](IHNotificationsApi.md#add_ihcreate_ihcreate_post) | **POST** /ihcreate | Add Ihcreate
[**get_ihclose_ihclose_get**](IHNotificationsApi.md#get_ihclose_ihclose_get) | **GET** /ihclose | Get Ihclose
[**get_ihcreate_by_id_ihcreate_transaction_id_get**](IHNotificationsApi.md#get_ihcreate_by_id_ihcreate_transaction_id_get) | **GET** /ihcreate/{transaction_id} | Get Ihcreate By Id
[**get_ihcreate_by_state_ihcreate_find_by_state_post**](IHNotificationsApi.md#get_ihcreate_by_state_ihcreate_find_by_state_post) | **POST** /ihcreate/findByState | Get Ihcreate By State
[**get_ihcreate_ihcreate_get**](IHNotificationsApi.md#get_ihcreate_ihcreate_get) | **GET** /ihcreate | get ihcreate

# **add_ihclose_ihclose_post**
> ApiResponse add_ihclose_ihclose_post(body)

Add Ihclose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IHNotificationsApi()
body = swagger_client.IHCloseCreate() # IHCloseCreate | 

try:
    # Add Ihclose
    api_response = api_instance.add_ihclose_ihclose_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IHNotificationsApi->add_ihclose_ihclose_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IHCloseCreate**](IHCloseCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ihcreate_ihcreate_post**
> ApiResponse add_ihcreate_ihcreate_post(body)

Add Ihcreate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IHNotificationsApi()
body = swagger_client.IHCreateCreate() # IHCreateCreate | 

try:
    # Add Ihcreate
    api_response = api_instance.add_ihcreate_ihcreate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IHNotificationsApi->add_ihcreate_ihcreate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IHCreateCreate**](IHCreateCreate.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ihclose_ihclose_get**
> object get_ihclose_ihclose_get()

Get Ihclose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IHNotificationsApi()

try:
    # Get Ihclose
    api_response = api_instance.get_ihclose_ihclose_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IHNotificationsApi->get_ihclose_ihclose_get: %s\n" % e)
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

# **get_ihcreate_by_id_ihcreate_transaction_id_get**
> IHCreate get_ihcreate_by_id_ihcreate_transaction_id_get(transaction_id)

Get Ihcreate By Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IHNotificationsApi()
transaction_id = NULL # object | 

try:
    # Get Ihcreate By Id
    api_response = api_instance.get_ihcreate_by_id_ihcreate_transaction_id_get(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IHNotificationsApi->get_ihcreate_by_id_ihcreate_transaction_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**object**](.md)|  | 

### Return type

[**IHCreate**](IHCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ihcreate_by_state_ihcreate_find_by_state_post**
> object get_ihcreate_by_state_ihcreate_find_by_state_post(state)

Get Ihcreate By State

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IHNotificationsApi()
state = NULL # object | 

try:
    # Get Ihcreate By State
    api_response = api_instance.get_ihcreate_by_state_ihcreate_find_by_state_post(state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IHNotificationsApi->get_ihcreate_by_state_ihcreate_find_by_state_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ihcreate_ihcreate_get**
> object get_ihcreate_ihcreate_get()

get ihcreate

description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IHNotificationsApi()

try:
    # get ihcreate
    api_response = api_instance.get_ihcreate_ihcreate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IHNotificationsApi->get_ihcreate_ihcreate_get: %s\n" % e)
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

