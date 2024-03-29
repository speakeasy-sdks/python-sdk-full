# Settlements
(*settlements*)

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
    order_id='<value>',
    x_client_id='<value>',
    x_client_secret='<value>',
)

res = s.settlements.getsettlements(req)

if res.settlements_entity is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetsettlementsRequest](../../models/operations/getsettlementsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetsettlementsResponse](../../models/operations/getsettlementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settlements

Use this API to get all settlement details by specifying the settlement ID, settlement UTR or date range.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.PostSettlementsRequest(
    x_client_id='<value>',
    x_client_secret='<value>',
    fetch_settlement_recon_request=shared.FetchSettlementReconRequest(
        filters=shared.FetchSettlementReconRequestFilters(
            cf_settlement_ids=[
                4234233,
            ],
            end_date='2022-07-21T23:59:59Z',
            settlement_utrs=[
                'utr1',
                'utr2',
            ],
            start_date='2022-07-20T00:00:00Z',
        ),
        pagination=shared.FetchSettlementReconRequestPagination(
            limit=10,
            cursor='eyJzZWFyY2hBZnRlciI6eyJsaXN0IjpbMTg4NjcxNDVdLCJlbXB0eSI6ZmFsc2V9LCJyZWNvbkFQSVR5cGUiOiJMRURHRVIifQ==',
        ),
    ),
)

res = s.settlements.post_settlements(req)

if res.fetch_settlement is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PostSettlementsRequest](../../models/operations/postsettlementsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PostSettlementsResponse](../../models/operations/postsettlementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
