"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import linkcustomerdetailsentity as shared_linkcustomerdetailsentity
from ..shared import linkmetaentity as shared_linkmetaentity
from ..shared import linknotifyentity as shared_linknotifyentity
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkCancelledResponse:
    cf_link_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_link_id'), 'exclude': lambda f: f is None }})
    customer_details: Optional[shared_linkcustomerdetailsentity.LinkCustomerDetailsEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details'), 'exclude': lambda f: f is None }})
    link_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_amount'), 'exclude': lambda f: f is None }})
    link_amount_paid: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_amount_paid'), 'exclude': lambda f: f is None }})
    link_auto_reminders: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_auto_reminders'), 'exclude': lambda f: f is None }})
    link_created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_created_at'), 'exclude': lambda f: f is None }})
    link_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_currency'), 'exclude': lambda f: f is None }})
    link_expiry_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_expiry_time'), 'exclude': lambda f: f is None }})
    link_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_id'), 'exclude': lambda f: f is None }})
    link_meta: Optional[shared_linkmetaentity.LinkMetaEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_meta'), 'exclude': lambda f: f is None }})
    link_minimum_partial_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_minimum_partial_amount'), 'exclude': lambda f: f is None }})
    link_notes: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_notes'), 'exclude': lambda f: f is None }})
    r"""Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs"""
    link_notify: Optional[shared_linknotifyentity.LinkNotifyEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_notify'), 'exclude': lambda f: f is None }})
    link_partial_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_partial_payments'), 'exclude': lambda f: f is None }})
    link_purpose: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_purpose'), 'exclude': lambda f: f is None }})
    link_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_status'), 'exclude': lambda f: f is None }})
    link_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_url'), 'exclude': lambda f: f is None }})
    

