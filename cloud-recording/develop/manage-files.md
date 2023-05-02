---
title: "Manage recorded files"
sidebar_position: 11
type: docs
platform_selector: false
description: >
  Know the naming conventions of the recorded files, how to parse the information in the M3U8 file, and when slicing occurs
---

## Overview

Agora Cloud Recording generates M3U8 files, TS/WebM files, and MP4 files after a recording. To process the recorded files, such as [merging the audio and video files](../develop/merge-files), [convert recorded file format](../develop/convert-format) or [synchronizing the playback](../develop/playback) with other stream files, you need to know the naming conventions of the recorded files, how to parse the information in the M3U8 file, and when slicing occurs.

## Naming conventions

### Individual recording

The naming conventions of individual recording are as follows:

- M3U8 file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>.m3u8`
- TS file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>_utc.ts`
- WebM file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>_utc.webm`:

- `<sid> `is the recording ID.
- `<cname> `is the channel name.
- `<uid> `is the user ID.
- `<type> `is the file type (`audio` or `video`).
- `<utc> `is the UTC time when the slice file starts. The time zone is UTC+0, and the timestamp consists of the year, month, day, hour, minute, second, and millisecond. When `utc` is `20190611073246073`, for example, the slice file starts at 07:32:46.073 a.m., June 11, 2019.

For example, in the file name `sid713476478245_cnameagora__uid_s_123__uid_e_video_20190920125142485.ts`, `sid713476478245` is the recording ID, `cnameagora` is the channel name, `123` is the user ID, `video` is the file type, and the start time of the recording is 12:51:42.485 a.m., September 20, 2019.


### Individual audio non-transcoding recording

The naming conventions of [individual audio non-transcoding recording](../develop/individual-nontranscoding) are as follows:

The naming conventions of individual recording are as follows:

- M3U8 file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>.m3u8`
- TS file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>_utc.ts`

- `<sid> `is the recording ID.
- `<cname> `is the channel name.
- `<uid> `is the user ID.
- `<type> `is the file type (`audio`).
- `<utc> `is the UTC time when the slice file starts. The time zone is UTC+0, and the timestamp consists of the year, month, day, hour, minute, second, and millisecond. When `utc` is `20190611073246073`, for example, the slice file starts at 07:32:46.073 a.m., June 11, 2019.

### Individual audio non-transcoding recording and postpone audio mixing

The naming conventions of [postpone audio mixing](../develop/individual-nontranscoding#implement-an-postpone-audio-mixing) are as follows:

- M3U8 file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>.m3u8`
- TS file: `<sid>_<cname>__uid_s_<uid>__uid_e_<type>_utc.ts`
- MP3/M4A/AAC file: `<sid>_<cname>_<index>.mp3/m4a/aac`

- In individual audio non-transcoding recording, only M3U8 and TS files are generated and uploaded to the third-party cloud storage in real time.
- Only MP3/M4A/AAC files are generated after enabling postpone audio mixing and upload to the third-party cloud storage within 24 hours.

- `<sid> `is the recording ID.
- `<cname> `is the channel name.
- `<uid> `is the user ID.
- `<type> `is the file type (`audio`).
- `<utc> `is the UTC time when the slice file starts. The time zone is UTC+0, and the timestamp consists of the year, month, day, hour, minute, second, and millisecond. When `utc` is `20190611073246073`, for example, the slice file starts at 07:32:46.073 a.m., June 11, 2019.
- `<index>` is the index number of the MP3/M4A/AAC file. The index number of the first MP3/M4A/AAC file is `0`.

### Composite recording

In composite recording mode, the naming conventions are as follows:

- M3U8 files: `<sid>_<cname>.m3u8`
- TS files: `<sid>_<cname>_<utc>.ts`
- MP4 files: `<sid>_<cname>_<index>.mp4`

To get MP4 files, you must set `avFileType` as `["hls","mp4"]`.

The definitions of the fields in these file names are as follows:

- `<sid>` is the recording ID.
- `<cname>` is the channel name.
- `<utc>` is the starting time (UTC) of the TS file. The time zone is UTC+0. The timestamp consists of the year, month, day, hour, minute, second, and millisecond. For example, if `<utc>` is `20190611073246073`, the starting time of the TS file is 07:32:46.073 a.m., June 11, 2019.
- `<index>` is the index number of the MP4 file. The index number of the first MP4 file is `0`. The recording service automatically generates an additional MP4 file when the length of the current file reaches approximately two hours or the size of the file exceeds approximately 2 GB.

### Web page recording

In web page recording mode, the naming conventions are as follows:

- M3U8 files: `<sid>_<cname>.m3u8`
- TS files: `<sid>_<cname>_<utc>.ts`
- MP4 file:` <sid>_<cname>_<index>.mp4`

To generate an MP4 file, you need to add `mp4` in `avFileType`

Where:

- `<sid>` is the recording ID.
- `<cname>` is the value of `cname` you use in the `acquire` method.
- `<utc>` is the starting time (UTC) of the TS file. The time zone is UTC+0. The timestamp consists of the year, month, day, hour, minute, second, and millisecond. For example, if `<utc>` is `20190611073246073`, the starting time of the TS file is 07:32:46.073 a.m., June 11, 2019.
- `<index>` is the index number of the MP4 file. The index number of the first MP4 file is `0`. The recording service automatically generates a new MP4 file when the length of the current file reaches about two hours or the size of the file exceeds about 2 GB.

Because the file name does support special characters, any special characters in `cname`, including "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "_", ".", "=", "[", "]", "{", "}", "~", "|", ",", ";", ":", "?", "\<", and ">", are replaced with "-" in the recording's filename.

## Recorded files in abnormal conditions

### When uploading files to the third-party cloud storage fails

If Agora Cloud Recording fails to upload the recorded files to the third-party cloud storage, it transfers the files to the third-party cloud storage from the Agora Cloud Backup. In order not to overwrite the latest files, the transferred M3U8 file is appended with `_<tick>_<index>.m3u8`,

where:

- `<tick>` is related to the time when the index file is generated.
- `<index>` is the index of the M3U8 file. The first version to be transferred has an index of `0`. The higher the index, the newer the version of the file.

For example, in the filename `sid713476478245_cnameagora__uid_s_123__uid_e_video_22194679897_3.m3u8` as an example, the "`3`" at the end indicates that this is the fourth version of the M3U8 file.

> When you find transferred M3U8 file(s) in the third-party cloud storage, compare the M3U8 file with the highest index to the file without a suffix, and choose the larger file.

The cloud recording service does not append the suffix to the names of the TS/WebM files and the MP4 files.

### When a server is disconnected or the process killed

When [a cloud recording server is disconnected or the process killed](../overview/product-overview#features), the cloud recording service enables the high availability mechanism, where the fault processing center automatically switches to a new server within 90 seconds to resume the service. Each time the service enables the high availability mechanism, it creates a new M3U8 file, which contains the index information of the recorded slice files from the time when the service resumes. The file name is prepended with `bak<n>`, where `n` stands for the number of times the mechanism is enabled in a recording, starting with `0`.

For example, in the filename `bak0_sid713476478245_cnameagora.m3u8`, `bak0` indicates that this file is generated after the service enables the high availability mechanism for the first time.

After the cloud recording service enables the high availability mechanism, the names of the recorded TS/WebM files and the MP4 files are also prepended with `bak<n>`.

## File size
In an individual recording, the size of a recorded file depends on the audio and video bitrates of the media source and the duration of the recording. For example, if the audio bitrate is 48 Kbps, the video bitrate is 500 Kbps, and the recording lasts for 30 minutes (1800 seconds), the size of the recorded file is approximately (48 Kbps + 500 Kbps) * 1800 s = 986.4 Mbit, or 123.3 MB.

In a composite recording, the size of a recorded file depends on the audio and video bitrates of in the transcoding configurations and the duration of the recording. For example, if you set `audioProfile` as `1` (setting the audio bitrate as 128 Kbps) and `bitrate` as 800 (setting the video bitrate as 800 Kbps), and the recording lasts for 30 minutes (1800 seconds), the size of the recorded file is approximately (128 Kbps + 800 Kbps) * 1800 s = 1670.4 Mbit, or 208.8 MB.

## M3U8 fIle

The M3U8 file contains the file names of several slice files and descriptive symbols. The M3U8 file generated by Agora Cloud Recording has three descriptive symbols:

- `#EXT-X-AGORA-TRACK-EVENT:EVENT=<event>,TRACK_TYPE=<type>,TIME=<utc>`: The first slice file after a stream starts or restarts after an interruption has this descriptive symbol, which describes the state of the stream.
  - `EVENT`: Name of the event. Currently, `EVENT` can only be `START`, which means that the stream has started or restarted after an interruption.
  - `TRACK_TYPE`: The content of the slice file, `AUDIO` or `VIDEO`.
  - `TIME`: Time when the state of the stream changes. `TIME` is in UTC and the time zone is UTC+0.
- `#EXT-X-AGORA-ROTATE:WIDTH=<width>,HEIGHT=<height>,ROTATE=<rotate>,TIME=<utc>`: The first slice file after a video rotates has this descriptive symbol, which describes the details of the rotation. A slice file may have several such symbols.
  - `WIDTH`: Width of the video.
  - `HEIGHT`: Height of the video.
  - `ROTATE`: The degrees by which the video rotates anticlockwise. `ROTATE` can only be `0`, `90`, `180`, or `270`.
  - `TIME`: The time when the video rotates. `TIME` is in UTC and the time zone is UTC+0.
- `#EXTINF:<length>`: Length of the slice file in seconds.

For example:

```json
#EXT-X-AGORA-ROTATE:WIDTH=640,HEIGHT=480,ROTATE=90,TIME=20190920125142485
#EXT-X-AGORA-TRACK-EVENT:EVENT=START,TRACK_TYPE=VIDEO,TIME=20190920125142485
#EXTINF:6.332000
sid713476478245_cnameagora__uid_s_123__uid_e_video_20190920125142485.ts
```

The sample M3U8 file above contains the file name of a TS file and three descriptive symbols, which indicates that the TS file is the first slice file after the video stream starts or restarts after an interruption, the video rotates by 90 degrees anticlockwise, and the TS file lasts for 6.332 seconds.

The generated M3U8 file does not have a comma after `#EXTINF:&#60-vod_started;length&#62;`, and thus may cause some compatibility issues with certain players. You can set `privateParams` in `recordingConfig` in the [start](../reference/rest-api/start) request to automatically add the comma: `"recordingConfig": {"privateParams":"{\"correctEXTINF\":true}", ...}`.

## Slicing

### Video file slicing

Slicing occurs when any of the following conditions is met:

- When an I frame appears and the slice file reaches 15 seconds.
- The codec changes.
- The width or height of the video changes.
- The video stream is interrupted.
- When you set the browser to use H.264 codec for encoding, forced slicing occurs when the slice file reaches 5.5 minutes, or the file size is over 50 MB. After forced slicing, the first frame of the new slice file might not be an I frame, in which case the slice file cannot be decoded and played directly. For example, in the communication channel, sometimes only one I frame may appear in several hours. In such case, the first frame of the new slice file is probably not an I frame.

When you set the browser to use VP8 codec, Agora Cloud Recording will not force slicing the file.

### Audio file slicing

Slicing occurs when the slice file reaches 15 seconds.

## Sample M3U8 file for audio

```json
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-ALLOW-CACHE:YES
#EXT-X-TARGETDURATION:18
#EXT-X-DISCONTINUITY
#EXT-X-AGORA-TRACK-EVENT:EVENT=START,TRACK_TYPE=AUDIO,TIME=20190920125142289
#EXTINF:15.019000
sid713476478245_cnameagora__uid_s_123__uid_e_audio_20190920125142289.ts
#EXTINF:15.019000
sid713476478245_cnameagora__uid_s_123__uid_e_audio_20190920125157307.ts
#EXTINF:15.019000
sid713476478245_cnameagora__uid_s_123__uid_e_audio_20190920125212326.ts
#EXTINF:15.019000
sid713476478245_cnameagora__uid_s_123__uid_e_audio_20190920125227345.ts
#EXTINF:12.523000
sid713476478245_cnameagora__uid_s_123__uid_e_audio_20190920125242363.ts
#EXT-X-ENDLIST
```

## Sample M3U8 file for video

```json
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-ALLOW-CACHE:YES
#EXT-X-TARGETDURATION:34
#EXT-X-DISCONTINUITY
#EXT-X-AGORA-ROTATE:WIDTH=640,HEIGHT=480,ROTATE=0,TIME=20190920125142485
#EXT-X-AGORA-TRACK-EVENT:EVENT=START,TRACK_TYPE=VIDEO,TIME=20190920125142485
#EXTINF:6.332000
sid713476478245_cnameagora__uid_s_123__uid_e_video_20190920125142485.ts
#EXT-X-AGORA-ROTATE:WIDTH=1280,HEIGHT=720,ROTATE=0,TIME=20190920125149174
#EXT-X-DISCONTINUITY
#EXTINF:17.442000
sid713476478245_cnameagora__uid_s_123__uid_e_video_20190920125149174.ts
#EXT-X-DISCONTINUITY
#EXT-X-AGORA-ROTATE:WIDTH=640,HEIGHT=480,ROTATE=0,TIME=20190920125206616
#EXTINF:33.326000
sid713476478245_cnameagora__uid_s_123__uid_e_video_20190920125206616.ts
#EXT-X-DISCONTINUITY
#EXT-X-AGORA-ROTATE:WIDTH=1280,HEIGHT=720,ROTATE=0,TIME=20190920125239942
#EXTINF:14.815000
sid713476478245_cnameagora__uid_s_123__uid_e_video_20190920125239942.ts
#EXT-X-ENDLIST
```
