# PortalBPIbanMailCreate

Model for creating new entries in the `PortalBPIbanMail` table.  Inherits from `PortalBPIbanMailBase` and doesn't add any new fields. Used in creation operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID for the main transaction. | 
**bpnr** | **str** | The Business Partner Number. | 
**iban** | **str** | The IBAN (International Bank Account Number) for the business partner. | 

## Example

```python
from sync_service_api_gateway.models.portal_bp_iban_mail_create import PortalBPIbanMailCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PortalBPIbanMailCreate from a JSON string
portal_bp_iban_mail_create_instance = PortalBPIbanMailCreate.from_json(json)
# print the JSON string representation of the object
print(PortalBPIbanMailCreate.to_json())

# convert the object into a dict
portal_bp_iban_mail_create_dict = portal_bp_iban_mail_create_instance.to_dict()
# create an instance of PortalBPIbanMailCreate from a dict
portal_bp_iban_mail_create_from_dict = PortalBPIbanMailCreate.from_dict(portal_bp_iban_mail_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


