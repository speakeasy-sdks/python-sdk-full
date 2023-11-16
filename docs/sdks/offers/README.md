# Offers
(*offers*)

### Available Operations

* [create_offer](#create_offer) - Create Offer
* [get_offer](#get_offer) - Get Offer by ID

## create_offer

Use this API to create offers with Cashfree from your backend

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.CreateOfferRequest(
    create_offer_backend_request=shared.CreateOfferBackendRequest(
        offer_details=shared.OfferDetails(
            cashback_details=shared.CashbackDetails(
                max_cashback_amount='string',
            ),
            discount_details=shared.DiscountDetails(
                discount_type=shared.DiscountType.PERCENTAGE,
                discount_value='string',
                max_discount_amount='string',
            ),
            offer_type=shared.OfferDetailsOfferType.DISCOUNT_AND_CASHBACK,
        ),
        offer_meta=shared.OfferMeta(
            offer_code='CFTESTOFFER',
            offer_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
            offer_end_time='2023-03-29T08:09:51Z',
            offer_start_time='2023-03-21T08:09:51Z',
            offer_title='Test Offer',
        ),
        offer_tnc=shared.OfferTnc(
            offer_tnc_type=shared.OfferTncType.POST,
            offer_tnc_value='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        ),
        offer_validations=shared.OfferValidations(
            max_allowed='10',
            min_amount='1',
            shared.OfferNB(
                netbanking=shared.NBOffer(
                    bank_name='all',
                ),
            ),
        ),
    ),
    x_client_id='string',
    x_client_secret='string',
)

res = s.offers.create_offer(req)

if res.offer_entity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOfferRequest](../../models/operations/createofferrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOfferResponse](../../models/operations/createofferresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_offer

Use this API to get offer by offer_id

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetOfferRequest(
    offer_id='string',
    x_client_id='string',
    x_client_secret='string',
)

res = s.offers.get_offer(req)

if res.offer_entity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetOfferRequest](../../models/operations/getofferrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetOfferResponse](../../models/operations/getofferresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
