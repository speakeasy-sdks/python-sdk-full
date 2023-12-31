"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils
from typing import Optional

class Action(str, Enum):
    r"""One of CAPTURE or VOID"""
    CAPTURE = 'CAPTURE'
    VOID = 'VOID'

class Status(str, Enum):
    r"""One of SUCCESS or PENDING"""
    SUCCESS = 'SUCCESS'
    PENDING = 'PENDING'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthorizationInPaymentsEntity:
    r"""The authorization details are present for payments which go through the preauthorization workflow. Or else this parameter will be null."""
    action: Optional[Action] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action'), 'exclude': lambda f: f is None }})
    r"""One of CAPTURE or VOID"""
    action_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_reference'), 'exclude': lambda f: f is None }})
    r"""CAPTURE or VOID reference number based on action"""
    action_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_time'), 'exclude': lambda f: f is None }})
    r"""Time of action (CAPTURE or VOID)"""
    approve_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approve_by'), 'exclude': lambda f: f is None }})
    r"""Approve by time as passed in the authorization request (only for UPI)"""
    captured_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('captured_amount'), 'exclude': lambda f: f is None }})
    r"""The captured amount for this authorization request"""
    end_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'exclude': lambda f: f is None }})
    r"""End time of this authorization hold (only for UPI)"""
    start_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'exclude': lambda f: f is None }})
    r"""Start time of this authorization hold (only for UPI)"""
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""One of SUCCESS or PENDING"""
    

