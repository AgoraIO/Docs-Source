---
title: "Understand Extensions"
sidebar_position: 1
type: docs
description: >
  A brief introduction to extensions.
---
export const toc = [{}];

## What are extensions

In the Agora Extensions Marketplace:
- Vendors create and publish extensions to provide functionality such as audio and video processing.
- App developers use extensions to quickly implement fun and interactive functionality.

Extensions allow vendor developers to access, modify, and transfer voice and video data from the transmission pipeline in the Agora SDK.

![](https://web-cdn.agora.io/docs-files/1638781024344)

A typical transmission pipeline consists of a chain of procedures, including capture, pre-processing, encoding, transmitting, decoding, post-processing, and play. Audio or video filter extensions are inserted into either the pre-processing or post-processing procedure, in order to modify the voice or video data in the transmission pipeline.


## Extension types

There are currently two types of extension:

- Audio filter extension: Modifies the audio data to provide features such as voice effects and noise cancellation. In the media transmission pipeline of Agora SDK, audio filters work as follows:
 ![](https://web-cdn.agora.io/docs-files/1638345519987)
- Video filter extension: Modifies the video data to provide features such as face filters and background removal. In the media transmission pipeline of Agora SDK, video filters work as follows:
 ![](https://web-cdn.agora.io/docs-files/1638346128292)
 
## Extension formats
Agora currently supports the following formats of extension:

- Android: `.aar` or `.so`
- iOS/macOS: `.xcframework` or `.framework`
- Windows: `.dll`