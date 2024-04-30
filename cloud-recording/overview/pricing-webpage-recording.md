---
title: "Pricing for Web Page Recording"
sidebar_position: 4
type: docs
platform_selector: false
description: >
  Depending on the number of minutes you intend to record, estimate your monthly cost for Web Page Recording. 
---

This page explains how <Vg k="COMPANY" /> calculates your monthly bill for 
[Web Page Recording](../develop/webpage-mode). 

If you have already signed a contract with Agora, the billing terms and 
conditions within that contract take precedence.

## Web Page Recording pricing 

The unit pricing for video usage is as follows:

| Video category                 | Pricing, $US/1,000 minutes |
| :----------------------------- |:---------------------------|
| High-definition (HD)           | 14                         |
| Full high-definition (Full HD) | 28                         |

When you use Web Page Recording, Agora charges you based on the usage and resolution of the recorded videos.

If you use other Agora products or services in the web page being recorded, 
such as [Video Calling](/video-calling/overview/product-overview), 
[Interactive Whiteboard](../../interactive-whiteboard/overview/product-overview), 
or [Real-time Messaging](../../signaling/overview/product-overview), expect additional charges. 

See pricing documentation of each product or service for details.

## Cost calculation

Billing occurs monthly. At the end of each month, Agora calculates the total duration of web page recording 
usage (in minutes) for that month in all projects under your Agora account, 
[publishes bills, and performs deductions](../reference/billing-policies). 
Note that this usage is divided into different video categories. 
After deducting the monthly 
[10,000 free-of-charge minutes](../reference/billing-policies#agoras-free-of-charge-policy-for-the-first-10000-minutes) 
that Agora grants to every account, Agora multiplies any remaining usage by its corresponding unit price 
and adds up the costs to get the total cost for that month.

The basic formula is shown here:

**Monthly cost = total usage per category × unit price per category**

### Usage

For the web page recording service, Agora calculates usage from the moment a recording begins until the moment 
it ends, measured in seconds.

When starting a web page recording, you can [set the video profile](../develop/recording-video-profile) 
(resolution, frame rate, and bitrate) for the output video stream.

### Resolution 

Based on the resolution of the output video of the web page recording, Agora divides the usage into the
following categories:

| Video category                 | Video resolution                                             |
| :----------------------------- | :----------------------------------------------------------- |
| High-definition (HD)           | Up to 921,600 (1280 × 720）                                  |
| Full high-definition (Full HD) | From greater than 921,600 (1280 × 720) to 2,073,600 (1920 × 1080) |

## Preferential billing policies

If Video SDK is used in the web page being recorded to implement real-time communications, and the user is 
subscribed to a channel with a high-definition (HD) [aggregate video resolution](pricing#aggregate), Agora waives the cost of the video <Vg k="VSDK" /> usage during the web page recording; only the web page recording fees apply. Real-time communication at higher aggregate resolutions does not receive this discount.

## Examples 

This section provides a simple example of calculating the cost of a web page recording session.

Suppose you start a web page recording process that runs for 6,000 seconds, where you set the resolution of the output video as 960 × 720.

The output resolution is 691,200, which puts it into the high-definition (HD) category. The unit pricing for HD video is US$14/1,000 minutes.

To calculate billable time, the usage is converted from seconds to minutes, so 6,000 seconds of usage converts to 100 billable minutes.

| Process                     | HD video | Full HD video |
| :-------------------------- | :------- | :------------ |
| Usage duration (in seconds) | 6,000    | 0             |
| Billable service minutes    | 100      | 0             |

Therefore, the cost is as follows:

**Cost = video unit price × video duration usage = 14 × (100/1000) = 1.4**

Therefore, the actual recording fee is US$1.40.

## Reference

### Accuracy of service minutes

Agora bills usage by the minute but records usage by the second. Monthly usage for billing is actually calculated by totaling each type of usage (in seconds) and then dividing by 60, rounding up to the nearest integer. For example, if the HD service usage for a month is 59 seconds, then this is billed as 1 minute; if the Full HD service usage for a month is 61 seconds, then this is billed as 2 minutes. Therefore, the margin of error for usage of each category per month is less than 1 minute.

### Multiple recordings

If two web page recording processes are started for the same web page, Agora charges fees for both.

### Charge duration

The charging will continue until the web page recording stops. 
You should set a reasonable [maxRecordingHour](../reference/restful-api#start#extension-service-configuration) based on the 
actual business scenario or actively stop the web page recording. 

## See also

- [Agora's free-of-charge policy for the first 10,000 minutes](../reference/billing-policies#agoras-free-of-charge-policy-for-the-first-10000-minutes)
- [Billing, free deduction, and account suspension](../reference/billing-policies#billing-fee-deductions-and-account-suspension-policies)
- [Cloud Recording pricing](pricing)