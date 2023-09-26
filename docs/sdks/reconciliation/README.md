# Reconciliation

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
    fetch_pg_recon_request=shared.FetchPGReconRequest(
        filters=shared.FetchPGReconRequestFilters(
            end_date='vitae',
            start_date='laborum',
        ),
        pagination=shared.FetchPGReconRequestPagination(
            cursor='animi',
            limit=317202,
        ),
    ),
    x_api_version='odit',
    x_client_id='quo',
    x_client_secret='sequi',
)

res = s.reconciliation.post_recon(req)

if res.fetch_pg_recon is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PostReconRequest](../../models/operations/postreconrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostReconResponse](../../models/operations/postreconresponse.md)**


## post_settlement_recon

Use this API to get settlement reconciliation details using Settlement ID, settlement UTR or date range.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.PostSettlementReconRequest(
    fetch_settlement_recon_request=shared.FetchSettlementReconRequest(
        filters=shared.FetchSettlementReconRequestFilters(
            cf_settlement_ids=[
                949572,
            ],
            end_date='ipsam',
            settlement_utrs=[
                'id',
            ],
            start_date='possimus',
        ),
        pagination=shared.FetchSettlementReconRequestPagination(
            cursor='aut',
            limit=97101,
        ),
    ),
    x_api_version='error',
    x_client_id='temporibus',
    x_client_secret='laborum',
)

res = s.reconciliation.post_settlement_recon(req)

if res.fetch_settlement_recon is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostSettlementReconRequest](../../models/operations/postsettlementreconrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PostSettlementReconResponse](../../models/operations/postsettlementreconresponse.md)**

