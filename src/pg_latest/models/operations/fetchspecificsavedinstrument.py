"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import fetchallsavedinstruments as shared_fetchallsavedinstruments
from typing import Optional



@dataclasses.dataclass
class FetchSpecificSavedInstrumentRequest:
    customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customer_id', 'style': 'simple', 'explode': False }})
    instrument_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'instrument_id', 'style': 'simple', 'explode': False }})
    x_client_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-id', 'style': 'simple', 'explode': False }})
    x_client_secret: str = dataclasses.field(metadata={'header': { 'field_name': 'x-client-secret', 'style': 'simple', 'explode': False }})
    x_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-api-version', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class FetchSpecificSavedInstrumentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Any bad or invalid request will lead to following error object"""
    fetch_all_saved_instruments: Optional[shared_fetchallsavedinstruments.FetchAllSavedInstruments] = dataclasses.field(default=None)
    r"""OK"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

