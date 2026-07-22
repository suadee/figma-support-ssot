---
기술지원명: Add a font to Figma
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Add a font to Figma
출처링크: https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

By default, Figma includes [Google fonts](https://fonts.google.com/) and [Apple fonts](https://developer.apple.com/fonts/) in files. You can access additional fonts by installing them on your computer.

![Flowchart illustrating steps to use custom fonts in Figma: download, install to font manager, install font helper, and use in Figma.](https://help.figma.com/hc/article_attachments/19825105682327)

## 1. Download and install the font files

Figma supports .TTF and .OTF font files. Downloaded fonts often come compressed in .zip folders. In one .zip folder, you might find several variations on the same font, such as "regular" or "heavy".

The process to install a font varies depending on your computer:

- **Mac**: On Mac, installed fonts are added to the Font Book. For instructions on installing fonts, visit the [Install and validate fonts in Font Book on Mac](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) article on Apple’s Help Center.
- **Windows**: On Windows, installed fonts are added to the Fonts folder. For instructions on installing fonts, visit the [Add a font](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1) article on Microsoft’s Help Center.

**Note**: Figma does not support additional fonts for computers running ChromeOS or Linux. Chromebook and Linux users can only use Google fonts and available Apple fonts (SF Pro and SF Compact), which are available by default in Figma.

## 2. Install the Figma font installer (web browser users only)

If you access Figma via your web browser, you must install the Figma font installer, also known as the FigmaAgent, before you can access additional fonts in Figma.

If you’re using the Figma desktop app, you can skip this step. The desktop app includes the Figma font installer.

[Download the Figma font installer](https://www.figma.com/downloads/)

**Note**: The Figma font installer, FigmaAgent, has no interface to open. It runs silently in the background, automatically detecting fonts already installed on your computer and making them available in Figma.

Behind the scenes, FigmaAgent runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

You can [uninstall the Figma font installer](https://help.figma.com/hc/en-us/articles/19764441960599) at any time, but doing so will remove access to your local and Adobe fonts in Figma.

## 3. Use your font in a design file

After installing the Figma font installer, reload any open design files in your browser or restart the Figma desktop app to use your new fonts.

To find fonts installed by you:

1. Open a Figma Design file.
2. Create or select a text layer.
3. Open the **Font** menu in the right sidebar.
4. Open the filter dropdown, choose **Installed by you**, then search for your font.

**Note**: If you’re working with others in the same file, make sure everyone has the same font styles installed. If someone uses a font style that you don’t have access to, you’ll receive a [missing font error](https://help.figma.com/hc/en-us/articles/360039956994-Missing-font-alert-in-Figma-Design).

![Font selector dropdown showing "Installed by you" filter with "Inter" highlighted in Figma's typography panel.](https://help.figma.com/hc/article_attachments/26982310211479)

## Upload local fonts to use with MCP and Figma agent

Uploading a font to your account makes them available in any file you view or edit, and enables Figma’s MCP and agent to access them.

To upload a font to your account:

1. Open Figma in the file browser.
2. Click your avatar in the top-left corner to open the account menu.
3. Select **Settings** to open the settings modal.
4. Select **Account** > **Your uploaded fonts**.
5. Click **Upload fonts** to search and select one from your files.
6. Confirm that you have the rights to upload this font and that you authorize its storage and use on the Figma platform.

Uploaded fonts will be listed under the **Uploaded by you** section of the font picker.

## Troubleshooting resources

If you're running into issues with fonts not working as expected, check out these troubleshooting resources:

- [Missing font alert in Figma Design](https://help.figma.com/hc/en-us/articles/360039956994-Missing-font-alert-in-Figma-Design)
- [Manage conflicting fonts](https://help.figma.com/hc/en-us/articles/4403175325719-Manage-conflicting-fonts)
- [Access and troubleshoot missing Adobe fonts](https://help.figma.com/hc/en-us/articles/23035569468439-Access-and-troubleshoot-missing-Adobe-fonts-in-Figma-Design)
- [Troubleshoot the Figma font installer](https://help.figma.com/hc/en-us/articles/32801027692183-Troubleshoot-the-Figma-Font-installer)
