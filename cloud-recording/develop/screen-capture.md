---
title: "Cloud-based screenshot upload"
sidebar_position: 11
type: docs
platform_selector: false
description: >
    The key steps in using the Cloud Recording RESTful API to take screenshots of a video stream.
---


You can use Cloud Recording RESTful API to take screenshots of a video stream in a channel and upload the screenshots to your third-party cloud storage.

The following two screenshot methods are supported:

- Take screenshots only.
- Capture screenshots and recording during a recording process. Agora only charges recording fees.

For pricing details, see [Pricing](../overview/pricing).
To implement client-side screen capture, see [Screenshot Upload](../../video-calling/enable-features/screenshot-upload).


## Implementation

### Get a resource ID

Before recording, call the [`acquire`](../reference/restful-api#acquire) method to apply for a resource ID.

#### An HTTP request example of `acquire`

- Request URL: 

    ```html
    https://api.agora.io/v1/apps/<yourappid>/cloud_recording/acquire
    ```
- `Content-type`: `application/json;charset=utf-8`
- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).
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

Set `mode` to `individual` when calling [`start`](../reference/restful-api#start) to enable [individual recording mode](../develop/individual-mode).

You cannot switch to a different recording mode once you start recording.

To capture screenshots, you need to configure the following parameters in `clientRequest`:

| Parameter         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Note                                                                                                                                                                                          |
| :---------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`token`](../reference/glossary#token)           | The dynamic key used for the channel to record.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Required if the channel uses a token                                                                                                                                                          |
| [`recordingConfig`](../reference/restful-api#recordingconfig) | Configures stream subscription, transcoding, and the profile of the output audio and video.                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                      |
| [`snapshotConfig`](../reference/restful-api#snapshotconfig)  | Configures the time interval between two successive screenshots and the file format of the screenshots. `snapshotConfig` includes the following fields:<li>`captureInterval`: (Optional) Integer. The time interval (in seconds) between two successive screenshots. captureInterval should be within the range [1, 3600]. The default value is `10`.</li><li>`fileType`: JSONArray. File format of the screenshots. fileType can only take ["jpg"], setting screenshots to the JPG format.</li> | Required                                                                                                                                                                                      |
| [`storageConfig`](../reference/restful-api#storageconfig)   | Configures the third-party cloud storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                      |
| [`recordingFileConfig`](../reference/restful-api#recordingfileconfig)   | Configurations for the recorded files.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | If you are recording and taking screenshots in a recording process, this parameter is required; if you are only taking screenshots in a recording process, you cannot fill in this parameter. |



#### An HTTP request example of `start`

- Request URL:
	
    ```html
    https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/individual/start
    ```

- `Content-type`: `application/json;charset=utf-8`
- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).
- Request body:

**Capture screenshots only**
    ```json
    {
        "uid": "527841",
        "cname": "httpClient463224",
        "clientRequest": {
            "token": "<token if any>",
            "recordingConfig": {
                "channelType": 1,
                "subscribeUidGroup": 0
            },
            "snapshotConfig": {
                "captureInterval": 5,
                "fileType": [
                    "jpg"
                ]
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

**Capture screenshots and recording**
    ```json
    {
        "uid": "527841",
        "cname": "httpClient463224",
        "clientRequest": {
            "token": "<token if any>",
            "recordingConfig": {
                "maxIdleTime": 30,
                "streamTypes": 1,
                "channelType": 0
            },
            "snapshotConfig": {
                "captureInterval": 5,
                "fileType": [
                    "jpg"
                ]
            },
            "recordingFileConfig": {
                "avFileType": [
                    "hls"
                ]
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


## Screenshot files

The naming convention of screenshot files is `<sid>_<cname>__uid_s_<uid>__uid_e_video_<utc>.jpg`, where

- `<sid> `is the recording ID.
- `<cname>` is the channel name.
- `<uid>` is the user ID.
- `<utc>` is the UTC time when the screenshot was generated. The time zone is UTC+0, and the timestamp consists of the year, month, day, hour, minute, second, and millisecond. For example, if `utc` is `20190611073246073`, the screenshot was generated on June 11, 2019, at 07:32:46.073 a.m.

The screenshot file format is determined by `fileType` you set in `start`. Currently only the JPG format is supported.

When [a cloud recording server is disconnected or the process killed](../overview/product-overview#features), the cloud recording service enables the high availability mechanism, where the fault processing center automatically switches to a new server within 90 seconds to resume the service. When the service enables the mechanism, the screenshot filenames are prepended with `bak<n>`, where `n` stands for the number of times the mechanism is enabled in a recording and starts off with `0`. Taking the filename `bak0_sid_channel1__uid_s_123__uid_e_video_20190611073246073.jpg` as an example, `bak0` indicates that this file was generated after the service enabled the high availability mechanism for the first time.

## Considerations

Pay attention to the following parameters as incorrect settings result in errors and failure to capture screenshots:

- In the URL of your request, you must set `mode` as `individual`.
- Do not set `recordingFileConfig`.
- `streamTypes` must be `1` or `2`.
- If you set `subscribeAudioUid`, you must also set `subscribeVideoUids`.

If a user stops sending video stream during a session, the Cloud Recording service stops taking screenshots until the stream resumes.
