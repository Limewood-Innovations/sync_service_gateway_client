# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Mahnstufe(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bukrs': 'object',
        'customer_number': 'object',
        'dunning_block_reason': 'object',
        'transaction_id': 'object',
        'state': 'object',
        'creation_date': 'object'
    }

    attribute_map = {
        'bukrs': 'bukrs',
        'customer_number': 'customerNumber',
        'dunning_block_reason': 'dunningBlockReason',
        'transaction_id': 'transaction_id',
        'state': 'state',
        'creation_date': 'creation_date'
    }

    def __init__(self, bukrs=None, customer_number=None, dunning_block_reason=None, transaction_id=None, state=None, creation_date=None):  # noqa: E501
        """Mahnstufe - a model defined in Swagger"""  # noqa: E501
        self._bukrs = None
        self._customer_number = None
        self._dunning_block_reason = None
        self._transaction_id = None
        self._state = None
        self._creation_date = None
        self.discriminator = None
        self.bukrs = bukrs
        self.customer_number = customer_number
        self.dunning_block_reason = dunning_block_reason
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if state is not None:
            self.state = state
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def bukrs(self):
        """Gets the bukrs of this Mahnstufe.  # noqa: E501


        :return: The bukrs of this Mahnstufe.  # noqa: E501
        :rtype: object
        """
        return self._bukrs

    @bukrs.setter
    def bukrs(self, bukrs):
        """Sets the bukrs of this Mahnstufe.


        :param bukrs: The bukrs of this Mahnstufe.  # noqa: E501
        :type: object
        """
        if bukrs is None:
            raise ValueError("Invalid value for `bukrs`, must not be `None`")  # noqa: E501

        self._bukrs = bukrs

    @property
    def customer_number(self):
        """Gets the customer_number of this Mahnstufe.  # noqa: E501


        :return: The customer_number of this Mahnstufe.  # noqa: E501
        :rtype: object
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this Mahnstufe.


        :param customer_number: The customer_number of this Mahnstufe.  # noqa: E501
        :type: object
        """
        if customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def dunning_block_reason(self):
        """Gets the dunning_block_reason of this Mahnstufe.  # noqa: E501


        :return: The dunning_block_reason of this Mahnstufe.  # noqa: E501
        :rtype: object
        """
        return self._dunning_block_reason

    @dunning_block_reason.setter
    def dunning_block_reason(self, dunning_block_reason):
        """Sets the dunning_block_reason of this Mahnstufe.


        :param dunning_block_reason: The dunning_block_reason of this Mahnstufe.  # noqa: E501
        :type: object
        """
        if dunning_block_reason is None:
            raise ValueError("Invalid value for `dunning_block_reason`, must not be `None`")  # noqa: E501

        self._dunning_block_reason = dunning_block_reason

    @property
    def transaction_id(self):
        """Gets the transaction_id of this Mahnstufe.  # noqa: E501


        :return: The transaction_id of this Mahnstufe.  # noqa: E501
        :rtype: object
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this Mahnstufe.


        :param transaction_id: The transaction_id of this Mahnstufe.  # noqa: E501
        :type: object
        """

        self._transaction_id = transaction_id

    @property
    def state(self):
        """Gets the state of this Mahnstufe.  # noqa: E501


        :return: The state of this Mahnstufe.  # noqa: E501
        :rtype: object
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Mahnstufe.


        :param state: The state of this Mahnstufe.  # noqa: E501
        :type: object
        """

        self._state = state

    @property
    def creation_date(self):
        """Gets the creation_date of this Mahnstufe.  # noqa: E501


        :return: The creation_date of this Mahnstufe.  # noqa: E501
        :rtype: object
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Mahnstufe.


        :param creation_date: The creation_date of this Mahnstufe.  # noqa: E501
        :type: object
        """

        self._creation_date = creation_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Mahnstufe, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Mahnstufe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other