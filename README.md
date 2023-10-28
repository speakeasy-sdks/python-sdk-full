# PG-Latest

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/python-sdk-full.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.OTPRequestRequest(
    otp_request=shared.OTPRequest(
        action=shared.OTPRequestAction.SUBMIT_OTP,
        otp='string',
    ),
    payment_id='string',
)

res = s.authentication.otp_request(req)

if res.otp_response_entity is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [authentication](docs/sdks/authentication/README.md)

* [otp_request](docs/sdks/authentication/README.md#otp_request) - Submit or Resend OTP

### [eligibility_ap_is](docs/sdks/eligibilityapis/README.md)

* [eligibility_cardless_emi](docs/sdks/eligibilityapis/README.md#eligibility_cardless_emi) - Get eligible Cardless EMI
* [eligibility_offer](docs/sdks/eligibilityapis/README.md#eligibility_offer) - Get eligible Offers
* [eligibility_paylater](docs/sdks/eligibilityapis/README.md#eligibility_paylater) - Get eligible Paylater

### [offers](docs/sdks/offers/README.md)

* [create_offer](docs/sdks/offers/README.md#create_offer) - Create Offer
* [get_offer](docs/sdks/offers/README.md#get_offer) - Get Offer by ID

### [orders](docs/sdks/orders/README.md)

* [create_order](docs/sdks/orders/README.md#create_order) - Create Order
* [get_order](docs/sdks/orders/README.md#get_order) - Get Order
* [order_pay](docs/sdks/orders/README.md#order_pay) - Order Pay
* [preauthorization](docs/sdks/orders/README.md#preauthorization) - Preauthorization

### [payment_links](docs/sdks/paymentlinks/README.md)

* [cancel_payment_link](docs/sdks/paymentlinks/README.md#cancel_payment_link) - Cancel Payment Link
* [create_payment_link](docs/sdks/paymentlinks/README.md#create_payment_link) - Create Payment Link
* [get_payment_link_details](docs/sdks/paymentlinks/README.md#get_payment_link_details) - Fetch Payment Link Details
* [get_payment_link_orders](docs/sdks/paymentlinks/README.md#get_payment_link_orders) - Get Orders for a Payment Link

### [payments](docs/sdks/payments/README.md)

* [get_paymentby_id](docs/sdks/payments/README.md#get_paymentby_id) - Get Payment by ID
* [get_paymentsfororder](docs/sdks/payments/README.md#get_paymentsfororder) - Get Payments for an Order

### [reconciliation](docs/sdks/reconciliation/README.md)

* [post_recon](docs/sdks/reconciliation/README.md#post_recon) - PG Reconciliation
* [post_settlement_recon](docs/sdks/reconciliation/README.md#post_settlement_recon) - Settlement Reconciliation

### [refunds](docs/sdks/refunds/README.md)

* [createrefund](docs/sdks/refunds/README.md#createrefund) - Create Refund
* [get_refund](docs/sdks/refunds/README.md#get_refund) - Get Refund
* [getallrefundsfororder](docs/sdks/refunds/README.md#getallrefundsfororder) - Get All Refunds for an Order

### [settlements](docs/sdks/settlements/README.md)

* [getsettlements](docs/sdks/settlements/README.md#getsettlements) - Get Settlements by Order ID
* [post_settlements](docs/sdks/settlements/README.md#post_settlements) - Get All Settlements

### [token_vault](docs/sdks/tokenvault/README.md)

* [delete_specific_saved_instrument](docs/sdks/tokenvault/README.md#delete_specific_saved_instrument) - Delete Saved Instrument
* [fetch_all_saved_instruments](docs/sdks/tokenvault/README.md#fetch_all_saved_instruments) - Fetch All Saved Instruments
* [fetch_cryptogram](docs/sdks/tokenvault/README.md#fetch_cryptogram) - Fetch cryptogram for saved instrument
* [fetch_specific_saved_instrument](docs/sdks/tokenvault/README.md#fetch_specific_saved_instrument) - Fetch Single Saved Instrument

### [soft_pos](docs/sdks/softpos/README.md)

* [create_terminals](docs/sdks/softpos/README.md#create_terminals) - Create Terminal
* [get_terminal_by_mobile_number](docs/sdks/softpos/README.md#get_terminal_by_mobile_number) - Get terminal status using phone number
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://sandbox.cashfree.com/pg` | None |
| 1 | `https://api.cashfree.com/pg` | None |

For example:


```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest(
    server_idx=1
)

req = operations.OTPRequestRequest(
    otp_request=shared.OTPRequest(
        action=shared.OTPRequestAction.SUBMIT_OTP,
        otp='string',
    ),
    payment_id='string',
)

res = s.authentication.otp_request(req)

if res.otp_response_entity is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest(
    server_url="https://sandbox.cashfree.com/pg"
)

req = operations.OTPRequestRequest(
    otp_request=shared.OTPRequest(
        action=shared.OTPRequestAction.SUBMIT_OTP,
        otp='string',
    ),
    payment_id='string',
)

res = s.authentication.otp_request(req)

if res.otp_response_entity is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import pg_latest
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = pg_latest.PGLatest(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
