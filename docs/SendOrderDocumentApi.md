# sync_service_api_gateway.SendOrderDocumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_order_document_add_send_order_document**](SendOrderDocumentApi.md#send_order_document_add_send_order_document) | **POST** /api/v1/send_order_document | Add Send Order Document
[**send_order_document_find_send_order_document_by_state**](SendOrderDocumentApi.md#send_order_document_find_send_order_document_by_state) | **GET** /api/v1/send_order_document/find_by_state/ | Find Send Order Document By State
[**send_order_document_get_order_document_create_by_transaction_id**](SendOrderDocumentApi.md#send_order_document_get_order_document_create_by_transaction_id) | **GET** /api/v1/send_order_document/{transaction_id}/parent | Get Order Document Create By Transaction Id
[**send_order_document_get_send_order_document**](SendOrderDocumentApi.md#send_order_document_get_send_order_document) | **GET** /api/v1/send_order_document | Get Send Order Document
[**send_order_document_get_send_order_document_by_id**](SendOrderDocumentApi.md#send_order_document_get_send_order_document_by_id) | **GET** /api/v1/send_order_document/{transaction_id} | Get Send Order Document By Id
[**send_order_document_increment_send_order_document_retry_count**](SendOrderDocumentApi.md#send_order_document_increment_send_order_document_retry_count) | **PUT** /api/v1/send_order_document/{transaction_id}/retry_count | Increment Send Order Document Retry Count
[**send_order_document_update_send_order_document_state**](SendOrderDocumentApi.md#send_order_document_update_send_order_document_state) | **PUT** /api/v1/send_order_document/{transaction_id}/state | Update Send Order Document State


# **send_order_document_add_send_order_document**
> SendOrderDocument send_order_document_add_send_order_document(send_order_document_create)

Add Send Order Document

Add a new SendOrderDocument record.  This endpoint creates a new SendOrderDocument record in the database based on the provided data. Requires API key authentication.  Args:     send_order (SendOrderDocumentCreate): The request body containing the data for the new record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     SendOrderDocument: The created SendOrderDocument record.  Raises:     HTTPException: If a server error occurs during the database transaction.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.send_order_document import SendOrderDocument
from sync_service_api_gateway.models.send_order_document_create import SendOrderDocumentCreate
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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)
    send_order_document_create = sync_service_api_gateway.SendOrderDocumentCreate() # SendOrderDocumentCreate | 

    try:
        # Add Send Order Document
        api_response = api_instance.send_order_document_add_send_order_document(send_order_document_create)
        print("The response of SendOrderDocumentApi->send_order_document_add_send_order_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_add_send_order_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_order_document_create** | [**SendOrderDocumentCreate**](SendOrderDocumentCreate.md)|  | 

### Return type

[**SendOrderDocument**](SendOrderDocument.md)

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

# **send_order_document_find_send_order_document_by_state**
> List[SendOrderDocument] send_order_document_find_send_order_document_by_state(state)

Find Send Order Document By State

Find all SendOrderDocument records by state.  This endpoint fetches all SendOrderDocument records that match the provided state value. Requires API key authentication.  Args:     state (str): The state value to filter records by.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[SendOrderDocument]: List of SendOrderDocument records matching the provided state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.send_order_document import SendOrderDocument
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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)
    state = 'state_example' # str | 

    try:
        # Find Send Order Document By State
        api_response = api_instance.send_order_document_find_send_order_document_by_state(state)
        print("The response of SendOrderDocumentApi->send_order_document_find_send_order_document_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_find_send_order_document_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**List[SendOrderDocument]**](SendOrderDocument.md)

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

# **send_order_document_get_order_document_create_by_transaction_id**
> OrderDocumentCreate send_order_document_get_order_document_create_by_transaction_id(transaction_id)

Get Order Document Create By Transaction Id

Retrieve the parent OrderDocumentCreate record by child SendOrderDocument's transaction ID.  This endpoint fetches the parent OrderDocumentCreate record associated with the provided SendOrderDocument's transaction ID. Requires API key authentication.  Args:     transaction_id (str): The transaction ID of the SendOrderDocument record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     OrderDocumentCreate: The parent order document record.  Raises:     HTTPException: If either the SendOrderDocument or the parent order document record is not found.

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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Order Document Create By Transaction Id
        api_response = api_instance.send_order_document_get_order_document_create_by_transaction_id(transaction_id)
        print("The response of SendOrderDocumentApi->send_order_document_get_order_document_create_by_transaction_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_get_order_document_create_by_transaction_id: %s\n" % e)
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

# **send_order_document_get_send_order_document**
> List[SendOrderDocument] send_order_document_get_send_order_document()

Get Send Order Document

Retrieve all SendOrderDocument records.  This endpoint fetches and returns all SendOrderDocument records from the database. Requires API key authentication.  Args:     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[SendOrderDocument]: List of SendOrderDocument records.  Raises:     HTTPException: If no records are found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.send_order_document import SendOrderDocument
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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)

    try:
        # Get Send Order Document
        api_response = api_instance.send_order_document_get_send_order_document()
        print("The response of SendOrderDocumentApi->send_order_document_get_send_order_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_get_send_order_document: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SendOrderDocument]**](SendOrderDocument.md)

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

# **send_order_document_get_send_order_document_by_id**
> SendOrderDocument send_order_document_get_send_order_document_by_id(transaction_id)

Get Send Order Document By Id

Retrieve a SendOrderDocument record by its transaction ID.  This endpoint fetches a single SendOrderDocument record using the provided transaction ID. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the SendOrderDocument record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     SendOrderDocument: The SendOrderDocument record corresponding to the transaction ID.  Raises:     HTTPException: If the record is not found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.send_order_document import SendOrderDocument
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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Send Order Document By Id
        api_response = api_instance.send_order_document_get_send_order_document_by_id(transaction_id)
        print("The response of SendOrderDocumentApi->send_order_document_get_send_order_document_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_get_send_order_document_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**SendOrderDocument**](SendOrderDocument.md)

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

# **send_order_document_increment_send_order_document_retry_count**
> SendOrderDocument send_order_document_increment_send_order_document_retry_count(transaction_id)

Increment Send Order Document Retry Count

Increment the retry count of a SendOrderDocument record.  This endpoint increments the 'retry_count' field by the provided value. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the SendOrderDocument record.     retry_count (int): The number of retries to add.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     SendOrderDocument: The updated SendOrderDocument record with incremented retry count.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.send_order_document import SendOrderDocument
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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Increment Send Order Document Retry Count
        api_response = api_instance.send_order_document_increment_send_order_document_retry_count(transaction_id)
        print("The response of SendOrderDocumentApi->send_order_document_increment_send_order_document_retry_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_increment_send_order_document_retry_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**SendOrderDocument**](SendOrderDocument.md)

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

# **send_order_document_update_send_order_document_state**
> SendOrderDocument send_order_document_update_send_order_document_state(transaction_id, state)

Update Send Order Document State

Update the state of a SendOrderDocument record.  This endpoint updates the 'state' field of a specified SendOrderDocument record. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the SendOrderDocument record.     state (str): The new state value to be updated.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     SendOrderDocument: The updated SendOrderDocument record.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.send_order_document import SendOrderDocument
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
    api_instance = sync_service_api_gateway.SendOrderDocumentApi(api_client)
    transaction_id = 'transaction_id_example' # str | 
    state = 'state_example' # str | 

    try:
        # Update Send Order Document State
        api_response = api_instance.send_order_document_update_send_order_document_state(transaction_id, state)
        print("The response of SendOrderDocumentApi->send_order_document_update_send_order_document_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendOrderDocumentApi->send_order_document_update_send_order_document_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**SendOrderDocument**](SendOrderDocument.md)

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

