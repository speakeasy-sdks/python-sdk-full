"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple
from .utils.retries import RetryConfig
from .utils import utils


SERVERS = [
    'https://sandbox.cashfree.com/pg',
    # Sandbox server
    'https://api.cashfree.com/pg',
    # Production server
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '2022-09-01'
    sdk_version: str = '3.1.0'
    gen_version: str = '2.213.3'
    user_agent: str = 'speakeasy-sdk/python 3.1.0 2.213.3 2022-09-01 PG-Latest'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
