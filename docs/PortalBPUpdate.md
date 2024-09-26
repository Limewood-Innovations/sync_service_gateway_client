# PortalBPUpdate


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
**transaction_id** | **str** |  | [optional] [default to 'f55859a5-c25b-42ca-9919-3c8ce58f6571']
**state** | **str** |  | [optional] [default to 'initial']
**creation_date** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from sync_service_gateway_client.models.portal_bp_update import PortalBPUpdate

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


