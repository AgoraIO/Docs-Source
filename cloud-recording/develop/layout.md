---
title: "Set video layout"
sidebar_position: 6
type: docs
platform_selector: false
description: >
  Explains the layout types you can choose in a composite recording.
---

This page explains the layout types you can choose in a composite recording. See [Composite Recording](../develop/composite-mode) for more details about this recording mode

When there are multiple users sending streams in a channel, the Agora Cloud Recording Service mixes the streams of all the users into one stream. This is called **composite recording** mode. This page shows you how to set the video layout for composite recording.

As shown in the following image, the background of the video is **canvas**, and each user occupies a **region** on the canvas.

![](https://web-cdn.agora.io/docs-files/1577697787996)

You can set the video layout in two ways:

- [Select from the predefined layout types](#select-from-the-predefined-layout-types) (Floating Layout, Best Fit Layout, and Vertical Layout).
- [Customize the video layout](#customize-the-video-layout).

<Admonition type="info">
- The canvas can display up to 17 regions.
- If a user sends only audio, the user occupies a region.
- If the aspect ratio of a user's video does not match that of the user's region, the video may be cropped or scaled to fit the region. The aspect ratio of the user's region depends on the aspect ratio of the canvas and the layout type.
</Admonition>

## Select from the predefined layout types

The Agora Cloud Recording Service provides the following predefined layout types:

- [Floating Layout](#float): (Default) The first user in the channel occupies the full canvas. The other users occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel. This layout supports one full-size region and up to four rows of small regions on top with four regions per row, comprising 17 users.
- [Best Fit Layout](#bestfit): This is a grid layout. The number of columns and rows and the grid size vary depending on the number of users in the channel. This layout supports up to 17 users.
- [Vertical Layout](#vertical): One large region is displayed on the left edge of the canvas, and several smaller regions are displayed along the right edge of the canvas. The space on the right supports up to two columns of small regions with eight regions per column. This layout supports up to 17 users.

### Implementation

Set the `mixedVideoLayout` parameter in `transcodingConfig` as 0 (floating layout), 1 (best fit layout), or 2 (vertical layout) when calling the [`start`](../reference/restful-api#start) or [`updateLayout`](../reference/restful-api#updatelayout) method.

<Admonition type="info">
 If you set the `mixedVideoLayout` parameter as 0, 1, or 2, do not pass in the `layoutConfig` parameter.
</Admonition>

### Predefined layout types

This section describes the predefined layout types.

The numbers in the following figures indicate the order of users joining the channel. If user 1 leaves the channel, user 2 takes over user 1's region, and so on.

#### <a name="float"></a>Floating layout

This is the default layout, where small regions are on top of a full-size region. The first user in the channel occupies the full canvas. The other users occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel. This layout supports up to four rows of regions on top with four regions per row.

- If a user sends only audio, the user's region is transparent.
- If the aspect ratio of a user's video does not match that of the user's region, the video is cropped to fit the region.
- The width and height of each small region are 23.5% of those of the canvas. The gaps between two horizontally or vertically adjacent regions are 1.2 % of the width and height of the canvas respectively. The gap between the bottom row and the border-bottom is 1.2 % of the height of the canvas, and the left/right margin is also 1.2 % of the width of the canvas.


The following figures show the layouts with different number of users in the channel.

![](https://web-cdn.agora.io/docs-files/1577697865676)

![](https://web-cdn.agora.io/docs-files/1577697930206)

![](https://web-cdn.agora.io/docs-files/1577697950264)

#### <a name="bestfit"></a>Best fit layout

This is a grid layout. In this layout, the grid size varies depending on the number of users in the channel.

- The region that is not occupied by any user shows the background color.
- If a user sends only audio, the user's region shows the background color.
- If the aspect ratio of a user's video does not match that of the user's region, the video is cropped to fit the region.

The following figures show the layouts with different number of users in the channel.

![](https://web-cdn.agora.io/docs-files/1577697975441)

![](https://web-cdn.agora.io/docs-files/1577697997849)

![](https://web-cdn.agora.io/docs-files/1577698010532)

**17 Users**

The best fit layout for 17 users in a channel is unique.

As shown in the following figure, the regions are displayed across the middle of the canvas with bands on the left and right of the canvas. The width and height of each region are 20% of those of the canvas respectively, while the width of the two bands is 10% of that of the canvas. The 17<sup>th</sup> region is placed in the middle of the bottom row.

![](https://web-cdn.agora.io/docs-files/1577698032073)

#### <a name="vertical"></a>Vertical layout

In this layout, one large region is displayed on the left edge of the screen, and several smaller regions are displayed along the right edge of the screen.

Therefore, when you start cloud recording, you must specify a uid, whose region is displayed on the left edge of the screen in a large size.  

To specify a uid, set the `maxResolutionUid` parameter when calling the [`start`](../reference/restful-api#start) or [`updateLayout`](../reference/restful-api#updatelayout) method.

Sample code:
```json
"transcodingConfig": {
  "mixedVideoLayout": 2,
  "maxResolutionUid": "123456"
}
```

This layout supports up to two columns of small regions on the right edge with eight regions per column. 

- In the following figures, "Large" refers to the large region displaying the video of the specified user. 
	- If you do not specify a user or the specified user does not join the channel, the "Large" region shows the background color.
	- If the aspect ratio of the specified user's video does not match that of the large region, the video is scaled to fit the region, ensuring the completeness of the video.
- The small regions are tiled in the order of the users joining the channel. 
	- If user small 1 leaves the channel, user small 2 takes over user small 1's region, and so on.
	- If the aspect ratio of a user's video does not match that of the user's region, the video is cropped to fit the region.
- The region that is not occupied by any user shows the background color.
- If a user sends only audio, the user's region shows the background color.

See the following pictures for the layouts with different number of users in the channel.

![](https://web-cdn.agora.io/docs-files/1577698419720)

- For the layout of 1 to 5 users, the regions of users 1 to 4 are tiled along the right edge of the canvas. The width and height of the small region are one-fifth and one-fourth of those of the canvas respectively.
- For the layout of 6 to 7 users, the regions of users 1 to 6 are tiled along the right edge of the canvas. The width and height of the small region are one-seventh and one-sixth of those of the canvas respectively.

![](https://agora-doc.s3.us-east-1.amazonaws.com/images/cloud-recording/vertical-layout.png)

- For the layout of 6 to 7 users, the regions of users 1 to 8 are tiled along the right edge of the canvas. The width and height of the small region are one-ninth and one-eighth of those of the canvas respectively.
- For the layout of 6 to 7 users, the regions of users 1 to 16 are tiled along the right edge of the canvas. The width and height of the small region are one-tenth and one-eighth of those of the canvas respectively.

## Customize the video layout

You can customize the video layout by setting the size and position of each user's region on the canvas.

<Admonition type="info">
Regardless of the number of users displaying in the canvas, the Cloud Recording Service subscribes to all the streams in the channel.
</Admonition>

### Implementation

#### Customize the video layout when starting recording

Set `mixedVideoLayout` as 3 (customized layout) and pass in the `layoutConfig` parameter when calling the [`start`](../reference/restful-api#start) method to start the recording.

```json
Body:
{
  ......
  "clientRequest": {
    .......
    "recordingConfig": {
      ........
      "transcodingConfig": {
        .......
        "mixedVideoLayout": 3
        "layoutConfig":[
        {
          ........
        }]
      }
    },
  .......
  }
}
```

`layoutConfig` is an array consisting of the configurations of the user regions. You can configure up to 17 regions.

The configuration of a user region is a JSON object with the following parameters:

| Parameter        | Type   | Description                                                                                                                                                                                                                                 |
| :---------- | :----- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uid`         | String | (Optional) A string that contains the user ID of the user whose video you want to display in the region, for example, "527841". If this parameter is not specified, the configurations apply in the order of the users joining the channel. |
| `x_axis`      | Float  | (Mandatory) The relative horizontal position of the top-left corner of the region. The value is between 0.0 (leftmost) and 1.0 (rightmost).                                                                                                 |
| `y_axis`    | Float  | (Mandatory)  The relative vertical position of the top-left corner of the region. The value is between 0.0 (top) and 1.0 (bottom).                                                                                                          |
| `width`     | Float  | (Mandatory) The relative width of the region. The value is between 0.0 and 1.0.                                                                                                                                                             |
| `height`      | Float  | (Mandatory) The relative height of the region. The value is between 0.0 and 1.0.                                                                                                                                                            |
| `alpha`       | Float  | (Optional) The transparency of the image. The value is between 0.0 (transparent) and 1.0 (opaque). The default value is 1.0.                                                                                                                |
| `render_mode` | Integer | (Optional) The video display mode: <ul><li>0: (Default) Cropped mode. </li><li>1: Scaled to fit mode</li> </ul>.|

![](https://web-cdn.agora.io/docs-files/1563180630268)
	
As shown in the figure above, we set the upper left corner of the video canvas as the origin. The `x_axis` and `y_axis` parameters define the relative position of a user's region on the canvas, representing the horizontal and vertical distance between the upper left corner of the region and the origin respectively. The `width` and `height` parameters define the relative width and relative height of the region. The `x_axis`, `y_axis`, `width`, and `height` parameters are floats between 0.0 and 1.0. Ensure that x_axis + width &lt;= 1, and y_axis + height &lt;= 1.

For example, in the interactive live streaming, a host can invite the audience to become guest hosts. When you start the recording, you know the user ID of the host but the user IDs of the guest hosts change. The following sample code is for the layout of three hosts: one large region for the main host and two small regions for the guest hosts. The guest hosts occupy the small regions in the order of joining the channel.

Sample code:

```json
"transcodingConfig": {
  "mixedVideoLayout": 3,
  "backgroudColor": "#FF0000",
  "layoutConfig": [
  {
    "uid": "1",
    "x_axis": 0.0,
    "y_axis": 0.0,
    "width": 1.0,
    "height": 0.5,
    "alpha": 1.0,
    "render_mode": 1
  },
  {
    "x_axis": 0.0,
    "y_axis": 0.5,
    "width": 0.5,
    "height": 0.5,
    "alpha": 1.0,
    "render_mode": 1
  },
  {
    "x_axis": 0.5,
    "y_axis": 0.5,
    "width": 0.5,
    "height": 0.5,
    "alpha": 1.0,
    "render_mode": 1
  }]
}
```
	
The following figure shows the layout of the sample code:

![](https://web-cdn.agora.io/docs-files/1563183775409)

#### Update the customized layout during a recording

During a recording, you can call the [`updateLayout`](../reference/restful-api#updatelayout) method to update the video mixing layout multiple times.

To update a customized layout, set the `mixedVideoLayout` parameter as 3 (customized layout), and populate `layoutConfig`.

Sample code:

```
"clientRequest": {
  "mixedVideoLayout": 3,
  "backgroundColor": "#0000FF",
  "layoutConfig": [
  {
    "uid": "1",
    "x_axis": 0.0,
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
  }]
},
```

<a name="background"></a>
## Set the background color or background image

You can set the background color or background image of the canvas or a user region when you call the `start` or `updateLayout` methods. 3.5 seconds after a user stops sending video streams, the user region switches to the background image or background color.

### Sample code

```json
"transcodingConfig": {
    ......
    "backgroundColor": "#FF0000",
    "defaultUserBackgroundImage": "https://xx.xxx/xxx.jpg",
    "backgroundConfig": [{
        "uid": "16",
        "image_url": "https://xx.xxx.xxx/xxx.bmp",
        "render_mode": 0
    },
    {
        "uid": "17",
        "image_url": "https://xx.xxx.xxx/xxx.bmp",
        "render_mode": 0
    }]
}
```

The following figure shows the corresponding layout of the sample code:

![](https://web-cdn.agora.io/docs-files/1617180127672)

- The canvas uses `"#FF0000"` (black) as the background color, set by the `backgroundColor` parameter.
- User 1-15 use the default background image for the user region, set by the `defaultUserBackgroundImage` parameter.
- User 16 and17 use the background image for individual user regions, set by the `image_url` parameter.

### Considerations

- Settings for the background color and the background image are overridden if their priorities are low. The parameters are listed from high to low priority as follows:
  - The `image_url` field in `backgroundConfig` (the background image of an individual user)
  - `defaultUserBackgroundImage` (the default background image of user regions)
  - `backgroundImage` (the background image of the canvas)
  - `backgroundColor` (the background color of the canvas)
- If a user leaves the channel in the middle of a call, the user region displays different contents in different circumstances. Refer to [Considerations](../develop/composite-mode#considerations) in *Composite Recording* for details.