"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import settlementsentity as shared_settlementsentity
from typing import Optional



@dataclasses.dataclass
class GetsettlementsRequest:
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    x_api_version: Optional[str] = dataclasses.field(default='2022-09-01', metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetsettlementsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Any bad or invalid request will lead to following error object"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    settlements_entity: Optional[shared_settlementsentity.SettlementsEntity] = dataclasses.field(default=None)
    r"""OK"""
    

