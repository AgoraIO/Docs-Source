---
title: 'Capture Screenshots'
sidebar_position: 5
type: docs
description: >
  How to record screenshots using the On-Premise Recording.
---

## Overview

This page shows how to capture screenshots by the command line. With screenshots, you can analyze and monitor the video contents to ensure that the contents are permissible.

Before proceeding, ensure that you have compiled the Agora Recorder Demo and know how to record a call by the command line. For more information, see [Record by Command Line](../get-started/record-cmd).

## Implementation

You can use the `getVideoFrame` parameter to set the format of the recording files. You can also use the `captureInterval` parameter to set the screen capture interval, which must be longer than one second and the default value is five seconds.

The following sections describe the `getVideoFrame` and `captureInterval` parameters in details.

<Admonition type="info">Currently, only capture screenshots in individual recording mode is supported. </Admonition>

### Set the format of the recording files

Use the `getVideoFrame` parameter to set the format of the recording files depending on your recording mode.

In individual recording mode (`isMixingEnabled` is set as 0), you can set the `getVideoFrame` parameter as 3, 4, or 5.

| Use case  | Settings |
| --- | --- |
| Only capture screenshots | <li>`-- getVideoFrame 3`: Capture video frames in the JPEG format.</li><li>`-- getVideoFrame 4`: Capture screenshots in the JPEG format.</li> |
| Capture screenshots while recording | `-- getVideoFrame 5`: <li>One video file in MP4 format and multiple screenshots in JPEG format for each UID that uses the Agora native SDK.</li><li>One video file in WebM or MP4 format and multiple screenshots in JPEG format for each UID that uses the Agora Web SDK.</li> |

### Set the screen capture interval

You can also use the `captureInterval` parameter to set the screen capture interval, which must be longer than one second and the default value is five seconds.

## Example

The following example shows how to capture screenshots in JPEG format in individual recording mode.

```
./recorder_local --appId <Your App ID> --channel <The name of the channel to be recorded> --uid 0 --appliteDir ~/Agora_Recording_SDK_for_Linux_FULL/bin --isVideoOnly 1 --getVideoFrame 4
```