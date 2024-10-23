# PortalBPUpdate

Database model for storing business partner updates.  This model extends `PortalBPUpdateBase` to include metadata for transaction management, such as a unique transaction ID, state tracking, retry count, and timestamps for creation and last update. It is used in FastAPI endpoints and database migrations.  Attributes:     transaction_id (str): A unique identifier for the transaction, generated as a UUID.     state (str): The current state of the transaction (e.g., 'initial', 'processing', 'completed').     retry_count (int): The number of times the transaction has been retried.     creation_date (datetime): The date when the transaction was created.     last_updated (datetime): The date when the transaction was last updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bpnr** | **str** | The Business Partner Number. | 
**mail** | **str** | The email address of the business partner. | 
**mail_change** | **int** | Flag indicating if the email has changed (0 &#x3D; no change, 1 &#x3D; changed). | 
**mobile** | **str** | The mobile phone number of the business partner. | 
**mobile_change** | **int** | Flag indicating if the mobile number has changed (0 &#x3D; no change, 1 &#x3D; changed). | 
**iban** | **str** | The IBAN (International Bank Account Number) of the business partner. | 
**iban_change** | **int** | Flag indicating if the IBAN has changed (0 &#x3D; no change, 1 &#x3D; changed). | 
**datenschutz** | **str** | The data privacy preferences (e.g., consent or refusal). | 
**datenschutz_change** | **int** | Flag indicating if data privacy preferences have changed (0 &#x3D; no change, 1 &#x3D; changed). | 
**post** | **str** | Postal communication preferences of the business partner. | 
**post_change** | **int** | Flag indicating if postal communication preferences have changed (0 &#x3D; no change, 1 &#x3D; changed). | 
**anmeldeid** | **str** | The registration ID of the business partner. | 
**anmeldeid_change** | **int** | Flag indicating if the registration ID has changed (0 &#x3D; no change, 1 &#x3D; changed). | 
**change_timestamp** | **datetime** | The timestamp indicating when the changes were made. | 
**transaction_id** | **str** | A unique transaction ID generated as a UUID. | [optional] 
**state** | **str** | The current state of the transaction (e.g., &#39;initial&#39;, &#39;processing&#39;, &#39;completed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | The number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | The timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | The timestamp when the transaction was last updated. | [optional] 

## Example

```python
from sync_service_api_gateway.models.portal_bp_update import PortalBPUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PortalBPUpdate from a JSON string
portal_bp_update_instance = PortalBPUpdate.from_json(json)
# print the JSON string representation of the object
print(PortalBPUpdate.to_json())

# convert the object into a dict
portal_bp_update_dict = portal_bp_update_instance.to_dict()
# create an instance of PortalBPUpdate from a dict
portal_bp_update_from_dict = PortalBPUpdate.from_dict(portal_bp_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


