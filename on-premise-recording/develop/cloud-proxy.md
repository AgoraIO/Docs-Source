---
title: 'Cloud Proxy'
sidebar_position: 6
type: docs
description: >
  To ensure that enterprise users can connect to Agora's services through a firewall, Agora supports setting up a cloud proxy. 
---

## Introduction

Enterprises with high-security requirements usually have firewalls that restrict employees from visiting unauthorized sites to protect internal information.

To ensure that enterprise users can connect to Agora's services through a firewall, Agora supports setting up a cloud proxy. 

Compared with setting a single proxy server, the cloud proxy is more flexible and stable, thus widely implemented in organizations with high-security requirements, such as large-scale enterprises, hospitals, universities, and banks.

## Implementation

<div class="note alert">The Agora On-Premise Recording SDK v3.0.0 or later supports the cloud proxy service. Before using the Agora Cloud Proxy Service, ensure that you prepare the development environment and integrate the Agora On-Premise Recording SDK v3.0.0 or later.</div>

Follow these steps to use the cloud proxy service.

1. Contact support@agora.io with the following information to enable the cloud proxy service:

  - The regions to use cloud proxy.
  - The scale of your app in terms of channel concurrency.
  - Your Internet service provider.

2. Add the following test IP addresses and ports to your whitelist.
    The sources are the clients that integrate the Agora On-Premise Recording SDK.

   | Protocol | Destination IP address  | Port                   | Port function      |
 | ---- | ------------- | ---------------------- | ---------------------- |
 | TCP  | 120.92.118.34 | 4000                   | Message data transmission |
 | TCP  | 120.92.18.162 | 4000                   | Message data transmission |
 | TCP  | 47.74.211.17  | 1080, 8000, 25000, 9700 | Edge node communication |
 | TCP  | 52.80.192.229 | 1080, 8000, 25000, 9700 | Edge node communication |
 | TCP  | 52.52.84.170  | 1080, 8000, 25000, 9700 | Edge node communication |
 | TCP  | 47.96.234.219 | 1080, 8000, 25000, 9700 | Edge node communication |
 | UDP  | 120.92.118.34 | 4500 to 4650            | Media data exchange |
 | UDP  | 120.92.18.162 | 4500 to 4650            | Media data exchange |
 | UDP  | 47.74.211.17  | 1080, 8000, 25000, 9700 | Edge node communication |
 | UDP  | 52.80.192.229 | 1080, 8000, 25000, 9700 | Edge node communication |
 | UDP  | 52.52.84.170  | 1080, 8000, 25000, 9700 | Edge node communication |
 | UDP  | 47.96.234.219 | 1080, 8000, 25000, 9700 | Edge node communication |

<Admonition type="info">These IP addresses and ports are for testing purposes only. In a production environment, apply for the dedicated IP addresses and ports.</Admonition>

3. When the recording server joins a channel, set `enableCloudProxy` in `RecordingConfig` as `true` to enable the cloud proxy service. Agora will configure the default domain of the cloud proxy service for you. If you can not resolve the domain name to an IP address, take the following steps to directly configure a list of proxy server IP addresses:

  1. Set `proxyType` in `RecordingConfig` as `2`;
  
  2. Set `proxyServer` in `RecordingConfig` as  `"47.74.211.17,52.80.192.229,52.52.84.170,47.96.234.219:0"`.
 
  > If you use our command-line demo, add `--enableCloudProxy 1 --proxyType ${type} --proxyServer ${ip,port}` to your command when starting a recording.

4. To use the cloud proxy service in the production environment, contact support@agora.io for the IP addresses and ports for the production environment and add these resources to your whitelist.


