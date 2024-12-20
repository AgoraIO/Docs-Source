---
title: "Individual recording"
sidebar_position: 2
type: docs
platform_selector: false
description: >
  Use the Cloud Recording RESTful API to make an individual recording
---

This guide includes the key steps in using the Cloud Recording RESTful API to make an individual recording. For more information, see [Get started](../get-started/getstarted).

Agora Cloud Recording supports three recording modes:

-   Individual recording

-   Composite recording

-   Web page recording

In individual recording mode, the audio and video of each user ID in a channel are recorded in separate files.

Agora recommends that you use the standard mode when you start individual recording, and get audio and video files that can be played directly for each user IDs after the recording stops. For details, see [Start recording](#start-recording).

For example, if a channel has two users and you choose to record both audio and video, the files generated for standard mode of individual recording is shown in the following diagram:


![Image](/images/cloud-recording/individual-mode.svg)


## Implementation

### Get a resource ID

Before recording, call the [`acquire`](../reference/restful-api#acquire) method to apply for a resource ID.

#### An HTTP request example of `acquire`

-   Request URL:

  ```json
    https://api.agora.io/v1/apps/<yourappid>/cloud_recording/acquire
  ``` 
-   `Content-type`: `application/json;charset=utf-8`

-   `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

-   Request body:

  ```json
  {
      "cname": "https://xxxxx",
      "uid": "527841",
      "clientRequest": {
          "resourceExpiredHour": 24,
          "scene": 0
      }
  }
  ```

### Start recording

To enable individual recording mode, set `mode` to `individual` when calling [`start`](../reference/restful-api#start). Use `recordingConfig` to configure individual recording, and use `storageConfig` to configure your third-party cloud storage.

Agora recommends that you use the standard mode when you start recording, that is, set the `streamMode` field in the `recordingConfig` parameterto `standard` to generate combined audio and video files that can be played directly.

In individual recording mode, you can configure the following parameters in `clientRequest`:

| Parameter                                                                                       | Description                                                                                       | Note                                       |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------|
| [`token`](../reference/glossary#token)                                                     | String. The dynamic key used for the channel to record.                                           | JSON. Required if the channel uses a token |
| [`recordingConfig`](../reference/restful-api#recordingconfig)                   | JSON. Configures stream subscription, transcoding, and the profile of the output audio and video. | Required                                   |
| [`recordingConfig.streamMode`](../reference/restful-api#recordingconfig)        | String. The output mode of the media stream in individual recording mode.                         | Required                                   |
| [`recordingFileConfig`](../reference/restful-api#recordingfileconfig) | JSON. Configures the recorded files.                                                              | Optional                                   |
| [`storageConfig`](../reference/restful-api#storageconfig)                 | JSON. Configures the third-party cloud storage.                                                   | Required                                   |

#### An HTTP request example of `start`

-   Request URL:
  ```json
    https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/individual/start
  ```
-   `Content-type`: `application/json;charset=utf-8`

-   `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

-   Request body:

**Real-time recording for standard mode**

```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token if any>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 2,
            "channelType": 0,
            "videoStreamType": 0,
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

-   The request URL is:
  ```json
     http://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/individual/stop
  ```
-   `Content-type`: `application/json;charset=utf-8`

-   `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).


-   Request body:

  ```json
  {
      "cname": "httpClient463224",
      "uid": "527841",
      "clientRequest": {}
  }
  ```

## Recorded files

In individual recording mode, the audio and video profiles of the recorded file are as follows:

-   Audio profile: The sample rate is 48 kHz, and the bitrate and number of audio channels are the same as those of the original audio stream.

-   Video profile: The video profile of the recorded file is the same as that of the original video stream.


The recorded files vary according to the recorded content. See the table below.

| Recorded content                   | Settings                                                                                                              | Recorded files                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Audio only                         | Set [`streamTypes`](../reference/restful-api#recordingconfig) to `0`                                  | One M3U8 file and several TS files for each user ID. The TS files store the audio.                                                                                                                                                                                                                                                                       |
| Video only                         | Set [`streamTypes`](../reference/restful-api#recordingconfig) to `1`                                  | One M3U8 file and several TS/WebM files for each user ID. The TS/WebM files store the video.                                                                                                                                                                                                                                                             |
| Audio and video, and standard mode | Set [`streamTypes`](../reference/restful-api#recordingconfig) to `2` and `streamMode` to `standard`。 | One M3U8 audio index file, one M3U8 video index file, a combined M3U8 audio and video index file, multiple TS audio slice files and multiple TS video slice files are generated per user ID. If VP9 encoding is used on the web side, a combined MPD audio and video index file and multiple WebM video slice files are generated per user ID. |

For detailed information about the naming conventions of the recorded files, see [Manage Recorded Files](../develop/manage-files).

## Considerations

-   Use standard mode to record (set `streamMode` to `standard`), if you switch the native side to the web side (or vice versa) during the recording process, two combined audio and video index files in M3U8 format and MPD format are generated after recording, and the whole recording process cannot be played continuously.

-   The recording effects of Web SDK 4.x after disabling the video track are shown below:

| Publisher   | Ways to disable the video track                                                                                                                                    | Recording effects                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Web SDK 4.x | Call <Link target="_blank" to="{{global.API_REF_WEB_ROOT}}/interfaces/ilocaltrack.html#setenabled">setEnabled</Link> method | Displays the last frame on the user screen in this slice and does not continue to generate video slices. |


