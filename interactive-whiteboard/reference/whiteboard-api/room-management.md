---
title: 'Room management'
sidebar_position: 4
type: docs
description: >
    Create a live room.
---



## Create a room (POST)

Call this API to create a live room.

### Prototype

- Method: `POST`
- Access point: `https://api.netless.link/v5/rooms`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :-------- | :-------- | :---------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token`   | string    | Required          | The SDK token, which can be obtained through one of the following methods:<li>Get a test-purpose SDK token from <Vg k="CONSOLE" />. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region`  | string    | Required         | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>         |

### Request body

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                            |
| :--------- | :------ | :------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `isRecord` | boolean |  Optional      | This function is not supported yet. This parameter is `false` by defaut for `us-sv`, `sg`, `in-mum`, `eu` region.                                                                      |
| `limit` | integer | Optional | The maximum number of users with a `writer` or `admin` token who can be in the room at the same time. If you set this to `0`, there is no maximum. Agora recommends setting it to `0`. |

### Request example

```
POST /v5/rooms
Host: api.netless.link
token: NETLESSSDK_YWs9xxxxxxZGM2MjRi
region: us-sv
Content-Type: application/json

{
 "isRecord": false
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
    "uuid": "4a5xxxxx6b",
    "teamUUID": "RMxxxxx5aw",
    "appUUID": "i54xxxxx1AQ",
	"isRecord": false,
    "isBan": false,
    "createdAt": "2021-01-18T06:56:29.432Z",
    "limit": 0
}
```

**Description of parameters in the response:**

| Parameter | Data type | Description                                                                                                                                      |
| :---------- | :------ |:-------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid` | string | The room UUID, which is the unique identifier of a room.                                                                                         |
| `teamUUID` | string | The unique identifier of the <Vg k="CONSOLE" /> account that creates the whiteboard project.                                                          |
| `appUUID` | string | The unique identifier of the whiteboard project.                                                                                                 |
| `isRecord` | boolean | Whether recording is enabled for the room:<li>`true`: Enabled.</li><li>`false`: Not enabled.</li>                                                     |
| `isBan` | boolean | Whether the room is disabled:<li>`true`: Disabled.</li><li>`false`: Not disabled.</li>                                                           |
| `createdAt` | string | The UTC time when the room was created.                                                                                                          |
| `limit` | integer | The maximum number of users with a `writer` or `admin` token who can be in the room at the same time. If you set it to `0`, there is no maximum. |


If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.


## Get room information (GET)

Call this API to get information about a room.

### Prototype

- Method: GET
- Access point: `https://api.netless.link/v5/rooms/{uuid}`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :-------- | :-------- | :---------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token`   | string    | Required          | A SDK token or room token with the `writer` or `admin` role. To get a SDK token, you can:<li>Get a test-purpose SDK token from <Vg k="CONSOLE" />. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region`  | string    | Required         | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>                        |

### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description |
| :------ | :----- | :------- | :----------------------------------------------------------- |
| `uuid` | string | Required | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](#create-a-room-post) or calling the [RESTful API to get room information](#get-room-information-get). |


### Request example

```
GET /v5/rooms/a7exxxxxxa69
Host: api.netless.link
region: us-sv
Content-Type: application/json
token: NETLESSSDK_YWs9xxxxxxM2MjRi
```

### HTTP response

For details about all possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
"status": 200,
"body":
{
    "uuid": "4axxxxx96b",
    "teamUUID": "RMmxxxxx5aw",
    "appUUID": "i5xxxxx1AQ",
	"isRecord": false,
    "isBan": false,
    "createdAt": "2021-01-18T06:56:29.432Z",
    "limit": 0
}
```

**Description of parameters in the response:**


| Parameter | Data type | Description |
| :---------- | :------ | :----------------------------------------------------------- |
| `uuid` | string | The room UUID, which is the unique identifier of a room. |
| `teamUUID` | string | The unique identifier of the Agora Console account that creates the whiteboard project. |
| `appUUID` | string | The unique identifier of the whiteboard project. |
| `isRecord` | boolean | Whether recording is enabled for the room:<li>`true`: Enabled.</li><li>`false`: Not enabled.</li> |
| `isBan` | boolean | Whether the room is disabled:<li>`true`: Disabled.</li><li>`false`: Not disabled.</li> |
| `createdAt` | string | The UTC time when the room was created. |
| `limit` | integer | The maximum number of users with a `writer` or `admin` token who can be in the room at the same time. If you set it to 0, there is no maximum. |


If the status code is not `200`, the request fails. The response body includes a `message` field that describes the reason for the failure.

## Get a room list (GET)

Call this API to get a list of rooms.

### Prototype

- Method: `GET`
- Access point: `https://api.netless.link/v5/rooms`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :-------- | :-------- | :---------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `token`   | string    | Required          | A SDK token or room token with the `writer` or `admin` role. To get a SDK token, you can:<li>Get a test-purpose SDK token from <Vg k="CONSOLE" />. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region`  | string    | Required          | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li>           |

### Query parameters

You can choose to pass in the following query parameters:

| Parameter | Data type | Required/Optional | Description |
| :---------- | :------ | :------- | :----------------------------------------------------------- |
| `beginUUID` | string | Optional | The UUID of the room you want to start querying from. |
| `limit` | integer | Optional | The maximum number of rooms on the list. The range is (0,1000]. If you do not set this parameter, the default maximum is 100 rooms. |

### Request example

```
GET /v5/rooms/?beginUUID=0e6exxxxxx4d95&limit=2
Host: api.netless.link
region: us-sv
Content-Type: application/json
token: NETLESSSDK_YWs9QlxxxxxxM2MjRi
```

### HTTP response

For details about all possible response status codes, see the [status code table](../../reference/whiteboard-api/overview#status-codes).

If the status code is `200`, the request is successful. The response returns the status code and corresponding parameters.

**The following is a response example for a successful request:**

```
"status": 200,
"body":
[
    {
        "uuid": "0e6exxxxxxd95",
        "teamUUID": "RMmxxxxxxaw",
        "appUUID": "vVxxxxzJF-A",
	    "isRecord": false,
        "isBan": false,
        "createdAt": "2020-12-20T14:02:54.846Z",
        "limit": 0
    },
    {
        "uuid": "1d4xxxxxxca69",
        "teamUUID": "RMmxxxxxx5aw",
        "appUUID": "vVsxxxxzJF-A",
	    "isRecord": false,
        "isBan": false,
        "createdAt": "2020-12-20T14:10:29.265Z",
        "limit": 0
    }
]
```

**Description of parameters in the response:**

| Parameter | Data type | Description |
| :---------- | :------ | :----------------------------------------------------------- |
| `uuid` | string | The room UUID, which is the unique identifier of a room. |
| `teamUUID` | string | The unique identifier of the <Vg k="CONSOLE" /> account that creates the whiteboard project. |
| `appUUID` | string | The unique identifier of the whiteboard project. |
| `isRecord` | boolean | Whether recording is enabled for the room:<li> `true`: Enabled.</li> <li>`false`: Not enabled.</li> |
| `isBan` | boolean | Whether the room is disabled:<li>`true`: Disabled.</li><li>`false`: Not disabled.</li> |
| `createdAt` | string | The UTC time when the room was created. |
| `limit` | integer | The maximum number of users with a `writer` or `admin` token who can be in the room at the same time.. If you set it to 0, there is no maximum.`` |

If the status code is not 200, the request fails. The response body includes a message field that describes the reason for the failure.``

## Disable a room (PATCH)

Refer to the following information to disable or cancel disabling a room.

Note that when you disable a room, the users in the room will be removed and no users will be able to join the room.

If you want to cancel disabling the room, call the RESTful API again and set `isBan` to `false`.

### Prototype

- Method: `PATCH`
- Access point: `https://api.netless.link/v5/rooms/{uuid}`

### Request header

Pass in the following parameters in the request header:

| Parameter | Data type | Required/Optional | Description                                                  |
| :-------- | :-------- | :---------------- | :----------------------------------------------------------- |
| `token`   | string    | Required          | A SDK token or room token with the `admin` role. To get a SDK token, you can:<li>Get a test-purpose SDK token from <Vg k="CONSOLE" />. See [Get security credentials for your whiteboard project](../../develop/enable-whiteboard#get-security-credentials-for-your-whiteboard-project).</li><li>Call the RESTful API. See [Generate an SDK token](../../develop/generate-token-rest).</li><li>Use code samples. See [Generate a token from your app server](../../develop/generate-token-app-server).</li> |
| `region`  | string    | Required         | Specifies a data center to process the request: <li>`us-sv`: Silicon Valley, US, which provides services to North America and South America.</li><li>`sg`: Singapore, which provides services to Singapore, East Asia, and Southeast Asia.</li><li>`in-mum`: Mumbai, India, which provides services to India.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`eu`: Frankfurt, Europe, which provides services to Europe.</li><li>`cn-hz`: Hangzhou, China, which provides services to the areas not covered by other data centers.</li> |


### Request path

The following parameters are required in the URL:

| Parameter | Data type | Required/Optional | Description |
| :----- | :----- | :------- | :----------------------------------------------------------- |
| `uuid` | string | Required | The room UUID, which is the unique identifier of a room. You can get it by calling the [RESTful API to create a room](#create-a-room-post) or calling the [RESTful API to get room information](#get-room-information-get). |

### Request body

| Parameter | Data type | Required/Optional | Description |
| :------ | :------ | :------- | :----------------------------------------------------------- |
| `isBan` | boolean | Required | Whether the room is disabled:<li>`true`: Disabled.</li> <li>`false`: (Default) Not disabled.</li> |

### Request example

```
PATCH /v5/rooms/0e6exxxxxx4d95
Host: api.netless.link
region: us-sv
Content-Type: application/json
token: NETLESSSDK_YWs9xxxxxx5ZGM2MjRi

{
  "isBan": true
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
    "uuid": "0e6xxxxxx95",
    "teamUUID": "RMxxxxxaw",
    "appUUID": "vVxxxxxJF-A",
	"isRecord": false,
    "isBan": true,
    "createdAt": "2020-12-20T14:02:54.846Z",
    "limit": 0
}
```

**Description of parameters in the response:**

| Parameter | Data type | Description |
| :---------- | :------ | :----------------------------------------------------------- |
| Parameter | Data type | Description |
| `uuid` | string | The room UUID, which is the unique identifier of a room. |
| `teamUUID` | string | The unique identifier of the <Vg k="CONSOLE" /> account that creates the whiteboard project. |
| `appUUID` | string | The unique identifier of the whiteboard project. |
| `isRecord` | boolean | Whether recording is enabled for the room:<li> `true`: Enabled.</li><li>`false`: Not enabled.</li> |
| `isBan` | boolean | Whether the room is disabled:<li>`true`: Disabled.</li><li>`false`: Not disabled.</li> |
| `createdAt` | string | The UTC time when the room was created. |
| `limit` | integer | The maximum number of users with a `writer` or `admin` token who can be in the room at the same time. If you set it to `0`, there is no maximum. |

If the status code is not `201`, the request fails. The response body includes a `message` field that describes the reason for the failure.

