# EligibilityAPIs
(*eligibility_ap_is*)

### Available Operations

* [eligibility_cardless_emi](#eligibility_cardless_emi) - Get eligible Cardless EMI
* [eligibility_offer](#eligibility_offer) - Get eligible Offers
* [eligibility_paylater](#eligibility_paylater) - Get eligible Paylater

## eligibility_cardless_emi

Use this API to get eligible Cardless EMI Payment Methods for a customer on an order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.EligibilityCardlessEMIRequest(
    eligibility_cardless_emi_request=shared.EligibilityCardlessEMIRequest(
        queries=shared.CardlessEMIQueries(
            amount=100,
            customer_details=shared.CustomerDetailsCardlessEMI(
                customer_phone='9898989898',
            ),
            order_id='order_413462PK1RI1IwYB1X69LgzUQWiSxYDF',
        ),
    ),
    x_client_id='string',
    x_client_secret='string',
)

res = s.eligibility_ap_is.eligibility_cardless_emi(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.EligibilityCardlessEMIRequest](../../models/operations/eligibilitycardlessemirequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.EligibilityCardlessEMIResponse](../../models/operations/eligibilitycardlessemiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## eligibility_offer

Use this API to get eligible offers for an order or amount.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.EligibilityOfferRequest(
    eligibility_offers_request=shared.EligibilityOffersRequest(
        filters=shared.OfferFilters(
            offer_type=[
                shared.OfferType.CASHBACK,
            ],
        ),
        queries=shared.OfferQueries(
            amount=100,
            order_id='order_413462PK1RI1IwYB1X69LgzUQWiSxYDF',
        ),
    ),
    x_client_id='string',
    x_client_secret='string',
)

res = s.eligibility_ap_is.eligibility_offer(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.EligibilityOfferRequest](../../models/operations/eligibilityofferrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.EligibilityOfferResponse](../../models/operations/eligibilityofferresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## eligibility_paylater

Use this API to get eligible Paylater Payment Methods for a customer on an order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.EligibilityPaylaterRequest(
    eligibility_cardless_emi_request=shared.EligibilityCardlessEMIRequest(
        queries=shared.CardlessEMIQueries(
            amount=100,
            customer_details=shared.CustomerDetailsCardlessEMI(
                customer_phone='9898989898',
            ),
            order_id='order_413462PK1RI1IwYB1X69LgzUQWiSxYDF',
        ),
    ),
    x_client_id='string',
    x_client_secret='string',
)

res = s.eligibility_ap_is.eligibility_paylater(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.EligibilityPaylaterRequest](../../models/operations/eligibilitypaylaterrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.EligibilityPaylaterResponse](../../models/operations/eligibilitypaylaterresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
