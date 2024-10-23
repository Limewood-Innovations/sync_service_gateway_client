# IHNotificationCreate

IH Notification database model for persistence and retrieval.  This model represents the IH Notification entity in the database, with additional fields for transaction tracking and metadata.  Attributes:     transaction_id (str): A unique identifier for the transaction, generated automatically.     state (str): The current state of the transaction (e.g., 'initial', 'success', 'failed').     retry_count (int): The number of retry attempts for the transaction.     creation_date (datetime): The timestamp when the transaction was initially created.     last_updated (datetime): The timestamp when the transaction was last modified.

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
**transaction_id** | **str** | A unique transaction ID, automatically generated. | [optional] 
**state** | **str** | The current state of the transaction (e.g., &#39;initial&#39;, &#39;success&#39;, &#39;failed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | The number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | The timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | The timestamp when the transaction was last updated. | [optional] 

## Example

```python
from sync_service_api_gateway.models.ih_notification_create import IHNotificationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHNotificationCreate from a JSON string
ih_notification_create_instance = IHNotificationCreate.from_json(json)
# print the JSON string representation of the object
print(IHNotificationCreate.to_json())

# convert the object into a dict
ih_notification_create_dict = ih_notification_create_instance.to_dict()
# create an instance of IHNotificationCreate from a dict
ih_notification_create_from_dict = IHNotificationCreate.from_dict(ih_notification_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


