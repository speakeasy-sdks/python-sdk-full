"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pg_latest import utils
from pg_latest.models import errors, operations, shared
from typing import Optional

class Authentication:
    r"""The Authentication API allows merchants to show a native screen and capture OTP on their own page and submit to Cashfree. This feature is only available on request."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def otp_request(self, request: operations.OTPRequestRequest) -> operations.OTPRequestResponse:
        r"""Submit or Resend OTP
        If you accept OTP on your own page, you can use the below API to send OTP to Cashfree.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.OTPRequestRequest, base_url, '/orders/pay/authenticate/{payment_id}', request)
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, operations.OTPRequestRequest, "otp_request", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.OTPRequestResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res, headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OTPResponseEntity])
                res.otp_response_entity = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    