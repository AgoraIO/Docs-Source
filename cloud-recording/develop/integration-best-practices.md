---
title: "Best Practices in integrating Cloud Recording"
sidebar_position: 13
type: docs
description: >
   Guidelines for integrating cloud recording into your app.
---

To improve application robustness, Agora recommends that you do the following when integrating Cloud Recording RESTful APIs:

## Use dual domain names

If you send a Cloud Recording RESTful API request to `api.agora.io` and the request fails, retry with the same domain name first. If it fails again, replace the domain name with `api.sd-rtn.com` and retry. Best practice is to first try the DNS domain close to your server. See the [domain name table](#domain-name-table) for a list of DNS servers.

Agora recommends that you use a backoff strategy, for example, retry after 1, 3, and 6 seconds successively, to avoid exceeding the Queries Per Second (QPS) limits.

The initial QPS limit is 10 per API per CID when you register. You can estimate the QPS quota your project needs according to your peak current worker (PCW) quota and query frequency. The initial peak current worker (PCW) limit is 50 per AppID when you register. If the RESTful API returns QPS limitation error code `429`, or PCW quota limitation error code `406`, then retry, or contact support@agora.io to increase your QPS or PCW quota.

## Get service status

You can use Cloud Recording RESTful APIs to get the status of the recording service. 

Agora recommends that core apps should not rely on the Message Notification Service. If your apps already rely heavily on the Message Notification Service, Agora recommends that you contact <a href="mailto:support@agora.io">support@agora.io</a> to enable the redundant message notification function, which doubles the received notifications and reduces the probability of message loss. After enabling the redundant message notification function, you need to deduplicate messages based on `sid`. Redundant message notification still cannot guarantee a 100% arrival rate.

### Ensure the recording service starts successfully

Take the following steps to ensure that the recording service starts successfully:

1. Ensure that the `start` request is successful, that is, you receive a `sid` (recording ID) from the response. If the request fails, take measures according to the HTTP status code:

   - If the returned HTTP status code is always `40x`, check the parameter values in your request.
   - If the returned HTTP status code is `50x`, you can retry several times with the same parameters until you receive a `sid`. Agora recommends that you use a backoff strategy, for example, retry after 3, 6, and 9 seconds successively, to avoid exceeding the QPS limits. If you retry three times and still do not get a `sid`, retry with a new user ID.
   -  If you receive error code `65`, retry with the same parameters. Agora recommends that you use a backoff strategy, for example, retry after 3 and 6 seconds successively.

2. Five seconds after you receive a `sid`, use a backoff strategy to call `query`. Agora recommends that the interval between two `query` calls is shorter than `maxIdleTime`, which you set in the `start` call. If the `query` call succeeds, and `status` in `serverResponse` is `4` or `5`, it means the recording service starts successfully. Otherwise, you can deem the recording service as not having started, or quit halfway after starting.

- Agora recommends that you prepare a backup user ID, which you can use when restarting the recording service, to avoid two identical user IDs kicking each other out of the channel. You can alternate between the backup user ID and the original one.

### Monitor service status during a recording

You can periodically call `query` to ensure that the recording service is in progress and in a normal state. Apart from `query`, you can use the Message Notification Service as a complementary method to monitor the service status. See [Comparison Between the Message Notification Service and the `query` Method](../reference/rest-api/query#what-are-the-differences-between-the-message-notification-service-and-the-query-method) for detailed comparison between the two methods.

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

The default value of `maxIdleTime` in the `start` method is 30 seconds. If the host frequently goes online and offline, a brief `maxIdleTime` value causes the recording service to join and exit the channel frequently. For scenarios that require the recording service to be in the channel all the time, it is necessary to increase `maxIdleTime` in case the recording quits after a short idle time.

For example, if there is a fixed 5-minute break in each class, you can set `maxIdleTime` to 10 minutes to ensure uninterrupted recording of the entire class.

## Fault recovery

Network failures and potential risks may occur due to factors such as cloud and network software, infrastructure, and other elements outside of <Vg k="COMPANY"/>'s control. To enhance the user experience, Cloud Recording offers automatic high availability task migration for failure recovery. When a failure is detected, the recording task will be migrated within 90 seconds. During this time, the recording may be disrupted and recorded files may be lost.

For scenes with a large audience in the channel or high availability requirements, consider whether you can accept the impact of high availability migration based on your own business characteristics, and decide whether to adopt higher quality assurance measures. For example, create multiple recording tasks for critical scenes using distinct UIDs, and ensure use of servers in different geographical regions through geofencing. Alternatively, you can make periodic API calls and monitor notifications to get the latest recording task status, then create a new cloud recording task with a different UID once you confirm the recording task status is unhealthy.

If you create multiple cloud recording tasks, you are charged separately for each of them. For details, see [Pricing](../reference/pricing).

## Integration requirements checklist

To ensure reliability of the cloud recording service, refer to the following checklist to confirm that your solution meets the integration requirements:

| Serial | Importance | Item | Description |
|--|----------|----------|----------|
| 1 | required | Subscribe to a service | Make sure you have activated the cloud recording service. | 
| 2 | required | request method | <ul><li>To query, use the `POST` request method; to query the recording status use `GET`. </li> <li>Request URLs and request body content are case-sensitive.</li></ul> |
| 3 | required | Get recording resources | <ul><li>The passed in `uid` cannot duplicate any UID within the current channel.</li><li>For page recording, make sure an appid + cname + uid corresponds to a resource ID.</li><li>Make sure that a resource ID is only used for one cloud recording service.</li><li>Make sure to call the `start` method.</li></ul> |
| 4 | required | channel scene | Make sure that the channel scene (`channelType`) is consistent with the settings of the <Vg k="VSDK" />. |
| 5 | required | recording parameters | <ul><li>Make sure that the type, case, and value range of all the parameters passed in when starting the recording are correct, and the required parameters are filled; otherwise, error code 2 is returned.</li><li>Set the layout and video bit rate of the combined recording by referring to the combined layout document and the recording bit rate comparison table.</li></ul> |
| 6 | required | Confirm that the recording service has started successfully | <ul><li>Make sure that the start request is successful, that is, the `sid` (recording ID) is successfully obtained.</li><li>Make sure to be or within 90 seconds `sid` of getting status 4 5</li></ul> |
| 7 | required | PCW & QPS limits | <ul><li>Make sure that each App ID does not exceed 10 requests per second (QPS).</li><li>Ensure that the maximum number of concurrent tasks (PCW) in China does not exceed 1,000, and that in other regions does not exceed 300. To increase the QPS and PCW limits, please contact technical support.</li></ul> |
| 8 | optional | NCS Service Activation | Activate the cloud recording callback service and subscribe to the following events as an auxiliary means of monitoring the recording service status: <ul><li>`40 recorder_started`: The recording service has started.</li><li>`11 session_exit`: The recording service ended the task and exited.</li><li>`1 cloud_recording_error`: An error occurred in the recording service.</li><li>`12 session_failover`: Enable high availability mechanism for recording.</li><li>`31 uploaded`: All recorded files have been uploaded to the specified third-party cloud storage.</li></ul> |
| 9 | optional | Use dual domain names | If the request fails with the primary domain name `api.agora.io`, try again with the primary domain name; if it fails again, switch to the secondary domain name `api.sd-rtn.com` and send the request again. |
| 10 | optional | timeout logic | Make sure that the `maxIdleTime` setting is reasonable. The recommended value is 300 seconds. |

## Reference

### Domain name table

|Primary domain name  |Region domain name	|Region|
|:--------------------|:--------------------|:-----|
|`api.sd-rtn.com`      |`api-us-west-1.sd-rtn.com` |Western United States|
|                      |`api-us-east-1.sd-rtn.com` |Eastern United States|
|                      |`api-ap-southeast-1.sd-rtn.com`|Southeast Asia Pacific|
|                      |`api-ap-northeast-1.sd-rtn.com`| Northeast Asia Pacific|
|                      |`api-eu-west-1.sd-rtn.com` |Western Europe|
|                      |`api-eu-central-1.sd-rtn.com` |Central Europe|
|                      |`api-cn-east-1.sd-rtn.com`|East China|
|                      |`api-cn-north-1.sd-rtn.com`|North China|
|`api.agora.io`         |`api-us-west-1.agora.io`|Western United States|
|                       |`api-us-east-1.agora.io`|Eastern United States|
|                       |`api-ap-southeast-1.agora.io`|Southeast Asia Pacific|
|                       |`api-ap-northeast-1.agora.io`|Northeast Asia Pacific|
|                	    |`api-eu-west-1.agora.io`|Western Europe|
|                       |`api-eu-central-1.agora.io`|Central Europe|
|                       |`api-cn-east-1.agora.io`|East China|
|                       |`api-cn-north-1.agora.io`|North China|
