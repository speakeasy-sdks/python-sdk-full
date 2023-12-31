"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .linkcustomerdetailsentity import LinkCustomerDetailsEntity
from .paymenturlobject import PaymentURLObject
from .refundurlobject import RefundURLObject
from .settlementurlobject import SettlementURLObject
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkOrdersResponse:
    cf_order_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_order_id'), 'exclude': lambda f: f is None }})
    customer_details: Optional[LinkCustomerDetailsEntity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details'), 'exclude': lambda f: f is None }})
    entity: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    order_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_amount'), 'exclude': lambda f: f is None }})
    order_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_currency'), 'exclude': lambda f: f is None }})
    order_expiry_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_expiry_time'), 'exclude': lambda f: f is None }})
    order_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_id'), 'exclude': lambda f: f is None }})
    order_note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_note'), 'exclude': lambda f: f is None }})
    order_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_status'), 'exclude': lambda f: f is None }})
    order_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_token'), 'exclude': lambda f: f is None }})
    payments: Optional[PaymentURLObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payments'), 'exclude': lambda f: f is None }})
    refunds: Optional[RefundURLObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refunds'), 'exclude': lambda f: f is None }})
    settlements: Optional[SettlementURLObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlements'), 'exclude': lambda f: f is None }})
    

