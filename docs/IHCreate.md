# IHCreate


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
**transaction_id** | **str** |  | 
**state** | **str** |  | [optional] [default to 'initial']
**creation_date** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from sync_service_gateway_client.models.ih_create import IHCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHCreate from a JSON string
ih_create_instance = IHCreate.from_json(json)
# print the JSON string representation of the object
print(IHCreate.to_json())

# convert the object into a dict
ih_create_dict = ih_create_instance.to_dict()
# create an instance of IHCreate from a dict
ih_create_from_dict = IHCreate.from_dict(ih_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


