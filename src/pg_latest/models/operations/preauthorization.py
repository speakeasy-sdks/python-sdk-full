"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import authorizationrequest as shared_authorizationrequest
from ..shared import errorresponse as shared_errorresponse
from ..shared import paymentsentity as shared_paymentsentity
from typing import Optional



@dataclasses.dataclass
class PreauthorizationRequest:
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    authorization_request: Optional[shared_authorizationrequest.AuthorizationRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class PreauthorizationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Any bad or invalid request will lead to following error object"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    payments_entity: Optional[shared_paymentsentity.PaymentsEntity] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

