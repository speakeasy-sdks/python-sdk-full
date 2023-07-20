"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import vendorsplit as shared_vendorsplit
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils
from typing import Optional

class CreateRefundRequestRefundSpeed(str, Enum):
    r"""Speed at which the refund is processed. It's an optional field with default being STANDARD"""
    STANDARD = 'STANDARD'
    INSTANT = 'INSTANT'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateRefundRequest:
    refund_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_amount') }})
    r"""Amount to be refunded. Should be lesser than or equal to the transaction amount. (Decimals allowed)"""
    refund_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_id') }})
    r"""An unique ID to associate the refund with. Provie alphanumeric values"""
    refund_note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_note'), 'exclude': lambda f: f is None }})
    r"""A refund note for your reference."""
    refund_speed: Optional[CreateRefundRequestRefundSpeed] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_speed'), 'exclude': lambda f: f is None }})
    r"""Speed at which the refund is processed. It's an optional field with default being STANDARD"""
    refund_splits: Optional[list[shared_vendorsplit.VendorSplit]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_splits'), 'exclude': lambda f: f is None }})
    

