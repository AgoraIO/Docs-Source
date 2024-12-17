---
title: "Composite recording"
sidebar_position: 5
type: docs
platform_selector: false
description: >
   Use the Cloud Recording RESTful API to make a composite recording.
---

Agora Cloud Recording supports three recording modes:

- Individual recording
- Composite recording
- Web page recording

In composite recording mode, the audio and video of multiple user IDs in a channel are recorded in a single file.

For example, if a channel has two users, and you choose to record both audio and video, Agora Cloud Recording generates files as shown in the following diagram:

![](/images/cloud-recording/composite-mode.svg)

The recording service generates one M3U8 file and multiple TS files. If you set `avFileType` as `["hls","mp4"]` when calling the [`start`](../reference/restful-api#start) method, the recording service also generates MP4 files, which include the audio and video of all users in the channel.

This guide explains how to implement composite recording using Cloud Recording REST API.

## Implementation

### Get a resource ID

Before recording, call the [`acquire`](../reference/restful-api#acquire) method to apply for a resource ID.

#### An HTTP request example of `acquire`

- Request URL: 

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/acquire
```

- `Content-type`: `application/json;charset=utf-8`
- `Authorization`: Basic authorization. For more information, see [Authenticate REST calls](../reference/restful-authentication).
- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {
        "resourceExpiredHour": 24,
        "scene": 0
    }
}
```

### Start recording

To enable composite recording mode, set `mode` to `mix` when calling  [`start`](../reference/restful-api#start). Use `recordingConfig` to configure composite recording, and use `storageConfig` to configure your third-party cloud storage.

You cannot switch to a different recording mode once you start recording.


In composite recording mode, you can configure the following parameters in `clientRequest`:

| Parameter             | Description                                                  | Note                                 |
| :-------------------- | :----------------------------------------------------------- | :----------------------------------- |
| [`token`](../reference/glossary#token)               | The dynamic key used for the channel to record. | Required if the channel uses a token |
| [`recordingConfig`](../reference/restful-api#recordingconfig)     | Configures stream subscription, transcoding, and the profile of the output audio and video. | Required                             |
| [`recordingFileConfig`](../reference/restful-api#recordingfileconfig) | Configures the recorded files.                               | Optional                             |
|  [`storageConfig`](../reference/restful-api#storageconfig)       | Configures the third-party cloud storage.                    | Required                             |

#### An HTTP request example of `start`

- Request URL:

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/mix/start
```

- `Content-type`: `application/json;charset=utf-8`
- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).
- Request body:

```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token if any>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 2,
            "audioProfile": 1,
            "channelType": 0,
            "videoStreamType": 0,
            "transcodingConfig": {
                "height": 640,
                "width": 360,
                "bitrate": 500,
                "fps": 15,
                "mixedVideoLayout": 1,
                "backgroundColor": "#FF0000"
            },
            "subscribeVideoUids": [
                "123",
                "456"
            ],
            "subscribeAudioUids": [
                "123",
                "456"
            ],
            "subscribeUidGroup": 0
        },
        "storageConfig": {
            "accessKey": "xxxxxxf",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

### Stop recording    

When a recording finishes, call [`stop`](../reference/restful-api#stop) to leave the channel and stop recording. To use Agora Cloud Recording again, you need to call the [`acquire`](../reference/restful-api#acquire) method for a new resource ID.

#### An HTTP request example of `stop`

- The request URL is: 

 ```html
 http://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/mix/stop
 ```
- `Content-type`: `application/json;charset=utf-8`

- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {}
}
```

## Recorded files

The content of the recorded files varies according to the setting of `streamTypes`. See the table below:

| Recorded content | Settings                           | Recorded files                                               |
| :--------------- | :--------------------------------- | :----------------------------------------------------------- |
| Audio only       | Set [`streamTypes`](../reference/restful-api#recordingconfig) as `0`           | One M3U8 file, several TS files, and one or more MP4 files if you set avFileType as `["hls","mp4"]`. The TS files and MP4 files store the audio. |
| Video only       | Set [`streamTypes`](../reference/restful-api#recordingconfig) as `1`           | One M3U8 file, several TS files, and one or more MP4 files if you set avFileType as `["hls","mp4"]`. The TS files and MP4 files store the video. |
| Audio and video  | Set [`streamTypes`](../reference/restful-api#recordingconfig) as `2` (default) | One M3U8 file, several TS files, and one or more MP4 files if you set avFileType as `["hls","mp4"]`. The TS files and MP4 files store the audio and video. |


For detailed information about the naming conventions of the recorded files, see [Manage Recorded Files](../develop/manage-files).

<a name="Considerations"></a>
## Considerations

A Web client and a Native client have different display strategies when they stop publishing streams or leave the channel. See the table below for details.
|Type of the publisher|The client unpublishes the local video stream (`unpublish`)|The client disables the video track (`muteVideo`/`setEnabled`)|The client leaves the channel|
|--- |--- |--- |--- |
|Native client|Displays the last frame of the video within 3.5 seconds.Displays the preset background image of the canvas or the user region after 3.5 seconds, see <a href = "./layout#set-the-background-color-or-background-image">Set the background image</a>; If a background image is not set, the last frame is displayed.|Displays the last frame of the video within 3.5 seconds.Displays the preset background image of the canvas or the user region after 3.5 seconds, see <a href="./layout#set-the-background-color-or-background-image">Set the background image</a>; If a background image is not set, the last frame is displayed.|Displays the background color of the canvas (`backgroundColor`).|
|Web client|For the Web SDK 4.x and later, the last frame of the video is displayed within 3.5 seconds.The preset background image of the canvas or the user region is displayed after 3.5 seconds, see <a href="./layout#set-the-background-color-or-background-image">Set the background image</a>. If a background image is not set, the last frame is displayed.|For the Web SDK 4.x and later, the last frame of the video is displayed within 3.5 seconds.The preset background image of the canvas or the user region is displayed after 3.5 seconds, <a href="./layout#set-the-background-color-or-background-image">Set the background image</a>. If a background image is not set, the last frame is displayed.|Displays the background color of the canvas (`backgroundColor`).|




