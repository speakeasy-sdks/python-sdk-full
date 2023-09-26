# Refunds

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
        refund_amount=960.98,
        refund_id='reiciendis',
        refund_note='voluptatibus',
        refund_speed=shared.CreateRefundRequestRefundSpeed.INSTANT,
        refund_splits=[
            shared.VendorSplit(
                amount=4686.51,
                percentage=5096.24,
                vendor_id='voluptatibus',
            ),
        ],
    ),
    order_id='ipsa',
    x_api_version='omnis',
    x_client_id='voluptate',
    x_client_secret='cum',
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
    order_id='perferendis',
    refund_id='doloremque',
    x_api_version='reprehenderit',
    x_client_id='ut',
    x_client_secret='maiores',
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
    order_id='dicta',
    x_api_version='corporis',
    x_client_id='dolore',
    x_client_secret='iusto',
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

