"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentmethodappinpaymentsentity import PaymentMethodAppInPaymentsEntity
from .paymentmethodcardinpaymentsentity import PaymentMethodCardInPaymentsEntity
from .paymentmethodcardlessemiinpaymentsentity import PaymentMethodCardlessEMIInPaymentsEntity
from .paymentmethodnetbankinginpaymentsentity import PaymentMethodNetBankingInPaymentsEntity
from .paymentmethodpaylaterinpaymentsentity import PaymentMethodPaylaterInPaymentsEntity
from .paymentmethodupiinpaymentsentity import PaymentMethodUPIInPaymentsEntity
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentMethodInPaymentsEntity:
    payment_method: Optional[Union[PaymentMethodCardInPaymentsEntity, PaymentMethodNetBankingInPaymentsEntity, PaymentMethodUPIInPaymentsEntity, PaymentMethodAppInPaymentsEntity, PaymentMethodCardlessEMIInPaymentsEntity, PaymentMethodPaylaterInPaymentsEntity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method'), 'exclude': lambda f: f is None }})
    

