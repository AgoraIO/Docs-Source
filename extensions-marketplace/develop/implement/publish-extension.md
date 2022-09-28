---
title: "Publish your extension"
sidebar_position: 8
type: docs
description:
  Publish your extension in the Marketplace.
---

export const toc = [{}];

Your extension is distributed to app developers through the [Extensions Marketplace](https://www.agora.io/en/agora-extensions-marketplace/).

## Prerequisites

Before publishing your extension, ensure that you have tested your extension following the procedure in [Test Your Extension](./test_extension).

## Apply for Agora review

To apply for final review by Agora, contact Agora and provide the following:

### Extension

Make sure your extension is delivered in the correct format:

- Android: `.aar` or `.so`
- iOS/macOS: `.framework` or `.xcframework`
- Windows: `.dll`
- Web: npm link

### Provisioning, Usage, and Billing API endpoints

Include these endpoints in a markdown file.

### Extension listing assets

You need to provide the following assets for your extension listing. If you have provided some of them when testing the extension, ensure that what you provide at this stage is the final version.

|      | Content                     | Requirements                                                 |
| :--- | :-------------------------- | :----------------------------------------------------------- |
| 1    | Extension name              | A name that reflects the core functionality of your extension. |
| 2    | Extension short description | A short summary of what your extension can do. Use no more than 160 characters. |
| 3    | Extension logo              | A 600 x 315 JPG file                                         |
| 4    | Extension category          | Currently must be one of the following: <li>Audio and video modifiers: Extensions that modify the audio or video source.</li><li>Tools: Extensions that provide other stand-alone functions.</li> |
| 5    | Vendor name                 | Your company's real name.  |
| 6    | Vendor description          | A brief introduction about your company. Use no more than 300 words |
| 7    | Vendor logo                 | A 600 x 315 JPG file                                         |
| 8    | Vendor website URL          | Must be accessible                                           |
| 9    | Vendor support URL          | Must link to a page providing your company's contact information |
| 10   | Implementation guides     | Must include quickstart guides and API reference. You need to provide the URL to the documentation. See [Implementation guides](./implementation-guide) for details. |

### Supplementary information

Supplementary information includes but is not limited to:

- Pricing plans: Make sure this is the pricing plan both you and Agora agree to. Include it in a markdown file.
- Extension Privacy Policy and EULA: Include it in a markdown file.

## Make your extension public

Once you submit the application for final review, Agora starts testing your extension. If your extension passes the review, Agora updates your extension listing, and sends you an email to confirm when you would like to make your extension public in the Extensions Marketplace.

