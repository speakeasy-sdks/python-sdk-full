"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CustomerDetailsCardlessEMI:
    r"""Details of the customer for whom eligibility is being checked."""
    customer_phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_phone') }})
    r"""Phone Number of the customer"""
    

