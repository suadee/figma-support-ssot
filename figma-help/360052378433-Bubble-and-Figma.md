---
기술지원명: Bubble and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Bubble and Figma
출처링크: https://help.figma.com/hc/en-us/articles/360052378433-Bubble-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

 

Users on [any Figma team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

This feature is available to all Bubble users and creating an account is free at [bubble.io](https://bubble.io/home)

[Bubble](https://bubble.io/) lets you create interactive, multi-user apps for desktop and mobile web browsers, without having to write a single line of code.

Turn your designs into working prototypes and full-fledged applications. Import your Figma frames into Bubble, then add logic, workflows, and database capabilities to your designs. No coding required.

Bubble's Figma integration will:

- Import Figma frames as new pages of your app in Bubble
- Upload images from your Figma file to your app in Bubble
- Label the newly created Bubble elements with the same names as your Figma file

This feature is available to all Bubble users and creating an account is free at [bubble.io](http://bubble.io/)

Tip! For more information about how the import works, known limitations, and tips for setting up your Figma file for best results with this import, visit the [Bubble Manual](https://manual.bubble.io/help-guides/building-a-user-interface/importing-from-figma).

# Connect Bubble to Figma

The import tool exists in the Bubble editor and will ask for your Figma API Key. This is so Bubble can access the Figma file you specify and see all its contents. This integration can only access the specific files you tell it to, and will not make any changes to those files in Figma.

## In Figma

To import a Figma file to Bubble, you'll need:

- Your account's Figma API Key
- The ID of the file you want to import

To add a Figma API key in Bubble, you will need to generate a **Personal Access Token** in Figma.

1. Go to the [File Browser](https://www.figma.com/files/).
2. Click your name at the top left and go to the **Settings** tab.
3. Under **Personal Access Tokens**, click **Create a new personal access token**.
4. Copy this token. This is your Figma API key.

Each Figma file has a unique URL containing its ID. The file ID is the string of random alphanumeric characters found in the section of the URL after `figma.com/file/`.

![View of a browser address bar with a Figma file's URL highlighted at the ID](https://help.figma.com/hc/article_attachments/360082234774)

To find and copy the ID of the Figma file you want to import:

1. Open the Figma file you want to import.
2. Copy the file's ID from your browser's address bar. If you're in the Figma Desktop App, right-click the file's tab to **Copy link** and paste it in a browser's address bar to view and copy the file ID.

## In Bubble

1. Navigate to your app in Bubble.
2. Click **Settings** from the left side panel.
3. In the **General** tab, scroll down to the **Design import** section.
4. Enter your Figma API key and the file ID.
5. Click **Import**. The import can take a few moments depending on the size of your Figma file.
