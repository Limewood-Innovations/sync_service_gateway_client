# sync_service_api_gateway.OrderDocumentCreateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_document__create_add_order_document_create**](OrderDocumentCreateApi.md#order_document__create_add_order_document_create) | **POST** /api/v1/order_document_create | Add Order Document Create
[**order_document__create_find_order_document_create_by_state**](OrderDocumentCreateApi.md#order_document__create_find_order_document_create_by_state) | **GET** /api/v1/order_document_create/find_by_state/ | Find Order Document Create By State
[**order_document__create_get_ih_notification_create_by_transaction_id**](OrderDocumentCreateApi.md#order_document__create_get_ih_notification_create_by_transaction_id) | **GET** /api/v1/order_document_create/{transaction_id}/parent | Get Ih Notification Create By Transaction Id
[**order_document__create_get_order_document_create**](OrderDocumentCreateApi.md#order_document__create_get_order_document_create) | **GET** /api/v1/order_document_create | Get Order Document Create
[**order_document__create_get_order_document_create_by_id**](OrderDocumentCreateApi.md#order_document__create_get_order_document_create_by_id) | **GET** /api/v1/order_document_create/{transaction_id} | Get Order Document Create By Id
[**order_document__create_increment_order_document_create_retry_count**](OrderDocumentCreateApi.md#order_document__create_increment_order_document_create_retry_count) | **PUT** /api/v1/order_document_create/{transaction_id}/retry_count | Increment Order Document Create Retry Count
[**order_document__create_update_order_document_create_state**](OrderDocumentCreateApi.md#order_document__create_update_order_document_create_state) | **PUT** /api/v1/order_document_create/{transaction_id}/state | Update Order Document Create State


# **order_document__create_add_order_document_create**
> OrderDocumentCreate order_document__create_add_order_document_create(order_document_create_create)

Add Order Document Create

Add a new OrderDocumentCreate record.  This endpoint creates a new order document record in the database based on the provided data. Requires API key authentication.  Args:     order_document (OrderDocumentCreateCreate): The request body containing the data for the new record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     OrderDocumentCreate: The created order document record.  Raises:     HTTPException: If a server error occurs during the database transaction.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.order_document_create import OrderDocumentCreate
from sync_service_api_gateway.models.order_document_create_create import OrderDocumentCreateCreate
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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)
    order_document_create_create = sync_service_api_gateway.OrderDocumentCreateCreate() # OrderDocumentCreateCreate | 

    try:
        # Add Order Document Create
        api_response = api_instance.order_document__create_add_order_document_create(order_document_create_create)
        print("The response of OrderDocumentCreateApi->order_document__create_add_order_document_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_add_order_document_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_document_create_create** | [**OrderDocumentCreateCreate**](OrderDocumentCreateCreate.md)|  | 

### Return type

[**OrderDocumentCreate**](OrderDocumentCreate.md)

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

# **order_document__create_find_order_document_create_by_state**
> List[OrderDocumentCreate] order_document__create_find_order_document_create_by_state(state)

Find Order Document Create By State

Find all OrderDocumentCreate records by state.  This endpoint fetches all OrderDocumentCreate records that match the provided state value. Requires API key authentication.  Args:     state (str): The state value to filter records by.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[OrderDocumentCreate]: List of OrderDocumentCreate records matching the provided state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.order_document_create import OrderDocumentCreate
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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)
    state = 'state_example' # str | 

    try:
        # Find Order Document Create By State
        api_response = api_instance.order_document__create_find_order_document_create_by_state(state)
        print("The response of OrderDocumentCreateApi->order_document__create_find_order_document_create_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_find_order_document_create_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**List[OrderDocumentCreate]**](OrderDocumentCreate.md)

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

# **order_document__create_get_ih_notification_create_by_transaction_id**
> IHNotificationCreate order_document__create_get_ih_notification_create_by_transaction_id(transaction_id)

Get Ih Notification Create By Transaction Id

Retrieve the parent IHNotificationCreate record by child order document's transaction ID.  This endpoint fetches the parent IHNotificationCreate record associated with the provided order document's transaction ID. Requires API key authentication.  Args:     transaction_id (str): The transaction ID of the order document record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     IHNotificationCreate: The parent notification record.  Raises:     HTTPException: If either the order document or the parent notification record is not found.

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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Ih Notification Create By Transaction Id
        api_response = api_instance.order_document__create_get_ih_notification_create_by_transaction_id(transaction_id)
        print("The response of OrderDocumentCreateApi->order_document__create_get_ih_notification_create_by_transaction_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_get_ih_notification_create_by_transaction_id: %s\n" % e)
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

# **order_document__create_get_order_document_create**
> List[OrderDocumentCreate] order_document__create_get_order_document_create()

Get Order Document Create

Retrieve all OrderDocumentCreate records.  This endpoint fetches and returns all OrderDocumentCreate records from the database. Requires API key authentication.  Args:     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[OrderDocumentCreate]: List of OrderDocumentCreate records.  Raises:     HTTPException: If no records are found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.order_document_create import OrderDocumentCreate
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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)

    try:
        # Get Order Document Create
        api_response = api_instance.order_document__create_get_order_document_create()
        print("The response of OrderDocumentCreateApi->order_document__create_get_order_document_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_get_order_document_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrderDocumentCreate]**](OrderDocumentCreate.md)

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

# **order_document__create_get_order_document_create_by_id**
> OrderDocumentCreate order_document__create_get_order_document_create_by_id(transaction_id)

Get Order Document Create By Id

Retrieve an OrderDocumentCreate record by its transaction ID.  This endpoint fetches a single order document record using the provided transaction ID. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the order document record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     OrderDocumentCreate: The order document record corresponding to the transaction ID.  Raises:     HTTPException: If the record is not found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.order_document_create import OrderDocumentCreate
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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Order Document Create By Id
        api_response = api_instance.order_document__create_get_order_document_create_by_id(transaction_id)
        print("The response of OrderDocumentCreateApi->order_document__create_get_order_document_create_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_get_order_document_create_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**OrderDocumentCreate**](OrderDocumentCreate.md)

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

# **order_document__create_increment_order_document_create_retry_count**
> OrderDocumentCreate order_document__create_increment_order_document_create_retry_count(transaction_id)

Increment Order Document Create Retry Count

Increment the retry count of an OrderDocumentCreate record.  This endpoint increments the 'retry_count' field by the provided value. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the order document record.     retry_count (int): The number of retries to add.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     OrderDocumentCreate: The updated OrderDocumentCreate record with incremented retry count.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.order_document_create import OrderDocumentCreate
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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Increment Order Document Create Retry Count
        api_response = api_instance.order_document__create_increment_order_document_create_retry_count(transaction_id)
        print("The response of OrderDocumentCreateApi->order_document__create_increment_order_document_create_retry_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_increment_order_document_create_retry_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**OrderDocumentCreate**](OrderDocumentCreate.md)

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

# **order_document__create_update_order_document_create_state**
> OrderDocumentCreate order_document__create_update_order_document_create_state(transaction_id, state)

Update Order Document Create State

Update the state of an OrderDocumentCreate record.  This endpoint updates the 'state' field of a specified OrderDocumentCreate record. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the order document record.     state (str): The new state value to be updated.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     OrderDocumentCreate: The updated OrderDocumentCreate record.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.order_document_create import OrderDocumentCreate
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
    api_instance = sync_service_api_gateway.OrderDocumentCreateApi(api_client)
    transaction_id = 'transaction_id_example' # str | 
    state = 'state_example' # str | 

    try:
        # Update Order Document Create State
        api_response = api_instance.order_document__create_update_order_document_create_state(transaction_id, state)
        print("The response of OrderDocumentCreateApi->order_document__create_update_order_document_create_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderDocumentCreateApi->order_document__create_update_order_document_create_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**OrderDocumentCreate**](OrderDocumentCreate.md)

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

