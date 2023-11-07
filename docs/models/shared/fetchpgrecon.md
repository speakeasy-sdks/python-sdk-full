# FetchPGRecon


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `cursor`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Specifies from where the next set of settlement details should be fetched. |
| `data`                                                                     | List[[shared.Data](../../models/shared/data.md)]                           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `limit`                                                                    | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | Number of settlements you want to fetch in the next iteration.             |