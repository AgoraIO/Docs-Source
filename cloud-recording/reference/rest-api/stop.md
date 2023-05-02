---
title: "Stop recording"
sidebar_position: 6
type: docs
platform_selector: false
description: 
  Stop recording
---

When a recording finishes, call the `stop` method to leave the channel and stop recording. To use Agora Cloud Recording again, you need to call the  [`acquire`](../rest-api/acquire) method for a new resource ID.

- Method: POST
- Endpoint: /v1/apps/\<appid\>/cloud_recording/resourceid/\<resourceid\>/sid/\<sid\>/mode/\<mode\>/stop

> - The request frequency limit is 10 requests per second for each [Agora account](../manage-agora-account#create-an-agora-account). Contact [Agora technical supoort](mailto:support@agora.io) if you need to raise the limit.
> - By default, Agora Cloud Recording automatically leaves the channel and stops recording if there are ever no users in the channel for more than 30 seconds.

## HTTP request

The following parameters are required in the URL.

| Parameter    | Type   | Description                                                                                                     |
| :----------- | :----- |:----------------------------------------------------------------------------------------------------------------|
| `appid`      | String | Your App ID.                                                                                                    |
| `resourceid` | String | The resource ID requested by the  [`acquire`](../rest-api/acquire) method.                                      |
| `sid`        | String | The recording ID created by the [`start`](../rest-api/start) method.                                            |
| `mode`       | String | The recording mode. Supports individual mode (`individual`), composite mode (`mix`), and web page mode (`Web`). |

The following parameters are required in the request body.

| Parameter       | Type   | Description                                                                                                                                                                                                                                                                               |
| :-------------- | :----- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cname`         | String | <ul><li>In web page recording mode, use `cname` to distinguish between recording sessions.</li><li>In other recording modes, use `cname` to set the name of the channel to be recorded.</li></ul>                                                                                         |
| `uid`           | String | A string that contains the user ID of the recording client. Must be the same `uid` used in the [`acquire`](../rest-api/acquire) method.                                                                                                                                                   |
| `clientRequest` | JSON   | A specific client request that is empty for this method.                                                                                                                                                                                                                                  |
| `clientRequest.async_stop` | (Optional) bool   | Whether the `stop` method call is asynchronous.<li>Asynchronous. A response is received immediately after calling `stop`.</li><li>Synchronize. After calling `stop`, you need to wait for all recording files to be uploaded to the third-party cloud storage to receive a response.</li> |

### Request example

- The request URL is:

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/stop
```
- `Content-type` is `application/json;charset=utf-8`.
- `Authorization` is the basic authentication, see [RESTful API authentication](../restful-authentication) for details.

- The request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",  
    "clientRequest":{
        "async_stop": false   
    }
}
```

### Response example

```json
"Code": 200,
"Body":
{
    "resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG",
    "sid": "38f8e3cfdc474cd56fc1ceba380d7e1a",
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
        "uploadingStatus": "uploaded"
    }
}
```

## HTTP response

If the returned HTTP status code is `200`, it means the request was successful, and the response body contains the following fields:
- `code`: Number. [Status code](../common-errors#status-codes).
- `resourceId`: String. The resource ID for cloud recording. The resource ID is valid for five minutes.
- `sid`: String. The recording ID. The unique identification of the current recording.
- `serverResponse`: JSON. The details about the recording status. The child elements in `serverResponse` vary according to your configurations in [`start`](../rest-api/start). For example, if you configure `snapshotConfig` or `extensionServiceConfig` in `start`, then `stop` does not return `fileListMode`.
  - `fileListMode`: String. The data type of `fileList`.
    - `"string"`: `fileList` is a string. In composite mode, if you set `avFileType` as [`"hls"]`, `fileListMode` is `"string"`.
    - `"json"`: `fileList` is a JSONArray. In individual mode, or if you set `avFileType` as [`"hls","mp4"]` in composite recording mode, `fileListMode` is `"json"`.
  - `fileList`: When `fileListMode` is `"string"`, `fileList` is a string that represents the filename of the M3U8 file. When `fileListMode` is `"json"`, `fileList` is a JSONArray that contains the details of each recorded file.
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
  - `uploadingStatus`: String. The upload status.
    - `"uploaded"`: All the recorded files are uploaded to the third-party cloud storage.
    - `"backuped"`:  Some of the recorded files fail to upload to the third-party cloud storage and upload to Agora Cloud Backup instead. Agora Cloud Backup automatically uploads these files to your cloud storage. 
    - `"unknow"`: Unknown status.
  - `extensionServiceState`: JSONArray. An array of the detailed status information of each service.
	**Uploading service**
   - `serviceName`: String. The name of the service. `"upload_service"` means the uploading service.
    - `payload`: JSON. The status of the service.
      - `uploadingStatus`: String. The uploading status.
        - `"uploaded"`: All the recorded files are uploaded to the third-party cloud storage.
        - `"backuped"`: All the recorded files are uploaded, but at least one TS file is uploaded to Agora Cloud Backup. Agora Cloud Backup will automatically upload these files to your cloud storage later.
        - `"unknow"`: Unknown status.

	**Web page recording**
   - `serviceName`: String. The name of the service. `"web_recorder_service"` means web page recording.
	- `payload`: JSON. The status of the extension service.
     - `state`: String. The status of uploading subscribed content to the extension service.
       - `"init"`: The service is initializing.
        - `"inProgress"`: The service has initialized and is working.
        - `"exit"`: The service exits.
      - `onhold`：Bool. Whether the page recording is paused.
         - `true`: The web page recording is paused.
         - `false`: The web page recording continues.
	 - `fileList`: JSONArray. An array that contains detailed information of each recorded file.
	   - `fileName`: String. The name of the M3U8 file or MP4 file.
	   - `sliceStartTime`: Number. The Unix timestamp (ms) when the recording starts.
	
	**Push media stream to the CDN during a web page recording**
	- `serviceName`: String. The name of the service. `"rtmp_publish_service"` means pushing media stream to the CDN during a web page recording.
	- `payload`: JSON. The status of the extension service.
	 - `status`: String. The CDN streaming status of the web page recording, including the following options:
	   - `"connecting"`: Connecting to the CDN server.
	   - `"publishing"`: Pushing the stream to the CDN server.
	   - `"onhold"`: Pause streaming.
	   - `"disconnected"`: Failed to connect to the CDN server. Agora recommends that you change the CDN address.