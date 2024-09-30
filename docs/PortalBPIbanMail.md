# PortalBPIbanMail

Model for reading and storing additional metadata for IBAN and email transactions.  Extends `PortalBPIbanMailBase` by adding metadata such as transaction ID, state, retry count, and timestamps for creation and last update.  Attributes:     transaction_id (str): A unique transaction ID, auto-generated as a UUID.     state (str): The current state of the transaction (e.g., 'initial', 'processing', 'completed').     retry_count (int): The number of times the transaction has been retried.     creation_date (datetime): The timestamp when the transaction was created.     last_updated (datetime): The timestamp when the transaction was last updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID for the main transaction. | 
**bpnr** | **str** | The Business Partner Number. | 
**iban** | **str** | The IBAN (International Bank Account Number) for the business partner. | 
**transaction_id** | **str** | Unique ID for this transaction, generated as a UUID. | [optional] 
**state** | **str** | Current state of the transaction (e.g., &#39;initial&#39;, &#39;processing&#39;, &#39;completed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | Number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | Timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | Timestamp when the transaction was last updated. | [optional] 

## Example

```python
from sync_service_api_gateway.models.portal_bp_iban_mail import PortalBPIbanMail

# TODO update the JSON string below
json = "{}"
# create an instance of PortalBPIbanMail from a JSON string
portal_bp_iban_mail_instance = PortalBPIbanMail.from_json(json)
# print the JSON string representation of the object
print(PortalBPIbanMail.to_json())

# convert the object into a dict
portal_bp_iban_mail_dict = portal_bp_iban_mail_instance.to_dict()
# create an instance of PortalBPIbanMail from a dict
portal_bp_iban_mail_from_dict = PortalBPIbanMail.from_dict(portal_bp_iban_mail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


