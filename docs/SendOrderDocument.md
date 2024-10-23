# SendOrderDocument

Database model for persisting the transaction of sending an order document.  This model represents the `SendOrderDocument` entity in the database and is used to return data to the user via API. It includes additional fields for tracking the transaction state and metadata.  Attributes:     transaction_id (str): A unique identifier for the transaction, generated automatically.     state (str): The current state of the transaction (e.g., 'initial', 'processing', 'completed').     retry_count (int): The number of retry attempts for the transaction.     creation_date (datetime): The timestamp when the transaction was initially created.     last_updated (datetime): The timestamp when the transaction was last updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID from the Order Document creation process. | 
**mail_address** | **str** | The email address to send the order document to. | 
**osid_order_document** | **int** | The OSID number of the order document. | 
**transaction_id** | **str** | A unique transaction ID, automatically generated for the sending order document transaction. | [optional] 
**state** | **str** | The current state of the transaction (e.g., &#39;initial&#39;, &#39;processing&#39;, &#39;completed&#39;). | [optional] [default to 'initial']
**retry_count** | **int** | The number of times the transaction has been retried. | [optional] [default to 0]
**creation_date** | **datetime** | The timestamp when the transaction was created. | [optional] 
**last_updated** | **datetime** | The timestamp when the transaction was last updated. | [optional] 

## Example

```python
from sync_service_api_gateway.models.send_order_document import SendOrderDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SendOrderDocument from a JSON string
send_order_document_instance = SendOrderDocument.from_json(json)
# print the JSON string representation of the object
print(SendOrderDocument.to_json())

# convert the object into a dict
send_order_document_dict = send_order_document_instance.to_dict()
# create an instance of SendOrderDocument from a dict
send_order_document_from_dict = SendOrderDocument.from_dict(send_order_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


