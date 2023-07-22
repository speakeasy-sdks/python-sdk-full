"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import linkcustomerdetailsentity as shared_linkcustomerdetailsentity
from ..shared import linkmetaentity as shared_linkmetaentity
from ..shared import linknotifyentity as shared_linknotifyentity
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateLinkRequest:
    customer_details: shared_linkcustomerdetailsentity.LinkCustomerDetailsEntity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details') }})
    link_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_amount') }})
    r"""Amount to be collected using this link. Provide upto two decimals for paise."""
    link_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_currency') }})
    r"""Currency for the payment link. Default is INR. Contact care@cashfree.com to enable new currencies."""
    link_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_id') }})
    r"""Unique Identifier (provided by merchant) for the Link. Alphanumeric and only - and _ allowed (50 character limit). Use this for other link-related APIs."""
    link_purpose: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_purpose') }})
    r"""A brief description for which payment must be collected. This is shown to the customer."""
    link_auto_reminders: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_auto_reminders'), 'exclude': lambda f: f is None }})
    r"""If \\"true\\", reminders will be sent to customers for collecting payments."""
    link_expiry_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_expiry_time'), 'exclude': lambda f: f is None }})
    r"""Time after which the link expires. Customers will not be able to make the payment beyond the time specified here. You can provide them in a valid ISO 8601 time format. Default is 30 days."""
    link_meta: Optional[shared_linkmetaentity.LinkMetaEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_meta'), 'exclude': lambda f: f is None }})
    link_minimum_partial_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_minimum_partial_amount'), 'exclude': lambda f: f is None }})
    r"""Minimum amount in first installment that needs to be paid by the customer if partial payments are enabled. This should be less than the link_amount."""
    link_notes: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_notes'), 'exclude': lambda f: f is None }})
    r"""Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs"""
    link_notify: Optional[shared_linknotifyentity.LinkNotifyEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_notify'), 'exclude': lambda f: f is None }})
    link_partial_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_partial_payments'), 'exclude': lambda f: f is None }})
    r"""If \\"true\\", customer can make partial payments for the link."""
    

