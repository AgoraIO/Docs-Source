---
title: "Implementation guides"
sidebar_position: 1
type: docs
description: > 
   Write the guide used by developers to incorporate your extension into their app. 
---

export const toc = [{}];

Implementation guides are the documentation you provide to guide users through the implementation of your extension in Agora projects. In the [Extensions Marketplace](https://www.agora.io/en/agora-extensions-marketplace/), your extension has a detail page that contains a link to your implementation guides. The link leads users to the latest version of your documentation.

Your implementation guides must contain the following:

- Quickstart: A step-by-step procedure that explains how to integrate and use your extension in an Agora project.
- API reference: A detailed description of the APIs that users use to customize your extension.

To build your extension documentation, you do not have to start from scratch. This page shows how to use the template provided by Agora to write, output HTML for local testing using [Sphinx](https://www.sphinx-doc.org/en/master/), and host your documentation on a web server using [Read the Docs](https://docs.readthedocs.io/en/stable/index.html).

## Prerequisites

To follow the procedure on this page, you must have:

- Python 3.7 or later, with `pip` installed.
- A code editing tool, such as Visual Studio Code.
- A GitHub, BitBucket, or GitLab account, which is used to create a public repository to host your documentation.

## Use the template to write

To use the template to write your documentation, take the following steps:
1. Unzip the [extension documentation template](https://web-cdn.agora.io/docs-files/1631696989677) to a local folder.
2. In your code editing tool, open the `_content` folder and edit the following files:
   - `quickstart.md`: Explain how to integrate the features of your extension step by step. Use the template instructions as a reference.
   - `api-reference.md`: Provide detailed description of the APIs related to using your extension. Use the template instructions as a reference.
   - `index.md`: Provide your documentation repository URL and write a welcome page.

## Output HTML for local testing

Before making your documentation publicly accessible, the best practice is to view and test it locally. This section describes how to generate an HTML output for your documentation using configurations in the template.

### Set up the build environment

The template is configured to generate styled HTML from source files written in Markdown. To generate HTML output that is customized for your extension, take the following steps:

1. In `_content/conf.py`, make the following changes: 
   - Fill in the `project`,` copyright`, `author, and github_doc_root `fields to add your project information.
   - Replace `html_logo` and `html_favicon` with your logo and icon. You can either put the source image in the `_static` folder or insert the URL to the image.
   - Change `html_title` to the title of your documentation.

2. In Terminal, run the following command line to install Sphinx:
   ```
	 pip install sphinx
	```

3. In Terminal, run the following command line to install the packages for Markdown support:
   ```
	 pip install myst-parser
	```
	
4. In Terminal, run the following command line to install the HTML theme:
   ```
	 pip install furo
	```

### Output HTML locally

To generate an HTML output for local testing, take the following steps:

1. In Terminal, change the directory to the `_content` folder and run the following command line:
   ```
	 make html
	```
   If everything goes well, you see something like this:

   `build succeeded, 1 warning.`

2. In your browser, open `_content/__build/html/index.html` to see the welcome page of your documentation. In the left navigation panel, click **Quickstart** or **API Reference** to review your work.

3. To change the content on the HTML pages, edit the corresponding source file and save your edits. Then run `make html` again to review your change.

4. Repeat the previous step until you think your HTML pages are ready to be published.

## Publish your documentation

To make your documentation publicly accessible through a URL, take the following steps:

1. Create a public repository for your documentation folder (`extension-doc-template` if you have not renamed it).
2. [Import and build your documentation](https://docs.readthedocs.io/en/stable/intro/import-guide.html) using Read the Docs, which assigns a URL for your documentation.
3. If you need to update your documentation, edit the source files and push the commit to your repository. The update is automatically published in your documentation.

To ensure that users always get up-to-date content about your extension, provide your documentation URL to Agora before officially publishing your extension in the Gallery. For details, see [Publish Your Extension](./publish_extension).