---
title: 'Cloud Proxy'
sidebar_position: 6
type: docs
description: >
  To ensure that enterprise users can connect to Agora's services through a firewall, Agora supports setting up a cloud proxy. 
---

Large enterprises, hospitals, universities, banks, and other institutions commonly deploy firewalls to meet their stringent security requirements. To ensure uninterrupted access to its services for enterprise users behind firewalls, Agora offers firewall whitelist and <Vg k="CP" /> services.

Admins enable users to use <Vpd k="SDK" /> in network-restricted environments by adding specific IP addresses and ports to the firewall whitelist. Users make API calls to configure the <Vg k="CP" /> service.

## Understand the tech

<Vg k="CP" /> works as follows:

1. <Vpd k="SDK" /> initiates a request to <Vg k="CP" />.
1. <Vg k="CP" /> returns the corresponding proxy information.
1. Agora SDK sends data to <Vg k="CP" />. <Vg k="CP" /> receives the data and transmits it to Agora SD-RTN™.
1. Agora SD-RTN™ returns data to <Vg k="CP" />. <Vg k="CP" /> receives the data and sends it to the SDK.

<details>
<summary>Cloud proxy workflow</summary>

![](/images/video-sdk/cloud-proxy-tech.svg)
</details>

## Prerequisites

Ensure that you have implemented the [Quickstart](/on-premise-recording/get-started/) in your project.

## Implement <Vg k="CP" />

Take the following steps to implement the use of <Vg k="CP" /> in your <Vpl k="CLIENT" />:

1. Contact [Agora support](mailto:support@agora.io) and provide the following information to request <Vg k="CP" /> service:
    - App ID
    - <Vg k="CP" /> service usage area
    - Concurrency scale
    - Network operator and other relevant information

2. After receiving the request, <Vg k="COMPANY" /> provides the IP addresses and ports used for <Vg k="CP" />.

3. Add the IP addresses and ports provided by <Vg k="COMPANY" /> to your firewall whitelist.

4. To enable the cloud proxy service, call `setBool` and set the private parameter `rtc.enable_proxy` to `true`:

<PlatformWrapper platform="linux-cpp">
  ```cpp
  auto agoraParameter = service->getAgoraParameter();
  agoraParameter->setBool("rtc.enable_proxy", true);
  ```
</PlatformWrapper>
<PlatformWrapper platform="linux-java">
  ```java
  AgoraParameter parameter = agoraService.getAgoraParameter();
  parameter.setBool("rtc.enable_proxy", true);
  ```
</PlatformWrapper>


5. After enabling the proxy, test whether audio and video recording function correctly.

6. To disable the cloud proxy service, set `rtc.enable_proxy` to `false`.


