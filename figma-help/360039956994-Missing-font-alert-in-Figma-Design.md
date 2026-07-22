---
기술지원명: Missing font alert in Figma Design
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Missing font alert in Figma Design
출처링크: https://help.figma.com/hc/en-us/articles/360039956994-Missing-font-alert-in-Figma-Design
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

A missing font icon appears in the left sidebar of a Figma Design file if you don’t have access to a font being used. This is often caused by a font not installed on your computer, a missing font style, or conflicting versions of a font being used.

If you select a text layer with a missing font, the missing font icon will also appear next to the font name in the right sidebar. To see which fonts are missing and identify affected layers, click  in the left sidebar to open the **Missing fonts** modal.

![Missing fonts modal in Figma design](https://help.figma.com/hc/article_attachments/40566995036695)

## Common causes and solutions

### The font is not installed on your computer

The text layer is using a font which you don't have installed. The font could have been used by a collaborator or a different device with the font installed.

How do I check if this is my issue?

Check if the missing font in your Figma file is installed on your computer:

1. Open the fonts manager on your device.
2. Search for the font in question to confirm it is installed.
3. If the font is not installed, follow the steps to add it to your device:
   - **Mac**: [How to install, view, and remove fonts on your Mac](https://support.apple.com/en-us/HT201749) (via Apple)
   - **Windows**: [View and add a font](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1) (via Microsoft)

How do I fix it?

#### Add the missing font to Figma Design

**1. Prepare and download the font files**

Fonts are typically collections of OpenType (.OTF) or TrueType (.TTF) files. Each font can have several styles, and each style has its own file.

For example, using Inter Regular, Inter Bold, and Inter Extra Light requires three font files.

**Tip:** If you're using a font that other people use too, make sure you have the same styles. If someone uses a font style in a file but you don't have that style on your computer, you'll get a missing font error.

**Note**: Figma only supports .TTF and .OTF font files.

**2. Install the font on your computer**

To use a font, it must be installed in your computer’s font manager.

- On Mac, the font manager is called Font Book. Apple provides guidelines for [installing and validating fonts in Font Book on Mac.](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) As a general rule, if you can see your font in Font Book, it’s installed on your computer.
- On Windows, you can install fonts by adding font files to the **Fonts** folder. [Add a font →](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1)

**Note**: Figma doesn't support fonts for devices running ChromeOS or Linux. Chromebook and Linux users can only use Google fonts, which are the default fonts in Figma.

**3. Install the Figma font installer (browser only)**

**Note**: If you're using the desktop app, you can skip this step. The desktop app includes the Figma font helper.

If you use Figma in your web browser, you need to install the Figma installer, otherwise known as the font helper, before you can add your own font to Figma Design files.

[Download the Figma font installer](https://www.figma.com/downloads/)

After installation, reload any open files in your browser to start using your font.

**Note**: The Figma font installer, FigmaAgent, runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

You can always [troubleshoot](https://help.figma.com/hc/en-us/articles/32801027692183) and [uninstall the font helper](https://help.figma.com/hc/en-us/articles/19764441960599) if you need to.

### You're trying to use a local font with MCP

You're using a font that's only installed on your computer. MCP and the Figma agent run on Figma's servers, so they can't access fonts that are stored and accessed on your computer.

How do I check if this is my issue?

The error message from the Figma agent or in your terminal mentions missing fonts.

How do I fix it?

If the missing font isn’t displayed in the **Installed by you** section of the font picker, [add the missing font to Figma](#h_01HVS4JCNM9K0GQHGGVWQR03FM).

If the font is already installed on your device, upload it as a user-level font in the **Account Settings**. Fonts that can be accessed by Assistant will be listed under the **Uploaded by you** section of the font picker.

To upload a font to your account:

1. Open Figma in the file browser.
2. Click your avatar in the top-left corner to open the account menu.
3. Select **Settings** to open the settings modal.
4. Select **Account** > **Your uploaded fonts**.
5. Click **Upload fonts** to search and select one from your files.
6. Confirm that you have the rights to upload this font and that you authorize its storage and use on the Figma platform.

### There are conflicting versions of the font

Collaborators or devices are using a different (older or newer) version of the font.

How do I check if this is my issue?

To use a font, the same font version must be installed in your and your collaborator's computer’s font manager.

![Georgia font details in Font Book, showing preview and details about a font.](https://help.figma.com/hc/article_attachments/22979628458135)

- On Mac, the font manager is called Font Book. Apple provides guidelines for [installing and validating fonts in Font Book on Mac.](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) Select a font and click  to confirm the font version on all devices across collaborators.
- On Windows, you can view a font's version by going to **Start** > **Settings** > **Personalization** > **Fonts** > select a font to view its version.

How do I fix it?

#### Add the missing font to Figma Design

**1. Prepare and download the font files**

Fonts are typically collections of OpenType (.OTF) or TrueType (.TTF) files. Each font can have several styles, and each style has its own file.

For example, using Inter Regular, Inter Bold, and Inter Extra Light requires three font files.

**Tip:** If you're using a font that other people use too, make sure you have the same styles. If someone uses a font style in a file but you don't have that style on your computer, you'll get a missing font error.

**Note**: Figma only supports .TTF and .OTF font files.

**2. Install the font on your computer**

To use a font, it must be installed in your computer’s font manager.

- On Mac, the font manager is called Font Book. Apple provides guidelines for [installing and validating fonts in Font Book on Mac.](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) As a general rule, if you can see your font in Font Book, it’s installed on your computer.
- On Windows, you can install fonts by adding font files to the **Fonts** folder. [Add a font →](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1)

**Note**: Figma doesn't support fonts for devices running ChromeOS or Linux. Chromebook and Linux users can only use Google fonts, which are the default fonts in Figma.

**3. Install the Figma font installer (browser only)**

**Note**: If you're using the desktop app, you can skip this step. The desktop app includes the Figma font helper.

If you use Figma in your web browser, you need to install the Figma installer, otherwise known as the font helper, before you can add your own font to Figma Design files.

[Download the Figma font installer](https://www.figma.com/downloads/)

After installation, reload any open files in your browser to start using your font.

**Note**: The Figma font installer, FigmaAgent, runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

You can always [troubleshoot](https://help.figma.com/hc/en-us/articles/32801027692183) and [uninstall the font helper](https://help.figma.com/hc/en-us/articles/19764441960599) if you need to.

#### Use shared fonts (Organization and Enterprise plans)

Any fonts you upload to the organization will be available to everyone. Members of any team in the organization can access and use these fonts.

Only organization admins can upload fonts to the organization.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select **Resources** and then click **Fonts.**
3. Click  **Font** to add a font.
4. Select the font file from your computer. You can upload multiple font files at once. Click **Open** to select the fonts.
5. Confirm you have the necessary rights and licenses to use the font(s). Click **Upload** to start the upload process. The font will now be available in the font picker for files in the organization.

**Note**: Figma will let you know if you already have fonts uploaded with that font family name. Click **Skip** to leave the font out of the upload, or **Replace** to update the existing font.

#### Replace the missing font with an existing one

The missing fonts modal allows you to quickly update affected text layers, so you can update the font to one that already exists. This could be a font that’s already installed or a Google font, which is always available in Figma. You can use this approach to select an alternative font to use in your files. Updating the font applies to everyone in the file, not just you.

Note: Updating the font applies to all collaborators, including those with access to the original font. You may want to save a version of the file before you do, in case you need to reverse those changes.

1. Click  in the left sidebar.
2. View a list of fonts and styles that are missing or unavailable in this file:
3. Use the dropdown fields below **Replacement** to update the family and style for each missing font. Figma will only show you fonts available to you.
4. Click **Replace fonts** to complete the process. All text objects in the file will be updated to the new fonts.

### Font styles are missing

If you're using a font that other people use too, make sure you have the same styles for that font. If someone uses a font style in a file but you don't have that style on your computer, you'll get a missing font error.

How do I check if this is my issue?

To use a font style, the same font version must be installed in your and your collaborator's computer’s font manager.

![Georgia font details displayed in a Mac Font Book, showing preview, formats, and usage details.](https://help.figma.com/hc/article_attachments/22979628458135)

- On Mac, the font manager is called Font Book. Apple provides guidelines for [installing and validating fonts in Font Book on Mac.](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) Select a font and click  to confirm the font version on all devices across collaborators.
- On Windows, you can view a font's version by going to **Start** > **Settings** > **Personalization** > **Fonts** > select a font to view its version.

How do I fix it?

#### Add the missing font to Figma Design

**1. Prepare and download the font files**

Fonts are typically collections of OpenType (.OTF) or TrueType (.TTF) files. Each font can have several styles, and each style has its own file.

For example, using Inter Regular, Inter Bold, and Inter Extra Light requires three font files.

**Tip:** If you're using a font that other people use too, make sure you have the same styles. If someone uses a font style in a file but you don't have that style on your computer, you'll get a missing font error.

**Note**: Figma only supports .TTF and .OTF font files.

**2. Install the font on your computer**

To use a font, it must be installed in your computer’s font manager.

- On Mac, the font manager is called Font Book. Apple provides guidelines for [installing and validating fonts in Font Book on Mac.](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) As a general rule, if you can see your font in Font Book, it’s installed on your computer.
- On Windows, you can install fonts by adding font files to the **Fonts** folder. [Add a font →](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1)

**Note**: Figma doesn't support fonts for devices running ChromeOS or Linux. Chromebook and Linux users can only use Google fonts, which are the default fonts in Figma.

**3. Install the Figma font installer (browser only)**

**Note**: If you're using the desktop app, you can skip this step. The desktop app includes the Figma font helper.

If you use Figma in your web browser, you need to install the Figma installer, otherwise known as the font helper, before you can add your own font to Figma Design files.

[Download the Figma font installer](https://www.figma.com/downloads/)

After installation, reload any open files in your browser to start using your font.

**Note**: The Figma font installer, FigmaAgent, runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

You can always [troubleshoot](https://help.figma.com/hc/en-us/articles/32801027692183) and [uninstall the font helper](https://help.figma.com/hc/en-us/articles/19764441960599) if you need to.

#### Use shared fonts (Organization and Enterprise plans)

Any fonts you upload to the organization will be available to everyone. Members of any team in the organization can access and use these fonts.

Only organization admins can upload fonts to the organization.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select **Resources** and then click **Fonts.**
3. Click  **Font** to add a font.
4. Select the font file from your computer. You can upload multiple font files at once. Click **Open** to select the fonts.
5. Confirm you have the necessary rights and licenses to use the font(s). Click **Upload** to start the upload process. The font will now be available in the font picker for files in the organization.

**Note**: Figma will let you know if you already have fonts uploaded with that font family name. Click **Skip** to leave the font out of the upload, or **Replace** to update the existing font.

#### Replace the missing font with an existing one

The missing fonts modal allows you to quickly update affected text layers, so you can update the font to one that already exists. This could be a font that’s already installed or a Google font, which is always available in Figma. You can use this approach to select an alternative font to use in your files. Updating the font applies to everyone in the file, not just you.

Note: Updating the font applies to all collaborators, including those with access to the original font. You may want to save a version of the file before you do, in case you need to reverse those changes.

1. Click  in the left sidebar.
2. View a list of fonts and styles that are missing or unavailable in this file:
3. Use the dropdown fields below **Replacement** to update the family and style for each missing font. Figma will only show you fonts available to you.
4. Click **Replace fonts** to complete the process. All text objects in the file will be updated to the new fonts.
