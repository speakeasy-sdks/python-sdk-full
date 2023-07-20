# orders

### Available Operations

* [create_order](#create_order) - Create Order
* [get_order](#get_order) - Get Order
* [order_pay](#order_pay) - Order Pay
* [preauthorization](#preauthorization) - Preauthorization

## create_order

Use this API to create orders with Cashfree from your backend and get the payment link. To use this API S2S flag needs to be enabled from the backend. In case you want to use the cards payment option the PCI DSS flag is required, for more information email us at "care@cashfree.com".

### Example Usage

```python
import pg_latest
from pg_latest.models import callbacks, operations, shared

s = pg_latest.PGLatest()

req = operations.CreateOrderRequest(
    create_order_backend_request=shared.CreateOrderBackendRequest(
        customer_details=shared.CustomerDetails(
            customer_bank_account_number='sapiente',
            customer_bank_code='quo',
            customer_bank_ifsc='odit',
            customer_email='at',
            customer_id='at',
            customer_phone='maiores',
        ),
        order_amount=10.15,
        order_currency='INR',
        order_expiry_time='2021-07-29T00:00:00Z',
        order_id='molestiae',
        order_meta=shared.OrderMeta(
            notify_url='quod',
            payment_methods='quod',
            return_url='esse',
        ),
        order_note='Test order',
        order_splits=[
            shared.VendorSplit(
                amount=7805.29,
                percentage=6788.8,
                vendor_id='dicta',
            ),
            shared.VendorSplit(
                amount=7206.33,
                percentage=6399.21,
                vendor_id='occaecati',
            ),
            shared.VendorSplit(
                amount=1433.53,
                percentage=5373.73,
                vendor_id='hic',
            ),
        ],
        order_tags={
            "totam": 'beatae',
            "commodi": 'molestiae',
            "modi": 'qui',
            "impedit": 'cum',
        },
        terminal=shared.TerminalDetails(
            terminal_id='esse',
            terminal_phone_no='ipsum',
            terminal_type='excepturi',
        ),
    ),
    x_api_version='aspernatur',
    x_client_id='perferendis',
    x_client_secret='ad',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOrderRequest](../../models/operations/createorderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**


## get_order

Use this API to view all details of an order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetOrderRequest(
    order_id='natus',
    x_api_version='sed',
    x_client_id='iste',
    x_client_secret='dolor',
)

res = s.orders.get_order(req)

if res.orders_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetOrderRequest](../../models/operations/getorderrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetOrderResponse](../../models/operations/getorderresponse.md)**


## order_pay

Use this API when you have already created the orders and want Cashfree to process the payment. To use this API S2S flag needs to be enabled from the backend. In case you want to use the cards payment option the PCI DSS flag is required, for more information send an email to "care@cashfree.com".

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.OrderPayRequest(
    order_pay_request=shared.OrderPayRequest(
        offer_id='faa6cc05-d1e2-401c-b0cf-0c9db3ff0f0b',
        payment_method=shared.CardEMIPaymentMethod(
            emi=shared.CardEMI(
                card_alias='laboriosam',
                card_bank_name=shared.CardEMICardBankName.AMEX,
                card_cvv='saepe',
                card_expiry_mm='fuga',
                card_expiry_yy='in',
                card_holder_name='corporis',
                card_number='iste',
                channel='iure',
                emi_tenure=902349,
            ),
        ),
        payment_session_id='session__CvcEmNKDkmERQrxnx39ibhJ3Ii034pjc8ZVxf3qcgEXCWlgDDlHRgz2XYZCqpajDQSXMMtCusPgOIxYP2LZx0-05p39gC2Vgmq1RAj--gcn',
        save_instrument=False,
    ),
    x_api_version='quidem',
)

res = s.orders.order_pay(req)

if res.order_pay_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.OrderPayRequest](../../models/operations/orderpayrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.OrderPayResponse](../../models/operations/orderpayresponse.md)**


## preauthorization

Use this API to capture or void a preauthorized payment

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.PreauthorizationRequest(
    authorization_request=shared.AuthorizationRequest(
        action=shared.AuthorizationRequestAction.CAPTURE,
        amount=602.25,
    ),
    order_id='reiciendis',
    x_api_version='est',
    x_client_id='mollitia',
    x_client_secret='laborum',
)

res = s.orders.preauthorization(req)

if res.payments_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PreauthorizationRequest](../../models/operations/preauthorizationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PreauthorizationResponse](../../models/operations/preauthorizationresponse.md)**

