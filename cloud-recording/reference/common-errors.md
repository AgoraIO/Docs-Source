---
title: "Common errors"
sidebar_position: 5
type: docs
platform_selector: false
description: >
  Common error codes and status codes you may encounter when using the Cloud Recording RESTful APIs.
---

This article lists the common errors, error codes and status codes you may encounter when using the Cloud Recording RESTful APIs. If you encounter other errors, contact [Agora technical support](mailto:support@agora.io).

## Errors

### Why do I get a 404 error when I call query?

After the cloud recording enables the high availability mechanism, the fault processing center needs a certain period of time to find the cause of the failure and act accordingly.

When the service detects that the server process is killed, the fault processing center switches the service to another server within 30 seconds; when the service detects that the server is disconnected, the fault processing center tries to reconnect to that server or switch to a different server if it fails to reconnect within one minute. Before the service resumes, you get a 404 for the method call of `query`, `updateLayout`, or `stop`.

## Error codes

- `2`: Invalid parameter. Possible reasons:
	- A parameter's data type is wrong.
	- A parameter is spelt wrong. All the parameters are case sensitive.
	- A parameter value is out of range.
	- A mandatory parameter is missing.
  
- `7`: The recording is already running. Do not repeat the `start` request with the same resource ID.
- `8`: Errors in the HTTP request header fields. Possible reasons:
  - Content-type is wrong. Ensure that the `Content-type` field is `application/json;charset=utf-8`.
  - `cloud_recording` is missing in the request URL.
  - The HTTP method is wrong.
  - The request is not valid JSON
- `49`: Caused by repeated `stop` requests with the same resource ID and recording ID (sid).
- `53`: The recording is already running. This error occurs when you use the same parameters to call `acquire` again and use the new resource ID in the `start` request. To start multiple recording instances, use a different user ID for each instance.
- `62`: If you receive this error when calling `acquire`, the cloud recording service is not enabled. See [Enable Cloud Recording](../get-started/getstarted) for details.
- `65`: Usually caused by network jitter. Retry with the same resource ID. Agora recommends that you use a backoff strategy, for example, retry after 3 and 6 seconds successively.
- `109`: The authentication token for joining the <Vg k="VSDK" /> channel has expired. You need to get a new token.
- `110`: The authentication token for joining the rtc channel is wrong. You need to confirm if you have got the right one.
- `432`: The parameter in the request is incorrect. Either the parameter is invalid, or the App ID, channel name, or user ID does not match the resource ID.
- `433`: The resource ID has expired. You need to start recording within five minutes after getting a resource ID. Call acquire to get a new resource ID.
- `435`: No recorded files created. There is nothing to record because no user is sending any stream in the channel.
- `501`: The recording service is exiting. This error might occur when you call query after stop.
- `1001`: Fails to parse the resource ID. Call acquire to get a new resource ID.
- `1003`: The App ID or recording ID (sid) does not match the resource ID. Ensure that the App ID or recording ID matches the resource ID in each recording session.
- `1013`: The channel name is invalid. The string length must be less than 64 bytes. Supported character scopes are:
  - All lowercase English letters: a to z.        
  - All uppercase English letters: A to Z.
  - All numeric characters: 0 to 9.
  - The space character.
  - Punctuation characters and other symbols, including: "!", "#", "$", "%", "&", "(", ")", "+", "-", ":", ";", "\<", "=", ".", ">", "?", "@", "[", "]", "^", "_", " {", "}", "|", "~", ",".
- `1028`: Invalid parameters in the request body of the `updateLayout` method.
- `"invalid appid"`: The App ID you entered is invalid. If the error persists after you verify the App ID, contact [support@agora.io](mailto:support@agora.io).
- `"no Route matched with those values"`: A possible reason for this message is that you entered an incorrect HTTP method in your request, such as using GET when it should have been POST. Another possible reason is that you sent your request to a wrong URL.
- `"Invalid authentication credentials"`: The following list contains possible reasons for this message. If the error persists after you correct the following issues, contact [support@agora.io](mailto:support@agora.io):
  - The Customer ID or Customer Certificate you entered is incorrect.
  - The cloud recording service is not enabled. See [Enable Cloud Recording](../get-started/getstarted) for details.
  - HTTP header contains incorrect information. For example, `Basic` is missing in the `Authorization` field.
  - HTTP header contains incorrectly formatted content. For example, the capitalization is wrong or there is an unnecessary space in the `Content-type` field. The correct value is `application/json;charset=utf-8`.

## Status codes

| Code | Description                                                  |
| :--- | :----------------------------------------------------------- |
| `200`  | The request is successful.                                   |
| `201`  | The recording is already running. Do not repeat the `start` request with the same resource ID. |
| `206`  | No user in the channel sent a stream during the recording process, or some of the recorded files are uploaded to the Agora Cloud Backup instead of the third-party cloud storage, or the recording process is not over yet. |
| `400`  | The server cannot process the request due to malformed request syntax, or [the cloud recording service is not enabled](../get-started/getstarted). |
| `401`  | Unauthorized (incorrect Customer ID/Customer Secret).        |
| `404`  | The requested resource could not be found.                   |
| `500`  | Internal server error.                                       |
| `504`  | The server was acting as a gateway or proxy and did not receive a timely response from the upstream server. |

## Service status

| State                     | Description                                                  |
| :------------------------ | :----------------------------------------------------------- |
| "serviceIdle"             | The submodule is idle.                                       |
| "serviceStarted"          | The submodule has started.                                   |
| "serviceReady"            | The submodule is ready.                                      |
| "serviceInProgress"       | The submodule is running.                                    |
| "serviceCompleted"        | All subscribed contents have been uploaded to the extension service. |
| "servicePartialCompleted" | Part of the subscribed contents have been uploaded to the extension service. |
| "serviceValidationFailed" | The validation of the extension service failed. For example, `apiData` is incorrect. |
| "serviceAbnormal"         | The submodule is in an abnormal status.                      |

