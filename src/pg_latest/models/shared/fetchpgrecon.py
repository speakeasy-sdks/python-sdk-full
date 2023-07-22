"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchPGReconData:
    adjustment: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjustment'), 'exclude': lambda f: f is None }})
    r"""Amount that is adjusted from the settlement amount because of any credit/debit event such as refund, refund_reverse etc."""
    adjustment_remarks: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjustment_remarks'), 'exclude': lambda f: f is None }})
    r"""Other adjustment remarks."""
    amount_settled: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_settled'), 'exclude': lambda f: f is None }})
    r"""Net amount that is settled after considering the adjustments, settlement charge and tax."""
    cf_payment_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_payment_id'), 'exclude': lambda f: f is None }})
    r"""Cashfree Payments unique ID to identify a payment."""
    cf_settlement_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_settlement_id'), 'exclude': lambda f: f is None }})
    r"""Unique ID to identify the settlement."""
    closed_in_favor_of: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('closed_in_favor_of'), 'exclude': lambda f: f is None }})
    r"""Specifies whether the dispute was closed in favor of the merchant or customer. /n Possible values - Merchant, Customer"""
    customer_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_email'), 'exclude': lambda f: f is None }})
    r"""Customer email."""
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_name'), 'exclude': lambda f: f is None }})
    r"""Customer name."""
    customer_phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_phone'), 'exclude': lambda f: f is None }})
    r"""Customer phone number."""
    dispute_category: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dispute_category'), 'exclude': lambda f: f is None }})
    r"""Category of the dispute - Dispute code and the reason for dispute is shown."""
    dispute_note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dispute_note'), 'exclude': lambda f: f is None }})
    r"""Note regarding the dispute."""
    dispute_resolved_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dispute_resolved_on'), 'exclude': lambda f: f is None }})
    r"""Date and time when the dispute was resolved."""
    entity: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    r"""Recon"""
    event_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_amount'), 'exclude': lambda f: f is None }})
    r"""Amount of the event. Example, refund amount, dispute amount, payment amount, etc."""
    event_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_currency'), 'exclude': lambda f: f is None }})
    r"""Curreny type - INR."""
    event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_id'), 'exclude': lambda f: f is None }})
    r"""Unique ID associated with the event."""
    event_settlement_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_settlement_amount'), 'exclude': lambda f: f is None }})
    r"""Amount that is part of the settlement corresponding to the event."""
    event_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_status'), 'exclude': lambda f: f is None }})
    r"""Status of the event. Example - SUCCESS, FAILED, PENDING, CANCELLED."""
    event_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_time'), 'exclude': lambda f: f is None }})
    r"""Time associated with the event. Example, transaction time, dispute initiation time"""
    event_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_type'), 'exclude': lambda f: f is None }})
    r"""The event type can be SETTLEMENT, PAYMENT, REFUND, REFUND_REVERSAL, DISPUTE, DISPUTE_REVERSAL, CHARGEBACK, CHARGEBACK_REVERSAL, OTHER_ADJUSTMENT."""
    order_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_amount'), 'exclude': lambda f: f is None }})
    r"""The amount which was passed at the order creation time."""
    order_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_id'), 'exclude': lambda f: f is None }})
    r"""Unique order ID. Alphanumeric and only '-' and '_' allowed."""
    payment_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_amount'), 'exclude': lambda f: f is None }})
    r"""Payment amount captured."""
    payment_from: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_from'), 'exclude': lambda f: f is None }})
    r"""The start time of the time range of the payments considered for the settlement."""
    payment_service_charge: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_service_charge'), 'exclude': lambda f: f is None }})
    r"""Service charge applicable for the payment."""
    payment_service_tax: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_service_tax'), 'exclude': lambda f: f is None }})
    r"""Service tax applicable on the payment."""
    payment_till: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_till'), 'exclude': lambda f: f is None }})
    r"""The end time of time range of the payments considered for the settlement."""
    payment_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_time'), 'exclude': lambda f: f is None }})
    r"""Date and time when the payment was initiated."""
    payment_utr: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_utr'), 'exclude': lambda f: f is None }})
    r"""Unique transaction reference number of the payment."""
    reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason'), 'exclude': lambda f: f is None }})
    r"""Reason for settlement failure."""
    refund_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_arn'), 'exclude': lambda f: f is None }})
    r"""The bank reference number for the refund."""
    refund_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_id'), 'exclude': lambda f: f is None }})
    r"""An unique ID to associate the refund with."""
    refund_note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_note'), 'exclude': lambda f: f is None }})
    r"""A refund note for your reference."""
    refund_processed_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_processed_at'), 'exclude': lambda f: f is None }})
    r"""Date and time when the refund was processed."""
    remarks: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remarks'), 'exclude': lambda f: f is None }})
    r"""Remarks on the settlement."""
    sale_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sale_type'), 'exclude': lambda f: f is None }})
    r"""Indicates if it is CREDIT/DEBIT sale."""
    service_charge: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_charge'), 'exclude': lambda f: f is None }})
    r"""Service charge applicable on the settlement amount."""
    service_tax: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_tax'), 'exclude': lambda f: f is None }})
    r"""Service tax applicable on the settlement amount."""
    settlement_charge: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_charge'), 'exclude': lambda f: f is None }})
    r"""Settlement charges applicable on the settlement."""
    settlement_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_date'), 'exclude': lambda f: f is None }})
    r"""Date and time when the settlement was processed."""
    settlement_initiated_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_initiated_on'), 'exclude': lambda f: f is None }})
    r"""Date and time when the settlement was initiated."""
    settlement_tax: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_tax'), 'exclude': lambda f: f is None }})
    r"""Settlement tax applicable on the settlement."""
    settlement_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_type'), 'exclude': lambda f: f is None }})
    r"""Type of settlement. Possible values - Standard, Instant, On demand."""
    settlement_utr: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_utr'), 'exclude': lambda f: f is None }})
    r"""Unique transaction reference number of the settlement."""
    split_service_charge: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('split_service_charge'), 'exclude': lambda f: f is None }})
    r"""Service charge that is applicable for splitting the payment."""
    split_service_tax: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('split_service_tax'), 'exclude': lambda f: f is None }})
    r"""Service tax applicable for splitting the amount to vendors."""
    vendor_commission: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vendor_commission'), 'exclude': lambda f: f is None }})
    r"""Vendor commission applicable for this transaction."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchPGRecon:
    r"""OK"""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor'), 'exclude': lambda f: f is None }})
    r"""Specifies from where the next set of settlement details should be fetched."""
    data: Optional[list[FetchPGReconData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    r"""Number of settlements you want to fetch in the next iteration."""
    

