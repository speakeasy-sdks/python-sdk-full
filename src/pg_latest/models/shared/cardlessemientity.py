"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .emiplansarray import EMIPlansArray
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CardlessEMIEntity:
    emi_plans: Optional[List[EMIPlansArray]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emi_plans'), 'exclude': lambda f: f is None }})
    payment_method: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method'), 'exclude': lambda f: f is None }})
    

