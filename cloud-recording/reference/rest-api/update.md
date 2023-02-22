---
title: "Update a recording"
sidebar_position: 4
type: docs
platform_selector: false
description:  >
  Change recordings.
---

During cloud recording process, you can call the `update` method to update the subscription list and web page recording configuration, or call the `updateLayout` method to update the video mixing layout.

## update: Update the cloud recording

During a cloud recording, you can call this method to update the Cloud Recording API-related configurations multiple times. This method call overrides the existing subscription configuration.

- Method: POST
- Endpoint: /v1/apps/\<appid\>/cloud_recording/resourceid/\<resourceid\>/sid/\<sid\>/mode/\<mode\>/update

> The request frequency limit is 10 requests per second for each [Agora account](../manage-agora-account#create-an-agora-account). Contact support@agora.io if you want to raise the limit.

### HTTP request

The following parameters are required in the URL:

| Parameter    | Type   | Description                                                                                                                                        |
| :----------- | :----- |:---------------------------------------------------------------------------------------------------------------------------------------------------|
| `appid`      | String | The App ID in the channel to be recorded.                                                                                                          |
| `resourceid` | String | The resource ID requested by [`acquire`](../rest-api/acquire).                                                                                     |
| `sid`        | String | The recording ID created by [`start`](../rest-api/start).                                                                                          |
| `mode`       | String | The recording mode. Supports individual mode (`individual`), composite mode (`mix`) and web page recording (`web`). Composite mode is the default. |


The following parameters are required in the request body:

| Parameter       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------------- | :----- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cname`         | String | The name of the channel to be recorded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `uid`           | String | A string that contains the user ID of the recording client. Must be the same user ID used in the [`acquire`](../rest-api/acquire) method.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `clientRequest` | JSON   | A specific client request that includes the `streamSubscribe` parameter and `webRecordingConfig` parameter.<li>Use `streamSubscribe` to update the subscription list. This is only applicable to individual recording (`individual`) and composite recording (`mix`).</li><li>Use `webRecordingConfig` to update parameters of web page recording. This is only applicable to Web page recording (`web`).</li><li>Use `rtmpPublishConfig` to update parameters of pushing media stream to the CDN during a web page recording. This is only applicable to Web page recording (`web`).</li> |

`streamSubscribe` requires the following parameters:

- audioUidList: (Optional) JSON. The audio subscription list. If you set this parameter, do not set `streamTypes` in `recordingConfig` as `1` (video only).
  - `subscribeAudioUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose audio you want to subscribe. The length of the array should not exceed 32 user IDs, and the array should not be empty. See [Set up subscription lists](../../develop/subscription) for details.
  - `unsubscribeAudioUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose audio you do not want to subscribe. Once you set this parameter, the recording service subscribes to the audio of all user IDs except the specified ones. The length of the array should not exceed 32 user IDs, and the array should not be empty. See [Set up subscription lists](../../develop/subscription) for details.
- videoUidList: (Optional) JSON. The video subscription list. If you set this parameter, do not set `streamTypes` in `recordingConfig` as `0` (audio only).
  - `subscribeVideoUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose video you want to subscribe. The length of the array should not exceed 32 user IDs, and the array should not be empty. See [Set up subscription lists](../../develop/subscription) for details.
  - `unsubscribeVideoUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose video you do not want to subscribe. Once you set this parameter, the recording service subscribes to the video of all user IDs except the specified ones. The length of the array should not exceed 32 user IDs, and the array should not be empty. See [Set up subscription lists](../../develop/subscription) for details.

`webRecordingConfig` requires the following parameters:

- `onhold`: (Optional) Bool. Sets whether to pause the web page recording during recording.

  - `true`: Pauses the web page recording during recording. The recording service does not generate slice files.

  - (Default) `false`: Continues the web page recording. If the recording has been paused, call the `update` method and set the `onhold` parameter to false to continue the recording. If you need to continuously call the `update` method to pause or resume page recording, call it after receiving the last HTTP response of `update`; otherwise the actual result may be inconsistent with your expectation.

- `url`: (Optional) String. Sets the address of the web page to record.

`rtmpPublishConfig` requires the following parameters:
- `outputs`：JSON Array. Configure as follows:
- `rtmpUrl`：String. The CDN address which you want to push stream to.


### Request example

- The request URL is:
```
https://api.agora.io/v1/apps/<appid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/update
```

- `Content-type` is `application/json;charset=utf-8`.
- `Authorization` is the basic authorization. See [RESTful API authentication](../restful-authentication) for details.
- The request body:

#### Update the subscription lists
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "streamSubscribe": {
            "audioUidList": {
                "subscribeAudioUids": [
                    "#allstream#"
                ]
            },
            "videoUidList": {
                "unSubscribeVideoUids": [
                    "444",
                    "555",
                    "666"
                ]
            }
        }
    }
}                                              
```

#### Update the web page recording config
```json
{
    "cname":"httpClient463224",
    "uid":"527841",
    "clientRequest":{
        "webRecordingConfig":{
            "url": "https://xxxxx", 
            "onhold": false
        }
   }
}
```
#### Update the CDN address which you push stream to during a web page recording
```json
{
    "cname":"httpClient463224",
    "uid":"527841",
    "clientRequest":{
        "rtmpPublishConfig": {
          "outputs": [
             {
                "rtmpUrl": "rtmp://xxx"
             }
           ]
        }
    }
}
```

### HTTP response

If the returned HTTP status code is `200`, it means the request was successful, and the response body contains the following fields:
- `code`: Number. [Status code](../common-errors#status-codes).
- `resourceId`: String. The resource ID for cloud recording.
- `sid`: String. The recording ID. The unique identification of the current recording.

### Response example

```json
"Code": 200,
"Body":
{
    "sid": "38f8e3cfdc474cd56fc1ceba380d7e1a",
    "resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG"
}
```

## updateLayout: Update the video mixing layout

During a recording, you can call this method to update the video mixing layout multiple times.

This method call overrides the existing layout configurations. For example, if you set the `backgroundColor` parameter as `"#FF0000"` (red) when starting a recording and call this method to update the layout without setting the `backgroundColor` parameter, the background color changes back to black (the default value).

- Method: POST
- Endpoint: /v1/apps/\<appid\>/cloud_recording/resourceid/\<resourceid\>/sid/\<sid\>/mode/\<mode\>/updateLayout

> The request frequency limit is 10 requests per second for each [Agora account](../manage-agora-account#create-an-agora-account). Contact [Agora technical support](mailto:support@agora.io) if you want to raise the limit.

### HTTP request

The following parameters are required in the URL.

| Parameter    | Type   | Description                                                               |
| :----------- | :----- |:--------------------------------------------------------------------------|
| `appid`      | String | The App ID used in the channel to be recorded.                            |
| `resourceid` | String | The resource ID requested by the [`acquire`](../rest-api/acquire) method. |
| `sid`        | String | The recording ID created by the [`start`](../rest-api/start) method.      |
| `mode`       | String | The recording mode. Supports composite mode (`mix`) only.                 |

The following parameters are required in the request body.

| Parameter       | Type   | Description                                                                                                                             |
| :-------------- | :----- |:----------------------------------------------------------------------------------------------------------------------------------------|
| `cname`         | String | The name of the channel to be recorded.                                                                                                 |
| `uid`           | String | A string that contains the user ID of the recording client. Must be the same `uid` used in the [`acquire`](../rest-api/acquire) method. |
| `clientRequest` | JSON   | A specific client request. See the following list for details.                                                                          |

`clientRequest` requires the following parameters:

- `maxResolutionUid`: (Optional) String. When the `layoutType` parameter is set as `2` (vertical layout), you can specify the user ID of the large video window by this parameter.
- `mixedVideoLayout`: (Optional) Number. The video mixing layout. 0, 1, and 2 are the [predefined layouts](../../develop/layout#predefined-layout-types). If you set this parameter as 3, you need to set the layout by the `layoutConfig` parameter.
    - `0`: (Default) Floating layout. The first user in the channel occupies the full canvas. The other users occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel. This layout supports one full-size region and up to four rows of small regions on top with four regions per row, comprising 17 users.
    - `1`: Best fit layout. This is a grid layout. The number of columns and rows and the grid size vary depending on the number of users in the channel. This layout supports up to 17 users.
    - `2`: Vertical layout. One large region is displayed on the left edge of the canvas, and several smaller regions are displayed along the right edge of the canvas. The space on the right supports up to 2 columns of small regions with 8 regions per column. This layout supports up to 17 users.
    - `3`: Customized layout. Set the `layoutConfig` parameter to customize the layout.
- `backgroundColor`: (Optional) String. The background color of the video canvas. Supports RGB color codes that start with a hashtag(#) followed by six hexadecimal numbers. The default value is `"#000000"`, the black color.
- `backgroundImage`: (Optional) String. The URL address of the background image of the video canvas. The display mode of the background image is cropped mode. In cropped mode, the recording service uniformly scales the image until it fills the visible boundaries (cropped). One dimension of the image may have clipped contents.
- `defaultUserBackgroundImage`: (Optional) String. The URL address of the default background image of the user regions. After you set this parameter, the user region switches to the background image 3.5 seconds after a user stops sending the video stream; if you set a different background image for a specific user ID, this setting is overridden for that user ID.
- `layoutConfig`: (Optional) JSONArray. An array of the configuration of each user's region. Supports 17 users at most. Each user's region configuration is a JSON object with the following parameters:
    - `uid`: (Optional) String. The string contains the user ID of the user displaying the video in the region. If this parameter is not specified, the configurations apply in the order of the users joining the channel.
    - `x_axis`: Float. The relative horizontal position of the top-left corner of the region. The value is between 0.0 (leftmost) and 1.0 (rightmost). `x_axis` can also be an integer 0 or 1.
    - `y_axis`: Float. The relative vertical position of the top-left corner of the region. The value is between 0.0 (top) and 1.0 (bottom). `y_axis` can also be an integer 0 or 1.
    - `width`: Float. The relative width of the region. The value is between 0.0 and 1.0. `width` can also be an integer 0 or 1.
    - `height`: Float. The relative height of the region. The value is between 0.0 and 1.0. `height` can also be an integer 0 or 1.
    - `alpha`: (Optional) Float. The transparency of the image. The value is between 0.0 (transparent) and 1.0 (opaque). The default value is 1.0.
    - `render_mode`: (Optional) Number. The video display mode:
        - `0`: (Default) Cropped mode. Uniformly scales the video until it fills the visible boundaries (cropped). One dimension of the video may have clipped contents.
        - `1`: Fit mode. Uniformly scales the video until one of its dimension fits the boundary (zoomed to fit). Areas that are not filled due to the disparity in the aspect ratio will be filled with black.
- `backgroundConfig:` (Optional) JSONArray. The array contains the background configuration for specific user IDs.
    - `uid`: String. User ID (user ID).
    - `image_url`: String. The URL address of the background image of the user ID. After you set the background image, the user region switches to the background image 3.5 seconds after the user stops sending the video stream.
    - `render_mode`: (Optional) Number. The display mode.
        - 0: (Default) Cropped mode. Uniformly scales the image until it fills the visible boundaries (cropped). One dimension of the image may have clipped contents.
        - 1: Fit mode. Uniformly scales the video until one of its dimension fits the boundary (zoomed to fit). Areas that are not filled due to the disparity in the aspect ratio will be filled with black.

In the above background image settings, the URL supports the HTTP and HTTPS protocols, and the background image supports the JPG and BMP formats. The size of the image should not exceed 6MB. The settings take effect only after the recording service successfully downloads the picture. Settings may be overridden if their priorities are low. See <a href="../../develop/layout#set-the-background-color-or-background-image">Set the background color or background image</a> for details.


### Request example

- The request URL is:

```html
https://api.agora.io/v1/apps/<appid>/cloud_recording/resourceid/<resourceid>/sid/<sid>/mode/<mode>/updateLayout
```

- `Content-type` is `application/json;charset=utf-8`.
- `Authorization` is the basic authorization, see [RESTful API authentication](../restful-authentication) for details.
- The request body:

```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "mixedVideoLayout": 3,
        "backgroundColor": "#FF0000",
        "layoutConfig": [
        {
             "uid": "1",
             "x_axis": 0.1,
             "y_axis": 0.1,
             "width": 0.1,
             "height": 0.1,
             "alpha": 1.0,
             "render_mode": 1
         },
        {
             "uid": "2",
             "x_axis": 0.2,
             "y_axis": 0.2,
             "width": 0.1,
             "height": 0.1,
             "alpha": 1.0,
             "render_mode": 1
         }
         ]
     }
}
```

### HTTP response

If the returned HTTP status code is `200`, it means the request was successful, and the response body contains the following fields:

- `code`: Number. [Status code](../common-errors#status-codes).
- `resourceId`: String. The resource ID for cloud recording. The resource ID is valid for five minutes.
- `sid`: String. The recording ID. The unique identification of the current recording.


### Response example

```json
"Code": 200,
"Body":
{
    "sid": "38f8e3cfdc474cd56fc1ceba380d7e1a",
    "resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG"
}
```
