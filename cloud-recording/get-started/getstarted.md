---
title: "REST quickstart"
sidebar_position: 1
platform_selector: false
description: >
  Start cloud recording, query cloud recording status, and stop cloud recording by sending a RESTful API request.
---

The command-line examples in this article are for demonstration only and should not be used in a production environment. In a production environment, you need to send RESTful API requests through your application server.

## Understand the tech

The complete process of implementing a cloud recording is as follows:
![](https://web-cdn.agora.io/docs-files/1627889715871)

**1. Get a resource ID**
Before starting a cloud recording, you must call the [`acquire`](#acquire) method to obtain a cloud recording resource. After calling this method successfully, you can get a resource ID in the response body.

**2. Start a cloud recording**
Call the [`start`](#start) method to join the channel and start a cloud recording. After calling this method successfully, you can get a recording ID from the response body to mark the current recording process.

**3. Query the recording status**
Call the [`query`](#query) method to check the recording status during the recording.

**4. Stop the cloud recording**
Call the [`stop`](#stop) method to stop the cloud recording.

**5. Upload the recording file**
After the recording is over, the cloud recording service uploads the recording file to the [third-party cloud storage](../reference/rest-api/start#cloud-storage-configuration) you specify.

## Prerequisites

- A valid <Link to="{{Global.AGORA_CONSOLE_URL}}">Agora Account</Link>.
- A valid Agora project with an App ID and a temporary token. For details, see [Get Started with Agora](../reference/manage-agora-account#get-the-app-id).
- A computer with access to the internet. If your network has a firewall, follow the instructions in [Firewall Requirements](../reference/firewall).
- Ensure that a third-party cloud storage service has been enabled. The currently supported third-party cloud storage service providers are as follows:
  - [Qiniu Cloud](https://www.qiniu.com/en/products/kodo)
  - [Amazon S3](https://aws.amazon.com/s3/?nc1=h_ls)
  - [Alibaba Cloud](https://www.alibabacloud.com/product/object-storage-service)
  - [Tencent Cloud](https://intl.cloud.tencent.com/product/cos)
  - [Kingsoft Cloud](https://en.ksyun.com/nv/product/KS3)
  - [Microsoft Azure](https://azure.microsoft.com/en-us/services/storage/blobs/)
  - [Google Cloud](https://cloud.google.com/storage)
  - [Huawei Cloud](https://www.huaweicloud.com/intl/en-us/product/obs)
  - [Baidu AI Cloud](https://intl.cloud.baidu.com/product/bos.html)
- Ensure that you have joined the <Vg k="VSDK" /> channel and have users in the channel and are streaming.

## Project setup

Enable the cloud recording service before using Agora Cloud Recording for the first time.

1. Log in to <Link to="{{Global.AGORA_CONSOLE_URL}}"><Vg k="CONSOLE" /></Link>, and click the **Project Management** icon on the left navigation panel.
2. On the **Project Management** page, find the project for which you want to enable the cloud recording service, and click the edit icon. 
3. On the **Edit Project** page, find **Cloud Recording**, and click **Enable**.
![](https://web-cdn.agora.io/docs-files/1638866909361)

4. Click **Enable Cloud Recording**.
![](https://web-cdn.agora.io/docs-files/1636367386978)
5. Click **Apply**.

Now, you can use Agora Cloud Recording and see the usage statistics in the **Usage** page.

## Implement the cloud recording

The following figure shows the API call sequence of a cloud recording:
Querying the recording status ([`query`](#query)), updating the subscription list ([`update`](#update)), and updating the video layout ([`updateLayout`](#update-video-layout)) are optional and can be called multiple times, but they must be called during the recording process, that is, after the recording starts and before the recording ends.
![](https://web-cdn.agora.io/docs-files/1627527945942)

### Pass the basic HTTP authentication

The RESTful APIs require basic HTTP authentication. You need to set the `Authorization` parameter in every HTTP request header. For how to get the value for Authorization, see [basic HTTP authentication](../reference/restful-authentication).

<a name="acquire"></a>
### acquire: Get a resource ID

Call the [`acquire`](../reference/rest-api/acquire) method to request a resource ID for cloud recording.

After calling this method successfully, you can get a resource ID in the response body. The resource ID is valid for five minutes, so you need to start recording with this resource ID within five minutes. One resource ID can only be used for one recording session.

- The recording service is equivalent to a non-streaming client in the channel. The `uid`parameter in the request body is used to identify the recording service and cannot be the same as any existing user ID in the channel. For example, if there are two users already in the channel and their user IDs are 123 and 456, the `uid` cannot be `"123"` or `"456"`.
- Agora Cloud Recording does not support user IDs in string format, that is, User Accounts. Ensure that every user in the channel has an integer user ID. The string content of the`uid` parameter must also be an integer.

#### Sample code

You can use the command-line tool to send the following command to call the `acquire` method. 

```json
# Replace <appid> with the App ID of your Agora project
curl --location --request POST 'https://api.agora.io/v1/apps/<appid>/cloud_recording/acquire' \
# Replace <Authorization> with the Base64-encoded credential in basic HTTP authentication
--header 'Authorization: Basic <Authorization>' \
--header 'Content-Type: application/json' \
--data-raw '{
  # Replace <YourChannelName> with the name of the channel you need to record
  "cname": "<YourChannelName>",
  # Replace <YourRecordingUID> with your user ID
  "uid": "<YourRecordingUID>",
  "clientRequest":{
  }
}'

```

<a name="start"></a>
### Start recording

Call the [`start`](../reference/rest-api/start) method within five minutes after getting the resource ID to join a channel and start the recording. You can choose either [individual recording](../develop/individual-mode) or [composite recording](../develop/composite-mode) as the recording mode.

If this method call succeeds, you get a recording ID (sid) from the HTTP response body. This ID is the unique identification of the current recording.

#### Sample code

You can use the command-line tool to send the following commands to call the `start` method. 

```shell
# Replace <appid> with the App ID of your Agora project
# Replace <resourceid> with the resource ID obtained through the acquire method
# Replace "<mode>" with "individual" for individual recording or "composite" for composite recording
curl --location --request POST  'https://api.agora.io/v1/apps/<appid>/cloud_recording/resourceid/<resourceid>/mode/<mode>/start' \
# Replace <Authorization> with the Base64-encoded credential in basic HTTP authentication
--header 'Authorization: Basic <Authorization>' \
--header 'Content-Type: application/json' \
--data-raw '{
    # Replace <YourChannelName> with the name of the channel you need to record.
    "cname": "<YourChannelName>",
	# Replace <YourRecordingUID> with your user ID that identifies the recording service.
    "uid": "<YourRecordingUID>",
    "clientRequest": {
		# Replace <YourToken> with the temporary token you obtain from the console.
	    "token": "<YourToken>",
		# Set the storageConfig related parameters.
        "storageConfig": {
            "secretKey": "<YourSecretKey>",
            "vendor": 0,
            "region": 0,
            "bucket": "<YourBucketName>",
            "accessKey": "<YourAccessKey>"
        },
		# Set the recordingConfig related parameters.
        "recordingConfig": {
		   # Which is consistent with the "channelType" of the Agora <Vg k="VSDK" />.
            "channelType": 0
        }
    }
}'

```

<a name="query"></a>
### query: Query recording status

During the recording, you can call the [`query`](../reference/rest-api/query) method to query the recording status multiple times.

After calling this method successfully, you can get the current recording status and related information about the recording file from the response body. See *Best Practices in Integrating Cloud Recording* for details about how to [Monitor service status during a recording](../develop/integration-best-practices#monitor-service-status-during-a-recording) and[ Obtain the M3U8 file name](../develop/integration-best-practices#obtain-the-m3u8-file-name).

#### Sample code

You can use the command-line tool to send the following commands to call the `query` method. 

```shell
# Replace <appid> with the App ID of your Agora project
# Replace <resourceid> with the resource ID obtained through the acquire method
# Replace <sid> with the sid obtained through the start method
# Replace "<mode>" with "individual" for individual recording or "composite" for composite recording
curl --location --request GET 'https://api.agora.io/v1/apps/<appid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/query' \
# Replace <Authorization> with the Base64-encoded credential in basic HTTP authentication
--header 'Authorization: Basic <Authorization>' \
--header 'Content-Type: application/json' \
```

<a name="stop"></a>
### stop: Stop recording

Call the [`stop`](../reference/rest-api/stop) the recording.

After calling this method successfully, you can get the status of the recording file upload and information about the recording file from the response body.

#### Sample code

You can use the command-line tool to send the following command to call the `stop` method. 

```shell
# Replace <appid> with the App ID of your Agora project
# Replace <resourceid> with the resource ID obtained through the acquire method
# Replace <sid> with the sid obtained through the start method
# Replace "<mode>" with "individual" for individual recording or "composite" for composite recording 
curl --location --request POST 
'https://api.agora.io/v1/apps/<appid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/stop' \
--header 'Content-Type: application/json;charset=utf-8' \
# Replace <Authorization> with the Base64-encoded credential in basic HTTP authentication
--header 'Authorization: Basic <Authorization>' \
--data-raw '{
    # Replace <YourRecordingUID> with your user ID that identifies the recording service.
    "uid": "<YourRecordingUID>",
	# Replace <YourChannelName> with the name of the channel you are recording.
    "cname": "<YourChannelName>",
	"clientRequest":{
    }
}'

```

## Considerations

### Parameter settings

- If the `uid` parameter in the request body is the same as the user ID in the channel, or if a non-integer user ID is used, the recording fails. For details, see the notes on the `uid` parameter in the section [Get a cloud recording resource](#acquire).
- When the `start` request returns 200, it means only that the RESTful API request is successful. To ensure that the recording starts successfully and goes on normally, you also need to call query to query the recording status. Errors such as uUnreasonable `transcodingConfig` parameter settings, incorrect third-party cloud storage information, or incorrect token information cause the `query` method to return 404. See [Why do I get a 404 error when I call query after successfully starting a cloud recording? ](../reference/common-errors#errors).
- Set `maxIdleTime` reasonably according to your actual business needs. Within the time range set by `maxIdleTime`, even if the channel is idle, the recording continues and billing is generated.

### API call

- After obtaining the resource ID, you must call the `start`method within 5 minutes to start a recording. After the timeout, you need to request a resource ID again.
- After obtaining the `sid` (recording ID), after the time set by `resourceExpiredHour` has passed, you are not able to call the `query`, `updateLayout`, and `stop` methods.

## Next steps

### Manage recorded files

After the recording starts, the Agora server splits the recorded content into multiple TS/WebM files and keeps uploading them to the third-party cloud storage until the recording stops. You can refer to [Manage Recorded Files](../develop/manage-files) to learn about the naming rules, file sizes, and slicing rules of recording files.

### Token authentication

To ensure communication security, in a formal production environment, you need to generate tokens on your app server. See [Authenticate Your Users with Token](../develop/authentication-workflow).

## See also

<a name="update"></a>
### Update subscription lists

During the recording, you can call [`update`](../reference/rest-api/update) to update the subscription lists multiple times. See [Set up subscription lists](../develop/subscription) for details.

<a name="updateLayout"></a>
### Update video layout

During the recording, you can call the [`updateLayout`](../reference/rest-api/update#updatelayout-update-the-video-mixing-layout) method to set or update the video layout. See [Set Video Layout](../develop/layout) for details.

### Sample project

Agora provides a [Postman collection](https://documenter.getpostman.com/view/6319646/SVSLr9AM), which contains sample requests of RESTful API for a cloud recording. You can use the collection to quickly grasp the basic functionalities of the Cloud Recording RESTful APIs. You only need to import the collection to Postman and set your environment variables.

You can also use Postman to generate code snippets written in various programming languages. To do so, select a request, click **Code**, and select the desired language in **GENERATE CODE SNIPPETS**.

![img](https://web-cdn.agora.io/docs-files/1588737379230)

### Reference documents

- [Common errors in cloud recording](../reference/common-errors) lists common error codes and error messages in the response body.

- [Agora Cloud Recording RESTful API Callback Service](../reference/rest-api/rest-api-overview) lists all the callback events of cloud recording.
- To learn more about the implementation steps and details of basic functions, you can refer to the following documents:
  - [Individual recording](../develop/individual-mode)
  - [Composite recording](../develop/composite-mode)
  - [Web page recording](../develop/webpage-mode)
  - [Capture screenshots](../develop/screen-capture)

