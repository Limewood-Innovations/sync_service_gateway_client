# PortalBPUpdate

Model for managing business partner updates in the database.  This model extends PortalBPUpdateBase to include transaction metadata for database storage, and is used for both FastAPI endpoints and Alembic migrations.  Attributes:     transaction_id (str): Unique identifier for the transaction, generated as a UUID.     state (str): Current state of the transaction (e.g., 'initial', 'processing', 'completed').     retry_count (int): Number of times the transaction has been retried.     creation_date (datetime): The date when the transaction was created.     last_updated (datetime): The date when the transaction was last updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bpnr** | **str** |  | 
**mail** | **str** |  | 
**mail_change** | **int** |  | 
**mobile** | **str** |  | 
**mobile_change** | **int** |  | 
**iban** | **str** |  | 
**iban_change** | **int** |  | 
**datenschutz** | **str** |  | 
**datenschutz_change** | **int** |  | 
**post** | **str** |  | 
**post_change** | **int** |  | 
**anmeldeid** | **str** |  | 
**anmeldeid_change** | **int** |  | 
**change_timestamp** | **datetime** |  | 
**transaction_id** | **str** |  | [optional] 
**state** | **str** | Current state of the transaction (e.g., &#39;initial&#39;, &#39;processing&#39;, &#39;completed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | Number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | Timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | Timestamp when the transaction was last updated. | [optional] 

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


