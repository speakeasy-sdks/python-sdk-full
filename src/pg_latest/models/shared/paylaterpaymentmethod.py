"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import paylater as shared_paylater
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PaylaterPaymentMethod:
    paylater: shared_paylater.Paylater = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paylater') }})
    

