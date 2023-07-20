"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import customerdetails as shared_customerdetails
from ..shared import ordermeta as shared_ordermeta
from ..shared import terminaldetails as shared_terminaldetails
from ..shared import vendorsplit as shared_vendorsplit
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOrderBackendRequest:
    customer_details: shared_customerdetails.CustomerDetails = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details') }})
    r"""The customer details that are necessary. Note that you can pass dummy details if your use case does not require the customer details."""
    order_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_amount') }})
    r"""Bill amount for the order. Provide upto two decimals. 10.15 means Rs 10 and 15 paisa"""
    order_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_currency') }})
    r"""Currency for the order. INR if left empty. Contact care@cashfree.com to enable new currencies."""
    order_expiry_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_expiry_time'), 'exclude': lambda f: f is None }})
    r"""Time after which the order expires. Customers will not be able to make the payment beyond the time specified here. We store timestamps in IST, but you can provide them in a valid ISO 8601 time format."""
    order_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_id'), 'exclude': lambda f: f is None }})
    r"""Order identifier present in your system. Alphanumeric and only - and _ allowed."""
    order_meta: Optional[shared_ordermeta.OrderMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_meta'), 'exclude': lambda f: f is None }})
    order_note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_note'), 'exclude': lambda f: f is None }})
    r"""Order note for reference."""
    order_splits: Optional[list[shared_vendorsplit.VendorSplit]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_splits'), 'exclude': lambda f: f is None }})
    order_tags: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_tags'), 'exclude': lambda f: f is None }})
    r"""Custom Tags which can be passed for an order. A maximum of 6 tags can be added"""
    terminal: Optional[shared_terminaldetails.TerminalDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terminal'), 'exclude': lambda f: f is None }})
    

