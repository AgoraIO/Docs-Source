---
title: 'Repair Recorded Files'
sidebar_position: 11
type: docs
description: >
  How to repair recorded files after the recording crashes.
---

## Overview

Before v3.0.3, the MP4 files generated after a recording might not be playable due to recording crashes. To solve this issue, as of v3.0.3, the Agora Recording SDK provides the following solutions:

- The SDK now generates video files in TS format during the recording. When the recording ends, the SDK automatically converts these TS files into MP4 format. Even if occasional crashes occur during the recording, the MP4 files can still be played.
- The SDK adds the `crash_restore.sh` script. If the recording service quits after multiple crashes, you can run the script to convert these TS files into MP4 files and repair the incomplete `uid_UID_timestamp.txt` files.

## Applicable use-cases

The Agora Recording SDK generates recording files in TS format during the recording process in the following use-cases:

| Recording mode                                    | Recording Type   | Parameter Settings                          | Recording files and formats during the recording             | Recording files and formats after the recording              |
|:--------------------------------------------------| :--------------- | :------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Individual recording](./develop/individual-mode) | Audio and video  | Default settings                            | <li>One audio file in AAC format and one video file in TS format for each UID that uses the Agora Native SDK</li><li>One audio file in AAC format and one video file in TS or WebM format for each UID that uses the Agora Web SDK</li> | <li>One audio file in AAC format and one video file in MP4 format for each UID that uses the Agora Native SDK</li><li>One audio file in AAC format and one video file in MP4 or WebM format for each UID that uses the Agora Web SDK</li> |
| [Composite recording](./develop/composite-mode)   | Video (no audio) | <li>`-- isVideoOnly 1`</li><li>`-- isMixingEnabled 1`</li>    | One video file in TS format                                  | One video file in MP4 format                                 |
| [Composite recording](./develop/composite-mode)           | Audio and video  | <li>`-- isMixingEnabled 1`</li><li>`-- mixedVideoAudio 2`</li> | One file in TS format containing both audio and video        | One file in MP4 format containing both audio and video       |

<Admonition type="info"><li>This table shows the files generated when there are no crashes during recording. If crashes occur during recording, multiple TS files are generated (based on the number of crashes; each crash creates a new one), and therefore multiple MP4 files will also be generated once the recording is complete.</li><li>The files in AAC or WebM format can still be played even if the recording crashes.</li></Admonition>

## Implementation

In different recording modes, you need to convert and repair the recording files based on the number of crashes in a single recording process, as shown in the following table:

| Number of crashes | Individual recording                                         |Composite recording                                     |
| :---------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Fewer than 4      |<li> The recording service resumes after each crash, resulting in multiple TS files and multiple incomplete `uid_UID_timestamp.txt `files.</li><li>When the recording ends, the SDK automatically converts these TS files into MP4 files one by one.</li><li>However, the SDK does not automatically repair the incomplete `uid_UID_timestamp.txt` files. If you want to use the transcoding script to merge the separated audio file and video file into one MP4 file, you must first run the `crash_restore.sh `script to repair the `uid_UID_timestamp.txt` files.</li> | <li>The recording service resumes after each crash, resulting in multiple TS files.</li><li>When the recording ends, the SDK automatically converts these TS files into MP4 files one by one.</li> |
| 4                 | <li>The recording service quits abnormally, leaving the TS files unconverted and the `uid_UID_timestamp.txt` files incomplete.</li><li>You need to run the `crash_restore.sh` script to convert these TS files into MP4 files and restores the `uid_UID_timestamp.txt` files.</li> | <li>The recording service quits abnormally, leaving the TS files unconverted.</li><li>You need to run the `crash_restore.sh` script to convert these TS files into MP4 files.</li> |

## Run the `crash_restore.sh` script 

### Prerequisites

-   Linux operating system

-   Python 3.0 or later

-   FFmpeg 4.0 or later (The Agora Recording SDK provides FFmpeg in the **tools** folder.）

**File preparation**

Ensure that the recording files are stored in an accessible directory.

### Run the script

Run the following command:

```
$ ./crash_restore.sh <recorderDir>/
```

Where `recorderDir` is the directory of your recording files.

When you run the command, the script searches for all files in TS format in the directory and converts them to MP4 format one by one. In individual recording mode, the script also searches for and repairs the `uid_UID_timestamp.txt` files.

The name of the converted MP4 files are the same as the source TS files. The source TS files are not deleted after this conversion process, in case they are needed later.

## Example

To convert all the TS files under the `20200915` folder to MP4 format and repair the `uid_UID_timestamp.txt` files, use the following command:

```
$ ./crash_restore.sh 20200915/
```

Before the conversion and repair:
![](https://web-cdn.agora.io/docs-files/1600314197717)

After the conversion and repair:
![](https://web-cdn.agora.io/docs-files/1600314313477)

## Considerations

- As of v3.0.3, after a recording ends, you need to wait for the conversion to complete before you can get the MP4 files. The time required for this conversion depends on the IOPS of the server and the total size of the TS files to be converted. For example, it takes approximately 85 to 150 seconds to convert a 4GB TS file (this data is for reference only).
- The conversion process consumes disk I/O resources. If the server disk performance is poor, Agora recommends you do not perform other operations until the conversion is completed.