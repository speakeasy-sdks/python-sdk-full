"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Netbanking:
    channel: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel') }})
    r"""The channel for netbanking will always be `link`"""
    netbanking_bank_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netbanking_bank_code') }})
    r"""Bank code"""
    

