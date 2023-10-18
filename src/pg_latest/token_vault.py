"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pg_latest import utils
from pg_latest.models import errors, operations, shared
from typing import List, Optional

class TokenVault:
    r"""Cashfree's token Vault helps you save cards and tokenize them in a PCI complaint manner. We support creation of network tokens which can be used across acquiring banks"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_specific_saved_instrument(self, request: operations.DeleteSpecificSavedInstrumentRequest) -> operations.DeleteSpecificSavedInstrumentResponse:
        r"""Delete Saved Instrument
        To delete a saved instrument for a customer id and instrument id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteSpecificSavedInstrumentRequest, base_url, '/customers/{customer_id}/instruments/{instrument_id}', request)
        headers = utils.get_headers(request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteSpecificSavedInstrumentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FetchAllSavedInstruments])
                res.fetch_all_saved_instruments = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        else:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def fetch_all_saved_instruments(self, request: operations.FetchAllSavedInstrumentsRequest) -> operations.FetchAllSavedInstrumentsResponse:
        r"""Fetch All Saved Instruments
        To get all saved instruments for a customer id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.FetchAllSavedInstrumentsRequest, base_url, '/customers/{customer_id}/instruments', request)
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.FetchAllSavedInstrumentsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FetchAllSavedInstrumentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.FetchAllSavedInstruments]])
                res.fetch_all_saved_instruments = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        else:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def fetch_cryptogram(self, request: operations.FetchCryptogramRequest) -> operations.FetchCryptogramResponse:
        r"""Fetch cryptogram for saved instrument
        To get the card network token, token expiry and cryptogram for a saved instrument using instrument id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.FetchCryptogramRequest, base_url, '/customers/{customer_id}/instruments/{instrument_id}/cryptogram', request)
        headers = utils.get_headers(request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FetchCryptogramResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Cryptogram])
                res.cryptogram = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        else:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def fetch_specific_saved_instrument(self, request: operations.FetchSpecificSavedInstrumentRequest) -> operations.FetchSpecificSavedInstrumentResponse:
        r"""Fetch Single Saved Instrument
        To get specific saved instrument for a customer id and instrument id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.FetchSpecificSavedInstrumentRequest, base_url, '/customers/{customer_id}/instruments/{instrument_id}', request)
        headers = utils.get_headers(request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FetchSpecificSavedInstrumentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FetchAllSavedInstruments])
                res.fetch_all_saved_instruments = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        else:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    