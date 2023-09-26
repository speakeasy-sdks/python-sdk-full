# Offers

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
                cashback_type=shared.CashbackDetailsCashbackType.PERCENTAGE,
                cashback_value='iusto',
                max_cashback_amount='excepturi',
            ),
            discount_details=shared.DiscountDetails(
                discount_type=shared.DiscountDetailsDiscountType.FLAT,
                discount_value='recusandae',
                max_discount_amount='temporibus',
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
            offer_tnc_type=shared.OfferTncOfferTncType.LINK,
            offer_tnc_value='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        ),
        offer_validations=shared.OfferValidations(
            max_allowed='10',
            min_amount='1',
            payment_method=shared.OfferNB(
                netbanking=shared.NBOffer(
                    bank_name='all',
                ),
            ),
        ),
    ),
    x_api_version='veritatis',
    x_client_id='deserunt',
    x_client_secret='perferendis',
)

res = s.offers.create_offer(req)

if res.offer_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOfferRequest](../../models/operations/createofferrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOfferResponse](../../models/operations/createofferresponse.md)**


## get_offer

Use this API to get offer by offer_id

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetOfferRequest(
    offer_id='ipsam',
    x_api_version='repellendus',
    x_client_id='sapiente',
    x_client_secret='quo',
)

res = s.offers.get_offer(req)

if res.offer_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetOfferRequest](../../models/operations/getofferrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetOfferResponse](../../models/operations/getofferresponse.md)**

