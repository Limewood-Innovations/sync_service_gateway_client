# IHNotificationCreateCreate

Model for handling user input when creating a new IH Notification.  This class is used when receiving data from the API to create new notifications. Inherits all base fields from IHNotificationCreateBase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_ticket_number** | **str** | The JIRA ticket number associated with the notification. | 
**notif_type** | **str** | The type of the notification. | 
**short_text** | **str** | A brief description or title for the notification. | 
**long_text** | **str** | A more detailed description of the notification. | 
**func_loc** | **str** | The functional location relevant to this notification. | 
**reported_by** | **str** | The user or system that reported the issue. | 
**notif_date** | **datetime** | The date and time when the notification was reported. | 
**plan_group** | **str** | The planning group involved with the notification. | 
**partner_number** | **str** | The business partner number associated with the notification. | 
**plan_plant** | **str** | The planning plant relevant to the notification. | 
**partner_role** | **str** | The role of the business partner in this context. | 
**set_active** | **bool** | Indicates whether the notification is active or inactive. | 

## Example

```python
from sync_service_api_gateway.models.ih_notification_create_create import IHNotificationCreateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHNotificationCreateCreate from a JSON string
ih_notification_create_create_instance = IHNotificationCreateCreate.from_json(json)
# print the JSON string representation of the object
print(IHNotificationCreateCreate.to_json())

# convert the object into a dict
ih_notification_create_create_dict = ih_notification_create_create_instance.to_dict()
# create an instance of IHNotificationCreateCreate from a dict
ih_notification_create_create_from_dict = IHNotificationCreateCreate.from_dict(ih_notification_create_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


