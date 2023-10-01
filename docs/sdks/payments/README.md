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
    order_id='coulomb',
    x_api_version='Solutions',
    x_client_id='Surinam Centreville Berkshire',
    x_client_secret='Consultant Southwest',
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
    order_id='female indexing',
    x_api_version='Convertible Regional SAS',
    x_client_id='Salad',
    x_client_secret='copying Daniel',
)

res = s.payments.get_paymentsfororder(req)

if res.get_paymentsfororder_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPaymentsfororderRequest](../../models/operations/getpaymentsfororderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetPaymentsfororderResponse](../../models/operations/getpaymentsfororderresponse.md)**

