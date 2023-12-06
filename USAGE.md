<!-- Start SDK Example Usage [usage] -->
```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.DeleteSpecificSavedInstrumentRequest(
    customer_id='string',
    instrument_id='string',
    x_client_id='string',
    x_client_secret='string',
)

res = s.token_vault.delete_specific_saved_instrument(req)

if res.fetch_all_saved_instruments is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->