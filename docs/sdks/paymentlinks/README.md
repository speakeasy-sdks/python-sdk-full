# payment_links

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
    link_id='dolores',
    x_api_version='dolorem',
    x_client_id='corporis',
    x_client_secret='explicabo',
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
            customer_email='nobis',
            customer_name='enim',
            customer_phone='omnis',
        ),
        link_amount=3637.11,
        link_auto_reminders=False,
        link_currency='minima',
        link_expiry_time='excepturi',
        link_id='accusantium',
        link_meta=shared.LinkMetaEntity(
            notify_url='iure',
            payment_methods='culpa',
            return_url='doloribus',
            upi_intent=False,
        ),
        link_minimum_partial_amount=9589.5,
        link_notes={
            "mollitia": 'dolorem',
        },
        link_notify=shared.LinkNotifyEntity(
            send_email=False,
            send_sms=False,
        ),
        link_partial_payments=False,
        link_purpose='culpa',
    ),
    x_api_version='consequuntur',
    x_client_id='repellat',
    x_client_secret='mollitia',
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
    link_id='occaecati',
    x_api_version='numquam',
    x_client_id='commodi',
    x_client_secret='quam',
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
    link_id='molestiae',
    x_api_version='velit',
    x_client_id='error',
    x_client_secret='quia',
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

