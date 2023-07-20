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
        refund_amount=4417.11,
        refund_id='ut',
        refund_note='maiores',
        refund_speed=shared.CreateRefundRequestRefundSpeed.STANDARD,
        refund_splits=[
            shared.VendorSplit(
                amount=2961.4,
                percentage=4808.94,
                vendor_id='dicta',
            ),
            shared.VendorSplit(
                amount=6886.61,
                percentage=3179.83,
                vendor_id='accusamus',
            ),
        ],
    ),
    order_id='commodi',
    x_api_version='repudiandae',
    x_client_id='quae',
    x_client_secret='ipsum',
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
    order_id='quidem',
    refund_id='molestias',
    x_api_version='excepturi',
    x_client_id='pariatur',
    x_client_secret='modi',
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
    order_id='praesentium',
    x_api_version='rem',
    x_client_id='voluptates',
    x_client_secret='quasi',
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

