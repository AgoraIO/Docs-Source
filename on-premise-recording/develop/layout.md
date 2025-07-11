---
title: 'Set Video Layout'
sidebar_position: 4
type: docs
description: >
  Learn how to set the video layout for composite recording with the Agora Recording SDK.
---

This guide shows you how to configure the video layout during composite recording using the <Vg k="OPREC_SDK" />.

## Understand the tech

In composite recording mode, the final video is rendered on a canvas that includes multiple user video streams arranged in specified regions. The canvas acts as the video background, and each user occupies a region on that canvas.

![](https://web-cdn.agora.io/docs-files/1577697787996)

<Admonition type="info" info="info">
The aspect ratio of the user video must match the aspect ratio of its designated region on the canvas. If not, the SDK automatically crops the video, which may cause image loss.
</Admonition>

## Prerequisites

Before continuing, follow the [Quickstart](/on-premise-recording/get-started/) guide to integrate the Recording SDK and implement basic recording functionality.

## Implementation

To define the layout, use the `setVideoMixingLayout` method. This method takes a [VideoMixingLayout](#videomixinglayout-class) object that configures the canvas dimensions, frame rate, background color or image, and the layout of each user's video stream.

```java
VideoMixingLayout recorderLayout = new VideoMixingLayout();
recorderLayout.setCanvasWidth(1280);
recorderLayout.setCanvasHeight(720);
recorderLayout.setCanvasFps(25);

// Set layout for two users
UserMixerLayout[] layout = new UserMixerLayout[2];

// User 1 layout
layout[0] = new UserMixerLayout();
layout[0].setUserId("1234");
MixerLayoutConfig mixerLayoutConfig1 = new MixerLayoutConfig();
mixerLayoutConfig1.setX(0);
mixerLayoutConfig1.setY(0);
mixerLayoutConfig1.setWidth(640);
mixerLayoutConfig1.setHeight(360);
layout[0].setConfig(mixerLayoutConfig1);

// User 2 layout
layout[1] = new UserMixerLayout();
layout[1].setUserId("5678");
MixerLayoutConfig mixerLayoutConfig2 = new MixerLayoutConfig();
mixerLayoutConfig2.setX(720);
mixerLayoutConfig2.setY(270);
mixerLayoutConfig2.setWidth(540);
mixerLayoutConfig2.setHeight(320);
layout[1].setConfig(mixerLayoutConfig2);

// Apply the layout
recorderLayout.setUserLayoutConfigs(layout);
agoraMediaRtcRecorder.setVideoMixingLayout(recorderLayout);
```

## Reference

This section explains how to implement different sound effects and audio mixing in your app, covering essential steps and code snippets.

#### `VideoMixingLayout` class

```java
public class VideoMixingLayout {
    private int canvasWidth;               // Width of the canvas
    private int canvasHeight;              // Height of the canvas
    private int canvasFps;                 // Frame rate
    private long backgroundColor;          // Background color (ARGB format)
    private String backgroundImage;        // Path to the background image (optional)
    private int userLayoutConfigNum;       // Number of user video layouts
    private UserMixerLayout[] userLayoutConfigs; // Layouts for each user stream
}
```

#### `UserMixerLayout` and `MixerLayoutConfig` classes

Each user stream is configured through `UserMixerLayout`, which contains a `MixerLayoutConfig` object defining size, position, and appearance.

```java
public class UserMixerLayout {
    private String userId;                 // UID of the user to include in the mix
    private MixerLayoutConfig config;      // Layout configuration for the user stream
}
```

```java
public class MixerLayoutConfig {
    private int x;                         // X offset from the canvas origin
    private int y;                         // Y offset from the canvas origin
    private int width;                     // Width of the user video region
    private int height;                    // Height of the user video region
    private int zOrder;                    // Layer order for overlapping videos
    private float alpha;                   // Transparency (0.0 to 1.0)
    private boolean mirror;                // Whether to mirror the video
    private String imagePath;              // Optional background image
    private int rotation;                  // Clockwise rotation (0, 90, 180, 270)
}
```