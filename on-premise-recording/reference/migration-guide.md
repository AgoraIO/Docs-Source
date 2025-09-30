---
title: 'Migration from SDK 3.x'
sidebar_position: 3
type: docs
description: >
  Sunset plans for Agora services.
---

The <Vpd k="SDK" /> 4.x is the latest version that enables audio and video recording during real-time interactions. For a complete list of features and applicable use cases, refer to the [Product Overview](/on-premise-recording/overview/product-overview).

This guide highlights the major changes introduced in version 4.x compared to version 3.x.

## Key improvements in 4.x

The <Vpd k="SDK" /> 4.x is built on top of the latest Agora RTC SDK 4.x. It provides significant improvements in compatibility, performance, and codec support.

### New capabilities

- Supports the latest Agora cloud agent
- Improved resilience in weak network conditions and adaptive feedback
- Compatibility with <Vg k="VSDK" /> 4.x and later
- Support for H.265 and other peer codecs
- Easier upgrades due to shared RTC engine between the RTC SDK and the recording SDK

## Functionality changes

Version 4.x focuses on recording audio and video streams in the RTC channel and generating MP4 files.

### Deprecated features

The following features are not available in SDK 4.x. If needed, use the Agora RTC Server SDK:

* Access to raw audio and video (For example, YUV or PCM data)
* Local screenshot capture
* Built-in cloud container deployment

<Admonition type="info" >
Version 4.x is designed for self-hosted deployment. It is not a cloud or aPaaS service.
</Admonition>

## Changes in service behavior

The following runtime behaviors from version 3.x have been removed in version 4.x:

- Multi-process service management
- Automatic crash recovery

You must implement service management and failover handling in your own infrastructure.

## API comparison

The following table compares key APIs between version 4.x and 3.x:

<PlatformWrapper platform="linux-java">

| Functional module        | 4.x        | 3.x           |
|--------------------------|------------|---------------|
| Create and initialize a recording instance | - `AgoraService`<br/> - `AgoraService.initialize`<br/> - `createAgoraMediaComponentFactory`<br/> - `createMediaRtcRecorder`<br/> - `AgoraMediaRtcRecorder.initialize`          | `RecordingSDK`|
| Join a channel          | `joinChannel`<br/>If the String UID function is enabled, you can directly use the String UID to pass parameters when calling `joinChannel`, without calling other APIs.           |  - `createChannel`<br/> - `createChannelWithUserAccount`<br/> - `getUidByUserAccount`<br/> - `getUserAccountByUid`  |
| Implement subscription logic        | - `subscribeAllAudio`<br/> - `unsubscribeAllAudio`<br/> - `subscribeAllVideo`<br/> - `unsubscribeAllVideo`<br/> - `subscribeAudio`<br/> - `unsubscribeAudio`<br/> - `subscribeVideo`<br/> - `unsubscribeVideo`     | The following fields of the `RecordingConfig` object in the `create` method:<br/> - `autoSubscribe`<br/> - `subscribeVideoUids` <br/> - `subscribeAudioUids`|
| Start or stop recording| **Individual recording:**<br/> - `startSingleRecordingByUid`<br/> - `stopSingleRecordingByUid`<br/> - `setRecorderConfigByUid`<br/><br/>**Composite recording:**<br/> - `startRecording`<br/> - `stopRecording`<br/> - `setRecordingConfig`<br/>Use with `enableMix` set to `true` when calling `initialize` |  - `startService`<br/> - `stopService`<br/>Use with `isMixingEnabled` in `RecordingConfig`       |
| Watermark | - `enableAndUpdateVideoWatermarks`<br/> - `disableVideoWatermarks`<br/> - `enableAndUpdateVideoWatermarksByUid`<br/> - `disableVideoWatermarksByUid`       | `updateWatermarkConfigs`    |

</PlatformWrapper>


<PlatformWrapper platform="linux-cpp">

| Functional module        | 4.x API | Older versions   |
|--------------------------|------------|---------------|
| Create and initialize a recording instance | - `createAgoraService`<br/>- `IAgoraService::initialize`<br/>- `createAgoraMediaComponentFactory`<br/>- `createMediaRtcRecorder`<br/>- `IAgoraMediaRtcRecorder::initialize` | `createAgoraRecordingEngine`                                                             |
| Join a channel                         | `joinChannel`<br/>If the String UID function is enabled, you can directly use the String UID to pass parameters when calling `joinChannel`, without calling other APIs.         | - `joinChannel`<br/>- `joinChannelWithUserAccount`<br/>- `getUserInfoByUserAccount`<br/>- `getUserInfoByUid` |
| Implement subscription logic           | - `subscribeAllAudio`<br/>- `unsubscribeAllAudio`<br/>- `subscribeAllVideo`<br/>- `unsubscribeAllVideo`<br/>- `subscribeAudio`<br/>- `unsubscribeAudio`<br/>- `subscribeVideo`<br/>- `unsubscribeVideo` | Use the following fields in `RecordingConfig` when calling `joinChannel`:<br/>- `autoSubscribe`<br/>- `subscribeVideoUids`<br/>- `subscribeAudioUids` |
| Start or stop recording                | **Individual recording:**<br/>- `startSingleRecordingByUid`<br/>- `stopSingleRecordingByUid`<br/>- `setRecorderConfigByUid`<br/><br/>**Composite recording:**<br/>- `startRecording`<br/>- `stopRecording`<br/>- `setRecordingConfig`<br/>Use with `enable_mix` set in `initialize` | - `startService`<br/>- `stopService`<br/>Use with `isMixingEnabled` in `RecordingConfig` |
| Watermark                              | - `enableAndUpdateVideoWatermarks`<br/>- `disableVideoWatermarks`<br/>- `enableAndUpdateVideoWatermarksByUid`<br/>- `disableVideoWatermarksByUid` | Use `updateWatermarkConfigs` with `wm_num` and `wm_configs` in `VideoMixingLayout`       |

</PlatformWrapper>

## Callback comparison

The following table compares key callbacks between version 4.x and 3.x:

| Event            | 4.x API | Older versions     |
|---------------------|-----|---------|
| Local user joins the channel              | `onConnected`                | `onJoinChannelSuccess`          |
| Local user leaves the channel             | `onDisconnected`             | `onLeaveChannel`                |
| Local user rejoins after reconnecting     | `onReconnected`              | `onRejoinChannelSuccess`        |
| Remote user leaves the channel            | `onUserLeft`                 | `onUserOffline`                 |
| First frame of remote audio is received   | `onFirstRemoteAudioDecoded`  | `onFirstRemoteAudioFrame`       |
| Remote user's audio state changes         | `onUserAudioStateChanged`    | `onRemoteAudioStreamStateChanged` |
| Remote user's video state changes         | `onUserVideoStateChanged`    | `onRemoteVideoStreamStateChanged` |

For more information, refer to the [API reference](/on-premise-recording/reference/api-reference).
