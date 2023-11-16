"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import errorresponse as shared_errorresponse
from ...models.shared import paymentsentity as shared_paymentsentity
from typing import Dict, List, Optional


@dataclasses.dataclass
class GetPaymentbyIDRequest:
    cf_payment_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'cf_payment_id', 'style': 'simple', 'explode': False }})
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    x_api_version: Optional[str] = dataclasses.field(default='2022-09-01', metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetPaymentbyIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Any bad or invalid request will lead to following error object"""
    payments_entity: Optional[shared_paymentsentity.PaymentsEntity] = dataclasses.field(default=None)
    r"""OK"""
    

