# IHNotificationCloseCreate

Model for creating a new IHNotificationClose entry.  This class is used when handling user input for creating a new IH notification closure via API. Inherits all base fields from IHNotificationCloseBase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_ticket_number** | **str** | The Jira ticket number associated with the notification. | 
**notif_number** | **int** | The unique notification number. | 

## Example

```python
from sync_service_api_gateway.models.ih_notification_close_create import IHNotificationCloseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHNotificationCloseCreate from a JSON string
ih_notification_close_create_instance = IHNotificationCloseCreate.from_json(json)
# print the JSON string representation of the object
print(IHNotificationCloseCreate.to_json())

# convert the object into a dict
ih_notification_close_create_dict = ih_notification_close_create_instance.to_dict()
# create an instance of IHNotificationCloseCreate from a dict
ih_notification_close_create_from_dict = IHNotificationCloseCreate.from_dict(ih_notification_close_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


