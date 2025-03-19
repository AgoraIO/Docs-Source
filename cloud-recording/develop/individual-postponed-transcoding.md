---
title: "Individual recording with postponed transcoding"
sidebar_position: 3
type: docs
platform_selector: false
description:
  Make an individual audio recording with postponed transcoding
---

Postponed transcoding generates a single MP4 file containing both audio and video, unlike individual recording, which produces separate audio and video files for each UID. With postponed transcoding, Cloud Recording processes the files within 24 hours (or 48 hours in special cases) after recording and uploads the MP4 file to your specified third-party cloud storage. This option is ideal for use-cases where combining audio and video streams into one file is preferred and immediate transcoding is unnecessary.

<Admonition type="caution" title="Note"> 
In postponed transcoding, recorded files are cached on Agora's edge server for up to 24 hours. If data security is important to your business, consider this when deciding whether to use postponed transcoding. For questions, contact [Agora technical support](mailto:support@agora.io). 
</Admonition>

## Implementation

To set up postponed transcoding, use the following `clientRequest` configuration:

- Set the `appsCollection.combinationPolicy` field to `postpone_transcoding`.
- Set the `transcodeOptions.transConfig.transMode` field to `postponeTranscoding`.
- Set the field format as needed. For supported values, see the [API documentation](../reference/restful-api#transcodeoptions).

The following request example shows how to enable postponed transcoding:

```json
{
  "cname": "httpClient463224",
  "uid": "527841",
  "clientRequest": {
    "token": "<token if any>",
    // highlight-start
    "appsCollection": {
      "combinationPolicy": "postpone_transcoding"
    },
    "transcodeOptions": {
      "container": {
        "format": "mp4"
      },
      "transConfig": {
        "transMode": "postponeTranscoding"
      }
    },
    // highlight-end
    "recordingConfig": {
      "channelType": 1,
      "streamTypes": 2,
      "streamMode": "default",
      "videoStreamType": 0,
      "maxIdleTime": 30,
      "subscribeAudioUids": [
        "123",
        "456"
      ],
      "subscribeVideoUids": [
        "123",
        "456"
      ],
      "subscribeUidGroup": 0
    },
    "recordingFileConfig": {
      "avFileType": [
        "hls"
      ]
    },
    "storageConfig": {
      "vendor": 2,
      "region": 3,
      "bucket": "xxxxx",
      "accessKey": "xxxxx",
      "secretKey": "xxxxx",
      "fileNamePrefix": [
        "directory1",
        "directory2"
      ]
    }
  }
}
```

