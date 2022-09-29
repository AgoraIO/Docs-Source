---
title: 'File conversion overview'
sidebar_position: 7
type: docs
description: >
  Deprecated methods for converting files. 
---

Interactive Whiteboard supports file conversion from PPT and PPTX files into dynamic HTML web pages. The generated web pages can be accessed directly or presented on the whiteboard.

<div class="alert note">Agora Interactive Whiteboard released a new version of file conversion service on July 27, 2022, that greatly improves conversion speed, content parsing, and stability.  The new version also adds the ability to integrate with third-party whiteboard SDKs. Agora strongly recommends you use the new version of file conversion. See <a href="/interactive-whiteboard/reference/whiteboard-api/file-conversion">File conversion RESTful API reference</a>. </div>

## Introduction

The file-conversion feature supports the following types of file conversion:

- Static-file conversion
- Dynamic-file conversion

### Static-file conversion

Static-file conversion refers to converting PPT, PPTX, DOC, DOCX, and PDF files to static images in PNG or JPG/JPEG formats. The generated file does not preserve animations present in the source file.

When using static-file conversion, pay attention to the following issues:

-  The conversion process works best when the source file is less than 50 pages long. If the source file has more than 100 pages, you may experience a conversion timeout.  
- The higher the image resolution in the source file, the slower the conversion.
- PDF files generate the most accurate images when converted. If the generated image differs greatly from the source file in content or formatting, convert the source file to PDF and try again.
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

<div class="alert info">Although Agora Interactive Whiteboard continues to maintain the old version of file conversion, some issues could arise due to inherent limits in the architectural design.  Agora recommends you choose an appropriate time to switch to the new file conversion.  If you need support for the old version of file conversion, see the following resources: <li><a href="/interactive-whiteboard/reference/file-conversion-overview-deprecated">Old File Conversion Overview</a></li><li><a href="/interactive-whiteboard/reference/whiteboard-api/file-conversion-deprecated">Old File Conversion API Reference</a></li></div>

## Prerequisites

Before using file conversion, ensure that you have completed the following steps:

### Create a third-party cloud storage account

You need to use an Amazon S3 cloud storage service to save files generated by file conversion.

### Enable file conversion 

Refer to the following steps:

1. Go to the [Project Management](https://console.agora.io/projects) page in Agora Console, find the project that has the whiteboard feature enabled, and click **Edit**.

2. On the **Edit Project** page, find **Whiteboard**, and click **Config**.

3. Under **Services**, select a data center, and click **Config**. The data center must be the same as the one you fill in the `region` field when calling the [Create a room](/interactive-whiteboard/reference/whiteboard-api/room-management#create-a-room-post) API; otherwise, the service configurations do not take effect.
  ![](https://web-cdn.agora.io/docs-files/1658998783322)
 
4. On the **Services configuration** page, select **Enabled** for **Docs to Picture** or **Docs to web**.
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

   <div class="alert note">
   	 <ul>
    <li>To get the above information about a third-party storage service, see the documentation provided by the vendor.</li>
   	<li>You should enable <b>public access</b> or higher permission for third-party storage spaces so that your app clients can access files saved in the space.</li>
   	 </ul>
   </div>

6. Click **Save**, read the pop-up prompt carefully, and click **Confirm**.

### Upload the source file

Before you launch a file-conversion task, you must upload the source file to a third-party cloud storage space or your Nginx server. This produces a URL address for the file. Make sure that the Interactive Whiteboard can access the file via this URL address.

## Start file conversion

File conversion is implemented by Agora's server for Interactive Whiteboard service. When an app client requests to convert a file, your app server needs to call the Interactive Whiteboard RESTful API to send the request to the Agora server. The full process is illustrated in the following diagram:![](https://web-cdn.agora.io/docs-files/1618477596512)


> - To call the RESTful API to start a file-conversion task, pass in the URL address of the source file and other parameters. See [Start file conversion](/interactive-whiteboard/reference/whiteboard-api/file-conversion#start-file-conversion). 
> - To query the progress of a file-conversion task, pass in the corresponding task UUID and Task Token. See [Query file-conversion progress](/interactive-whiteboard/reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task).
> - Agora recommends that you design an algorithm to regularly query the conversion progress so that your data is up to date.
