---
title: "Cloud Recording API callback service"
sidebar_position: 5
type: docs
platform_selector: false
description: >
  Notifies the Message Notification Service, and then the Message Notification Service notifies your server of that event through an HTTP/HTTPS request.
---

import SignatureVerification from '@docs/shared/notification-center-service/signature-verification.mdx';

Agora provides <Vg k="NCS_LONG" /> (<Vg k="NCS" />). You can set up an HTTP/HTTPS server to receive the event notifications of Agora Cloud Recording. When an event occurs, the Agora Cloud Recording service notifies the Message Notification Service, and then the Message Notification Service notifies your server of that event through an HTTP/HTTPS request.

Best practice is that core apps do not rely on <Vg k="NCS_LONG" /> (<Vg k="NCS" />). If your apps already rely heavily on the <Vg k="NCS" />, contact <a href="mailto:support@agora.io">support@agora.io</a> and enable the redundant message notification function. This doubles the received notifications and reduces the probability of message loss. After enabling the message notification function, you need to deduplicate messages based on `sid`. Message notification still cannot guarantee a 100% arrival rate.

## Callback information

After you enable the callback service, when a specified event occurs, the Agora notification center sends an HTTP/HTTPS request as a callback. The request body provides the main information of the callback in a JSON object. The JSON object contains different fields for different events.

The following is an example that shows the fields in the request body.
![](https://web-cdn.agora.io/docs-files/1567593635825)
- The fields in the red rectangle are the common fields of all the callback events. For details, see [Notification callback format](https://docs-preview.agoralab.co/en/Agora%20Platform/ncs#notification-callback-format).
- The fields in the blue rectangle are the common fields in `payload` of all the cloud recording events. For details, see [Fields in payload](#payload).
- The values of `eventType`, `serviceType`, and `details` depend on the event. For details, see [Callback events](#event).


### <a name="payload"></a>Fields in payload

`payload` is a JSON object, which is the main body of the notification. `payload` in each type of event notification includes the following fields:

- `cname`: String. The name of the channel to be recorded.
- `uid`: String. The user ID of the recording client.
- `sid`: String. The recording ID. The unique identifier of each recording.
- `sequence`: Number. The serial number of the notifications, starting from 0. You can use this parameter to identify notifications that are random, lost, or resent.
- `sendts`: Number. The time (UTC) when the event happens. Unix timestamp in ms.
- `serviceType`: Number. The type of Agora service.
  - `0`: The cloud recording service.
  - `1`: The recorder module.
  - `2`: The uploader module.
  - `4`: The extension services. 
  - `6`: The web page recording module.
  - `8`: The download module.
- `details`: JSON. The details of the callback events are described as follows. The message notification service may add new fields in `details` in the future. To ensure backward compatibility, the service will not change the data format of existing fields.

## Signature verification

<SignatureVerification />

For details on setting up a <Vg k="NCS" /> webhook server, see [Create your webhook](../../../video-calling/develop/receive-notifications#create-your-webhook).

## <a name="event"></a>Callback events

The related fields of the Agora Cloud Recording callback events are listed below:

| eventType | serviceType                   | Event description                                                                                                             |
| :-------- | :---------------------------- |:------------------------------------------------------------------------------------------------------------------------------|
| [1](#1)   | 0 (cloud recording service)   | An error occurs during the recording.                                                                                         |
| [2](#2)   | 0 (cloud recording service)   | A warning occurs during the recording.                                                                                        |
| [3](#3)   | 0 (cloud recording service)   | The status of the Agora Cloud Recording service changes.                                                                      |
| [4](#4)   | 0 (cloud recording service)   | The M3U8 playlist file is generated.                                                                                          |
| [11](#11)   | 0 (cloud recording service)   | The cloud recording service has ended its tasks and exited.                                                                   |
| [12](#12-session_failover)   | 0 (cloud recording service)   | The cloud recording service has enabled the [high availability mechanism](../../overview/product-overview).                   |
| [30](#30) | 2 (uploader module)           | The upload service starts.                                                                                                    |
| [31](#31-uploaded) | 2 (uploader module)           | All the recorded files are uploaded to the specified third-party cloud storage.                                               |
| [32](#32-backuped) | 2 (uploader module)           | All the recorded files are uploaded, but at least one file is uploaded to Agora Cloud Backup.                                 |
| [33](#33) | 2 (uploader module)           | The progress of uploading the recorded files to the cloud storage.                                                            |
| [40](#40) | 1 (recorder module)           | The recording starts.                                                                                                         |
| [41](#41) | 1 (recorder module)           | The recording exits.                                                                                                          |
| [42](#42) | 1 (recorder module)           | The recording service syncs the information of the recorded files.                                                            |
| [43](#43) | 1 (recorder module)           | The state of the audio stream changes.                                                                                        |
| [44](#44) | 1 (recorder module)           | The state of the video stream changes.                                                                                        |
| [45](#45) | 1 (recorder module)           | The screenshot is captured successfully.                                                                                      |
| [60](#60-vod_started) | 4 (extension services)           | The uploader for ApsaraVideo for VoD has started and successfully acquired the upload credential.                             |
| [61](#61-vod_triggered) | 4 (extension services)         | All recorded files have been uploaded to ApsaraVideo for VoD.                                                                 |
| [70](#70-web_recorder_started) | 6 (web page recording module) | Web page recording starts.                                                                                                    |
| [71](#71-web_recorder_stopped) | 6 (web page recording module) | Web page recording stops.                                                                                                     |
| [72](#72-web_recorder_capability_limit) | 6 (web page recording module) | The web page to record uses a feature that is unsupported by web page recording. The recording service will stop immediately. |
| [73](#73) | 6 (web page recording module) | The web page reloads.                                                                                                         |
| [90](#90) | 	8（download module） | The recording service fails to download the recorded files.                                                                   |
| [100](#100) | 	6（web page recording module） | The CDN streaming status of the web page recording changes.                                                                   |
| [1001](#1001) | 0 (cloud recording service) | The result of the transcoding.                                                                                                |

### <a name="1"></a>1 cloud_recording_error

`eventType` 1 indicates that an error occurs during the recording. `details` includes the following fields:

- `msgName`: String. The name of the message, `"cloud_recording_error"`.
- `module`: Number. The module in which the error occurs.
  - `0`: The recorder
  - `1`: The uploader
  - `2`: The Agora Cloud Recording Service
  - `6`：The Agora Web Page Recording Service
- `errorLevel`: Number. The error level.
  - `1`: Debug
  - `2`: Minor
  - `3`: Medium
  - `4`: Major
  - `5`: Fatal. A fatal error may cause the recording to exit. If you receive a message of this level, call `query` to check the current status and process the error according to the error notifications.
- `errorCode`: Number. The error code. 
  - If the error occurs in the recorder module (`0`), see [common errors](../common-errors).
  - If the error occurs in the uploader (`1`), see [upload error code](#uploaderr). 
  - If the error occurs in the Agora Cloud Recording Service (`2`), see [cloud recording service error code](#clouderr).
  - If the error occurs in the other modules, see [common errors](../common-errors).
  If you do not find any error code in the above-mentioned pages, contact our technical support.

- `stat`: Number. The event status. 0 indicates normal status; other values indicate abnormal status.
- `errorMsg`: String. The detailed description of the error.

### <a name="2"></a>2 cloud_recording_warning

`eventType` 2 indicates that a warning occurs during the recording. `details` includes the following fields:

- `msgName`: String. The message name, `cloud_recording_warning`.
- `module`: Number. The name of the module where the warning occurs.
  - `0`: The recorder.
  - `1`: The uploader.
- `warnCode`: Number. The warning code. 
  - If the warning occurs in the recorder, see [warning code](../../../on-premise-recording/reference/error-code#warning-codes).
  - If the warning occurs in the uploader, see [upload warning code](#uploadwarn).

### <a name="3"></a>3 cloud_recording_status_update

`eventType` 3 indicates that the method call fails because it does not match the status of the cloud recording service. For example, the method call of `start` fails if the service has already started. `details` includes the following fields:

- `msgName`: String. The message name, `cloud_recording_status_update`.
- `status`: Number. The status of the cloud recording service. See [Status codes for the Agora Cloud Recording service](#state) for details.
- `recordingMode`: Number. The recording mode:
	- `0`: Individual recording mode
	- `1`: Composite recording mode
- `fileList`: String. The name of the M3U8 index file generated by the service.

### <a name="4"></a>4 cloud_recording_file_infos

`eventType` 4 indicates that an M3U8 playlist file is generated and uploaded. During a recording, the recording service repeatedly uploads and overwrites the M3U8 file, but this event is triggered the first time the M3U8 file is generated and uploaded.

`details` includes the following fields:

- `msgName`: String. The message name, `cloud_recording_file_infos`.
- `fileList`: String. The name of the M3U8 file.


### <a name="11"></a>11 session_exit

`eventType` 11 indicates that the cloud recording service has ended its tasks and exited. `details` includes the following fields:

- `msgName`: String. The message name, `session_exit`.
- `exitStatus`: Number. The exit status. 
  - `0`: A normal exit, indicating that the recording service exits after the recording ends and the recorded files are uploaded.
  - `1`: An abnormal exit. An abnormal exist occurs when, for example, a parameter is incorrectly set.

### <a name="12"></a>12 session_failover

`eventType` 12 indicates that the cloud recording service has enabled the high availability mechanism, where the fault processing center automatically switches to a new server within 90 seconds to resume the service. `details` includes the following fields:

- `msgName`: String. The message name, `session_failover`.
- `newUid`: Number. A randomly-generated recording user ID. After the high availability mechanism is enabled and the service is switched to a new server, the service rejoins the channel with a randomly-generated recording user ID, abandoning the old one.

### <a name="30"></a>30 uploader_started

`eventType` 30 indicates that the upload service starts, and `details` includes the following fields:

- `msgName`: String. The message name, `uploader_started`.
- `status`: Number. The event status. 0 indicates normal status; other values indicate abnormal status.

### <a name="31"></a>31 uploaded

`eventType` 31 indicates that all the recorded files are uploaded to the specified third-party cloud storage, and `details` includes the following fields:

- `msgName`: String. The message name, `uploaded`.
- `status`: Number. The event status. 0 indicates normal status; other values indicate abnormal status.
- `fileList`: JSONArray. An array that contains detailed information of each recorded file. 
  - `fileName`: String. The name of the M3U8 file or MP4 file.
  - `trackType`: String. The type of the recorded file.
    - `"audio"`: Audio file.
    - `"video"`: Video file (no audio).
    - `"audio_and_video"`: Video file (with audio).
  - `uid`: String. The user ID. The user whose audio or video is recorded in the file. In composite recording mode, `uid` is `"0"`.
  - `mixedAllUser`: Boolean. Whether the audio and video of all users are combined into a single file.
    - `true`: All users are recorded in a single file.
    - `false`: Each user is recorded separately.
  - `isPlayable`: Boolean. Whether the file can be played online.
    - `true`: The file can be played online.
    - `false`: The file cannot be played online.
  - `sliceStartTime`: Number. The Unix time (ms) when the recording starts.

#### Example

- Individual recording:

```json
{
  "msgName": "uploaded",
  "fileList": [
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio",
      "uid": "57297",
      "mixedAllUser": false,
      "isPlayable": true,
      "sliceStartTime": 1619172871089
    },
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio",
      "uid": "10230",
      "mixedAllUser": false,
      "isPlayable": true,
      "sliceStartTime": 1619172871099
    }
  ],
  "status": 0
}
```

- Composite recording with no MP4 files generated:

```json
{
  "msgName": "uploaded",
  "fileList": [
    {
      "fileName": xxx.m3u8",
      "trackType": "audio_and_video",
      "uid": "0",
      "mixedAllUser": true,
      "isPlayable": true,
      "sliceStartTime": 1619170461821
    }
  ],
  "status": 0
}
```

- Composite recording with MP4 files generated:

```json
{
  "msgName": "uploaded",
  "fileList": [
    {
      "fileName": "xxx.mp4",
      "trackType": "audio_and_video",
      "uid": "0",
      "mixedAllUser": true,
      "isPlayable": true,
      "sliceStartTime": 1619172632080
    },
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio_and_video",
      "uid": "0",
      "mixedAllUser": true,
      "isPlayable": true,
      "sliceStartTime": 1619172632080
    }
  ],
  "status": 0
}
```

- Web page recording with MP4 files generated:

```json
{
  "msgName": "uploaded",
  "status": 0
}
```

### <a name="32"></a>32 backuped

`eventType` 32 indicates that all the recorded files are uploaded, but at least one of them is uploaded to Agora Cloud Backup. Agora Cloud Backup automatically uploads the files to the specified third-party cloud storage. `details` includes the following fields:

- `msgName`: String. The message name, `backuped`.
- `status`: Number. The event status. 0 indicates normal status; other values indicate abnormal status.
- `fileList`: JSONArray. An array that contains detailed information of each recorded file. 
  - `fileName`: String. The name of the M3U8 file or MP4 file.
  - `trackType`: String. The type of the recorded file.
    - `"audio"`: Audio file.
    - `"video"`: Video file (no audio).
    - `"audio_and_video"`: Video file (with audio).
  - `uid`: String. The user ID. The user whose audio or video is recorded in the file. In composite recording mode, `uid` is `"0"`.
  - `mixedAllUser`: Boolean. Whether the audio and video of all users are combined into a single file.
    - `true`: All users are recorded in a single file.
    - `false`: Each user is recorded separately.
  - `isPlayable`: Boolean. Whether the file can be played online.
    - `true`: The file can be played online.
    - `false`: The file cannot be played online.
  - `sliceStartTime`: Number. The Unix time (ms) when the recording starts.

#### Example

- Individual recording:

```json
{
  "msgName": "backuped",
  "fileList": [
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio",
      "uid": "57297",
      "mixedAllUser": false,
      "isPlayable": true,
      "sliceStartTime": 1619172871089
    },
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio",
      "uid": "10230",
      "mixedAllUser": false,
      "isPlayable": true,
      "sliceStartTime": 1619172871099
    }
  ],
  "status": 0
}
```

- Composite recording with no MP4 files generated:

```json
{
  "msgName": "backuped",
  "fileList": [
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio_and_video",
      "uid": "0",
      "mixedAllUser": true,
      "isPlayable": true,
      "sliceStartTime": 1619170461821
    }
  ],
  "status": 0
}
```

- Composite recording with MP4 files generated:

```json
{
  "msgName": "backuped",
  "fileList": [
    {
      "fileName": "xxx.mp4",
      "trackType": "audio_and_video",
      "uid": "0",
      "mixedAllUser": true,
      "isPlayable": true,
      "sliceStartTime": 1619172632080
    },
    {
      "fileName": "xxx.m3u8",
      "trackType": "audio_and_video",
      "uid": "0",
      "mixedAllUser": true,
      "isPlayable": true,
      "sliceStartTime": 1619172632080
    }
  ],
  "status": 0
}
```

- Web page recording with MP4 files generated:

```json
{
  "msgName": "backuped",
  "status": 0
}
```

### <a name="33"></a>33 uploading_progress

`eventType` 33 indicates the current upload progress. The Agora server notifies you of the upload progress once every minute after the recording starts. `details` includes the following fields:

- `msgName`: String. The message name, `uploading_progress`.
- `progress`: Number. An ever-increasing number between 0 and 10,000, equal to the ratio of the number of the uploaded files to the number of the recorded files multiplied by 10,000. After the recording service exits and when the number reaches 10,000, the upload completes.

### <a name="40"></a>40 recorder_started

`eventType` 40 indicates that the recording service starts, and `details` includes the following fields:

- `msgName`: String. The message name, `recorder_started`.
- `status`: Number. The event status. 0 indicates normal status; other values indicate abnormal status.

### <a name="41"></a>41 recorder_leave

`eventType` 41 indicates that the recorder leaves the channel, and `details` includes the following fields:

- `msgName`: String. The message name, `recorder_leave`.
- `leaveCode`: Number. The leave code. You can perform a bitwise AND operation on the code and each enum value, and those with non-zero results are the reason for the exit. For example, if you perform a bit-by-bit AND operation on code 6 (binary 110) and each enum value, only LEAVE_CODE_SIG (binary 10) and LEAVE_CODE_NO_USERS (binary 100) get a non-zero result. The reasons for exiting, in this case, include a timeout and a signal triggering the exit.
  | Enumerator              |                                                              |
  | :---------------------- | ------------------------------------------------------------ |
  | LEAVE_CODE_INIT         | 0: The initialization fails.                                 |
  | LEAVE_CODE_SIG          | 2 (binary 10): The AgoraCoreService process receives the SIGINT signal.  |
  | LEAVE_CODE_NO_USERS     | 4 (binary 100): The recording server automatically leaves the channel and stops recording because the channel has no user. |
  | LEAVE_CODE_TIMER_CATCH  | 8 (binary 1000): Ignore it.                                                |
  | LEAVE_CODE_CLIENT_LEAVE | 16 (binary 10000): The recording server calls the `leaveChannel` method to leave the channel. |

### <a name="42"></a>42 recorder_slice_start

`eventType` 42 indicates that the recording service syncs the information of the recorded files, and `details` includes the following fields:

- `msgName`: String. The message name, `recorder_slice_start`.
- `startUtcMs`：Number. The time (ms) in UTC when the recording starts (the starting time of the first slice file).
- `discontinueUtcMs`：Number. In most cases, this field is the same as `startUtcMs`. When the recording is interrupted, the Agora Cloud Recording service automatically resumes the recording and  triggers this event. In this case, the value of this field is the time (ms) in UTC when the last slice file stops.
- `mixedAllUser`:  Boolean. Whether the audio and video of all users are mixed into a single file.
  - `true`: All users are recorded in a single file.
  - `false`: Each user is recorded separately.
- `streamUid`: String. User ID. The user whose audio or video is recorded in the file. In composite mode, `streamUid` is `0`.
- `trackType`: String. Type of the recorded file.
  - `"audio"`: Audio file.
  - `"video"`: Video file (no audio).
  - `"audio_and_video"`: Video file (with audio).

For example, you start a recording session and get this event notification in which `startUtcMs` is the starting time of slice file 1. Then, the recording session continues and records slice file 2 to slice file N, during which the recording service does not send this notification again. If an error occurs when recording slice file N + 1, you lose this file and the recording session stops. Agora Cloud Recording automatically resumes the recording and triggers this event again. In the event notification, `startUtcMs` is the time when slice file N + 2 starts, and `discontinueUtcMs` is the time when slice file N stops.


### <a name="43"></a>43 recorder_audio_stream_state_changed

eventType 43 indicates that the state of the audio stream has changed, and `details` includes the following fields:

- `msgName`: String. The message name, `recorder_audio_stream_state_changed`.
- `streamUid`: String. The ID of the user whose audio is being recorded. In composite recording mode, `streamUid` can be `0`, which represents the combined stream of all or the specified user IDs.
- `state` : Number. Whether Agora Cloud Recording is receiving the audio stream.
  - `0`: Agora Cloud Recording is receiving the audio stream.
  - `1`: Agora Cloud Recording is not receiving the audio stream.
- `UtcMs`: Number. The UTC time (ms) when the state of the audio stream changes.



### <a name="44"></a>44 recorder_video_stream_state_changed

`eventType` 44 indicates that the state of the video stream has changed, and `details` includes the following fields:

- `msgName`: String. The message name, `recorder_video_stream_state_changed`.
- `streamUid`: String. The ID of the user whose video is being recorded. In composite recording mode, `streamUid` can be `0`, which represents the combined stream of all or the specified user IDs.
- `state`: Number. Whether Agora Cloud Recording is receiving the video stream.
  - `0`: Agora Cloud Recording is receiving the video stream.
  - `1`: Agora Cloud Recording is not receiving the video stream.
- `UtcMs`: Number. The UTC time (ms) when the state of the video stream changes.

<a name="45"></a>
### 45 recorder_snapshot_file

`eventType` 45 indicates that the screenshot is captured successfully and uploaded to the third-party cloud storage. The `details` includes the following fields:

- `msgName`: String. The message name, `"recorder_snapshot_file"`.
- `fileName`: String. The file name of the JPG file generated by the screenshot. The format is: `"fileName": "<fileNamePrefix>/<file name>"`.

> `fileNamePrefix` refers to the path of the screenshot files in the third-party cloud storage.

### <a name="60"></a>60 vod_started

`eventType` 60 indicates that the uploader for ApsaraVideo for VoD has started and successfully acquired the upload credential. `details` includes the following fields:

- `msgName`: String. The message name, `"vod_started"`.
- `aliVodInfo`: JSON. The information of the video to upload.  
  - `videoId`: String. The video ID.

### <a name="61"></a>61 vod_triggered

`eventType` 61 indicates that all recorded files have been uploaded to ApsaraVideo for VoD. `details` includes the following fields:

- `msgName`: String. The message name, `"vod_triggered"`.

### <a name="70"></a>70 web_recorder_started
`eventType` 70 indicates that web page recording starts. `details` includes the following field:
- `msgName`: String. The message name, `"web_recorder_started"`.
- `recorderStartTime`: Number. The time (UTC) when the recording starts. Unix timestamp in milliseconds.

### <a name="71"></a>71 web_recorder_stopped
`eventType` 71 indicates that web page recording stops. `details` includes the following field:
- `msgName`: String. The message name, `"web_recorder_stopped"`.
- `code`: Number. The error code. If the error code is not `0`, it means that the web page recording stopped abnormally.
- `message`: String. The error message, which indicates the reason why the recording stopped normally or abnormally.
- `details`: String. A specific description of the error message, which provides a more complete description of the reason why the recording stopped normally or abnormally. You can take corresponding measures based on the information.
- `fileList`: JSONArray. An array that contains detailed information of each recorded file.
  - `fileName`: String. The name of the M3U8 file or MP4 file.
  - `sliceStartTime`: Number. The Unix timestamp (ms) when the recording starts.

| Error Code | Message             | Description                                                  |
| :--------- | :------------------ | :----------------------------------------------------------- |
| `0`        | `ok`                  | Normal, the user stops the recording.                        |
| `1`          | `max_recording_hour`  | The recording time reaches the set maximum recording length (`maxRecordingHour`), which causes the recording to stop. |
| `2`          | `capability_limit`    | The web page to be recorded uses an unsupported function, causing the web page recording to stop. |
| `3`          | `start_engine_failed` | The recording engine failed to start, causing the web page recording to stop. |
| `4`          | `page_load_timeout`   | When you use the [web page load timeout detection](../../develop/webpage-load-timeout), the web page load timeout causes the web page recording to stop. |
| `5`          | `access_url_failed`   | An error occurred when opening the web page to be recorded, which causes the web page recording to stop. |
| `6`          | `recorder_error `     | The web page recording has an error and cannot continue, causing the web page recording to stop. |

#### Example
```json
{
  "msgName": "web_recorder_stopped",
  "code": 1,
  "message": "max_recording_hour",
  "details": "max recording hour is 4",
  "fileList": [
    {
      "filename": "test_p1627613634_www.m3u8",
      "sliceStartTime": 1627613641393
    },
    {
      "filename": "test_p1627613634_www_0.mp4",
      "sliceStartTime": 1627613641393
    }
  ]
}
```

### <a name="72"></a>72 web_recorder_capability_limit
`eventType` 72 indicates that the web page to record uses a feature that is unsupported by web page recording, and the recording service will stop immediately. `details` includes the following fields:
- `msgName`: String. The message name, `"web_recorder_capability_limit"`.
- `limitType`: String. The type of the feature that causes the failure.
  - `"resolution"`: The web page to record contains a video source with a resolution that exceeds 1280 × 720.
  - `"WebGL"`: The web page to record uses WebGL.
  - `"bandwidth"`：The upstream bandwidth exceeds 10 M, or the downstream bandwidth exceeds 1 G.

### <a name="73"></a>73 web_recorder_reload
`eventType` 73 indicates a web page reload. `details` includes the following fields:

- `msgName: `String. The message name, `"web_recorder_reload"`:
- `reason: `String. The reason for the page reload:
  - `"audio_silence"`: Audio loss issue.
  - `"page_load_timeout"`: Web page load timeout. The callback returns this field only if the web page load detection function is enabled and there is a web page load timeout. See [Web page load detection](../../develop/webpage-load-timeout).
 
### <a name="80"></a>80 transcoder_started

`eventType` 80 indicates that the transcoding starts, and `details` includes the following field:

   `msgName`: String. The message name, `"transcoder_started"`.

### <a name="81"></a>81 transcoder_completed

`eventType` 81 indicates that the transcoding completes, and `details` includes the following fields:

- `msgName`: String. The message name, `"transcoder_completed"`.

- `result`: String. The result of the transcoding.

  - `"all_success"`: Successfully transcodes all files.
  - `"partial_success"`: Fails to transcode some files.
  - `"fail"`: The transcoding fails.

- `uids`: JSONArray. The array contains the transcoding result and the name of the MP4 file of a specific user ID.
 - `uid`: String. The corresponding user ID of the MP4 file.
 - `result`: String. The result of transcoding.
   - `"success"`: Transcoding succeeds.
   - `"fail"`: Transcoding fails.
  - `fileList`: JSONArray. The array contains information about the MP4 file.
  - `fileName`: String. The name of the MP4 file. 

### <a name="90"></a>90 download_failed

`eventType` 90 indicates that the recording service fails to download the recorded files. This callback is triggered only once in the entire recording process, and `details` includes the following fields:

- `msgName`: String. The message name, `"download_failed"`.
- `vendor`: Number. The name of the third-party cloud storage service, which is the same as `vendor` in your `start` request.
- `region`: Number. The region of the third-party cloud storage, which is the same as region set in your `start` request.
- `bucket`: String. The bucket name of the third-party cloud storage, which is the same as `bucket` set in your `start` request.
- `fileName`: String. The list of M3U8 or TS/WebM files that fail to be downloaded. The file names are separated by `";"`.

### <a name="100"></a>100 rtmp_publish_status

`eventType` 100 indicates the CDN streaming status of the web page recording. `details` includes the following fields:

- `msgName`：String. The message name, `"rtmp_publish_status"`.
- `rtmpUrl`: String. The CDN address you want to the push the stream to.
- `status`: Number. The CDN streaming status of the web page recording, including the following options:
  - `"connecting"`: Connecting to the CDN server.
  - `"publishing"`: Pushing the stream to the CDN server.
  - `"onhold"`: Pause streaming.
  - `"disconnected"`: Failed to connect to the CDN server. Agora recommends that you change the CDN address.

### <a name="1001"></a>1001 postpone_transcode_final_result

`eventType` 1001 indicates the final transcoding result, and `details` includes the following fields:

- `msgName`: String. The message name, `"postpone_transcode_final_result"`.

- `result`: String. The final result of the transcoding.

  - `"total_success"`: Successfully transcodes all files.
  - `"partial_success"`: Fails to transcode some files.
  - `"failed"`: The transcoding fails.
- `fileList`: JSONArray. The array contains information about the generated MP4 files.
- `fileName`: String. The name of an individual MP4 file. 


## Reference

### <a name="uploaderr"></a>Error codes related to uploading

| Error code | Description                                                  |
| :--------- | :----------------------------------------------------------- |
| 32         | An error occurs in the configuration of the third-party cloud storage. |
| 47         | The recording file upload fails.                             |
| 51         | An error occurs when the uploader processes the recorded files. |

### <a name="uploadwarn"></a>Warning codes related to uploading

| Warning code | Description                                                  |
| :----------- | :----------------------------------------------------------- |
| 31           | The recording service re-uploads the slice file to the specified cloud storage.                   |
| 32           | The recording service re-uploads the slice file to Agora Cloud Backup.                            |

### <a name="clouderr"></a>Error codes for the Agora Cloud Recording service

| Error code | Description                                               |
| :--------- | :-------------------------------------------------------- |
| 50         | A timeout occurs in uploading the recorded files.         |
| 52         | A timeout occurs in starting the Cloud Recording Service. |

### <a name="state"></a>Status codes for the Agora Cloud Recording service

| Status code | Description                                                  |
| :---------- | :----------------------------------------------------------- |
| 0           | The recording has not started.                               |
| 1           | The initialization is complete.                              |
| 2           | The recorder is starting.                                    |
| 3           | The uploader is ready.                                       |
| 4           | The recorder is ready.                                       |
| 5           | The first recorded file is uploaded. After uploading the first file, the status is `5` when the recording is running. |
| 6           | The recording stops.                                         |
| 7           | The Agora Cloud Recording service stops.                     |
| 8           | The recording is ready to exit.                              |
| 20          | The recording exits abnormally.                              |


### What are the differences between the Message Notification Service and the query Method?

You can monitor the status of the cloud recording service either through the `query` method or by the Message Notification Service, to take action when required. Both options have pros and cons.

#### The query method

You can periodically call the `query` method to monitor the status of a cloud recording.

- Pros: Reliable, as the status is queried proactively.
- Cons:
  - Provides limited status information.
  - Requires an active query. You cannot query too often because of the Queries Per Second (QPS) limit, and thus it is not as real-time as the Message Notification Service.

If the reliability of the status of a cloud recording is a high priority, Agora strongly recommends using the `query` method.

#### Message Notification Service

You can use the Message Notification Service as a complementary option to monitor the recording service status. You need to configure an HTTP/HTTPS server to receive event notifications. 

- Pros: Real-time
- Cons:
  - The server passively receives messages, and the messages may get lost.
  - The confirmation message of the message delivery may get lost, causing the message to be resent. In such a case, you need to deduplicate the notifications.
  - The messages may not arrive in the correct order.

Best practice is that core apps do not rely on <Vg k="NCS_LONG" /> (<Vg k="NCS" />). If your apps already rely heavily on the Message Notification Service, Agora recommends that you contact [support@agora.io](mailto:support@agora.io) to enable the redundant message notification function, which doubles the received notifications and reduces the probability of message loss. Redundant message notification still cannot guarantee a 100% arrival rate.