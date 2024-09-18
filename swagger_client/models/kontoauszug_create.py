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

class KontoauszugCreate(object):
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
        'bukrs': 'int',
        'customer_number': 'int',
        'contract_number': 'str',
        '_date': 'date',
        'jira_ticket_number': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'bukrs': 'bukrs',
        'customer_number': 'customerNumber',
        'contract_number': 'contractNumber',
        '_date': 'date',
        'jira_ticket_number': 'jiraTicketNumber',
        'mode': 'mode'
    }

    def __init__(self, bukrs=None, customer_number=None, contract_number=None, _date=None, jira_ticket_number=None, mode=None):  # noqa: E501
        """KontoauszugCreate - a model defined in Swagger"""  # noqa: E501
        self._bukrs = None
        self._customer_number = None
        self._contract_number = None
        self.__date = None
        self._jira_ticket_number = None
        self._mode = None
        self.discriminator = None
        self.bukrs = bukrs
        self.customer_number = customer_number
        self.contract_number = contract_number
        self._date = _date
        self.jira_ticket_number = jira_ticket_number
        self.mode = mode

    @property
    def bukrs(self):
        """Gets the bukrs of this KontoauszugCreate.  # noqa: E501


        :return: The bukrs of this KontoauszugCreate.  # noqa: E501
        :rtype: int
        """
        return self._bukrs

    @bukrs.setter
    def bukrs(self, bukrs):
        """Sets the bukrs of this KontoauszugCreate.


        :param bukrs: The bukrs of this KontoauszugCreate.  # noqa: E501
        :type: int
        """
        if bukrs is None:
            raise ValueError("Invalid value for `bukrs`, must not be `None`")  # noqa: E501

        self._bukrs = bukrs

    @property
    def customer_number(self):
        """Gets the customer_number of this KontoauszugCreate.  # noqa: E501


        :return: The customer_number of this KontoauszugCreate.  # noqa: E501
        :rtype: int
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this KontoauszugCreate.


        :param customer_number: The customer_number of this KontoauszugCreate.  # noqa: E501
        :type: int
        """
        if customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def contract_number(self):
        """Gets the contract_number of this KontoauszugCreate.  # noqa: E501


        :return: The contract_number of this KontoauszugCreate.  # noqa: E501
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """Sets the contract_number of this KontoauszugCreate.


        :param contract_number: The contract_number of this KontoauszugCreate.  # noqa: E501
        :type: str
        """
        if contract_number is None:
            raise ValueError("Invalid value for `contract_number`, must not be `None`")  # noqa: E501

        self._contract_number = contract_number

    @property
    def _date(self):
        """Gets the _date of this KontoauszugCreate.  # noqa: E501


        :return: The _date of this KontoauszugCreate.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this KontoauszugCreate.


        :param _date: The _date of this KontoauszugCreate.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def jira_ticket_number(self):
        """Gets the jira_ticket_number of this KontoauszugCreate.  # noqa: E501


        :return: The jira_ticket_number of this KontoauszugCreate.  # noqa: E501
        :rtype: str
        """
        return self._jira_ticket_number

    @jira_ticket_number.setter
    def jira_ticket_number(self, jira_ticket_number):
        """Sets the jira_ticket_number of this KontoauszugCreate.


        :param jira_ticket_number: The jira_ticket_number of this KontoauszugCreate.  # noqa: E501
        :type: str
        """
        if jira_ticket_number is None:
            raise ValueError("Invalid value for `jira_ticket_number`, must not be `None`")  # noqa: E501

        self._jira_ticket_number = jira_ticket_number

    @property
    def mode(self):
        """Gets the mode of this KontoauszugCreate.  # noqa: E501


        :return: The mode of this KontoauszugCreate.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this KontoauszugCreate.


        :param mode: The mode of this KontoauszugCreate.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

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
        if issubclass(KontoauszugCreate, dict):
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
        if not isinstance(other, KontoauszugCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
