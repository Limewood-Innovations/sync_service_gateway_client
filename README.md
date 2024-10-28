# sync-service-api-gateway
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.2.3
- Generator version: 7.8.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sync_service_api_gateway
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sync_service_api_gateway
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sync_service_api_gateway
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.HealthCheckApi(api_client)

    try:
        # Pong
        api_response = api_instance.health_check_pong()
        print("The response of HealthCheckApi->health_check_pong:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HealthCheckApi->health_check_pong: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HealthCheckApi* | [**health_check_pong**](docs/HealthCheckApi.md#health_check_pong) | **GET** /ping | Pong
*IHNotificationCloseApi* | [**i_h_notification__close_add_ih_notification_close**](docs/IHNotificationCloseApi.md#i_h_notification__close_add_ih_notification_close) | **POST** /api/v1/ih_notification_close | Add Ih Notification Close
*IHNotificationCloseApi* | [**i_h_notification__close_find_ih_notification_close_by_state**](docs/IHNotificationCloseApi.md#i_h_notification__close_find_ih_notification_close_by_state) | **GET** /api/v1/ih_notification_close/find_by_state/ | Find Ih Notification Close By State
*IHNotificationCloseApi* | [**i_h_notification__close_get_ih_notification_close**](docs/IHNotificationCloseApi.md#i_h_notification__close_get_ih_notification_close) | **GET** /api/v1/ih_notification_close | Get Ih Notification Close
*IHNotificationCloseApi* | [**i_h_notification__close_get_ih_notification_close_by_id**](docs/IHNotificationCloseApi.md#i_h_notification__close_get_ih_notification_close_by_id) | **GET** /api/v1/ih_notification_close/{transaction_id} | Get Ih Notification Close By Id
*IHNotificationCloseApi* | [**i_h_notification__close_increment_ih_notification_close_retry_count**](docs/IHNotificationCloseApi.md#i_h_notification__close_increment_ih_notification_close_retry_count) | **PUT** /api/v1/ih_notification_close/{transaction_id}/retry_count | Increment Ih Notification Close Retry Count
*IHNotificationCloseApi* | [**i_h_notification__close_update_ih_notification_close_state**](docs/IHNotificationCloseApi.md#i_h_notification__close_update_ih_notification_close_state) | **PUT** /api/v1/ih_notification_close/{transaction_id}/state | Update Ih Notification Close State
*IHNotificationCreateApi* | [**i_h_notification__create_add_ih_notification_create**](docs/IHNotificationCreateApi.md#i_h_notification__create_add_ih_notification_create) | **POST** /api/v1/ih_notification_create | Add Ih Notification Create
*IHNotificationCreateApi* | [**i_h_notification__create_find_ih_notification_create_by_state**](docs/IHNotificationCreateApi.md#i_h_notification__create_find_ih_notification_create_by_state) | **GET** /api/v1/ih_notification_create/find_by_state/ | Find Ih Notification Create By State
*IHNotificationCreateApi* | [**i_h_notification__create_get_ih_notification_create**](docs/IHNotificationCreateApi.md#i_h_notification__create_get_ih_notification_create) | **GET** /api/v1/ih_notification_create | Get Ih Notification Create
*IHNotificationCreateApi* | [**i_h_notification__create_get_ih_notification_create_by_id**](docs/IHNotificationCreateApi.md#i_h_notification__create_get_ih_notification_create_by_id) | **GET** /api/v1/ih_notification_create/{transaction_id} | Get Ih Notification Create By Id
*IHNotificationCreateApi* | [**i_h_notification__create_increment_ih_notification_create_retry_count**](docs/IHNotificationCreateApi.md#i_h_notification__create_increment_ih_notification_create_retry_count) | **PUT** /api/v1/ih_notification_create/{transaction_id}/retry_count | Increment Ih Notification Create Retry Count
*IHNotificationCreateApi* | [**i_h_notification__create_update_ih_notification_create_state**](docs/IHNotificationCreateApi.md#i_h_notification__create_update_ih_notification_create_state) | **PUT** /api/v1/ih_notification_create/{transaction_id}/state | Update Ih Notification Create State
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_add_ih_notification_update_jira_close**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_add_ih_notification_update_jira_close) | **POST** /api/v1/ih_notification_jira_update_close | Add Ih Notification Update Jira Close
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_find_ih_notification_update_jira_close_by_state**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_find_ih_notification_update_jira_close_by_state) | **GET** /api/v1/ih_notification_jira_update_close/find_by_state/ | Find Ih Notification Update Jira Close By State
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_get_ih_notification_close_by_transaction_id**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_get_ih_notification_close_by_transaction_id) | **GET** /api/v1/ih_notification_jira_update_close/{transaction_id}/parent | Get Ih Notification Close By Transaction Id
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_get_ih_notification_update_jira_close**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_get_ih_notification_update_jira_close) | **GET** /api/v1/ih_notification_jira_update_close | Get Ih Notification Update Jira Close
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_get_ih_notification_update_jira_close_by_id**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_get_ih_notification_update_jira_close_by_id) | **GET** /api/v1/ih_notification_jira_update_close/{transaction_id} | Get Ih Notification Update Jira Close By Id
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_increment_ih_notification_update_jira_close_retry_count**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_increment_ih_notification_update_jira_close_retry_count) | **PUT** /api/v1/ih_notification_jira_update_close/{transaction_id}/retry_count | Increment Ih Notification Update Jira Close Retry Count
*IHNotificationJiraUpdateCloseApi* | [**i_h_notification__jira_update_close_update_ih_notification_update_jira_close_state**](docs/IHNotificationJiraUpdateCloseApi.md#i_h_notification__jira_update_close_update_ih_notification_update_jira_close_state) | **PUT** /api/v1/ih_notification_jira_update_close/{transaction_id}/state | Update Ih Notification Update Jira Close State
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_add_ih_notification_update_jira_create**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_add_ih_notification_update_jira_create) | **POST** /api/v1/ih_notification_jira_update_create | Add Ih Notification Update Jira Create
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_find_ih_notification_update_jira_create_by_state**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_find_ih_notification_update_jira_create_by_state) | **GET** /api/v1/ih_notification_jira_update_create/find_by_state/ | Find Ih Notification Update Jira Create By State
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_get_ih_notification_create_by_transaction_id**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_get_ih_notification_create_by_transaction_id) | **GET** /api/v1/ih_notification_jira_update_create/{transaction_id}/parent | Get Ih Notification Create By Transaction Id
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_get_ih_notification_update_jira_create**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_get_ih_notification_update_jira_create) | **GET** /api/v1/ih_notification_jira_update_create | Get Ih Notification Update Jira Create
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_get_ih_notification_update_jira_create_by_id**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_get_ih_notification_update_jira_create_by_id) | **GET** /api/v1/ih_notification_jira_update_create/{transaction_id} | Get Ih Notification Update Jira Create By Id
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_increment_ih_notification_update_jira_create_retry_count**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_increment_ih_notification_update_jira_create_retry_count) | **PUT** /api/v1/ih_notification_jira_update_create/{transaction_id}/retry_count | Increment Ih Notification Update Jira Create Retry Count
*IHNotificationJiraUpdateCreateApi* | [**i_h_notification__jira_update_create_update_ih_notification_update_jira_create_state**](docs/IHNotificationJiraUpdateCreateApi.md#i_h_notification__jira_update_create_update_ih_notification_update_jira_create_state) | **PUT** /api/v1/ih_notification_jira_update_create/{transaction_id}/state | Update Ih Notification Update Jira Create State
*OrderDocumentCreateApi* | [**order_document__create_add_order_document_create**](docs/OrderDocumentCreateApi.md#order_document__create_add_order_document_create) | **POST** /api/v1/order_document_create | Add Order Document Create
*OrderDocumentCreateApi* | [**order_document__create_find_order_document_create_by_state**](docs/OrderDocumentCreateApi.md#order_document__create_find_order_document_create_by_state) | **GET** /api/v1/order_document_create/find_by_state/ | Find Order Document Create By State
*OrderDocumentCreateApi* | [**order_document__create_get_ih_notification_create_by_transaction_id**](docs/OrderDocumentCreateApi.md#order_document__create_get_ih_notification_create_by_transaction_id) | **GET** /api/v1/order_document_create/{transaction_id}/parent | Get Ih Notification Create By Transaction Id
*OrderDocumentCreateApi* | [**order_document__create_get_order_document_create**](docs/OrderDocumentCreateApi.md#order_document__create_get_order_document_create) | **GET** /api/v1/order_document_create | Get Order Document Create
*OrderDocumentCreateApi* | [**order_document__create_get_order_document_create_by_id**](docs/OrderDocumentCreateApi.md#order_document__create_get_order_document_create_by_id) | **GET** /api/v1/order_document_create/{transaction_id} | Get Order Document Create By Id
*OrderDocumentCreateApi* | [**order_document__create_increment_order_document_create_retry_count**](docs/OrderDocumentCreateApi.md#order_document__create_increment_order_document_create_retry_count) | **PUT** /api/v1/order_document_create/{transaction_id}/retry_count | Increment Order Document Create Retry Count
*OrderDocumentCreateApi* | [**order_document__create_update_order_document_create_state**](docs/OrderDocumentCreateApi.md#order_document__create_update_order_document_create_state) | **PUT** /api/v1/order_document_create/{transaction_id}/state | Update Order Document Create State
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_add_portal_bp_iban_mail**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_add_portal_bp_iban_mail) | **POST** /api/v1/portal_bp_iban_mail | Add Portal Bp Iban Mail
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_find_portal_bp_iban_mail_by_state**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_find_portal_bp_iban_mail_by_state) | **GET** /api/v1/portal_bp_iban_mail/find_by_state/ | Find Portal Bp Iban Mail By State
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_get_portal_bp_iban_mail**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_get_portal_bp_iban_mail) | **GET** /api/v1/portal_bp_iban_mail | Get Portal Bp Iban Mail
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_get_portal_bp_iban_mail_by_id**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_get_portal_bp_iban_mail_by_id) | **GET** /api/v1/portal_bp_iban_mail/{transaction_id} | Get Portal Bp Iban Mail By Id
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_get_portal_bp_update_by_transaction_id**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_get_portal_bp_update_by_transaction_id) | **GET** /api/v1/portal_bp_iban_mail/{transaction_id}/parent | Get Portal Bp Update By Transaction Id
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_increment_portal_bp_iban_mail_retry_count) | **PUT** /api/v1/portal_bp_iban_mail/{transaction_id}/retry_count | Increment Portal Bp Iban Mail Retry Count
*PortalBPIBANMailApi* | [**portal__bp_iban_mail_update_portal_bp_iban_mail_state**](docs/PortalBPIBANMailApi.md#portal__bp_iban_mail_update_portal_bp_iban_mail_state) | **PUT** /api/v1/portal_bp_iban_mail/{transaction_id}/state | Update Portal Bp Iban Mail State
*PortalBPUpdateApi* | [**portal__bp_update_add_portal_bp_update**](docs/PortalBPUpdateApi.md#portal__bp_update_add_portal_bp_update) | **POST** /api/v1/portal_bp_update | Add Portal Bp Update
*PortalBPUpdateApi* | [**portal__bp_update_find_portal_bp_update_by_state**](docs/PortalBPUpdateApi.md#portal__bp_update_find_portal_bp_update_by_state) | **GET** /api/v1/portal_bp_update/find_by_state/ | Find Portal Bp Update By State
*PortalBPUpdateApi* | [**portal__bp_update_get_portal_bp_update**](docs/PortalBPUpdateApi.md#portal__bp_update_get_portal_bp_update) | **GET** /api/v1/portal_bp_update | Get Portal Bp Update
*PortalBPUpdateApi* | [**portal__bp_update_get_portal_bp_update_by_id**](docs/PortalBPUpdateApi.md#portal__bp_update_get_portal_bp_update_by_id) | **GET** /api/v1/portal_bp_update/{transaction_id} | Get Portal Bp Update By Id
*PortalBPUpdateApi* | [**portal__bp_update_increment_portal_bp_update_retry_count**](docs/PortalBPUpdateApi.md#portal__bp_update_increment_portal_bp_update_retry_count) | **PUT** /api/v1/portal_bp_update/{transaction_id}/retry_count | Increment Portal Bp Update Retry Count
*PortalBPUpdateApi* | [**portal__bp_update_update_portal_bp_update_state**](docs/PortalBPUpdateApi.md#portal__bp_update_update_portal_bp_update_state) | **PUT** /api/v1/portal_bp_update/{transaction_id}/state | Update Portal Bp Update State
*SendOrderDocumentApi* | [**send_order_document_add_send_order_document**](docs/SendOrderDocumentApi.md#send_order_document_add_send_order_document) | **POST** /api/v1/send_order_document | Add Send Order Document
*SendOrderDocumentApi* | [**send_order_document_find_send_order_document_by_state**](docs/SendOrderDocumentApi.md#send_order_document_find_send_order_document_by_state) | **GET** /api/v1/send_order_document/find_by_state/ | Find Send Order Document By State
*SendOrderDocumentApi* | [**send_order_document_get_order_document_create_by_transaction_id**](docs/SendOrderDocumentApi.md#send_order_document_get_order_document_create_by_transaction_id) | **GET** /api/v1/send_order_document/{transaction_id}/parent | Get Order Document Create By Transaction Id
*SendOrderDocumentApi* | [**send_order_document_get_send_order_document**](docs/SendOrderDocumentApi.md#send_order_document_get_send_order_document) | **GET** /api/v1/send_order_document | Get Send Order Document
*SendOrderDocumentApi* | [**send_order_document_get_send_order_document_by_id**](docs/SendOrderDocumentApi.md#send_order_document_get_send_order_document_by_id) | **GET** /api/v1/send_order_document/{transaction_id} | Get Send Order Document By Id
*SendOrderDocumentApi* | [**send_order_document_increment_send_order_document_retry_count**](docs/SendOrderDocumentApi.md#send_order_document_increment_send_order_document_retry_count) | **PUT** /api/v1/send_order_document/{transaction_id}/retry_count | Increment Send Order Document Retry Count
*SendOrderDocumentApi* | [**send_order_document_update_send_order_document_state**](docs/SendOrderDocumentApi.md#send_order_document_update_send_order_document_state) | **PUT** /api/v1/send_order_document/{transaction_id}/state | Update Send Order Document State
*VersionApi* | [**version_get_version**](docs/VersionApi.md#version_get_version) | **GET** /api/v1/version/ | Get Version


## Documentation For Models

 - [ApiResource](docs/ApiResource.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [IHNotificationClose](docs/IHNotificationClose.md)
 - [IHNotificationCloseCreate](docs/IHNotificationCloseCreate.md)
 - [IHNotificationCreate](docs/IHNotificationCreate.md)
 - [IHNotificationCreateCreate](docs/IHNotificationCreateCreate.md)
 - [IHNotificationUpdateJiraClose](docs/IHNotificationUpdateJiraClose.md)
 - [IHNotificationUpdateJiraCloseCreate](docs/IHNotificationUpdateJiraCloseCreate.md)
 - [IHNotificationUpdateJiraCreate](docs/IHNotificationUpdateJiraCreate.md)
 - [IHNotificationUpdateJiraCreateCreate](docs/IHNotificationUpdateJiraCreateCreate.md)
 - [OrderDocumentCreate](docs/OrderDocumentCreate.md)
 - [OrderDocumentCreateCreate](docs/OrderDocumentCreateCreate.md)
 - [PortalBPIbanMail](docs/PortalBPIbanMail.md)
 - [PortalBPIbanMailCreate](docs/PortalBPIbanMailCreate.md)
 - [PortalBPUpdate](docs/PortalBPUpdate.md)
 - [PortalBPUpdateCreate](docs/PortalBPUpdateCreate.md)
 - [SendOrderDocument](docs/SendOrderDocument.md)
 - [SendOrderDocumentCreate](docs/SendOrderDocumentCreate.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [VersionBase](docs/VersionBase.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="HTTPBearer"></a>
### HTTPBearer

- **Type**: Bearer authentication


## Author




