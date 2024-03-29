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
    cf_payment_id=310675,
    order_id='<value>',
    x_client_id='<value>',
    x_client_secret='<value>',
)

res = s.payments.get_paymentby_id(req)

if res.payments_entity is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetPaymentbyIDRequest](../../models/operations/getpaymentbyidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetPaymentbyIDResponse](../../models/operations/getpaymentbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_paymentsfororder

Use this API to view all payment details for an order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetPaymentsfororderRequest(
    order_id='<value>',
    x_client_id='<value>',
    x_client_secret='<value>',
)

res = s.payments.get_paymentsfororder(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPaymentsfororderRequest](../../models/operations/getpaymentsfororderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetPaymentsfororderResponse](../../models/operations/getpaymentsfororderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
