# refunds

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
        refund_amount=1103.75,
        refund_id='laborum',
        refund_note='animi',
        refund_speed=shared.CreateRefundRequestRefundSpeed.STANDARD,
        refund_splits=[
            shared.VendorSplit(
                amount=1381.83,
                percentage=7783.46,
                vendor_id='sequi',
            ),
        ],
    ),
    order_id='tenetur',
    x_api_version='ipsam',
    x_client_id='id',
    x_client_secret='possimus',
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
    order_id='aut',
    refund_id='quasi',
    x_api_version='error',
    x_client_id='temporibus',
    x_client_secret='laborum',
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
    order_id='quasi',
    x_api_version='reiciendis',
    x_client_id='voluptatibus',
    x_client_secret='vero',
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

