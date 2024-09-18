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

class PortalBPUpdate(object):
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
        'bpnr': 'str',
        'mail': 'str',
        'mail_change': 'int',
        'mobile': 'str',
        'mobile_change': 'int',
        'iban': 'str',
        'iban_change': 'int',
        'datenschutz': 'str',
        'datenschutz_change': 'int',
        'post': 'str',
        'post_change': 'int',
        'anmeldeid': 'str',
        'anmeldeid_change': 'int',
        'change_timestamp': 'datetime',
        'transaction_id': 'str',
        'state': 'str',
        'creation_date': 'datetime',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'bpnr': 'BPNR',
        'mail': 'MAIL',
        'mail_change': 'MAIL_Change',
        'mobile': 'MOBILE',
        'mobile_change': 'MOBILE_Change',
        'iban': 'IBAN',
        'iban_change': 'IBAN_Change',
        'datenschutz': 'DATENSCHUTZ',
        'datenschutz_change': 'DATENSCHUTZ_Change',
        'post': 'POST',
        'post_change': 'POST_Change',
        'anmeldeid': 'ANMELDEID',
        'anmeldeid_change': 'ANMELDEID_Change',
        'change_timestamp': 'Change_Timestamp',
        'transaction_id': 'transaction_id',
        'state': 'state',
        'creation_date': 'creation_date',
        'last_updated': 'last_updated'
    }

    def __init__(self, bpnr=None, mail=None, mail_change=None, mobile=None, mobile_change=None, iban=None, iban_change=None, datenschutz=None, datenschutz_change=None, post=None, post_change=None, anmeldeid=None, anmeldeid_change=None, change_timestamp=None, transaction_id='657af177-8c44-4c6f-a1ab-821b06027b3c', state='initial', creation_date=None, last_updated=None):  # noqa: E501
        """PortalBPUpdate - a model defined in Swagger"""  # noqa: E501
        self._bpnr = None
        self._mail = None
        self._mail_change = None
        self._mobile = None
        self._mobile_change = None
        self._iban = None
        self._iban_change = None
        self._datenschutz = None
        self._datenschutz_change = None
        self._post = None
        self._post_change = None
        self._anmeldeid = None
        self._anmeldeid_change = None
        self._change_timestamp = None
        self._transaction_id = None
        self._state = None
        self._creation_date = None
        self._last_updated = None
        self.discriminator = None
        self.bpnr = bpnr
        self.mail = mail
        self.mail_change = mail_change
        self.mobile = mobile
        self.mobile_change = mobile_change
        self.iban = iban
        self.iban_change = iban_change
        self.datenschutz = datenschutz
        self.datenschutz_change = datenschutz_change
        self.post = post
        self.post_change = post_change
        self.anmeldeid = anmeldeid
        self.anmeldeid_change = anmeldeid_change
        self.change_timestamp = change_timestamp
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if state is not None:
            self.state = state
        if creation_date is not None:
            self.creation_date = creation_date
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def bpnr(self):
        """Gets the bpnr of this PortalBPUpdate.  # noqa: E501


        :return: The bpnr of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._bpnr

    @bpnr.setter
    def bpnr(self, bpnr):
        """Sets the bpnr of this PortalBPUpdate.


        :param bpnr: The bpnr of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if bpnr is None:
            raise ValueError("Invalid value for `bpnr`, must not be `None`")  # noqa: E501

        self._bpnr = bpnr

    @property
    def mail(self):
        """Gets the mail of this PortalBPUpdate.  # noqa: E501


        :return: The mail of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this PortalBPUpdate.


        :param mail: The mail of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if mail is None:
            raise ValueError("Invalid value for `mail`, must not be `None`")  # noqa: E501

        self._mail = mail

    @property
    def mail_change(self):
        """Gets the mail_change of this PortalBPUpdate.  # noqa: E501


        :return: The mail_change of this PortalBPUpdate.  # noqa: E501
        :rtype: int
        """
        return self._mail_change

    @mail_change.setter
    def mail_change(self, mail_change):
        """Sets the mail_change of this PortalBPUpdate.


        :param mail_change: The mail_change of this PortalBPUpdate.  # noqa: E501
        :type: int
        """
        if mail_change is None:
            raise ValueError("Invalid value for `mail_change`, must not be `None`")  # noqa: E501

        self._mail_change = mail_change

    @property
    def mobile(self):
        """Gets the mobile of this PortalBPUpdate.  # noqa: E501


        :return: The mobile of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this PortalBPUpdate.


        :param mobile: The mobile of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if mobile is None:
            raise ValueError("Invalid value for `mobile`, must not be `None`")  # noqa: E501

        self._mobile = mobile

    @property
    def mobile_change(self):
        """Gets the mobile_change of this PortalBPUpdate.  # noqa: E501


        :return: The mobile_change of this PortalBPUpdate.  # noqa: E501
        :rtype: int
        """
        return self._mobile_change

    @mobile_change.setter
    def mobile_change(self, mobile_change):
        """Sets the mobile_change of this PortalBPUpdate.


        :param mobile_change: The mobile_change of this PortalBPUpdate.  # noqa: E501
        :type: int
        """
        if mobile_change is None:
            raise ValueError("Invalid value for `mobile_change`, must not be `None`")  # noqa: E501

        self._mobile_change = mobile_change

    @property
    def iban(self):
        """Gets the iban of this PortalBPUpdate.  # noqa: E501


        :return: The iban of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PortalBPUpdate.


        :param iban: The iban of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501

        self._iban = iban

    @property
    def iban_change(self):
        """Gets the iban_change of this PortalBPUpdate.  # noqa: E501


        :return: The iban_change of this PortalBPUpdate.  # noqa: E501
        :rtype: int
        """
        return self._iban_change

    @iban_change.setter
    def iban_change(self, iban_change):
        """Sets the iban_change of this PortalBPUpdate.


        :param iban_change: The iban_change of this PortalBPUpdate.  # noqa: E501
        :type: int
        """
        if iban_change is None:
            raise ValueError("Invalid value for `iban_change`, must not be `None`")  # noqa: E501

        self._iban_change = iban_change

    @property
    def datenschutz(self):
        """Gets the datenschutz of this PortalBPUpdate.  # noqa: E501


        :return: The datenschutz of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._datenschutz

    @datenschutz.setter
    def datenschutz(self, datenschutz):
        """Sets the datenschutz of this PortalBPUpdate.


        :param datenschutz: The datenschutz of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if datenschutz is None:
            raise ValueError("Invalid value for `datenschutz`, must not be `None`")  # noqa: E501

        self._datenschutz = datenschutz

    @property
    def datenschutz_change(self):
        """Gets the datenschutz_change of this PortalBPUpdate.  # noqa: E501


        :return: The datenschutz_change of this PortalBPUpdate.  # noqa: E501
        :rtype: int
        """
        return self._datenschutz_change

    @datenschutz_change.setter
    def datenschutz_change(self, datenschutz_change):
        """Sets the datenschutz_change of this PortalBPUpdate.


        :param datenschutz_change: The datenschutz_change of this PortalBPUpdate.  # noqa: E501
        :type: int
        """
        if datenschutz_change is None:
            raise ValueError("Invalid value for `datenschutz_change`, must not be `None`")  # noqa: E501

        self._datenschutz_change = datenschutz_change

    @property
    def post(self):
        """Gets the post of this PortalBPUpdate.  # noqa: E501


        :return: The post of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._post

    @post.setter
    def post(self, post):
        """Sets the post of this PortalBPUpdate.


        :param post: The post of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if post is None:
            raise ValueError("Invalid value for `post`, must not be `None`")  # noqa: E501

        self._post = post

    @property
    def post_change(self):
        """Gets the post_change of this PortalBPUpdate.  # noqa: E501


        :return: The post_change of this PortalBPUpdate.  # noqa: E501
        :rtype: int
        """
        return self._post_change

    @post_change.setter
    def post_change(self, post_change):
        """Sets the post_change of this PortalBPUpdate.


        :param post_change: The post_change of this PortalBPUpdate.  # noqa: E501
        :type: int
        """
        if post_change is None:
            raise ValueError("Invalid value for `post_change`, must not be `None`")  # noqa: E501

        self._post_change = post_change

    @property
    def anmeldeid(self):
        """Gets the anmeldeid of this PortalBPUpdate.  # noqa: E501


        :return: The anmeldeid of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._anmeldeid

    @anmeldeid.setter
    def anmeldeid(self, anmeldeid):
        """Sets the anmeldeid of this PortalBPUpdate.


        :param anmeldeid: The anmeldeid of this PortalBPUpdate.  # noqa: E501
        :type: str
        """
        if anmeldeid is None:
            raise ValueError("Invalid value for `anmeldeid`, must not be `None`")  # noqa: E501

        self._anmeldeid = anmeldeid

    @property
    def anmeldeid_change(self):
        """Gets the anmeldeid_change of this PortalBPUpdate.  # noqa: E501


        :return: The anmeldeid_change of this PortalBPUpdate.  # noqa: E501
        :rtype: int
        """
        return self._anmeldeid_change

    @anmeldeid_change.setter
    def anmeldeid_change(self, anmeldeid_change):
        """Sets the anmeldeid_change of this PortalBPUpdate.


        :param anmeldeid_change: The anmeldeid_change of this PortalBPUpdate.  # noqa: E501
        :type: int
        """
        if anmeldeid_change is None:
            raise ValueError("Invalid value for `anmeldeid_change`, must not be `None`")  # noqa: E501

        self._anmeldeid_change = anmeldeid_change

    @property
    def change_timestamp(self):
        """Gets the change_timestamp of this PortalBPUpdate.  # noqa: E501


        :return: The change_timestamp of this PortalBPUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._change_timestamp

    @change_timestamp.setter
    def change_timestamp(self, change_timestamp):
        """Sets the change_timestamp of this PortalBPUpdate.


        :param change_timestamp: The change_timestamp of this PortalBPUpdate.  # noqa: E501
        :type: datetime
        """
        if change_timestamp is None:
            raise ValueError("Invalid value for `change_timestamp`, must not be `None`")  # noqa: E501

        self._change_timestamp = change_timestamp

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PortalBPUpdate.  # noqa: E501


        :return: The transaction_id of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PortalBPUpdate.


        :param transaction_id: The transaction_id of this PortalBPUpdate.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def state(self):
        """Gets the state of this PortalBPUpdate.  # noqa: E501


        :return: The state of this PortalBPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PortalBPUpdate.


        :param state: The state of this PortalBPUpdate.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def creation_date(self):
        """Gets the creation_date of this PortalBPUpdate.  # noqa: E501


        :return: The creation_date of this PortalBPUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PortalBPUpdate.


        :param creation_date: The creation_date of this PortalBPUpdate.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_updated(self):
        """Gets the last_updated of this PortalBPUpdate.  # noqa: E501


        :return: The last_updated of this PortalBPUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this PortalBPUpdate.


        :param last_updated: The last_updated of this PortalBPUpdate.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(PortalBPUpdate, dict):
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
        if not isinstance(other, PortalBPUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
