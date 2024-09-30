# ApiResource

Represents an API resource response structure.  Attributes:     data (VersionBase): The version information for the API resource.     error (str): An error message, if any occurred while fetching the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VersionBase**](VersionBase.md) |  | 
**error** | **str** |  | 

## Example

```python
from sync_service_api_gateway.models.api_resource import ApiResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResource from a JSON string
api_resource_instance = ApiResource.from_json(json)
# print the JSON string representation of the object
print(ApiResource.to_json())

# convert the object into a dict
api_resource_dict = api_resource_instance.to_dict()
# create an instance of ApiResource from a dict
api_resource_from_dict = ApiResource.from_dict(api_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


