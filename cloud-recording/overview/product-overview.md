---
title: 'Product overview'
sidebar_position: 1
description: >
  sThe functionality, uses, and features integrated in Cloud Recording.
---

You can quickly and flexibly record one-to-one or one-to-many audio and video calls or interactive live streaming through simple integration. Compared with Agora On-premise Recording, Agora Cloud Recording is more efficient and convenient as it does not require deploying Linux servers.

With Agora Cloud Recording, you can record calls or live streaming for your users to watch at their convenience. For example, a user can either attend an online course at the time of the course or watch the recorded course later, made possible by the Agora Cloud Recording service.

## Functions

The following table lists the main functions that Agora Cloud Recording provides. To learn more about these functions, click the links below.

| Feature   | Description                                                  |
| :------------------------------------------------ | :----------------------------------------------------------- |
| Recording mode                                    | Supports three recording modes: <ul><li>[Individual recording mode](../develop/individual-mode) : Records the audio and video as separate files for each user ID in a channel.</li><li>[Composite recording mode](../develop/composite-mode): Generates a single mixed audio and video file for all or specified user IDs in a channel.</li><li>[Web page recording mode](../develop/webpage-mode): Records the content and the audio of a specified web page in a single file</li></ul> |
| Capture screenshots                           | You can [take screenshots of each video stream](../develop/screen-capture) in individual recording mode.                |
| Subscribe to specified user IDs                             | You can specify the user IDs to subscribe or unsubscribe. You can also update the subscription lists during the recording. For details, see [Set up subscription lists](../develop/subscription).              |
| Subscribe to specified media types                       | You can specify the type of media to subscribe to:<ul><li>Audio only</li><li>Video only</li><li>Both audio and video</li></ul>|
| Set audio and video profiles                      | In composite recording mode, you can set audio and video profiles, such as the bit rate and resolution. |
| Set video layout                                  | In composite recording mode, you can [customize the video layout](../develop/layout#customize-the-video-layout) or [use predefined layouts](../develop/layout#predefined-layout-types), and set the background color or background image of the canvas or the user region. You can update the settings during recording. |
| Store recorded files in third-party cloud storage | You can store recorded files in the following third-party cloud storage services. You can customize the directory of the recorded files in the cloud storage.<ul><li>Amazon S3</li><li>Alibaba Cloud</li><li>Tencent Cloud</li><li>Qiniu Cloud</li><li>Kingsoft Cloud</li><li>Microsoft Azure</li><li>Google Cloud</li><li>Huawei Cloud</li><li>Baidu AI Cloud</li></ul>|
| Record dual streams                               | If the [Agora Video SDK ](../reference/glossary#agora-video-sdk)enables the [dual-stream mode](../reference/glossary#dual-stream), you can choose to record the high-video stream or the low-video stream. |
| Record encrypted channels                         | You can record a channel that is encrypted.  |
| Transcoding                               | Agora Cloud Recording provides transcoding scripts for you to [merge audio and video files](../develop/merge-files) and to [convert file formats](../develop/convert-format). |
| Callback service                                  | The [callback service](../reference/rest-api/rest-api-overview) provides information including:<ul><li>The filenames of the recorded files</li><li>The start time of the first slice file</li><li>The timestamp when the stream status changes</li></ul> |
| Extension services  |  Supports third-party extension services. Currently supports [ApsaraVideo for VoD](https://www.alibabacloud.com/help/doc-detail/51236.htm) only. |

## Applications

Agora Cloud Recording can be used in the following scenarios:

| Industry                      | Applications                                                 |
| ----------------------------- | ------------------------------------------------------------ |
| Online Education              | One-to-one and one-to-many online courses. Agora Cloud Recording provides high-quality voice and video recordings. <li>Students can replay recordings for review.</li><li>Students can make up for missed courses at their convenience.</li> |
| Live Streaming               | <li>The replay of live streaming highlights.</li><li>Captures screenshots.</li><li>Detects sexually explicit content.</li> |
| Financial Industry            | When conducting financial management, account registration, and face-to-face businesses, the financial industry can use audio and video recordings for record keeping and archival purposes. |
| Customer Service/Call Centers | The recordings can be used for customer research and service quality evaluations. |
| Remote Health Care            | <li>Recordings of remote diagnoses and online medical consultations enable patients to acquire medical resources in remote or inaccessible areas. </li><li> Can be used as references for subsequent treatments.</li> |

## Features

Agora Cloud Recording consists of the following features:

| Feature          | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| High Availability| When a recording server drops offline or a process gets killed, the cloud recording service enables the high availability mechanism, where the fault processing center automatically switches to a new server within 90 seconds to resume the service. |
| High Reliability | <li>Supports globally distributed cluster deployment and highly available services.</li><li>Automatically backs up files on Agora cloud server when the third-party cloud storage fails and automatically uploads the backup to the third-party cloud storage when it recovers.</li> |
| High Security    | Provides end-to-end security mechanisms for video calls, data transmission, data storage, and so on. For details, see [Information Security Policy](../reference/security#information-security-policy). |
| Compatibility    | Supports third-party cloud storages, such as [Amazon S3](https://aws.amazon.com/s3/?nc1=h_ls), [Alibaba Cloud](https://www.alibabacloud.com/product/oss), [Tencent Cloud](https://intl.cloud.tencent.com/product/cos), [Kingsoft Cloud](https://en.ksyun.com/post/product/KS3.html) , [Qiniu Cloud](https://www.qiniu.com/en/products/kodo), [Microsoft Azure](https://azure.microsoft.com/en-us/),[Google Cloud](https://cloud.google.com/),  [Huawei Cloud](https://www.huaweicloud.com/intl/en-us/) and [Baidu AI Cloud](https://intl.cloud.baidu.com/). |
| Ease of Use      | Simple implementation and easy to learn. With four RESTful API calls, you can start, stop, and query the recording. You can get started quickly, flexibly deploy recording services, and easily record on mobile and web pages. |

## References

- [Quickstart for RESTful API](../reference/rest-api/rest) describes how to use Agora Cloud Recording with the RESTful API.
- [Agora Cloud Recording RESTful API](../reference/rest-api/rest) describes the functions of the RESTful API.
- [RESTful API Callback Service](../reference/rest-api/rest-api-overview) describes the events of the RESTful API.