---
title: 'Screenshots'
sidebar_position: 6
type: docs
description: >
    Create a scene.
---

The screenshot-management feature is implemented by <Vg k="WHITE" />. You can take screenshots for a single scene or a scene directory, generate images in PNG format, and upload them to a third-party cloud storage space.

Before calling the RESTful API for screen management, ensure that:

- You have created a third-party cloud storage account and a storage space under that account. Agora supports only [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/?nc1=h_ls) now.
- You have enabled the screenshot feature and configured storage settings in Agora Console. See [Enable whitebaord server-side features](../../whiteboard-sdk/get-started/enable-whiteboard#enable-whiteboard-server-side-features).

## Screenshot a scene (POST)

Call this API to take screenshots for a single scene.

### Prototype

- Method: `POST`
- Access point: `https://api.netless.link/v5/rooms/{uuid}/screenshots`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :-------- | :-------- | :---------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token`   | string    | Required          | An SDK token or room token with the `writer` or `admin` role. To get an SDK token, you can:<li>Get a test-purpose SDK token from Agora Console. See [Get security credentials for your whiteboard project](../../whiteboard-sdk/get-started/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate a room token](../../whiteboard-sdk/develop/generate-token-rest#generate-a-room-token-post).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>To get a room token, you can:<li>Call the RESTful API. See [Generate a room token](../../whiteboard-sdk/develop/generate-token-rest#generate-a-room-token-post).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li> |
| `region`  | string    | Required          | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                                                                                                                                                                                                                                                                                                                    |

### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                   |
| :----- | :----- | :------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid` | string | Required | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](../whiteboard-api/room-management#create-a-room-post) or calling the [RESTful API to get room information](../whiteboard-api/room-management#get-room-information-get). |

### Request body

| Parameter | Data type | Required/Optional | Description |
| :------- | :----- | :------- | :----------------------------------------------------------- |
| `width` | number | Required | The width of the screenshot in pixels. |
| `height` | number | Required | The height of the screenshot in pixels. |
| `path` | string | Optional | The path to the scene, which starts with `/`. If you do not set this parameter, the default path `/init` is used. |

### Request example

```
POST /v5/rooms/a7e04xxxxx7d1eca69/screenshots
Host: api.netless.link
region: us-sv
Content-Type: application/json
token: NETLESSSDK_YWs9xxxxxxzA5ZGM2MjRi
 
{
    "width": 640,
    "height": 480
}
```

### HTTP response

For details about all possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `201`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
"status": 201,
"body":
{
    "url": "https://white-cover.oss-cn-hangzhou.aliyuncs.com/room_cover/2811/a7exxxxca69undefined.png",
    "key": "room_cover/2811/a7exxxxxca69undefined.png",
    "bucket": "white-cover",
    "region": "oss-cn-hangzhou"
}
```

**Description of parameters in the response:**

| Parameter | Data type | Description |
| :------- | :----- | :--------------------------- |
| `url` | string | The URL of the screenshot. |
| `key` | string | The filename of the screenshot in the storage space. |
| `bucket` | string | The name of the storage space where the screenshot is saved. |
| `region` | string | The region where the storage space is located. |

If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.

## Screenshot a scene directory (POST)

Call this API to take screenshots for a scene directory.

### Prototype

- Method: `POST`
- Access point: `https://api.netless.link/v5/rooms/{uuid}/screenshot-list`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------- | :-------- | :---------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token`   | string    | Required          | An SDK token or room token with the `writer` or `admin` role. To get an SDK token, you can:<li>Get a test-purpose SDK token from Agora Console. See [Get security credentials for your whiteboard project](../../whiteboard-sdk/get-started/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../whiteboard-sdk/develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>To get a room token, you can:<li>Call the RESTful API. See [Generate a room token](../../whiteboard-sdk/develop/generate-token-rest#generate-a-room-token-post).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li> |
| `region`  | string    | Required          | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                                                                                                                                                                                                                                                                                         |

### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                   |
| :----- | :----- | :------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid` | string | Required | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](../whiteboard-api/room-management#create-a-room-post) or calling the [RESTful API to get room information](../whiteboard-api/room-management#get-room-information-get). |

#### Request body

| Parameter | Data type | Required/Optional | Description |
| :------- | :----- | :------- | :----------------------------------------------------------- |
| `width` | number | Required | The width of the screenshot in pixels. |
| `height` | number | Required | The height of the screenshot in pixels. |
| `path` | string | Required | The path to the scene directory, which starts with `/`. If you do not set this parameter , the current scene directory is used. |

#### Request example

```
POST /v5/rooms/faed3130727911ebaea37759ee91947c/screenshot-list
Host: api.netless.link
region: us-sv
token: NETLESSSDK_YWsxxxxxxYjc0
Content-Type: application/json
 
{
    "width": 640,
    "height": 480,
    "path": "/test"
}
```

#### HTTP response

For details about all possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `201`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
"status": 201,
"body":
[
    {
        "url": "https://docs-test-xxx.oss-cn-hangzhou.aliyuncs.com/room_cover/2811/faxxxxx47c/test/cover.png",
        "key": "room_cover/2811/faxxxxx47c/test/cover.png",
        "bucket": "docs-test-xxx",
        "region": "oss-cn-hangzhou"
    },
    {
        "url": "https://docs-test-xxx.oss-cn-hangzhou.aliyuncs.com/room_cover/2811/faxxxxx47c/test/page1.png",
        "key": "room_cover/2811/faxxxxx47c/test/page1.png",
        "bucket": "docs-test-xxx",
        "region": "oss-cn-hangzhou"
    }
]
```

The response body is an array of the screenshot information for each scene. Every member in the array contains the following parameters:

| Parameter | Data type | Description |
| :------- | :----- | :--------------------------- |
| `url` | string | The URL of the screenshot. |
| `key` | string | The filename of the screenshot in the storage space. |
| `bucket` | string | The name of the storage space where the screenshot is saved. |
| `region` | string | The region where the storage space is located. |

If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.

