---
title: 'Enable Interactive Whiteboard'
sidebar_position: 1
type: docs
description: >
  Enable and configure Interactive Whiteboard
---

To use <Vg k="WHITE" />, you need to enable and configure it in <Link to="{{Global.AGORA_CONSOLE_URL}}"><Vg k="CONSOLE" /></Link>.

## Prerequisites

Before enabling the whiteboard feature, ensure that you meet the following requirements:
- A valid Agora account. If you have a Netless account, you must complete the account migration first. See [Migrate from Netless to Agora](./develop/migration-guide).
- Active Agora projects. If you have not created a project, see [Manage projects](../get-started/manage-agora-account/#create-and-manage-projects).

## Enable <Vg k="WHITE" />

Follow these steps to enable the <Vg k="WHITE" /> in <Vg k="CONSOLE" />:

1. Log in to <Link to="{{Global.AGORA_CONSOLE_URL}}"><Vg k="CONSOLE" /></Link>, and click the **Projects** in the navigation panel.

2. On the **My Projects** page, click the **Edit** ✎ icon against the project for which you want to enable <Vg k="WHITE" />.
 ![](/images/common/console-configure-project.png)

3. Under **ALL FEATURES**, select **Whiteboard**, and then toggle the **Enable Whiteboard** button.
 ![Enable Whiteboard](/images/interactive-whiteboard/console-enable-whiteboard.png)

## Get security credentials for your whiteboard project

After you enable <Vg k="WHITE" /> for your project, you can obtain the following security credentials:

- **App Identifier**: The unique App Identifier required for initializing the <Vg k="WHITE_SDK" />.
- **Access Key (AK)** and **Secret Key (SK)**: A pair of keys you use to generate whiteboard tokens. See [Generate token using an app server](../develop/generate-token-app-server).
- **SDK Token**: An SDK token is a dynamic key. You can generate an [SDK Token](../develop/authentication-workflow) here for development and testing purposes. In a production environment, you generate an SDK Token at your app server either by using the [code samples](../develop/generate-token-app-server) or calling the [RESTful API](../develop/generate-token-rest).

To get the security credentials:

1. On the **Projects** page in <Vg k="CONSOLE" />, find the project that has the whiteboard feature enabled, and click **Edit** ✎.

1. Under **ALL FEATURES**, select **Whiteboard**, and then choose **Basic information**.

    ![Security Credentials](/images/interactive-whiteboard/console-security-credentials.png)

3. **Copy** ⧉ the **App Identifier**, **Access Key (AK)**, and **Secret Key (SK)**. Save them to a secure location.

4. Click **Generate**, to generate an SDK token. Read the prompt carefully, and then click **Copy** ⧉. Save the SDK Token to a secure location.
	
<Admonition type="caution">
Exposing security credentials can lead to serious risks. To improve security, Agora recommends the following best practices:

- Avoid sending the Access Key (AK) and Secret Key (SK) to app clients or hard-coding them in the application. Ensure only the app server can read the keys from a secure configuration file.

- Since SDK tokens generated through the Agora Console have high level permissions, do not send these tokens to app clients to prevent potential security risks.
</Admonition>

## Enable whiteboard server-side features

<Vg k="WHITE" /> sets up five [data centers](../reference/security#network-geofencing). Each data center provides the following server-side features: 

- File conversion features:
    - **Docs to Picture** 
    - **Docs to web**
    
    After enabling the file conversion features, you can call the [RESTful APIs](../reference/whiteboard-api/file-conversion) to launch a file conversion task or query the conversion progress.

    Agora charges for the file-conversion feature. See [Pricing](../overview/pricing).

- **Screenshot**. After enabling, you can call the [RESTful APIs](../reference/whiteboard-api/screenshots) to take screenshots.

Follow these steps to enable one or more features and configure the storage settings:

1. On the **My Projects** page in Agora Console, find the project that has the whiteboard feature enabled, and click **Edit** ✎.

2. Under **ALL FEATURES**, select **Whiteboard > Whiteboard Services**.

3. On the **Services Configuration** view, select a data center and click **Configure** ✎. The data center must be the same as the one you fill in the `region` field when calling the [Create a room](../reference/whiteboard-api/room-management#create-a-room-post) API; otherwise, the service configurations does not take effect.

    ![](/images/interactive-whiteboard/console-services-configuration.png)

4. On the **Services configuration** page, one or more of **Docs to Picture**, **Docs to web**, or **Screenshot**.
    ![](/images/interactive-whiteboard/console-configure-service.png)

5. Set up the storage space:
    - Click the **Storage** dropdown and select a previously configured storage space in the drop-down list or click **Create** to add a new storage space. 
    
    ![](/images/interactive-whiteboard/console-storage.png)

    To add a new storage space, fill in the following information:
    - **Name**: (Required) The name of your storage space.
    - **Vendor**: (Required) The third-party cloud storage vendor. Choose from the following options:
        - `AWS`
        - `Alibaba Cloud`
        - `Google Cloud Platform`
        - `Huawei Cloud`
        
    - **Region**: (Required) The location of the data center you specified when creating a bucket.
    - **Secret Key**: (Required) The secret key provided by the third-party cloud storage vendor, which is used to authenticate signatures.
    - **Access Key**: (Required) The access key provided by the third-party cloud storage vendor, which is used by the vendor to identify visitors.
    - **Bucket**: (Required) The name of the bucket.
    - **Storage Path**: The path used to save the resources in the storage space. The default is the root directory.
    - **Domain**: The domain name used to access the third-party cloud storage service.    
        
    To get the above information for a third-party storage service, see the documentation provided by the vendor.
        
    You should enable public access or higher permission for third-party storage spaces so that your app clients can access files saved in the space.

    Click **Create** to save the storage space parameters.

6. Click **Save** to save the service configuration. Read the prompt carefully, and click **Confirm**.

## Reference
After enabling the <Vg k="WHITE" />, you can refer to the following documents to use its functions:
- [Join a whiteboard room](../get-started/get-started-sdk)
- [File conversion overview](../reference/whiteboard-api/file-conversion)
