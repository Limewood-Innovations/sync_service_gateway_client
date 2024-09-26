# MahnstufeCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bukrs** | **int** |  | 
**customer_number** | **int** |  | 
**dunning_block_reason** | **str** |  | 

## Example

```python
from sync_service_gateway_client.models.mahnstufe_create import MahnstufeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MahnstufeCreate from a JSON string
mahnstufe_create_instance = MahnstufeCreate.from_json(json)
# print the JSON string representation of the object
print(MahnstufeCreate.to_json())

# convert the object into a dict
mahnstufe_create_dict = mahnstufe_create_instance.to_dict()
# create an instance of MahnstufeCreate from a dict
mahnstufe_create_from_dict = MahnstufeCreate.from_dict(mahnstufe_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


