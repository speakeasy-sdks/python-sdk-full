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
    link_id='string',
    x_client_id='string',
    x_client_secret='string',
)

res = s.payment_links.cancel_payment_link(req)

if res.link_cancelled_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CancelPaymentLinkRequest](../../models/operations/cancelpaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CancelPaymentLinkResponse](../../models/operations/cancelpaymentlinkresponse.md)**
### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.LinkCancelledError | 400                       | application/json          |
| errors.SDKError           | 4x-5xx                    | */*                       |

## create_payment_link

Use this API to create a new payment link. The created payment link url will be available in the API response parameter link_url.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.CreatePaymentLinkRequest(
    x_client_id='string',
    x_client_secret='string',
    create_link_request=shared.CreateLinkRequest(
        customer_details=shared.LinkCustomerDetailsEntity(
            customer_phone='string',
        ),
        link_amount=100,
        link_currency='INR',
        link_id='my_link_id',
        link_purpose='Payment for PlayStation 11',
        link_auto_reminders=True,
        link_expiry_time='2021-10-14T15:04:05+05:30',
        link_meta=shared.LinkMetaEntity(),
        link_minimum_partial_amount=20,
        link_notes={
            '$ref': '#/components/schemas/LinkNotesEntity/example',
        },
        link_notify=shared.LinkNotifyEntity(),
        link_partial_payments=True,
    ),
)

res = s.payment_links.create_payment_link(req)

if res.link_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreatePaymentLinkRequest](../../models/operations/createpaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreatePaymentLinkResponse](../../models/operations/createpaymentlinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_payment_link_details

Use this API to view all details and status of a payment link.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentLinkDetailsRequest(
    link_id='string',
    x_client_id='string',
    x_client_secret='string',
)

res = s.payment_links.get_payment_link_details(req)

if res.link_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetPaymentLinkDetailsRequest](../../models/operations/getpaymentlinkdetailsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetPaymentLinkDetailsResponse](../../models/operations/getpaymentlinkdetailsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_payment_link_orders

Use this API to view all order details for a payment link.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentLinkOrdersRequest(
    link_id='string',
    x_client_id='string',
    x_client_secret='string',
)

res = s.payment_links.get_payment_link_orders(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetPaymentLinkOrdersRequest](../../models/operations/getpaymentlinkordersrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetPaymentLinkOrdersResponse](../../models/operations/getpaymentlinkordersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
