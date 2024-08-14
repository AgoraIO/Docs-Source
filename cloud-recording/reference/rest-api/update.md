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

| Parameter       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------- | :----- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cname`         | String | The name of the channel to be recorded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `uid`           | String | A string that contains the user ID of the recording client. Must be the same user ID used in the [`acquire`](../rest-api/acquire) method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `clientRequest` | JSON   | A specific client request that includes the `streamSubscribe`, `webRecordingConfig`, `rtmpPublishConfig`, and `storageConfig` parameters.<li>Use `streamSubscribe` to update the subscription list. This is only applicable to individual recording (`individual`) and composite recording (`mix`).</li><li>Use `webRecordingConfig` to update parameters of web page recording. This is only applicable to Web page recording (`web`).</li><li>Use `rtmpPublishConfig` to update parameters of pushing media stream to the CDN during a web page recording. This is only applicable to Web page recording (`web`).</li><li>Use `storageConfig` to update the configuration items of third-party cloud storage.</li> |

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

`rtmpPublishConfig` requires the following parameters:

- `outputs`：JSON Array. Configure as follows:
- `rtmpUrl`：String. The CDN address which you want to push stream to.

`storageConfig` requires the following parameters:

- `vendor`: Number. The third-party cloud storage vendor.

  - `1`: [Amazon S3](https://aws.amazon.com/s3/?nc1=h_ls)
  - `2`: [Alibaba Cloud](https://www.alibabacloud.com/product/object-storage-service)
  - `3`: [Tencent Cloud](https://intl.cloud.tencent.com/product/cos)
  - `4`: [Kingsoft Cloud](https://en.ksyun.com/nv/product/KS3)
  - `5`: [Microsoft Azure](https://azure.microsoft.com/en-us/services/storage/blobs/)
  - `6`: [Google Cloud](https://cloud.google.com/storage)
  - `7`: [Huawei Cloud](https://www.huaweicloud.com/intl/en-us/product/obs)
  - `8`: [Baidu AI Cloud](https://intl.cloud.baidu.com/product/bos.html)

- `region`: Number. The region information specified for the third-party cloud storage. The recording service only supports regions in the following lists:

  In order to improve the success rate and real-time performance when uploading recording files, if you set the `region` of the cloud recording service in the `acquire` method, make sure that the region of the third-party cloud storage corresponds to the same geographical region. For example, if the region of the cloud recording service is set to `NA` (North America), the third-party cloud storage needs to be set to a location within North America.

  - Third-party cloud storage is Amazon S3 (`vendor` = 1):
    - `0`: US_EAST_1
    - `1`: US_EAST_2
    - `2`: US_WEST_1
    - `3`: US_WEST_2
    - `4`: EU_WEST_1
    - `5`: EU_WEST_2
    - `6`: EU_WEST_3
    - `7`: EU_CENTRAL_1
    - `8`: AP_SOUTHEAST_1
    - `9`: AP_SOUTHEAST_2
    - `10`: AP_NORTHEAST_1
    - `11`: AP_NORTHEAST_2
    - `12`: SA_EAST_1
    - `13`: CA_CENTRAL_1
    - `14`: AP_SOUTH_1
    - `15`: CN_NORTH_1
    - `16`: CN_NORTHWEST_1
    - `17`: US_GOV_WEST_1
    - `20`：AP_NORTHEAST_3
    - `21`：EU_NORTH_1
    - `22`：ME_SOUTH_1
    - `23`：US_GOV_EAST_1
    - `24`: AP_SOUTHEAST_3
    - `25`: EU_SOUTH_1
    - `28`: IL_CENTRAL_1
  - Third-party cloud storage is Alibaba Cloud (`vendor` = 2):
    - `0`: CN_Hangzhou
    - `1`: CN_Shanghai
    - `2`: CN_Qingdao
    - `3`: CN_Beijing
    - `4`: CN_Zhangjiakou
    - `5`: CN_Huhehaote
    - `6`: CN_Shenzhen
    - `7`: CN_Hongkong
    - `8`: US_West_1
    - `9`: US_East_1
    - `10`: AP_Southeast_1
    - `11`: AP_Southeast_2
    - `12`: AP_Southeast_3
    - `13`: AP_Southeast_5
    - `14`: AP_Northeast_1
    - `15`: AP_South_1
    - `16`: EU_Central_1
    - `17`: EU_West_1
    - `18`: EU_East_1
    - `19`：AP_Southeast_6
    - `20`：CN_Heyuan
    - `21`：CN_Guangzhou
    - `22`：CN_Chengdu
    - `23`: CN_Nanjing
    - `24`: CN_Fuzhou
    - `25`: CN_Wulanchabu
    - `26`: CN_Northeast_2
    - `27`: CN_Southeast_7
      For details, see <a href="https://www.alibabacloud.com/help/doc-detail/31837.html">Alibaba Cloud Documentation</a>.
  - Third-party cloud storage is Tencent Cloud (`vendor` = 3):
    - `0`：AP_Beijing_1
    - `1`：AP_Beijing
    - `2`：AP_Shanghai
    - `3`：AP_Guangzhou
    - `4`：AP_Chengdu
    - `5`：AP_Chongqing
    - `6`：AP_Shenzhen_FSI
    - `7`：AP_Shanghai_FSI
    - `8`：AP_Beijing_FSI
    - `9`：AP_Hongkong
    - `10`：AP_Singapore
    - `11`：AP_Mumbai
    - `12`：AP_Seoul
    - `13`：AP_Bangkok
    - `14`：AP_Tokyo
    - `15`：NA_Siliconvalley
    - `16`：NA_Ashburn
    - `17`：NA_Toronto
    - `18`：EU_Frankfurt
    - `19`：EU_Moscow
  - Third-party cloud storage is Kingsoft Cloud (`vendor` = 4):
    - `0`：CN_Hangzhou
    - `1`：CN_Shanghai
    - `2`：CN_Qingdao
    - `3`：CN_Beijing
    - `4`：CN_Guangzhou
    - `5`：CN_Hongkong
    - `6`：JR_Beijing
    - `7`：JR_Shanghai
    - `8`：NA_Russia_1
    - `9`：NA_Singapore_1
  - Third-party cloud storage is Microsoft Azure (`vendor` = 5), the `region` parameter has no effect, if it is set or not.
  - Third-party cloud storage is Google Cloud (`vendor` = 6), the `region` parameter has no effect, if it is set or not.
  - Third-party cloud storage is Huawei Cloud (`vendor` = 7):
    - `0`：CN_North_1
    - `1`：CN_North_4
    - `2`：CN_East_2
    - `3`：CN_East_3
    - `4`：CN_South_1
    - `5`：CN_Southwest_2
    - `6`：AP_Southeast_1
    - `7`：AP_Southeast_2
    - `8`：AP_Southeast_3
    - `9`：AF_South_1
    - `10`：SA_Argentina_1
    - `11`：SA_Peru_1
    - `12`：NA_Mexico_1
    - `13`：SA_Brazil_1
    - `14`：LA_South_2
    - `15`：SA_Chile_1
  - Third-party cloud storage is Huawei Cloud (`vendor` = 7):
    - `0`：CN_North_1
    - `1`：CN_North_4
    - `2`：CN_East_2
    - `3`：CN_East_3
    - `4`：CN_South_1
    - `5`：CN_Southwest_2
    - `6`：AP_Southeast_1
    - `7`：AP_Southeast_2
    - `8`：AP_Southeast_3
    - `9`：AF_South_1
    - `10`：SA_Argentina_1
    - `11`：SA_Peru_1
    - `12`：NA_Mexico_1
    - `13`：SA_Brazil_1
    - `14`：LA_South_2
    - `15`：SA_Chile_1
  - Third-party cloud storage is Baidu AI Cloud (`vendor` = 8):
    - `0`：Beijing
    - `1`：Baoding
    - `2`：Suzhou
    - `3`：Guangzhou
    - `4`：Hongkong
    - `5`：Singapore
    - `6`：Wuhan
    - `7`：Shanghai

- `bucket`: String. The bucket name of the third-party cloud storage.

- `accessKey`: String. The access key of the third-party cloud storage. Agora suggests that you use a write-only access key.

- `secretKey`: String. The secret key of the third-party cloud storage.

- `stsToken`: String. A temporary security token for third-party cloud storage. This token is issued by the cloud service provider's Security Token Service (STS) and used to grant limited access rights to third-party cloud storage resources.

  <Admonition type="info" title="Note">Currently supported cloud service providers include only the following: `1`: Amazon S3, `2`: Alibaba Cloud, `3`: Tencent Cloud.</Admonition>

- `stsExpiration`: Number. The `stsToken` expiration timestamp used to mark UNIX time, in seconds.

  <Admonition type="info" title="Note"><ul><li>To avoid timestamp overflow, use Uint64 storage.</li><li>Set the longest possible validity period when applying the `stsToken`. The minimum validity period must be at least 4 hours. Call `update` to update the `stsToken` value before it expires.</li><li>If the recording task lasts for more than 1 hour, reapply the `stsToken` every 60 minutes and call `update` to update the relevant parameters in `storageConfig`</li></ul></Admonition>

- `fileNamePrefix`: (Optional) JSONArray. An array of strings. Sets the path of the recorded files in the third-party cloud storage. For example, if `fileNamePrefix` = `["directory1","directory2"]`, Agora Cloud Recording will add the prefix "`directory1/directory2/`" before the name of the recorded file, that is, `directory1/directory2/xxx.m3u8`. The prefix's length, including the slashes, should not exceed 128 characters. The string itself should not contain symbols such as slash, underscore, or parenthesis. The supported characters are as follows:
  - The 26 lowercase English letters: a to z
  - The 26 uppercase English letters: A to Z
  - The 10 numbers: 0 to 9

- `extensionParams`: (Optional) JSON Object. The third-party cloud storage service encrypts and labels the uploaded recording files according to `extensionParams`, which contains the following fields:
  - `sse`：Encryption mode. The third-party cloud storage service encrypts the uploaded recording file according to the encryption mode. This field is only applicable to Amazon S3. See [official Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption) for details. It can be set to:
    - `kms`: KMS encryption.
    - `aes256`: AES256 encryption.
  - `tag`: Tag content. The third-party cloud storage service tags the uploaded recording file according to the tag content. This field is only applicable to Alibaba Cloud and Amazon S3. See [Alibaba Cloud official documentation](https://www.alibabacloud.com/help/en/doc-detail/106678) and [Amazon S3 official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging) for details.


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
            "onhold": true
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
