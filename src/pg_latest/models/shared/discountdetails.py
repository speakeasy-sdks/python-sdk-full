"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils

class DiscountType(str, Enum):
    r"""Type of discount"""
    FLAT = 'flat'
    PERCENTAGE = 'percentage'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DiscountDetails:
    discount_type: DiscountType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount_type') }})
    r"""Type of discount"""
    discount_value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount_value') }})
    r"""Value of Discount."""
    max_discount_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_discount_amount') }})
    r"""Maximum Value of Discount allowed."""
    

