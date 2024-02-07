# Reconciliation
(*reconciliation*)

### Available Operations

* [post_recon](#post_recon) - PG Reconciliation
* [post_settlement_recon](#post_settlement_recon) - Settlement Reconciliation

## post_recon

Use this API to get the payment gateway reconciliation details with date range.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.PostReconRequest(
    x_client_id='string',
    x_client_secret='string',
    fetch_pg_recon_request=shared.FetchPGReconRequest(
        filters=shared.Filters(
            end_date='string',
            start_date='string',
        ),
        pagination=shared.Pagination(
            limit=85382,
        ),
    ),
)

res = s.reconciliation.post_recon(req)

if res.fetch_pg_recon is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PostReconRequest](../../models/operations/postreconrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostReconResponse](../../models/operations/postreconresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settlement_recon

Use this API to get settlement reconciliation details using Settlement ID, settlement UTR or date range.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.PostSettlementReconRequest(
    x_client_id='string',
    x_client_secret='string',
    fetch_settlement_recon_request=shared.FetchSettlementReconRequest(
        filters=shared.FetchSettlementReconRequestFilters(
            cf_settlement_ids=[
                956121,
            ],
            settlement_utrs=[
                'string',
            ],
        ),
        pagination=shared.FetchSettlementReconRequestPagination(
            limit=71166,
        ),
    ),
)

res = s.reconciliation.post_settlement_recon(req)

if res.fetch_settlement_recon is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostSettlementReconRequest](../../models/operations/postsettlementreconrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PostSettlementReconResponse](../../models/operations/postsettlementreconresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
