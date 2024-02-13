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
    x_client_id='string',
    x_client_secret='string',
    create_terminal_request=shared.CreateTerminalRequest(
        terminal_name='Jane Doe',
        terminal_phone_no='9876543210',
        terminal_id='1',
    ),
)

res = s.soft_pos.create_terminals(req)

if res.terminal_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateTerminalsRequest](../../models/operations/createterminalsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateTerminalsResponse](../../models/operations/createterminalsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_terminal_by_mobile_number

Use this API to view all details of a terminal.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.GetTerminalByMobileNumberRequest(
    terminal_phone_no='string',
    x_client_id='string',
    x_client_secret='string',
)

res = s.soft_pos.get_terminal_by_mobile_number(req)

if res.terminal_details is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetTerminalByMobileNumberRequest](../../models/operations/getterminalbymobilenumberrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetTerminalByMobileNumberResponse](../../models/operations/getterminalbymobilenumberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
