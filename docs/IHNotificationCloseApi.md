# sync_service_api_gateway.IHNotificationCloseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_h_notification__close_add_ih_notification_close**](IHNotificationCloseApi.md#i_h_notification__close_add_ih_notification_close) | **POST** /api/v1/ih_notification_close | Add Ih Notification Close
[**i_h_notification__close_find_ih_notification_close_by_state**](IHNotificationCloseApi.md#i_h_notification__close_find_ih_notification_close_by_state) | **GET** /api/v1/ih_notification_close/find_by_state/ | Find Ih Notification Close By State
[**i_h_notification__close_get_ih_notification_close**](IHNotificationCloseApi.md#i_h_notification__close_get_ih_notification_close) | **GET** /api/v1/ih_notification_close | Get Ih Notification Close
[**i_h_notification__close_get_ih_notification_close_by_id**](IHNotificationCloseApi.md#i_h_notification__close_get_ih_notification_close_by_id) | **GET** /api/v1/ih_notification_close/{transaction_id} | Get Ih Notification Close By Id
[**i_h_notification__close_increment_ih_notification_close_retry_count**](IHNotificationCloseApi.md#i_h_notification__close_increment_ih_notification_close_retry_count) | **PUT** /api/v1/ih_notification_close/{transaction_id}/retry_count | Increment Ih Notification Close Retry Count
[**i_h_notification__close_update_ih_notification_close_state**](IHNotificationCloseApi.md#i_h_notification__close_update_ih_notification_close_state) | **PUT** /api/v1/ih_notification_close/{transaction_id}/state | Update Ih Notification Close State


# **i_h_notification__close_add_ih_notification_close**
> IHNotificationClose i_h_notification__close_add_ih_notification_close(ih_notification_close_create)

Add Ih Notification Close

Add a new IHNotificationClose record.  This endpoint creates a new IH notification closure record in the database based on the provided data. Requires API key authentication.  Args:     notification (IHNotificationCloseCreate): The request body containing the data for the new record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationClose: The created IHNotificationClose record.  Raises:     HTTPException: If a server error occurs during the database transaction.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose
from sync_service_api_gateway.models.ih_notification_close_create import IHNotificationCloseCreate
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
    api_instance = sync_service_api_gateway.IHNotificationCloseApi(api_client)
    ih_notification_close_create = sync_service_api_gateway.IHNotificationCloseCreate() # IHNotificationCloseCreate | 

    try:
        # Add Ih Notification Close
        api_response = api_instance.i_h_notification__close_add_ih_notification_close(ih_notification_close_create)
        print("The response of IHNotificationCloseApi->i_h_notification__close_add_ih_notification_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCloseApi->i_h_notification__close_add_ih_notification_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ih_notification_close_create** | [**IHNotificationCloseCreate**](IHNotificationCloseCreate.md)|  | 

### Return type

[**IHNotificationClose**](IHNotificationClose.md)

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

# **i_h_notification__close_find_ih_notification_close_by_state**
> List[IHNotificationClose] i_h_notification__close_find_ih_notification_close_by_state(state)

Find Ih Notification Close By State

Find all IHNotificationClose records by state.  This endpoint fetches all IHNotificationClose records that match the provided state value. Requires API key authentication.  Args:     state (str): The state value to filter records by.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[IHNotificationClose]: List of IHNotificationClose records matching the provided state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose
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
    api_instance = sync_service_api_gateway.IHNotificationCloseApi(api_client)
    state = 'state_example' # str | 

    try:
        # Find Ih Notification Close By State
        api_response = api_instance.i_h_notification__close_find_ih_notification_close_by_state(state)
        print("The response of IHNotificationCloseApi->i_h_notification__close_find_ih_notification_close_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCloseApi->i_h_notification__close_find_ih_notification_close_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**List[IHNotificationClose]**](IHNotificationClose.md)

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

# **i_h_notification__close_get_ih_notification_close**
> List[IHNotificationClose] i_h_notification__close_get_ih_notification_close()

Get Ih Notification Close

Retrieve all IHNotificationClose records.  This endpoint fetches and returns all IHNotificationClose records from the database. Requires API key authentication.  Args:     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[IHNotificationClose]: List of IHNotificationClose records.  Raises:     HTTPException: If no records are found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose
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
    api_instance = sync_service_api_gateway.IHNotificationCloseApi(api_client)

    try:
        # Get Ih Notification Close
        api_response = api_instance.i_h_notification__close_get_ih_notification_close()
        print("The response of IHNotificationCloseApi->i_h_notification__close_get_ih_notification_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCloseApi->i_h_notification__close_get_ih_notification_close: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IHNotificationClose]**](IHNotificationClose.md)

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

# **i_h_notification__close_get_ih_notification_close_by_id**
> IHNotificationClose i_h_notification__close_get_ih_notification_close_by_id(transaction_id)

Get Ih Notification Close By Id

Retrieve an IHNotificationClose record by its transaction ID.  This endpoint fetches a single notification closure record using the provided transaction ID. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the IHNotificationClose record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationClose: The IHNotificationClose record corresponding to the transaction ID.  Raises:     HTTPException: If the record is not found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose
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
    api_instance = sync_service_api_gateway.IHNotificationCloseApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Ih Notification Close By Id
        api_response = api_instance.i_h_notification__close_get_ih_notification_close_by_id(transaction_id)
        print("The response of IHNotificationCloseApi->i_h_notification__close_get_ih_notification_close_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCloseApi->i_h_notification__close_get_ih_notification_close_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**IHNotificationClose**](IHNotificationClose.md)

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

# **i_h_notification__close_increment_ih_notification_close_retry_count**
> IHNotificationClose i_h_notification__close_increment_ih_notification_close_retry_count(transaction_id)

Increment Ih Notification Close Retry Count

Increment the retry count of an IHNotificationClose record.  This endpoint increments the 'retry_count' field by the provided value. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the IHNotificationClose record.     retry_count (int): The number of retries to add.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationClose: The updated IHNotificationClose record with incremented retry count.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose
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
    api_instance = sync_service_api_gateway.IHNotificationCloseApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Increment Ih Notification Close Retry Count
        api_response = api_instance.i_h_notification__close_increment_ih_notification_close_retry_count(transaction_id)
        print("The response of IHNotificationCloseApi->i_h_notification__close_increment_ih_notification_close_retry_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCloseApi->i_h_notification__close_increment_ih_notification_close_retry_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**IHNotificationClose**](IHNotificationClose.md)

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

# **i_h_notification__close_update_ih_notification_close_state**
> IHNotificationClose i_h_notification__close_update_ih_notification_close_state(transaction_id, state)

Update Ih Notification Close State

Update the state of an IHNotificationClose record.  This endpoint updates the 'state' field of a specified IHNotificationClose record. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the IHNotificationClose record.     state (str): The new state value to be updated.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationClose: The updated IHNotificationClose record.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose
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
    api_instance = sync_service_api_gateway.IHNotificationCloseApi(api_client)
    transaction_id = 'transaction_id_example' # str | 
    state = 'state_example' # str | 

    try:
        # Update Ih Notification Close State
        api_response = api_instance.i_h_notification__close_update_ih_notification_close_state(transaction_id, state)
        print("The response of IHNotificationCloseApi->i_h_notification__close_update_ih_notification_close_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IHNotificationCloseApi->i_h_notification__close_update_ih_notification_close_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**IHNotificationClose**](IHNotificationClose.md)

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

