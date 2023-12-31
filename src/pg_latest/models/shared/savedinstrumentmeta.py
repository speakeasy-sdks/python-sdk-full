"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclasses.dataclass
class CardTokenDetails:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedInstrumentMeta:
    card_bank_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_bank_name'), 'exclude': lambda f: f is None }})
    r"""Issuing bank name of saved card"""
    card_country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_country'), 'exclude': lambda f: f is None }})
    r"""Issuing country of saved card"""
    card_network: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_network'), 'exclude': lambda f: f is None }})
    r"""card scheme/network of the saved card"""
    card_token_details: Optional[CardTokenDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_token_details'), 'exclude': lambda f: f is None }})
    card_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_type'), 'exclude': lambda f: f is None }})
    r"""Type of saved card"""
    

