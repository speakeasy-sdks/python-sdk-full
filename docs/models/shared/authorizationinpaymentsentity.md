# AuthorizationInPaymentsEntity

The authorization details are present for payments which go through the preauthorization workflow. Or else this parameter will be null.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `action`                                                              | [Optional[shared.Action]](../../models/shared/action.md)              | :heavy_minus_sign:                                                    | One of CAPTURE or VOID                                                |
| `action_reference`                                                    | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | CAPTURE or VOID reference number based on action                      |
| `action_time`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Time of action (CAPTURE or VOID)                                      |
| `approve_by`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Approve by time as passed in the authorization request (only for UPI) |
| `captured_amount`                                                     | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | The captured amount for this authorization request                    |
| `end_time`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | End time of this authorization hold (only for UPI)                    |
| `start_time`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Start time of this authorization hold (only for UPI)                  |
| `status`                                                              | [Optional[shared.Status]](../../models/shared/status.md)              | :heavy_minus_sign:                                                    | One of SUCCESS or PENDING                                             |