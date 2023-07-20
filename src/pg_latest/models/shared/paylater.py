"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg_latest import utils
from typing import Optional

class PaylaterProvider(str, Enum):
    r"""One of [\\"kotak\\", \\"flexipay\\", \\"zestmoney\\", \\"lazypay\\", \\"olapostpaid\\",\\"simpl\\", \\"freechargepaylater\\"]. Please note that Flexipay is offered by HDFC bank"""
    KOTAK = 'kotak'
    FLEXIPAY = 'flexipay'
    ZESTMONEY = 'zestmoney'
    LAZYPAY = 'lazypay'
    OLAPOSTPAID = 'olapostpaid'
    SIMPL = 'simpl'
    FREECHARGEPAYLATER = 'freechargepaylater'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Paylater:
    channel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    r"""The channel for cardless EMI is always `link`"""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Customers phone number for this payment instrument. If the customer is not eligible you will receive a 400 error with type as 'invalid_request_error' and code as 'invalid_request_error'"""
    provider: Optional[PaylaterProvider] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    r"""One of [\\"kotak\\", \\"flexipay\\", \\"zestmoney\\", \\"lazypay\\", \\"olapostpaid\\",\\"simpl\\", \\"freechargepaylater\\"]. Please note that Flexipay is offered by HDFC bank"""
    

