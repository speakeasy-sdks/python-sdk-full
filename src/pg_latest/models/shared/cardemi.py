"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils
from typing import Optional

class CardEMICardBankName(str, Enum):
    r"""Card bank name, required for EMI payments. This is the bank user has selected for EMI. One of [\\"hdfc, \\"kotak\\", \\"icici\\", \\"rbl\\", \\"bob\\", \\"standard chartered\\", \\"axis\\", \\"au\\", \\"yes\\", \\"sbi\\", \\"fed\\", \\"hsbc\\", \\"citi\\", \\"amex\\"]"""
    HDFC = 'hdfc'
    KOTAK = 'kotak'
    ICICI = 'icici'
    RBL = 'rbl'
    BOB = 'bob'
    STANDARD_CHARTERED = 'standard chartered'
    AXIS = 'axis'
    AU = 'au'
    YES = 'yes'
    SBI = 'sbi'
    FED = 'fed'
    HSBC = 'hsbc'
    CITI = 'citi'
    AMEX = 'amex'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CardEMI:
    card_alias: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_alias'), 'exclude': lambda f: f is None }})
    r"""Card alias as returned by Cashfree Vault API"""
    card_bank_name: Optional[CardEMICardBankName] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_bank_name'), 'exclude': lambda f: f is None }})
    r"""Card bank name, required for EMI payments. This is the bank user has selected for EMI. One of [\\"hdfc, \\"kotak\\", \\"icici\\", \\"rbl\\", \\"bob\\", \\"standard chartered\\", \\"axis\\", \\"au\\", \\"yes\\", \\"sbi\\", \\"fed\\", \\"hsbc\\", \\"citi\\", \\"amex\\"]"""
    card_cvv: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_cvv'), 'exclude': lambda f: f is None }})
    r"""CVV mentioned on the card."""
    card_expiry_mm: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_expiry_mm'), 'exclude': lambda f: f is None }})
    r"""Card expiry month."""
    card_expiry_yy: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_expiry_yy'), 'exclude': lambda f: f is None }})
    r"""Card expiry year."""
    card_holder_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_holder_name'), 'exclude': lambda f: f is None }})
    r"""Customer name mentioned on the card."""
    card_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card_number'), 'exclude': lambda f: f is None }})
    r"""Customer card number."""
    channel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    r"""The channel for card payments will always be \\"link\\" """
    emi_tenure: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emi_tenure'), 'exclude': lambda f: f is None }})
    r"""EMI tenure selected by the user"""
    

