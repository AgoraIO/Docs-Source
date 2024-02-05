---
title: "Pricing for Cloud Recording"
sidebar_position: 3
type: docs
platform_selector: false
description: >
   Depending on the number of minutes you intend to record, estimate your monthly Cloud Recording cost.
---

This page explains how <Vg k="COMPANY" /> calculates your monthly bill for Cloud Recording. 

If you have already signed a contract with <Vg k="COMPANY" />, the billing terms and conditions within that contract take precedence.

## Cloud Recording pricing

The unit pricing for audio and video usage is as follows:

| Service Type    | Category                       | Pricing, US$/1,000 minutes |
|:----------------|:-------------------------------|:---------------------------|
| Recording Audio | N/A                            | 1.49                       |
| Recording Video | High-Definition (HD)           | 5.99                       |
| Recording Video | Full High-Definition (Full HD) | 13.49                      |
| Recording Video | 2K                             | 23.99                      |
| Recording Video | 2K+                            | 53.99                      |
| Cloud-Based Screenshot Upload | All definitions  | 2.49 or free               |

**Note**: Cloud-Based Screenshot Upload is free if bundled with Cloud Recording, that is, initiated along with Cloud Recording in a single task.  

Agora determines video category based on **aggregate video resolution**, which is the sum of resolutions of all the video 
streams a user subscribes to at the same time. Agora adds up the resolution of all the video streams recorded at the same 
time to get the aggregate resolution, which categorizes video as follows:

| Video category                 | Aggregate video resolution                      |
| :----------------------------- | :----------------------------------------------------------- |
| High-Definition (HD)           | Up to 921,600 (1280 × 720）           |
| Full High-Definition (Full HD) | From greater than 921,600 (1280 × 720) to 2,073,600 (1920 × 1080) |
| 2K                             | From greater than 2,073,600 (1920 × 1080) to 3,686,400 (2560 × 1440)  |
| 2K+                            | From greater than 3,686,400 (2560 × 1440) to 8,847,360 (4096 × 2160)  |

For example, if the recording server records two 960 × 720 video streams at the same time, 
the aggregate resolution is 960 × 720 + 960 × 720 = 1,382,400. The recording service is charged based on the Full HD video pricing. 

The recording fee does not depend on the recording mode you choose. Regardless of whether you use the individual mode or 
composite mode, the recording fee relates only to the number of the streams recorded, the recording time, and the aggregate 
recording resolutions. The number of the streams recorded does not affect the recording duration, 
but affects the aggregate recording resolution.

## Cost calculation

Billing for Cloud Recording begins once you use Cloud Recording to record and save audio calls, group video calls, or interactive video streaming made via the Agora <Vg k="VSDK" /> on your cloud storage.

Agora calculates the billing of all projects under your <Link to="{{Global.AGORA_CONSOLE_URL}}">Agora Account</Link> monthly. 
After deducting the monthly [10,000 free-of-charge minutes](../reference/billing-policies#agoras-free-of-charge-policy-for-the-first-10000-minutes) 
that Agora grants to every account, Agora adds up the usage duration (in seconds) of audio and video in each category, 
and divides them by 60 to get the respective service minutes (rounded up to the nearest integer). 
Then, Agora multiplies the service minutes by the corresponding pricing to get the cost of that month.

The basic formula is shown here:

**Monthly cost = audio pricing × audio service minutes + video pricing × video service minutes**

If the recording server successfully records both audio and video at the same time, then Agora only charges for the video minutes. During a recording, the idle minutes are charged based on the audio pricing. The cost is the audio pricing × idle minutes.

### Service minutes

Service minutes (accurate to seconds) are calculated from the time when the recording starts to the time when the recording stops in a channel.

Service minutes comprise the following:

- **Video minutes**: The duration that the recording server records video in a channel.
- **Audio minutes**: The remaining duration after deducting the video minutes from the total duration when the recording server is in the channel, regardless of whether the recording server records any audio.

If you create a recording instance and record multiple audio and video streams at the same time in a channel, the total service minutes per streams are not additive. For example: <ul><li>If a recording instance records the video streams of both user A and user B for the same 10 minutes, the billing for the recording service is for 10 minutes of video.</li><li>If a recording instance records the audio stream of user A and the video stream of user B for the same 10 minutes, the billing for the recording device is also for 10 minutes of video.</li></ul>If you use multiple recording sessions at the same time in a channel, then the service minutes per recording session are additive.

## Examples

This section shows how to calculate the monthly audio and video service minutes of each category, as well as the total cost based on the corresponding unit price.

Suppose you have an enabled project named Test under your Agora account, and the project uses the Agora Cloud Recording to implement the recording function.

The recording usage duration of the project between February 1 and February 28, 2021 is as follows:

#### Recording one

On February 4, 2021: Four users join the channel at the same time and have a video call for 6,000 seconds. You start one cloud recording session to record only the audio streams of the four users in the channel.

During this recording, the recording service generates only charges for the audio minutes.

| Session                     | Audio | HD video | Full HD video | 2K video | 2K+ video |
| :-------------------------- | :---- | :------- | :------------ | :------- | :-------- |
| Usage duration (in seconds) | 6,000 | 0        | 0             | 0        | 0         |

#### Recording two

On February 9, 2021: Four users join the channel at the same time and have a video call for 6,000 seconds. You start an individual Recording and a composite Recording, two cloud recording sessions to record only the audio streams of the four users in the channel.

During this recording, the recording service generates only charges for the audio minutes.

| Session                   | Audio                  | HD video | Full HD video | 2K video | 2K+ video |
|:--------------------------| :--------------------- | :------- | :------------ | :------- | :-------- |
| Usage duration in seconds | 6,000 + 6,000 = 12,000 | 0        | 0             | 0        | 0         |

#### Recording three

On February 13, 2021: Four users join the channel at the same time and have a video call for 3,500 seconds. You start one cloud recording session to record the audio and video streams of the four users in the channel. The video resolution of each user is 640 × 360.

During this recording, the recording service generates charges for the video minutes. The aggregate video resolution is 4 × (640 × 360) = 921,600, falling into the category of HD.

| Session                   | Audio | HD video | Full HD video | 2K video | 2K+ video |
|:--------------------------| :---- | :------- | :------------ | :------- | :-------- |
| Usage duration in seconds | 0     | 3,500    | 0             | 0        | 0         |

#### Recording four

On February 15, 2021: Users A, B, and C join the channel at the same time and have interactive live video streaming. The video resolution of A, B, and C is 640 x 360, 1280 x 720, and 960 x 720. 1,680 seconds later, user D joins the channel, and has interactive live streaming with A, B, and C for 520 seconds. The video resolution of D is 1920 x 1080. During live streaming, you start one cloud recording session to record the audio and video streams of all the users in the channel.

During this recording, the recording service generates charges for the video minutes.

In the initial 1,680 seconds, the aggregate resolution is 640 x 360 + 1280 x 720 + 960 x 720 = 1,843,200, falling into the category of Full HD video.

In the subsequent 520 seconds, the aggregate resolution is 640 x 360 + 1280 x 720 + 960 x 720 + 1920 x 1080 = 3,916,800, falling into the category of 2K+ video.

| Session                     | Audio | HD video | Full HD video | 2K video | 2K+ video |
| :-------------------------- | :---- | :------- | :------------ | :------- | :-------- |
| Usage duration (in seconds) | 0     | 0        | 1,680         | 0        | 520       |

### Calculate cost

<table>
                <colgroup span="1">
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                    <col/>
                </colgroup>
                <tbody>
                    <tr>
                        <th rowspan="2">Date</th>
                        <th colspan="5">Actual usage duration in seconds</th>
                        <th colspan="5">Usage duration displayed on Agora Console in minutes</th>
                    </tr>
                    <tr>
                        <td>
                            <p>Audio</p>
                        </td>
                        <td>
                            <p>HD video</p>
                        </td>
                        <td>
                            <p>Full HD video</p>
                        </td>
                        <td>
                            <p>2K video</p>
                        </td>
                        <td>
                            <p>2K+ video</p>
                        </td>
                        <td>
                            <p>Audio</p>
                        </td>
                        <td>
                            <p>HD video</p>
                        </td>
                        <td>
                            <p>Full HD video</p>
                        </td>
                        <td>
                            <p>2K video</p>
                        </td>
                        <td>
                            <p>2K+ video</p>
                        </td>
                    </tr>
                    <tr>
                        <td>2020-02-04</td>
                        <td>6,000</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>100</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>2020-02-09</td>
                        <td>12,000</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>200</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>2020-02-13</td>
                        <td>0</td>
                        <td>3,500</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>59</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>2020-02-15</td>
                        <td>0</td>
                        <td>0</td>
                        <td>1,680</td>
                        <td>0</td>
                        <td>520</td>
                        <td>0</td>
                        <td>0</td>
                        <td>28</td>
                        <td>0</td>
                        <td>9</td>
                    </tr>
                    <tr>
                        <td>Monthly usage</td>
                        <td>18,000</td>
                        <td>3,500</td>
                        <td>1,680</td>
                        <td>0</td>
                        <td>520</td>
                        <td>300</td>
                        <td>59</td>
                        <td>28</td>
                        <td>0</td>
                        <td>9</td>
                    </tr>
                    <tr>
                        <td><strong>Billable service minutes</strong></td>
                        <td>300<br /> minutes</td>
                        <td>59<br /> minutes</td>
                        <td>28<br /> minutes</td>
                        <td>0</td>
                        <td>9<br /> minutes</td>
                        <td  colspan="5"  ><strong>The usage displayed on Agora Console is for
                                reference only and not used as the actual billing
                            basis.</strong></td>
                    </tr>
                    <tr>
                        <td>
                            <p>Cost of each service,</p>
                            <p>US$</p>
                        </td>
                        <td>(300/1000 )<br /> × 1.49<br /> = 0.447</td>
                        <td>(59/1000)<br /> × 5.99<br /> = 0.35341</td>
                        <td>(28/1000) <br />× 13.49<br /> = 0.37772</td>
                        <td>0</td>
                        <td>(9/1000)<br /> × 53.99<br /> = 0.48591</td>
                        <td  colspan="5"  ></td>
                    </tr>
                    <tr>
                        <td>
                            <p>Total cost,</p>
                            <p>US$</p>
                        </td>
                        <td>
                            <p ><strong><strong>1.66</strong></strong></p>
                            <p ><strong><strong>(0.447 + 0.35341 + 0.37772 + 0.48591 =
                                        1.66404 ≈ 1.66）</strong></strong></p>
                        </td>
                        <td  colspan="9"></td>
                    </tr>
                </tbody>
            </table>


<ul><li>Agora rounds up the monthly total fees to two decimal places.</li><li>Agora gives each Agora account 10,000 minutes of free time per month. Because the monthly total service minutes in the above example do not exceed 10,000 minutes, the service is free of charge and the bill would show $US 0.</li></ul>


## Reference

### Accuracy of service minutes

At the end of each month, Agora adds up the usage duration (in seconds) of audio and video in each category, and divides them by 60 to get the respective service minutes (rounded up to the next integer). For example, if the duration of audio service of the month is 59 seconds, then the audio service minutes is calculated as 1 minute; if the duration of video service is 61 seconds, then the video service minutes is calculated as 2 minutes. The error of service minutes for each month is within 1 minute. 

### Aggregate video resolution in dual-stream scenarios

When the user being recorded enables [dual-stream mode](../reference/glossary#dual-stream-mode), the recording service can receive only one stream at a time:

- If the recording server records the high-quality video stream, the aggregate video resolution is calculated based on the resolution of the high-quality video.
- If the recording server records the low-quality video stream, the aggregate video resolution is calculated based on the resolution of the video received by the server.

### Resolution calibration

When calculating the aggregate resolution, Agora counts the resolution of 225,280 (640 × 352) as 640 × 360.

## See also

- [Agora's free-of-charge policy for the first 10,000 minutes](../reference/billing-policies#agoras-free-of-charge-policy-for-the-first-10000-minutes)
- [Billing, free deduction, and account suspension](../reference/billing-policies#billing-fee-deductions-and-account-suspension-policies)
- [Web Page Recording pricing](pricing-webpage-recording)