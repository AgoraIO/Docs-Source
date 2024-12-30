---
title: 'Scene management '
sidebar_position: 5
type: docs
description: >
    Create a scene.
---

## Get scene path list (GET)

Call this API to get a list of scene paths in a room.

### Prototype

- Method: `GET`
- Access point: `https://api.netless.link/v5/rooms/{uuid}/scenes`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                  |
| :-------- | :-------- | :---------------- | :----------------------------------------------------------- |
| `token`   | string    | Required          | An SDK token or room token with the `writer` or `admin` role. To get an SDK token, you can:<li>Get a test-purpose SDK token from Agora Console. See [Get security credentials for your whiteboard project](../../whiteboard-sdk/get-started/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../whiteboard-sdk/develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>To get a room token, you can:<li>Call the RESTful API. See [Generate a Room Token](../../whiteboard-sdk/develop/generate-token-rest#generate-a-room-token-post).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>  |
| `region`  | string    | Required          | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li> |

### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                     |
| :-------- | :-------- | :---------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid`    | string    | Required          | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](../whiteboard-api/room-management#create-a-room-post) or calling the [RESTful API to get room information](../whiteboard-api/room-management#get-room-information-get). |

### Query parameters

You can choose to pass in the following query parameters:

| Parameter  | Data type | Required/Optional | Description                                                  |
| :--------- | :-------- | :---------------- | :----------------------------------------------------------- |
| `sceneDir` | string    | Optional          | The path to the scene directory, which starts with `/`. If you pass in this parameter, a list of the scene paths under the specified directory is generated. If you do not pass it in, a list of the scene paths under the current directory is generated. |

### Request example

```
GET /v5/rooms/faexxxxx47c/scenes?sceneDir=/test
Host: api.netless.link
region: us-sv
token: NETLESSSDK_YWs9T3YtxxxxxYjc0
Content-Type: application/json
```

### HTTP response

For details about all possible response status codes, see the [status code table](../whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**Response example**

```
"status": 200,
"body":
[
    "/test/cover",
    "/test/page1"
]
```

The response body is a JSON Array of scene path strings.

If the status code is not `200`, the request fails. The response body includes a `message` field that describes the reason for the failure.

## Add a scene (POST)

Call this API to add a scene.

### Prototype

- Method: `POST`
- Access point: `https://api.netless.link/v5/rooms/{uuid}/scenes`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------- | :-------- | :---------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token`   | string    | Required          | An SDK token or room token with the `writer` or `admin` role. To get an SDK Token, you can:<li>Get a test-purpose SDK token from Agora Console. See [Get security credentials for your whiteboard project](../../whiteboard-sdk/get-started/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../whiteboard-sdk/develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>To get a room token, you can:<li>Call the RESTful API. See [Generate a room token](../../whiteboard-sdk/develop/generate-token-rest#generate-a-room-token-post).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li> |
| `region`  | string    | Required          | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                                                                                                                                                                                                                                                                                         |

### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                   |
| :-------- | :-------- | :---------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid`    | string    | Required          | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](../whiteboard-api/room-management#create-a-room-post) or calling the [RESTful API to get room information](../whiteboard-api/room-management#get-room-information-get). |


### Request Body

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-------- | :-------- | :---------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `scenes`  | array     | Required          | An array of scenes, each containing the following parameters:<li>`name`: String. Sets the scene name. It cannot be the same as another scene in the same group and cannot contain `/`.</li><li>`ppt`: (Optional) Object. Sets the property of the background image of the scene.</li><li>`src`: String. Sets the URL of the image. Ensure that your browser can access and display the image properly; otherwise, the image may not be displayed in the scene.</li><li>`width`: Number. Sets the width of the image in pixels.</li><li>`height`: Number. Sets the height of the image in pixels.</li> |
| `path`    | string    | Required          | The path of a scene directory.If the path already exists, the new scene is added under the existing scene directory; if not, a new scene directory is created, and the new scene is added under the created directory. |


### Request example

```
POST /v5/rooms/a7e0xxxxxa69/scenes
Host: api.netless.link
region: us-sv
Content-Type: application/json
token: NETLESSSDK_YWs9QlxxxxxA0NzA5ZGM2MjRi

{
    "scenes": [
        {
            "name": "page1",
            "ppt": {
                "src": "xxxx",
                "width": 640,
                "height": 360
            }
        },
        {
            "name": "page2",
            "ppt": {
                "src": "xxxx",
                "width": 640,
                "height": 360
            }
        }
    ],
    "path": "/test"
}
```

### HTTP response

For details about all possible response status codes, see the [status code table](../whiteboard-api/overview#status-codes).

If the status code is `201`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
"status": 201,
"body":
{}
```

The response body is an empty JSON object.

If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.

## Switch to a scene (PATCH)

Call this API to switch scenes when there are multiple scenes or scene directories in the room.

### Prototype

- Method: `PATCH`
- Access point: `https://api.netless.link/v5/rooms/{uuid}/scene-state`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                  |
| :-------- | :-------- | :---------------- | :----------------------------------------------------------- |
| `token`   | string    | Required          | An SDK token or room token with the `admin` role. To get an SDK token, you can:<li>Get a test-purpose SDK token from Agora Console. See [Get security credentials for your whiteboard project](../../whiteboard-sdk/get-started/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../whiteboard-sdk/develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>To get a room token, you can:<li>Call the RESTful API. See [Generate a room token](../../whiteboard-sdk/develop/generate-token-rest#generate-a-room-token-post).</li><li>Use code samples. See [Generate a token from your app server](../../whiteboard-sdk/develop/generate-token-app-server).</li>  |
| `region`  | string    | Required          | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li> |

### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                     |
| :-------- | :-------- | :---------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid`    | string    | Required          | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](../whiteboard-api/room-management#create-a-room-post) or calling the [RESTful API to get room information](../whiteboard-api/room-management#get-room-information-get). |

### Request body

| Parameter   | Data type | Required/Optional | Description                                  |
| :---------- | :-------- | :---------------- | :------------------------------------------- |
| `scenePath` | string    | Required          | The path of the scene you want to switch to. |

### Request example

```
PATCH /v5/rooms/faexxxxx1947c/scene-state
Host: api.netless.link
region: us-sv
Content-Type: application/json
token: NETLESSSDK_YWs9TxxxxxYjc0

{
    "scenePath": "/test/page1"
}
```

### HTTP response

For details about all possible response status codes, see the [status code table](../whiteboard-api/overview#status-codes).


If the status code is `201`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
"status": 201,
"body":
{
    "currentScenePath": [
        "test",
        "page1"
    ]
}
```

**Description of parameters in the response:**

| Parameter          | Data type | Description                                                  |
| :----------------- | :-------- | :----------------------------------------------------------- |
| `currentScenePath` | array     | The path of the current scene, which is an array consisting of the scene name and the corresponding scene directory. |

If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.


