---
title: Pricing
sidebar_position: 1
description: >
    Provides you with information on billing, fee deductions, free-of-charge policy, and any suspension to your account based on the account type.
---


export const toc = [{}]

This page introduces the pricing policy for <Vg k="WHITE" />.

Your pricing details may differ if you have signed a contract with Agora. If your scenario involves other Agora products or services, such as the <Vg k="VSDK" />, <Vg k="MESS_SDK" />, or <Vg k="CREC" />, expect additional charges for these products or services. For details, see the pricing policy for each Agora product or service.

## <Vg k="WHITE" /> pricing

Billing for <Vg k="WHITE" /> begins once you enable and implement the service in your project. Agora sends your bill and deducts the payment from your account on a monthly basis. For details, see [Billing, fee deduction, and account suspension](/help/account-and-billing/billing_account). 
The unit price for each whiteboard feature is as follows:

| Whiteboard feature   | Pricing, US$/1,000 minutes |
| :------------------- |:---------------------------|
| Online whiteboard    | 1.40                       |
| File conversion      | 0.50                       |

## Cost calculation

At the end of each month, Agora adds up the usage of each whiteboard feature in all projects under your [Agora account](https://console.agora.io/) and subtracts your monthly free usage allowances. Agora multiplies each resulting usage number by the corresponding price and adds up the cost of each feature to get the total cost for that month.
<Vg k="WHITE" /> provides the following features:

- Online whiteboard
- File conversion, including file conversion to images and file conversion to web pages

**Cost of each whiteboard feature = (monthly total usage - free-of-charge usage) × unit price**

**Total cost = online whiteboard cost + file conversion cost**

### Usage calculation

This section describes how to calculate the usage of each whiteboard feature.

#### Online whiteboard

The usage duration of each whiteboard room equals **the total sum of usage duration of all users** in the room.

For each user, Agora calculates the usage duration from the user joining a room to the user leaving the room. **The usage duration is calculated in minutes.**

#### File conversion

Agora calculates the usage amount by the number of images and web pages successfully converted from source files.

<ul><li>The cost of converting a file to web pages is five times the cost of converting it to images. When charging for file conversion to web pages, Agora multiplies the number of generated web pages by five in order to use a consistent unit price for the file conversion feature.</li><li>Agora does not charge for a failed file conversion task. You can call the [Query file conversion progress](../reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task) API to get the result of a file conversion task.</li><li>The file conversion feature can also be charged by QPS. See [QPS-based Pricing](../reference/qps-pricing).</li></ul>

### Free-of-charge usage

Agora gives each whiteboard feature the following free-of-charge usage each month:

| Whiteboard feature   | Monthly free-of-charge usage |
| :------------------- | :--------------------------- |
| Online whiteboard    | The first 10,000 minutes     |
| File conversion      | The first 1000 images (effective from September 1, 2022)        |

<div class="alert note"><ul><li>If the monthly total usage of a whiteboard feature does not exceed its free usage allowance, the feature is free of charge for that month. </li><li>The remaining free-of-charge usage is cleared at the end of each calendar month.</li></ul></div>

## Check your current usage

You can check your usage of <Vg k="WHITE" /> in <Vg k="CONSOLE" />. Perform the following steps:

1. Log in to [<Vg k="CONSOLE" />](https://console.agora.io/) and click the **Products & Usage** button on the left navigation panel.

2. Click the arrowhead in the top left corner, and select the project you want to check in the drop-down box.

3. Click **Duration** under **Whiteboard**, select a time frame, and check the usage duration.
 ![](https://web-cdn.agora.io/docs-files/1620288770652)


- The time frame cannot exceed 12 months.
- Only Agora accounts that are assigned with the role of Admin or Finance have access to the usage statistics.
- The usage duration provided by <Vg k="CONSOLE" /> is for reference only. Your actual billing may differ.


## Examples

This section shows how to calculate your monthly usage of <Vg k="WHITE" />, as well as the total cost based on the corresponding unit price.

### Scenario description

User A joins a whiteboard room to give an online lecture and successfully converts a 50-page PPTX file to HTML files using the file conversion feature. Another 200 users join the room to watch the lecture. The lecture lasts 60 minutes. When the lecture ends, all users leave the room at the same time.

The usage calculation is as follows:


| Feature                         | Usage                                                              |
| :------------------------------ |:-------------------------------------------------------------------|
| Online whiteboard               | <li>User A: 60 minutes</li><li>Another 200 users: 60 × 200 minutes</li> |
| File conversion to web page | 50 web pages = 50 × 5 = 250 images                                 |

### Calculation

The following table shows the calculation of the total cost of the lecture:

<div><table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th><span class="td-span"><span class="md-plain">Billed service</span></span></th><th><span class="td-span"><span class="md-plain">Unit price, US$/1,000 minutes </span></span></th><th><span class="td-span"><span class="md-plain">Cost of each service, US$</span></span></th><th><span class="td-span"><span class="md-plain">Total cost, US$</span></span></th></tr></thead><tbody><tr><td class="confluenceTd"><span class="td-span"><span class="md-plain">Online whiteboard</span></span></td><td class="confluenceTd"><span class="td-span"><span class="md-plain">$1.40/1,000 minutes</span></span></td><td class="confluenceTd"><span class="td-span"><span class="md-plain">(12,060 - 10,000)/1000 × 1.40 = 2.884</span></span></td><td rowspan="3" class="confluenceTd"><span class="td-span"><span class="md-plain">2.884 </span><span><strong>≈ 2.89</strong></span></span><br/><br/></td></tr><tr><td class="confluenceTd"><span class="td-span"><span class="md-plain">Document conversion to web page</span></span></td><td class="confluenceTd"><span class="td-span"><span class="md-plain">$0.50/1,000 images</span></span></td><td class="confluenceTd">0 (The first 1000 converted images are free of charge）<span> </span></td></tr></tbody></table></div>

Agora rounds up the total cost to two decimal places.

## Q&A

- Will usage calculation continue if live streaming has ended but users are still in the room?

    Yes. Usage calculation for <Vg k="WHITE" /> depends on the presence of active long-lived connections. To avoid additional costs, Agora recommends that you:

    - Call `disconnect()` to cut off a user's connection when the user leaves the room, and ensure that you receive the `onPhaseChanged(disconnected)` callback.
    - Call the [Interactive Whiteboard RESTful API](../reference/whiteboard-api/room-management#disableroom)  on your app server to move all users out of the room when live streaming ends.


- Does billing begin when a room is created?

  No, because no user joins the room.

- Does joining a room using different modes result in different costs?

  No. The usage calculation and unit price are the same whether the user joins a room in interactive mode or subscription mode.



