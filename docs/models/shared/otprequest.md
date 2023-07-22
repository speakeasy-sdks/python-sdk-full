# OTPRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `action`                                                               | [OTPRequestAction](../../models/shared/otprequestaction.md)            | :heavy_check_mark:                                                     | The action for this workflow. Could be either SUBMIT_OTP or RESEND_OTP |
| `otp`                                                                  | *str*                                                                  | :heavy_check_mark:                                                     | OTP to be submitted                                                    |