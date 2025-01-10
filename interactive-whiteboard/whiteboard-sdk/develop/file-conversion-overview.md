---
title: 'File conversion overview'
sidebar_position: 7
type: docs
description: >
  Deprecated methods for converting files. 
---

<Vg k="WHITE" /> supports file conversion from PPT and PPTX files into dynamic HTML web pages. The generated web pages can be accessed directly or presented on the whiteboard.

<Vg k="WHITE" /> released a new version of file conversion service on July 27, 2022, that greatly improves conversion speed, content parsing, and stability.  The new version also adds the ability to integrate with third-party whiteboard SDKs. Agora strongly recommends you use the new version of file conversion. See [File conversion RESTful API reference](../../reference/whiteboard-api/file-conversion).
 
## Introduction

File conversion is implemented by Agora's server for Interactive Whiteboard service. When an app client requests to convert a file, your app server calls the Interactive Whiteboard RESTful API to send the request to the Agora server. The completes process is illustrated in the following diagram:

<details>
<summary>File conversion process</summary>

![](https://web-cdn.agora.io/docs-files/1618477596512)
</details>

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
- A generated web page can be rendered into canvas pages via Fastboard SDK, [@netless/slide](https://www.npmjs.com/package/@netless/slide), or [@netless/projector-plugin](https://github.com/netless-io/projector-plugin). The differences between these three rendering solutions are as follows: 
  - Fastboard SDK is the rendering plan designed for multi-window use-cases in Agora Interactive Whiteboard.
  - @netless/slide is a stand-alone document conversion and rendering dependency that does not include such things as whiteboards or state synchronization.  Adopting this solution requires you to write extra codes to synchronize states. It is designed for use-cases where PPT is used alone in whiteboard apps. 
  - @netless/projector-plugin is a plug-in for Whiteboard SDK that supports state synchronization, but it only works in single-window use-cases.

### Version comparison

Compared with the old version, the new file conversion adopts an engine developed by Agora and has the following advantages: 

- **Support for stand-alone access**.  The new file conversion is no longer bound to Interactive Whiteboard and can be integrated with third-party whiteboard SDKs. 
- **Faster conversion speed**.  The conversion speed of the new version is increased by 200% to 400%.
- **Stronger content parsing**.  The new file conversion supports parsing content that the old version cannot, including additional animations, filters, and other effects.  The new version can parse all normal PPTX content. 
- **Improved stability**.  The new file conversion fixes multiple issues in the old version that could cause conversion failures.  
- **New features**.  Users can now pause ongoing conversion tasks or adjust task priorities. 

The new and the old versions of file conversion are **independent of each other**: The conversion task UUID generated by the new version cannot call the old version to query the progress, while the uuid generated by the old version cannot query the progress through the new version.  If you want to query the progress of the old conversion tasks through the new version, contact <a href="mailto:support@agora.io">support@agora.io</a >. 

Although Agora Interactive Whiteboard continues to maintain the old version of file conversion, some issues could arise due to inherent limits in the architectural design.  Agora recommends you choose an appropriate time to switch to the new file conversion.  If you need support for the old version of file conversion, see the following resources: 

- [Old File Conversion Overview](../../reference/file-conversion-overview-deprecated)
- [Old File Conversion API Reference](../../reference/whiteboard-api/file-conversion-deprecated)


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

3. On the **Services Configuration** view, select a data center and click **Configure** ✎. The data center must be the same as the one you fill in the `region` field when calling the [Create a room](../../reference/whiteboard-api/room-management#create-a-room-post) API; otherwise, the service configurations does not take effect.

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

1. To start a file-conversion task, call the RESTful API and pass in the URL address of the source file along with other parameters. See [Start file conversion](../../reference/whiteboard-api/file-conversion#start-file-conversion). 

2. To query the progress of a file-conversion task, pass in the corresponding task UUID and Task Token. See [Query file-conversion progress](../../reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task). Agora recommends that you implement an algorithm to regularly query the conversion progress so that your data is up to date.


## PPT Conversion: Supported features, limitations, and troubleshooting

When converting PPT or PPTX files created in Microsoft PowerPoint into dynamic HTML web pages using [File conversion](../../reference/whiteboard-api/file-conversion), some elements—such as special effects, images, or animations—might not parse correctly. This can result in issues like missing or non-functional effects in the converted output. This section outlines the compatibility of the document conversion service with various PPT features, helping you identify and fix problematic elements in your presentations.

<Admonition type="info">
- These notes are only applicable to PPT or PPTX files made with MS PowerPoint. For PPT files made with WPS, <Vg k="COMPANY" /> does not guarantee the conversion effect.
- Some functions and effects are not mentioned in the following list. This is due to functional inconsistencies caused by different versions which require manual testing.
</Admonition>

### Supported effects

| PPT element           | Effects menu | Support effect        | Measures to take      |
|:-----------|:-------------|:------------------|:--------------------|
| Word	    | Font         | <ul><li>Font style: See the list of [Supported fonts](#supported-fonts)</li><li>Font size: All</li><li>Color and underline: All</li><li>Effect: Supports strikethrough, double strikethrough, superscript, subscript, equal-height characters</li><li>Character Spacing: All</li></ul>        | After some fonts are converted, ensure that the font is installed locally for it to be displayed correctly. |
|          | Paragraph | <ul><li>Bullet</li><li>Serial number</li><li>Text alignment: All</li><li>Indentation</li><li>Spacing</li><li>Chinese version: All</li><li>Multi-column layout</li></ul>         | - |
| Shape    | Shape Format | <ul><li>Shape Fill: All</li><li>Shape Outlines/Lines: All</li></ul>           | - |
| Sheet    | Table Design | <ul><li>Table style options: All</li><li>Table style:<ul><li>Subject: All</li><li>Shading</li><li>Frame</li><li>Fill: color fill, picture fill, texture fill, gradient fill, pattern fill</li></ul></li></ul>   | - |
|          | Table Layout | All           | - |
| Picture  | Image Format | <ul><li>Remove background</li><li>Adjustments: All</li><li>Image style:<ul><li>Style templates</li><li>Frame</li><li>Format</li><li>Effects: shadow, reflection, glow, soft edge</li></ul></li><li>Arrangement: All</li><li>Cropping</li></ul>           | - |
| Audio and Video       | Audio/Video Format | <ul><li>Cropping (progressive cropping)</li><li>Add bookmark</li></ul>        | - |
| Animation             | Animation Type | <ul><li>Page cutting animation: fade in, fade out, push in, erase, split, reveal, cut in, random lines, shapes, uncover, cover, fall, hang, curtain, peel off, dissolve, chessboard, blinds, clock, ripple, switch, rotate, library, cube, box, comb, zoom, pan, carousel</li><li>Appearance/disappearance animation: All</li><li>Word animation: All</li><li>Path Animation: All</li><li>Template Animation: All</li><li>Animation with sound</li></ul> | - |
|          | Animation Properties | <ul><li>Timing: start condition, duration, delay, repeat</li><li>Trigger: by click, by bookmark</li><li>Set text animation and combine text.</li></ul> | - |
| Other    | Other Menu | Modify PPT theme, customize theme | - |


### Unsupported effects

| PPT element      | Unsupported effects | Imperfectly supported effects | Measures to take        |
|:-----------------|:--------------------|:----------------|:------|
| Word	            | <ul><li>Font effect: All Caps, Small Caps</li><li>Shape format - Text Options: Shadow, reflection, glow, soft edges, 3D format, 3D rotation</li></ul>   | <ul><li>Text stroke: Cannot perfectly restore the effect in PPT.</li><li>Custom fonts: Some font line breaks are inconsistent with the original PPT.</li><li>Vertical text: Line spacing that is not single-spaced may be inconsistent with the original PPT, and the horizontal coordinate of the font will be offset.</li><li>WordArt: The conversion effect is not perfect.</li></ul>   | <ul><li>Avoid inserting too much text on one page.</li><li>Avoid using line breaks continuously. It is recommended to split large paragraphs into multiple text boxes.</li></ul> |
| Shape	           | Shapes with formulas do not support adding color fill animations.           | <ul><li>Shape Format - Effects: When using shadow, reflection, glow, or soft edge effects, the entire shape is displayed first, and the special effects will take effect later.</li><li>Shape Format - Shape Outline:<ul><li>When you select Dashed Line, dashed lines smaller than 1.5 pt are converted to solid lines.</li><li>Arrows may shift after conversion.</li></ul></li></ul> | Some special graphics should not exceed the graphic boundary, and the part beyond the boundary is not displayed.     |
| Sheet	           | <ul><li>Shape Format - Fill:<ul><li>Pattern Fill</li><li>The option to tile the image as a texture is not supported in image or texture fills.</li></ul></li><li>Shape Format - Effects: Shadow, reflection, glow, soft edge, 3D format, 3D rotation.</li></ul>    | - | -         |
| Picture	         | Image format-effect: 3D format, 3D rotation.     | <ul><li>Image format - Remove background: Support is not perfect, the converted image may have white edges.</li><li>Image format - Image color: Images that are recolored or use color filters may have color differences after conversion.</li><li>Image Format - Image Correction: Brightness and contrast adjustment effects are not perfectly restored.</li></ul>             | -         |
| Audio and Video	 | <ul><li>Option: Play across slides.</li><li>Style: Play in the background.</li></ul>      | - | -         |
| Animation	       | <ul><li>Page cutting animation: airplane, origami, fragments, vortex, shining, smooth.</li><li>Emphasis animation: Zoom in or zoom out (only for text, not supported)/ brush color, color stretch, color pulse, underline.</li><li>Path Animation: Rewind after playback is complete.</li></ul>  | <ul><li>Timing-delay: There may be a small error in the animation delay time.</li><li>Advanced Animation triggered by click: Click events penetrate the underlying elements.</li></ul>       | -         |
| Other	           | <ul><li>Extract annotations</li><li>The following effects are not effective in the thumbnails generated after document conversion preview:<ul><li>All gradient effects</li><li>All page switching animations</li><li>Animations that involve changes to the inside of a shape do not work, including: blinds, checkerboard, dissolve, random Lines, shapes, splits, stairs, wheels, erase, fade, float</li><li>Transparency</li><li>Recolor</li><li>Shadow, reflection, glow, soft edge</li></ul></li></ul> | The hide slide function does not support hiding the first page of the slide.          | -         |

### Best practices for troubleshooting conversion issues

If some effects are missing in the converted PPT or are different from the original PPT, refer to the following steps to locate the problematic elements and fix them:

1. Locate the problematic element

    Compare the PPT before and after conversion to find the problematic elements.

1. Deal with problematic elements

    Resolve the problem using one of the following methods:

    - Remove the problematic element directly or remove unsupported effects on the element.
    - Replace the effect that is already supported by other document transformations for the element in question.
    - Save the problematic element as a picture, delete the element, and then reinsert the picture to the original position. If there are many problematic elements, combine those elements first and convert them to pictures.

1. Restart the conversion

    Call the RESTful API again to restart the conversion. After the conversion is successful, compare the PPT effects before and after the conversion. If there are any remaining problems, repeat the previous steps.

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

### Supported fonts

<Vpd k="NAME" /> file conversion supports the following fonts:

- AaManYuShouXieTi, AaManYuShouXieTi
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi B, Alibaba PuHuiTi B
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi H, Alibaba PuHuiTi H
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi Heavy, Alibaba PuHuiTi Heavy
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi L, Alibaba PuHuiTi L
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi Light, Alibaba PuHuiTi Light
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi M, Alibaba PuHuiTi M
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi Medium, Alibaba PuHuiTi Medium
- Alibaba PuHuiTi, Alibaba PuHuiTi, Alibaba PuHuiTi R, Alibaba PuHuiTi R
- Alimama DongFangDaKai, Alimama DongFangDaKai
- Alimama FangYuanTi VF, Alimama FangYuanTi VF
- Aqua Kana,.Aqua Kana
- Cat chewing assorted black, MaokenAssortedSans
- Do Hyeon
- Dubai
- Gen Shin Gothic, Gen Shin Gothic, Gen Shin Gothic Bold
- Gen Shin Gothic, Gen Shin Gothic Regular
- Georgia Pro
- Gmarket Sans TTF, Gmarket Sans TTF Medium
- HanWang SinSongThin-Gb5, Wang Hanzong's Thin New Song Bamboo Slips, Wang Hanzong's Thin New Song Bamboo Slips
- HanWangGB06, Wang Hanzong's regular script with pen
- HappyZcool-2016, HappyZcool 2016 revised version
- HGMaruGothicMPRO
- HGMinchoE,HGMing DynastyE
- HGPMinchoE,HGP Ming Dynasty E
- HGSMinchoE,HGS Ming Dynasty E
- HuXiaoBo-NanShen, Hu Xiaobo’s male body
- JiangChengYuanTi, JiangChengYuanTi, JiangChengYuanTi 300W
- JiangChengYuanTi, JiangChengYuanTi, JiangChengYuanTi 600W
- Lato
- Lato,Lato Light
- LXGW WenKai,
- MaoKenTangYuan (beta), MaoKenTangYuan (beta)
- Merriweather
- Merriweather,Merriweather Black
- Merriweather,Merriweather Light
- MingLiU_HKSCS, MingLiU_HKSCS
- Mitr
- Mitr,Mitr ExtraLight
- Mitr,Mitr Light
- Mitr,Mitr Medium
- Mitr,Mitr SemiBold
- Mukta Mahee,Mukta Mahee Bold
- Mukta Mahee,Mukta Mahee ExtraBold
- Mukta Mahee,Mukta Mahee Light
- Mukta Mahee,Mukta Mahee Medium
- Mukta Mahee,MuktaMahee Regular
- Mukta Mahee,MuktaMahee SemiBold
- New York
- Noteworthy
- NoTo Nastaliq Urdu
- Noto Nastaliq Urdu UI
- Noto Sans Armenian
- Noto Sans Armenian,Noto Sans Armenian Blk
- Noto Sans Armenian,Noto Sans Armenian ExtBd
- Noto Sans Armenian,Noto Sans Armenian ExtLt
- Noto Sans Armenian,Noto Sans Armenian Light
- Noto Sans Armenian,Noto Sans Armenian Med
- Noto Sans Armenian,Noto Sans Armenian SemBd
- Noto Sans Armenian,Noto Sans Armenian Thin
- Noto Sans Avestan
- Noto Sans Bamum
- Noto Sans Batak
- Noto Sans Brahmi
- Noto Sans Buginese
- Noto Sans Buhid
- Noto Sans Carian
- Noto Sans Chakma
- Noto Sans Cham
- Noto Sans Coptic
- Noto Sans Cuneiform
- Noto Sans Cypriot
- Noto Sans Egyptian Hieroglyphs,Noto Sans EgyptHiero
- Noto Sans Glagolitic
- Noto Sans Gothic
- Noto Sans Hanunoo
- Noto Sans Imperial Aramaic,Noto Sans ImpAramaic
- Noto Sans Inscriptional Pahlavi,Noto Sans InsPahlav
- Noto Sans Inscriptional Parthian,Noto Sans InsParthi
- Noto Sans Javanese
- Noto Sans Kaithi
- Noto Sans Kannada
- Noto Sans Kannada,Noto Sans Kannada Black
- Noto Sans Kannada,Noto Sans Kannada ExtraBold
- Noto Sans Kannada,Noto Sans Kannada ExtraLight
- Noto Sans Kannada,Noto Sans Kannada Light
- Noto Sans Kannada,Noto Sans Kannada Medium
- Noto Sans Kannada,Noto Sans Kannada SemiBold
- Noto Sans Kannada,Noto Sans Kannada Thin
- Noto Sans Kayah Li
- Noto Sans Kharoshthi
- Noto Sans Lepcha
- Noto Sans Limbu
- Noto Sans Linear B
- Noto Sans Lisu
- Noto Sans Lycian
- Noto Sans Lydian
- Noto Sans Mandaic
- Noto Sans Meetei Mayek
- Noto Sans Mongolian
- Noto Sans Myanmar
- Noto Sans Myanmar,Noto Sans Myanmar Blk
- Noto Sans Myanmar,Noto Sans Myanmar ExtBd
- Noto Sans Myanmar,Noto Sans Myanmar ExtLt
- Noto Sans Myanmar,Noto Sans Myanmar Light
- Noto Sans Myanmar,Noto Sans Myanmar Med
- Noto Sans Myanmar,Noto Sans Myanmar SemBd
- Noto Sans Myanmar,Noto Sans Myanmar Thin
- Noto Sans New Tai Lue
- Noto Sans NKo,Noto Sans N'Ko
- Noto Sans Ogham
- Noto Sans Ol Chiki
- Noto Sans Old Italic
- Noto Sans Old Persian
- Noto Sans Old South Arabian,Noto Sans OldSouArab
- Noto Sans Old Turkish
- Noto Sans Oriya
- Noto Sans Osmanya
- Noto Sans PhagsPa
- Noto Sans Phoenician
- Noto Sans Rejang
- Noto Sans Runic
- Noto Sans Samaritan
- Noto Sans Saurashtra
- Noto Sans SC
- Noto Sans SC,Noto Sans SC Black
- Noto Sans SC,Noto Sans SC Light
- Noto Sans SC,Noto Sans SC Medium
- Noto Sans SC,Noto Sans SC Thin
- Noto Sans Shavian
- Noto Sans Sundanese
- Noto Sans Syloti Nagri
- Noto Sans Syriac
- Noto Sans Tagalog
- Noto Sans Tagbanwa
- Noto Sans Tai Le
- Noto Sans Tai Tham
- Noto Sans Tai Viet
- Noto Sans Thaana
- Noto Sans Tifinagh
- Noto Sans Ugaritic
- Noto Sans Vai
- Noto Sans Yi
- Noto Sans Zawgyi
- Noto Sans Zawgyi,Noto Sans Zawgyi Blk
- Noto Sans Zawgyi,Noto Sans Zawgyi ExtBd
- Noto Sans Zawgyi,Noto Sans Zawgyi ExtLt
- Noto Sans Zawgyi,Noto Sans Zawgyi Light
- Noto Sans Zawgyi,Noto Sans Zawgyi Med
- Noto Sans Zawgyi,Noto Sans Zawgyi SemBd
- Noto Sans Zawgyi,Noto Sans Zawgyi Thin
- Noto Serif Balinese
- Noto Serif Myanmar
- Noto Serif Myanmar,Noto Serif Myanmar Blk
- Noto Serif Myanmar,Noto Serif Myanmar ExtBd
- Noto Serif Myanmar,Noto Serif Myanmar ExtLt
- Noto Serif Myanmar,Noto Serif Myanmar Light
- Noto Serif Myanmar,Noto Serif Myanmar Med
- Noto Serif Myanmar,Noto Serif Myanmar SemBd
- Noto Serif Myanmar,Noto Serif Myanmar Thin
- Noto Serif SC
- Noto Serif SC,Noto Serif SC Black
- Noto Serif SC,Noto Serif SC ExtraLight
- Noto Serif SC,Noto Serif SC Light
- Noto Serif SC,Noto Serif SC Medium
- Noto Serif SC,Noto Serif SC SemiBold
- Open Sans
- Open Sans,Open Sans Extrabold
- Open Sans,Open Sans Light
- Open Sans,Open Sans Semibold
- Oswald
- Pangolin
- PT Mono
- PT Sans
- PT Sans Caption
- PT Serif
- Quicksand
- Quicksand, Quicksand SemiBold
- Quicksand,Quicksand Medium
- Roboto
- Roboto Condensed
- Roboto Slab
- Roboto, Roboto Black
- Roboto, Roboto Medium
- Roboto, Roboto Thin
- shetumodengxiaofangti, photo modern small cube
- Soukou Mincho, Armored Ming Dynasty
- Source Han Sans CN, Source Han Sans CN ExtraLight, Source Han Sans CN ExtraLight
- Source Han Sans CN, Source Han Sans CN Heavy, Source Han Sans CN Heavy
- Source Han Sans CN, Source Han Sans CN Light, Source Han Sans CN Light
- Source Han Sans CN, Source Han Sans CN Medium, Source Han Sans CN Medium
- Source Han Sans CN,Siyuan Bold CN,Source Han Sans CN Regular,Siyuan Bold CN Regular
- Source Han Sans CN,Source Han Sans CN Normal,Source Han Sans CN Normal
- Source Han Sans SC, Source Han Sans SC Heavy, Source Han Sans SC Heavy
- Source Han Sans SC, Source Han Sans SC Light, Source Han Sans SC Light
- Source Han Serif CN, Source Han Serif CN, Source Han Serif CN ExtraLight, Source Han Serif CN ExtraLight
- Source Han Serif CN, Source Han Serif CN, Source Han Serif CN Heavy, Source Han Serif CN Heavy
- Source Han Serif CN, Source Han Serif CN, Source Han Serif CN Light, Source Han Serif CN Light
- Source Han Serif CN, Source Han Serif CN, Source Han Serif CN SemiBold, Source Han Serif CN SemiBold
- Source Han Serif CN,Siyuan Songti CN
- Source Han Serif CN,Siyuan Songti CN,Source Han Serif CN Medium,Siyuan Songti CN Medium
- Source Han Serif K,
- Source Han Serif K, Source Han Serif K ExtraLight
- Source Han Serif K, Source Han Serif K Medium
- Source Han Serif SC
- Source Han Serif SC, Source Han Serif SC ExtraLight, Source Han Serif SC ExtraLight
- Source Han Serif SC, Source Han Serif SC Light, Source Han Serif SC Light
- Source Han Serif SC,Source Han Serif SC Heavy,Source Han Serif SC Heavy
- Source Han Serif SC,Source Han Serif SC Medium,Source Han Serif SC Medium
- Source Han Serif SC,Source Han Serif SC SemiBold,Source Han Serif SC SemiBold
- Source Han Serif TC
- Source Han Serif TC,Source Han Serif TC,Source Han Serif Heavy,Source Han Serif TC Heavy
- Source Han Serif TC,Source Han Serif TC,Source Han Serif Light,Source Han Serif TC Light
- Source Han Serif TC,Source Han Serif TC,Source Han Serif TC ExtraLight,Source Han Serif TC ExtraLight
- Source Han Serif TC,Source Han Serif TC,Source Han Serif TC Medium
- Source Han Serif TC,Source Han Serif TC,Source Han Serif TC SemiBold
- Source Han Serif,Source Han Serif Heavy,Source Han Serif Heavy
- Source Han Serif, Source Han Serif Light
- Source Han Serif, Source Han Serif Medium
- Source Sans Pro
- STIXGeneral
- STIXSizeFourSym
- STIXSizeOneSym
- STIXSizeTwoSym
- STKaiti, Chinese Kaiti
- Sukhumvit Set
- Taipei Sans TC Beta
- Taipei Sans TC Beta,Taipei Sans TC Beta Light
- Webdings
- YRDZST,Yang Rendong Bamboo Stone,YRDZST-Extralight,Yang Rendong Bamboo Stone-Extralight
- YRDZST,Yang Rendong Bamboo Stone,YRDZST-Heavy,Yang Rendong Bamboo Stone-Heavy
- YRDZST,Yang Rendong Bamboo Stone,YRDZST-Light,Yang Rendong Bamboo Stone-Light
- YRDZST,Yang Rendong Bamboo Stone,YRDZST-Medium,Yang Rendong Bamboo Stone-Medium
- YRDZST,Yang Rendong Bamboo Stone,YRDZST-Regular,Yang Rendong Bamboo Stone-Regular
- YRDZST,Yang Rendong Bamboo Stone,YRDZST-Semibold,Yang Rendong Bamboo Stone-Semibold
- Yu Gothic UI
- ZCOOL Addict Italic 01,Lucida Calligraphy
- ZCOOL Addict Italic 02,Lucida Calligraphy
- ZCOOL_KuHei, ZCOOL_KuHei
- zcool-gdh, zcool high-end black
- zcoolqingkehuangyouti, zcoolqingkehuangyouti
- ZCOOLtongtong
- zcoolwenyiti, zcoolwenyiti
- ZhenyanGB, Ruizi Zhenyan font is free for commercial use

<Admonition type="info">
Don't see your font listed? Contact [support@agora.io](mailto:support@agora.io) and provide the font file. Agora can implement a backend change to support more fonts.
</Admonition>