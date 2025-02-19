---
title: "Best practice in integrating Cloud Recording"
sidebar_position: 1
type: docs
platform_selector: false
description: >
   Guidelines for integrating cloud recording into your app.
---

import SwitchDomainName from '@docs/shared/common/_switch-domain-name.mdx';

To improve application robustness, Agora recommends that you do the following when integrating Cloud Recording RESTful APIs:

## Failover
In response to network failures, as well as risks that arise from factors such as non-Agora cloud services, non-Agora software, infrastructure, and force majeure, Agora cloud recording provides high-availability automatic task migration services. When the fault is confirmed, the migration is completed in the shortest possible time (estimated to be within 90 seconds). During this period, there are risks such as recording interruption and recording file loss.

For use-cases with a large number of viewers in the channel or extremely high requirements for high availability, consider whether you can accept the impact of high availability migration based on your own business characteristics, and decide whether to adopt higher quality assurance measures, such as [Multi-channel task assurance](#multi-channel-task-assurance), or [Monitor service status during a recording](#monitor-service-status-during-a-recording) through periodic channel query and message notification service, and re-initiate new recording tasks in a timely manner using a different `uid`.

## Multi-channel task assurance
If you need higher quality assurance than failover, use a multi-tasking assurance strategy. Each cloud recording task is billed separately. Please see [Pricing](../overview/pricing) for details on the billing method. Take the following steps to implement this strategy:

1. Initiate the main task and a backup task at the same time to achieve multi-channel recording of the same channel. To do this, use the same `appId` and `cname`, and different `uid`s to initiate multiple recording tasks. When initiating a subsequent recording task, set the `clientRequest.excludeResourceIds` field in the `acquire` request's body to the previous recording task or several previous recording tasks. This prevents the subsequent task from using resources in the area where the previous recording task is located. When the network in the area where the previous recording task is located fails, the subsequent recording task will not be affected.

1. Listening to the following callback events on the client side promptly notifies the audience to subscribe to the backup task `uid`:

   - Anchor offline `callbackonUserOffline`
   - Anchor audio and video status change callbacks `onRemoteAudioStateChanged` and `onRemoteVideoStateChanged`

## Use dual domain names

If you send a Cloud Recording RESTful API request to `api.agora.io` and the request fails, retry with the same domain name first. If it fails again, replace the domain name with `api.sd-rtn.com` and retry. Best practice is to first try the DNS domain close to your server. See the [domain name table](#domain-name-table) for a list of DNS servers.

Agora recommends that you use a backoff strategy, for example, retry after 1, 3, and 6 seconds successively, to avoid exceeding the Queries Per Second limits.

## Check the limits

Check that your Peak Concurrent Worker (PCW), Queries Per Second (QPS), and the number of streams do not exceed the following limits set by Agora.

#### PCW

The PCW limit is set to 50 for all regions and resolutions. If you need to extend the PCW limit, please contact support@agora.io.

#### QPS

The initial QPS limit is 10 per App ID when you register. You can estimate the QPS that your project needs based on your PCW value and query frequency. If you need to extend the limit for QPS, contact support@agora.io.

#### Number of streams

The upper limit of video attributes supported by Agora is as follows: 

- Resolution 1920 × 1080 
- Frame rate 30 FPS

The maximum number of supported streams is as follows:

| Service type    | Mainland China        | Europe               | America               | Asia (excluding mainland China) |
|:----------------|:----------------------|:---------------------|:----------------------|:--------------------------------|
| Cloud recording | <ul><li>SD 100</li> <li>HD 50</li> <li>FHD 30</li></ul> | <ul><li>SD 50</li> <li>HD 30</li> <li>FHD 10</li></ul> | <ul><li>SD 50</li> <li>HD 50</li> <li>FHD 30</li></ul> | <ul><li>SD 50</li> <li>HD 50</li> <li>FHD 30</li></ul>           |

<Admonition type="caution" title="Note">If you need to record multiple streams of different resolutions at the same time, make sure you meet the following requirements:<ul><li>The number of streams per resolution cannot exceed the corresponding limit for that resolution.</li><li>The total number of streams cannot exceed the limit set for the higher resolution. For example, if you need to use cloud recording in Europe to record in both SD and HD, the total number of streams cannot exceed 50. If you record in both HD and FHD, the total number cannot exceed 30.</li></ul></Admonition>

## Get service status

You use Cloud Recording RESTful APIs to get the status of the recording service.

Best practice is that core apps do not rely on <Vg k="NCS_LONG" /> (<Vg k="NCS" />). If your apps already rely heavily on the <Vg k="NCS" />, contact <a href="mailto:support@agora.io">support@agora.io</a> and enable the redundant message notification function. This doubles the received notifications and reduces the probability of message loss. After enabling the message notification function, you need to deduplicate messages based on `sid`. Message notification still cannot guarantee a 100% arrival rate.

### Ensure the recording service starts successfully

Take the following steps to ensure that the recording service starts successfully:

1. Ensure that the `start` request is successful, that is, you receive a `sid` (recording ID) from the response. If the request fails, take measures according to the HTTP status code:

   - If the returned HTTP status code is always `40x`, check the parameter values in your request.
   - If the returned HTTP status code is `50x`, you can retry several times with the same parameters until you receive a `sid`. Agora recommends that you use a backoff strategy, for example, retry after 3, 6, and 9 seconds successively, to avoid exceeding the QPS limits. If you retry three times and still do not get a `sid`, retry with a new user ID.
   -  If you receive error code `65`, retry with the same parameters. Agora recommends that you use a backoff strategy, for example, retry after 3 and 6 seconds successively.

2. Five seconds after you receive a `sid`, use a backoff strategy to call `query`. Agora recommends that the interval between two `query` calls is shorter than `maxIdleTime`, which you set in the `start` call. If the `query` call succeeds, and `status` in `serverResponse` is `4` or `5`, it means the recording service starts successfully. Otherwise, you can deem the recording service as not having started, or quit halfway after starting.

- Agora recommends that you prepare a backup user ID, which you can use when restarting the recording service, to avoid two identical user IDs kicking each other out of the channel. You can alternate between the backup user ID and the original one.

### Monitor service status during a recording

You can periodically call `query` to ensure that the recording service is in progress and in a normal state. Apart from `query`, you can use the <Vg k="NCS" /> as a complementary method to monitor the service status. See [Comparison Between the <Vg k="NCS" /> and the `query` Method](../reference/rest-api-overview#what-are-the-differences-between-the-message-notification-service-and-the-query-method) for detailed comparison between the two methods.

#### Periodically query service status

If the reliability of the status of a cloud recording is a high priority, Agora strongly recommends using the `query` method to periodically query the recording service status. The interval between two calls can be around two minutes. Take the corresponding measure based on the received HTTP status code:

- If the returned HTTP status code is always `40x`, check the parameter values in your request.
- If the returned HTTP status code is `404`, and the request parameters are confirmed to be correct, the recording has either not started successfully, or the recording quit after starting. Agora recommends that you use a backoff strategy, for example, retry after 5, 10, and 15 seconds successively.
- If the returned HTTP status code is `50x`, the `query` request failed, but it is not clear whether the recording has quit. The `50x` error is rare. You can continue to use the backoff strategy (waiting for 5 seconds, 10 seconds, 15 seconds, or 30 seconds) to call `query`.

#### Redundant message notifications

After enabling the redundant message notification function, you need to deduplicate messages based on `sid`. For example, if you need to start recording again after a recording session times out and quits, the process is:

1. Your server receives the notifications of event `31`, `32`, or `11`, which means that the recording service quits normally.
2. After receiving the notifications, your application calls `acquire` to restart the recording service.
3. During this period, your server receives notifications of event `31`, `32`, or `11` again. If `sid` contained in the above notifications is identical to the previous ones, you can ignore them as redundant notifications.
4. Call `query` if you need to fully ensure that the recording service successfully starts.

When the recording service enables the [high availability mechanism](../overview/product-overview#features), some notifications may be sent twice. You can distinguish them by the user ID in the notification. If the user ID is the same as the one you use when you start the recording, the notification belongs to the original recording session; otherwise, the notification belongs to the recording session initiated by the high availability mechanism.

### <a name="get_filename"></a>Obtain the M3U8 file name

You can obtain the M3U8 file name by two means. One is by splicing according to the file naming rules. The other is by calling the `query` method. Agora recommends that you use splicing to obtain the M3U8 file name.

#### Obtain file name by splicing

In composite recording mode, the format of the M3U8 file name is `<sid>_<cname>.m3u8`. Therefore, you can predict the M3U8 file name by splicing. See [Naming conventions](../develop/manage-files#naming-conventions) for details.

#### Obtain file name via the `query` call

The M3U8 file name is generated after the first slice file is generated. Therefore, you should call `query` after the first slicing completes. See [Slicing](../develop/manage-files#slicing) for details.

In composite recording mode, call `query` 15 seconds after the cloud recording starts; in individual recording mode, call `query` one minute after the cloud recording starts. If the first `query` call fails, you can try again after one minute.

## Avoid frequent quits of the recording service

The default value of `maxIdleTime` in the `start` method is 30 seconds. If the host frequently goes online and offline, a brief `maxIdleTime` value causes the recording service to join and exit the channel frequently. For use-cases that require the recording service to be in the channel all the time, it is necessary to increase `maxIdleTime` in case the recording quits after a short idle time.

For example, if there is a fixed 5-minute break in each class, you can set `maxIdleTime` to 10 minutes to ensure uninterrupted recording of the entire class.

## Fault recovery

Network failures and potential risks may occur due to factors such as cloud and network software, infrastructure, and other elements outside of <Vg k="COMPANY"/>'s control. To enhance the user experience, Cloud Recording offers automatic high availability task migration for failure recovery. When a failure is detected, the recording task will be migrated within 90 seconds. During this time, the recording may be disrupted and recorded files may be lost.

To guarantee high availability of important scenes with a large audience, best practice is to:

1. Monitor recording tasks with calls to the [query](/en/cloud-recording/reference/restful-api#query) method.

   If the call returns a `404` error, create a new recording task with a different UID.

1. Use Notifications to [Handle notifications for specific events](/en/cloud-recording/develop/receive-notifications#cloud-recording-callback-events). After starting the recording, if you don't receive event `13` `High availability register success` within 10 seconds, create a new recording task with a different UID.

These fault recovery methods may result in multiple recording tasks. You are charged separately for each task. For more information, see [Pricing](../overview/pricing).

<SwitchDomainName />

## Reference

### Integration requirements checklist

To ensure reliability of the cloud recording service, refer to the following checklist to confirm that your solution meets the integration requirements:

| Serial | Importance | Item | Description |
|--|----------|----------|----------|
| 1 | required | Subscribe to a service | Make sure you have activated the cloud recording service. | 
| 2 | required | request method | <ul><li>To query, use the `POST` request method; to query the recording status use `GET`. </li> <li>Request URLs and request body content are case-sensitive.</li></ul> |
| 3 | required | Get recording resources | <ul><li>The passed in `uid` cannot duplicate any UID within the current channel.</li><li>For page recording, make sure an `appid + cname + uid` corresponds to a resource ID.</li><li>Make sure that a resource ID is only used for one cloud recording service.</li><li>Make sure to call the `start` method.</li></ul> |
| 4 | required | channel scene | Make sure that the channel scene (`channelType`) is consistent with the settings of the <Vg k="VSDK" />. |
| 5 | required | recording parameters | <ul><li>Make sure that the type, case, and value range of all the parameters passed in when starting the recording are correct, and the required parameters are filled; otherwise, error code 2 is returned.</li><li>Set the layout and video bit rate of the combined recording by referring to the combined layout document and the recording bit rate comparison table.</li></ul> |
| 6 | required | Confirm that the recording service has started successfully | <ul><li>Make sure that the start request is successful, that is, the `sid` (recording ID) is successfully obtained.</li><li>Call the query method 5 seconds after getting the `sid` using the backoff strategy. If the returned status is still not `4` or `5`, after 90 seconds, it can be considered that the recording has not started or exited after a timeout.</li></ul> |
| 7 | required | PCW & QPS limits | <ul><li>Make sure that each App ID does not exceed 10 requests per second (QPS).</li><li>To increase the QPS and PCW limits, please contact technical support.</li></ul> |
| 8 | optional | NCS Service Activation | Activate the cloud recording callback service and subscribe to the following events as an auxiliary means of monitoring the recording service status: <ul><li>`40 recorder_started`: The recording service has started.</li><li>`11 session_exit`: The recording service ended the task and exited.</li><li>`1 cloud_recording_error`: An error occurred in the recording service.</li><li>`12 session_failover`: Enable high availability mechanism for recording.</li><li>`31 uploaded`: All recorded files have been uploaded to the specified third-party cloud storage.</li></ul> |
| 9 | optional | Use dual domain names | If the request fails with the primary domain name `api.agora.io`, try again with the primary domain name. If it fails again, switch to the secondary domain name `api.sd-rtn.com` and send the request again. |
| 10 | optional | timeout logic | Make sure that the `maxIdleTime` setting is reasonable. The recommended value is 300 seconds. |


