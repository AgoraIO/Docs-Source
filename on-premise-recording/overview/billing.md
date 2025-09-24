---
title: 'Pricing'
sidebar_position: 2
type: docs
description: >
  Pricing information for On-Premise Recording.
---

This article introduces the billing policy for the on-premise recording service provided by Agora.

Starting in April 2021, Agora further divided HD+ video into Full HD, 2K, and 2K+ video and set a more fine-grained pricing.

<Admonition type="info"><ul><li>Your billing details may differ if you have signed a contract with Agora.</li><li>If the previous pricing set for HD and HD+ video still applies to you, see <a href="#question">What is the previous pricing for audio and video?</a> for detailed video categorization and unit price.</li></ul></Admonition>

## Overview

Agora calculates the billing of all projects under your <Link to="{{Global.AGORA_CONSOLE_URL}}">Agora Account</Link> monthly.

Billing for the on-premise recording service begins once you use the Agora On-Premise Recording SDK to record and save audio calls, group video calls, or interactive live video streaming made via the Agora <Vg k="VSDK" /> on your server. 

On the first day of each month, Agora sends you the bill via email, and five days later deducts the payment from your account. For details, see [Billing, fee deduction, and account suspension](../../video-calling/reference/billing-policies).

<Admonition type="info">Agora gives each Agora account 10,000 free-of-charge minutes each month. For more information on the deduction sequence and applicable products, see<a href="https://docs.agora.io/en/faq/billing_free"> Agora's free-of-charge policy for the first 10,000 minutes</a>.</Admonition>

## Composition

Agora calculates the recording service minutes of audio and video used by your projects on a monthly basis.

At the end of each month, Agora adds up the usage duration (in seconds) of audio and video in each category, and divides them by 60 to get the respective service minutes (rounded up to the nearest integer). Then, Agora multiplies the service minutes by the corresponding pricing to get the cost of that month.

**Cost = audio charges + video charges = audio pricing × audio service minutes + video pricing × video service minutes**

<Admonition type="info"><ul><li>If the recording server successfully records both audio and video at the same time, then Agora only charges for the video minutes.</li><li>During a recording, the idle minutes are charged based on the audio pricing. The cost is the audio pricing × idle minutes.</li></ul></Admonition>

### Service minutes

Service minutes (accurate to seconds) are calculated from the time when the recording starts to the time when the recording stops in a channel.

Service minutes comprise the following:

- **Video minutes**: The duration that the recording server records video in a channel.
- **Audio minutes**: The remaining duration after deducting the video minutes from the total duration when the recording server is in the channel, regardless of whether the recording server records any audio.

<Admonition type="info">If you create a recording instance and record multiple audio and video streams at the same time in a channel, the total service minutes per streams are not additive. For example: <ul><li>If a recording instance records the video streams of both user A and user B for the same 10 minutes, the billing for the recording service is for 10 minutes of video.</li><li>If a recording instance records the audio stream of user A and the video stream of user B for the same 10 minutes, the billing for the recording device is also for 10 minutes of video.</li></ul>If you use multiple recording instances at the same time in a channel, then the service minutes per recording instance are additive.</Admonition>

### Unit Price

The unit pricing for audio and video is as follows:

<table>
                <colgroup>
                    <col />
                    <col />
                    <col />
                </colgroup>
                <thead>
                    <tr>
                        <th>Service type</th>
                        <th>Category</th>
                        <th>Pricing ($US/1,000 minutes)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Recording audio</td>
                        <td>N/A</td>
                        <td>0.99</td>
                    </tr>
                    <tr>
                        <td rowspan="4">Recording video</td>
                        <td>High-Definition (HD)<sup>①</sup></td>
                        <td>3.99</td>
                    </tr>
                    <tr>
                        <td>Full High-Definition (Full HD)<sup>①</sup></td>
                        <td>8.99</td>
                    </tr>
                    <tr>
                        <td>2K<sup>①</sup></td>
                        <td>15.99</td>
                    </tr>
                    <tr>
                        <td>2K+<sup>①</sup></td>
                        <td>35.99</td>
                    </tr>
                </tbody>
            </table>      

<Admonition type="info">
Agora determines video category based on aggregate video resolution, which is the sum of resolutions of all the video streams a user subscribes to at the same time. For details, see <a href="#aggregate">Aggregate video resolution</a>.
</Admonition>

<a name="aggregate"></a>
#### Aggregate video resolution

Agora adds up the resolution of all the video streams recorded at the same time to get the **aggregate resolution**, which categorizes video as follows:

| Video category                 | Aggregate video resolution                      |
| :----------------------------- | :----------------------------------------------------------- |
| High-Definition (HD)           | Up to 921,600 (1280 × 720)           |
| Full High-Definition (Full HD) | From greater than 921,600 (1280 × 720) to 2,073,600 (1920 × 1080) |
| 2K                             | From greater than 2,073,600 (1920 × 1080) to 3,686,400 (2560 × 1440)  |
| 2K+                            | From greater than 3,686,400 (2560 × 1440) to 8,847,360 (4096 × 2160)  |


For example, if the recording server records two video streams with resolutions of 1280 × 720 and 1920 × 1080 at the same time, the aggregated resolution is (1280 × 720) + (1920 × 1080) = 2,995,200. Because 2,995,200 is greater than 2,073,600 but less than 3,686,400, the recording service is charged based on the 2K video pricing.


## Examples

This section shows how to calculate the monthly audio and video service minutes of each category, as well as the total cost based on the corresponding unit price.

### Use-case description

Suppose you have an enabled project named Test under your Agora account, and the project uses the Agora On-Premise Recording SDK to implement the recording function.

The project records the following sessions between February 1 and February 28, 2021:

#### Session one

On February 4, 2021: Four users join the channel at the same time and have a video call for 6,000 seconds. One on-premise recording instance joins the channel and records only the audio streams of the four users.

In this session, the recording service generates only charges for the audio minutes.

| Session                     | Audio | HD video | Full HD video | 2K video | 2K+ video |
| :-------------------------- | :---- | :------- | :------------ | :------- | :-------- |
| Usage duration (in seconds) | 6,000 | 0        | 0             | 0        | 0         |

#### Session two

On February 9, 2021: Four users join the channel at the same time and have a video call for 6,000 seconds. Two on-premise recording instances join the channel and record only the audio streams of the four users.

In this session, the recording service generates only charges for the audio minutes.

| Session                     | Audio                  | HD video | Full HD video | 2K video | 2K+ video |
| :-------------------------- | :--------------------- | :------- | :------------ | :------- | :-------- |
| Usage duration (in seconds) | 6,000 + 6,000 = 12,000 | 0        | 0             | 0        | 0         |

#### Session three

On February 13, 2021: Four users join the channel at the same time and have a video call for 3,500 seconds. One on-premise recording instance joins the channel and records the audio and video streams of the four users. The video resolution of each user is 640 × 360.

In this session, the recording service generates charges for the video minutes. The aggregate video resolution is 4 × (640 × 360) = 921,600, falling into the category of HD.

| Session                     | Audio | HD video | Full HD video | 2K video | 2K+ video |
| :-------------------------- | :---- | :------- | :------------ | :------- | :-------- |
| Usage duration (in seconds) | 0     | 3,500    | 0             | 0        | 0         |

#### Session four

On February 15, 2021: Users A, B, and C join the channel at the same time and have interactive live video streaming. The video resolution of A, B, and C is 640 x 360, 1280 x 720, and 960 x 720. 1,680 seconds later, user D joins the channel, and has interactive live streaming with A, B, and C for 520 seconds. The video resolution of D is 1920 x 1080. During live streaming, one on-premise recording instance joins the channel and records the audio and video streams of all the users.

In this session, the recording service generates charges for the video minutes.

In the initial 1,680 seconds, the aggregate resolution is 640 x 360 + 1280 x 720 + 960 x 720 = 1,843,200, falling into the category of Full HD video.

In the subsequent 520 seconds, the aggregate resolution is 640 x 360 + 1280 x 720 + 960 x 720 + 1920 x 1080 = 3,916,800, falling into the category of 2K+ video.

| Session                     | Audio | HD video | Full HD video | 2K video | 2K+ video |
| :-------------------------- | :---- | :------- | :------------ | :------- | :-------- |
| Usage duration (in seconds) | 0     | 0        | 1,680         | 0        | 520       |

### Cost calculation

<table class="relative-table confluenceTable" resolved="">
                <colgroup span="1">
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                    <col span="1" />
                </colgroup>
                <tbody>
                    <tr>
                        <th class="confluenceTh" rowspan="2"
                            colspan="1">Date</th>
                        <th class="confluenceTh" colspan="5"
                            rowspan="1">Actual usage duration (seconds)</th>
                        <th class="confluenceTh" colspan="5"
                            rowspan="1">Usage duration displayed on Agora Console (minutes)</th>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>Audio</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>HD video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>Full HD video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>2K video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>2K+ video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>Audio</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>HD video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>Full HD video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>2K video</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>2K+ video</p>
                        </td>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">2025-02-04</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">6,000</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">100</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                    </tr>
                    <tr>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">2025-02-09</td>
                        <td class="confluenceTd"
                            owspan="1" colspan="1">12,000</td>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">0</td>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            owspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">200</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                    </tr>
                    <tr>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">2025-02-13</td>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">0</td>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">3,500</td>
                        <td class="confluenceTd"
                            rowspan="1" colspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">59</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">2025-02-15</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">1,680</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">520</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">28</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">9</td>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">Monthly usage</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">18,000</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">3,500</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">1,680</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">520</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">300</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">59</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">28</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">9</td>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1"><strong>Billable service minutes</strong></td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">300<br /> minutes</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">59<br /> minutes</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">28<br /> minutes</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">9<br /> minutes</td>
                        <td class="confluenceTd" colspan="5"
                            rowspan="1"><strong>The usage displayed on Agora Console is for
                                reference only and not used as the actual billing
                            basis.</strong></td>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>Cost of each service</p>
                            <p>($US)</p>
                        </td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">(300/1000 )<br /> × 0.99<br /> = 0.297</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">(59/1000)<br /> × 3.99<br /> = 0.23541</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">(28/1000) <br />× 8.99<br /> = 0.25172</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">0</td>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">(9/1000)<br /> × 35.99<br /> = 0.32391</td>
                        <td class="confluenceTd" colspan="5"
                            rowspan="1"></td>
                    </tr>
                    <tr>
                        <td class="confluenceTd" colspan="1"
                            rowspan="1">
                            <p>Total cost</p>
                            <p>($US)</p>
                        </td>
                        <td class="confluenceTd" colspan="5"
                            rowspan="1">
                            <p>1.11</p>
                            <p>(0.297 + 2.3541 + 2.5172 + 0.32391 =
                                        1.10804 ≈ 1.11）</p>
                        </td>
                        <td class="confluenceTd" colspan="5"
                            rowspan="1"></td>
                    </tr>
                </tbody>
            </table>


<Admonition type="info"><ul><li>Agora rounds up the monthly total fees to two decimal places.</li><li>Agora gives each Agora account 10,000 minutes of free time per month. Because the monthly total service minutes in the above example do not exceed 10,000 minutes, the service is free of charge and the bill would show $US 0.</li></ul></Admonition>


## Considerations

### Accuracy of service minutes

At the end of each month, Agora adds up the usage duration (in seconds) of audio and video in each category, and divides them by 60 to get the respective service minutes (rounded up to the nearest integer). For example, if the duration of audio service of the month is 59 seconds, then the audio service minutes is calculated as 1 minute; if the duration of video service is 61 seconds, then the video service minutes is calculated as 2 minutes. The margin of error for service minutes for each month is within 1 minute. 





### Video resolution in the dual-stream use-case

When the user being recorded enables [dual-stream mode](../../video-calling/reference/glossary#dual-stream-mode), the recording service can receive only one stream at a time:

- If the recording server records the high-quality video stream, the aggregate video resolution is calculated based on the resolution of the high-quality video.
- If the recording server records the low-quality video stream, the aggregate video resolution is calculated based on the resolution of the video received by the server.

### Resolution calibration

When calculating the aggregate resolution, Agora counts the resolution of 225,280 (640 × 352) as 640 × 360.

<a name="question"></a>
## Q&A



<details>
	<summary><font color="#3ab7f8">Question: How does Agora charge if I use different recording modes?</font></summary>

Your recording fee has nothing to do with the recording mode you choose. Regardless of whether you use the individual mode or composite mode, your recording fee relates only to the number of the streams recorded, the recording time, and the aggregate recording resolutions. The number of the streams recorded does not affect the recording duration, but affects the aggregate recording resolution.

</details>



<details>
	<summary><font color="#3ab7f8">Question: Does Agora charge the screen capture function separately?</font></summary>

Agora does not charge for the screen capture function separately. Screen capture is a different form of the recording function. The recording service joins the corresponding channel and subscribes to the specified video streams all the time in order to capture screens at the specified interval. Therefore, if you have enabled the screen capture function, Agora charges you for the full-time recording of the corresponding stream, but do not charge you for the screen capture function separately.

</details>







## Relevant links

- [Agora's free-of-charge policy for the first 10,000 minutes](https://docs.agora.io/en/faq/billing_free)
- [Billing, free deduction, and account suspension](https://docs.agora.io/en/faq/billing_account)