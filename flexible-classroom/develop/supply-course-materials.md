---
title: "Supply course materials"
sidebar_position: 6
type: docs
description: >
    Supply learning materials for a course. 
---


In many online teaching scenarios, teachers use a variety of interactive courseware to deliver an informative learning experience. Flexible Classroom enables teachers to display such courseware during classes. The supported formats are PPT, PPTX, DOC, DOCX, PDF, MP3, MP4, PNG, JPG, and GIF. 

Courseware in flexible classrooms can be divided into two categories:

- Public resources: Uploaded and maintained by educational agencies; teachers cannot edit the courseware.
- Personal resources: Uploaded and maintained by teachers on the client end.

To display courseware on the whiteboard in flexible classrooms, you must convert the courseware to a format supported by the Agora Interactive Whiteboard service. For security reasons, Flexible Classroom does not store your courseware; all courseware must be stored either in a third-party cloud storage account that you provide or on your own server.

## Upload courseware before a class

If you want to upload the courseware to third-party cloud storage or to your own server before a class and then display the courseware in Flexible Classroom, perform the following steps:

1. In Agora Console, [enable and configure the Whiteboard](../../interactive-whiteboard/develop/enable-whiteboard) feature to store the courseware used in Flexible Classroom.

1. In Agora Console, enable the file-conversion feature of the Whiteboard service, and add a storage configuration for storing the converted courseware. For details, see [How to enable the file-conversion feature](../../interactive-whiteboard/develop/file-conversion-overview).

1. On your app server, call this [RESTful API](../../interactive-whiteboard/reference/whiteboard-api/file-conversion#start-file-conversion) to start a file-conversion task. The Agora Interactive Whiteboard service uploads the converted files to the third-party cloud storage that you have configured in Agora Console.

1. On your app server, poll this [RESTful API](../../interactive-whiteboard/reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task) to query the progress of a file-conversion task. Pay special attention to the `convertedFileList` parameter in the response. This parameter contains an array of converted files. Each `convertedFileList` object contains the following parameters:

   - `width`: Number. Indicates the width of the image in pixels.
   - `height`: Number. Indicates the height of the image in pixels.
   - `conversionFileUrl`: String. Indicates the URL of the generated image.
   - `preview`: String. Indicates the address of the preview. This field is returned only when `preview` is set as `true` and `type` is set as `dynamic` in the request body when starting file conversion.

1. When you call [launch](../reference/classroom-sdk#launch) on your client, pass in the list of converted files by setting the [courseWareList](../reference/classroom-sdk#configcourseware) parameter. Then students can see the courseware in the classroom.

   ```json
   courseWareList:
   [
      {
      resourceName: xxxxxxx,
      resourceUuid: xxxxxxxxx,
      ext: 'pptx',
      url: 'https://xxxxxxxxxxxxxx',
      size: 0,
      updateTime: xxxxxxxx
      taskUuid: 'xxxxxxxxx',
      conversion: {
                  type: 'dynamic',
                  preview: true,
                  scale: 2,
                  outputFormat: 'png',
                  },
      taskProgress: {
         totalPageSize: 3,
         convertedPageSize: 3,
         convertedPercentage: 100,
         convertedFileList: [
                  {
                  name: '1',
                  ppt: {
                        src: 'pptx://convertcdn.netless.link/dynamicConvert/3bxxxxxxx/1.slide',
                        width: 1280,
                        height: 720,
                        preview:'dddddddddddddddurl'
                     },
                  },
                  ...
         ] as any,
         currentStep: '',
         },
      },
   ],
   ```

## Upload courseware during a class

To upload courseware during a class, perform the following steps:

1. Log in to Flexible Classroom, and enter the desired classroom.

1. Click **Cloud Drive** in the tool bar, and then click **Upload** as shown in the following screenshot:

   ![](https://web-cdn.agora.io/docs-files/1663562311451)

   You can delete your personal resources by selecting the option icon and clicking **Delete**, as shown in the following screenshot:

   ![](https://web-cdn.agora.io/docs-files/1663562326661)

## Cloud storage configuration

To ensure that Flexible Classroom can access your cloud storage, configure your cloud storage account as follows:

* Alibaba Cloud OSS account

   * Ensure that read and write permissions are set to public read.

   * Cross domain rule configuration
      * Configure Source and Allow Headers according to your actual situation.
      * Exposure Headers must be filled in according to the figure below:

     ![alibaba-cloud-storage-config](/images/flexible-classroom/alibaba-cloud-storage-config.png)

* AWS S3 accounts

   * Bucket policy

      ```json
      {
      "Version": "2012-10-17",
      "Id": "Policy1622700880591",
      "Statement": [
            {
               "Sid": "Stmt1622700872941",
               "Effect": "Allow",
               "Principal": "*",
               "Action": "s3:GetObject",
               "Resource": "arn:aws-cn:s3:::agora-adc-artifacts/*"
            }
      ]
      }
      ```

   * Cross-origin resource sharing

      ```json
      [
      {
            "AllowedHeaders": [
               "*"
            ],
            "AllowedMethods": [
               "PUT",
               "GET"
            ],
            "AllowedOrigins": [
               "*"
            ],
            "ExposeHeaders": []
      }
      ]
      ```
