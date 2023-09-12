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
    link_id='perferendis',
    x_api_version='ad',
    x_client_id='natus',
    x_client_secret='sed',
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
            customer_email='iste',
            customer_name='dolor',
            customer_phone='natus',
        ),
        link_amount=3864.89,
        link_auto_reminders=False,
        link_currency='hic',
        link_expiry_time='saepe',
        link_id='fuga',
        link_meta=shared.LinkMetaEntity(
            notify_url='in',
            payment_methods='corporis',
            return_url='iste',
            upi_intent=False,
        ),
        link_minimum_partial_amount=4370.32,
        link_notes={
            "saepe": 'quidem',
        },
        link_notify=shared.LinkNotifyEntity(
            send_email=False,
            send_sms=False,
        ),
        link_partial_payments=False,
        link_purpose='architecto',
    ),
    x_api_version='ipsa',
    x_client_id='reiciendis',
    x_client_secret='est',
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
    link_id='mollitia',
    x_api_version='laborum',
    x_client_id='dolores',
    x_client_secret='dolorem',
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
    link_id='corporis',
    x_api_version='explicabo',
    x_client_id='nobis',
    x_client_secret='enim',
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

