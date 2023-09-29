# PaymentLinks
(*payment_links*)

### Available Operations

* [cancel_payment_link](#cancel_payment_link) - Cancel Payment Link
* [create_payment_link](#create_payment_link) - Create Payment Link
* [get_payment_link_details](#get_payment_link_details) - Fetch Payment Link Details
* [get_payment_link_orders](#get_payment_link_orders) - Get Orders for a Payment Link

## cancel_payment_link

Use this API to cancel a payment link. No further payments can be done against a cancelled link. Only a link in ACTIVE status can be cancelled.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.CancelPaymentLinkRequest(
    link_id='Mercury Michel',
    x_api_version='yellow',
    x_client_id='Draper sweltering Diesel',
    x_client_secret='Maine',
)

res = s.payment_links.cancel_payment_link(req)

if res.link_cancelled_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CancelPaymentLinkRequest](../../models/operations/cancelpaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CancelPaymentLinkResponse](../../models/operations/cancelpaymentlinkresponse.md)**


## create_payment_link

Use this API to create a new payment link. The created payment link url will be available in the API response parameter link_url.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.CreatePaymentLinkRequest(
    create_link_request=shared.CreateLinkRequest(
        customer_details=shared.LinkCustomerDetailsEntity(
            customer_email='grin Fort',
            customer_name='Licensed',
            customer_phone='firewall Bicycle Jordan',
        ),
        link_amount=4444.02,
        link_auto_reminders=False,
        link_currency='reintermediate',
        link_expiry_time='Forward Reggae Designer',
        link_id='fuga flexibility',
        link_meta=shared.LinkMetaEntity(
            notify_url='female',
            payment_methods='Northeast Blues Communications',
            return_url='SUV Smart Clothing',
            upi_intent=False,
        ),
        link_minimum_partial_amount=7331.25,
        link_notes={
            "quia": 'Bermuda',
        },
        link_notify=shared.LinkNotifyEntity(
            send_email=False,
            send_sms=False,
        ),
        link_partial_payments=False,
        link_purpose='brr Account',
    ),
    x_api_version='Colombia',
    x_client_id='firewall Bicycle Ferry',
    x_client_secret='static',
)

res = s.payment_links.create_payment_link(req)

if res.link_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreatePaymentLinkRequest](../../models/operations/createpaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreatePaymentLinkResponse](../../models/operations/createpaymentlinkresponse.md)**


## get_payment_link_details

Use this API to view all details and status of a payment link.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentLinkDetailsRequest(
    link_id='Bayamon male Northwest',
    x_api_version='regional Hybrid ew',
    x_client_id='Operative',
    x_client_secret='migrate Southwest',
)

res = s.payment_links.get_payment_link_details(req)

if res.link_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetPaymentLinkDetailsRequest](../../models/operations/getpaymentlinkdetailsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetPaymentLinkDetailsResponse](../../models/operations/getpaymentlinkdetailsresponse.md)**


## get_payment_link_orders

Use this API to view all order details for a payment link.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentLinkOrdersRequest(
    link_id='North sophomore',
    x_api_version='Supervisor sue Tunnel',
    x_client_id='Account',
    x_client_secret='Ferrari South Beauty',
)

res = s.payment_links.get_payment_link_orders(req)

if res.link_orders_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetPaymentLinkOrdersRequest](../../models/operations/getpaymentlinkordersrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetPaymentLinkOrdersResponse](../../models/operations/getpaymentlinkordersresponse.md)**

