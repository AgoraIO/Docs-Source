---
title: "Synchronous playback"
sidebar_position: 14
type: docs
platform_selector: false
description: >
  Use the start timestamp of the recording, provided by Agora Cloud Recording, to achieve synchronized playbac
---

Synchronizing the playback of recorded files with other stream files, such as online whiteboards, courseware, or messages, is essential for recreating real-time scenarios in various applications. Whether you're building educational platforms, hosting virtual training sessions, conducting business presentations, or enabling collaborative teamwork, synchronized playback helps deliver a seamless and engaging user experience. This guide explains how to achieve synchronized playback using the start timestamp provided by Agora Cloud Recording.

## Prerequisites

To enable synchronized playback, you need a single file containing both audio and video. In individual recording mode, <Vpd k="NAME" /> records audio and video for each user ID separately. Use the audio and video merging script to combine audio and video into one file.

To ensure that the period when a user is absent is included and displayed as the last frame before the absence in the recorded files:
- Set `-m` to `1` 
- Do not set `-s`

For details, see [Merge Audio and Video Files](../develop/merge-files).

## Get the timestamp

Use the [Agora Cloud Recording RESTful API Callback Service](../reference/rest-api-overview) to acquire the start timestamp of the recording. The `startUtcMs` parameter in the `recorder_slice_start` event indicates the time when Agora Cloud Recording starts to record a user ID, or the start time of the first slice file for the user ID. `startUtcMs` is the UTC time in ms.

<Admonition type="info">
Contact [support@agora.io](http://support@agora.io) to enable the callback service. 
</Admonition>

You can also get the start timestamp by parsing the M3U8 file.

1. Get the M3U8 file

    Find the M3U8 file in the specified directory in the third-party cloud storage. You can identify the M3U8 file of a certain recording instance by its filename:
    
    - In composite recording mode, the name of the M3U8 file consists of the recording ID and the channel name, for example `sid_cname.m3u8`.
    - See [Manage Recorded Files](../develop/manage-files) for the detailed naming conventions of the M3U8 file in individual recording mode.

2. Get the timestamp by parsing the M3U8 file. You can find the start timestamp at the start of each M3U8 file. For example:

    ```
    #EXT-X-AGORA-TRACK-EVENT:EVENT=START,TRACK_TYPE=AUDIO,TIME=1568597779021
    ```

    Where: 
    - `TRACK_TYPE` indicates the type of the recording, `VIDEO` or `AUDIO`. 
    - `Time` is the UNIX timestamp (ms) when the recording starts for the user ID. 
    
    If the user leaves the channel and then rejoins it, there might be several timestamps in the M3U8 file. In this case, the first timestamp in the M3U8 file is the start time of the recording.

<Admonition type="info">
In individual mode, if the video stream and audio stream of a user ID start at different times, use the earlier of the two times as the start time of this recording instance.
</Admonition>

## Examples

### Individual mode

Suppose that four users, A, B, C, and D, join the same channel at different times. In individual mode, the recording generates two M3U8 files and several TS/WebM files for each user ID. After merging the audio and video by using the Audio & Video Merge script, each user ID has one MP4 file. Through the RESTful API callback service or by parsing the M3U8 file, you can get the start timestamp of each user ID. You can then synchronize the playback by playing the four MP4 files and other stream files on the same timeline.

### Composite mode

Suppose that four users, A, B, C, and D, join the same channel at different times. In composite mode, the recording generates one M3U8 file and several TS files, including the audio and video of all the users in the channel. Through the RESTful API callback service or by parsing the M3U8 file, you can get the start timestamp of this recording instance. You can then synchronize the playback by playing the TS file and other stream files on the same timeline.
