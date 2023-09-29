"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import linkordersresponse as shared_linkordersresponse
from typing import Optional



@dataclasses.dataclass
class GetPaymentLinkOrdersRequest:
    link_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'link_id', 'style': 'simple', 'explode': False }})
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    x_api_version: Optional[str] = dataclasses.field(default='2022-09-01', metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetPaymentLinkOrdersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    link_orders_responses: Optional[list[shared_linkordersresponse.LinkOrdersResponse]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

