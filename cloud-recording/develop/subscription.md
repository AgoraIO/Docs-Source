---
title: "Set up subscription lists"
sidebar_position: 15
type: docs
platform_selector: false
description: >
  Create a whitelist or blacklist for audio and video subscriptions.
---

## Overview

By default, Agora Cloud Recording subscribes to all published audio and video streams in a channel. This feature enables you to create a whitelist or blacklist for audio and video subscriptions. You can also update the subscription lists during a cloud recording.

## Implementation

When the recording starts, set the parameters in [`start`](../reference/restful-api#start) to create subscription lists. During the recording, set the `streamSubscribe` parameter in [`update`](../reference/restful-api#update) to update the subscription lists.

If you set up a subscription list for audio, but not for video, then Agora Cloud Recording will not subscribe to any video streams. If you set up a subscription list for video, but not for audio, then Agora Cloud Recording will not subscribe to any audio streams.


### Set up the subscription list for audio streams

Use either of the following parameters to set up a subscription list for audio:

- `subscribeAudioUids`: Specify the users whose audio streams you want to subscribe to. The setting creates a whitelist for audio subscription.
- `unSubscribeAudioUids`: Specify the users whose audio streams you do not want to subscribe to. The setting creates a blacklist for audio subscription.

### Set up the subscription list for video streams

Use either of the following parameters to set up a subscription list for video:

- `subscribeVideoUids`: Specify the users whose video streams you want to subscribe to. The setting creates a whitelist for video subscription.
- `unSubscribeVideoUids`: Specify the users whose video streams you do not want to subscribe to. The setting creates a blacklist for video subscription.

## Example

Suppose that four users, whose user IDs are 111, 222, 333, and 444, are in a channel when the recording begins, and two more users with unknown user IDs join the channel during the recording. The following lists the typical scenarios and recommended settings:

| Scenarios                                                    | Recommended settings                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Subscribe to all audio and video streams.                    | You do not need to set up a subscription list.               |
| Subscribe to all audio streams and the video streams of 111 and 222. | `subscribeAudioUids: ["#allstream#"]` `subscribeVideoUids: ["111","222"]` |
| Subscribe to all audio streams and the video streams of all user IDs except 111 and 222. | `subscribeAudioUids: ["#allstream#"]` `unSubscribeVideoUids: ["111","222"]`The recording service records the audio streams of all user IDs and the video streams of 333, 444, and the other two unknown user IDs. |
| Subscribe to all audio streams but no video streams.         | `subscribeAudioUids: ["#allstream#"]` Setting `streamType` to `0` leads to the same result. |
| Subscribe to the audio streams of all user IDs except 222 and the video stream of 111. | `unSubscribeAudioUids: ["222"]` `subscribeVideoUids: ["111"]`The recording service records the audio streams of 111, 333, 444, and the other two unknown user IDs, and the video stream of 111. |

## Considerations

- Use `["#allstream#"]` to specify all user IDs in a channel.
- When `streamTypes` in `recordingConfig` is set to `0` (audio only), you cannot set `subscribeVideoUids` or `unSubscribeVideoUids`; when `streamTypes` in `recordingConfig` is set to `1` (video only), you cannot set `subscribeAudioUids` or `unSubscribeAudioUids`.
- The recording service only records the first 17 user IDs that join a channel. If a subscribed user ID leaves, then the recording service automatically subscribes to the 18th user ID that joined the channel.