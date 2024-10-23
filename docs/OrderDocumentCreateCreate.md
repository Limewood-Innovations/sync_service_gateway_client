# OrderDocumentCreateCreate

Model for creating a new OrderDocumentCreate entry.  This class is used when handling user input for creating a new order document via API. Inherits all base fields from OrderDocumentCreateBase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID from the IH notification create process. | 
**jira_ticket_number** | **str** | The Jira ticket number associated with the notification. | 
**notif_number** | **int** | The unique notification number. | 
**osid_ticket_object** | **int** | The OSID number of the ticket object. | 
**osid_order_document** | **int** | The OSID number of the order document. | 

## Example

```python
from sync_service_api_gateway.models.order_document_create_create import OrderDocumentCreateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDocumentCreateCreate from a JSON string
order_document_create_create_instance = OrderDocumentCreateCreate.from_json(json)
# print the JSON string representation of the object
print(OrderDocumentCreateCreate.to_json())

# convert the object into a dict
order_document_create_create_dict = order_document_create_create_instance.to_dict()
# create an instance of OrderDocumentCreateCreate from a dict
order_document_create_create_from_dict = OrderDocumentCreateCreate.from_dict(order_document_create_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


