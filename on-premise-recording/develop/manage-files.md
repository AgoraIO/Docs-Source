---
title: 'Manage Recording Files'
sidebar_position: 8
type: docs
description: >
  How to manage the recording files.
---

After recording files using the On-premise recording SDK, the recorded files are stored on your Linux server. This page introduces how to manage these recorded files.

## Use the default directory structure 

Set the root directory of the recording files by the `recordFileRootDir` parameter and the sub-directory is generated automatically. 

For example, the path to a recorded MP4 file is `yyyymmdd/ChannelName_HHMMSS_MSUSNS/xxxx.mp4`: 

- `yyyymmdd`: The date when the SDK joins the channel. All files and directories on the same day are stored under this directory and the time zone is UTC+0.

- `ChannelName_HHMMSS_MSUSNS`: The recording files are stored in the directory created on the same date as the recording. The directory name contains a channel name and a timestamp (hour, minute, second, millisecond, microsecond, and nanosecond). The timestamp is the time when the server starts recording, and the time zone is UTC+0.

<Admonition type="info">
- For versions earlier than v2.3.0, the directory of the recording files is `ChannelName_HHMMSS`, named after the channel name and timestamp (hour, minute, and second).
- For v2.3.0 or later, the directory of the recording files is `ChannelName_HHMMSS_MSUSNS`, named after the channel name and timestamp (hour, minute, second, millisecond, microsecond, and nanosecond).
</Admonition>

## Customize the directory structure

To customize the directory structure, you need to create a configuration file in JSON format and specify the path of the configuration file through the `cfgFilePath` parameter.

Set the `Recording_Dir` parameter in the configuration file to customize the directory structure. For example: `{“Recording_Dir” : “<recording path>”}`. You cannot change the `Recording_Dir` parameter.

<Admonition type="info">
Agora does not recommend customizing the directory structure because if multiple recording instances use the same configuration parameter, the recording files of different recording instances are stored in the same directory and cannot be distinguished.
</Admonition>

## The recording files

| File | Description |
| --- | --- |
| UID_HHMMSSMS.aac | If you record on the Agora Native SDK, PC, or the Web, each uid has an AAC file containing the voice content. |
| UID_HHMMSSMS.mp4 | If you record on the Agora Native SDK or PC, each uid has an MPEG-4 file. If the user joins and leaves the channel multiple times, this uid can have multiple MPEG-4 files containing the video content. |
| UID_HHMMSSMS.webm | If you record on the Web, each uid has a WebM file. If the user joins and leaves the channel multiple times, this uid can have multiple WebM files containing the video content. |
| recording2-done.txt | This text file indicates that the recording in this channel has finished. |
| UID_HHMMSSMS.txt | This text file indicates the start and end time of each voice or video file and the related information, such as the video width and rotation. |


The recording files are stored on your server only, and Agora has no access to them. You are responsible for the protection and security of the recording files. Consult a security expert if necessary.

The `recording_sys.log` files under the same directory of the recording files list any exception or problem that occurred during recording.


