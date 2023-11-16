"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils
from typing import Optional

class OTPResponseEntityAction(str, Enum):
    r"""The action that was invoked for this request."""
    SUBMIT_OTP = 'SUBMIT_OTP'
    RESEND_OTP = 'RESEND_OTP'

class AuthenticateStatus(str, Enum):
    r"""Status of the is action. Will be either failed or successful. If the action is successful, you should still call the authorization status to verify the final payment status."""
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OTPResponseEntity:
    r"""This is the response shared when merchant inovkes the OTP submit or resend API"""
    action: Optional[OTPResponseEntityAction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action'), 'exclude': lambda f: f is None }})
    r"""The action that was invoked for this request."""
    authenticate_status: Optional[AuthenticateStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authenticate_status'), 'exclude': lambda f: f is None }})
    r"""Status of the is action. Will be either failed or successful. If the action is successful, you should still call the authorization status to verify the final payment status."""
    cf_payment_id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_payment_id'), 'exclude': lambda f: f is None }})
    r"""The payment id for which this request was sent"""
    payment_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_message'), 'exclude': lambda f: f is None }})
    r"""Human readable message which describes the status in more detail"""
    

