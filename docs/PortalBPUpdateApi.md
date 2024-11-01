# sync_service_api_gateway.PortalBPUpdateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal__bp_update_add_portal_bp_update**](PortalBPUpdateApi.md#portal__bp_update_add_portal_bp_update) | **POST** /api/v1/portal_bp_update | Add Portal Bp Update
[**portal__bp_update_find_portal_bp_update_by_state**](PortalBPUpdateApi.md#portal__bp_update_find_portal_bp_update_by_state) | **GET** /api/v1/portal_bp_update/find_by_state/ | Find Portal Bp Update By State
[**portal__bp_update_get_portal_bp_update**](PortalBPUpdateApi.md#portal__bp_update_get_portal_bp_update) | **GET** /api/v1/portal_bp_update | Get Portal Bp Update
[**portal__bp_update_get_portal_bp_update_by_id**](PortalBPUpdateApi.md#portal__bp_update_get_portal_bp_update_by_id) | **GET** /api/v1/portal_bp_update/{transaction_id} | Get Portal Bp Update By Id
[**portal__bp_update_increment_portal_bp_update_retry_count**](PortalBPUpdateApi.md#portal__bp_update_increment_portal_bp_update_retry_count) | **PUT** /api/v1/portal_bp_update/{transaction_id}/retry_count | Increment Portal Bp Update Retry Count
[**portal__bp_update_update_portal_bp_update_state**](PortalBPUpdateApi.md#portal__bp_update_update_portal_bp_update_state) | **PUT** /api/v1/portal_bp_update/{transaction_id}/state | Update Portal Bp Update State


# **portal__bp_update_add_portal_bp_update**
> PortalBPUpdate portal__bp_update_add_portal_bp_update(portal_bp_update_create)

Add Portal Bp Update

Add a new PortalBPUpdate record.  This endpoint creates a new PortalBPUpdate record in the database based on the provided data. Requires API key authentication.  Args:     bp_update (PortalBPUpdateCreate): The request body containing the data for the new record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPUpdate: The created PortalBPUpdate record.  Raises:     HTTPException: If a server error occurs during the database transaction.

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

Find all PortalBPUpdate records by state.  This endpoint fetches all PortalBPUpdate records that match the provided state value. Requires API key authentication.  Args:     state (str): The state value to filter records by.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[PortalBPUpdate]: List of PortalBPUpdate records matching the provided state.

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

Retrieve all portal business partner updates.  This endpoint fetches and returns all PortalBPUpdate records from the database. Requires API key authentication.  Args:     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[PortalBPUpdate]: List of PortalBPUpdate records.  Raises:     HTTPException: If no records are found.

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

Retrieve a PortalBPUpdate record by its transaction ID.  This endpoint fetches a single PortalBPUpdate record using the provided transaction ID. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the PortalBPUpdate record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPUpdate: The PortalBPUpdate record corresponding to the transaction ID.  Raises:     HTTPException: If the record is not found.

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

# **portal__bp_update_increment_portal_bp_update_retry_count**
> PortalBPUpdate portal__bp_update_increment_portal_bp_update_retry_count(transaction_id)

Increment Portal Bp Update Retry Count

Increment the retry count of a PortalBPUpdate record.  This endpoint increments the 'retry_count' field by the provided value. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the PortalBPUpdate record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPUpdate: The updated PortalBPUpdate record with incremented retry count.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

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
        # Increment Portal Bp Update Retry Count
        api_response = api_instance.portal__bp_update_increment_portal_bp_update_retry_count(transaction_id)
        print("The response of PortalBPUpdateApi->portal__bp_update_increment_portal_bp_update_retry_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_increment_portal_bp_update_retry_count: %s\n" % e)
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
> PortalBPUpdate portal__bp_update_update_portal_bp_update_state(transaction_id, state)

Update Portal Bp Update State

Update the state of a PortalBPUpdate record.  This endpoint updates the 'state' field of a specified PortalBPUpdate record. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the PortalBPUpdate record.     state (str): The new state value to be updated.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPUpdate: The updated PortalBPUpdate record.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

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
    state = 'state_example' # str | 

    try:
        # Update Portal Bp Update State
        api_response = api_instance.portal__bp_update_update_portal_bp_update_state(transaction_id, state)
        print("The response of PortalBPUpdateApi->portal__bp_update_update_portal_bp_update_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPUpdateApi->portal__bp_update_update_portal_bp_update_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **state** | **str**|  | 

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

