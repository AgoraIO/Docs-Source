---
title: "API overview"
sidebar_position: 1
type: docs
platform_selector: false
description:
  Detailed help for Cloud Recording API.
---

Before proceeding, we recommend you take a quick look at the key features of Cloud Recording.

- [Individual recording](../../develop/individual-mode): Records the audio and video of each user ID in separate files and uploads the recorded files to a third-party cloud storage service.
- [Composite recording](../../develop/composite-mode): Records the audio and video of multiple user IDs in a single file and uploads the recorded file to a third-party cloud storage service.
- [Capture screenshots](../../develop/screen-capture): In individual recording mode, takes screenshots of the video stream and uploads the screenshots to a third-party cloud storage service.
- [Web page recording](../../develop/webpage-mode): Records the content and the audio of a specified web page in a single file and uploads the recorded file to a third-party cloud storage service.

Cloud Recording does not support finishing two tasks in one recording session. For example, if you want to record the video and audio of a channel and the content of a web page at the same time, you must start two recording sessions. More specifically, you must get two `resource ID`s by using two different `uid`s to call `acquire` twice, one for individual or composite recording and the other for web page recording. Please note that both sessions are charged.

## Prerequisites

- Ensure that the cloud recording service has been activated. See [Quickstart](../../get-started/getstarted#project-setup).
- The RESTful APIs only support HTTPS. Before using the Agora RESTful API, you need to pass the [basic HTTP authentication](../restful-authentication).

## Data format

All requests are sent to the host: `api.agora.io`.

- Request: See the examples in the APIs.
- Response: The response content is in JSON format.

<div class="alert warning">All the request URLs and request bodies are case sensitive.</div>

## Call sequence

Use the RESTful APIs in the following steps:

1. Call the [`acquire`](../rest-api/acquire) method to request a resource ID for cloud recording.
2. Call the  [`start`](../rest-api/start) method within five minutes after getting the resource ID to start the recording.
3. Call the [`stop`](../rest-api/stop) method to stop the recording.

During the recording, you can call the [`query`](../rest-api/query) method to check the recording status.