# Mahnstufe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bukrs** | **int** |  | 
**customer_number** | **int** |  | 
**dunning_block_reason** | **str** |  | 
**transaction_id** | **str** |  | [optional] [default to '8dd19fc8-1961-4ee2-865e-45aeb263f0e9']
**state** | **str** |  | [optional] [default to 'initial']
**creation_date** | **datetime** |  | [optional] 

## Example

```python
from sync_service_gateway_client.models.mahnstufe import Mahnstufe

# TODO update the JSON string below
json = "{}"
# create an instance of Mahnstufe from a JSON string
mahnstufe_instance = Mahnstufe.from_json(json)
# print the JSON string representation of the object
print(Mahnstufe.to_json())

# convert the object into a dict
mahnstufe_dict = mahnstufe_instance.to_dict()
# create an instance of Mahnstufe from a dict
mahnstufe_from_dict = Mahnstufe.from_dict(mahnstufe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


