# sync_service_api_gateway.PortalBPUpdateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal__bp_update_add_portal_bp_update**](PortalBPUpdateApi.md#portal__bp_update_add_portal_bp_update) | **POST** /api/v1/portal_bp_update | Add Portal Bp Update
[**portal__bp_update_find_portal_bp_update_by_state**](PortalBPUpdateApi.md#portal__bp_update_find_portal_bp_update_by_state) | **GET** /api/v1/portal_bp_update/find_by_state/ | Find Portal Bp Update By State
[**portal__bp_update_get_portal_bp_update**](PortalBPUpdateApi.md#portal__bp_update_get_portal_bp_update) | **GET** /api/v1/portal_bp_update | Get Portal Bp Update
[**portal__bp_update_get_portal_bp_update_by_id**](PortalBPUpdateApi.md#portal__bp_update_get_portal_bp_update_by_id) | **GET** /api/v1/portal_bp_update/{transaction_id} | Get Portal Bp Update By Id
[**portal__bp_update_increment_portal_bp_update_retry**](PortalBPUpdateApi.md#portal__bp_update_increment_portal_bp_update_retry) | **PUT** /api/v1/portal_bp_update/{transaction_id}/retry_count | Increment Portal Bp Update Retry
[**portal__bp_update_update_portal_bp_update_state**](PortalBPUpdateApi.md#portal__bp_update_update_portal_bp_update_state) | **PUT** /api/v1/portal_bp_update/{transaction_id}/state | Update Portal Bp Update State


# **portal__bp_update_add_portal_bp_update**
> PortalBPUpdate portal__bp_update_add_portal_bp_update(portal_bp_update_create)

Add Portal Bp Update

Add a new portal business partner update.  This endpoint creates a new business partner update record in the database.  Args:     bp (PortalBPUpdateCreate): The data model for creating a new `PortalBPUpdate` record.     session (AsyncSession): The SQLAlchemy session dependency for asynchronous DB operations.  Returns:     PortalBPUpdate: The newly created `PortalBPUpdate` record.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate
from sync_service_api_gateway.models.portal_bp_update_create import PortalBPUpdateCreate
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = sync_service_api_gateway.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.PortalBPUpdateApi(api_client)
    portal_bp_update_create = sync_service_api_gateway.PortalBPUpdateCreate() # PortalBPUpdateCreate | 

    try:
        # Add Portal Bp Update
        api_response = api_instance.portal__bp_update_add_portal_bp_update(portal_bp_update_create)
        print("The response of PortalBPUpdateApi->portal__bp_update_add_portal_bp_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_add_portal_bp_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_bp_update_create** | [**PortalBPUpdateCreate**](PortalBPUpdateCreate.md)|  | 

### Return type

[**PortalBPUpdate**](PortalBPUpdate.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal__bp_update_find_portal_bp_update_by_state**
> List[PortalBPUpdate] portal__bp_update_find_portal_bp_update_by_state(state)

Find Portal Bp Update By State

Retrieve portal business partner updates by state.  This endpoint fetches all business partner update records from the database by their state.  Args:     state (str): The state of the transactions to search for.     session (AsyncSession): The SQLAlchemy session dependency for asynchronous DB operations.  Returns:     list[PortalBPUpdate]: A list of `PortalBPUpdate` records with the specified state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = sync_service_api_gateway.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.PortalBPUpdateApi(api_client)
    state = 'state_example' # str | 

    try:
        # Find Portal Bp Update By State
        api_response = api_instance.portal__bp_update_find_portal_bp_update_by_state(state)
        print("The response of PortalBPUpdateApi->portal__bp_update_find_portal_bp_update_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_find_portal_bp_update_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**List[PortalBPUpdate]**](PortalBPUpdate.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal__bp_update_get_portal_bp_update**
> List[PortalBPUpdate] portal__bp_update_get_portal_bp_update()

Get Portal Bp Update

Retrieve all portal business partner updates.  This endpoint fetches all records of business partner updates from the database.  Args:     session (AsyncSession): The SQLAlchemy session dependency for asynchronous DB operations.  Returns:     list[PortalBPUpdate]: A list of all `PortalBPUpdate` records in the database.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = sync_service_api_gateway.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.PortalBPUpdateApi(api_client)

    try:
        # Get Portal Bp Update
        api_response = api_instance.portal__bp_update_get_portal_bp_update()
        print("The response of PortalBPUpdateApi->portal__bp_update_get_portal_bp_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_get_portal_bp_update: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortalBPUpdate]**](PortalBPUpdate.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal__bp_update_get_portal_bp_update_by_id**
> PortalBPUpdate portal__bp_update_get_portal_bp_update_by_id(transaction_id)

Get Portal Bp Update By Id

Retrieve a single portal business partner update by transaction ID.  This endpoint fetches a single business partner update record from the database by its transaction ID.  Args:     transaction_id (str): The unique identifier of the transaction.     session (AsyncSession): The SQLAlchemy session dependency for asynchronous DB operations.  Returns:     PortalBPUpdate: The `PortalBPUpdate` record with the specified transaction ID.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = sync_service_api_gateway.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.PortalBPUpdateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Portal Bp Update By Id
        api_response = api_instance.portal__bp_update_get_portal_bp_update_by_id(transaction_id)
        print("The response of PortalBPUpdateApi->portal__bp_update_get_portal_bp_update_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_get_portal_bp_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**PortalBPUpdate**](PortalBPUpdate.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal__bp_update_increment_portal_bp_update_retry**
> PortalBPUpdate portal__bp_update_increment_portal_bp_update_retry(transaction_id)

Increment Portal Bp Update Retry

Increment the retry count of a portal business partner update.  This endpoint increments the retry count of a business partner update record in the database.  Args:     transaction_id (str): The unique identifier of the transaction.     session (AsyncSession): The SQLAlchemy session dependency for asynchronous DB operations.  Returns:     PortalBPUpdate: The updated `PortalBPUpdate` record with the incremented retry count.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = sync_service_api_gateway.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.PortalBPUpdateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Increment Portal Bp Update Retry
        api_response = api_instance.portal__bp_update_increment_portal_bp_update_retry(transaction_id)
        print("The response of PortalBPUpdateApi->portal__bp_update_increment_portal_bp_update_retry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_increment_portal_bp_update_retry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**PortalBPUpdate**](PortalBPUpdate.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal__bp_update_update_portal_bp_update_state**
> PortalBPUpdate portal__bp_update_update_portal_bp_update_state(transaction_id, new_state)

Update Portal Bp Update State

Update the state of a portal business partner update.  This endpoint updates the state of a business partner update record in the database.  Args:     transaction_id (str): The unique identifier of the transaction.     new_state (str): The new state to update the transaction to.     session (AsyncSession): The SQLAlchemy session dependency for asynchronous DB operations.  Returns:     PortalBPUpdate: The updated `PortalBPUpdate` record with the new state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = sync_service_api_gateway.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.PortalBPUpdateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 
    new_state = 'new_state_example' # str | 

    try:
        # Update Portal Bp Update State
        api_response = api_instance.portal__bp_update_update_portal_bp_update_state(transaction_id, new_state)
        print("The response of PortalBPUpdateApi->portal__bp_update_update_portal_bp_update_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_update_portal_bp_update_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **new_state** | **str**|  | 

### Return type

[**PortalBPUpdate**](PortalBPUpdate.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

