# sync_service_api_gateway.IHNotificationCreateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_h_notification__create_add_ih_notification_create**](IHNotificationCreateApi.md#i_h_notification__create_add_ih_notification_create) | **POST** /api/v1/ih_notification_create | Add Ih Notification Create
[**i_h_notification__create_find_ih_notification_create_by_state**](IHNotificationCreateApi.md#i_h_notification__create_find_ih_notification_create_by_state) | **GET** /api/v1/ih_notification_create/find_by_state/ | Find Ih Notification Create By State
[**i_h_notification__create_get_ih_notification_create**](IHNotificationCreateApi.md#i_h_notification__create_get_ih_notification_create) | **GET** /api/v1/ih_notification_create | Get Ih Notification Create
[**i_h_notification__create_get_ih_notification_create_by_id**](IHNotificationCreateApi.md#i_h_notification__create_get_ih_notification_create_by_id) | **GET** /api/v1/ih_notification_create/{transaction_id} | Get Ih Notification Create By Id
[**i_h_notification__create_increment_ih_notification_create_retry_count**](IHNotificationCreateApi.md#i_h_notification__create_increment_ih_notification_create_retry_count) | **PUT** /api/v1/ih_notification_create/{transaction_id}/retry_count | Increment Ih Notification Create Retry Count
[**i_h_notification__create_update_ih_notification_create_state**](IHNotificationCreateApi.md#i_h_notification__create_update_ih_notification_create_state) | **PUT** /api/v1/ih_notification_create/{transaction_id}/state | Update Ih Notification Create State


# **i_h_notification__create_add_ih_notification_create**
> IHNotificationCreate i_h_notification__create_add_ih_notification_create(ih_notification_create_create)

Add Ih Notification Create

Add a new IHNotificationCreate record.  This endpoint creates a new notification record in the database based on the provided data. Requires API key authentication.  Args:     notification (IHNotificationCreateCreate): The request body containing the data for the new record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationCreate: The created notification record.  Raises:     HTTPException: If a server error occurs during the database transaction.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate
from sync_service_api_gateway.models.ih_notification_create_create import IHNotificationCreateCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCreateApi(api_client)
    ih_notification_create_create = sync_service_api_gateway.IHNotificationCreateCreate() # IHNotificationCreateCreate | 

    try:
        # Add Ih Notification Create
        api_response = api_instance.i_h_notification__create_add_ih_notification_create(ih_notification_create_create)
        print("The response of IHNotificationCreateApi->i_h_notification__create_add_ih_notification_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCreateApi->i_h_notification__create_add_ih_notification_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ih_notification_create_create** | [**IHNotificationCreateCreate**](IHNotificationCreateCreate.md)|  | 

### Return type

[**IHNotificationCreate**](IHNotificationCreate.md)

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

# **i_h_notification__create_find_ih_notification_create_by_state**
> List[IHNotificationCreate] i_h_notification__create_find_ih_notification_create_by_state(state)

Find Ih Notification Create By State

Find all IHNotificationCreate records by state.  This endpoint fetches all notification records that match the provided state value. Requires API key authentication.  Args:     state (str): The state value to filter records by.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[IHNotificationCreate]: List of notification records matching the provided state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCreateApi(api_client)
    state = 'state_example' # str | 

    try:
        # Find Ih Notification Create By State
        api_response = api_instance.i_h_notification__create_find_ih_notification_create_by_state(state)
        print("The response of IHNotificationCreateApi->i_h_notification__create_find_ih_notification_create_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCreateApi->i_h_notification__create_find_ih_notification_create_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**List[IHNotificationCreate]**](IHNotificationCreate.md)

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

# **i_h_notification__create_get_ih_notification_create**
> List[IHNotificationCreate] i_h_notification__create_get_ih_notification_create()

Get Ih Notification Create

Retrieve all IHNotificationCreate records.  This endpoint fetches and returns all IHNotificationCreate records from the database. Requires API key authentication.  Args:     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[IHNotificationCreate]: List of IHNotificationCreate records.  Raises:     HTTPException: If no records are found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCreateApi(api_client)

    try:
        # Get Ih Notification Create
        api_response = api_instance.i_h_notification__create_get_ih_notification_create()
        print("The response of IHNotificationCreateApi->i_h_notification__create_get_ih_notification_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCreateApi->i_h_notification__create_get_ih_notification_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IHNotificationCreate]**](IHNotificationCreate.md)

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

# **i_h_notification__create_get_ih_notification_create_by_id**
> IHNotificationCreate i_h_notification__create_get_ih_notification_create_by_id(transaction_id)

Get Ih Notification Create By Id

Retrieve an IHNotificationCreate record by its transaction ID.  This endpoint fetches a single notification record using the provided transaction ID. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the notification record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationCreate: The notification record corresponding to the transaction ID.  Raises:     HTTPException: If the record is not found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Ih Notification Create By Id
        api_response = api_instance.i_h_notification__create_get_ih_notification_create_by_id(transaction_id)
        print("The response of IHNotificationCreateApi->i_h_notification__create_get_ih_notification_create_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCreateApi->i_h_notification__create_get_ih_notification_create_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**IHNotificationCreate**](IHNotificationCreate.md)

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

# **i_h_notification__create_increment_ih_notification_create_retry_count**
> IHNotificationCreate i_h_notification__create_increment_ih_notification_create_retry_count(transaction_id)

Increment Ih Notification Create Retry Count

Increment the retry count of an IHNotificationCreate record.  This endpoint increments the 'retry_count' field by the provided value. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the notification record.     retry_count (int): The number of retries to add.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationCreate: The updated notification record with incremented retry count.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Increment Ih Notification Create Retry Count
        api_response = api_instance.i_h_notification__create_increment_ih_notification_create_retry_count(transaction_id)
        print("The response of IHNotificationCreateApi->i_h_notification__create_increment_ih_notification_create_retry_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCreateApi->i_h_notification__create_increment_ih_notification_create_retry_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**IHNotificationCreate**](IHNotificationCreate.md)

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

# **i_h_notification__create_update_ih_notification_create_state**
> IHNotificationCreate i_h_notification__create_update_ih_notification_create_state(transaction_id, state)

Update Ih Notification Create State

Update the state of an IHNotificationCreate record.  This endpoint updates the 'state' field of a specified notification record. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the notification record.     state (str): The new state value to be updated.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationCreate: The updated notification record.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 
    state = 'state_example' # str | 

    try:
        # Update Ih Notification Create State
        api_response = api_instance.i_h_notification__create_update_ih_notification_create_state(transaction_id, state)
        print("The response of IHNotificationCreateApi->i_h_notification__create_update_ih_notification_create_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCreateApi->i_h_notification__create_update_ih_notification_create_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**IHNotificationCreate**](IHNotificationCreate.md)

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

