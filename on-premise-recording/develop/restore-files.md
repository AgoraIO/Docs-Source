---
title: 'Repair recorded files'
sidebar_position: 11
type: docs
description: >
  How to repair recorded files after the recording crashes.
---

If the recording process crashes, the generated MP4 file may become unplayable. To help preserve recorded audio and video content, the Agora SDK provides a feature to recover corrupted files after a crash.

## Prerequisites

Before proceeding, integrate the <Vg k="OPREC_SDK" /> and complete the [Quickstart](/on-premise-recording/get-started/quickstart) guide to ensure basic recording functionality is in place.

## Implementation

This section guides you through the implementation of repairing the recorded files.

### Enable file recovery

During `AgoraService` initialization, enable file recovery mode by setting the following private parameter:

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

### Understand recoverable file behavior

When recovery mode is enabled, the SDK generates an MP4 file along with an H264 video file and an AAC audio file with the same base name in the same directory.

For example, if the recorded MP4 file is saved as:

```
storagePath/agoraRecording.mp4
```

Then the following additional files will also be generated in the same path:

```
agoraRecording.mp4.h264
agoraRecording.mp4.aac
```

* If the recording completes successfully (i.e., `stopRecording` is called and the `onRecorderStateChanged` callback is triggered with the status `RECORDER_STATE_STOP`), the SDK automatically deletes the H264 and AAC files.
* If the recording crashes or exits unexpectedly, the H264 and AAC files are retained.

### Regenerate the MP4 file

If the MP4 file is corrupted due to a crash, you can attempt to regenerate it using the retained H264 and AAC files. One common method is using `ffmpeg`:

<PlatformWrapper platform="linux-java">
```bash
ffmpeg -i agoraRecording.mp4.h264 -i agoraRecording.mp4.aac -c:v copy -c:a copy output.mp4
```
</PlatformWrapper>
<PlatformWrapper platform="linux-cpp">
```bash
ffmpeg -i video.h264 -i audio.aac -c:v copy -c:a copy output.mp4
```
</PlatformWrapper>

This command merges the video and audio files into a new playable MP4 file.
