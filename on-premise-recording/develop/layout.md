---
title: 'Set Video Layout'
sidebar_position: 4
type: docs
description: >
  How to set video layout according to your use case.
---

## Overview
In the composite recording mode, you need to set the size and position of the region for each user in the layout.

As shown in the following image, the background of the video is **canvas**, and each user occupies a **region** on the canvas.

![](https://web-cdn.agora.io/docs-files/1577697787996)

<Admonition type="info">
If the aspect ratio of a user's video does not match that of the user's region, the video may be cropped or letterboxed to fit the region. The aspect ratio of the user's region depends on the aspect ratio of the canvas and the layout type.
</Admonition>

You can set the video layout in two ways:
- **Select from the predefined layout types**: If you start recording in the command line, you can selelct one of the three predefined video layouts provided by the demo of Agora On-Premise Recording:
 - Floating Layout
 - Best Fit Layout
 - Vertical Layout
- **Customize the video layout**: If you start recording by calling API methods, you can customize the video layout by setting the size and position of each user's region on the canvas.

## Select from the predefined layout types
### Implementation

When you start recording in the command line, set `--isMixingEnabled 1`  to use the composite mode and set the `--layoutMode` parameter to choose a layout:

- `--layoutMode 0` : [Floating Layout](#float). (Default) The first user in the channel occupies the full canvas. The other users occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel. This layout supports one full-size region and up to four rows of small regions on top with four regions per row, comprising 17 users.
- `--layoutMode 1`: [Best Fit Layout](#bestfit). This is a grid layout. The number of columns and rows and the grid size vary depending on the number of users in the channel. This layout supports up to 17 users.
- `--layoutMode 2`: [Vertical Layout](#vertical). One large region is displayed on the left edge of the canvas, and several smaller regions are displayed along the right edge of the canvas. The space on the right supports up to 2 columns of small regions with 8 regions per column. This layout supports up to 17 users.

### <a name="float"></a>Floating layout

This is the default layout, where small regions are on top of a full-size region. The first user in the channel occupies the full canvas. The other users occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel. This layout supports up to 4 rows of regions on top with 4 regions per row.

- If a user sends only audio, the user's region is transparent.
- If the aspect ratio of a user's video does not match that of the user's region, the video is cropped to fit the region.
- The width and height of each small region are 23.5% of those of the canvas. The gaps between two horizontally or vertically adjacent regions are 1.2 % of the width and height of the canvas respectively. The gap between the bottom row and the border-bottom is 1.2 % of the height of the canvas, and the left/right margin is also 1.2 % of the width of the canvas.

See the following pictures for the layouts with different number of users in the channel.

![](https://web-cdn.agora.io/docs-files/1577697865676)

![](https://web-cdn.agora.io/docs-files/1577697930206)

![](https://web-cdn.agora.io/docs-files/1577697950264)

### <a name="bestfit"></a>Best fit layout

This is a grid layout. In this layout, the grid size varies depending on the number of users in the channel.

- The region which is not occupied by any user shows the background color.
- If a user sends only audio, the user's region shows the background color.
- If the aspect ratio of a user's video does not match that of the user's region, the video is cropped to fit the region.

See the following pictures for the layouts with different number of users in the channel.

![](https://web-cdn.agora.io/docs-files/1577697975441)

![](https://web-cdn.agora.io/docs-files/1577697997849)

![](https://web-cdn.agora.io/docs-files/1577698010532)

The best fit layout for 17 users in a channel is unique. As shown in the following figure, the regions are displayed across the middle of the canvas with bands on the left and right of the canvas. The width and height of each region are 20% of those of the canvas respectively, while the width of the two bands is 10% of that of the canvas. The 17th region is placed in the middle of the bottom row.

![](https://web-cdn.agora.io/docs-files/1577698032073)

### <a name="vertical"></a>Vertical layout

In this layout, one large region is displayed on the left edge of the screen, and several smaller regions are displayed along the right edge of the screen.

Therefore, when you recording, you must  set the `--maxResolutionUid` parameter to specify a uid, whose region is displayed on the left edge of the screen in a large size.

This layout supports up to two columns of small regions on the right edge with eight regions per column.

- In the following figures, "Large" refers to the large region, displaying the video of the specified user.
	- If you do not specify a user or the specified user does not join the channel, the "Large" region shows the background color.
	- If the aspect ratio of the specified user's video does not match that of the large region, the video is letterboxed to fit within the region, ensuring the completeness of the video.
- The small regions are tiled in the order of the users joining the channel.
	- If user 1 leaves the channel, user 2 takes over user 1's region, and so on.
	- If the aspect ratio of a user's video does not match that of the user's region, the video is cropped to fit the region.
- The region which is not occupied by any user shows the background color.
- If a user sends only audio, the user's region shows the background color.

See the following pictures for the layouts with different number of users in the channel.

![](https://web-cdn.agora.io/docs-files/1577698419720)

- For the layout of 1 to 5 users, the regions of users 1 to 4 are tiled along the right edge of the canvas. The width and height of the small region are one-fifth and one-fourth of those of the canvas respectively.
- For the layout of 6 to 7 users, the regions of users 1 to 6 are tiled along the right edge of the canvas. The width and height of the small region are one-seventh and one-sixth of those of the canvas respectively.

![](https://web-cdn.agora.io/docs-files/1577698564432)

- For the layout of 6 to 7 users, the regions of users 1 to 8 are tiled along the right edge of the canvas. The width and height of the small region are one-ninth and one-eighth of those of the canvas respectively.
- For the layout of 6 to 7 users, the regions of users 1 to 16 are tiled along the right edge of the canvas. The width and height of the small region are one-tenth and one-eighth of those of the canvas respectively.

## Customize the video layout

If the predefined layout types do not meet your needs, you can call `setVideoMixingLayout` to customize the video layout. You can set the size and position of each user's region on the canvas.

### Implementation

After joining the channel, configure the video layout settings in the `VideoMixingLayout` class, and then call `setVideoMixingLayout` to implement the customized video layout.

![](https://web-cdn.agora.io/docs-files/1600078283568)

To configure the video layout settings, you need pass in the following parameters:

- `canvasWidth`: The width of the canvas in pixels.
- `canvasHeight`: The height of the canvas in pixels.
- `backgroundColor`: The background color of the canvas in RGB hex value, for example, `#000000`.
- `regionCount`: The number of the users (`COMMUNICATION` profile)/hosts (`LIVE_BROADCASTING` profile) in the channel.
- `regions`: An array consisting of the configurations of the user regions. The configuration of a user region has the following parameters to be set:
  - `uid`: The UID of the user (`COMMUNICATION` profile)/host (`LIVE_BROADCASTING` profile) displaying the video in the region. You can get the UID of the user/host joining the channel in the `onUserJoined` callback. If this parameter is not specified, the configurations apply in the order of the users joining the channel.
  - `x`: (Mandatory) The relative horizontal position of the top-left corner of the region. The value is between 0.0 (leftmost) and 1.0 (rightmost).
  - `y`: (Mandatory) The relative vertical position of the top-left corner of the region. The value is between 0.0 (top) and 1.0 (bottom).
  - `width`: (Mandatory) The relative width of the region. The value is between 0.0 and 1.0.
  - `height`: (Mandatory) The relative height of the region. The value is between 0.0 and 1.0.
  - `alpha`: The transparency of the image. The value is between 0.0 (transparent) and 1.0 (opaque). The default value is 1.0.
  - `renderMode`: The video display mode:
    - `RENDER_MODE_HIDDEN(0)`: (Default) Cropped mode.
    - `RENDER_MODE_FIT(1)`: Fit mode.

As shown in the figure below, the upper left corner of the video canvas is the origin. The `x` and `y` parameters define the relative position of a user's region on the canvas, representing the horizontal and vertical distance between the upper left corner of the region and the origin respectively. The `width` and `height` parameters define the relative width and relative height of the region. The `x`, `y`, `width`, and `height` parameters are floats between 0.0 and 1.0. Ensure that `x` + `width` ≤ 1, and `y` + `height` ≤ 1.

![](https://web-cdn.agora.io/docs-files/1600078304952)

### Sample code

This section provides sample code for a customized video layout of four users in composite recording mode.

In this example, the first user joining the channel occupies the full canvas, while the other three users occupy small regions layered on top of the canvas, as shown in the figure below.
![](https://web-cdn.agora.io/docs-files/1600078341737)

```cpp
// After creating an IRecordingEngine instance and joining the channel, set the width, height, and background color of the canvas as well as the number of user regions on the canvas.
agora::linuxsdk::VideoMixingLayout layout;
layout.canvasWidth = 720;
layout.canvasHeight = 480;
layout.backgroundColor = "#E7E6E6";
layout.regionCount = 4;

// Configure the settings of each user region.
agora::linuxsdk::VideoMixingLayout::Region * regionList = new agora::linuxsdk::VideoMixingLayout::Region[4];
// Set the first user in the channel to occupy the full canvas.
regionList[0].uid = <uid0>;
regionList[0].x = 0.f;
regionList[0].y = 0.f;
regionList[0].width = 1.f;
regionList[0].height = 1.f;
regionList[0].alpha = 1.f;
regionList[0].renderMode = 0;

// Set the other three users to occupy the small regions on top of the canvas, starting from the bottom left corner. The small regions are arranged in the order of the users joining the channel.
// The width of each small region is 23.5% of the width of the canvas.
// The height of each small region is the width of each small region × (canvas height/canvas width), that is, the aspect ratio of each small region is the same as the aspect ratio of the canvas.
// The horizontal spacing of adjacent small regions is 1.2% of the width of the canvas, and the vertical spacing is the horizontal spacing × (canvas height/canvas width).
// The horizontal distance between each small region and the canvas is also 1.2% of the width of the canvas, and the vertical distance between each small region and the canvas is the horizontal distance × (canvas height/canvas width).
float canvasWidth = 720;
float canvasHeight = 480;
float viewWidth = 0.235f;
float viewHEdge = 0.012f;
float viewHeight = viewWidth * (canvasHeight/canvasWidth);
float viewVEdge = viewHEdge * (canvasHeight/canvasWidth);

for (size_t i = 1; i < 4; i++) {
regionList[i].uid = <uidi>;
float xIndex = static_cast<float>((i-1) % 4);
float yIndex = static_cast<float>((i-1) / 4);
regionList[i].x = xIndex * (viewWidth + viewHEdge) + viewHEdge;
regionList[i].y = 1 - (yIndex + 1) * (viewHeight + viewVEdge);
regionList[i].width = viewWidth;
regionList[i].height = viewHeight;
regionList[i].alpha = static_cast<double>(i + 1);
regionList[i].renderMode = 0;
}
layout.regions = regionList;
// Call setVideoMixingLayout to implement the customized video layout.
m_engine->setVideoMixingLayout(layout);
```