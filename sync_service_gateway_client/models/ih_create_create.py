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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class IHCreateCreate(BaseModel):
    """
    IHCreateCreate
    """ # noqa: E501
    jira_ticket_number: StrictStr
    notif_type: StrictStr
    short_text: StrictStr
    long_text: StrictStr
    func_loc: StrictStr
    reported_by: StrictStr
    notif_date: datetime
    plan_group: StrictStr
    partner_number: StrictStr
    plan_plant: StrictStr
    partner_role: StrictStr
    set_active: StrictBool
    __properties: ClassVar[List[str]] = ["jira_ticket_number", "notif_type", "short_text", "long_text", "func_loc", "reported_by", "notif_date", "plan_group", "partner_number", "plan_plant", "partner_role", "set_active"]

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
        """Create an instance of IHCreateCreate from a JSON string"""
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
        """Create an instance of IHCreateCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jira_ticket_number": obj.get("jira_ticket_number"),
            "notif_type": obj.get("notif_type"),
            "short_text": obj.get("short_text"),
            "long_text": obj.get("long_text"),
            "func_loc": obj.get("func_loc"),
            "reported_by": obj.get("reported_by"),
            "notif_date": obj.get("notif_date"),
            "plan_group": obj.get("plan_group"),
            "partner_number": obj.get("partner_number"),
            "plan_plant": obj.get("plan_plant"),
            "partner_role": obj.get("partner_role"),
            "set_active": obj.get("set_active")
        })
        return _obj

