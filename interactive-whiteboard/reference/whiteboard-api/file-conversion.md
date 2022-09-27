---
title: 'File conversion'
sidebar_position: 2
type: docs
description: >
    Basic information about the Interactive Whiteboard API.
---

<Vg k="WHITE" /> can convert PPT and PPTX files into dynamic HTML web pages. The generated images and web pages can be directly accessed or presented on the whiteboard. 

Before calling the RESTful API for file conversion, ensure that you have done the following:
- You have enabled **Docs to Web** and configured storage settings in Agora Console. See [Enable server-side supporting features](../../develop/enable-whiteboard#enable-whiteboard-server-side-features)
- You have generated a URL address for the file you want to convert, and the address is publicly accessible.


## Start file conversion

Call this API to start a file-conversion task.

### Prototype

- Method: `POST`
- Access point: `https://api.netless.link/v5/projector/tasks`

### Request header

Pass in the following parameters in the request header:

| Parameter | Category | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :------- | :----- | :------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token` | string | Required | A `writer` or `admin` SDK token. You can obtain a token using one of the following methods:<li>Get an SDK token for testing purposes from <Vg k="CONSOLE" />. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Write code on your app server. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region` | string | Required | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                                                                                   |


### Request Body

The following parameters are required in the URL:

| Parameter | Category | Required/Optional | Description |
| :---------------- | :------ | :------- | :----------------------------------------------------------- |
| `resource` | string | Required | The URL of the file you want to convert. |
| `preview` | boolean | Optional | Whether to generate a preview of the generated files:<li>`true`: Generate a preview.</li><li>`false`: Do not generate a preview.</li> |
| `webhookEndpoint` | string | Optional | The address of the Webhook callback, generally the app server address, is used to receive information sent by the server, such as the progress of tasks. See <a href="#webhook-callback">Webhook callback</a >. | 
| `webhookRetry` | number | Optional | The number of retries the system attempts when the Webhook callback fails. The default value is `3`, and the maximum is `10`. |

### Request example

```
POST /v5/projector/tasks
Host: api.netless.link
region: cn-hz
Content-Type: application/json
token: NETLESSSDK_YWs9QxxxxxxMjRi

{
    "resource": "https://docs-test-xx.oss-cn-hangzhou.aliyuncs.com/xxx",
    "preview": true,
    "webhookEndpoint": "https://example.com/agoracallback",
    "webhookRetry": 1
}
```

### HTTP response

For the details of all the possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `201`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**


```
{
    "uuid": "2fd2dxxxxx367e",
    "status": "Waiting"
}
```

**Description of parameters in the response:**

| Parameter | Category | Description |
| :------- | :----- | :----------------------------------------------------------- |
| `uuid` | string | The task UUID, which is the unique identifier of the file-conversion task. |
| `status` | string | The status of the file-conversion task:<li>`Waiting`: Conversion is `waiting `to start.</li><li>`Converting`: Conversion is in progress.</li><li>`Finished`: Conversion has `finished`.</li><li>`Fail`: Conversion failed.</li> |

If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.



## Query the progress of a file-conversion task

Call this API to query the progress of a file-conversion task.

### Prototype

- Method: `GET`
- Access point: `https://api.netless.link/v5/projector/tasks/{uuid}`



### Request header

Pass in the following parameters in the request header:

| Parameter | Category | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------- | :----- | :------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token.` | string | Required | The Task token. You can obtain a token using one of the following methods:<li>Call the RESTful API. See [Generate a task token](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Write code on your app server. See [Generate a token from your app server](../../develop/generate-token-app-server).    </li>                                                   |
| `region` | string | Required | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li> |

### Request Path


The following parameters are required in the URL:

| Parameter | Category | Required/Optional | Description |
| :----- | :----- | :------- | :----------------------------------------------------------- |
| `uuid` | string | Required | The task UUID, which is the unique identifier of the file-conversion task. You can get it by calling the RESTful API to start a file conversion. |

### Request example

```
GET /v5/projector/tasks/2fxxxxxx367e
Host: api.netless.link
region: cn-hz
Content-Type: application/json
token: NETLESSSDK_YWsxxxxxM2MjRi
```

### HTTP response

For the details of all the possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
{
    "uuid": "2fdxxxx7e",
    "status": "Finished",
    "convertedPercentage": 100,
    "prefix": "https://xxxx.com/dynamicConvert"
    "pageCount": 10,
    "previews": {
      "1": "https://xxxx.xx.xx/1.png",
      "2": "https://xxxx.xx.xx/2.png",
      ...
    }
    "note": "https://xxx.xx.xx/note.json"，
    "errorCode": "20xxxxx",
    "errorMessage": "xxx",
}
```

**Description of parameters in the response:**


| Parameter | Category | Description                                                                                                                                                                                                                                                                              |
| :-------------------- | :----- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid` | string | The task UUID, which is the unique identifier of the file-conversion task.                                                                                                                                                                                                               |
| `status` | string | The status of the conversion task:<li>`Waiting`: Conversion is `waiting `to start.</li><li>`Converting`: Conversion is in progress.</li><li>`Finished`: Conversion has `finished`.</li><li>`Fail`: Conversion failed.</li>                                                               |
| `convertedPercentage` | number | The progress of the conversion expressed as a percentage.                                                                                                                                                                                                                                |
| `prefix` | string | The prefix of the address of the generated file.                                                                                                                                                                                                                                         |
| `pageCount` | number | The number of file pages. This value is not available when the conversion task fails.                                                                                                                                                                                                    |
| `previews` | object | The address of the preview. Each page corresponds to a preview address.  This parameter is only returned when `preview` is set to `true` in the <a href="#request-body">request body</a> when starting the file conversion.  This value is not available when the conversion task fails. |
| `note` | string | Notes and comments extracted from the file. This parameter contains only the pages that have notes or comments.                                                                                                                                                                          |
| `errorCode` | string | The error code. This parameter is only returned when the conversion task fails.  For the details of all the possible error codes, see <a href="#error-code">Error code</a>.                                                                                                              |
| `errorMessage` | string | The error message corresponding to the error code, describing the cause of the error. This parameter is only returned when the conversion task fails.                                                                                                                                    |



## Query to-be-converted tasks

Call this API to list all tasks that are waiting to be converted.

### Prototype



- Method: `GET`
- Access point: `https://api.netless.link/v5/projector/tasks`

### Request header

Pass in the following parameters in the request header:

| Parameter | Category | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------- | :----- | :------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token.` | string | Required | A `writer` or `admin` SDK token. You can obtain a token using one of the following methods:<li>Get an SDK token for testing purposes from <Vg k="CONSOLE" />. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Write code on your app server. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region` | string | Required | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                                                                                                                    |

### Request example

```
GET /v5/projector/tasks
Host: api.netless.link
region: cn-hz
Content-Type: application/json
token: NETLESSSDK_YWs9QxxxxxxMjRi
```

### HTTP response

For the details of all the possible response status codes, see the [status code table](./overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**



```
[
    {
      taskId: 'xxx',
      status: 1
    },
    {
       ....
    }
]
```

**Description of parameters in the response:**

| Parameter | Category | Description |
| :------- | :----- | :----------------------------------------------------------- |
| `taskId` | string | The task UUID, which is the unique identifier of the file-conversion task. |
| `status` | number | The status of the conversion task:<li>`1`: In progress. </li><li>`0`: Waiting to be converted. </li> |

If the status code is not `200`, the request fails. The response body includes a `message` field that describes the reason for the failure.



## Cancel conversion task

Call this API to cancel a specified conversion task.

### Prototype

- Method: `DELETE`
- Access point: `https://api.netless.link/v5/projector/tasks/{uuid}`

### Request header

Pass in the following parameters in the request header:

| Parameter | Category | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------- | :----- | :------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token` | string | Required | An SDK token. You can obtain a token using one of the following methods:<li>Call the RESTful API. See [Generate an SDK token](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Write code on your app server. See [Generate a token from your app server](../../develop/generate-token-app-server).</li>                                                                       |
| `region` | string | Required | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li> |



```
[
    {
      taskId: 'xxx',
      status: 1
    },
    {
       ....
    }
]
```

**Description of parameters in the response:**

| Parameter | Category | Description |
| :------- | :----- | :----------------------------------------------------------- |
| `taskId` | string | The task UUID, which is the unique identifier of the file-conversion task. |
| `status` | number | The status of the conversion task:<li>`1`: In progress. </li><li>`0`: Waiting to be converted. </li> |

If the status code is not `200`, the request fails. The response body includes a `message` field that describes the reason for the failure.


## Cancel conversion task

Call this API to cancel a specified conversion task.

### Prototype

- Method: `DELETE`
- Access point: `https://api.netless.link/v5/projector/tasks/{uuid}`

### Request header

Pass in the following parameters in the request header:

| Parameter | Category | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------- | :----- | :------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token` | string | Required | An SDK token. You can obtain a token using one of the following methods:<li>Call the RESTful API. See [Generate an SDK token](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Write code on your app server. See [Generate a token from your app server](../../develop/generate-token-app-server).</li>                                                                       |
| `region` | string | Required | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li> |

### Request Path

The following parameters are required in the URL:

| Parameter | Category | Required/Optional | Description |
| :----- | :----- | :------- | :----------------------------------------------------------- |
| `uuid` | string | Required | The task UUID, which is the unique identifier of the file-conversion task. You can get it by calling the RESTful API to start a file conversion. |

### Request example

```
DELETE /v5/projector/tasks/2fxxxxxx367e
Host: api.netless.link
region: cn-hz
Content-Type: application/json
token: NETLESSSDK_YWsxxxxxM2MjRi
```

### HTTP response

For the details of all the possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
{
  taskId: 'xxx',
  success: true
}
```

**Description of parameters in the response:**

| Parameter | Category | Description |
| :-------- | :------ | :----------------------------------------------------------- |
| `taskId` | string | The task UUID, which is the unique identifier of the file-conversion task. |
| `success` | boolean | Whether canceling the conversion task is successful: <li>`true`: Task cancellation is successful.</li><li>`false`: Task cancellation is unsuccessful.</li> |

If the status code is not `200`, the request fails. The response body includes a `message` field that describes the reason for the failure.

## Set task priority

Call this API to move the specified conversion task in the waiting list to the front or the back of the task queue.

### Prototype

- Method: `PUT`
- Access point: `https://api.netless.link/v5/projector/tasks/{uuid}`

### Request header

Pass in the following parameters in the request header:

| Parameter | Category | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :------- | :----- | :------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token` | string | Required | A `writer` or `admin` SDK token. You can obtain a token using one of the following methods::<li>Get an SDK token for testing purposes from Agora Console. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Write code on your app server. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region` | string | Required | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                                                                                                                |

### Request Body

The following parameters are required in the URL.

| Parameter | Category | Required/Optional | Description |
| :--------- | :----- | :------- | :----------------------------------------------------------- |
| `priority` | string | Required | Set task priority: <li>`highest`: Move to the front of the task queue. </li> <li>`lowest`: Move to the back of the task queue. </li> |

### Request Path

The following parameters are required in the URL:

| Parameter | Category | Required/Optional | Description |
| :----- | :----- | :------- | :----------------------------------------------------------- |
| `uuid` | string | Required | The task UUID, which is the unique identifier of the file-conversion task. You can get it by calling the RESTful API to start a file conversion. |

### Request example

```
PUT /v5/projector/tasks/2fxxxxxx367e
Host: api.netless.link
region: cn-hz
Content-Type: application/json
token: NETLESSSDK_YWs9QxxxxxxMjRi

{
    "priority": highest
}
```

### HTTP response

For the details of all the possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
{
  uuid: 'xxx',
  success: true
}
```


**Description of parameters in the response:**

| Parameter | Category | Description |
| :-------- | :------ | :----------------------------------------------------------- |
| `uuid` | string | The task UUID, which is the unique identifier of the file-conversion task. |
| `success` | boolean | Whether setting the priority is successful: <li>`true`: Setting the priority succeeded. </li><li>`false`: Setting the priority failed. </li> |

If the status code is not `200`, the request fails. The response body includes a `message` field that describes the reason for the failure.



## Webhook callback

Call this callback to receive reports on the progress and operating status of file-conversion tasks from the server.  You can call this callback by passing in the relevant parameters in the <a href="#request-body">request body</a> when launching a file-conversion task.

The Webhook callback could be repeated multiple times. To ensure that the app server processes identical responses in the same manner, you need to apply idempotent processing.

### HTTP response

For the details of all the possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
{
  code: 0 ,
  message: "success",
  data: {
      "taskId": "da4c1b9ae************92af4ef22b8",
      "taskType": "dynamic_conversion",
      "prefixUrl": "https://xxxx.com/dynamicConvert",
      "pageCount": 10,
      "previews": {
        "1": "https://xxxx.xx.xx/1.png",
        "2": "https://xxxx.xx.xx/2.png"
        ...
      },
      "note": "https://xxx.xx.xx/note.json"，
      "noticeTimestamp": 1231369699739
  }

}
```

**Description of parameters in the response:**

| Parameter                                                      | Category | Description                                                                                                                                                                                                                |
|:---------------------------------------------------------------| :----- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `code`                                                         | number | The error code. When the task succeeds, the value is `0`.  For the details of all the possible error codes, see <a href="#error-code">Error code</a>.                             |
| `message`                                                      | string | The error message corresponding to the error code, describing the cause of the error.                                                                                                                                      |
| `uuid`                                                         | string | The task UUID, which is the unique identifier of the file-conversion task.                                                                                                                                                 |
| `taskType`                                                     | string | The type of the conversion task. Currently, only `dynamic_conversion` is available.                                                                                                                                        |
| `prefixUrl`                                                    | string | The prefix of the address of the generated file.                                                                                                                                                                           |
| `pageCount`                                                    | number | The number of file pages. This parameter is not available when the conversion task fails.                                                                                                                                  |
| `previews`                                                     | object | The address of the preview. Each page corresponds to a preview address. This parameter is only returned when `preview` is set to `true` in the <a href="#request-body">request body</a> when starting the file conversion. |
| This parameter is not available when the conversion task fails.|||
| `note`                                                         | string | Notes and comments extracted from the file. This parameter contains only the pages that have notes or comments.                                                                                                            |
| `noticeTimestamp`                                              | number | The time when you receive the Webhook callback.                                                                                                                                                                            |


## Error code

The following are details and solutions for all the possible error codes that could occur when calling the file conversion RESTful API.

| Error code | Error message | Solution |
| :------ | :------------------------------------------------------ | ------------------------------------------------------------ |
| 2010201 | unsupported file format | Upload the PPT or PPTX files.  |
| 2010202 | dynamic conversion only support pptx | Upload the PPTX files.  |
| 2010203 | the number of tasks exceeds limit | Call <a href="#cancel-conversion-task">Cancel conversion task</a> to reduce the number of tasks in the queue, or wait for existing conversion tasks to complete before starting a conversion task. |
| 2010605 | task not found | Check whether the task UUID is correct.  |
| 2011201 | task timeout | Check the network connection or compress the file size.  |
| 2010606 | team not found | Check whether the token is correct.  In Agora Console, check whether the data center is correctly configured and docs-to-web is enabled.  |
| 2010607 | modify priority for running task is not allowed | Ensure that the target task is in the waiting list.  |
| 2011301 | task not found | Check whether the task UUID is correct.  |
| 2030100 | download from OSS file failed | Check whether the target file has been uploaded.  |
| 2030101 | unzip file failed, unsupported file in PPT | Check whether the file can be opened with PowerPoint.  |
| 2030102 | can't find media file from unzip PPT | Check whether the path of the media files in the PPT is correct and whether an external link is used. On the user's computer, move the PPT file to other folders and check whether the media files in the PPT file are playable.  |
| 2030200 | read xml file failed | Check whether the uploaded file is edited with software other than PowerPoint.  |
| 2030201 | formula resolve failed, please check animation of PPT | Examine or delete the animation in the PPT, and retry.  |
| 2030202 | unsupported formula type, please check animation of PPT | Examine or delete the animation in the PPT, and retry.  |
| 2040005 | task timeout | Abnormal or oversized images are used in the uploaded file; contact <a href="mailto:support@agora.io">support@agora.io</a>.  |
| 2050099 | unknown error | Check whether the uploaded file is edited with software other than PowerPoint.  |
| 2050100 | unsupported file type | Upload the PPT or PPTX files.  |
| 2050101 | file download failed | Check the network connection.  |
| 2050102 | file is empty | Open the file locally, and check whether the file is empty.  |
| 2050107 | file url encode failed | Check whether the URL address of the file is correct.  |
| 2050201 | init presentation parser failed | Check whether the uploaded file is edited with software other than PowerPoint.  |
| 2050299 | unknown parsing error | Check whether the uploaded file is edited with software other than PowerPoint.  |
| 2050401 | generate preview failed | Check whether the uploaded file is edited with software other than PowerPoint.  |
| 2060402 | fonts in the rules that are not provided | Contact <a href="mailto:support@agora.io">support@agora.io</a>.  |
| 2090304 | upload file to custom storage failed | Check whether the storage configuration is correct.  |
| 2090305 | not supported storage provider | Check whether the link to the cloud storage service provider is correct, or consider changing the service provider.  |







