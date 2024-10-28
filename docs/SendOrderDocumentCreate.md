# SendOrderDocumentCreate

Model for creating a new SendOrderDocument record.  This class is used when handling user input for sending an order document via API. Inherits all base fields from SendOrderDocumentBase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_transaction_id** | **str** | The parent transaction ID from the Order Document creation process. | 
**mail_address** | **str** | The email address to send the order document to. | 
**mail_address_iv** | **str** | The email address to which a copy of the order document will be sent. | 
**osid_order_document** | **int** | The OSID number of the order document. | 

## Example

```python
from sync_service_api_gateway.models.send_order_document_create import SendOrderDocumentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SendOrderDocumentCreate from a JSON string
send_order_document_create_instance = SendOrderDocumentCreate.from_json(json)
# print the JSON string representation of the object
print(SendOrderDocumentCreate.to_json())

# convert the object into a dict
send_order_document_create_dict = send_order_document_create_instance.to_dict()
# create an instance of SendOrderDocumentCreate from a dict
send_order_document_create_from_dict = SendOrderDocumentCreate.from_dict(send_order_document_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


