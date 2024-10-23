# IHNotificationClose

Database model for persisting IH notification closures.  This model represents the IHNotificationClose entity in the database and is used to return data to the user via API. It includes additional fields for tracking the transaction state and metadata.  Attributes:     transaction_id (str): A unique identifier for the transaction, generated automatically.     state (str): The current state of the transaction (e.g., 'initial', 'processing', 'completed').     retry_count (int): The number of retry attempts for the transaction.     creation_date (datetime): The timestamp when the transaction was initially created.     last_updated (datetime): The timestamp when the transaction was last updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_ticket_number** | **str** | The Jira ticket number associated with the notification. | 
**notif_number** | **int** | The unique notification number. | 
**transaction_id** | **str** | A unique transaction ID, automatically generated for the closure transaction. | [optional] 
**state** | **str** | The current state of the transaction (e.g., &#39;initial&#39;, &#39;processing&#39;, &#39;completed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | The number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | The timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | The timestamp when the transaction was last updated. | [optional] 

## Example

```python
from sync_service_api_gateway.models.ih_notification_close import IHNotificationClose

# TODO update the JSON string below
json = "{}"
# create an instance of IHNotificationClose from a JSON string
ih_notification_close_instance = IHNotificationClose.from_json(json)
# print the JSON string representation of the object
print(IHNotificationClose.to_json())

# convert the object into a dict
ih_notification_close_dict = ih_notification_close_instance.to_dict()
# create an instance of IHNotificationClose from a dict
ih_notification_close_from_dict = IHNotificationClose.from_dict(ih_notification_close_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


