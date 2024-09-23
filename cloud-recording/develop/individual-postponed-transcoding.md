---
title: "Individual recording with postponed transcoding"
sidebar_position: 3
type: docs
platform_selector: false
description:
  Make an individual audio recording with postponed transcoding
---

If the individual transcoding recording does not meet your business needs, you can set up postponed transcoding. When set, Cloud Recording transcodes the recording file to generate an MP4 file within 24 hours after recording (or within 48 hours in special cases) and uploads it to the third-party cloud storage you specify.

<Admonition type="caution" title="Note">In the postponed transcoding scenario, the recorded files are cached on the Agora edge server for no longer than 24 hours. If your business is sensitive to information security, carefully consider whether to use the postponed transcoding in view of data compliance. If you have any questions, contact [Agora technical support](mailtosupport@agora.io).</Admonition>

The request example is as follows:

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

Set up the following `clientRequest` configurations:

- Set the `appsCollection.combinationPolicy` field to `postpone_transcoding`.
- Set the `transcodeOptions.transConfig.transMode` field to `postponeTranscoding`.
- Set the field format as needed. For supported values, see the [API documentation](../reference/restful-api#transcodeoptions).