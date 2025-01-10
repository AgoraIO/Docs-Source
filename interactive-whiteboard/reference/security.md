---
title: Security
sidebar_position: 10
description: >
    The security practices that Agora has implemented for Agora Interactive Whiteboard.
---

Data security and user privacy are the top priorities for Agora. To provide safe and reliable services, Agora adopts industry-recognized security standards and security best practices at every layer for each product.

<Vg k="WHITE" /> is a newly launched product that provides online whiteboard rooms where users can present ideas, share multimedia content, and collaborate on projects from multiple devices simultaneously. Starting in the product-design phase, Agora has assessed and prepared for the potential security threats associated with these functions and has implemented a variety of measures to secure the high availability of <Vg k="WHITE" /> as well as the confidentiality and integrity of your data.

This page describes the security practices that Agora has implemented for <Vg k="WHITE" />.

## Identity and access management

Securing access to your services and resources starts with identity and access controls. <Vg k="WHITE" /> uses tokens for user authentication. <Vg k="WHITE" /> offers three types of tokens: SDK Token, Room Token, and Task Token, in descending order of granted permissions. These tokens must be generated with access keys and secret keys by role and include a validity period; they must also be issued from your app server to your app client. The <Vg k="WHITE" /> server verifies the information stored in the token when your app client requests to access the whiteboard services.

Refer to the following guides for detailed information on <Vg k="WHITE" /> tokens:

- [<Vg k="WHITE" /> Token Overview](../whiteboard-sdk/develop/authentication-workflow): Describes the different types of whiteboard tokens and their uses, the various methods of generating a token, and token safety precautions.
- [Generate Token Using an App Server](../whiteboard-sdk/develop/generate-token-app-server): Introduces how to generate tokens at your app server using code samples.
- [Generate Token Using REST API](../whiteboard-sdk/develop/generate-token-rest): Describes the RESTful APIs for generating whiteboard tokens.

## Data encryption and storage

<Vg k="WHITE" /> does not store any of your business data or user data except for caching it for transmission purposes. The cached data is immediately released after the completion of the business-dependent logic. To guarantee data confidentiality during transmission, Agora uses the Secure Sockets Layer (SSL) encryption protocol.

Data centers hosting <Vg k="WHITE" /> are maintained by certified and industry-leading cloud service providers, offering state-of-the-art physical protection for the servers and infrastructure that comprise the Agora environment.

<Vg k="WHITE" /> also offers server-side file conversion and screenshotting. Agora does not store any files or screenshots when users use these features. The transcoded files and the captured screenshots are stored in the third-party cloud storage designated by you. In addition, these features are disabled by default. Only after you enable the features and specify the storage space. the users authorized by you can access the services and the stored resources.

Refer to the following articles for more information on file conversion and taking screenshots:

- [Enable <Vg k="WHITE" />](../whiteboard-sdk/get-started/enable-whiteboard): The **Enable whiteboard server-side features** section describes how to configure the third-party storage space.
- [File Conversion Overview](../reference/whiteboard-api/file-conversion): The **Start file conversion** section describes the basic workflow for converting a file.

## Network geofencing

To conform to the laws and regulations of different countries and regions, <Vg k="WHITE" /> supports network geofencing, which allows you to specify a data center and limits the transmission of your business data to the service area the data center covers.

Now <Vg k="WHITE" /> sets up five data centers and each data center provides services to specific areas, as follows:

| Data center | Location                      | Service area                             |
| :---------- | :---------------------------- | :--------------------------------------- |
| `us-sv`     | Silicon Valley, United States | North America and South America          |
| `sg`        | Singapore                     | Singapore, East Asia, and Southeast Asia |
| `in-mum`    | Mumbai, India                 | India                                    |
| `gb-lon`    | London, England               | Europe                                   |
| `cn-hz`     | Hangzhou, China               | Areas not covered by other data centers  |

<Vg k="WHITE" /> has implemented network geofencing in each server-side RESTful API as well as all client-side whiteboard SDKs. This enables you to specify a data center whenever you create a whiteboard room or launch a file-conversion task by calling the RESTful APIs, or whenever you enable a user to join a whiteboard room by calling the methods provided by the SDKs.

Refer to the following API references for more information:

- [RESTful APIs](../reference/whiteboard-api/overview)
- <Link to="{{Global.API_REF_WEB_WHITE}}/index.html">Web SDK APIs</Link>
- <Link to="{{Global.API_REF_ANDROID_WHITE}}/index.html">Android SDK APIs</Link>
- <Link to="{{Global.API_REF_IOS_WHITE}}/docs/headers/Agora-Interactive-Whiteboard-Objective-C-Overview.html">iOS SDK APIs</Link>


With network geofencing enabled, data transfer is restricted to the service areas that your specified data center covers. However, this does not prohibit users located in different areas from communicating with each other, as long as they join the same whiteboard room. For example, when a teacher creates a whiteboard room that is geofenced in Europe, students located in India can join the room through the global accelerator and interact with the teacher. If the students join a whiteboard room that is geofenced in India, then they cannot communicate with the teacher in Europe, because no data is allowed to be transmitted across data centers.

## Network redundancy

<Vg k="WHITE" /> deploys Kubernetes clusters to build fault tolerance and disaster recovery into its services. This ensures these services are not interrupted due to a single point of failure.

<Vg k="WHITE" /> adopts incremental data synchronization, serialized data compression, and optimized network congestion control algorithms to ensure high data-packet delivery success rate within the smallest time window.

## Ongoing commitment to security

Agora is committed to building interactive whiteboard services with compliance, safety, security, and trust. If you think you might have found a security vulnerability within <Vg k="WHITE" />, please contact the Agora security team directly at [security@agora.io](mailto:security@agora.io).