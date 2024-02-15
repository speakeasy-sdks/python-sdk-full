# Authentication
(*authentication*)

## Overview

The Authentication API allows merchants to show a native screen and capture OTP on their own page and submit to Cashfree. This feature is only available on request.

### Available Operations

* [otp_request](#otp_request) - Submit or Resend OTP

## otp_request

If you accept OTP on your own page, you can use the below API to send OTP to Cashfree.

### Example Usage

```python
import pg_latest
from pg_latest.models import operations

s = pg_latest.PGLatest()

req = operations.OTPRequestRequest(
    payment_id='<value>',
)

res = s.authentication.otp_request(req)

if res.otp_response_entity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.OTPRequestRequest](../../models/operations/otprequestrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.OTPRequestResponse](../../models/operations/otprequestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
