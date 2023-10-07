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
    fetch_pg_recon_request=shared.FetchPGReconRequest(
        filters=shared.FetchPGReconRequestFilters(
            end_date='Bentley',
            start_date='Bolingbrook Generic',
        ),
        pagination=shared.FetchPGReconRequestPagination(
            limit=405830,
        ),
    ),
    x_client_id='joule',
    x_client_secret='Diesel Liaison',
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
                956121,
            ],
            settlement_utrs=[
                'Buckinghamshire',
            ],
        ),
        pagination=shared.FetchSettlementReconRequestPagination(
            limit=661166,
        ),
    ),
    x_client_id='pro',
    x_client_secret='Southeast schemas',
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

