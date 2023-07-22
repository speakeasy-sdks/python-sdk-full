# Cryptogram

OK


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `card_display`                        | *Optional[str]*                       | :heavy_minus_sign:                    | last 4 digits of original card number |
| `card_expiry_mm`                      | *Optional[str]*                       | :heavy_minus_sign:                    | token pan expiry month                |
| `card_expiry_yy`                      | *Optional[str]*                       | :heavy_minus_sign:                    | token pan expiry year                 |
| `card_number`                         | *Optional[str]*                       | :heavy_minus_sign:                    | token pan number                      |
| `cryptogram`                          | *Optional[str]*                       | :heavy_minus_sign:                    | cryptogram                            |
| `instrument_id`                       | *Optional[str]*                       | :heavy_minus_sign:                    | instrument_id of saved instrument     |
| `token_requestor_id`                  | *Optional[str]*                       | :heavy_minus_sign:                    | TRID issued by card networks          |