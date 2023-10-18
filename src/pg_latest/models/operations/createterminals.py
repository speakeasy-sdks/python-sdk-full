"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createterminalrequest as shared_createterminalrequest
from ..shared import terminalresponse as shared_terminalresponse
from typing import Dict, List, Optional


@dataclasses.dataclass
class CreateTerminalsRequest:
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    create_terminal_request: Optional[shared_createterminalrequest.CreateTerminalRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_api_version: Optional[str] = dataclasses.field(default='2022-09-01', metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class CreateTerminalsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    headers: Optional[Dict[str, List[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    terminal_response: Optional[shared_terminalresponse.TerminalResponse] = dataclasses.field(default=None)
    r"""Terminal created"""
    

