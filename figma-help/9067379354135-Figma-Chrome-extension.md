---
기술지원명: Figma Chrome extension
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Figma Chrome extension
출처링크: https://help.figma.com/hc/en-us/articles/9067379354135-Figma-Chrome-extension
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available on [all plans](https://figma.zendesk.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

The [Figma Chrome extension](https://chromewebstore.google.com/detail/figma/fkmaohpngenfoccdgceedjkfhkdcohmg) allows you to capture webpages and convert them into editable design layers, and to add Figma files to Google Calendar events.

This article covers how to download and install the extension, and step-by-step instructions on how to use it.

## Install the extension

1. Open the [**Figma** extension listing](https://chromewebstore.google.com/detail/figma/fkmaohpngenfoccdgceedjkfhkdcohmg) in the Chrome Web Store.
2. Click **Add to Chrome**, then confirm **Add extension** in the prompt.
3. Pin the Figma icon to your toolbar for easy access.
4. Click the Figma icon and sign in with the same account you use for Figma.

**Tip:** Optionally, you can configure a keyboard shortcut for the Figma extension at `chrome://extensions/shortcuts`. You can create shortcuts for launching the extension, capturing a whole page, or capturing individual elements.

If you already use the Figma Chrome extension for adding FigJam links to calendar events, you're set. Code to canvas is part of the same extension and turns on automatically once you're signed in to a paid plan.

Other extension features (such as the Google Calendar integration) remain available on all plans.

## Turn a webpage into editable designs

Capture any webpage or element on a page, and bring it to Figma design and FigJam as editable design layers. The Figma Chrome extension looks at the available code that's backing the web elements and translate it to Figma. This means that Figma is able to apply things like certain auto layout properties, font properties, and variables (if available) to the design.

#### Step 1: Open the toolbar

Navigate to the webpage you want to capture, then click  in your Chrome toolbar or use the keyboard shortcut you configured. The capture toolbar appears, anchored to the page.

![](https://help.figma.com/hc/article_attachments/42003741390615)

#### Step 2: Select what to capture

You have two options:

- To capture an element, click **Select element**, hover to highlight a region (a card, hero section, or button), then click to capture it.
- To capture the full page, click **Capture page**. The capture includes parts of the page that are scrolled out of view.

Each item you capture is added to the tray in the toolbar and automatically copied to your clipboard.

#### Step 3: Add a library to bind variables to the pasted design (Optional)

When you copy and paste designs using the Figma Chrome Extension, Figma will try to connect existing variables (color, number, and string) when pasting into Figma Design files. This includes variables from added libraries or variables local to the file.

If there are variables from a different file that you’d like to use, be sure to [add the library](https://help.figma.com/hc/en-us/articles/1500008731201) **before** you paste the design. If the variables you want to use already live inside the file, you can skip this step.

**Note**: Figma uses a [set of rules to decide which variables to match](https://help.figma.com/hc/articles/40826832449303#h_01KXNQ2P2GG9ZGJS2WGYZHASZ5) and bind to the pasted designs.

#### Step 4: Paste into Figma

Open a Figma Design file or FigJam board and paste with `⌘V` (macOS) or `Ctrl+V` (Windows / Linux). The capture is placed on the canvas as Figma layers, such as frames, text, images, and shapes, which you can move, edit, and restyle like any other content.

## Add Figma files to Google Calendar events

Start meetings off on the right foot by connecting Google calendar to Figma. Use the [Figma Chrome extension](https://chrome.google.com/webstore/detail/figma/fkmaohpngenfoccdgceedjkfhkdcohmg?hl=en) to attach FigJam and Figma Design files to your Google Calendar events and make every brainstorm, project kick off, and critique a jam.

### Get started

1. [Log in to your Figma account](https://help.figma.com/hc/en-us/articles/360041064554-Log-in-or-add-accounts)
2. [Create an event in your Google Calendar](https://support.google.com/calendar/answer/72143?hl=en&co=GENIE.Platform%3DDesktop)

### Create a new file

![Attach FigJam or Figma Design files to a Google Calendar event using the Figma for Chrome extension interface.](https://help.figma.com/hc/article_attachments/9097202642199)

1. Click **Add FigJam board** or **Add Figma file**.
2. Click a **New FigJam board** or **New Figma file**.
3. Give the file a name, then click **Create file**.

### Add existing files

1. Click **Add FigJam board** or **Add Figma file**.
2. Browse files from your **Recents** folder.
3. Select one or multiple files.
4. Click **Add to event**.
