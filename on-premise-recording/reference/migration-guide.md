---
title: 'Migration from SDK 3.x'
sidebar_position: 3
type: docs
description: >
  Sunset plans for Agora services.
---

The <Vg k="OPREC_SDK" /> 4.x is the latest version that enables audio and video recording during real-time interactions. For a complete list of features and applicable use cases, refer to the [Product Overview](/on-premise-recording/overview/product-overview).

This guide highlights the major changes introduced in version 4.x compared to version 3.x.

## Key improvements in 4.x

The <Vg k="OPREC_SDK" /> 4.x is built on top of the latest Agora RTC SDK 4.x. It provides significant improvements in compatibility, performance, and codec support.

### New capabilities

* Supports the latest Agora cloud agent
* Improved weak network resilience and adaptive feedback
* Compatible with new RTC SDK versions
* Supports subscription to peer H.265 and other codecs
* Easier maintenance and upgrades, as both RTC and <Vg k="OPREC_SDK" /> share the same RTC engine version

## Functionality changes

Version 4.x focuses on recording audio and video streams in the RTC channel and generating MP4 files.

### Deprecated features

The following features are not available in <Vg k="OPREC_SDK" /> 4.x. If needed, use the Agora RTC Server SDK:

* Access to raw audio and video (e.g., YUV or PCM data)
* Local screenshot capture
* Built-in cloud container deployment

<Admonition type="info" info="info">
The <Vg k="OPREC_SDK" /> 4.x is designed for developers to integrate and manage within their own server environments. It is **not** a cloud service or aPaaS offering.
</Admonition>

## Service behavior changes

Unlike the 3.x SDK, version 4.x does not include:

* Multi-process management
* Crash recovery mechanisms

You must implement service management and failover handling in your own infrastructure.

## API comparison

The following table compares key APIs between version 4.x and 3.x:

| Functional Module                     | 4.x                                                                                                                                                                                                           | 3.x                                                                                                      |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Create and initialize a recording instance | - `AgoraService`<br/> - `AgoraService.initialize`<br/> - `createAgoraMediaComponentFactory`<br/> - `createMediaRtcRecorder`<br/> - `AgoraMediaRtcRecorder.initialize`                                                 | `RecordingSDK`                                                                                           |
| Join a channel                       | `joinChannel`<br/>*If String UID is enabled, you can pass it directly without calling additional APIs*                                                                                                      |  - `createChannel`<br/> - `createChannelWithUserAccount`<br/> - `getUidByUserAccount`<br/> - `getUserAccountByUid`  |
| Implement subscription logic        | - `subscribeAllAudio`<br/> - `unsubscribeAllAudio`<br/> - `subscribeAllVideo`<br/> - `unsubscribeAllVideo`<br/> - `subscribeAudio`<br/> - `unsubscribeAudio`<br/> - `subscribeVideo`<br/> - `unsubscribeVideo`                  | Fields in `createRecordingConfig`:<br/> - `autoSubscribe`<br/> - `subscribeVideoUids`                          |
| Start or stop recording             | **Individual recording:**<br/> - `startSingleRecordingByUid`<br/> - `stopSingleRecordingByUid`<br/> - `setRecorderConfigByUid`<br/><br/>**Composite recording:**<br/> - `startRecording`<br/> - `stopRecording`<br/> - `setRecordingConfig`<br/>Use with `enableMix = true` when initializing |  - `startService`<br/> - `stopService`<br/>Use with `isMixingEnabled` in `RecordingConfig`                    |
| Watermark                           | - `enableAndUpdateVideoWatermarks`<br/> - `disableVideoWatermarks`<br/> - `enableAndUpdateVideoWatermarksByUid`<br/> - `disableVideoWatermarksByUid`                                 | `updateWatermarkConfigs`                                                                                               |

## Callback comparison

The following table compares key callbacks between version 4.x and 3.x:

| Function                                                   | 4.x                          | 3.x                               |
|------------------------------------------------------------|------------------------------|------------------------------------|
| Callback when a local user joins a channel                 | `onConnected`                | `onJoinChannelSuccess`             |
| The local user leaves the channel                          | `onDisconnected`             | `onLeaveChannel`                   |
| Callback when a local user joins a channel after reconnecting | `onReconnected`           | `onRejoinChannelSuccess`           |
| The remote user leaves the channel                         | `onUserLeft`                 | `onUserOffline`                    |
| Callback when the remote audio first frame is received     | `onFirstRemoteAudioDecoded`  | `onFirstRemoteAudioFrame`          |
| Callback when the remote user's audio status changes       | `onUserAudioStateChanged`    | `onRemoteAudioStreamStateChanged`  |
| Callback when the remote user's video status changes       | `onUserVideoStateChanged`    | `onRemoteVideoStreamStateChanged`  |
