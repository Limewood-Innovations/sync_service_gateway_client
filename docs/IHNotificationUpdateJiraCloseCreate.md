# IHNotificationUpdateJiraCloseCreate

Model for creating a new IHNotificationUpdateJiraClose entry.  This class is used when handling user input for creating a new IH notification closure related to Jira via API. Inherits all base fields from IHNotificationUpdateJiraCloseBase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID from the IH notification close process. | 
**jira_ticket_number** | **str** | The Jira ticket number associated with the notification. | 
**notif_number** | **int** | The notification number for the update. | 

## Example

```python
from sync_service_api_gateway.models.ih_notification_update_jira_close_create import IHNotificationUpdateJiraCloseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHNotificationUpdateJiraCloseCreate from a JSON string
ih_notification_update_jira_close_create_instance = IHNotificationUpdateJiraCloseCreate.from_json(json)
# print the JSON string representation of the object
print(IHNotificationUpdateJiraCloseCreate.to_json())

# convert the object into a dict
ih_notification_update_jira_close_create_dict = ih_notification_update_jira_close_create_instance.to_dict()
# create an instance of IHNotificationUpdateJiraCloseCreate from a dict
ih_notification_update_jira_close_create_from_dict = IHNotificationUpdateJiraCloseCreate.from_dict(ih_notification_update_jira_close_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


