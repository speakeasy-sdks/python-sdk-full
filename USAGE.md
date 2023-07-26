<!-- Start SDK Example Usage -->


```python
import pg_latest
from pg_latest.models import operations, shared

s = pg_latest.PGLatest()

req = operations.OTPRequestRequest(
    otp_request=shared.OTPRequest(
        action=shared.OTPRequestAction.RESEND_OTP,
        otp='provident',
    ),
    payment_id='distinctio',
    x_api_version='quibusdam',
)

res = s.authentication.otp_request(req)

if res.otp_response_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->