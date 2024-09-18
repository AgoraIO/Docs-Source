---
title: "Synchronous playback"
sidebar_position: 14
type: docs
platform_selector: false
description: >
  Use the start timestamp of the recording, provided by Agora Cloud Recording, to achieve synchronized playbac
---

## Overview

Many educational apps need to synchronize the playback of recorded files and other stream files, such as online whiteboards, courseware, and messages, to recreate real-time classroom scenarios. You can use the start timestamp of the recording, provided by Agora Cloud Recording, to achieve synchronized playback.

## Prerequisites

In individual recording mode, Agora Cloud Recording records the audio and video of each user ID separately. Before you start, you need to first merge the audio and video into one file with the Audio & Video Merging script. See [Merge Audio and Video Files](../develop/merge-files) for details. Ensure that you set `-m` as `1` and do not set `-s`, so that the period when a user is absent will be included and displayed as the last frame before the absence in the recorded files.

## Get the timestamp

You can use the [Agora Cloud Recording RESTful API Callback Service](../reference/rest-api-overview) to acquire the start timestamp of the recording. The `startUtcMs` parameter in the `recorder_slice_start` event indicates the time when Agora Cloud Recording starts to record a user ID, or the start time of the first slice file for the user ID. `startUtcMs` is the time (ms) in UTC.

> Contact [support@agora.io](http://support@agora.io) to enable the callback service. 


You can also get the start timestamp by parsing the M3U8 file.

1. Get the M3U8 file: Find the M3U8 file in the specified directory in the third-party cloud storage. You can find the M3U8 file of a certain recording instance by its filename:
  - In composite recording mode, the name of the M3U8 file consists of the recording ID and the channel name, that is, `sid_cname.m3u8`.
  - See [Manage Recorded Files](../develop/manage-files) for the detailed naming conventions of the M3U8 file in individual recording mode.
2. Get the timestamp by parsing the M3U8 file. You can find the start timestamp at the start of each M3U8 file:
```
#EXT-X-AGORA-TRACK-EVENT:EVENT=START,TRACK_TYPE=AUDIO,TIME=1568597779021
```
   
  `TRACK_TYPE` indicates the type of the recording (`VIDEO` or `AUDIO`), `Time` is the time when the recording starts for the user ID,  and is a UNIX timestamp (ms). If the user leaves the channel and then rejoins it, there might be several timestamps in the M3U8 file. In this circumstance, the first timestamp in the M3U8 file is the start time of the recording.

> In individual mode, if the video stream and audio stream of a user ID start at different times, use the earlier of the two times as the start time of this recording instance.

## Example

### Individual mode

Suppose that four users, A, B, C, and D, join the same channel at different times. In individual mode, the recording generates two M3U8 files and several TS/WebM files for each user ID. After merging the audio and video by using the Audio & Video Merge script, each user ID has one MP4 file. Through the RESTful API callback service or by parsing the M3U8 file, you can get the start timestamp of each user ID. You can then synchronize the playback by playing the four MP4 files and other stream files on the same timeline.


### Composite mode

Suppose that four users, A, B, C, and D, join the same channel at different times. In composite mode, the recording generates one M3U8 file and several TS files, including the audio and video of all the users in the channel. Through the RESTful API callback service or by parsing the M3U8 file, you can get the start timestamp of this recording instance. You can then synchronize the playback by playing the TS file and other stream files on the same timeline.