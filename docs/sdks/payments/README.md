# Payments
(*payments*)

### Available Operations

* [get_paymentby_id](#get_paymentby_id) - Get Payment by ID
* [get_paymentsfororder](#get_paymentsfororder) - Get Payments for an Order

## get_paymentby_id

Use this API to view payment details of an order for a payment ID.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentbyIDRequest(
    cf_payment_id=607831,
    order_id='nemo',
    x_api_version='minima',
    x_client_id='excepturi',
    x_client_secret='accusantium',
)

res = s.payments.get_paymentby_id(req)

if res.payments_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetPaymentbyIDRequest](../../models/operations/getpaymentbyidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetPaymentbyIDResponse](../../models/operations/getpaymentbyidresponse.md)**


## get_paymentsfororder

Use this API to view all payment details for an order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentsfororderRequest(
    order_id='iure',
    x_api_version='culpa',
    x_client_id='doloribus',
    x_client_secret='sapiente',
)

res = s.payments.get_paymentsfororder(req)

if res.payments_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPaymentsfororderRequest](../../models/operations/getpaymentsfororderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetPaymentsfororderResponse](../../models/operations/getpaymentsfororderresponse.md)**

