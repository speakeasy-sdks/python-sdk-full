# TokenVault
(*token_vault*)

## Overview

Cashfree's token Vault helps you save cards and tokenize them in a PCI complaint manner. We support creation of network tokens which can be used across acquiring banks

### Available Operations

* [delete_specific_saved_instrument](#delete_specific_saved_instrument) - Delete Saved Instrument
* [fetch_all_saved_instruments](#fetch_all_saved_instruments) - Fetch All Saved Instruments
* [fetch_cryptogram](#fetch_cryptogram) - Fetch cryptogram for saved instrument
* [fetch_specific_saved_instrument](#fetch_specific_saved_instrument) - Fetch Single Saved Instrument

## delete_specific_saved_instrument

To delete a saved instrument for a customer id and instrument id

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.DeleteSpecificSavedInstrumentRequest(
    customer_id='West',
    instrument_id='Sports',
    x_client_id='Buckinghamshire',
    x_client_secret='azure',
)

res = s.token_vault.delete_specific_saved_instrument(req)

if res.fetch_all_saved_instruments is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteSpecificSavedInstrumentRequest](../../models/operations/deletespecificsavedinstrumentrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteSpecificSavedInstrumentResponse](../../models/operations/deletespecificsavedinstrumentresponse.md)**


## fetch_all_saved_instruments

To get all saved instruments for a customer id

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.FetchAllSavedInstrumentsRequest(
    customer_id='Louisiana',
    instrument_type=operations.FetchAllSavedInstrumentsInstrumentType.CARD,
    x_client_id='SDD',
    x_client_secret='Diesel',
)

res = s.token_vault.fetch_all_saved_instruments(req)

if res.fetch_all_saved_instruments is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.FetchAllSavedInstrumentsRequest](../../models/operations/fetchallsavedinstrumentsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.FetchAllSavedInstrumentsResponse](../../models/operations/fetchallsavedinstrumentsresponse.md)**


## fetch_cryptogram

To get the card network token, token expiry and cryptogram for a saved instrument using instrument id

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.FetchCryptogramRequest(
    customer_id='BMW',
    instrument_id='invoice',
    x_client_id='Honda',
    x_client_secret='overbook',
)

res = s.token_vault.fetch_cryptogram(req)

if res.cryptogram is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.FetchCryptogramRequest](../../models/operations/fetchcryptogramrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.FetchCryptogramResponse](../../models/operations/fetchcryptogramresponse.md)**


## fetch_specific_saved_instrument

To get specific saved instrument for a customer id and instrument id

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.FetchSpecificSavedInstrumentRequest(
    customer_id='wiry',
    instrument_id='Turkish',
    x_client_id='perspiciatis',
    x_client_secret='sensor',
)

res = s.token_vault.fetch_specific_saved_instrument(req)

if res.fetch_all_saved_instruments is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.FetchSpecificSavedInstrumentRequest](../../models/operations/fetchspecificsavedinstrumentrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.FetchSpecificSavedInstrumentResponse](../../models/operations/fetchspecificsavedinstrumentresponse.md)**

