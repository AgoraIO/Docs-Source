---
title: "Individual audio non-transcoding recording"
sidebar_position: 3
type: docs
platform_selector: false
description:
  Make an individual audio non-transcoding recording or postpone audio mixing
---


## Overview

When recording audio only (`streamTypes` is `0`) in [individual recording mode](../develop/individual-mode), you can choose whether to use transcoding recording or non-transcoding recording through simple parameter settings. The differences between the two are as follows:

|                                          | Individual Audio Recording                                   | Individual Audio Non-transcoding Recording                   |
| :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Whether to transcode when encoding audio | Yes.                                                         | No.                                                          |
| Audio profile                            | The sample rate, number of audio channels, and bitrate are fixed at 48 kHz, mono, and 48 Kbps, respectively. | The sample rate, number of audio channels, and bitrate are determined by the [AudioProfile](../reference/restful-api#transcodingconfig) configuration of the streaming sender. |
| Audio codec                              | LC-AAC.                                                      | Determined by the [AudioProfile](../reference/restful-api#transcodingconfig) configuration set by the streaming sender. |
| Recorded files                           | One M3U8 file and several TS files are generated per user ID. | The same as Individual transcoding recording. However, when the user calls `mute`, `disable`, or `leaveChannel`, the audio recording is stopped immediately, and there is no recorded data for silenced audio frames. |
| Player compatibility                     | Use a player that supports the HLS protocol to play recorded files. | The audio codec format is determined by the [AudioProfile](../reference/restful-api#transcodingconfig) configured by the streaming sender, and player compatibility varies by audio codec. |

If you need to get the mixed audio recording files of all users in the channel, you can enable the Postpone Audio Mixing function when starting the individual audio non-transcoding recording.

## Implement an Audio Individual non-transcoding Recording 

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
    "clientRequest":{
      "resourceExpiredHour": 24,
      "scene": 0
   }
}

```

### Start recording

To enable individual recording mode, set `mode` to `individual` when calling [`start`](../reference/restful-api#start). 

Configure the following parameters in `clientRequest` for Audio Individual non-transcoding Recording:

| Parameter                     | Description                                                  | Note                                  |
| :---------------------------- | :----------------------------------------------------------- | :------------------------------------ |
| [`token`](../reference/glossary#token)                       | String. The dynamic key used for the channel to record. | Required if the channel uses a token. |
| [`recordingConfig`](../reference/restful-api#recordingconfig)             | JSON. Configures stream subscription, transcoding, and the profile of the output audio and video. | Required.                             |
| [`recordingConfig.streamTypes`](../reference/restful-api#recordingconfig) | Number. The type of the media stream to subscribe to. Set this to `0` for Audio Individual non-transcoding Recording. | Required.                             |
| [`recordingConfig.streamMode`](../reference/restful-api#recordingconfig)  | String. The output mode of the media stream in individual mode. Set this to `original` for Audio Individual non-transcoding Recording. | Required.                             |
| [`storageConfig`](../reference/restful-api#storageconfig)               | JSON. Configures the third-party cloud storage.              | Required.                             |

#### An HTTP request example of `start`

- Request URL:

```html
https://http://api.agora.io//v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/individual/start
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
            "streamTypes": 0,
            "streamMode": "original",
            "channelType": 0,
            "subscribeAudioUids": [
                "123",
                "456"
            ],
            "subscribeUidGroup": 0
        },
        "storageConfig": {
            "accessKey": "xxxxx",
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



When the user who publishes the stream mutes or leaves the channel, the recording service immediately slices the audio file and stops recording.

### Stop recording

When a recording finishes, call [`stop`](../reference/restful-api#stop) to leave the channel and stop recording. To use Agora Cloud Recording again, you need to call the `acquire` method for a new resource ID.

#### An HTTP request example of `stop`

- The request URL is:

```html
http://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/individual/stop
```

- `Content-type` 为 `application/json;charset=utf-8`

- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest":{
      "resourceExpiredHour": 24,
      "scene": 0
   }
}
```

## Implement an Postpone Audio Mixing

If you want to get the mixed audio recording files of all users in the channel, you can enable the Postpone Audio Mixing function when starting an individual audio non-transcoding recording. After you enable this function, the recording service merges and transcodes the recording files of all user IDs in the specified channel within 24 hours after the recording ends to generate an MP3/M4A/AAC file, and then uploads the recording file to the third-party cloud storage you specify.

### Enable Postpone Audio Mixing

To enable individual recording mode, set `mode` to `individual` when calling [`start`](../reference/restful-api#start). 

Configure the following parameters in `clientRequest` for Postpone Audio Mixing:

| Parameter                          | Description                                                  | Note                                  |
| :--------------------------------- | :----------------------------------------------------------- | :------------------------------------ |
| [`token`](../reference/glossary#token)                            | String. The dynamic key used for the channel to record. | Required if the channel uses a token. |
| [`appsCollection`](../reference/restful-api#appscollection)                   | JSON. Configures how the application services are combined and applied. | Required.                             |
| [`appsCollection.combinationPolicy`](../reference/restful-api#appscollection) | String. The combination method of various Cloud Recording applications, set to `postpone_transcoding` for Postpone Audio Mixing。 | Required.                             |
| [`recordingConfig`](../reference/restful-api#recordingconfig)                  | JSON. Configures stream subscription, transcoding, and the profile of the output audio and video. | Required.                             |
| [`recordingConfig.streamTypes`](../reference/restful-api#recordingconfig)      | Number. The type of the media stream to subscribe to. Set this to `0` for Audio Individual non-transcoding Recording. | Required.                             |
| [`recordingConfig.streamMode`](../reference/restful-api#recordingconfig)       | String. The output mode of the media stream in individual mode. Set this to `original` for Audio Individual non-transcoding Recording. | Required.                             |
| [`transcodeOptions`](../reference/restful-api#transcodingconfig)                 | JSON. Configures how the Cloud Recording service transcode the recording files. It is applicable to Postpone Audio Mixing. | Required.                             |
| [`storageConfig`](../reference/restful-api#storageconfig)                    | JSON. Configures the third-party cloud storage.              | Required.                             |

#### An HTTP request example of `start`

- Request URL:

```html
https://http://api.agora.io//v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/individual/start
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
        "appsCollection": {
            "combinationPolicy": "postpone_transcoding"
        },
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 0,
            "streamMode": "original",
            "channelType": 0,
            "subscribeAudioUids": [
                "123",
                "456"
            ],
            "subscribeUidGroup": 0
        },
        "transcodeOptions": {
            "container": {
                "format": "m4a"
            },
            "transConfig": {
                "transMode": "audioMix"
            },
            "audio": {
                "sampleRate": "48000",
                "bitrate": "48000",
                "channels": "2"
            }
        },
        "storageConfig": {
            "accessKey": "xxxxx",
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

## Recorded files


 
For the naming rules of recorded files, see [Manage Recording Files](../develop/manage-files). You can play M3U8 
audio files, or you can use the <Link target="_blank" to="{{Global.CREC_FCS}}">Agora Format Converter Script</Link> to 
merge and convert all TS files of the specified user ID into one MP3/M4A/AAC audio file for playback. See [Merge Audio and Video Files after an Individual Recording](../develop/merge-files) for details.

If you enable Postpone Audio Mixing, you can also get the MP3/M4A/AAC file of all user IDs mixed in the channel within 24 hours after the Audio Individual non-transcoding Recording ends.

## Callback events
You can subscribe to the related callback events of the cloud recording service (`serviceType` is `0`) before you start an individual audio non-transcoding recording. For details, see [Callback Events](../reference/rest-api-overview#callback-events).