<!-- Start SDK Example Usage -->


```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.OTPRequestRequest(
    otp_request=shared.OTPRequest(
        action=shared.OTPRequestAction.SUBMIT_OTP,
        otp='1080p',
    ),
    payment_id='whey',
)

res = s.authentication.otp_request(req)

if res.otp_response_entity is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->