# sync_service_api_gateway.PortalBPIBANMailApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal__bp_iban_mail_add_portal_bp_iban_mail**](PortalBPIBANMailApi.md#portal__bp_iban_mail_add_portal_bp_iban_mail) | **POST** /api/v1/portal_bp_iban_mail | Add Portal Bp Iban Mail
[**portal__bp_iban_mail_find_portal_bp_iban_mail_by_state**](PortalBPIBANMailApi.md#portal__bp_iban_mail_find_portal_bp_iban_mail_by_state) | **GET** /api/v1/portal_bp_iban_mail/find_by_state/ | Find Portal Bp Iban Mail By State
[**portal__bp_iban_mail_get_portal_bp_iban_mail**](PortalBPIBANMailApi.md#portal__bp_iban_mail_get_portal_bp_iban_mail) | **GET** /api/v1/portal_bp_iban_mail | Get Portal Bp Iban Mail
[**portal__bp_iban_mail_get_portal_bp_iban_mail_by_id**](PortalBPIBANMailApi.md#portal__bp_iban_mail_get_portal_bp_iban_mail_by_id) | **GET** /api/v1/portal_bp_iban_mail/{transaction_id} | Get Portal Bp Iban Mail By Id
[**portal__bp_iban_mail_get_portal_bp_update_by_transaction_id**](PortalBPIBANMailApi.md#portal__bp_iban_mail_get_portal_bp_update_by_transaction_id) | **GET** /api/v1/portal_bp_iban_mail/{transaction_id}/parent | Get Portal Bp Update By Transaction Id
[**portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count**](PortalBPIBANMailApi.md#portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count) | **PUT** /api/v1/portal_bp_iban_mail/{transaction_id}/retry_count | Increment Portal Bp Iban Mail Retry Count
[**portal__bp_iban_mail_update_portal_bp_iban_mail_state**](PortalBPIBANMailApi.md#portal__bp_iban_mail_update_portal_bp_iban_mail_state) | **PUT** /api/v1/portal_bp_iban_mail/{transaction_id}/state | Update Portal Bp Iban Mail State


# **portal__bp_iban_mail_add_portal_bp_iban_mail**
> PortalBPIbanMail portal__bp_iban_mail_add_portal_bp_iban_mail(portal_bp_iban_mail_create)

Add Portal Bp Iban Mail

Add a new PortalBPIbanMail record.  This endpoint creates a new IBAN mail record in the database based on the provided data. Requires API key authentication.  Args:     bp (PortalBPIbanMailCreate): The request body containing the data for the new record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPIbanMail: The created IBAN mail record.  Raises:     HTTPException: If a server error occurs during the database transaction.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail
from sync_service_api_gateway.models.portal_bp_iban_mail_create import PortalBPIbanMailCreate
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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)
    portal_bp_iban_mail_create = sync_service_api_gateway.PortalBPIbanMailCreate() # PortalBPIbanMailCreate | 

    try:
        # Add Portal Bp Iban Mail
        api_response = api_instance.portal__bp_iban_mail_add_portal_bp_iban_mail(portal_bp_iban_mail_create)
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_add_portal_bp_iban_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_add_portal_bp_iban_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_bp_iban_mail_create** | [**PortalBPIbanMailCreate**](PortalBPIbanMailCreate.md)|  | 

### Return type

[**PortalBPIbanMail**](PortalBPIbanMail.md)

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

# **portal__bp_iban_mail_find_portal_bp_iban_mail_by_state**
> List[PortalBPIbanMail] portal__bp_iban_mail_find_portal_bp_iban_mail_by_state(state)

Find Portal Bp Iban Mail By State

Find all PortalBPIbanMail records by state.  This endpoint fetches all IBAN mail records that match the provided state value. Requires API key authentication.  Args:     state (str): The state value to filter records by.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[PortalBPIbanMail]: List of IBAN mail records matching the provided state.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail
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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)
    state = 'state_example' # str | 

    try:
        # Find Portal Bp Iban Mail By State
        api_response = api_instance.portal__bp_iban_mail_find_portal_bp_iban_mail_by_state(state)
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_find_portal_bp_iban_mail_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_find_portal_bp_iban_mail_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 

### Return type

[**List[PortalBPIbanMail]**](PortalBPIbanMail.md)

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

# **portal__bp_iban_mail_get_portal_bp_iban_mail**
> List[PortalBPIbanMail] portal__bp_iban_mail_get_portal_bp_iban_mail()

Get Portal Bp Iban Mail

Retrieve all PortalBPIbanMail records.  This endpoint fetches and returns all IBAN mail records from the database. Requires API key authentication.  Args:     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     list[PortalBPIbanMail]: List of IBAN mail records.  Raises:     HTTPException: If no records are found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail
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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)

    try:
        # Get Portal Bp Iban Mail
        api_response = api_instance.portal__bp_iban_mail_get_portal_bp_iban_mail()
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_get_portal_bp_iban_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_get_portal_bp_iban_mail: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortalBPIbanMail]**](PortalBPIbanMail.md)

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

# **portal__bp_iban_mail_get_portal_bp_iban_mail_by_id**
> PortalBPIbanMail portal__bp_iban_mail_get_portal_bp_iban_mail_by_id(transaction_id)

Get Portal Bp Iban Mail By Id

Retrieve a PortalBPIbanMail record by its transaction ID.  This endpoint fetches a single IBAN mail record using the provided transaction ID. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the IBAN mail record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPIbanMail: The IBAN mail record corresponding to the transaction ID.  Raises:     HTTPException: If the record is not found.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail
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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Portal Bp Iban Mail By Id
        api_response = api_instance.portal__bp_iban_mail_get_portal_bp_iban_mail_by_id(transaction_id)
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_get_portal_bp_iban_mail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_get_portal_bp_iban_mail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**PortalBPIbanMail**](PortalBPIbanMail.md)

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

# **portal__bp_iban_mail_get_portal_bp_update_by_transaction_id**
> PortalBPUpdate portal__bp_iban_mail_get_portal_bp_update_by_transaction_id(transaction_id)

Get Portal Bp Update By Transaction Id

Retrieve the parent PortalBPUpdate record by child IBAN mail's transaction ID.  This endpoint fetches the parent PortalBPUpdate record associated with the provided IBAN mail's transaction ID. Requires API key authentication.  Args:     transaction_id (str): The transaction ID of the IBAN mail record.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPUpdate: The parent BP update record.  Raises:     HTTPException: If either the IBAN mail or the parent BP update record is not found.

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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get Portal Bp Update By Transaction Id
        api_response = api_instance.portal__bp_iban_mail_get_portal_bp_update_by_transaction_id(transaction_id)
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_get_portal_bp_update_by_transaction_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_get_portal_bp_update_by_transaction_id: %s\n" % e)
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

# **portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count**
> PortalBPIbanMail portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count(transaction_id)

Increment Portal Bp Iban Mail Retry Count

Increment the retry count of a PortalBPIbanMail record.  This endpoint increments the 'retry_count' field by the provided value. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the IBAN mail record.     retry_count (int): The number of retries to add.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPIbanMail: The updated IBAN mail record with incremented retry count.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail
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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Increment Portal Bp Iban Mail Retry Count
        api_response = api_instance.portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count(transaction_id)
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**PortalBPIbanMail**](PortalBPIbanMail.md)

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

# **portal__bp_iban_mail_update_portal_bp_iban_mail_state**
> PortalBPIbanMail portal__bp_iban_mail_update_portal_bp_iban_mail_state(transaction_id, state)

Update Portal Bp Iban Mail State

Update the state of a PortalBPIbanMail record.  This endpoint updates the 'state' field of a specified IBAN mail record. Requires API key authentication.  Args:     transaction_id (str): The unique transaction ID of the IBAN mail record.     state (str): The new state value to be updated.     session (AsyncSession): The database session, provided by FastAPI dependency injection.  Returns:     PortalBPIbanMail: The updated IBAN mail record.  Raises:     HTTPException: If the record is not found or if a server error occurs during the update.

### Example

* Bearer Authentication (HTTPBearer):

```python
import sync_service_api_gateway
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail
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
    api_instance = sync_service_api_gateway.PortalBPIBANMailApi(api_client)
    transaction_id = 'transaction_id_example' # str | 
    state = 'state_example' # str | 

    try:
        # Update Portal Bp Iban Mail State
        api_response = api_instance.portal__bp_iban_mail_update_portal_bp_iban_mail_state(transaction_id, state)
        print("The response of PortalBPIBANMailApi->portal__bp_iban_mail_update_portal_bp_iban_mail_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalBPIBANMailApi->portal__bp_iban_mail_update_portal_bp_iban_mail_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**PortalBPIbanMail**](PortalBPIbanMail.md)

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

