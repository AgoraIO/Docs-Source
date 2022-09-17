---
title: 'Enable Interactive Whiteboard'
sidebar_position: 1
type: docs
description: >
  Enable and configure Interactive Whiteboard
---

To use Agora Interactive Whiteboard, you need to enable and configure the whiteboard service in [Agora Console](https://console.agora.io/#onboarding).

## Prerequisites

Before enabling the whiteboard feature, ensure that you meet the following requirements:
- A valid Agora account. If you have a Netless account, you must complete the account migration first. See [Migrate from Netless to Agora](/en/whiteboard/netless_migration).
- Active Agora projects. If you have not created a project, see <a href="https://docs.agora.io/en/Agora%20Platform/manage_projects?platform=All%20Platforms">Manage Projects</a >.

## Enable the whiteboard service

Follow these steps to enable the whiteboard service in Agora Console:

1. Log in to [Agora Console](https://console.agora.io/), and click the **Project Management** icon on the left navigation panel.

2. On the **Project Management** page, click **Config** for the project for which you want to enable the whiteboard service.
 ![](https://web-cdn.agora.io/docs-files/1641971710869)

3. Under **Real-time engagement extensions**, find **Whiteboard**, and click **Enable**.
 ![](https://web-cdn.agora.io/docs-files/1638182516342)

4. Read the pop-up prompt carefully, and click **Confirm**. 
   The **Enable** button changes to the **Config** button, which allows you to configure the whiteboard service.
	 ![](https://web-cdn.agora.io/docs-files/1638182576182)

## Get security credentials for your whiteboard project

Agora Console assigns the following security credentials to each whiteboard project:

- **AppIdentifier**: The unique App Identifier, which is required for initializing the whiteboard SDK.
- **AK** and **SK**: A pair of access keys, which you can use to generate whiteboard tokens.  See [Generate a Token at App Server](/en/whiteboard/generate_whiteboard_token_at_app_server).
- **sdkToken**: An [SDK Token (a dynamic key)](/en/whiteboard/whiteboard_token_overview) for test purpose. In a production environment, you need to generate an SDK token at your app server either by using the [code samples](/en/whiteboard/generate_whiteboard_token_at_app_server) or calling the [RESTful API](/en/whiteboard/generate_whiteboard_token). 

To get the security credentials, do the following steps:

1. On the [Project Management](https://console.agora.io/projects) page in Agora Console, find the project that has the whiteboard feature enabled, and click **Edit**.

3. On the **Edit Project** page, find **Whiteboard**, and click **Config**.

3. Navigate to the **Basic information** section, click the eye icons to copy the **AppIdentifier**, **AK**, and **SK**. Save them to a secure location.
   ![](https://web-cdn.agora.io/docs-files/1620392824592)

4. Click **Generate sdk Token**, read the pop-up prompt carefully, and then click **Copy sdkToken**. Save the SDK Token to a secure location.
   ![](https://web-cdn.agora.io/docs-files/1619518873012)
	
Unexpected exposure of the security credentials can cause severe security problems. To enhance security, Agora recommends the following practices:

- Do not send the AK and SK to your app clients or hard-code them in your app. Ensure that only your app server is allowed to read the keys from the configuration file.
- Because the SDK Token generated at the Console grants a high level of permission, do not send them to your app clients; otherwise, there might be a risk of leakage.

## Enable whiteboard server-side features

Agora Interactive Whiteboard sets up [five data centers](https://docs.agora.io/en/whiteboard/whiteboard_security_practices?platform=Web#network-geofencing) and each data center provides the following server-side features: 

- File conversion, including **Docs to Picture** and **Docs to web**. 
After enabling the file conversion feature, you can call the [RESTful APIs](/en/whiteboard/whiteboard_file_conversion) to launch a file conversion task or query the conversion progress.
Agora charges for the file-conversion feature. See [Pricing](/en/whiteboard/billing_whiteboard).
- **Screenshot**. After enabling the screenshot feature, you can call the [RESTful APIs](/en/whiteboard/whiteboard_screenshot) to take screenshots.

Follow these steps to enable one or more features and configure the storage settings:

1. Go to the [Project Management](https://console.agora.io/projects) page in Agora Console, find the project that has the whiteboard feature enabled, and click **Edit**.

2. On the **Edit Project** page, find **Whiteboard**, and click **Config**.

3. Under **Services**, select a data center, and click **Config**. The data center must be the same as the one you fill in the `region` field when calling the [Create a room](https://docs.agora.io/en/whiteboard/whiteboard_room_management?platform=RESTful#create-a-room-post) API; otherwise, the service configurations do not take effect.
  ![](https://web-cdn.agora.io/docs-files/1658998783322)


4. On the **Services configuration** page, select **Enabled** for **Docs to Picture**, **Docs to web**, or **Screenshot**.
     ![](https://web-cdn.agora.io/docs-files/1637660984577)






5. Set up the storage space:
- Click the arrowhead to the right of **Storage**, and select a previously configured storage space in the drop-down list.
- Click **Create** to add a new storage space. You need to fill in the following information:
   - **Name**: (Required) The name of your storage space.
   - **Vendor**: (Required) The third-party cloud storage vendor. 
   - **Region**: (Required) The location of the data center you specified when creating a bucket.
   - **accessKey**: (Required) The Access Key provided by the third-party cloud storage vendor, which is used by the vendor to identify visitors.
   - **secretKey**: (Required) The Secret Key provided by the third-party cloud storage vendor, which is used to authenticate signatures.
   - **bucket**: (Required) The name of the bucket.
   - **Storage path**: The path used to save the resources in the storage space. The default is the root directory.
   - **Domain**: The domain name used to access the third-party cloud storage service.
 
        - To get the above information about a third-party storage service, see the documentation provided by the vendor.
        - You should enable **public access** or higher permission for third-party storage spaces so that your app clients can access files saved in the space.
 
7. Click **Save**, read the pop-up prompt carefully, and click **Confirm**.

## Reference
After enabling the whiteboard service, you can refer to the following documents to use its functions:
- [Join a Whiteboard Room for Web](https://docs.agora.io/en/whiteboard/join_whiteboard_room_web?platform=Web)
- [Join a Whiteboard Room for Android](https://docs.agora.io/en/whiteboard/join_whiteboard_room_android?platform=Android)
- [Join a Whiteboard Room for iOS](https://docs.agora.io/en/whiteboard/join_whiteboard_room_ios?platform=iOS)
- [File Conversion Overview](https://docs.agora.io/en/whiteboard/file_conversion_overview?platform=RESTful)
