"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils
from typing import Optional

class CardCardBankName(str, Enum):
    r"""One of [\\"Kotak\\", \\"ICICI\\", \\"RBL\\", \\"BOB\\", \\"Standard Chartered\\"]. Card bank name, required for EMI payments. This is the bank user has selected for EMI"""
    KOTAK = 'Kotak'
    ICICI = 'ICICI'
    RBL = 'RBL'
    BOB = 'BOB'
    STANDARD_CHARTERED = 'Standard Chartered'

class CardChannel(str, Enum):
    r"""The channel for card payments can be \\"link\\" or \\"post\\". Post is used for seamless OTP payments where merchant captures OTP on their own page."""
    LINK = 'link'
    POST = 'post'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Card:
    card_alias: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_alias'), 'exclude': lambda f: f is None }})
    r"""Card alias as returned by Cashfree Vault API."""
    card_bank_name: Optional[CardCardBankName] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_bank_name'), 'exclude': lambda f: f is None }})
    r"""One of [\\"Kotak\\", \\"ICICI\\", \\"RBL\\", \\"BOB\\", \\"Standard Chartered\\"]. Card bank name, required for EMI payments. This is the bank user has selected for EMI"""
    card_cvv: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_cvv'), 'exclude': lambda f: f is None }})
    r"""CVV mentioned on the card."""
    card_display: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_display'), 'exclude': lambda f: f is None }})
    r"""last 4 digits of original card number. Required only for tokenized card transactions."""
    card_expiry_mm: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_expiry_mm'), 'exclude': lambda f: f is None }})
    r"""Card expiry month for plain card transactions. Token expiry month for tokenized card transactions."""
    card_expiry_yy: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_expiry_yy'), 'exclude': lambda f: f is None }})
    r"""Card expiry year for plain card transactions. Token expiry year for tokenized card transactions."""
    card_holder_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_holder_name'), 'exclude': lambda f: f is None }})
    r"""Customer name mentioned on the card."""
    card_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_number'), 'exclude': lambda f: f is None }})
    r"""Customer card number for plain card transactions. Token pan number for tokenized card transactions."""
    channel: Optional[CardChannel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    r"""The channel for card payments can be \\"link\\" or \\"post\\". Post is used for seamless OTP payments where merchant captures OTP on their own page."""
    cryptogram: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cryptogram'), 'exclude': lambda f: f is None }})
    r"""cryptogram received from card network. Required only for tokenized card transactions."""
    emi_tenure: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emi_tenure'), 'exclude': lambda f: f is None }})
    r"""EMI tenure selected by the user"""
    instrument_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instrument_id'), 'exclude': lambda f: f is None }})
    r"""instrument id of saved card. Required only to make payment using saved instrument."""
    token_requestor_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_requestor_id'), 'exclude': lambda f: f is None }})
    r"""TRID issued by card networks. Required only for tokenized card transactions."""
    

