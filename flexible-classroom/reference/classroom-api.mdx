---
title: 'Classroom REST API'
sidebar_position: 4
type: docs
description: >
    This page provides the API reference for the Agora Classroom REST API
---


export const toc = [{}];

This page provides detailed help for the Flexible Classroom RESTful APIs.

## Basic information

### Server

All requests are sent to the host: api.agora.io.

### Data format

The Content-Type of all requests is application/json.

### Authentication

Flexible Classroom Cloud Service uses tokens for authentication. You need to put the following information to the `x-agora-token` and `x-agora-uid` fields when sending your HTTP request:

- The <Vg k="SIG"/> token generated at your server.
- The uid you use to generate the <Vg k="SIG"/> token.

For details, see [Generate an RTM Token](/signaling/develop/authentication-workflow).

## Create a classroom

#### Description

Call this method to create a classroom. After it is created, the classroom is reserved for five days.

#### Prototype

- Method: POST
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUuid}

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter  | Type   | Description                                                  |
| :--------- | :----- | :----------------------------------------------------------- |
| `region`   | String | (Required) The region for connection. Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId`    | String | (Required) Agora App ID.                                     |
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins an RTC or RTM channel. The string length must be less than 64 bytes. The following characters are supported:<ul><li>All lowercase English letters: a to z.</li><li>All uppercase English letters: A to Z.</li><li>The numbers 0 to 9.</li><li>The space character.</li><li>The following special characters: "!", "#", "$", "%", "&", "(", ")", "+", "-", ":", ";", "\<", "=", ".", ">", "?", "@", "[", "]", "^", "_",  "\{", "\}",  "\|",  "~", ","</li></ul> |

**Request body parameters**

Pass in the following parameters in the request body:

| Parameter                                     | Type    | Description                                                  |
| :-------------------------------------------- | :------ | :----------------------------------------------------------- |
| `roomType`                                    | String  | (Required) The type of the classroom. You can set the value to : <ul><li>`0`: One-to-one classroom.</li><li>`2`: Lecture hall. </li><li>`4`: Small classroom. </li></ul>Once set, this parameter value cannot be changed. |
| `roomName`                                    | String  | (Required) The name of the classroom.                        |
| `roomProperties`                              | Object  | (Optional) The properties of the classroom.                  |
| `roomProperties.schedule`                     | Object  | (Optional) The schedule of the classroom.                    |
| `roomProperties.schedule.startTime`           | Integer | (Optional) The start time of the class. Once set, this parameter value cannot be changed. |
| `roomProperties.schedule.duration`            | Integer | (Optional) The duration of the class.                        |
| `roomProperties.schedule.closeDelay`          | Integer | (Optional) The delay of the class end time.                  |
| `roomProperties.processes`                    | Object  | (Optional) The process of inviting students to go "on the stage". |
| `roomProperties.processes.handsUp`            | Object  | (Optional) The settings of "on the stage".                   |
| `roomProperties.processes.handsUp.maxAccept`  | Integer | (Optional) The maximum number of students "on the stage".    |
| `roomProperties.hostingScene`                 | Object  | (Optional) The unique classroom properties of a vocational lecture hall. |
| `roomProperties.hostingScene.videoURL`        | String  | (Optional) The teacher's CDN stream URL (main video URL).    |
| `roomProperties.hostingScene.reserveVideoURL` | String  | (Optional) The teacher's CDN stream URL (backup video URL).  |
| `roomProperties.hostingScene.finishType`      | Integer | (Optional) The way the class ends.<li>`0`: The class automatically ends when the recording finishes playing.</li><li>`1`: The class ends when the teacher clicks the End Class button; this also stops the recording playback.</li> |

#### Request example

```json
{
"roomName": "jasoncai61734",
"roomType": 4,
"roomProperties": {
"schedule": {
"startTime": 1655452800000,
"duration": 600,
"closeDelay": 300
},
"processes": {
"handsUp": {
"maxAccept": 10
}
}
}
}
```

#### Response parameters

| Parameter | Type    | Description                                                  |
| :-------- | :------ | :----------------------------------------------------------- |
| `code`    | Integer | Request status code:<ul><li>0: The request succeeds.</li><li>Non-zero: The request fails.</li></ul> |
| `msg`     | String  | Detailed information about the code.                         |
| `ts`      | Number  | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
"msg": "Success",
"code": 0,
"ts": 1610167740309
}
```



## Kick a user out of a classroom

#### Description

Call this method to kick a specified user out of a classroom. After a successful method call, the server triggers an event indicating a user leaves the classroom. You can use the `dirty` parameter to determine whether the user can enter the classroom afterwards.

#### Prototype

- Method: POST
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/users/\{userUuid}/exit

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |
| `userUuid` | String | (Required) The user ID. This is the unique identifier of the user and also the user ID used when logging in to <Vg k="SIG"/>. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |


**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :------ | :----- | :----------------------------------------------------------- |
| `dirty` | Object | (Optional) The user privilege:<ul><li>`state`: Boolean, whether the user is dirty:<ul><li>`1`: Dirty. A dirty user cannot enter the classroom.</li><li>`0`: Not dirty.</li></ul></li><li>`duration`: Number, the duration of the dirty state (seconds), starting from the time when the user is kicked out of the classroom.</li></ul> |

#### Request example

**Request URL**

```html
https://api.agora.io/edu/apps/{your_app_Id}/v2/rooms/test_class/users/123/exit
```

**Request Body**

```json
{
    "dirty": {
        "state": 1,
        "duration": 600
    }
}
```

#### Response parameters


| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example


```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Set the classroom state

#### Description

Call this method to set the classroom state: Not started, Started, Ended.

#### Prototype

- Method: PUT
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/states/\{state}


#### Request parameters

**URL parameters**

Pass the following parameter in the URL.

| Parameter | Type | Description |
| :--------- | :------ | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID. |
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z</li><li>All uppercase English letters: A to Z</li><li>All numeric characters: 0-9</li><li>The space character</li><li>"!", 1"#", "$", "%", "&", "(", ")", "+", "-", ":", ";", "\<", "=", ".", ">", "?", "@", "[", "]", "^", "_", "\{", "\}", "\|", "~", ","</li> |
| `state` | Integer | (Required) The classroom state:<li>`0`: Not started.</li><li>`1`: Started.</li><li>`2`: Ended.</li><li>`3`: The room is closed and users can no longer join the room.</li> |

#### Request example

```html
https://api.agora.io/edu/apps/{yourappId}/v2/rooms/test_class/states/1
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :------------------------------------------------ |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
"status": 200,
"body":
{
  "code": 0,
  "msg": "Success",
  "ts": 1610450153520
}
```

## Set the recording state

#### Description

Call this method to start or stop recording a specified classroom.

#### Prototype

- Method: PUT
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/records/states/\{state}

#### Request parameters

**URL parameters**

Pass the following parameter in the URL.

| Parameter | Type | Description |
| :--------- | :------ | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |
| `state` | Integer | (Required) The recording state:<li>`0`: Stop recoding.</li><li>`1`: Started.</li> |



**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :---------------- | :----- | :----------------------------------------------------------- |
| `mode` | String | (Optional) The recording mode:<li>Set this parameter as `web` to enable web page recording mode.  The format of recorded files is MP4. When the length of the recorded file reaches around two hours, or when the size of the file exceeds around 2 GB, the recording service automatically creates another MP4 file.</li><li>If you do not set this parameter, Flexible Classroom records the audio and video of the teachers in composite recording mode by default.  The format of recorded files is M3U8 and TS.</li> |
| `webRecordConfig` | Object | (Optional) When the `mode` is set as `web`, you need to set the detailed configuration of the web page recording through `webRecordConfig`, including the following fields:<ul><li>`url`: (Required) String, the address of the web page to record. If you want to record a certain flexible classroom, you need to pass in the parameters required for launching a classroom in the URL. The Agora Cloud Recording service can join the specified classroom as an "invisible user" for recording. See the URL example in the request example. The following parameters are required in the URL:<ul><li>`userUuid`: The user ID used by the Agora Cloud Recording service. Please ensure that the user ID used by the Agora Cloud Recording service is not the same as that of existing users in the classroom, otherwise, the Agora Cloud Recording service will fail to join the classroom.</li><li>`roomUuid`: The ID of the classroom to be recorded.</li><li>`roomType`: The type of the classroom to be recorded.</li><li>`roleType`: The role of the Agora Cloud Recording service in the classroom to be recorded. Set this parameter as 0.</li><li>`pretest`: Whether to enable the pre-class test. Set this parameter as `false`.</li><li>`rtmToken`: The <Vg k="SIG"/> token used by the Agora Cloud Recording service.</li><li>`language`: The language of the user interface. Set this parameter as `zh` or `en`.</li><li>`appId`: Your Agora App ID.</li></ul></li><li>`rootUrl`: (Required) String, the root address of the web page to be recorded. During the recording, Agora Edu Cloud Service automatically gets the full address of the web page to be recorded by putting `rootUrl`, `roomUuid`, `roomType`,and other parameters together. If you set both `url` and `rootUrl`, `url` overrides `rootUrl`.</li><li>`onhold`: (Required) Boolean. You can set this parameter as:<ul><li>`true`: Pauses recording immediately after the web page recording task is enabled. The recording service opens and renders the web page to be recorded, but does not generate a slice file.</li><li>`false`: (Default) Enables the web page recording task and starts recording.</li></ul></li><li>`videoBitrate`: (Optional) Number. The bitrate of the video (Kbps). The value range is [50, 8000]. The default value of `videoBitrate` varies according to the resolution of the output video:<ul><li>If the resolution of the output video is less than 1280 × 720, the default value of `videoBitrate` is 1500. </li><li>If the resolution of the output video is greater than or equal to 1280 × 720, the default value of `videoBitrate` is 2000.</li></ul></li><li>`videoFps`: (Optional) Number. The frame rate of the video (fps). The value range is [5, 60]. The default value is 15.</li><li>`audioProfile`: (Optional) Number. The sample rate, encoding mode, number of audio channels, and bitrate.<ul><li>0: (Default) Sample rate of 48 kHz, music encoding, mono, and a bitrate of up to 48 Kbps.</li><li>1: Sample rate of 48 kHz, music encoding, mono, and a bitrate of up to 128 Kbps.</li><li>2: Sample rate of 48 kHz, music encoding, stereo, and a bitrate of up to 192 Kbps.</li></ul></li><li>`videoWidth`: Number. The width of the video (pixels). The value range is [480, 1280]. The default value is 1280. The product of `videoWidth` and `videoHeight` should not exceed 921,600 (1280 × 720).</li><li>`videoHeight`: Number. The height of the video (pixels). The value range is [480, 1280]. The default value is 720. The product of `videoWidth` and `videoHeight` should not exceed 921,600 (1280 × 720).</li><li>`maxRecordingHour`: Number, the maximum recording length (hours). The value range is [1,720]. If you set the class duration, Agora Edu Cloud Service gets the maximum recording length by rounding up the class duration. For example, if the class duration is 1800 seconds, `maxRecordingHour` is one hour. If you do not set the class duration, the default value of `maxRecordingHour` is two hours. If the limit set by `maxRecordingHour` is exceeded, the recording stops automatically.</li></ul> |
| `retryTimeout` | Number | The amount of time (seconds) that the Flexible Classroom cloud service waits between tries. The Flexible Classroom cloud service reties twice at most. |

#### Request example

**Request URL**

```html
https://api.agora.io/edu/apps/{yourappId}/v2/rooms/test_class/records/states/1
```

**Request Body**

```json
{
    "mode": "web",
    "webRecordConfig": {
        "url":"https://webdemo.agora.io/xxxxx/?userUuid={recorder_id}&roomUuid={room_id_to_be_recorded}&roleType=0&roomType=4&pretest=false&rtmToken={recorder_token}&language=en&appId={your_app_id}",
        "rootUrl":"https://xxx.yyy.zzz"
    },
    "retryTimeout": 60
}
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :------------------------------------------------ |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
"status": 200,
"body":
{
    "code": 0,
    "ts": 1610450153520
}
```



## Update the recording configurations

#### Description

Call this method during the recording to update the recording configurations. Every time this method is called, the previous configurations are overwritten.

#### Prototype

- Method: PUT
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/records/states/\{state}

#### Request parameters

**URL parameters**

Pass the following parameter in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID. |
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |

**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :---------------- | :----- | :----------------------------------------------------------- |
| `webRecordConfig` | Object | (Optional) Recording configurations:<ul><li>`onhold`: (Required) Boolean. You can set this parameter as:<ul><li>`true`: Pauses the web page recording. The recording service no longer generates any slice file.</li><li>`false`: (Default) Continues the web page recording. After the recording is paused, you can call this method and set the `onhold` parameter as `false` to continue the web page recording.</li></ul></li></ul> |

#### Request example

**Request URL**

```html
https://api.agora.io/edu/apps/{yourappId}/v2/rooms/test_class/records/states/1
```

**Request Body**

```json
{
    "webRecordConfig": {
        "onhold": false
    }
}
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
"status": 200,
"body":
{
    "code": 0,
    "ts": 1610450153520
}
```

## Get the recording list

#### Description

Get the recording list in a specified classroom.

You can fetch data in batches with the `nextId` parameter. You can get up to 100 pieces of data for each batch.

#### Prototype

- Method: GET
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/records

#### Request parameters

**URL parameters**

Pass the following parameter in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |

**Query parameters**

| Parameter | Type | Description |
| :------- | :----- | :----------------------------------------------------------- |
| `nextId` | String | (Optional) The starting ID of the next batch of data. When you call this method to get the data for the first time, leave this parameter empty or set it as null. Afterward, you can set this parameter as the `nextId` that you get in the response of the previous method call. |

#### Request example

Example one:

```html
https://api.agora.io/edu/apps/{yourappId}/v2/rooms/test_class/records?null
```

Example two:

```html
https://api.agora.io/edu/apps/{yourappId}/v2/rooms/test_class/records?nextId=xxx
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :----------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |
| `data` | Object | Include the following parameters:<ul><li>`count`: Integer, the number of pieces of data in this batch.</li><li>`list`: JSONArray. An array of the recording list. A JSON object includes the following parameters:<ul><li>`appId`: Your Agora App ID.</li><li>`roomUuid`: The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel.</li><li>`recordId`: The unique identifier of a recording session. A recording session starts when you call a method to start recording and ends when you call this method to stop recording.</li><li>`startTime`: The UTC timestamp when a recording session starts, in milliseconds.</li><li>`endTime`: The UTC timestamp when a recording session ends, in milliseconds.</li><li>`resourceId`: The `resourceId` of the Agora Cloud Recording service.</li><li>`sid`: The `sid` of the Agora Cloud Recording service.</li><li>`recordUid`: The UID used by the Agora Cloud Recording service in the channel.</li><li>`boardAppId`: The App Identifier of the Agora Interactive Whiteboard service.</li><li>` boardToken`: The SDK Token of the Agora Interactive Whiteboard service.</li><li>`boardId`: The unique identifier of a whiteboard session.</li><li>`type`: Integer, the recording type:<ul><li>`1`: Individual Recording</li><li>`2`: Composite Recording</li></ul></li><li>`status`: Integer, the recording state:<ul><li>`1`: In recording.</li><li>`2`: Recording has ended.</li></ul></li><li>`url`: String, the URL address of the recorded files in composite recording mode.</li><li>`recordDetails`: JSONArray. The JSON object contains the following fields:<ul><li>`url`: String, the URL address of the recorded files in web page recording mode.</li></ul></li><li>`nextId`: String, the starting ID of the next batch of data. If it is null, there is no next batch of data. If it is not null, use this `nextId` to continue the query until null is reported.</li><li>`total`: Integer, the total number of pieces of data.</li></ul></li></ul> |

#### Response example

```json
"status": 200,
"body":
{
    "code": 0,
    "msg": "Success",
    "ts": 1610450153520,
    "data": {
      "total": 17,
      "list": [
          {
            "recordId": "xxxxxx",
            "appId": "xxxxxx",
            "roomUuid": "jason0",
            "startTime": 1602648426497,
            "endTime": 1602648430262,
            "resourceId": "xxxxxx",
            "sid": "xxxxxx",
            "recordUid": "xxxxxx",
            "boardId": "xxxxxx",
            "boardToken": "xxxxxx",
            "type": 2,
            "status": 2,
            "url": "scenario/recording/xxxxxx/xxxxxx/xxxxxx.m3u8",
            "recordDetails":[
                {
                    "url":"xxxx/xxxx.mp4"
                }
            ]
          },
          {...},
      ],
      "count": 17
    }
}
```

## Query a specified event

#### Description

Query a specified type of event in a specified classroom.

You can fetch data in batches with the `nextId` parameter. You can get up to 100 pieces of data for each batch.

<div class="note info"><li>You can query the same event repeatedly.</li><li> You cannot query events in a destroyed classroom. A classroom is destroyed automatically one hour after it is ended.</li></div>

#### Prototype

- Method: GET
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/sequences

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |



**Query parameters**

| Parameter | Type | Description |
| :------- | :------ | :----------------------------------------------------------- |
| `nextId` | String | (Optional) The starting ID of the next batch of data. When you call this method to get the data for the first time, leave this parameter empty or set it as null. Afterward, you can set this parameter as the `nextId` that you get in the response of the previous method call. |
| `cmd` | Integer | (Optional) Event type. For details, see [Flexible Classroom Cloud Service Events](../reference/classroom-api#events). |

#### Request example

**Request URL**



Example one:

```html
https://api.agora.io/edu/apps/\{appId}/v2/rooms/test_class/sequences?null&cmd=1
```

Example two:

```html
https://api.agora.io/edu/apps/\{appId}/v2/rooms/test_class/sequences?nextId=50&cmd=1
```

#### Response parameters


| Parameter | Type | Description |
| :----- | :------ | :----------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |
| `data` | Object | Include the following parameters:<ul><li>`total`: Integer, the total number of pieces of data.</li><li>`count`: Integer, the number of pieces of data in this batch.</li><li>`list`: JSONArray. An array of the recording list. A JSON object includes the following parameters:<ul><li>`roomUuid`: String, the classroom ID.</li><li>`cmd`: Integer, the event type. For details, see [Flexible Classroom Cloud Service Events](../reference/classroom-api#events).</li><li>`sequence`: Integer. The event ID. This is the unique identifier of an event, which is automatically generated to ensure the order of events.</li><li>`version`: Integer, the service version.</li><li>`data`: Object, the detailed data of the event. The data varies depending on the event type. For details, see [Flexible Classroom Cloud Service Events](../reference/classroom-api#events).</li></ul></li> <li>`nextId`: String, the starting ID of the next batch of data. If it is null, there is no next batch of data. If it is not null, use this `nextId` to continue the query until null is reported.</li></ul> |

#### Response example

```json
{
    "msg":"Success",
    "code":0,
    "ts":1610433913533,
    "data":{
        "total":1,
        "list":[
            {
                "roomUuid": "",
                "cmd": 20,
                "sequence": 1,
                "version": 1,
                "data":{}
            }
        ],
        "nextId": null,
        "count":1
    }
}
```

## Get classroom events

#### Description

Get all events in the classrooms associated with a specified App ID.

You can call this method at regular intervals to listen for all the events that occur in the flexible classrooms.

<div class="alert note"><li>Each event can only be obtained once.</li><li>Note: You cannot get events one hour after a classroom is destroyed.</li></div>


#### Prototype

- Method: GET
- Endpoint: /\{region}/edu/polling/apps/\{appId}/v2/rooms/sequences

#### Request parameters

**URL parameters**

Pass the following parameter in the URL.

| Parameter | Type | Description |
| :------ | :----- | :--------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|



#### Request example

```html
https://api.agora.io/edu/polling/apps/{yourappId}/v2/rooms/sequences
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :----------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |
| `data` | Object | Include the following parameters:<li>`roomUuid`: String, the classroom ID.</li><li>`cmd`: Integer, the event type. For details, see [Flexible Classroom Cloud Service Events](../reference/classroom-api#events).</li><li>`sequence`: Integer. The event ID. This is the unique identifier of an event, which is automatically generated to ensure the order of events.</li><li>`version`: Integer, the service version.</li><li>`data`: Object, the detailed data of the event. The data varies depending on the event type. For details, see [Flexible Classroom Cloud Service Events](../reference/classroom-api#events).</li> |



#### Response example

```json
"status": 200,
"body":
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309,
    "data":[
        {
            "roomUuid": "xxxxxx",
            "cmd": 20,
            "sequence": 1,
            "version": 1,
            "data":{}
        }
    ]
}
```

## Update custom classroom properties

#### Description

Add or update the custom properties of a specified classroom. 

#### Prototype

- Method: PUT
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/properties

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |


**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :----------- | :----- | :--------- |
| `properties` | Object | Classroom properties. |
| `cause` | Object | The update reason. |

#### Request example

**Request Body**

```json
{
    "properties" :{
        "key1":"value1",
        "key2":"value2"
    },
    "cause":{}
}
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Delete custom classroom properties

#### Description

Delete the custom properties of a specified classroom. 

#### Prototype

- Method: DELETE
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/properties

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |

**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :----------- | :---------- | :--------- |
| `properties` | String array | Classroom properties. |
| `cause` | Object | Reason for deletion. |



#### Request example

**Request Body**

```json
{
    "properties" :[
        "key1",
        "key2"
    ],
    "cause":{}
}
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Update custom user properties

#### Description

Add or update the custom properties of a specified user.

#### Prototype

- Method: PUT
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/users/\{userUuid}/properties

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |
| `userUuid` | String | (Required) The user ID. This is the unique identifier of the user and also the user ID used when logging in to <Vg k="SIG"/>. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |



**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :----------- | :----- | :--------- |
| `properties` | Object | The user properties. |
| `cause` | Object | The update reason. |

#### Request example

**Request Body**

```json
{
    "properties" :{
        "key1":"value1",
        "key2":"value2"
    },
    "cause":{}
}
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Delete custom user properties

#### Description

Delete the custom properties of a specified user. 

#### Prototype

- Method: DELETE
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/users/\{userUuid}/properties

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :--------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |
| `userUuid` | String | (Required) The user ID. This is the unique identifier of the user and also the user ID used when logging in to <Vg k="SIG"/>. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |

**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :----------- | :---------- | :--------- |
| `properties` | String array | The user properties. |
| `cause` | Object | Reason for deletion. |

#### Request example

**Request Body**

```json
{
    "properties" :[
        "key1",
        "key2"
    ],
    "cause":{}
}
```




#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Set the extApp properties

#### Description

Add or update the properties of the extApp in a specified classroom.

#### Prototype

- Method: PUT
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/extApps/\{extAppUuid}/properties

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :----------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |
| `extAppUuid` | String | (Required) The extApp ID. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |

**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :----------- | :----- | :----------------------------------------------------------- |
| `properties` | Object | The user properties. |
| `common` | Object | The JSON object contains the following fields:<li>`state`: Integer, the state of extApp. `0` means disabled, and `1` means enabled.</li> |
| `cause` | Object | The update reason. |

#### Request example

**Request Body**

```json
{
    "properties" :{},
    "common":{
        "state":0
    },
    "cause":{}
}
```



#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Delete the extApp properties

#### Description

Delete the properties of the extApp in a specified classroom.

#### Prototype

- Method: DELETE
- Endpoint: /\{region}/edu/apps/\{appId}/v2/rooms/\{roomUUid}/extApps/\{extAppUuid}/properties

#### Request parameters

**URL parameters**

Pass the following parameters in the URL.

| Parameter | Type | Description |
| :----------- | :----- | :----------------------------------------------------------- |
| `region` | String | (Required) The region for connection. For details, see [Network geofencing](../develop/classroom-security#network-geofencing). Flexible Classroom supports the following regions:<li>`cn`: Mainland China.</li><li>`ap`: Asia Pacific.</li><li>`eu`: Europe.</li><li>`na`: North America.</li> |
| `appId` | String | (Required) Agora App ID.|
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |
| `extAppUuid` | String | (Required) The extApp ID. The string length must be less than 64 bytes. Supported character scopes are:<li>All lowercase English letters: a to z.</li>All numeric characters.<li>0-9</li><li>The space character.</li><li>"!", "#", "$", "%",  "&", "(", ")", "+", "-", ":", ";", "\<",  "=", ".", ">", "?",  "@", "[", "]",  "^", "_",  "\{", "\}",  "\|",  "~", "," </li>  |

**Request body parameters**

Pass in the following parameters in the request body.

| Parameter | Type | Description |
| :----------- | :---------- | :--------- |
| `properties` | String array | The user properties. |
| `cause` | Object | Reason for deletion. |

#### Request example

**Request Body**

```json
{
    "properties" :[
        "key-path1",
        "key-path2"
    ],
    "cause":{}
}
```

#### Response parameters

| Parameter | Type | Description |
| :----- | :------ | :---------------------------------------------------------- |
| `code` | Integer | Business status code:<li>0: The request succeeds.</li><li>Non-zero: The request fails.</li> |
| `msg` | String | The detailed information. |
| `ts` | Number | The current Unix timestamp (in milliseconds) of the server in UTC. |

#### Response example

```json
{
    "msg": "Success",
    "code": 0,
    "ts": 1610167740309
}
```

## Get data for pop-up quizzes

#### Prototype

- Method: GET
- Request path: /edu/apps/\{appId}/v2/rooms/\{roomUUid}/widgets/popupQuiz/sequences

#### Request parameters

**URL parameters**

Pass the following parameters in the URL:

| Parameter  | Type   | Description                                                  |
| :--------- | :----- | :----------------------------------------------------------- |
| `appId`    | String | (Required) Agora App ID.                                     |
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. |

**Query parameters**

| Parameter | Type    | Description                                                  |
| :-------- | :------ | :----------------------------------------------------------- |
| `nextId`  | String  | (Optional) The starting ID of the next batch of data. When you call this method to get the data for the first time, leave this parameter empty or set it as null. Afterward, you can set this parameter as the `nextId` that you get in the response of the previous method call. |
| `count`   | Integer | (Optional) The number of pieces of data in this batch. The default value is 100. |

#### Response parameters

The fields returned in `data` vary in different situations.

- After the teacher clicks the Start button to start a quiz, the summarized data of the Pop-up Quiz widget updates. `data` contains the following fields:

  | Field name                                 | Type     | Description                                                  |
  | :----------------------------------------- | :------- | :----------------------------------------------------------- |
  | action                                     | Integer  | The action type                                              |
  | changeProperties                           | Object   | The changed properties                                       |
  | changeProperties.extra                     | Object   | The extra information of the changed properties              |
  | changeProperties.extra.correctItems        | Object[] | The correct choice                                           |
  | changeProperties.extra.correctCount        | Integer  | The number of students who have made the correct choice      |
  | changeProperties.extra.answerState         | Integer  | The status of this quiz:<ul><li>`1` : In progress</li><li>`0`: Ended</li></ul> |
  | changeProperties.extra.receiveQuestionTime | Long     | The time when the students receive the question              |
  | changeProperties.extra.popupQuizId         | String   | The question ID                                              |
  | changeProperties.extra.averageAccuracy     | Float    | The rate at which the correct choice is made for this question |
  | changeProperties.extra.totalCount          | Integer  | The total number of students who have submitted their answers to this question |
  | changeProperties.extra.items               | Object[] | The options of this question                                 |
  | changeProperties.state                     | Integer  | The state of the Pop-up Quiz widget:<ul><li>`0`: Inactive</li><li>`1`: Active</li></ul> |
  | cause                                      | String   | The reason for the property change                           |
  | operator                                   | Object   | The operator of the property change                          |
  | operator.userUuid                          | String   | The ID of the operator                                       |
  | operator.userName                          | String   | The name of the operator                                     |
  | operator.role                              | String   | The role of the operator                                     |

- After a student submits the answer, the student's data updates. `data` contains the following fields:


  | Field name                      | Type     | Description                                            |
  | :------------------------------ | :------- | :----------------------------------------------------- |
  | action                          | Integer  | The action type                                        |
  | changeProperties                | Object   | The changed properties                                 |
  | changeProperties.lastCommitTime | Long     | The last submit time                                   |
  | changeProperties.popupQuizId    | String   | The question ID                                        |
  | changeProperties.selectedItems  | Object[] | The answer submitted by this student                   |
  | changeProperties.isCorrect      | Boolean  | Whether the answer submitted by the student is correct |
  | cause                           | String   | The reason for the property change                     |
  | operator                        | Object   | The operator of the property change                    |
  | operator.userUuid               | String   | The ID of the operator                                 |
  | operator.userName               | String   | The name of the operator                               |
  | operator.role                   | String   | The role of the operator                               |
  | fromUser                        | Object   | The user who starts this quiz                          |
  | fromUser.userUuid               | String   | The ID of the user who starts this quiz                |
  | fromUser.userName               | String   | The name of the user who starts this quiz              |
  | fromUser.role                   | String   | The role of the user who starts this quiz              |

- After a student submits the answer, the summarized data of the Pop-up Quiz widget updates. `data` contains the following fields:

  | Field name                             | Type    | Description                                                  |
  | :------------------------------------- | :------ | :----------------------------------------------------------- |
  | action                                 | Integer | The action type                                              |
  | changeProperties                       | Object  | The changed properties                                       |
  | changeProperties.extra                 | Object  | The extra information of the changed properties              |
  | changeProperties.extra.selectedCount   | Integer | The number of students who have submitted their answers      |
  | changeProperties.extra.correctCount    | Integer | The number of students who have made the correct choice      |
  | changeProperties.extra.averageAccuracy | Float   | The rate at which the correct choice is made for this question |
  | changeProperties.extra.totalCount      | Integer | The total number of students who have submitted their answers to this question |
  | cause                                  | String  | The reason for the property change                           |
  | operator                               | Object  | The operator of the property change                          |
  | operator.userUuid                      | String  | The ID of the operator                                       |
  | operator.userName                      | String  | The name of the operator                                     |
  | operator.role                          | String  | The role of the operator                                     |

- After the teacher ends the quiz, the summarized data of the Pop-up Quiz widget updates. `data` contains the following fields:

  | Field name                             | Type    | Description                                                  |
  | :------------------------------------- | :------ | :----------------------------------------------------------- |
  | action                                 | Integer | The action type                                              |
  | changeProperties                       | Object  | The changed properties                                       |
  | changeProperties.extra                 | Object  | The extra information of the changed properties              |
  | changeProperties.extra.selectedCount   | Integer | The number of students who have submitted their answers      |
  | changeProperties.extra.correctCount    | Integer | The number of students who have made the correct choice      |
  | changeProperties.extra.answerState     | Integer | The status of this quiz:<ul><li>`1` : In progress</li><li>`0`: Ended</li></ul> |
  | changeProperties.extra.averageAccuracy | Float   | The rate at which the correct choice is made for this question |
  | changeProperties.extra.totalCount      | Integer | The total number of students who have submitted their answers to this question |
  | cause                                  | String  | The reason for the property change                           |
  | operator                               | Object  | The operator of the property change                          |
  | operator.userUuid                      | String  | The ID of the operator                                       |
  | operator.userName                      | String  | The name of the operator                                     |
  | operator.role                          | String  | The role of the operator                                     |

#### Response example

- After the teacher clicks the Start button to start a quiz, the summarized data of the Pop-up Quiz widget updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "extra.correctItems": [
           "A",
           "B",
           "D"
       ],
       "extra.totalCount": NumberInt("1"),
       "extra.answerState": NumberInt("1"),
       "state": NumberInt("1"),
       "extra.popupQuizId": "ab5b183238a74d5a9c955dc87c6397e0",
       "extra.averageAccuracy": 0,
       "extra.correctCount": NumberInt("0"),
       "extra.items": [
           "A",
           "C",
           "B"
       ],
       "extra.receiveQuestionTime": NumberLong("1652413962895")
   },
   "operator": {
       "userName": "server",
       "userUuid": "server",
       "role": "server"
   }
   ```

- After a student submits the answer, the student's data updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "selectedItems": [
           "A",
           "B",
           "D"
       ],
       "isCorrect": true,
       "popupQuizId": "ab5b183238a74d5a9c955dc87c6397e0",
       "lastCommitTime": NumberLong("1652413989997")
   },
   "fromUser": {
       "userName": "yerongzhe2",
       "userUuid": "yerongzhe22",
       "role": "audience"
   }
   ```

- After the teacher ends the quiz, the summarized data of the Pop-up Quiz widget updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "extra.totalCount": NumberInt("1"),
       "extra.answerState": NumberInt("0"),
       "extra.selectedCount": NumberInt("1"),
       "extra.averageAccuracy": 1,
       "extra.correctCount": NumberInt("1")
   },
   "operator": {
       "userName": "server",
       "userUuid": "server",
       "role": "server"
   }
   ```



## Get data for polls

#### Prototype

- Method: GET
- Request path: /edu/apps/\{appId}/v2/rooms/\{roomUUid}/widgets/poll/sequences

#### Request parameters

**URL parameters**

Pass the following parameters in the URL:

| Parameter  | Type   | Description                                                  |
| :--------- | :----- | :----------------------------------------------------------- |
| `appId`    | String | (Required) Agora App ID.                                     |
| `roomUuid` | String | (Required) The classroom ID. This is the globally unique identifier of a classroom. It is also used as the channel name when a user joins achannel. The string length must be less than 64 bytes. |

**Query parameters**

| Parameter | Type    | Description                                                  |
| :-------- | :------ | :----------------------------------------------------------- |
| `nextId`  | String  | (Optional) The starting ID of the next batch of data. When you call this method to get the data for the first time, leave this parameter empty or set it as null. Afterward, you can set this parameter as the `nextId` that you get in the response of the previous method call. |
| `count`   | Integer | (Optional) The number of pieces of data in this batch. The default value is 100. |

#### Response parameters

The fields returned in `data` vary in different situations.

- After the teacher clicks the Start button to start a poll, the summarized data of the Polling widget updates. `data` contains the following fields:

  | Field name                                    | Type                | Description                                                  |
  | :-------------------------------------------- | :------------------ | :----------------------------------------------------------- |
  | action                                        | Integer             | The action type                                              |
  | changeProperties                              | Object              | The changed properties                                       |
  | changeProperties.extra                        | Object              | The extra information of the changed properties              |
  | changeProperties.extra.mode                   | Integer             | The polling mode:<ul><li>`1`: Single-choice</li><li>`2`: Multiple-choice</li></ul> |
  | changeProperties.extra.pollingState           | Integer             | The status of this poll:<ul><li>`1` : In progress</li><li>`0`: Ended</li></ul> |
  | changeProperties.extra.pollDetails            | Map\<String, Object> | The polling results. `key` is the option index, starting from `0`. |
  | changeProperties.extra.pollDetails.num        | Integer             | The number of students who have selected this option         |
  | changeProperties.extra.pollDetails.percentage | Float               | The percentage of students who have selected this option in students who have submitted their choices |
  | changeProperties.extra.pollId                 | String              | The poll ID                                                  |
  | changeProperties.extra.pollItems              | Object            | The option content                                           |
  | changeProperties.state                        | Integer             | The state of the Polling widget:<ul><li>`0`: Inactive</li><li>`1`: Active</li></ul> |
  | cause                                         | String              | The reason for the property change                           |
  | operator                                      | Object              | The operator of the property change                          |
  | operator.userUuid                             | String              | The ID of the operator                                       |
  | operator.userName                             | String              | The name of the operator                                     |
  | operator.role                                 | String              | The role of the operator                                     |

- After a student submits the choice, the student's data updates. `data` contains the following fields:

  | Field name                         | Type     | Description                                      |
  | :--------------------------------- | :------- | :----------------------------------------------- |
  | action                             | Integer  | The action type                                  |
  | changeProperties                   | Object   | The changed properties                           |
  | changeProperties.extra             | Object   | The extra information of the changed properties  |
  | changeProperties.extra.pollId      | String   | The poll ID                                      |
  | changeProperties.extra.selectIndex | Object[] | The index of the option selected by this student |
  | cause                              | String   | The reason for the property change               |
  | operator                           | Object   | The operator of the property change              |
  | operator.userUuid                  | String   | The ID of the operator                           |
  | operator.userName                  | String   | The name of the operator                         |
  | operator.role                      | String   | The role of the operator                         |
  | fromUser                           | Object   | The user who starts this poll                    |
  | fromUser.userUuid                  | String   | The ID of the user who starts this poll          |
  | fromUser.userName                  | String   | The name of the user who starts this poll        |
  | fromUser.role                      | String   | The role of the user who starts this poll        |

- After a student submits the answer, the summarized data of the Polling widget updates. `data` contains the following fields:
  | Field name                                    | Type                | Description                                                  |
  | :-------------------------------------------- | :------------------ | :----------------------------------------------------------- |
  | action                                        | Integer             | The action type                                              |
  | changeProperties                              | Object              | The changed properties                                       |
  | changeProperties.extra                        | Object              | The extra information of the changed properties              |
  | changeProperties.extra.pollDetails            | Map\<String, Object> | The polling results. `key` is the option index, starting from `0`. |
  | changeProperties.extra.pollDetails.num        | Integer             | The number of students who have selected this option         |
  | changeProperties.extra.pollDetails.percentage | Float               | The percentage of students who have selected this option in students who have submitted their choices |
  | changeProperties.extra.pollId                 | String              | The poll ID                                                  |
  | cause                                         | String              | The reason for the property change                           |
  | operator                                      | Object              | The operator of the property change                          |
  | operator.userUuid                             | String              | The ID of the operator                                       |
  | operator.userName                             | String              | The name of the operator                                     |
  | operator.role                                 | String              | The role of the operator                                     |

- After the teacher ends the poll, the summarized data of the Polling widget updates. `data` contains the following fields:

  | Field name                                    | Type                | Description                                                  |
  | :-------------------------------------------- | :------------------ | :----------------------------------------------------------- |
  | action                                        | Integer             | The action type                                              |
  | changeProperties                              | Object              | The changed properties                                       |
  | changeProperties.extra                        | Object              | The extra information of the changed properties              |
  | changeProperties.extra.pollingState           | Integer             | The status of this poll:<ul><li>`1` : In progress</li><li>`0`: Ended</li></ul> |
  | changeProperties.extra.pollDetails            | Map\<String, Object> | The polling results. `key` is the option index, starting from `0`. |
  | changeProperties.extra.pollDetails.num        | Integer             | The number of students who have selected this option         |
  | changeProperties.extra.pollDetails.percentage | Float               | The percentage of students who have selected this option in students who have submitted their choices |
  | changeProperties.extra.pollId                 | String              | The poll ID                                                  |
  | cause                                         | String              | The reason for the property change                           |
  | operator                                      | Object              | The operator of the property change                          |
  | operator.userUuid                             | String              | The ID of the operator                                       |
  | operator.userName                             | String              | The name of the operator                                     |
  | operator.role                                 | String              | The role of the operator                                     |

#### Response example

- After the teacher clicks the Start button to start a poll, the summarized data of the Polling widget updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "extra.pollId": "e556ce3df5cd4c23941b03bf54d29ba3",
       "extra.pollState": NumberInt("1"),
       "extra.pollItems": [
           "aaa",
           "bbb",
           "ccc",
           "ddd",
           "eee"
       ],
       "extra.mode": NumberInt("2"),
       "state": NumberInt("1"),
       "extra.pollDetails": {
           "0": {
               "num": NumberInt("0"),
               "percentage": 0
           },
           "1": {
               "num": NumberInt("0"),
               "percentage": 0
           },
           "2": {
               "num": NumberInt("0"),
               "percentage": 0
           },
           "3": {
               "num": NumberInt("0"),
               "percentage": 0
           },
           "4": {
               "num": NumberInt("0"),
               "percentage": 0
           }
       }
   },
   "operator": {
       "userName": "server",
       "userUuid": "server",
       "role": "server"
   }
   ```

- After a student submits the choice, the student's data updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "pollId": "e556ce3df5cd4c23941b03bf54d29ba3",
       "selectIndex": [
           NumberInt("1"),
           NumberInt("2"),
           NumberInt("4")
       ]
   },
   "fromUser": {
       "userName": "yerongzhe2",
       "userUuid": "yerongzhe22",
       "role": "audience"
   },
   "operator": {
       "userName": "server",
       "userUuid": "server",
       "role": "server"
   }
   ```

- After a student submits the choice, the summarized data of the Polling widget updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "extra.pollId": "2f38e6de32064713adf135de41c963df",
       "extra.pollDetails": {
           "0": {
               "num": NumberInt("1"),
               "percentage": 0.33333334
           },
           "1": {
               "num": NumberInt("3"),
               "percentage": 1
           },
           "2": {
               "num": NumberInt("3"),
               "percentage": 1
           },
           "3": {
               "num": NumberInt("0"),
               "percentage": 0
           },
           "4": {
               "num": NumberInt("2"),
               "percentage": 0.6666667
           }
       }
   },
   "operator": {
       "userName": "server",
       "userUuid": "server",
       "role": "server"
   }
   ```


- After the teacher ends the poll, the summarized data of the Polling widget updates:

   ```json
   "action": NumberInt("1"),
   "changeProperties": {
       "extra.pollId": "2f38e6de32064713adf135de41c963df",
       "extra.pollDetails": {
           "0": {
               "num": NumberInt("1"),
               "percentage": 0.33333334
           },
           "1": {
               "num": NumberInt("3"),
               "percentage": 1
           },
           "2": {
               "num": NumberInt("3"),
               "percentage": 1
           },
           "3": {
               "num": NumberInt("0"),
               "percentage": 0
           },
           "4": {
               "num": NumberInt("2"),
               "percentage": 0.6666667
           }
       }
   },
   "operator": {
       "userName": "server",
       "userUuid": "server",
       "role": "server"
   }
   ```

## Status code

| Response status code | Business status code | Description |
| :-------------- | :--------- | :----------------------------------------------------------- |
| 200 | 0 | The request succeeds. |
| 400 | 400 | The request parameter is incorrect. |
| 401 | N/A | Possible reasons:<li>The App ID is invalid.</li><li>Unauthorized. Incorrect `x-agora-uid` or `x-agora-token`.</li> |
| 403 | 30403200 | The classroom is muted globally. Users cannot send chat messages. |
| 404 | N/A | The server cannot find the requested resource. |
| 404 | 20404100 | The classroom does not exist. |
| 404 | 20404200 | The user does not exist. |
| 409 | 30409410 | The recording has not been started. |
| 409 | 30409411 | The recording has not been ended. |
| 409 | 30409100 | The class has been started. |
| 409 | 30409101 | The class has been ended. |
| 500 | 500 | The server has an internal error and cannot process the request. |
| 503 | N/A | Internal server error. The gateway or proxy server does not receive a timely response from the upstream server. |



## Events
This section lists all types of events that you can get through the [Get classroom events](#get-classroom-events) method.

### The classroom state changes

When the `cmd` property of an event is `1`, the event indicates the classroom state changes, and the `data` property contains the following fields:

| Parameter | Type | Description |
| ----------- | ------- | ------------------------------------------------------------ |
| `startTime` | Number | The Unix timestamp (in milliseconds) when the classroom starts, in UTC. This property is available after the state of the classroom changes to "Started". |
| `state` | Integer | The current state of the classroom:<ul><li>`0`: Not started.</li><li>`1`: In progress.</li><li>`2`: Ended.</li><li>`3`: After the run-late time of a class, the room is closed and users can no longer enter the room.</li></ul> |

**Example**

```json
{
    "startTime":1611561776588,
    "state":1
}
```

### Receives a room chat message

When the `cmd` property of an event is `3`, the event indicates the server receives a room chat message, and the` data` contains the following fields:

| Parameter | Type | Description |
| ---------- | ------- | ------------------------------------------------------------ |
| `fromUser` | Object | The user who sends this message. This object contains the following fields:<ul><li>`userUuid`: String. The user ID.</li><li>`userName`: String. The user name.</li><li>`role`: Integer. The user role. This parameter can be set as one of the following values:<ul><li>`1`: Teacher.</li><li>`2`: Student.</li></ul></li></ul> |
| `message` | String | The message. |
| `type` | Integer | The type of the message. Temporarily, you can only set this parameter as `1`(text messages). |



**Example**
```json
{
    "fromUser":{
        "role":"host",
        "userName":"jason",
        "userUuid":"jason1"
    },
    "message":"aa",
    "type":1
}
```

### Users enter or leave the classroom

When the `cmd` property of an event is `20`, the event indicates that users have entered or left the classroom. `data` includes the following fields:

| Parameter | Type | Description |
| -------------- | ----------- | ------------------------------------------------------------ |
| `total` | Integer | The total number of users in the classroom after this event. |
| `onlineUsers` | Object Array | The new users who entered the classroom at the time of this event. This object contains the following fields:<ul><li>`userName`: String. The user name.</li><li>`userUuid`: String. The user ID.</li><li>`role`: Integer. The user role. This parameter can be set as one of the following values:<ul><li>`1`: Teacher.</li><li>`2`: Student.</li></ul></li><li>`userProperties`: Object. The user property.</li><li>`streamUuid`: String. The ID of the stream, which is also the uid used when joining an <Vg k="VSDK" /> channel.</li><li>`type`: Integer. The reasons why the user enters the room:<ul><li>`1`: The user enters the classroom in a normal way.</li><li>`2`: The user re-enters the classroom.</li></ul></li><li>`updateTime`: Number. The time when the user enters the classroom, Unix timestamp (milliseconds), UTC time.</li></ul> |
| `offlineUsers` | Object Array | The new users who have left the classroom at the time of this event. This object contains the following fields:<ul><li>`userName`: String. The user name.</li><li>`userUuid`: String. The user ID.</li><li>`role`: Integer. The user role. This parameter can be set as one of the following values:<ul><li>`1`: Teacher.</li><li>`2`: Student.</li></ul></li><li>`userProperties`: Object. The user property.</li><li>`streamUuid`: String. The ID of the stream, which is also the uid used when joining an <Vg k="VSDK" /> channel.</li><li>`type`: Integer. The reasons why the user leaves the classroom:<ul><li>`1`: The user leaves the classroom on the client, such as leaving the class normally, the application is forcibly closed, or the user is disconnected due to poor network conditions.</li><li>`2`: The user is kicked out of the classroom.</li></ul></li><li>`updateTime`: Number. The time when the user enters or leaves the classroom, Unix timestamp (in milliseconds), UTC time.</li></ul> |

**Example**
```json
{
    "total":3,
    "onlineUsers":[
        {
            "userName":"",
            "userUuid":"",
            "role":"0",
            "userProperties":{  },
            "streamUuid":"",
            "type":1,
            "updateTime":1611561776588
        }
    ],
    "offlineUsers":[
        {
            "userName":"",
            "userUuid":"",
            "role":"0",
            "userProperties":{},
            "streamUuid":"",
            "type":1,
            "updateTime":1611561776588
        }
    ]
}
```


### The recording state changes

When the `cmd` property of an event is `1001`, the event indicates the recording state changes, and the `data` property contains the following fields:

| Parameter | Type | Description |
| ------------ | ------- | ------------------------------------------------------------ |
| `recordId` | String | This is the unique identifier of a recording session. A recording session starts when you call a method to start recording and ends when you call this method to stop recording. This field is available only when `state` is `1`. |
| `sid` | String | The `sid` of the Agora Cloud Recording service. This field is available only when `state` is `1`. |
| `resourceId` | String | The `resourceId` of the Agora Cloud Recording service. This field is available only when `state` is `1`. |
| `state` | Integer | The current recording state:<ul><li>`2`: Recording has ended.</li><li>`1`: In recording.</li></ul> |
| `startTime` | Number | The Unix timestamp (in milliseconds) when the recording starts, in UTC. This property is available after the recording state changes to "Started". |

**Example**
```json
{
    "recordId":"xxx",
    "sid":"xxx",
    "resourceId":"xxx",
    "state":1,
    "startTime":1611564500488
}
```


### The number of rewards changes

When the `cmd` property of an event is `1101`, the event indicates the number of rewards changes, and the `data` property contains the following fields:

| Parameter | Type | Description |
| :-------------- | :---------- | :----------------------------------------------------------- |
| `rewardDetails` | Object Array | Each object represents the rewards of a user and contains the following fields:<li>`userUuid`: String. The user ID.</li><li>`changedReward`: Integer. The number of changed rewards.</li><li>`total`: Integer. The total number of rewards after the change.</li> |
| `updateTime` | Number | The Unix timestamp (in milliseconds) when the rewards change, in UTC. |

**Example**

```json
{
     "rewardDetails":[ {
            "userUuid":"",
            "changedReward": 1,
            "totalReward": 10
        } ],
       "updateTime":1611564500488
}
```

### The resources in the classroom change

When the `cmd` property of an event is `1003`, the event indicates the resources in the classroom change, and the `data` property contains the following fields:

| Parameter | Type | Description |
| :---------- | :---------- | :----------------------------------------------------------- |
| Parameter | Type | Description |
| `resources` | Object Array | Each object represents a public resource and contains the following fields:<li>`resourceUuid`: String. The resource ID.</li><li>`resourceName`: String. The resource name.</li><li>`size`: Number. The resourc size (bytes).</li><li>`url`: String. The URL address of the resource.</li><li>`taskUuid`: String. The ID of the file conversion task.</li><li>`taskToken`: String. The token used for the file conversion task.</li><li>`taskProgress`: Object. The progress of a file conversion task.</li> |
| `operator` | Object | It contains the following fields:<li>`userUuid`: String. The user ID.</li><li>`userName`: String. The user name.</li><li>`role`: Integer. Th user role.</li> |
| `action` | Integer | The resource change type:<li>`1`: The resource is added or updated.</li><li>`2`: The resource is deleted.</li> |

**Example**

```json
{
     "resources": [{
            "resourceUuid":"",
            "resourceName": "1",
            "size": 1024,
            "url": "http://xxx.com/ooo",
            "taskUuid": "",
            "taskToken": "",
            "taskProgress": {},
        } ],
      "operator":{
        "role":"1",
        "userName":"jason",
        "userUuid":"jason1"
        },
       "action": 1
}
```

### The users "on the stage" change

When the `cmd` property of an event is `1501`, the event indicates the users "on the stage" change, and the` data` property contains the following fields:

| Parameter | Type | Description |
| :-------------------- | :---------- | :----------------------------------------------------------- |
| `acceptedUsers` | Object Array | The list of users who are now "on the stage". The object contains the following fields:<li>`userUuid`: String. The user ID.</li> |
| `addAcceptedUsers` | Object Array | The list of users who have just "gone onto the stage". The object contains the following fields:<li>`userUuid`: String. The user ID.</li> |
| `removeAcceptedUsers` | Object Array | The list of users who have just "left the stage". The object contains the following fields:<li>`userUuid`: String. The user ID.</li> |

**Example**

```json
{
    "acceptedUsers": [{
        "userUuid":""
    }],
    "addAcceptedUsers": [{
        "userUuid":""
    }],
    "removeAcceptedUsers": [{
        "userUuid":""
    }]
}
```

### The users who wave their hands change

When the `cmd` property of an event is `1502`, the event indicates the users who wave their hands change, and the `data` property contains the following fields:

| Parameter | Type | Description |
| :-------------------- | :---------- | :----------------------------------------------------------- |
| `progressUsers` | Object Array | The list of users who are waving their hands. The object contains the following fields:<li>`userUuid`: String. The user ID.</li><li>`payload`: Object.</li> |
| `addProgressUsers` | Object Array | The list of users who have just started waving their hands. The object contains the following fields:<li>`userUuid`: String. The user ID.</li><li>`payload`: Object.</li> |
| `removeProgressUsers` | Object Array | The list of users who have just stopped waving their hands. The object contains the following fields:<li>`userUuid`: String. The user ID.</li><li>`payload`: Object.</li> |

**Example**

```json
{
    "progressUsers": [{
        "userUuid":"",
        "payload":{}
    }],
    "addProgressUsers": [{
        "userUuid":"",
        "payload": {}
    }],
    "removeProgressUsers": [{
        "userUuid":"",
        "payload": {}
    }]
}
```




