# sync_service_api_gateway.VersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get_version**](VersionApi.md#version_get_version) | **GET** /api/v1/version/ | Get Version


# **version_get_version**
> ApiResource version_get_version()

Get Version

Endpoint to retrieve the current application version details.  This endpoint returns version information such as the current Git version, raw version, branch name, and build time. These details are obtained from the `Settings` class, which pulls the information from the environment or defaults to \"unknown\".  Args:     request (Request): The FastAPI request object (not used in this example but included for completeness).  Returns:     version.ApiResource: A data model that contains version information (version, raw_version, git_branch, build_time)     and an optional error message (empty in this case).

### Example


```python
import sync_service_api_gateway
from sync_service_api_gateway.models.api_resource import ApiResource
from sync_service_api_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sync_service_api_gateway.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sync_service_api_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_service_api_gateway.VersionApi(api_client)

    try:
        # Get Version
        api_response = api_instance.version_get_version()
        print("The response of VersionApi->version_get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->version_get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResource**](ApiResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

