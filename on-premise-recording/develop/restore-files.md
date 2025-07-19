---
title: 'Repair recorded files'
sidebar_position: 11
type: docs
description: >
  How to repair recorded files after the recording crashes.
---

If a recording session crashes, the generated MP4 file may be unplayable. To preserve recorded audio and video content, the <Vpd k="SDK" /> provides a recovery feature that lets you reconstruct the MP4 file from temporary H264 and AAC files.

## Implementation

This section shows how to enable recovery mode and regenerate MP4 files after a crash.

### Enable file recovery

To enable file recovery, set the `che.media_recorder_recover_files` parameter to `true` during `AgoraService` initialization:

<PlatformWrapper platform="linux-cpp">

```cpp
auto agoraParameter = service->getAgoraParameter();
agoraParameter->setBool("che.media_recorder_recover_files", true);
```
</PlatformWrapper>

<PlatformWrapper platform="linux-java">

```java
AgoraParameter parameter = agoraService.getAgoraParameter();
parameter.setBool("che.media_recorder_recover_files", true);
```
</PlatformWrapper>

### Understand file behavior

When file recovery is enabled, the SDK generates an MP4 file as well as two additional files, H264 and AAC—with the same base name. For example, if the output file is `storagePath/agoraRecording.mp4`, then `agoraRecording.mp4.h264` and `agoraRecording.mp4.aac` files are also generated in the same path.

- If the recording ends normally and the SDK triggers `onRecorderStateChanged` with `RECORDER_STATE_STOP` after `stopRecording` is called, the SDK deletes the H264 and AAC files automatically.

- If the recording crashes or exits unexpectedly, the SDK retains the H264 and AAC files for recovery.

### Regenerate the MP4 file

To regenerate a corrupted MP4 file, use [ffmpeg](https://ffmpeg.org/), a command-line tool for processing video and audio, to merge the retained files into a playable MP4.

<PlatformWrapper platform="linux-cpp">
```bash
ffmpeg -i video.h264 -i audio.aac -c:v copy -c:a copy output.mp4
```
</PlatformWrapper>

<PlatformWrapper platform="linux-java">
```bash
ffmpeg -i agoraRecording.mp4.h264 -i agoraRecording.mp4.aac -c:v copy -c:a copy output.mp4
```
</PlatformWrapper>

This command creates a new playable MP4 file using the video and audio data from the retained files.

## Reference

This section contains content that completes the information on this page, or points you to documentation that explains other aspects to this product.

### API references

- [`getAgoraParameter`](/on-premise-recording/api-references/agora-service#getagoraparameter)
- [`onRecorderStateChanged`](/on-premise-recording/api-references/agora-media-rtc-recorder-eventhandler#onrecorderstatechanged)
- [`stopRecording`](/on-premise-recording/api-references/agora-media-rtc-recorder#stoprecording)
