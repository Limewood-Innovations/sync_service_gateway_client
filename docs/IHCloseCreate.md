# IHCloseCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_ticket_number** | **str** |  | 
**notif_number** | **int** |  | 

## Example

```python
from sync_service_gateway_client.models.ih_close_create import IHCloseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHCloseCreate from a JSON string
ih_close_create_instance = IHCloseCreate.from_json(json)
# print the JSON string representation of the object
print(IHCloseCreate.to_json())

# convert the object into a dict
ih_close_create_dict = ih_close_create_instance.to_dict()
# create an instance of IHCloseCreate from a dict
ih_close_create_from_dict = IHCloseCreate.from_dict(ih_close_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


