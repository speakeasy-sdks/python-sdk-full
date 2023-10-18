"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import upi as shared_upi
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UPIPaymentMethod:
    upi: shared_upi.Upi = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upi') }})
    

