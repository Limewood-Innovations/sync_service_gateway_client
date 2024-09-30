# VersionBase

Represents version information for a build.  Attributes:     version (str): The version number (e.g., '1.0.0').     raw_version (str): The raw version string from the build system.     git_branch (str): The name of the Git branch associated with this build.     build_time (str): The time when the build was created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**raw_version** | **str** |  | 
**git_branch** | **str** |  | 
**build_time** | **str** |  | 

## Example

```python
from sync_service_api_gateway.models.version_base import VersionBase

# TODO update the JSON string below
json = "{}"
# create an instance of VersionBase from a JSON string
version_base_instance = VersionBase.from_json(json)
# print the JSON string representation of the object
print(VersionBase.to_json())

# convert the object into a dict
version_base_dict = version_base_instance.to_dict()
# create an instance of VersionBase from a dict
version_base_from_dict = VersionBase.from_dict(version_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


