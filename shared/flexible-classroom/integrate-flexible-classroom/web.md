---
title: "Integrate Flexible Classroom into Your App"
weight: 7
type: docs
description: 

---

This page introduces how to add Flexible Classroom into your Web or Electron project.

## Integration methods

Choose any of the following integration methods according to your needs.

<a name="default_ui"></a>

### Use the default UI of Flexible Classroom

If you use the default UI of Flexible Classroom, choose one of the following methods to integrate the whole Flexible Classroom into your project:

- Integrate Flexible Classroom through [npm](:https://www.npmjs.com/package/agora-classroom-sdk):

   1. Run the following command to install the SDK:

      ```
      npm install agora-classroom-sdk
      ```

   2. To import the `AgoraEduSDK` module, add the following code in the Javascript code in your project.

      ```
      import {AgoraEduSDK} from 'agora-classroom-sdk'
      ```

- Integrate Flexible Classroom through CDN. Add the following code to the HTML file in your project.

   ```html
   <script src="https://download.agora.io/edu-apaas/release/edu_sdk@2.1.2.bundle.js"></script>
   ```

<a name="change_default_ui"></a>

### Customize the default UI of Flexible Classroom

If you want to customize the default UI of Flexible Classroom, integrate Flexible Classroom as follows:

1. To clone CloudClass-Desktop and check out the latest release branch, run the following command:

   ```
   git clone https://github.com/AgoraIO-Community/CloudClass-Desktop.git
   ```

   ```
   git checkout release/apaas/x.y.z
   ```

   <div class="alert info">Replace x.y.z with the version number. To get the latest version number, see the <a href="/en/agora-class/release_agora_class_web?platform=Web">release notes</a>.</div>

2. After pulling the code, you can modify the classroom UI according to your needs, and debug it with the following commands:

   - For a Web project: `yarn dev`
   - For an Electron project: `yarn dev:electron`

3. After completing the development, pack the SDK or application with the following commands:

   - Pack the Classroom SDK: `yarn pack:classroom:sdk`
   - Pack the Mac client: `yarn pack:electron:mac`
   - Pack the Windows client: `yarn pack:electron:win`