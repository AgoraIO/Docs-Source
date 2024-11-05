---
title: 'Record raw data'
sidebar_position: 7
type: docs
description: >
  How to record raw data using the On-Premise Recording SDK.
---

The Agora On-Premise Recording SDK supports raw audio and video data in individual recording mode, and only raw audio data in composite recording mode.

For details about configuring an on-premise recording in these modes, see [Individual Recording](../develop/individual-mode) and [Composite Recording](../develop/composite-mode).

## Get raw audio and video data from an individual recording session

Depending on whether you record by command line or by APIs, set the parameter according to the following table to get the raw audio and video data from an individual recording.

| Data type      | Command line                                                 | API settings                                                 |
| :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Raw audio data | <li>`--getAudioFrame 1`: AAC file</li><li>`--getAudioFrame 2`: PCM file</li> | <li>`decodeAudio = 1`: AAC file</li><li>`decodeAudio = 2`: PCM file</li> |
| Raw video data | <li>`--getVideoFrame 1`: H.264 file</li><li>`--getVideoFrame 2`: YUV frame file</li><li>`--getVideoFrame 3`: JPG frame file</li><li>`--getVideoFrame 4`: JPG file</li><li>`--getVideoFrame 5`: JPG file + MPEG-4 video file</li> | <li>`decodeVideo = 1`: H.264 file</li><li>`decodeVideo = 2`: YUV frame file</li><li>`decodeVideo = 3`: JPG frame file</li><li>`decodeVideo = 4`: JPG file</li><li>`decodeVideo = 5`: JPG file + MP4 video file</li> |

<Admonition type="info">
The Agora <Vg k="VSDK" /> for Web supports raw data in YUV format only, not in H.264 format.
</Admonition>

You can get the raw video data from the `videoFrameReceived` callback, and the raw audio data from `audioFrameReceived`.

## Get raw audio and video data from a composite recording session

The Agora On-Premise Recording SDK supports only raw audio data in composite recording mode. Depending on whether you record by command line or by APIs, set the parameter according to the following table to get the raw audio data in composite recording mode, storing it in a PCM file.

| Data type      | Command line                   | API settings                |
| :------------- | :----------------------------- | :-------------------------- |
| Raw audio data | `-- getAudioFrame 3`: PCM file | `decodeAudio = 3`：PCM file |

You can get the raw audio data from the `audioFrameReceived` callback.
