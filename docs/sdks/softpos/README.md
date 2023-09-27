# SoftPOS
(*soft_pos*)

## Overview

softPOS' agent and order management system now supported by APIs

### Available Operations

* [create_terminals](#create_terminals) - Create Terminal
* [get_terminal_by_mobile_number](#get_terminal_by_mobile_number) - Get terminal status using phone number

## create_terminals

Use this API to create new terminals to use softPOS.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.CreateTerminalsRequest(
    create_terminal_request=shared.CreateTerminalRequest(
        terminal_id='quasi',
        terminal_name='repudiandae',
        terminal_phone_no='sint',
    ),
    x_api_version='veritatis',
    x_client_id='itaque',
    x_client_secret='incidunt',
)

res = s.soft_pos.create_terminals(req)

if res.terminal_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateTerminalsRequest](../../models/operations/createterminalsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateTerminalsResponse](../../models/operations/createterminalsresponse.md)**


## get_terminal_by_mobile_number

Use this API to view all details of a terminal.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetTerminalByMobileNumberRequest(
    terminal_phone_no='enim',
    x_api_version='consequatur',
    x_client_id='est',
    x_client_secret='quibusdam',
)

res = s.soft_pos.get_terminal_by_mobile_number(req)

if res.terminal_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetTerminalByMobileNumberRequest](../../models/operations/getterminalbymobilenumberrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetTerminalByMobileNumberResponse](../../models/operations/getterminalbymobilenumberresponse.md)**

