"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkCustomerDetailsEntity:
    customer_phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_phone') }})
    r"""Customer phone number"""
    customer_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_email'), 'exclude': lambda f: f is None }})
    r"""Customer email address"""
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_name'), 'exclude': lambda f: f is None }})
    r"""Customer name"""
    

