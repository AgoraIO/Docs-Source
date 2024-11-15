---
title: 'File conversion overview'
sidebar_position: 7
type: docs
description: >
  Deprecated methods for converting files. 
---

<Vg k="WHITE" /> supports file conversion from PPT and PPTX files into dynamic HTML web pages. The generated web pages can be accessed directly or presented on the whiteboard.

<Vg k="WHITE" /> released a new version of file conversion service on July 27, 2022, that greatly improves conversion speed, content parsing, and stability.  The new version also adds the ability to integrate with third-party whiteboard SDKs. Agora strongly recommends you use the new version of file conversion. See [File conversion RESTful API reference](../reference/whiteboard-api/file-conversion).
 
## Introduction

File conversion is implemented by Agora's server for Interactive Whiteboard service. When an app client requests to convert a file, your app server calls the Interactive Whiteboard RESTful API to send the request to the Agora server. The completes process is illustrated in the following diagram:

![](https://web-cdn.agora.io/docs-files/1618477596512)

The file-conversion feature supports the following types of file conversion:

- Static-file conversion
- Dynamic-file conversion

### Static-file conversion

Static-file conversion refers to converting PPT, PPTX, DOC, DOCX, and PDF files to static images in PNG or JPG/JPEG formats. The generated file does not preserve animations present in the source file.

When using static-file conversion, pay attention to the following issues:

-  The conversion process works best when the source file is less than 50 pages long. If the source file has more than 100 pages, you may experience a conversion timeout.  
- The higher the image resolution in the source file, the slower the conversion.
- PDF files generate the most accurate images when converted. If the generated image differs greatly from the source file in content or formatting, convert the source file to PDF and try again.
- Only valid PDF files are supported, that is, files that conform to PDF standards and have a valid header starting with `%PDF`.
- Note that because this feature is implemented with support from [Aspose](https://www.aspose.app/), Agora might not be able to respond to requests for customization as quickly as usual.  Agora recommends that you run sufficient tests of the file-conversion feature. If the test result do not meet your expectations, consider using a third-party service.
- The new file conversion currently does not support generating resource packages. However, because the resources path is fixed, users can download resources by themselves. 

### Dynamic-file conversion

Dynamic-file conversion refers to converting PPT/PPTX files edited with Microsoft Office to HTML web pages. The generated file preserves animations present in the source file. 

When using dynamic-file conversion, pay attention to the following issues:

- Converting WPS files is not yet supported.  You might also encounter problems when using PPTX files converted from WPS files.
- The new file conversion currently does not support generating resource packages. However, because the resources path is fixed, users can download resources by themselves. 
- If a font is missing in a generated web page, you can either use the SDK to add a custom font or contact support@agora.io.
- Due to inherent constrains in the PPT file format, PPT files are converted into PPTX files at the backend before parsing, which might encounter failure. Therefore, Agora recommends you to upload PPTX files for conversion. 
- A generated web page can be rendered into canvas pages via Fastboard SDK (coming soon), [@netless/slide](https://www.npmjs.com/package/@netless/slide), or [@netless/projector-plugin](https://github.com/netless-io/projector-plugin). The differences between these three rendering solutions are as follows: 
  - Fastboard SDK is the rendering plan designed for multi-window scenarios in Agora Interactive Whiteboard. Fastboard SDK is coming soon. 
  - @netless/slide is a stand-alone document conversion and rendering dependency that does not include such things as whiteboards or state synchronization.  Adopting this solution requires you to write extra codes to synchronize states. It is designed for scenarios where PPT is used alone in whiteboard apps. 
  - @netless/projector-plugin is a plug-in for Whiteboard SDK that supports state synchronization, but it only works in single-window scenarios.

### Version comparison

Compared with the old version, the new file conversion adopts an engine developed by Agora and has the following advantages: 

- **Support for stand-alone access**.  The new file conversion is no longer bound to Interactive Whiteboard and can be integrated with third-party whiteboard SDKs. 
- **Faster conversion speed**.  The conversion speed of the new version is increased by 200% to 400%.
- **Stronger content parsing**.  The new file conversion supports parsing content that the old version cannot, including additional animations, filters, and other effects.  The new version can parse all normal PPTX content. 
- **Improved stability**.  The new file conversion fixes multiple issues in the old version that could cause conversion failures.  
- **New features**.  Users can now pause ongoing conversion tasks or adjust task priorities. 

The new and the old versions of file conversion are **independent of each other**: The conversion task UUID generated by the new version cannot call the old version to query the progress, while the uuid generated by the old version cannot query the progress through the new version.  If you want to query the progress of the old conversion tasks through the new version, contact <a href="mailto:support@agora.io">support@agora.io</a >. 

Although Agora Interactive Whiteboard continues to maintain the old version of file conversion, some issues could arise due to inherent limits in the architectural design.  Agora recommends you choose an appropriate time to switch to the new file conversion.  If you need support for the old version of file conversion, see the following resources: 

- [Old File Conversion Overview](../reference/file-conversion-overview-deprecated)
- [Old File Conversion API Reference](../reference/whiteboard-api/file-conversion-deprecated)


## Prerequisites

Before using file conversion, ensure that you have completed the following steps:

### Create a third-party cloud storage account

To save files generated by file conversion, you need an account on a third-party cloud storage service such as Amazon S3, Google Cloud platform, or Alibaba.

### Upload the source file

Before you launch a file-conversion task, you must upload the source file to a third-party cloud storage space or your Nginx server. This produces a URL address for the file. Make sure that the Interactive Whiteboard can access the file via this URL address.

### Enable file conversion 

Refer to the following steps:

1. On the **My Projects** page in Agora Console, find the project that has the whiteboard feature enabled, and click **Edit** ✎.

2. Under **ALL FEATURES**, select **Whiteboard > Whiteboard Services**.

3. On the **Services Configuration** view, select a data center and click **Configure** ✎. The data center must be the same as the one you fill in the `region` field when calling the [Create a room](../reference/whiteboard-api/room-management#create-a-room-post) API; otherwise, the service configurations does not take effect.

    ![](/images/interactive-whiteboard/console-services-configuration.png)

4. On the **Services configuration** page, , select **Enabled** for **Docs to Picture** or **Docs to web** to see **Storage** settings.
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

        If your vendor is `Google Cloud Platform`, refer to [Google Cloud Storage configuration](#google-cloud-storage-configuration). If you chose `AWS`, or `Alibaba Cloud`, fill in the following information:

    - **Region**: (Required) The location of the data center you specified when creating a bucket.
    - **Secret Key**: (Required) The secret key provided by the third-party cloud storage vendor, which is used to authenticate signatures.
    - **Access Key**: (Required) The access key provided by the third-party cloud storage vendor, which is used by the vendor to identify visitors.
    - **Bucket**: (Required) The name of the bucket.
    - **Storage Path**: The path used to save the resources in the storage space. The default is the root directory.
    - **Domain**: The domain name used to access the third-party cloud storage service.  

    To configure storage parameters for GCP, see [Google Cloud Storage configuration](#google-cloud-storage-configuration). To get configuration information for other third-party storage services, see the documentation provided by the vendor. 
        
    You should enable <b>public access</b> or higher permission for third-party storage spaces so that your app clients can access files saved in the space.

    Click **Create** to save the storage space parameters.

6. Click **Save** to save the service configuration. Read the prompt carefully, and click **Confirm**.


## Start file conversion

Take the following steps:

1. To start a file-conversion task, call the RESTful API and pass in the URL address of the source file along with other parameters. See [Start file conversion](../reference/whiteboard-api/file-conversion#start-file-conversion). 

2. To query the progress of a file-conversion task, pass in the corresponding task UUID and Task Token. See [Query file-conversion progress](../reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task). Agora recommends that you implement an algorithm to regularly query the conversion progress so that your data is up to date.

## Reference

This section contains information that completes the information on this page, or points you to documentation that explains other aspects of this product.

### Google Cloud Storage configuration

To set up cloud storage and obtain configuration information for Google Cloud Platform, take the following steps:

1. Create an account on [Google Cloud](https://cloud.google.com/) and assign permissions on the settings page of Google Cloud storage. 
    ![](/images/interactive-whiteboard/gcp-settings.png)

1. After creation, click on the ![](/images/interactive-whiteboard/ellipses.png) button in the upper right corner and select **Project settings**.

1. Under **IAM and Admin**, select **Service Accounts**. In the service account list, click on the ![](/images/interactive-whiteboard/ellipses.png) button for the account just added, and select **Manage keys**.

1. Click **ADD KEY** > **Create new key**. Select **JSON** in the pop-up box and click **CREATE**. A `json` file is downloaded with the name format `projectId-xxxxxxxx.json`. 
    ![](/images/interactive-whiteboard/gcp-create-private-key.png)    

1. Open the downloaded json file, which looks like the following example:

    ```json
    {
    "type": "service_account",
    "project_id": "argon-jetty-395210",
    "private_key_id": "yourprivateidkeyyourprivateidkeyyourprivateidkey",
    "private_key": "-----BEGIN PRIVATE KEY-----\nThisisYourPrivateKeyThisisYourPrivateKeyThisisYourPrivateKey\nThisisYourPrivateKey\nThisisYourPrivateKey\nThisisYourPrivateKey\n-----END PRIVATE KEY-----\n",
    "client_email": "xxxx-111@argon-jetty-395210.iam.gserviceaccount.com",
    "client_id": "123456789012345678901",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xxxx-111%40argon-jetty-395210.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
    }
    ```

1. Use the information in the json file to fill-in the Google Cloud Storage configuration:

    The `project_id` in the json file corresponds to the `projectId` on <Vg k="CONSOLE" />, `client_email` corresponds to `clientEmail`, `private_key` corresponds to `privateKey`, and `bucket` is filled with the name of the `bucket` to be used. The remaining parameters have the same meaning as for the AWS configuration.
    When copying the `private_key`, make sure that your text editor has not added any extra line breaks or `\n` after each `\n`.

1. Ensure that the newly created service account has writable permission for the Google storage bucket.
