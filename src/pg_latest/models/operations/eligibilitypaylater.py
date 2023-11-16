"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import eligibilitycardlessemirequest as shared_eligibilitycardlessemirequest
from ...models.shared import eligiblepaylater as shared_eligiblepaylater
from typing import Dict, List, Optional


@dataclasses.dataclass
class EligibilityPaylaterRequest:
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    eligibility_cardless_emi_request: Optional[shared_eligibilitycardlessemirequest.EligibilityCardlessEMIRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_api_version: Optional[str] = dataclasses.field(default='2022-09-01', metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class EligibilityPaylaterResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_eligiblepaylater.EligiblePaylater]] = dataclasses.field(default=None)
    r"""OK"""
    

