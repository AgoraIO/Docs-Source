---
title: "Web page recording"
sidebar_position: 9
type: docs
platform_selector: false
description:
   Use the Cloud Recording RESTful API to make a web page recording and push media stream to the CDN during a web page recording.
---

Agora Cloud Recording supports three recording modes:

- Individual recording
- Composite recording
- Web page recording

This guide outlines the key steps for using the Cloud Recording RESTful API to record a web page.
In this recording mode, the content and audio of the specified web page are captured in a single file.

![](/images/cloud-recording/web-page-recording.svg)

You can use web page recording to reproduce use-cases such as online classes and video conferences. For example, if your web application integrates both the Agora SDK and a third-party whiteboard SDK, web page recording can record everything on the web page instead of only the audio and video streams.

![](/images/cloud-recording/web-page-layout.svg)

In web page recording mode, you can also convert the content and audio of the page into a media stream and push it to the CDN during the recording process.

![](/images/cloud-recording/web-page-push-cdn.svg)

## Prerequisites

- If you want to use web page recording along with other cloud recording functions, such as individual recording or screenshot capturing, Agora suggests that you use a separate App ID for web page recording for more independent resource management.
- You need to provide a web application that can be accessed through a URL, so that the content can be recorded. (The hosts and the audience can use web or other platforms.)
- Your web application should support Chrome.
- The web page content is displayed completely in one screen, that is, no scrolling is needed.
- If you want to record every operation of the host on the screen, you need to sync the operations in your web application.

## Implement a Web Page Recording

### Get a resource ID

Before recording, call the [`acquire`](../reference/restful-api#acquire) method to apply for a resource ID. Note that you must set `scene` as `1`.

#### An HTTP request example of `acquire`

- Request URL: 

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/acquire
```
- `Content-type`: `application/json;charset=utf-8`
- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {
        "resourceExpiredHour": 24,
        "scene": 1
    }
}
```

### Start recording

To enable [web page recording mode](../develop/webpage-mode), set `mode` to `web` when calling  [`start`](../reference/restful-api#start). Use `extensionServiceConfig` to configure web page recording, and use `storageConfig` to configure your third-party cloud storage.

You cannot switch to a different recording mode once you start recording.

In web page recording mode, you can configure the following parameters in `clientRequest`:

| Parameter                | Description                               | Note     |
| :----------------------- | :---------------------------------------- | :------- |
| `storageConfig`          | Configures the third-party cloud storage. | Required |
| `recordingFileConfig`    | Configures the recorded files.            | Optional |
| `extensionServiceConfig` | Configures web page recording.            | Required |

#### An HTTP request example of `start`

- Request URL:

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/web/start
```

- `Content-type:` `application/json;charset=utf-8`
- `Authorization:` Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).
- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {
        "token": "<token if any>",
        "extensionServiceConfig": {
            "errorHandlePolicy": "error_abort",
            "extensionServices": [
                {
                    "serviceName": "web_recorder_service",
                    "errorHandlePolicy": "error_abort",
                    "serviceParam": {
                        "url": "https://xxxxx",
                        "audioProfile": 0,
                        "videoWidth": 1280,
                        "videoHeight": 720,
                        "maxRecordingHour": 3
                    }
                }
            ]
        },
        "recordingFileConfig": {
            "avFileType": [
                "hls",
                "mp4"
            ]
        },
        "storageConfig": {
            "vendor": 2,
            "region": 3,
            "bucket": "xxxxx",
            "accessKey": "xxxxx",
            "secretKey": "xxxxx",
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

### Stop recording    

The charging will continue until the web page recording stops. You should set a reasonable `maxRecordingHour` based on the actual business use-case or actively stop the web page recording.

When a recording finishes, call [`stop`](../reference/restful-api#stop) to leave the channel and stop recording. To use Agora Cloud Recording again, you need to call the [`acquire`](../reference/restful-api#acquire) method for a new resource ID.

#### An HTTP request example of `stop`

- The request URL is: 

 ```html
 http://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/web/stop
 ```
- `Content-type`: `application/json;charset=utf-8`

- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {}
}
```

## Implement Pushing Stream to the CDN during a Web Page Recording

### Get a resource ID

Before starting the process, call the [`acquire`](../reference/restful-api#acquire) method to apply for a resource ID. Note that you must set `scene` as `1`.

#### An HTTP request example of `acquire`

- Request URL: 

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/acquire
```
- `Content-type`: `application/json;charset=utf-8`
- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {
        "resourceExpiredHour": 24,
        "scene": 1
    }
}
```

### Start a process

To enable [web page recording mode](../develop/webpage-mode), set `mode` to `web` when calling  [`start`](../reference/restful-api#start). Use `extensionServiceConfig` to configure web page recording, and use `storageConfig` to configure your third-party cloud storage.

You cannot switch to a different recording mode once you start recording.

In web page recording mode, you can configure the following parameters in `clientRequest`:

| Parameter                | Description                               | Note     |
| :----------------------- | :---------------------------------------- | :------- |
| `storageConfig`          | Configures the third-party cloud storage. | Required |
| `recordingFileConfig`    | Configures the recorded files.            | Optional |
| `extensionServiceConfig` | Configures web page recording.            | Required |

#### An HTTP request example of `start`

- Request URL:

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/web/start
```

- `Content-type:` `application/json;charset=utf-8`
- `Authorization:` Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).
- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {
        "token": "<token>",
        "extensionServiceConfig": {
            "extensionServices": [
                {
                    "serviceName": "web_recorder_service",
                    "errorHandlePolicy": "error_abort",
                    "serviceParam": {
                        "url": "https://xxxxx",
                        "audioProfile": 0,
                        "videoWidth": 1280,
                        "videoHeight": 720,
                        "maxRecordingHour": 3,
                        "maxVideoDuration": 200
                    }
                },
                {
                    "serviceName": "rtmp_publish_service",
                    "errorHandlePolicy": "error_ignore",
                    "serviceParam": {
                        "outputs": [
                            {
                                "rtmpUrl": "rtmp://xxx"
                            }
                        ]
                    }
                }
            ]
        },
        "recordingFileConfig": {
            "avFileType": [
                "hls",
                "mp4"
            ]
        },
        "storageConfig": {
            "vendor": 2,
            "region": 3,
            "bucket": "xxxxx",
            "accessKey": "xxxxx",
            "secretKey": "xxxxx",
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

### Stop the process    

When a recording and stream pushing finishes, call [`stop`](../reference/restful-api#stop) to leave the channel and stop recording. To use Agora Cloud Web Page Recording again, you need to call the [`acquire`](../reference/restful-api#acquire) method for a new resource ID.

#### An HTTP request example of `stop`

- The request URL is: 

 ```html
 http://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/web/stop
 ```
- `Content-type`: `application/json;charset=utf-8`

- `Authorization`: Basic authorization. For more information, see [How to pass the basic HTTP authentication](../reference/restful-authentication).

- Request body:

```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {}
}
```

## Recorded files

A web page recording session generates one M3U8 file and multiple TS files. Depending on the value of `avFileType`, the recording session may also generate one or more MP4 files. For detailed information about the naming conventions of the recorded files, see [Manage Recorded Files](../develop/manage-files).

## Pricing

Web page recording mode is free to use by November 1, 2021. See [Pricing for Web Page Recording](../overview/pricing-webpage-recording) for details.

## Considerations

### Application restrictions

- The recorded web page should not contain any video that has a resolution higher than 1920 × 1080.
- The resolution of the videos generated by the web page recording is up to 1920 × 1080.
- The recorded web page should not use WebGL.
- The downlink bitrate of your web application should not exceed 10 Mbps, and the uplink bitrate should not exceed 2 Mbps.
- Ensure that your web application does not consume excessive CPU memory and network bandwidth and that your application is used legally.
- If you enable the autoplay property for a video element in the recorded web page, the recording service can play the video without any user interaction. However, if you disable the autoplay property, the video cannot be played automatically, and the recording service cannot record the content of the video.
- The recorded webpage should not be redirected to a different domain, and should avoid any other types of redirection. If the webpage requires login, complete the login first before the recording session starts.
- You can use the [web page load timeout detection function](/cloud-recording/develop/webpage-load-timeout) to prevent the recorded content from being inconsistent with the expected content caused by the web page load timeout.

### RESTful API requests

- Recording starts approximately five seconds after you send a request. We recommend you send the request in advance to ensure that everything you want to record is captured.
- Web page recording does not support the `update` and `updateLayout` methods.
- If the URL you specify in the `start` method cannot be accessed, the recording service exits automatically after the `start` call. To ensure that the recording service starts successfully, see [Best Practices in Integrating Cloud Recording](/cloud-recording/best-practices/integration-best-practices#ensure-the-recording-service-starts-successfully).

### Other considerations

- During a recording,  when the length of the recorded file reaches around the value of `maxVideoDuration`, or when the size of the file exceeds around 2 GB, the recording service automatically creates another MP4 file.
- In a web page recording, the recording service can be considered a client of your web application.
  - If the URL you specify in the `start` method automatically enables the client to publish streams, the browser engine started by the recording server becomes a video sender. As a result, the recording server's video may be displayed as empty in the video panel of your application.
  - If your application displays a user list, we recommend you hide the recording server from the list to avoid confusion among other users.