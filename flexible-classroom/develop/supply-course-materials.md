---
title: "Upload course materials"
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

1. On your app server, poll this [RESTful API](../../interactive-whiteboard/reference/whiteboard-api/file-conversion#query-the-progress-of-a-file-conversion-task) to query the progress of a file-conversion task. According to the different types of converted resources, it can be divided into two types, static and dynamic, corresponding to static and dynamic resources, respectively. After a static resource is successfully converted, the structure needs to be converted first and then passed into the launch method.

   Query results returned by the whiteboard resource conversion service:

    ```typescript
        {
                "uuid":"xxxxxxxxxxx",
                "type":"static",
                "status":"Finished",
                "convertedPercentage":100,
                "pageCount":2,
                "images":{
                        "1":{
                                "width":1700,
                                "height":952,
                                "url":"https://convertcdn.netless.link/staticConvert/xxx/1.png"
                        },
                        "2":{
                                "width":1700,
                                "height":952,
                                "url":"https://convertcdn.netless.link/staticConvert/xxx/2.png"
                        }
                }
        }
   ```

    converts to:

    ```typescript
        courseWareList:
        [
        {
                // The file name displayed on the cloud disk
                resourceName: xxxxxxx,
                // A unique ID
                resourceUuid: xxxxxxxxx,
                // File name suffix
                ext: 'pdf',
                // The resources converted by the whiteboard can be left blank.
                url: '',
                // File size in bytes
                size: 0,
                // The last update time of the file, in milliseconds
                updateTime: xxxxxxxx,
                // Pass in the whiteboard resource conversion task ID here
                taskUuid: 'xxxxxxxxx',
                // Pass in the parameters you passed when you called the whiteboard API to initiate the whiteboard resource conversion task.
                conversion: {
                        type: 'static',
                        preview: true,
                        scale: 2,
                        outputFormat: 'png',
                },
                // Task conversion progress needs to bring in the following structural data
                taskProgress: {
                        prefix: "", // The converted resource prefix, if any, is taken from the prefix in the whiteboard conversion result.
                        // The total number of pages, take the pageCount field in the whiteboard conversion result
                        totalPageSize: 2,
                        // The total number of pages, take the pageCount field in the whiteboard conversion result
                        convertedPageSize: 2,
                        // Conversion progress, take the convertedPercentage field in the whiteboard conversion result
                        convertedPercentage: 100,
                        // Leave array empty
                        convertedFileList: [],
                        // Conversion progress, take the status field in the whiteboard conversion result
                        currentStep: 'Finished',
                        // Data structure required by static courseware
                        images: [
                                {
                                        // Key in images object
                                        name: '1',
                                        width: 1700,
                                        height: 952,
                                        url:"https://convertcdn.netless.link/staticConvert/xxx/1.png"
                                },
                                {
                                        name: '2',
                                        width: 1700,
                                        height: 952,
                                        url:"https://convertcdn.netless.link/staticConvert/xxx/2.png"
                                },
                        ]
                },
        }
        ]
    ```

    Dynamic resources do not require additional processing of images and can be passed in through the `courseWareList` method.

1. When you call [launch](../client-api/classroom-sdk#launch) on your client, pass in the list of converted files by setting the [courseWareList](../reference/classroom-sdk#configcourseware) parameter. Then students can see the courseware in the classroom.

    ```typescript
       courseWareList:
       [
       {
                // The file name displayed on the cloud disk
                resourceName: xxxxxxx,
                // A unique ID
                resourceUuid: xxxxxxxxx,
                // File name suffix
                ext: 'pptx',
                // The resources converted by the whiteboard can be left blank
                url: '',
                // File size in bytes
                size: 0,
                // The last update time of the file, in milliseconds
                updateTime: xxxxxxxx,
                // Pass in the whiteboard resource conversion task ID here
                taskUuid: 'xxxxxxxxx',
                // Here you need to pass in the parameters you passed when you called the whiteboard API to initiate the whiteboard resource conversion task.
                conversion: {
                         type: 'dynamic',
                         preview: true,
                         scale: 2,
                         outputFormat: 'png',
                },
                // Task conversion progress needs to bring in the following structural data
                taskProgress: {
                         prefix: "", // The converted resource prefix, if any, is taken from the prefix in the whiteboard conversion result
                         // The total number of pages, take the pageCount field in the whiteboard conversion result
                         totalPageSize: 2,
                         // The total number of pages, take the pageCount field in the whiteboard conversion result
                         convertedPageSize: 2,
                         // Conversion progress, take the convertedPercentage field in the whiteboard conversion result
                         convertedPercentage: 100,
                         // Leave array empty
                         convertedFileList: [],
                         // Conversion progress, take the status field in the whiteboard conversion result
                         currentStep: 'Finished',
                         // The data structure required for static courseware, and the empty array for dynamic courseware
                         images: []
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
