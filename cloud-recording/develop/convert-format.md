---
title: "Convert the file format"
sidebar_position: 7
type: docs
platform_selector: false
description: >
  Use FFmpeg to convert an M3U8 file to MP4 or use Agora's Format Converter script to batch convert multiple TS files into MP4 or audio formats.
---

Composite recording mode generates one M3U8 file and multiple TS files which include the audio and video of all or specified user IDs in a channel. You can use FFmpeg to convert an M3U8 file to MP4 or use Agora's Format Converter script to batch convert multiple TS files into MP4 or audio formats.

## Convert using FFmpeg

<Admonition type = "info">
Since April 29, 2021, you can get MP4 files from a composite recording by setting the `avFileType` parameter. You no longer need to use the Format Converter script.
</Admonition>

You can use FFmpeg to convert an M3U8 file to MP4. Install [FFmpeg](https://ffmpeg.org/download.html) and run the following command:

```
ffmpeg -i input.m3u8 -vcodec copy -acodec copy -absf aac_adtstoasc output.mp4
```

Where `input.m3u8` is the name of the M3U8 file to convert, and `output.mp4` is the name of the MP4 file to output. For more information about the parameters used in this example, see the [FFmpeg Documentation](https://www.ffmpeg.org/ffmpeg.html).

## Convert using the script

You can use Agora's Format Converter script to batch convert TS files to MP4 or audio formats, including MP3, WAV, and AAC.

### Prerequisites

Recommended systems for transcoding:

- Ubuntu 14.04 and later x64
- CentOS 6.5 and later (7.0 recommended) x64

To run the script, you need to install [FFmpeg](https://ffmpeg.org/download.html) 3.3 or later and Python 2, version 2.7 or later.

#### File preparation

Ensure that the recorded files are stored in an accessible directory.

### Convert steps

#### 1. Get the Format Converter Script

Download the <Link target="_blank" to="{{Global.CREC_FCS}}">Agora Format Converter Script</Link> script and decompress it.

#### 2. Execute the Format Converter script

Use the following command:

```
python format_convert.py <directory> <source_format> <destination_format>
```

Where:

- `directory`: Directory of the source files.

- `source_format`: Format of the source files. `source_format` must be in lowercase:

  - Audio: `mp3`, `wav`, or `aac`.
  - Video: `mp4` or `ts`.
  
- `destination_format`: Format to which you want to convert the source files. `destination_format` must be in lowercase:

  - Audio: `mp3`, `wav`, or `aac`.
  - Video: `mp4` or `ts`.

When you run the command, the script will search for all files in the specified format in the directory and convert them to the target format. The converted files have the same name as the source files, except for the suffix.

### Example

To convert all the MP4 files under `/home/testname/testfolder` to TS format, use the following command:

```
python format_convert.py /home/testname/testfolder/ mp4 ts
```