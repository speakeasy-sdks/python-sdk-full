# Refunds
(*refunds*)

### Available Operations

* [createrefund](#createrefund) - Create Refund
* [get_refund](#get_refund) - Get Refund
* [getallrefundsfororder](#getallrefundsfororder) - Get All Refunds for an Order

## createrefund

Use this API to initiate refunds.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.CreaterefundRequest(
    create_refund_request=shared.CreateRefundRequest(
        refund_amount=567.71,
        refund_id='overstate Rutherfordium',
        refund_note='perferendis Account',
        refund_speed=shared.CreateRefundRequestRefundSpeed.INSTANT,
        refund_splits=[
            shared.VendorSplit(
                amount=9046.67,
                percentage=2487.44,
                vendor_id='Rubber raccoon Division',
            ),
        ],
    ),
    order_id='alarming back',
    x_api_version='users',
    x_client_id='Administrator whiteboard',
    x_client_secret='Transgender Identity Berkshire',
)

res = s.refunds.createrefund(req)

if res.refunds_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreaterefundRequest](../../models/operations/createrefundrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreaterefundResponse](../../models/operations/createrefundresponse.md)**


## get_refund

Use this API to fetch a specific refund processed on your Cashfree Account.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetRefundRequest(
    order_id='Connecticut East aliquid',
    refund_id='Chair',
    x_api_version='Elbert Personal Electric',
    x_client_id='Director Beach Borders',
    x_client_secret='networks Electric',
)

res = s.refunds.get_refund(req)

if res.refunds_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetRefundRequest](../../models/operations/getrefundrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetRefundResponse](../../models/operations/getrefundresponse.md)**


## getallrefundsfororder

Use this API to fetch all refunds processed against an order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetallrefundsfororderRequest(
    order_id='trial South',
    x_api_version='Music',
    x_client_id='Recycled red',
    x_client_secret='newton Lodge',
)

res = s.refunds.getallrefundsfororder(req)

if res.refunds_entities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetallrefundsfororderRequest](../../models/operations/getallrefundsfororderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetallrefundsfororderResponse](../../models/operations/getallrefundsfororderresponse.md)**

