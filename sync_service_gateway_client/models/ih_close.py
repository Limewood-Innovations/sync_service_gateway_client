# coding: utf-8

"""
    FastAPI

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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IHClose(BaseModel):
    """
    IHClose
    """ # noqa: E501
    jira_ticket_number: StrictStr
    notif_number: StrictInt
    transaction_id: Optional[StrictStr] = '62036b58-1055-43c9-8150-ead3309d7812'
    state: Optional[StrictStr] = 'initial'
    creation_date: Optional[datetime] = None
    last_updated: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["jira_ticket_number", "notif_number", "transaction_id", "state", "creation_date", "last_updated"]

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
        """Create an instance of IHClose from a JSON string"""
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
        """Create an instance of IHClose from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jira_ticket_number": obj.get("jira_ticket_number"),
            "notif_number": obj.get("notif_number"),
            "transaction_id": obj.get("transaction_id") if obj.get("transaction_id") is not None else '62036b58-1055-43c9-8150-ead3309d7812',
            "state": obj.get("state") if obj.get("state") is not None else 'initial',
            "creation_date": obj.get("creation_date"),
            "last_updated": obj.get("last_updated")
        })
        return _obj


