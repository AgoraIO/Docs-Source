---
title: Pricing
sidebar_position: 1
description: >
    Provides you with information on billing, fee deductions, free-of-charge policy, and any suspension to your account based on the account type.
---


export const toc = [{}]

This page explains how <Vg k="COMPANY" /> calculates your monthly bill for <Vg k="WHITE" />. 

If you have already signed a contract with <Vg k="COMPANY" />, the billing terms and conditions within that contract take precedence.

## <Vg k="WHITE" /> pricing

The unit prices for whiteboard features are as follows: 

| Whiteboard feature | Volume                      | Pricing                |
|:-------------------|:----------------------------|:-----------------------|
| Online whiteboard  | Under 10,000 minutes        | Free                   |
|                    | 10,000 - 60,000 minutes     | 1.40 US$/1,000 minutes |
|                    | 60,000 - 120,000 minutes    | 1.30 US$/1,000 minutes |
|                    | 120,000 - 1,000,000 minutes | 1.10 US$/1,000 minutes |
|                    | Over 1,000,000 minutes      | Contact Agora Sales    |
| File conversion    | Under 100,000 images        | Free                   |
|                    | Over 100,000 images         | 0.50 US$/1,000 images  |

If your scenario involves other Agora products or services, such as the <Vg k="VIDEO" />, <Vg k="MESS" />, or <Vg k="CREC" />, expect additional charges for these products or services. For details, see the pricing policy for each Agora product or service.

## Cost calculation

Billing for <Vg k="WHITE" /> begins once you enable and implement the service in your project and occurs monthly. 

<Vg k="COMPANY" /> calculates your monthly pricing by adding up the usage of each whiteboard feature in all 
projects under your [Agora account](https://console.agora.io/), subtracting your monthly free usage allowances, 
multiplying each resulting usage number by the corresponding price, and adding up the cost of each feature.

The basic formulas are shown here:

**Monthly cost** = **monthly online whiteboard cost** + **monthly file conversion cost**

**Monthly feature cost** = **(monthly total usage - free-of-charge usage) × unit price**

### Online whiteboard usage

The usage duration of each whiteboard room equals **the total sum of usage duration of all users** in the room. 
Billing **does not start** when the room is created, but rather when users join. 

For each user, Agora calculates the usage duration from when they join to when they leave the room. 

Note that usage calculation will continue if live streaming has ended but users are still in the room.

To avoid additional costs, Agora recommends that you:

    - Call `disconnect()` to cut off a user's connection when the user leaves the room, and ensure that you receive the `onPhaseChanged(disconnected)` callback.
    - Call the [Interactive Whiteboard RESTful API](../reference/whiteboard-api/room-management##disable-a-room-patch)  on your app server to move all users out of the room when live streaming ends.

The usage calculation and unit price are the same whether the user joins a room in interactive mode or subscription mode. 

The usage duration is calculated in minutes.

### File conversion usage

Agora calculates the usage amount by the number of images and web pages successfully converted from source files.

The cost of converting a file to web pages is five times the cost of converting it to images. 
When charging for file conversion to web pages, Agora multiplies the number of generated web pages by 
five in order to use a consistent unit price for the file conversion feature. 

Agora does not charge for a failed file conversion task. 
You can call the [Query file conversion progress](../reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task) 
API to get the result of a file conversion task. 

The file conversion feature can also be charged by QPS. See [QPS-based Pricing](../reference/qps-pricing).

## Examples

This section illustrates how <Vg k="COMPANY" /> calculates the cost for <Vg k="WHITE" />.

Suppose user A joins a whiteboard room to give an online lecture and successfully converts a 
50-page PPTX file to HTML files using the file conversion feature. Another 200 users join the room to 
watch the lecture. The lecture lasts 60 minutes. When the lecture ends, all users leave the room at the 
same time.

The usage calculation is as follows:

| Feature                         | Usage                                                              |
| :------------------------------ |:-------------------------------------------------------------------|
| Online whiteboard               | <li>User A: 60 minutes</li><li>Another 200 users: 60 × 200 minutes</li> |
| File conversion to web page | 50 web pages = 50 × 5 = 250 images                                 |

### Calculate cost

The following table shows the calculation of the total cost of the lecture:

<div><table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th><span class="td-span"><span class="md-plain">Billed service</span></span></th><th><span class="td-span"><span class="md-plain">Unit price, US$/1,000 minutes </span></span></th><th><span class="td-span"><span class="md-plain">Cost of each service, US$</span></span></th><th><span class="td-span"><span class="md-plain">Total cost, US$</span></span></th></tr></thead><tbody><tr><td class="confluenceTd"><span class="td-span"><span class="md-plain">Online whiteboard</span></span></td><td class="confluenceTd"><span class="td-span"><span class="md-plain">$1.40/1,000 minutes</span></span></td><td class="confluenceTd"><span class="td-span"><span class="md-plain">(12,060 - 10,000)/1000 × 1.40 = 2.884</span></span></td><td rowspan="3" class="confluenceTd"><span class="td-span"><span class="md-plain">2.884 </span><span><strong>≈ 2.89</strong></span></span><br/><br/></td></tr><tr><td class="confluenceTd"><span class="td-span"><span class="md-plain">Document conversion to web page</span></span></td><td class="confluenceTd"><span class="td-span"><span class="md-plain">$0.50/1,000 images</span></span></td><td class="confluenceTd">0 (The first 100,000 converted images are free of charge）<span> </span></td></tr></tbody></table></div>

Agora rounds up the total cost to two decimal places.


## Reference

### Check your current usage

You can check your usage of <Vg k="WHITE" /> in <Vg k="CONSOLE" />. Perform the following steps:

1. Log in to [<Vg k="CONSOLE" />](https://console.agora.io/) and click the **Products & Usage** button on the left navigation panel.

2. Click the arrowhead in the top left corner, and select the project you want to check in the drop-down box.

3. Click **Duration** under **Whiteboard**, select a time frame, and check the usage duration.

 ![](https://web-cdn.agora.io/docs-files/1620288770652)

- The time frame cannot exceed 12 months.
- Only Agora accounts that are assigned with the role of Admin or Finance have access to the usage statistics.
- The usage duration provided by <Vg k="CONSOLE" /> is for reference only. Your actual billing may differ.

## See also 

- [Billing policies and free-of-charge policy](../reference/billing-policies)
- [QPS-based Pricing](../reference/qps-pricing)

