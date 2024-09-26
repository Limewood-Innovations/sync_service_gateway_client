# IHClose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_ticket_number** | **str** |  | 
**notif_number** | **int** |  | 
**transaction_id** | **str** |  | [optional] [default to '62036b58-1055-43c9-8150-ead3309d7812']
**state** | **str** |  | [optional] [default to 'initial']
**creation_date** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from sync_service_gateway_client.models.ih_close import IHClose

# TODO update the JSON string below
json = "{}"
# create an instance of IHClose from a JSON string
ih_close_instance = IHClose.from_json(json)
# print the JSON string representation of the object
print(IHClose.to_json())

# convert the object into a dict
ih_close_dict = ih_close_instance.to_dict()
# create an instance of IHClose from a dict
ih_close_from_dict = IHClose.from_dict(ih_close_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


