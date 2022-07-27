---
title: "Test Your Extension"
sidebar_position: 1
type: docs
description:
  The necessary steps you should take to test your extension.
---

export const toc = [{}];

Once you have developed your extension and API endpoints, the next step is to test whether they work properly.


## Functional and performance test

Before publishing, you have to test the functionality and performance of your extension and submit a test report to Agora.

For iOS, Android, macOS, and Windows extensions, this report must contain:
- The following proof of functionality:
  - The extension is enabled and loaded in the SDK normally.
  - All key-value pairs in the `setExtensionProperty` or `setExtensionPropertyWithVendor`  method work properly.
  - All event callbacks of your extension work properly through `IMediaExtensionObserver`.
- The following performance data:
  - The average time the extension needs to process an audio or video frame.
  - The maximum amount of memory required by the extension.
  - The maximum amount of CPU/GPU consumption required by the extension.

## Extension listing test

The [Extensions Marketplace](https://www.agora.io/en/agora-extensions-marketplace/) is where developers discover your extension. In the Marketplace, each extension has a product listing that provides detailed information such as feature overview and implementation guides. Before making your extension listing publicly accessible, the best practice is to see how everything looks and try every function in a test environment.

### Apply for testing

To apply for access to the test environment, contact Agora and provide the following:

- Your extension package
- Extension listing assets, including:
  - Your company name
  - Your public email address
  - The Provisioning API endpoints
  - The Usage and Billing API endpoints
  - Your draft business model or pricing plan
  - Your support page URL
  - Your official website URL
  - Your implementation guides URL

### Test your extension listing

Once your application is approved, Agora publishes your extension in the test environment and sends you an e-mail.

To test if everything works properly with your extension in the Marketplace, do the following:
- Activate and deactivate your extension in an Agora project, and see whether the Provisioning APIs work properly.
- Follow your implementation guides to implement your extension in an Agora project, and see whether you need to update your documentation.
- By the end of the month, check the billing information and see whether the Usage and Billing APIs work properly.

## Next steps

Now you are ready to submit your extension for final review by Agora. For details, see [Publish Your Extension](./publish_extension).