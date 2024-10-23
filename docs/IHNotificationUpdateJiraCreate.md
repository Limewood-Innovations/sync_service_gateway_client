# IHNotificationUpdateJiraCreate

Model for persisting and retrieving Jira-related IH Notification updates.  This model represents the database structure for the Jira update transactions, with additional fields for tracking the transaction status and metadata.  Attributes:     transaction_id (str): A unique identifier for the Jira update transaction.     state (str): The current state of the transaction (e.g., 'initial', 'processing', 'completed').     retry_count (int): The number of retry attempts for the transaction.     creation_date (datetime): The timestamp when the transaction was created.     last_updated (datetime): The timestamp when the transaction was last updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID from the IH notification creation process. | 
**jira_ticket_number** | **str** | The Jira ticket number associated with the notification. | 
**notif_number** | **int** | The notification number for the update. | 
**transaction_id** | **str** | A unique transaction ID, automatically generated for the Jira update. | [optional] 
**state** | **str** | The current state of the transaction (e.g., &#39;initial&#39;, &#39;processing&#39;, &#39;completed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | The number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | The timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | The timestamp when the transaction was last updated. | [optional] 

## Example

```python
from sync_service_api_gateway.models.ih_notification_update_jira_create import IHNotificationUpdateJiraCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IHNotificationUpdateJiraCreate from a JSON string
ih_notification_update_jira_create_instance = IHNotificationUpdateJiraCreate.from_json(json)
# print the JSON string representation of the object
print(IHNotificationUpdateJiraCreate.to_json())

# convert the object into a dict
ih_notification_update_jira_create_dict = ih_notification_update_jira_create_instance.to_dict()
# create an instance of IHNotificationUpdateJiraCreate from a dict
ih_notification_update_jira_create_from_dict = IHNotificationUpdateJiraCreate.from_dict(ih_notification_update_jira_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


