"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import eligibilityoffersrequest as shared_eligibilityoffersrequest
from ...models.shared import eligibleoffersentity as shared_eligibleoffersentity
from typing import Dict, List, Optional


@dataclasses.dataclass
class EligibilityOfferRequest:
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    eligibility_offers_request: Optional[shared_eligibilityoffersrequest.EligibilityOffersRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_api_version: Optional[str] = dataclasses.field(default='2022-09-01', metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class EligibilityOfferResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_eligibleoffersentity.EligibleOffersEntity]] = dataclasses.field(default=None)
    r"""OK"""
    

