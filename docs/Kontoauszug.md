# Kontoauszug


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bukrs** | **int** |  | 
**customer_number** | **int** |  | 
**contract_number** | **str** |  | 
**var_date** | **date** |  | 
**jira_ticket_number** | **str** |  | 
**mode** | **str** |  | 
**transaction_id** | **str** |  | [optional] [default to '0039f3fe-7b2c-423f-a7b5-76e9b6d2c200']
**state** | **str** |  | [optional] [default to 'initial']
**creation_date** | **datetime** |  | [optional] 

## Example

```python
from sync_service_gateway_client.models.kontoauszug import Kontoauszug

# TODO update the JSON string below
json = "{}"
# create an instance of Kontoauszug from a JSON string
kontoauszug_instance = Kontoauszug.from_json(json)
# print the JSON string representation of the object
print(Kontoauszug.to_json())

# convert the object into a dict
kontoauszug_dict = kontoauszug_instance.to_dict()
# create an instance of Kontoauszug from a dict
kontoauszug_from_dict = Kontoauszug.from_dict(kontoauszug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


