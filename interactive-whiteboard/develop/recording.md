---
title: 'Recording and playback'
sidebar_position: 5.7
type: docs
description: >
   Record all interactions in a live room and implement high-quality playback.
---

Agora’s Fastboard SDK provides recording and playback features for all interactions in a live room. It offers higher efficiency and smoother playback than traditional screen recording.

Fastboard recording and playback provide the following advantages:

- **High-efficiency recording**: Uses signaling-based recording that reduces bandwidth usage and storage requirements.

- **High-quality playback**: Recreates live room interactions with clear visuals and smooth animations.

- **Server-side recording**: Performs all recording on the server. No additional processing is required on the client.

- **Flexible playback**: Supports time-range playback, playback controls, and camera tracking.

- **Complete recording**: Captures all interactive behavior such as whiteboard operations, custom events, viewpoint changes, and multi-window applications.

- **Built-in UI**: Includes ready-to-use playback components with theme and language customization.

This page describes how to enable whiteboard recording and how to use the Fastboard SDK to play back whiteboard content.

## Understand the tech

This section describes how Interactive Whiteboard recording and playback work and highlights the benefits of this model.

#### Recording

Interactive Whiteboard recording does not capture the screen. Instead, it records proprietary binary data that includes signaling and incremental updates. The server performs the entire recording process, which provides the following advantages:

- **Automatic recording**: To start recording, enable the recording function when you create a room. The server automatically records all interactions in the room.
- **Intelligent management**: The server generates recording data only when the room is active. Recording stops automatically when the room becomes inactive.
- **Compact data**: The recorded data is smaller and uses less storage compared to traditional audio and video formats.
- **Multi-window support**: The recorder captures all applications and operations in Fastboard's multi-window mode.

#### Playback

The Fastboard SDK uses the playback capabilities of the underlying Whiteboard SDK and provides a simplified API with built-in UI components. During playback, the SDK incrementally reconstructs the scene using recorded signaling and data, reproducing the experience of real-time interaction. Playback supports:

- Playback within a specified time range
- Playback controls such as play, pause, and skip
- Playback speed adjustment
- Camera follow mode and free camera mode
- Replay of custom events and global state changes
- Full replay of multi-window applications

## Prerequisites

To enable recording and playback with the Fastboard SDK, you need the following:

- The Agora Fastboard SDK integrated into your project. See [Fastboard quickstart](../get-started/get-started-uikit) for details.
- An Agora project with the <Vg k="WHITE" /> enabled. Get the app identifier and room token from <Vg k="CONSOLE" />. See [Enable and configure <Vg k="WHITE" />](../get-started/enable-whiteboard) and [Generate a room token](../get-started/get-started-uikit#generate-a-room-token).
- A room created on your business server. See the [Room management](../reference/whiteboard-api/room-management) server API for details. 

## Implement recording

### Enable recording

To enable whiteboard recording, set the required parameters when creating the room. Create a room with recording enabled by setting `isRecord: true` in the server-side API POST request:

```javascript
var url = "https://api.netless.link/v5/rooms";
var requestInit = {
    method: "POST",
    headers: {
        "content-type": "application/json",
        "token": "NETLESSSDK_YWs9xxxxxxM2MjRi", // Replace with your SDK Token
        "region": "us-sv", // Replace with your data center
    },
    body: JSON.stringify({
        name: "My Fastboard Recording Room",
        isRecord: true, // Enable recording
    }),
};

fetch(url, requestInit).then(function(response) {
    return response.json();
}).then(function(roomJSON) {
    // Room created successfully, get room information
    console.log("Room UUID:", roomJSON.uuid);
    console.log("Room recording enabled");
}).catch(function(err) {
    console.error("Failed to create room:", err);
});
```

After you enable recording, all interactions in the room are automatically recorded.

<Admonition type="caution">
SDK tokens are important security credentials and should be used on the business server, not hardcoded in the front-end code.
</Admonition>

### Recorded content

When the recording function is enabled, the following content is recorded automatically:

- Whiteboard drawing operations (pen, graphics, text, etc.)
- Scene switching and content changes
- Display and operation of images, audio and video, and courseware (PPT, DOC)
- All operations and state changes in a multi-window application
- Changes in User perspective
- Custom events (sent through `dispatchMagixEvent`)
- Global state changes (`GlobalStatemodifications`)

## Implement playback

Use one of the following methods to implement recording playback.

### Using the replay UI component (Recommended)

```javascript
import { replayFastboard, createReplayUI } from "@netless/fastboard";

// Create the playback player
const player = await replayFastboard({
    sdkConfig: {
        appIdentifier: "RMxxxAQ", // Replace with your App Identifier
        region: "us-sv", // Replace with your data center
    },
    replayRoom: {
        room: "a7xxx69", // Room UUID
        roomToken: "NETLESSROOM_YWxxxjk", // Room Token
        beginTimestamp: new Date("2023-01-01 08:00:00").getTime(), // Playback start time
        duration: 45 * 60 * 1000, // Playback duration in milliseconds
    },
    managerConfig: {
        cursor: true, // Show cursor
    },
});

// Create and mount the playback UI
const ui = createReplayUI(player, document.getElementById("whiteboard"));

// Optional: Update UI configuration
ui.update({ 
    theme: "dark", 
    language: "en-US" 
});

// Destroy when finished
// ui.destroy();
```

### Using React hooks

If you are using the React framework, you can use the `useReplayFastboard` hook:

```javascript
import React from "react";
import { useReplayFastboard, ReplayFastboard } from "@netless/fastboard-react";

function ReplayComponent() {
    const player = useReplayFastboard(() => ({
        sdkConfig: {
            appIdentifier: "RMxxxAQ", // Replace with your App Identifier
            region: "us-sv",
        },
        replayRoom: {
            room: "a7xxx69", // Room UUID
            roomToken: "NETLESSROOM_YWxxxjk", // Room Token
            beginTimestamp: new Date("2023-01-01 08:00:00").getTime(),
            duration: 45 * 60 * 1000,
        },
        managerConfig: {
            cursor: true,
        },
    }));
    
    return (
        <ReplayFastboard 
            player={player} 
            theme="light" 
            language="en-US" 
        />
    );
}
```

### Plugin configuration

If you enabled `AppliancePlugin` or `AppInMainViewPlugin` when creating the live room, configure the same plugin for playback:

```javascript
const player = await replayFastboard({
    sdkConfig: {
        appIdentifier: "RMxxxAQ",
        region: "us-sv",
    },
    replayRoom: {
        room: "a7xxx69",
        roomToken: "NETLESSROOM_YWxxxjk",
        beginTimestamp: new Date("2023-01-01 08:00:00").getTime(),
        duration: 45 * 60 * 1000,
    },
    // If AppliancePlugin was enabled in the live room, configure it for playback
    enableAppliancePlugin: {
        cdn: {
            fullWorkerUrl: "path/to/fullWorker.js",
            subWorkerUrl: "path/to/subWorker.js",
        },
        strokeWidth: {
            min: 1,
            max: 32
        },
        syncOpt: {
            interval: 200
        },
    },
    // If AppInMainViewPlugin was enabled in the live room, configure it for playback
    enableAppInMainViewPlugin: true,
});
```

### Player controls

`FastboardPlayer` provides the following playback control functions:

```javascript
// Playback controls
player.play();     // Start playback
player.pause();    // Pause playback
player.stop();     // Stop playback

// Seek to a specific position (in milliseconds, relative to playback start time)
player.seek(10 * 60 * 1000); // Seek to the 10-minute mark

// Set playback speed
player.setPlaybackRate(1.5); // Play at 1.5x speed
player.setPlaybackRate(1.0); // Resume normal speed

// Get playback status information
console.log("Current playback progress:", player.currentTime.value); // Current playback position in milliseconds
console.log("Total duration:", player.duration.value);                // Total playback duration in milliseconds
console.log("Playback state:", player.phase.value);                   // Playback state
console.log("Playback speed:", player.playbackRate.value);            // Current playback speed
console.log("Can play:", player.canplay.value);                       // Whether ready to play
```

### Monitor player status changes

You can listen for changes in the player's state by subscribing to observable properties:

```javascript
// Listen for playback progress changes
const unsubscribeProgress = player.currentTime.subscribe(time => {
    console.log("Current playback progress:", time + "ms");
});

// Listen for playback state changes
const unsubscribePhase = player.phase.subscribe(phase => {
    switch(phase) {
        case "playing":
            console.log("Playing");
            break;
        case "pause":
            console.log("Paused");
            break;
        case "buffering":
            console.log("Buffering");
            break;
        case "ended":
            console.log("Playback ended");
            break;
        case "waitingFirstFrame":
            console.log("Waiting for first frame");
            break;
    }
});

// Listen for playback speed changes
const unsubscribeRate = player.playbackRate.subscribe(rate => {
    console.log("Playback speed:", rate + "x");
});

// Unsubscribe
// unsubscribeProgress();
// unsubscribePhase();
// unsubscribeRate();
```

### Custom rendering

To customize the rendering, use the `bindContainer` method:

```javascript
// Render only the whiteboard content, without control UI
player.bindContainer(document.getElementById("whiteboard"));

// Optional: Move collector to a specific location
player.bindCollector(document.getElementById("collector"));
```

### Synchronize whiteboard with RTC playback

In real-world applications, you may need to replay whiteboard content simultaneously with audio and video recorded by RTC. Use the `@netless/combine-player` library to manage both the video player and the whiteboard playback player to ensure consistent playback status and synchronized playback.

<Admonition type="info">
The following access methods are supported only if `@netless/combine-player` version 1.1.7 or above is used.
</Admonition>

The following code demonstrates how to achieve synchronized playback of RTC audio and video with a whiteboard using `@netless/combine-player`:

```javascript
import { replayFastboard } from "@netless/fastboard";
import CombinePlayerFactory from "@netless/combine-player";

// Create the whiteboard playback player
const player = await replayFastboard({
    sdkConfig: {
        appIdentifier: "RMxxxAQ", // Replace with your App Identifier
        region: "us-sv",
    },
    replayRoom: {
        room: "a7xxx69", // Room UUID
        roomToken: "NETLESSROOM_YWxxxjk", // Room Token
        beginTimestamp: new Date("2023-01-01 08:00:00").getTime(),
        duration: 45 * 60 * 1000,
    },
    managerConfig: {
        cursor: true,
    },
    // If plugins were enabled in the live room, configure them for playback
    enableAppliancePlugin: {},
});

// Bind the whiteboard container
const whiteboard = document.getElementById("whiteboard");
player.bindContainer(whiteboard);

// Configure video player parameters
const factoryParams = {
    url: "https://example.com/rtc-recording.mp4", // URL of the RTC recorded video
    videoDOM: document.getElementById("videoDom"), // DOM element for the video player
};

// Create the synchronized player
const combinePlayer = new CombinePlayerFactory(player.player, factoryParams).create(false);

// Control playback using the synchronized player
combinePlayer.play();   // Start playback
combinePlayer.pause();  // Pause playback
combinePlayer.seek(10 * 1000); // Seek to 10-second position (in milliseconds)

// Listen for playback status changes
combinePlayer.setOnStatusChange((status, message) => {
    console.log("Playback status:", status, message);
});

// Get playback information
console.log("Playback rate:", combinePlayer.playbackRate);
console.log("Total duration:", combinePlayer.timeDuration);
console.log("Current status:", combinePlayer.combinedStatus);
```

## Reference

This section contains content that completes the information on this page, or points you to documentation that explains other aspects to this product.

### Development considerations

When using Fastboard's recording and playback features, note the following:

- **Recording delay**: Recording content is not generated in real time. Newly created rooms may need to wait for a period of time before the recording content becomes available.
- **Plugin consistency**: If plugins are enabled in the live room, configure the same plugins for playback. Otherwise, playback errors may occur.
- **Time range**: Set an appropriate playback time range based on your usage scenario to avoid playing unnecessary content.
- **Network buffering**: Playback may require network buffering, especially when seeking to a distant point in time.
- **Storage costs**: Prolonged use of the recording function incurs storage costs. Use it judiciously based on your business needs.
- **Resource release**: Remember to call `ui.destroy()` and `player.destroy()` to release resources after use.

### API reference

- [`replayFastboard`](../reference/uikit-sdk#replayfastboard) - Create a playback player
- [`createReplayUI`](../reference/uikit-sdk#createreplayui) - Create a replay UI
- [Create Room API](../reference/whiteboard-api/room-management)