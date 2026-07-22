---
기술지원명: Upload a web font to Figma Make
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Upload a web font to Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/38694569552151-Upload-a-web-font-to-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

If your Figma Make file uses a custom font, you’ll need to upload the corresponding web font file before publishing so it displays correctly in your live app.

Custom fonts are fonts [installed on your computer](https://help.figma.com/hc/en-us/articles/360039956894), or [shared by your organization](https://help.figma.com/hc/en-us/articles/360039956774-Upload-custom-fonts-to-an-organization) that aren’t included as standard system or Google fonts. Browsers require the web font file to render the font correctly in your published app.

Custom fonts may be added to your Figma Make file in several ways, including:

- [Using a design library as style context](https://help.figma.com/hc/en-us/articles/33024539096471)
- [Starting from a template](https://help.figma.com/hc/en-us/articles/34716178062871)
- [Pasting a design into Make](https://help.figma.com/hc/en-us/articles/31304529835671)
- Selecting [a font you added to Figma](https://help.figma.com/hc/en-us/articles/360039956894)—or one [shared by your organization](https://help.figma.com/hc/en-us/articles/360039956774-Upload-custom-fonts-to-an-organization)—in the [point and edit tool](https://help.figma.com/hc/en-us/articles/31304485164695)

If your file includes custom fonts that require web font files, you'll see a **Missing fonts** warning under **Typography** when you try to publish.

To publish your site with a custom font, upload the corresponding `.woff` or `.woff2` file so it displays correctly for visitors.

**Tip**: WOFF (Web Open Font Format) files are supported by all major browsers and are usually much smaller than desktop TTF or OTF files. Using WOFF or WOFF2 helps your app load faster and perform better.

## Upload a missing web font to Figma Make

![](https://help.figma.com/hc/article_attachments/38771336160663)

To check for missing fonts in your Figma Make file, click **Publish** at the top of the screen. If any fonts require web font files, you'll see a warning under **Typography** in the **Publish** modal.

You can publish without resolving this warning, but any missing fonts will fall back to the browser's default font on the live site.

To upload a missing web font:

1. In your Figma Make file, click **Settings** at the top of the screen.
2. Click **Fonts**.
3. Click **Upload** to add the `.woff` or `.woff2` file for each font listed.

After uploading, click **Publish** to publish or republish your app with the new fonts included.

## Remove a custom font

To remove a custom font, first update any text that uses it. Then delete the uploaded font file and republish your app.

### 1. Update text that uses the font

Use a prompt to ask Figma Make to remove all references to the font, or switch to  **Code** view and delete the references manually.

### 2. Delete the font file

1. In your Figma Make file, click **Settings** at the top of the screen.
2. Click  **Fonts**.
3. Click  **Delete font** next to the font you want to remove.

### 3. Republish your app

1. Click **Publish** in the preview.
2. Review the details in the modal, then click **Publish**.

**Note**: If you delete the font file without updating the text layers that use it, your published app's CSS will still reference the missing font. The browser won't be able to find it and will fall back to its default font.

## Frequently asked questions

**Why is the custom font showing on the canvas but not on the published app?**

The Figma Make editor renders fonts using files installed on your computer or shared with your organization. Browsers, however, need the web font files to correctly display the app to users.

To display a custom font on your published app, you must upload the corresponding web font file. Without it, the browser will fall back to its default font.
