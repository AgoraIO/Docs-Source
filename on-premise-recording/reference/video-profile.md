---
title: 'Set the Video Profile'
sidebar_position: 4
type: docs
description: >
  How to set the video profile in composite recording mode.
---

In composite recording mode, you can set the video profile (resolution, frame rate, and bitrate) for the output video stream. Agora recommends setting the video profile according to the values listed in the [video profile table](#video-profile-table). For Cloud Recording, use `transcodingConfig` to set the video profile. For On-Premise Recording, use `mixResolution` to set the video profile.

<div class="alert note">In individual recording mode, the recorded video keeps the original video profile.</div>

## Basic guidelines

- Agora recommends setting the recording resolution lower than the [aggregate resolution](../overview/billing#aggregate-video-resolution) of the original video streams, otherwise the recorded video may be blurry.
- The resolution you set in the video profile is that of the video canvas, and its aspect ratio does not need to be identical to any source video stream. The aspect ratio of each user region in the output video depends on the aspect ratio of the canvas and the video layout. See [Related articles](#relateddocs).
- Agora only supports the following frame rates: 1 fps, 7 fps, 10 fps, 15 fps, 24 fps, 30 fps, and 60 fps. The default value is 15 fps. If you set other frame rates, the SDK uses the default value.
- The base bitrate in the video profile table applies to the communication profile. The live-broadcast profile generally requires a higher bitrate to ensure better video quality. Set the bitrate of the live-broadcast profile as twice the base bitrate.
- Increasing the bitrate improves the output video quality, but requires higher bandwidth. The maximum bitrate is 6500 Kbps. Exceeding the limit causes an error.

## Calculate a bitrate manually

If you cannot find a matching video profile in the table, follow these steps to manually calculate a proper bitrate:

1. In the video profile table, find the resolution closest to your target resolution.
2. Calculate a bitrate based on your target frame rate. When the resolution is fixed, the bitrate increases as the frame rate increases. Suppose the base bitrate is *x* when the frame rate is 15 fps:
   - If the frame rate is 5 fps, the base bitrate is 0.5*x*.
   - If the frame rate is 30 fps, the base bitrate is 1.5*x.*
   - If you use a different frame rate, set the bitrate depending on the interval that the frame rate falls into. For example, if the frame rate is 10 fps, set the bitrate between 0.5*x* and 1*x*.

Suppose your target resolution is 300 * 240 with a frame rate of 30 fps. The closest resolution in the video profile table is 320 * 240, with a base bitrate of 200 Kbps and a frame rate of 15 fps. The inferred bitrate should be 200 Kbps * 1.5, which is 300 Kbps.



## <a name="profile_table"></a>Video profile table

| Resolution (width * height) | Frame rate (fps) | Base bitrate (Kbps, communication profile) | Live bitrate (Kbps, live-broadcast profile) |
| :-------------------------- | :--------------- | :----------------------------------------- | :------------------------------------------ |
| 160 * 120                   | 15               | 65                                         | 130                                         |
| 120 * 120                   | 15               | 50                                         | 100                                         |
| 320 * 180                   | 15               | 140                                        | 280                                         |
| 180 * 180                   | 15               | 100                                        | 200                                         |
| 240 * 180                   | 15               | 120                                        | 240                                         |
| 320 * 240                   | 15               | 200                                        | 400                                         |
| 240 * 240                   | 15               | 140                                        | 280                                         |
| 424 * 240                   | 15               | 220                                        | 440                                         |
| 640 * 360                   | 15               | 400                                        | 800                                         |
| 360 * 360                   | 15               | 260                                        | 520                                         |
| 640 * 360                   | 30               | 600                                        | 1200                                        |
| 360 * 360                   | 30               | 400                                        | 800                                         |
| 480 * 360                   | 15               | 320                                        | 640                                         |
| 480 * 360                   | 30               | 490                                        | 980                                         |
| 640 * 480                   | 15               | 500                                        | 1000                                        |
| 480 * 480                   | 15               | 400                                        | 800                                         |
| 640 * 480                   | 30               | 750                                        | 1500                                        |
| 480 * 480                   | 30               | 600                                        | 1200                                        |
| 848 * 480                   | 15               | 610                                        | 1220                                        |
| 848 * 480                   | 30               | 930                                        | 1860                                        |
| 640 * 480                   | 10               | 400                                        | 800                                         |
| 1280 * 720                  | 15               | 1130                                       | 2260                                        |
| 1280 * 720                  | 30               | 1710                                       | 3420                                        |
| 960 * 720                   | 15               | 910                                        | 1820                                        |
| 960 * 720                   | 30               | 1380                                       | 2760                                        |
| 1920 * 1080                 | 15               | 2080                                       | 4160                                        |
| 1920 * 1080                 | 30               | 3150                                       | 6300                                        |

## <a name="relateddocs"></a>Related articles

- Cloud Recording: [Set Video Layout](../../cloud-recording/develop/layout).
- On-Premise Recording: [Set Video Layout](../develop/layout).