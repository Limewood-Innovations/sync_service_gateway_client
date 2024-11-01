# coding: utf-8

"""
    sync-service-api-gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class PortalBPUpdateCreate(BaseModel):
    """
    Model for creating a new PortalBPUpdate instance via API.  This class is used for capturing and handling input when updating a business partner's details in the portal. It extends from the base class `PortalBPUpdateBase`.
    """ # noqa: E501
    bpnr: StrictStr = Field(description="The Business Partner Number.")
    mail: StrictStr = Field(description="The email address of the business partner.")
    mail_change: StrictInt = Field(description="Flag indicating if the email has changed (0 = no change, 1 = changed).")
    mobile: StrictStr = Field(description="The mobile phone number of the business partner.")
    mobile_change: StrictInt = Field(description="Flag indicating if the mobile number has changed (0 = no change, 1 = changed).")
    iban: StrictStr = Field(description="The IBAN (International Bank Account Number) of the business partner.")
    iban_change: StrictInt = Field(description="Flag indicating if the IBAN has changed (0 = no change, 1 = changed).")
    datenschutz: StrictStr = Field(description="The data privacy preferences (e.g., consent or refusal).")
    datenschutz_change: StrictInt = Field(description="Flag indicating if data privacy preferences have changed (0 = no change, 1 = changed).")
    post: StrictStr = Field(description="Postal communication preferences of the business partner.")
    post_change: StrictInt = Field(description="Flag indicating if postal communication preferences have changed (0 = no change, 1 = changed).")
    anmeldeid: StrictStr = Field(description="The registration ID of the business partner.")
    anmeldeid_change: StrictInt = Field(description="Flag indicating if the registration ID has changed (0 = no change, 1 = changed).")
    change_timestamp: datetime = Field(description="The timestamp indicating when the changes were made.")
    __properties: ClassVar[List[str]] = ["bpnr", "mail", "mail_change", "mobile", "mobile_change", "iban", "iban_change", "datenschutz", "datenschutz_change", "post", "post_change", "anmeldeid", "anmeldeid_change", "change_timestamp"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PortalBPUpdateCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortalBPUpdateCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bpnr": obj.get("bpnr"),
            "mail": obj.get("mail"),
            "mail_change": obj.get("mail_change"),
            "mobile": obj.get("mobile"),
            "mobile_change": obj.get("mobile_change"),
            "iban": obj.get("iban"),
            "iban_change": obj.get("iban_change"),
            "datenschutz": obj.get("datenschutz"),
            "datenschutz_change": obj.get("datenschutz_change"),
            "post": obj.get("post"),
            "post_change": obj.get("post_change"),
            "anmeldeid": obj.get("anmeldeid"),
            "anmeldeid_change": obj.get("anmeldeid_change"),
            "change_timestamp": obj.get("change_timestamp")
        })
        return _obj


