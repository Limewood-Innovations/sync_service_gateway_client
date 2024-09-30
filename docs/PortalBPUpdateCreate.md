# PortalBPUpdateCreate

Model for creating a new PortalBPUpdate instance via API.  This model is used for handling user input during business partner updates.

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


