---
기술지원명: Access and troubleshoot missing Adobe fonts in Figma Design
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Access and troubleshoot missing Adobe fonts in Figma Design
출처링크: https://help.figma.com/hc/en-us/articles/23035569468439-Access-and-troubleshoot-missing-Adobe-fonts-in-Figma-Design
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

You can access and use Adobe fonts in both the browser and the Figma desktop app. There are a few things to keep in mind when using Adobe fonts in Figma:

- If you’re working in the same file with collaborators, they’ll need to install the same font and version of the font to their computer
- Some versions of Adobe apps [require you use the fonts and applications on your computer on a regular basis](https://helpx.adobe.com/nz/fonts/using/activate-fonts-desktop.html) in order to keep them working on desktop apps like Figma
- We recommend restarting your Adobe and Figma app, or reloading your browser tab, after installing new Adobe fonts

## Add Adobe fonts to Figma Design

### 1. Download Adobe fonts to your computer

To access Adobe fonts in Figma Design, you’ll need to add them to your computer using Adobe Fonts. [Follow Adobe’s steps to add fonts to your computer →](https://helpx.adobe.com/nz/fonts/using/activate-fonts-desktop.html)

### 2. Access Adobe fonts in Figma Design

To access Adobe fonts [using Figma in a supported browser](https://help.figma.com/hc/en-us/articles/360039827194), you need to install the Font installer before you can add use Adobe fonts in Figma Design files. If you're using the [Figma desktop app,](https://help.figma.com/hc/en-us/articles/5601429983767) the font installer is already included in the app.

[Download the Figma font installer](https://www.figma.com/downloads/)

After installation, reload any open files in your browser to start using the font.

**Note**: The Figma font installer, FigmaAgent, runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

You can always [uninstall the font helper](https://help.figma.com/hc/en-us/articles/19764441960599) if you need to, but will lose access to local and Adobe fonts on your computer.

## Troubleshoot missing Adobe fonts

### The font is missing

The text layer is using a font you don't have installed. The font could have been used by a collaborator or a different device with the font installed.

![Missing fonts notification in Figma, prompting to replace unavailable fonts "Misto" and "Ribes" on the canvas.](https://help.figma.com/hc/article_attachments/27454856554135)

How do I check if this is my issue?

Reference the Adobe Fonts app to make sure the font installed on your computer. If the font or Adobe app hasn't been used recently, the font may need to be reinstalled.

How do I fix it?

Add Adobe Fonts to Figma Design by following the steps in [Adobe Learn and Support →](https://helpx.adobe.com/nz/fonts/using/activate-fonts-desktop.html)

### You haven't used Adobe fonts or apps recently

Adobe’s products require they be used or relaunched after a set amount of time has passed in order to keep using the font on your device.

How do I check if this is my issue?

Reference Adobe Fonts to see if the font you’re missing needs to be reinstalled. Look for a cloud icon next to the font name in your font list.

How do I fix it?

[Install the font to your computer,](https://helpx.adobe.com/nz/fonts/using/activate-fonts-desktop.html) then restart your browser, Figma desktop app, Adobe CC/Adobe Fonts, and also your computer if you haven't done so recently.

### There are conflicting versions of the font being used

If this only affects existing files you work on with multiple editors or on multiple devices you may see [conflicting fonts](https://help.figma.com/hc/en-us/articles/4403175325719).

How do I check if this is my issue?

Check if you can see this font available in the font picker in a new file in the desktop app.

How do I fix it?

To resolve conflicting font issues, all editors in the file need to:

#### Update the font

1. Uninstall and remove the local font from their computer.
2. Download and install the font from one common source.
3. Restart the desktop or browser app.

#### Update affected layers

1. Select a layer using that font.
2. Click  to open the main menu.
3. Go to **Edit** > **Select all with** > **Select all with same font**.
4. Open the quick actions menu and type **Recompute Text Layout in Selection** to reset text to the correct formatting.

[Learn more about conflicting fonts →](https://help.figma.com/hc/en-us/articles/4403175325719)
