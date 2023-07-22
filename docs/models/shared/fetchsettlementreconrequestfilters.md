# FetchSettlementReconRequestFilters

Specify either the Settlement ID, Settlement UTR, or start date and end date to fetch the settlement details.


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `cf_settlement_ids`                                                               | list[*int*]                                                                       | :heavy_minus_sign:                                                                | List of settlement IDs for which you want the settlement reconciliation details.  |
| `end_date`                                                                        | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Specify the end date till when you want the settlement reconciliation details.    |
| `settlement_utrs`                                                                 | list[*str*]                                                                       | :heavy_minus_sign:                                                                | List of settlement UTRs for which you want the settlement reconciliation details. |
| `start_date`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Specify the start date from when you want the settlement reconciliation details.  |