# settlements

### Available Operations

* [getsettlements](#getsettlements) - Get Settlements by Order ID
* [post_settlements](#post_settlements) - Get All Settlements

## getsettlements

Use this API to view all the settlements of a particular order.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetsettlementsRequest(
    order_id='repudiandae',
    x_api_version='sint',
    x_client_id='veritatis',
    x_client_secret='itaque',
)

res = s.settlements.getsettlements(req)

if res.settlements_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetsettlementsRequest](../../models/operations/getsettlementsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetsettlementsResponse](../../models/operations/getsettlementsresponse.md)**


## post_settlements

Use this API to get all settlement details by specifying the settlement ID, settlement UTR or date range.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.PostSettlementsRequest(
    fetch_settlement_recon_request=shared.FetchSettlementReconRequest(
        filters=shared.FetchSettlementReconRequestFilters(
            cf_settlement_ids=[
                318569,
                9356,
            ],
            end_date='est',
            settlement_utrs=[
                'explicabo',
                'deserunt',
                'distinctio',
                'quibusdam',
            ],
            start_date='labore',
        ),
        pagination=shared.FetchSettlementReconRequestPagination(
            cursor='modi',
            limit=183191,
        ),
    ),
    x_api_version='aliquid',
    x_client_id='cupiditate',
    x_client_secret='quos',
)

res = s.settlements.post_settlements(req)

if res.fetch_settlement is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PostSettlementsRequest](../../models/operations/postsettlementsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PostSettlementsResponse](../../models/operations/postsettlementsresponse.md)**

