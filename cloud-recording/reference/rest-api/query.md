---
title: "Query the recording status"
sidebar_position: 6
type: docs
platform_selector: false
description: >
  After you start a recording, you can call `query` method to check its status.
---



<div class="note alert">`query` works only with an ongoing recording session. If you call `query` after a recording ends or after it starts with error, you get a 404 (Not Found) error.</div>

- Method: GET
- Endpoint: /v1/apps/\<appid\>/cloud_recording/resourceid/\<resourceid\>/sid/\<sid\>/mode/\<mode\>/query

> The request frequency limit is 10 requests per second for each [Agora account](../manage-agora-account#create-an-agora-account). Contact [Agora technical support](mailto:support@agora.io) if you need to raise the limit.

## HTTP request

The following parameters are required in the URL.

| Parameter    | Type   | Description                                                                                                                                                                                                         |
| :----------- | :----- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `appid`      | String | Your App ID.                                                                                                                                                                                                        |
| `resourceid` | String | The resource ID requested by the [`acquire`](../rest-api/acquire) method.                                                                                                                                           |
| `sid`        | String | The recording ID created by the [`start`](../rest-api/start) method.                                                                                                                                                |
| `mode`       | String | The recording mode. Supports [`Individual recording mode`](../../develop/individual-mode), [`Composite recording mode`](../../develop/composite-mode), and [`Web page recording mode`](../../develop/webpage-mode). |

## Request example

- The request URL is:

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/query
```
- `Content-type` is `application/json;charset=utf-8`.
- `Authorization` is the basic authentication, see [RESTful API authentication](../restful-authentication) for details.


## HTTP response

If the returned HTTP status code is `200`, it means the request was successful, and the response body contains the following fields:

- `code`: Number. [Status code](../common-errors#status-codes).
- `resourceId`: String. The resource ID for cloud recording. The resource ID is valid for five minutes.
- `sid`: String. The recording ID. The unique identification of the current recording.
- `serverResponse`: JSON. The details about the recording status. 
  The child elements in `serverResponse` vary according to your configurations in `start`. For example, if you configure `snapshotConfig` or `extensionServiceConfig` in `start`, then `query` does not return `fileListMode`.
	
  - `fileListMode`: String. The data type of `fileList`.
    - `"string"`: `fileList` is a string. In composite mode, if you set `avFileType` as [`"hls"]`, `fileListMode` is `"string"`.
    - `"json"`: `fileList` is a JSONArray. In individual mode, or if you set `avFileType` as [`"hls","mp4"]` in composite recording mode, `fileListMode` is `"json"`.
  - `fileList`: When `fileListMode` is `"string"`, `fileList` is a string that represents the filename of the M3U8 file. When `fileListMode` is `"json"`, `fileList` is a JSONArray that contains the details of each recorded file. The `query` method does not return this field if you have set `snapshotConfig`.
    - `fileName`: String. The name of the M3U8 file and MP4 files.
    - `trackType`: String. The type of the recorded file.
      - `"audio"`: Audio file.
      - `"video"`: Video file (no audio).
      - `"audio_and_video"`: Video file (with audio).
    - `uid`: String. User ID. The user whose audio or video is recorded in the file. In composite recording mode, `uid` is `"0"`.
    - `mixedAllUser`: Boolean. Whether the audio and video of all users are combined into a single file.
      - `true`: All users are recorded in a single file.
      - `false`: Each user is recorded separately.
    - `isPlayable`: Boolean. Whether the file can be played online.
      - `true`: The file can be played online.
      - `false`: The file cannot be played online.
    - `sliceStartTime`: Number. The Unix time (ms) when the recording starts.
  - `status`: Number. The status of the cloud service.
    - `0`: The cloud service has not started.
    - `1`: The initialization is complete.
    - `2`: The cloud service is starting.
    - `3`: The cloud service is partially ready.
    - `4`: The cloud service is ready.
    - `5`: The cloud service is in progress.
    - `6`: The cloud service receives the request to stop.
    - `7`: The cloud service stops.
    - `8`: The cloud service exits.
    - `20`: The cloud service exits abnormally.
  - `sliceStartTime`: Number. The time when the recording starts. Unix timestamp (ms).
  - `subServiceStatus`: JSON. The status of the cloud recording submodules. The recording service does not return this field in web page recording mode.
   - `recordingService`: String. The status of the video subscription submodule. For details, see [Service status](../common-errors#service-status). 
  - `extensionServiceState`: JSONArray. An array of the detailed status information of each extension service. 
	  
	**ApsaraVideo for VoD**
	  - `serviceName`: String. The name of the extension service. `aliyun_vod_service` means ApsaraVideo for VoD.
  	- `payload`: JSON. The status of the extension service.
        - `state`: String. The status of uploading media content to the extension service.
          - `"inProgress"`: The recorded files are being uploaded to the extension service.
          - `"idle"`: No user is sending streams in the channel. Nothing is being uploaded.
        - `videoInfo`: JSONArray. An array of the M3U8 files and their corresponding video IDs. ApsaraVideo for VoD generates a video ID for each M3U8 file uploaded.
          - `fileName`: String. The name of the M3U8 file.
          - `videoId`: String. The corresponding video ID of the M3U8 file.

   **Web page recording**

   - `serviceName`: String . The name of the extension service. `"web_recorder_service"` means web page recording.
   - `payload`: JSON. The status of the extension service.
     - `state`: String. The status of uploading subscribed content to the extension service.
          - `"init"`: The service is initializing.
          - `"inProgress"`: The service has initialized and is working.
          - `"exit"`: The service exits.
	  - `onhold`：Bool. Whether the page recording is paused.
          - `true`: The web page recording is paused.
          - `false`: The eeb page recording continues.
      - `fileList`: JSONArray. An array that contains details of each recorded file.
       - `fileName`: String. The name of the M3U8 file or MP4 file.
	    - `sliceStartTime`: Number. The Unix timestamp (ms) when the recording starts.:
	
	**Push media stream to the CDN during a web page recording**
	
	- `serviceName`: String . The name of the extension service. `"rtmp_publish_service"` means pushing media stream to the CDN during a web page recording.
	- `payload`: JSON. The status of the extension service.
   - `outputs`: JSON Array. Configure as follows:
    - `rtmpUrl`: String. The CDN address which you want to push stream to.
	  - `status`：String. The CDN streaming status, including the following options:
	   - `connecting`: Connecting to the CDN server.
	   - `publishing`: Pushing the stream to the CDN server.
	   - `onhold`: Pause streaming.
	   - `disconnected`: Failed to connect to the CDN server. Agora recommends that you change the CDN address.
	
	
## Response example
#### Audio and video recording in a channel
```json
"Code": 200,
"Body":
{
    "resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG",
    "serverResponse": {
        "fileListMode": "json",
        "fileList": [
            {
                "fileName": "xxx.m3u8",
                "trackType": "audio_and_video",
                "uid": "123",
                "mixedAllUser": true,
                "isPlayable": true,
                "sliceStartTime": 1562724971626
            },
            {
                "fileName": "xxx.m3u8",
                "trackType": "audio_and_video",
                "uid": "456",
                "mixedAllUser": true,
                "isPlayable": true,
                "sliceStartTime": 1562724971626
            }
        ],
        "status": 5,
        "sliceStartTime": 1562724971626
    }
}
```
#### Web page recording
```json
"Code": 200,
"Body":
{
    "resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG",
    "serverResponse": {
        "extensionServiceState": [
            {
                "payload": {
                    "fileList": [],
                    "onhold": false,
                    "state": "inProgress"
                },
                "serviceName": "web_recorder_service"
            }
        ],
        "status": 4
    }
}
```
#### Push media stream to the CDN during a web page recording
```json
"Code": 200,
"Body":
{
    "resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG",
    "serverResponse": {
        "extensionServiceState": [
            {
                "payload": {
                    "fileList": [],
                    "onhold": false,
                    "state": "inProgress"
                },
                "serviceName": "web_recorder_service"
            },
            {
                "payload": {
                    "outputs": [
                        {
                            "rtmpUrl": "rtmp://xxx",
                            "status": "publishing"
                        }
                    ]
                },
                "serviceName": "rtmp_publish_service"
            }
        ],
        "status": 4
    }
}
```

## What are the differences between the Message Notification Service and the query Method?

You can monitor the status of the cloud recording service either through the `query` method or by the Message Notification Service, to take action when required. Both options have pros and cons.

### The query method

You can periodically call the `query` method to monitor the status of a cloud recording.

- Pros: Reliable, as the status is queried proactively.
- Cons:
  - Provides limited status information.
  - Requires an active query. You cannot query too often because of the Queries Per Second (QPS) limit, and thus it is not as real-time as the Message Notification Service.

If the reliability of the status of a cloud recording is a high priority, Agora strongly recommends using the `query` method.

### Message Notification Service

You can use the Message Notification Service as a complementary option to monitor the recording service status. You need to configure an HTTP/HTTPS server to receive event notifications. For details, see [Agora Cloud Recording RESTful API Callback Service](../rest-api/rest-api-overview).

- Pros: Real-time
- Cons:
  - The server passively receives messages, and the messages may get lost.
  - The confirmation message of the message delivery may get lost, causing the message to be resent. In such a case, you need to deduplicate the notifications.
  - The messages may not arrive in the correct order.

Agora recommends that core apps should not rely on the Message Notification Service. If your apps already rely heavily on the Message Notification Service, Agora recommends that you contact [support@agora.io](mailto:support@agora.io) to enable the redundant message notification function, which doubles the received notifications and reduces the probability of message loss. Redundant message notification still cannot guarantee a 100% arrival rate.
