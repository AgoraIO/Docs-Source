---
title: "Merge audio and video files"
sidebar_position: 4
type: docs
platform_selector: false
description: >
  Merge each user's audio and video files into one file.
---

In individual recording mode, Agora Cloud Recording generates one audio and/or video file for each user ID. If you want to merge each user ID's audio and video files into one file, you can use Agora Format Converter Script.

## Prerequisites

- Recommended systems for transcoding:
  - Ubuntu 14.04+ x64
  - CentOS 7.0+ x64
  - Debian 8.0 +

- Python 2, version 2.7 or later (Except Python 3)

### File preparation

- Use Agora Cloud Recording to generate the audio and/or video files. The transcoding will fail if any of the recorded files is missing.
- Ensure that the recorded files are stored in an accessible directory.

## Transcoding steps

### Get the Agora Format Converter Script

Download the <Link target="_blank" to="{{Global.CREC_FCS}}">Agora Format Converter Script</Link> and decompress it. Find `ffmpeg.tar.gz` and `convert.py`. Decompress `ffmpeg.tar.gz`, and make sure it is in the same directory as `convert.py.`

To avoid compatibility issues, Agora suggests that you use the FFmpeg binary in the zipped file or install FFmpeg 3.3.

### Execute the Agora Format Converter Script

You can start transcoding the files after you set the parameters.

#### Transcoding options

You can get the options with the `python convert.py` command.

![](https://web-cdn.agora.io/docs-files/1630915918701)

 Or you can refer to the following table to learn about the transcoding options:

| Option | Description     | Required or not |
| :----- |:----------| :-------------- |
| `-f`   | Specify the directory of the recorded files to be transcoded. If the directory contains files generated during several recording instances, the Agora Format Converter Script transcodes all the files by the order of the recording instances.     | YES             |
| `-m`   | Set the transcoding mode: See [-m options](#-m) for details.`0`: (Default) Merge the audio and video files of the same user ID based on the recording segment.`1`: Merge the audio and video files of the same user ID into one file.`2`: Merge the audio files of the same user ID into one audio file.`3`: Merge the video files of the same user ID into one video file (no audio).   | NO              |
| `-s`   | Set whether or not to include the period when a user is absent from a channel. If you do not set `-s`, which is the default mode, then if a user leaves the channel and rejoins it later, the period when the user is absent is included and displayed as the last frame before the user leaves. For example, if a user is in the channel for 2 minutes, then leaves the channel for 30 minutes, and rejoins the channel for another 2 minutes for a total recording time of 34 minutes, the recording will display the last frame before the user leaves for 30 minutes. If you set `-s`, then if a user leaves the channel and rejoins it later, the recording will not include the period when the user is absent. Do not set this parameter when `-m` is `0`. | NO              |
| `-p`   | Set the frame rate of the transcoded video. The default rate is 15 fps. The value range is from 5 fps to 120 fps. If `-p` is less than 5 fps, the video will be transcoded with the frame rate of 5 fps. For more details, see [How do I set the video profile of the recorded video?](../develop/recording-video-profile)      | NO              |
| `-r`   | Set the resolution of the transcoded video in the format of “width height”, for example, `-r 640 360`. For more details, see [How do I set the video profile of the recorded video?](../develop/recording-video-profile)         | NO              |
| `-a`     | While transcoding audio and video, generate the user's audio file, the file name format is: `user ID_timestamp.m4a`.              | NO              |
| `-c`     | Set the screenshot interval (millisecond), the generated file name format: `user ID_timestamp_index.jpg`.      | NO              |
| `-u`     | Specify the user ID to be transcoded; if not specified, all user IDs in the folder are transcoded.             | NO              |
| `-b`     | Specify the transcoding start timestamp. The unit is seconds and supports floating point numbers. For example `-b 10.500` means starting from 10 seconds and 500 milliseconds.             | NO              |
| `-t`     | Specify the length of time to be intercepted. This option must used with `-b` ; it cannot be used alone. For example, `-b 10 -t 5` means to intercept 5 seconds of data from the 10th second.                 | NO              |
| `-o`     | Specify the output file name, and only generate the specified file name when `-u` is valid; if not specified, generate the default file name.        | NO              |
| `-e`     | Transcode the recorded ts file into a standard format ts file, and output the MP4/M4A file with the same name. | NO              |

### <a name="-m"></a>-m options

Before introducing the `-m` options, we'll first explain the concept of a recording segment. A recording segment starts when Agora Cloud Recording starts recording a user ID and ends when Agora Cloud Recording stops recording a user ID.

Agora Cloud Recording starts recording a user ID only when all the following conditions are met:

- The user ID joins the channel and starts sending audio or video streams.
- You start Agora Cloud Recording

Agora Cloud Recording stops recording a user ID as long as one of the following conditions is met:

- The user ID stops sending streams and does not send streams again within 15 seconds
- The user ID leaves the channel and does not rejoin within 15 seconds
- You stop Agora Cloud Recording

See [Example](#example) for more information about the recording segment. 

Now, let's see the behaviors of different `-m` options:

It is assumed that each user ID in the channel generates several audio files and video files.

- `0`: Merge the audio and video files of the same user ID based on the recording segment. One recording segment of one user ID corresponds to one merged file, named as `user ID_timestamp_av.mp4`. In the filename, `timestamp` is the time when Agora Cloud Recording starts recording. If Agora Cloud Recording starts to record the audio and video at different times, `timestamp` is the earlier one of the two starting times. The time zone of `timestamp` is UTC+0. The `timestamp` parameter consists of the year, month, day, hour, minute, second, and millisecond. For example, `100_20190611073246073_av.mp4` is a merged file for user ID 100 and the start time of the recording is 07:32:46.073 a.m., June 11, 2019.
- `1`: Merge the audio and video files of the same user ID into one file. One user ID corresponds to one file, named as `user ID_0_merge_av.mp4`.
- `2`: Merge the audio files of the same user ID into one audio file. One user ID corresponds to one file, named as `user ID_0_merge.m4a`. The file uses AAC encoding. You can use the Agora Format Converter Script to transcode the file to other formats, such as MP3, see [Convert steps](../develop/convert-format#convert-steps) for details.
- `3`: Merge the video files of the same user ID into one video file (no audio). One user ID corresponds to one file, named as `user ID_0_merge.mp4`.

- If the transcoding mode is `-m 0`, and the `-b` parameter and `-t` parameter are used, the `-m` parameter is forced to 1, and the slice transcoding configuration is invalid. 
- If the `-b` parameter and `-t` parameter are used, the time period is added to the file name after transcoding. For example: The file name of `python convert.py -f <path of the file to be transcoded> -m 1 -b 10.5 -t 5.5`  is convertered to `123_0_merge_10.500_5.500_av.mp4` after transcoding.
- Switching between different [AudioProfile](../reference/restful-api#transcodingconfig) configuration at the streaming sender during a recording is not supported.

### <a name="example"></a>Example

The following examples show different merged files with different `-m` settings.

Suppose that two users, with user IDs 100 and 125, stay in the channel, and you start Agora Cloud Recording in individual recording mode. user ID 100 leaves the channel and rejoins the channel in 30 seconds, thus causing two segments in this recording instance. When the recording ends, user ID 100 has four recorded files: one audio file and one video file for each of the two segments. user ID 123 has one audio file and one video file.

To merge the audio and video files of the same user ID into one file, use the following command:

```
python convert.py -f <directory of the files to be transcoded> -m 1 -s -p 30 -r 640 360
```

Two files are generated after transcoding: `100_0_merge_av.mp4` and `123_0_merge_av.mp4`. The 30 seconds when user ID 100 is absent is not included in the merged file. To include the time interval, do not set `-s`.

To merge the audio and video files of the same user ID based on the recording segment, use the following command:

```
python convert.py -f <directory of the files to be transcoded> -m 0 -p 30 -r 640 360
```

Three files are generated after transcoding: `100_timestamp1_av.mp4`, `100_timestamp2_av.mp4`, and `123_timestamp1_av.mp4`.

A `convert-done.txt` file is generated after the transcoding is complete. Once the Agora Format Converter Script is used, a `convert.log` file is generated in the same directory as the audio and video files upon completion of the transcoding.

The transcoded MP4 file supports most mainstream media players. See the following table for details:

| Operating System | Media Players          |
| :--------------- | :--- |
| Linux            | <li>VLC</li><li>ffplayer</li>            |
| Windows          | <li>Media Player</li><li>KM Player</li><li>VLC Player</li><li>Chrome (49.0.2623 or later)</li>   |
| macOS            | <li>QuickTime Player</li><li>Movist</li><li>MPlayerX</li><li>Chrome (49.0.2623 or later)</li><li>Safari (11.0.3 or later)</li> |
| iOS              | <li>iOS default player</li><li>KMPlayer</li><li>Safari (9.0 or later)</li>              |
| Android          | <li>Android default player</li><li>MXPlayer</li><li>VLC</li><li>KMPlayer</li><li>Chrome (9.0.2623 or later)</li> |