# PortalBPUpdateCreate

Model for creating a new PortalBPUpdate instance via API.  This class is used for capturing and handling input when updating a business partner's details in the portal. It extends from the base class `PortalBPUpdateBase`.

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

## Example

```python
from sync_service_api_gateway.models.portal_bp_update_create import PortalBPUpdateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PortalBPUpdateCreate from a JSON string
portal_bp_update_create_instance = PortalBPUpdateCreate.from_json(json)
# print the JSON string representation of the object
print(PortalBPUpdateCreate.to_json())

# convert the object into a dict
portal_bp_update_create_dict = portal_bp_update_create_instance.to_dict()
# create an instance of PortalBPUpdateCreate from a dict
portal_bp_update_create_from_dict = PortalBPUpdateCreate.from_dict(portal_bp_update_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


