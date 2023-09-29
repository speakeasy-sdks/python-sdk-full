# OTPRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `action`                                                                         | [Optional[shared.OTPRequestAction]](undefined/models/shared/otprequestaction.md) | :heavy_check_mark:                                                               | The action for this workflow. Could be either SUBMIT_OTP or RESEND_OTP           |
| `otp`                                                                            | *Optional[str]*                                                                  | :heavy_check_mark:                                                               | OTP to be submitted                                                              |