# IHCreateCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_ticket_number** | **str** |  | 
**notif_type** | **str** |  | 
**short_text** | **str** |  | 
**long_text** | **str** |  | 
**func_loc** | **str** |  | 
**reported_by** | **str** |  | 
**notif_date** | **datetime** |  | 
**plan_group** | **str** |  | 
**partner_number** | **str** |  | 
**plan_plant** | **str** |  | 
**partner_role** | **str** |  | 
**set_active** | **bool** |  | 

## Example

```python
from sync_service_gateway_client.models.ih_create_create import IHCreateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHCreateCreate from a JSON string
ih_create_create_instance = IHCreateCreate.from_json(json)
# print the JSON string representation of the object
print(IHCreateCreate.to_json())

# convert the object into a dict
ih_create_create_dict = ih_create_create_instance.to_dict()
# create an instance of IHCreateCreate from a dict
ih_create_create_from_dict = IHCreateCreate.from_dict(ih_create_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


