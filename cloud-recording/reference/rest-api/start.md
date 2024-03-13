---
title: "Start recording"
sidebar_position: 4
type: docs
platform_selector: false
description: >
  Begin cloud recording
---

After getting a resource ID, call the `start` method to begin cloud recording. The Cloud Recording service does the following after you call `start`:

1. [Subscribes](../glossary#subscribe) to the audio and video streams in the channel according to `recordingConfig`.
2. Processes the subscribed media streams, such as generating recorded files in the specified file format, taking video screenshots, or uploading recorded files to an extension service.
3. Uploads the recorded files or screenshots to your third-party cloud storage according to `storageConfig`.

The HTTP method and endpoint of `start`:

- Method: POST
- Endpoint: /v1/apps/\<appid\>/cloud_recording/resourceid/\<resourceid\>/mode/\<mode\>/start

> The request frequency limit is 10 requests per second for each [Agora account](../manage-agora-account#create-an-agora-account). Contact [Agora technical support](mailto:support@agora.io) if you need to raise the limit.

## HTTP request

The following parameters are required in the URL.

| Parameter    | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| :----------- | :----- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `appid`      | String | Your App ID.                                                                                                                                                                                                                                                                                                                                                                                     |
| `resourceid` | String | The resource ID requested by the [`acquire`](../rest-api/acquire) method.                                                                                                                                                                                                                                                                                                                        |
| `mode`       | String | One of the following three recording modes:<ul><li> Individual recording (`individual`): Records the audio and video of each user ID in separate files.</li><li> Composite recording (`mix`): (Default) Records the audio and video of multiple user IDs in a single file.</li><li>Web page recording (`web`): Records the content and audio on a specified web page in a single file.</li></ul> |

The following parameters are required in the request body.

| Parameter       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :-------------- | :----- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cname`         | String | <ul><li> In web page recording mode, use `cname` to distinguish between recording sessions.</li><li> In other recording modes, use `cname` to set the name of the channel to be recorded. </li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `uid`           | String | A string containing the user ID of the recording client. Must be the same `uid` used in the [`acquire`](../rest-api/acquire) method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `clientRequest` | JSON   | A specific client request that requires the following parameters: <ul><li>[`token`](../glossary#token): String. The dynamic key used for the channel to record. Ensure that you set this parameter if App Certificate is enabled for your application. See [Secure authentication with tokens](../../develop/authentication-workflow).</li><li>[`recordingConfig`](#recordingConfig): JSON. Configurations for subscribing to media streams.</li><li>[`recordingFileConfig`](#recordingFileConfig): JSON. Configurations for the recorded files.</li><li>[`snapshotConfig`](#snapshotConfig): JSON. Video screenshot configurations.</li><li>[`storageConfig`](#storageConfig): JSON. Third-party cloud storage configurations.</li><li>[`extensionServiceConfig`](#extensionServiceConfig): JSON. Configurations for third-party extension services. </li><li>`appsCollection`: JSON. Configurations of application combinations.</li><li>`transcodeOptions`: JSON. Configuration of the recording files generated during postpone transcoding and audio mixing.</li></ul> |

### Application configuration

`appsCollection` is a JSON Object for configuring how the application services are combined and applied. It contains the following fields:

- `combinationPolicy`: (Optional) JSON Object. The combination method of various Cloud Recording applications.
  - `default`: (Default) String.  Use this method for all application services except for Postpone Audio Mixing.
  - `postpone_transcoding`: Use this method if you use [Postpone Audio Mixing](../../develop/individual-nontranscoding#implement-an-postpone-audio-mixing) and Postpone Transcoding. 
     
<a name="recordingConfig"></a>
### Recording configuration

`recordingConfig` is a JSON object for configuring how the Cloud Recording service subscribes to the media streams in the channel. `recordingConfig` has the following fields:

- `channelType`: Number. The channel profile. Agora Cloud Recording must use the same channel profile as the Agora <Vg k="VSDK" />. Otherwise, issues may occur.
  - `0`: (Default) Communication profile.
  - `1`: Live broadcast profile.
- `streamTypes`: (Optional) Number. The type of the media stream to subscribe to:
  - `0`: Subscribes to audio streams only.
  - `1`: Subscribes to video streams only.
  - `2`: (Default) Subscribes to both audio and video streams.
- `streamMode`: (Optional) String. The output mode of the media stream in individual recording mode.
- `default`: Default mode. The Cloud Recording service transcodes the audio stream during recording and generates a M3U8 audio index file and a M3U8 video index file.
- `standard`: Standard mode. Agora recommends that you use this mode. The Cloud Recording service transcodes the audio stream during recording and generates a M3U8 audio index file, a M3U8 video index file and a combined M3U8 audio and video index file. If VP9 encoding is used on the web side, a combined MPD audio and video index file are generated.
  When using the standard mode to generate MPD files, the player compatibility is as follows:
  - macOS: Movist/Chrome (47.0.2526.111+)
  - Windows: Media Player/KM Player/VLC Player/Chrome (49.0.2623+)
  - Linux: FFplay
- `original`: Original encoding mode, which takes effect only when `streamTypes` is `0`. The Cloud Recording service does not transcode the audio stream during recording and generates a M3U8 audio index file.
  The following table compares various aspects of the three modes of `streamMode`:
  | streamMode | Description                                                  | Index file generated                                         | Slice file generated                                         | Video encoded       | Audio encoded       | Features supported                                           |
  | :--------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :------------------ | :------------------ | :----------------------------------------------------------- |
  | `default`  | Default mode.                                                | One M3U8 audio index file and one M3U8 video index file are generated per user ID. | Multiple TS audio slice files and multiple TS video slice files are generated per user ID. | Does not transcode. | Transcodes.         | Individual Recording, Capturing Screenshots. |
  | `standard` | Standard mode.                                               | One M3U8 audio index file, one M3U8 video index file, and one combined M3U8 audio and video index file are generated per user ID. If VP9 encoding is used on the web side, a combined MPD audio and video index file is generated per user ID. | Multiple TS audio slice files and multiple TS video slice files are generated per user ID.If VP9 encoding is used on the web side, multiple WebM audio slice files and multiple WebM video slice files are generated per user ID. | Does not transcode. | Transcodes.         | Individual Recording and Capturing Screenshots.              |
  | `original` | Original encoding mode, which takes effect only when `streamTypes` is `0`. | One M3U8 audio index file is generated per user ID.          | Multiple TS audio slice files per user ID.                   | Not applicable.     | Does not transcode. | Individual Audio Non-transcoding Recording and Postpone Audio Mixing. |
- `decryptionMode`: (Optional) Number. The decryption mode, which corresponds to the encryption mode set by the Agora Native/Web SDK. When the channel is encrypted, Agora Cloud Recording uses `decryptionMode` to enable the built-in decryption function.
  - `0`: (Default) None.
  - `1`: AES_128_XTS. 128-bit AES encryption, XTS mode.
  - `2`: AES_128_ECB. 128-bit AES encryption, ECB mode.
  - `3`: AES_256_XTS.  256-bit AES encryption, XTS mode.
  - `4`: SM4_128_ECB. 128-bit SM4 encryption, ECB mode.
  - `5`: AES_128_GCM. 128-bit AES encryption, GCM mode.
  - `6`: AES_256_GCM. 256-bit AES encryption, GCM mode.
  - `7`: AES_128_GCM2. 128-bit AES encryption, GCM mode. Compared to AES_128_GCM encryption mode, AES_128_GCM2 encryption mode is more secure and requires you to set the secret and salt.
- `8`: AES_256_GCM2. 256-bit AES encryption, GCM mode. Compared to AES_256_GCM encryption mode, AES_256_GCM2 encryption mode is more secure and requires you to set the secret and salt.
- `secret`: (Optional) String. The decryption password when decryption mode is enabled. If `decryptionMode` is not `0`, you need to set this value.
- `salt`: (Optional) Base64 encoding, 32-bit bytes. The decryption [salt](/video-calling/develop/media-stream-encryption#_understand_the_tech) that needs to be set for the GCM2 encryption mode. If `decryptionMode` is `7` or `8`, you need to set this value.
- `audioProfile`: (Optional) Number. The profile of the output audio stream, including the sample rate, bitrate, encoding mode, and the number of channels. You cannot set this parameter in individual recording mode.
  - `0`: (Default) Sample rate of 48 kHz, music encoding, mono, and a bitrate of up to 48 Kbps.
  - `1`: Sample rate of 48 kHz, music encoding, mono, and a bitrate of up to 128 Kbps.
  - `2`: Sample rate of 48 kHz, music encoding, stereo, and a bitrate of up to 192 Kbps.
- `videoStreamType`: (Optional) Number. The type of the video stream to subscribe to.
  - `0`: (Default) Subscribes to the high-quality stream.
  - `1`: Subscribes to the low-quality stream.
- `maxIdleTime`: (Optional) Number. Agora Cloud Recording automatically stops recording and leaves the channel when there is no user in the recording channel after a time period (30 seconds by default) set by this parameter. The value range is from 5 to 2,592,000 (30 days). Once the recording stops, the recording service generates new recorded files if you call `start` for the second time.

  <ul><li>In a communication channel, the recording service does not recognize a channel as an idle channel, so long as the channel has users, regardless of whether they send stream or not.</li><li>If a live broadcast channel has an audience without a host for a set time (`maxIdleTime`), the recording service automatically stops and leaves the channel.</li></ul>

- `transcodingConfig`: (Optional) JSON. The video transcoding configuration. You cannot set this parameter in individual recording mode. If you set this parameter, ensure that you set `width`, `height`, `fps`, and `bitrate`. Refer to [Set the Video Profile](../../develop/recording-video-profile) for detailed information about setting `transcodingConfig`.
  - `width`: Number. The width of the mixed video (pixels). The default value is 360. `width` should not exceed 1920, and `width`*`height` should not exceed 1920 * 1080; otherwise, an error occurs.
  - `height`: Number. The height of the mixed video (pixels). The default value is 640. `height` should not exceed 1920, and `width`*`height`  should not exceed 1920 * 1080; otherwise, an error occurs.
  - `fps`: Number. The video frame rate (fps). The default value is 15.
  - `bitrate`: Number. The video bitrate (Kbps). The default value is 500.
  - `maxResolutionUid`: (Optional) String. When `mixedVideoLayout` is set as `2` (vertical layout), you can specify the user ID of the large video window by this parameter. It is a 32-bit unsigned integer within the range between 1 and (2<sup>32</sup>-1).
  - `mixedVideoLayout`: (Optional) Number. The video mixing layout. 0, 1, and 2 are the [predefined layouts](../../develop/layout#predefined-layout-types). If you set this parameter as 3, you need to set the layout by the `layoutConfig` parameter.
    - `0`: (Default) Floating layout. The first user in the channel occupies the full canvas. The other users occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel. This layout supports one full-size region and up to four rows of small regions on top with four regions per row, comprising 17 users.
    - `1`: Best fit layout. This is a grid layout. The number of columns and rows and the grid size vary depending on the number of users in the channel. This layout supports up to 17 users.
    - `2`: Vertical layout. One large region is displayed on the left edge of the canvas, and several smaller regions are displayed along the right edge of the canvas. The space on the right supports up to 2 columns of small regions with 8 regions per column. This layout supports up to 17 users. When `mixedVideoLayout` is set as `2`, you can specify the user ID of the large video window by `maxResolutionUid`.
    - `3`: Customized layout. Set the `layoutConfig` parameter to customize the layout.
  - `backgroundColor`: (Optional) String. The background color of the video canvas. Supports RGB color codes that start with a hashtag(#) followed by six hexadecimal numbers. The default value is `"#000000"`, the black color.
  - `backgroundImage`: (Optional) String. The URL address of the background image of the video canvas. The display mode of the background image is cropped mode. In cropped mode, the recording service uniformly scales the image until it fills the visible boundaries (cropped).  One dimension of the image may have clipped contents.
  - `defaultUserBackgroundImage`: (Optional) String. The URL address of the default background image of the user regions. After you set this parameter, the user region switches to the background image 3.5 seconds after a user stops sending the video stream; if you set a different background image for a specific user ID, this setting is overridden for that user ID.
  - `layoutConfig`: (Optional) JSONArray. An array of the configuration of each user's region. Supports 17 users at most. Each user's region configuration is a JSON object with the following parameters:
    - `uid`: (Optional) String. The string contains the user ID of the user displaying the video in the region. If this parameter is not specified, the configurations apply in the order of the users joining the channel.
    - `x_axis`: Float. The relative horizontal position of the top-left corner of the region. The value is between 0.0 (leftmost) and 1.0 (rightmost), and is accurate to six decimal places.
    - `y_axis`: Float. The relative vertical position of the top-left corner of the region. The value is between 0.0 (top) and 1.0 (bottom), and is accurate to six decimal places.
    - `width`: Float. The relative width of the region. The value is between 0.0 and 1.0, and is accurate to six decimal places.
    - `height`: Float. The relative height of the region. The value is between 0.0 and 1.0, and is accurate to six decimal places.
    - `alpha`: (Optional) Float. The transparency of the image. The value is between 0.0 (transparent) and 1.0 (opaque), and is accurate to six decimal places. The default value is 1.0.
    - `render_mode`: (Optional) Number. The video display mode:
      - `0`: (Default) Cropped mode. Uniformly scales the video until it fills the visible boundaries (cropped). One dimension of the video may have clipped contents.
      - `1`: Fit mode. Uniformly scales the video until one of its dimension fits the boundary (zoomed to fit). Areas that are not filled due to the disparity in the aspect ratio will be filled with black.
  - `backgroundConfig:` (Optional) JSONArray. The array contains the background configuration for specific user IDs.
    - `uid`: String. User ID (user ID).
    - `image_url`: String. The URL address of the background image of the user ID. After you set the background image, the user region switches to the background image 3.5 seconds after the user stops sending the video stream.
    - `render_mode`: (Optional) Number. The display mode.
      - `0`: (Default) Cropped mode. Uniformly scales the image until it fills the visible boundaries (cropped). One dimension of the image may have clipped contents.
      - `1`: Fit mode. Uniformly scales the video until one of its dimension fits the boundary (zoomed to fit). Areas that are not filled due to the disparity in the aspect ratio will be filled with black.

In the above background image settings, the URL supports the HTTP and HTTPS protocols, and the background image supports the JPG and BMP formats. The size of the image should not exceed 6MB. The settings take effect only after the recording service successfully downloads the picture. Settings may be overridden if their priorities are low. See <a href="../../develop/layout#set-the-background-color-or-background-image">Set the background color or background image</a> for details.

- `subscribeAudioUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose audio you want to subscribe. If you want to subscribe to all user IDs, you do not need to set this parameter. The length of the array should not exceed 32 user IDs. Agora recommends that you do not set the array as empty. Once you set the parameter, do not set `streamTypes` in `recordingConfig` as `1`. See [Set up subscription lists](../../develop/subscription) for details.

- `unSubscribeAudioUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose audio you do not want to subscribe. Once you set this parameter, the recording service subscribes to the audio of all user IDs except the specified ones. The length of the array should not exceed 32 user IDs. Agora recommends that you do not set the array as empty. Once you set the parameter, do not set `streamTypes` in `recordingConfig` as `1`. See [Set up subscription lists](../../develop/subscription) for details.

- `subscribeVideoUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose video you want to subscribe. If you want to subscribe to all user IDs, you do not need to set this parameter. The length of the array should not exceed 32 user IDs. Agora recommends that you do not set the array as empty. Once you set the parameter, do not set `streamTypes` in `recordingConfig` as `0`. See [Set up subscription lists](../../develop/subscription) for details.

- `unSubscribeVideoUids`: (Optional) JSONArray. An array of the user IDs (user IDs) of the users whose video you do not want to subscribe. Once you set this parameter, the recording service subscribes to the video of all user IDs except the specified ones. The length of the array should not exceed 32 user IDs. Agora recommends that you do not set the array as empty. Once you set the parameter, do not set `streamTypes` in `recordingConfig` as `0`. See [Set up subscription lists](../../develop/subscription) for details.

If you set up a subscription list for audio, but not for video, then Agora Cloud Recording will not subscribe to any video streams. If you set up a subscription list for video, but not for audio, then Agora Cloud Recording will not subscribe to any audio streams.

- `subscribeUidGroup`: (Optional) Number. The estimated maximum number of subscribed users. **You must set this parameter in individual mode.** For example, if `subscribeVideoUids` is `["100","101","102"]` and `subscribeAudioUids` is `["101","102","103"]`, the number of subscribed users is 4.

  - `0`: 1 to 2 user IDs
  - `1`: 3 to 7 user IDs
  - `2`: 8 to 12 user IDs
  - `3`: 13 to 17 user IDs
- `4`: 17 to 32 user IDs
- `5`: 32 to 49 user IDs

### Transcoding configuration

`transcodeOptions` is a JSON Object for configuring how the Cloud Recording service transcodes the recording files. It is applicable to [Postpone Audio mixing](../../develop/individual-nontranscoding#implement-an-postpone-audio-mixing) and contains the following fields:

- `container`: (Optional) JSON, transcoding profile：
  - `format`: String. Format of output audio file. It can be set to `mp3`, `m4a`, or `aac`. The default value is `mp3`.
- `transConfig`: (Required) JSON. Transcoding configuration：
  - `transMode`: String. Transcoding mode. It can only be set to `audioMix`.
- `audio`: JSON. Audio profile of the output recording file:
  - `sampleRate`: String. Audio sample rate (Hz). It can be set to `48000`, `32000`, or `16000`. The default value is `48000`.
  - `bitrate`: String. Audio bitrate (Kbps). It can only be set to the default value of `48000`.
  - `channels`: String. The number of channels. It can be set to `1` or `2`. The default value is `2`.

<a name="recordingFileConfig"></a>
### Configurations for the recorded files

`recordingFileConfig` is a JSON Object for configuring recorded files. You cannot set both `recordingFileConfig` and `snapshotConfig` at the same time, otherwise an error will occur. `recordingFileConfig `includes the following fields:

`avFileType`: (Optional) JSONArray.  An array of strings. Sets the format of the recorded files.
- `"hls"`: (Default) M3U8 and TS files.
- `"mp4"`: MP4 files. This value is for composite recording (`mix`) and web page recording (`web`) only. For composite recording, when the length of the recorded file reaches approximately 2 hours, or when the size of the file exceeds approximately 2 GB, the recording service automatically creates an additional MP4 file. For web page recording, when the length of the recorded file reaches `maxVideoDuration`, the recording service automatically creates an additional MP4 file.

You must set `"mp4"` together with `"hls"` (otherwise, the recording service returns error code `2`). After the recording is over, you will get both MP4 and HLS files.

<a name="snapshotConfig"></a>
### Snapshot configuration
Agora supports only taking screenshots in a recording process or recording and taking screenshots in a recording process.
`snapshotConfig` is a JSON object for configuring how Cloud Recording takes screenshots. Pay attention to the following parameters, as incorrect settings result in errors or failure to capture screenshots.

- In the URL of your request, `mode` must be `individual`.
- If you are recording and taking screenshots in a recording process, the `recordingFileConfig` parameter is required; if you are only taking screenshots in a recording process, you cannot set `recordingFileConfig` parameter.
- `streamTypes` must be `1` or `2`.
- If you have set `subscribeAudioUid`, you must also set `subscribeVideoUids`.

`snapshotConfig` includes the following fields:

- `captureInterval`: (Optional) Integer. The time interval (in seconds) between two successive screenshots. `captureInterval` should be within the range [1, 3600]. The default value is `10`.
- `fileType`: JSONArray. File format of the screenshots. `fileType` can only take `["jpg"]`, setting screenshots to the JPG format.

<a name="storageConfig"></a>
### Cloud storage configuration

`storageConfig` is a JSON object that configures the third-party cloud storage with the following fields.

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

- `fileNamePrefix`: (Optional) JSONArray. An array of strings. Sets the path of the recorded files in the third-party cloud storage. For example, if `fileNamePrefix` = `["directory1","directory2"]`, Agora Cloud Recording will add the prefix "`directory1/directory2/`" before the name of the recorded file, that is, `directory1/directory2/xxx.m3u8`. The prefix's length, including the slashes, should not exceed 128 characters. The string itself should not contain symbols such as slash, underscore, or parenthesis. The supported characters are as follows:
  - The 26 lowercase English letters: a to z
  - The 26 uppercase English letters: A to Z
  - The 10 numbers: 0 to 9

- `extensionParams`: (Optional) JSON Object. The third-party cloud storage service encrypts and labels the uploaded recording files according to `extensionParams`, which contains the following fields:
  - `sse`：Encryption mode. The third-party cloud storage service encrypts the uploaded recording file according to the encryption mode. This field is only applicable to Amazon S3. See [official Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption) for details. It can be set to:
    - `kms`: KMS encryption.
    - `aes256`: AES256 encryption.
  - `tag`: Tag content. The third-party cloud storage service tags the uploaded recording file according to the tag content. This field is only applicable to Alibaba Cloud and Amazon S3. See [Alibaba Cloud official documentation](https://www.alibabacloud.com/help/en/doc-detail/106678) and [Amazon S3 official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging) for details.

<a name="extensionServiceConfig"></a>
### Extension service configuration

`extensionServiceConfig` is a JSON Object for extension service configurations. Extension services are a collection of applications that process the media streams generated from the Agora <Vg k="VSDK" />. One example extension service is VoD service.

`extensionServiceConfig` has the following fields:

- `errorHandlePolicy`: (Optional) String. Error handling policy. You can only set it to the default value, `"error_abort"`, which means that once an error occurs to an extension service, all other non-extension services, such as stream subscription, also stop.
- `apiVersion`: (Optional) String. The version of the Cloud Recording RESTful API. The default value is `"v1"`.
- `extensionServices`: JSONArray. An array of the configuration for each extension service.

Currently you cannot configure more than one extension service per recording session.

Currently only composite recording is supported.

**Web page recording**
When using web page recording, `extensionServices` includes the following fields:
- `serviceName`: String. The name of the extension service. To use web page recording, set it as "`web_recorder_service`".
- `errorHandlePolicy`: (Optional) String. Error handling policy. Currently you can only set it to the default value, `"error_abort"`, which means that if an error occurs to the current extension service, other extension services also stop.
- `serviceParam`: JSON. Configurations for an extension service. To use web page recording, configure as follows:
- `url`：String. Sets the address of the web page to record.
- `videoBitrate`：(Optional) Number. Sets the bitrate of the video (Kbps). The value range is [50,8000]. The default value of `videoBitrate` varies according to the resolution of the output video:
  - If the resolution of the output video is greater than or equal to 1280 × 720, the default value of `videoBitrate` is 2000.
  - If the resolution of the output video is less than 1280 × 720, the default value of `videoBitrate` is 1500.
- `videoFps: (Optional)`Number. Sets the frame rate of the video (fps). The value range is [5,60]. The default value is 15.
- `audioProfile`：Number. Sets the sample rate, encoding mode, number of audio channels, and bitrate.
  - `0`: (Default) Sample rate of 48 kHz, music encoding, mono, and a bitrate of up to 48 Kbps.
  - `1`: Sample rate of 48 kHz, music encoding, mono, and a bitrate of up to 128 Kbps.
  - `2`: Sample rate of 48 kHz, music encoding, stereo, and a bitrate of up to 192 Kbps.
- `videoWidth`：Number. Sets the width of the video (pixels). The value range is [480,1920]. The product of `videoWidth` and `videoHeight` should not exceed 2,073,600 (1920 × 1080).
- `videoHeight`：Number. Sets the height of the video (pixels). The value range is [480,1920]. The product of `videoWidth` and `videoHeight` should not exceed 2,073,600 (1920 × 1080).
- `maxRecordingHour`: Number. Sets the maximum recording length (hours). If the limit is exceeded, the recording stops automatically. The value range is [1,720]. Agora recommend that you set a value smaller than the value of `resourceExpiredHour` specified in the `acquire` method.
  The charging will continue until the web page recording stops. You should set a reasonable `maxRecordingHour` based on the actual business scenario or actively stop the web page recording.
- `maxVideoDuration`: (Optional) Number. Sets the maximum duration (in minutes) of the MP4 slice file generated by the web page recording. The value range is [30,240], and the default value is 120 minutes. During a web page recording, when the length of the recorded file reaches around `maxVideoDuration`, the recording service creates another MP4 slice file.
- `onhold`: (Optional) Bool. Sets whether to pause the web page recording when starting the web page recording task.
  - `true`：Pauses the web page recording when starting the web page recording task. After the web page recording task is started, the web page recording is paused immediately. The recording service opens and renders the page to be recorded, but does not generate a slice file.
  - (Default) `false`: Starts the web page recording task and continue web page recording.
> Agora recommends that you use the `onhold` parameter as follows:
When calling the `start` method, set the `onhold` parameter to `true`, start and pause the web page recording, determine the appropriate time to start the web page recording, and call the `update` method and set the `onhold` parameter to `false` to continue the web page recording.
If you need to continuously call the `update` method to pause or resume page recording, call it after receiving the last HTTP response of `update`; otherwise the actual result may be inconsistent with your expectation.
- `readyTimeout`: (optional) Number. Sets the web page loading timeout limit, in seconds.The value range is [0,60].
- 0 or null, which means the web page loading status is not detected.
- An integer greater than or equal to 1, which sets the web page load timeout limit.
  If you set `readyTimeout` to less than 0 or a non-integer, an error code `2` is received.

**Push media stream to the CDN during a web page recording**
When pushing media stream to the CDN during a web page recording, `extensionServices` includes fields of web page recording and streaming. The fields of streaming are as follows:

- `serviceName`: String. The name of the extension service. To use web page recording, set it as "rtmp_publish_service".
- `errorHandlePolicy`: (Optional) String. Error handling policy. Currently you can only set it to the default value, "error_ignore", which means that if an error occurs to the current extension service, other extension services are not affected.
- `serviceParam`: JSON. Configurations for an extension service. To push media stream to the CDN during a web page recording, configure as follows:
- `outputs`：JSON Array. Configure as follows:
  - `rtmpUrl`：String. The CDN address which you want to push stream to.

## Request example

- The request URL is：

```html
https://api.agora.io/v1/apps/<yourappid>/cloud_recording/resourceid/<resourceid>/mode/<mode>/start
```

- `Content-type` is `application/json;charset=utf-8`.
- `Authorization` is basic HTTP authentication, see [RESTful API authentication](../restful-authentication) for details.
- The request body:

### Audio and video recording in a channel
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamMode": "default",
            "streamTypes": 2,
            "channelType": 0,
            "transcodingConfig": {
                "height": 640,
                "width": 360,
                "bitrate": 500,
                "fps": 15,
                "mixedVideoLayout": 1,
                "backgroundColor": "#FF0000"
            },
            "subscribeVideoUids": [
                "123",
                "456"
            ],
            "subscribeAudioUids": [
                "123",
                "456"
            ],
            "subscribeUidGroup": 0
        },
        "recordingFileConfig": {
            "avFileType": [
                "hls"
            ]
        },
        "storageConfig": {
            "accessKey": "xxxxxxf",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
            "extensionParams": {
                "tag":"xxxxxx",
                "sse":"kms"
           }
        }
    }
}
```

### VoD service
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 2,
            "channelType": 0,
            "subscribeUidGroup": 0
        },
        "extensionServiceConfig": {
            "extensionServices": [
                {
                    "serviceName": "aliyun_vod_service",
                    "serviceParam": {
                        "secretKey": "xxxxxx",
                        "accessKey": "xxxxxx",
                        "regionId": "cn-shanghai",
                        "apiData": {
                            "videoData": {
                                "title": "My Video",
                                "description": "This is my first video",
                                "coverUrl": "http://xxxxx"
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

### Capturing snapshots only

```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 2,
            "channelType": 0,
            "subscribeUidGroup": 0
        },
        "snapshotConfig": {
            "captureInterval": 5,
            "fileType": [
                "jpg"
            ]
        },
        "storageConfig": {
            "accessKey": "xxxxxxf",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

### Capturing snapshots and recording
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token if any>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 1,
            "channelType": 0
        },
        "snapshotConfig": {
            "captureInterval": 5,
            "fileType": [
                "jpg"
            ]
        },
        "recordingFileConfig": {
            "avFileType": [
                "hls"
            ]
        },
        "storageConfig": {
            "accessKey": "xxxxxxf",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

### Web page recording
```json
{
    "cname": "httpClient463224",
    "uid": "527841",
    "clientRequest": {
        "token": "<token>",
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
                        "maxRecordingHour": 3,
                        "maxVideoDuration": 200
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
### Push media stream to the CDN during a web page recording
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

### Individual audio non-transcoding recording
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "<token if any>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 0,
            "streamMode": "original",
            "channelType": 0,
            "videoStreamType": 0,
            "subscribeAudioUids": ["123","456"],
            "subscribeUidGroup": 0
        },
        "storageConfig": {
            "accessKey": "xxxxx",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": ["directory1","directory2"]
       }
   }
}
```
### Individual audio non-transcoding recording and postpone audio mixing
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "appsCollection": {
            "combinationPolicy": "postpone_transcoding"
        },
        "token": "<token if any>",
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 0,
            "streamMode": "original",
            "channelType": 0,
            "videoStreamType": 0,
            "subscribeAudioUids": [
                "123",
                "456"
            ],
            "subscribeUidGroup": 0
        },
        "transcodeOptions": {
            "container": {
                "format": "m4a"
            },
            "transConfig": {
                "transMode": "audioMix"
            },
            "audio": {
                "sampleRate": "xxxx",
                "bitrate": "xxxx",
                "channels": "xxxx"
            }
        },
        "storageConfig": {
            "accessKey": "xxxxx",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

### Postpone transcoding
```json
{
    "uid": "527841",
    "cname": "httpClient463224",
    "clientRequest": {
        "token": "",
        "appsCollection": {
            "combinationPolicy": "postpone_transcoding"
        },
        "recordingConfig": {
            "maxIdleTime": 30,
            "streamTypes": 2,
            "channelType": 0,
            "videoStreamType": 1,
            "subscribeVideoUids": [
                "123",
                "456"
            ],
            "subscribeAudioUids": [
                "123",
                "456"
            ],
            "subscribeUidGroup": 0
        },
        "storageConfig": {
            "accessKey": "xxxxxxf",
            "region": 3,
            "bucket": "xxxxx",
            "secretKey": "xxxxx",
            "vendor": 2,
            "fileNamePrefix": [
                "directory1",
                "directory2"
            ]
        }
    }
}
```

## HTTP response

If the returned HTTP status code is `200`, it means the request was successful, and the response body contains the following fields:
- `code`: Number. [Status code](../common-errors#status-codes).
- `resourceId`: String. The resource ID for cloud recording. The resource ID is valid for five minutes.
- `sid`: String. The recording ID. The unique identification of the current recording.

## Response example
```json
"Code": 200,
"Body":
{
"sid": "38f8e3cfdc474cd56fc1ceba380d7e1a",
"resourceId": "JyvK8nXHuV1BE64GDkAaBGEscvtHW7v8BrQoRPCHxmeVxwY22-x-kv4GdPcjZeMzoCBUCOr9q-k6wBWMC7SaAkZ_4nO3JLqYwM1bL1n6wKnnD9EC9waxJboci9KUz2WZ4YJrmcJmA7xWkzs_L3AnNwdtcI1kr_u1cWFmi9BWAWAlNd7S7gfoGuH0tGi6CNaOomvr7-ILjPXdCYwgty1hwT6tbAuaW1eqR0kOYTO0Z1SobpBxu1czSFh1GbzGvTZG"
}
```
