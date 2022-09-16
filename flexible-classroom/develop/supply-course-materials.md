---
title: "Supply course materials"
sidebar_position: 6
type: docs
description: >
    Supply learning materials for a course. 
---


In many virtual teaching scenes, teachers use multi-interactive teaching courseware, including PPT, PPTX, Word, and PDF, to bring an informative teaching experience.

Flexible Classroom provides such an ability to teachers, enabling them to display courseware during classes. Courseware in flexible classrooms can be divided into the following two categories:

- Public courseware of a classroom. All users in the classroom can see the public courseware. For this kind of courseware, you need to maintain the mapping relationship between classrooms and courseware.
- Personal courseware of a teacher. All users in the classroom that the teacher joins can see the teacher's personal courseware. For this kind of courseware, you need to maintain the mapping relationship between teachers and courseware.

To display courseware on the whiteboard in flexible classrooms, you must convert courseware to a format supported by the Agora Interactive Whiteboard service. For security reasons, Flexible Classroom does not store your courseware. All courseware is stored in a third-party cloud storage account that you provide.

## Upload courseware before a class

If you want to upload the courseware to third-party cloud storage or to your own server before a class and then display the courseware in Flexible Classroom, do the following steps:

1. Upload the courseware to third-party cloud storage or your own server and generate a URL address. You need to ensure that the Agora Interactive Whiteboard service can access the courseware through this URL address.
2. In Agora Console, enable the file-conversion feature of the Agora Interactive Whiteboard service and add a storage configuration for storing the converted courseware. For details, see [How to enable the file-conversion feature](/en/whiteboard/file_conversion_overview?platform=Web#enable-the-file-conversion-feature).
3. On your app server, call this [RESTful API](/en/whiteboard/whiteboard_file_conversion?platform=RESTful#start-file-conversion-post) to start a file-conversion task. The Agora Interactive Whiteboard service uploads the converted files to the third-party cloud storage that you have configured in Agora Console.
4. On your app server, poll this [RESTful API]( /en/whiteboard/whiteboard_file_conversion?platform=RESTful#query-file-conversion-progress-get) to query the progress of a file-conversion task. Pay special attention to the `convertedFileList` parameter in the response. This parameter contains an array of converted files. Each `convertedFileList` object contains the following parameters:
   - `width`: Number. Indicates the width of the image in pixels.
   - `height`: Number. Indicates the height of the image in pixels.
   - `conversionFileUrl`: String. Indicates the URL of the generated image.
   - `preview`: String. Indicates the address of the preview. This field is returned only when `preview` is set to `true` and `type` is set to `dynamic` in the request body when starting file conversion.
5. When you call [launch](/en/agora-class/agora_class_api_ref_web?platform=Web#launch) on your client, pass in the list of converted files by setting the [courseWareList](/en/agora-class/agora_class_api_ref_web?platform=Web#coursewarelist) parameter. Then students can see the courseware in the classroom.

## Upload courseware during a class

To upload courseware during a class, do the following steps:

1. In Agora Console, configure a third-party cloud storage service for storing files uploaded in a classroom. For details, see [how to configure the whiteboard feature](/en/agora-class/agora_class_configure?platform=RESTful#configure-the-whiteboard-feature).
2. In Agora Console, enable the file-conversion feature of the Agora Interactive Whiteboard service and add a storage configuration for storing the converted files. For details, see [configure the whiteboard feature](/en/agora-class/agora_class_configure?platform=RESTful#configure-the-whiteboard-feature).

## Considerations

To ensure that Agora can access files save in your third-party storage space, you should enable public access or higher permission for third-party storage spaces. Taking AWS S3 as an example:

- Bucket policy
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
- Cross-origin resource sharing
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