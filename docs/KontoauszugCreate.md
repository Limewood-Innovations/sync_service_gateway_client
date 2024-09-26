# KontoauszugCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bukrs** | **int** |  | 
**customer_number** | **int** |  | 
**contract_number** | **str** |  | 
**var_date** | **date** |  | 
**jira_ticket_number** | **str** |  | 
**mode** | **str** |  | 

## Example

```python
from sync_service_gateway_client.models.kontoauszug_create import KontoauszugCreate

# TODO update the JSON string below
json = "{}"
# create an instance of KontoauszugCreate from a JSON string
kontoauszug_create_instance = KontoauszugCreate.from_json(json)
# print the JSON string representation of the object
print(KontoauszugCreate.to_json())

# convert the object into a dict
kontoauszug_create_dict = kontoauszug_create_instance.to_dict()
# create an instance of KontoauszugCreate from a dict
kontoauszug_create_from_dict = KontoauszugCreate.from_dict(kontoauszug_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


