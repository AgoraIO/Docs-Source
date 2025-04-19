---
title: "REST quickstart"
sidebar_position: 1
platform_selector: false
description: >
  Start cloud recording, query cloud recording status, and stop cloud recording by sending a RESTful API request.
---
import Prerequisites from '@docs/shared/cloud-recording/prerequisites.mdx'

Cloud Recording enables you to record and store real-time audio and video streams from channels. To implement Cloud Recording, you set up a self-hosted backend that interacts with Agora servers to manage recording tasks. This guide introduces the essential Cloud Recording RESTful APIs you use to manage the recording process.

<Admonition type="info">
The command-line examples in this guide are for demonstration purposes only. Do not use them directly in a production environment. Implement RESTful API requests through your application server or use <Vg k="COMPANY"/>'s [Go backend middleware](https://github.com/AgoraIO-Community/agora-go-backend-middleware). For details, see [Quickstart using middleware](../get-started/middleware-quickstart)
</Admonition>

## Understand the tech

The basic process of implementing Cloud Recording is as follows:
![](https://agora-doc.s3.us-east-1.amazonaws.com/images/cloud-recording/cloud-recording-tech.svg)

1. Get a resource ID

    Before starting a cloud recording, call the [`acquire`](#acquire) method to obtain a cloud recording resource ID. After calling this method successfully, you get a resource ID in the response body.

2. Start cloud recording

    Call the [`start`](#start) method to join the channel and start a cloud recording. After calling this method successfully, you get a recording ID from the response body to identify the current recording process.

3. Query the recording status

    Call the [`query`](#query) method to check the recording status during the recording.

4. Stop cloud recording

    Call the [`stop`](#stop) method to stop the cloud recording.

5. Upload the recording file

    After the recording ends, the cloud recording service uploads the recording file to the [third-party cloud storage](../reference/restful-api#storageconfig) you specify.

## Prerequisites

<Prerequisites />

## Implement cloud recording

The following figure shows the API call sequence to start and manage cloud recording:

![](https://agora-doc.s3.us-east-1.amazonaws.com/images/cloud-recording/cloud-recording-sequence.svg)

The following APIs are optional and can be called multiple times. However, they must be called during a recording session, that is, after recording starts and before it ends:

- [`query`](#query): Query the recording status 
- [`update`](#update): Update the subscription list
- [`updateLayout`](#update-video-layout): Update the video layout  


### Use basic HTTP authentication

The <Vpd k="NAME" /> RESTful APIs require basic HTTP authentication. You need to set the `Authorization` parameter in every HTTP request header. For details, see [Basic HTTP authentication](../reference/restful-authentication).

<a name="acquire"></a>
### Get a resource ID

Call the [`acquire`](../reference/restful-api#acquire) method to request a resource ID for <Vpd k="NAME" />.

After calling this method successfully, you receive a resource ID in the response body. The resource ID is valid for five minutes. Start recording with this resource ID within the validity period. One resource ID can only be used for a single recording session.

- The recording service is equivalent to a non-streaming client in the channel. The `uid` parameter in the request body is used to identify the recording service and cannot be the same as any existing user ID in the channel. For example, if there are two users already in the channel and their user IDs are 123 and 456, the `uid` cannot be `"123"` or `"456"`.

- <Vg k="COMPANY"/> <Vpd k="NAME" /> does not support user IDs in string format (User Accounts). Ensure that every user in the channel has an integer user ID. The string content of the `uid` parameter must also be an integer.

#### Sample code

For testing purposes, use the following command in the terminal to call the `acquire` method.

``` bash
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
    "clientRequest":{}
}'
```

<a name="start"></a>
### Start recording

Call the [`start`](../reference/restful-api#start) method within five minutes of getting a resource ID to join a channel and start recording. You can choose either [individual recording](../develop/individual-mode) or [composite recording](../develop/composite-mode) as the recording mode.

If this method call succeeds, you receive a recording ID (sid) in the HTTP response body. This ID identifies the current recording.

<Admonition type="info">
After you obtain the recording ID `sid`, you can call the `query`, `updateLayout`, and `stop` methods before the time set (in hours) by `resourceExpiredHour` has passed.
</Admonition>

#### Sample code

For testing purposes, use the following command in the terminal to call the `start` method. 

``` bash
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
### Query recording status

During a recording session, can call the [`query`](../reference/restful-api#query) method to query the recording status. You can call this API multiple times.

When you call this method successfully, you receive the current recording status and related information about the recording file in the response body. See [Best Practices in Integrating Cloud Recording](../best-practices/integration-best-practices) for details about how to [Monitor service status during a recording](../best-practices/integration-best-practices#monitor-service-status-during-a-recording) and[ Obtain the M3U8 file name](../best-practices/integration-best-practices#obtain-the-m3u8-file-name).

#### Sample code

For testing purposes, use the following command in the terminal to call the `query` method. 

```bash
# Replace <appid> with the App ID of your Agora project
# Replace <resourceid> with the resource ID obtained through the acquire method
# Replace <sid> with the sid obtained through the start method
# Replace "<mode>" with "individual" for individual recording or "composite" for composite recording
curl --location --request GET 'https://api.agora.io/v1/apps/<appid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/query' \
# Replace <Authorization> with the Base64-encoded credential in basic HTTP authentication
--header 'Authorization: Basic <Authorization>' \
--header 'Content-Type: application/json'
```

<a name="stop"></a>
### Stop recording

Call the [`stop`](../reference/restful-api#stop) API to end the recording session.

When you call this method successfully, you receive the status of the recording file upload and information about the recording file in the response body.

#### Sample code

For testing purposes, use the following command in the terminal to call the `stop` method. 

```bash
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

<Admonition type="info" title="Parameter settings">

- If the `uid` parameter in the request body is the same as a user ID in the channel, or if you use a non-integer user ID, the recording fails. For details, see the notes on the `uid` parameter in the section [Get a cloud recording resource](#acquire).
- When the `start` request returns `200`, it only means that the RESTful API request is successful. To ensure that the recording has started successfully and continues normally, call `query` to check the recording status. Errors such as unreasonable `transcodingConfig` parameter settings, incorrect third-party cloud storage information, or incorrect token information cause the `query` method to return `404`. See [Why do I get a 404 error when I call query after successfully starting a cloud recording? ](../reference/common-errors#errors).
- Set the `maxIdleTime` parameter based on your business needs. Within the time range set by `maxIdleTime`, the recording continues and billing is generated even if the channel is idle.
</Admonition>

## Reference

This section contains content that completes the information on this page, or points you to documentation that explains other aspects to this product.

### Sample project

<Vg k="COMPANY"/> provides a [Postman collection](https://documenter.getpostman.com/view/6319646/SVSLr9AM), which contains sample requests of RESTful API for a cloud recording. You can use the collection to quickly grasp the basic functionalities of the Cloud Recording RESTful APIs. You only need to import the collection to Postman and set your environment variables.

You can also use Postman to generate code snippets written in various programming languages. To do so, select a request, click **Code**, and select the desired language in **GENERATE CODE SNIPPETS**.

![img](https://web-cdn.agora.io/docs-files/1588737379230)

### See also

- To streamline the use of Agora RESTful APIs within your infrastructure, see
[Quickstart using middleware](../get-started/middleware-quickstart). The community middleware project provides RESTful APIs for tasks such as token generation and cloud recording management.

<a name="update"></a>
- To update the subscription lists during the recording, call [`update`](../reference/restful-api#update). You can call this method multiple times. See [Set up subscription lists](../develop/subscription) for details.

<a name="updateLayout"></a>
- To set or update the video layout during the recording, call the [`updateLayout`](../reference/restful-api#updatelayout) method. See [Set Video Layout](../develop/layout) for details.

- [Common errors in cloud recording](../reference/common-errors) lists common error codes and error messages in the response body.

- [<Vg k="COMPANY"/> Cloud Recording RESTful API Callback Service](../reference/rest-api-overview) lists all the callback events of cloud recording.
- To learn more about the implementation steps and details of basic functions, you can refer to the following documents:
  - [Individual recording](../develop/individual-mode)
  - [Composite recording](../develop/composite-mode)
  - [Web page recording](../develop/webpage-mode)
  - [Capture screenshots](../develop/screen-capture)

## Next steps

### Manage recorded files

After the recording starts, the <Vg k="COMPANY"/> server splits the recorded content into multiple TS/WebM files and keeps uploading them to the third-party cloud storage until the recording stops. You can refer to [Manage Recorded Files](../develop/manage-files) to learn about the naming rules, file sizes, and slicing rules of recording files.

### Token authentication

To ensure communication security, in a formal production environment, you need to generate tokens on your app server. See [Authenticate Your Users with Token](../develop/authentication-workflow).