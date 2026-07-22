---
기술지원명: Troubleshoot opening links in the Desktop app
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Troubleshoot opening links in the Desktop app
출처링크: https://help.figma.com/hc/en-us/articles/22850791655831-Troubleshoot-opening-links-in-the-Desktop-app
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

If you're not able to open Figma links using the Figma desktop app, you may be encountering one of these issues:

## The Desktop app is not installed or up to date

Download Figma for desktop

- [Download Figma for macOS](https://www.figma.com/download/desktop/mac)
- [Download Figma for Windows](https://www.figma.com/download/desktop/win/)

Confirm you‘re running the latest version of the Figma Desktop app

1. Click **Figma** from the top menu bar on a Mac, or the ⌄ top level menu on Windows.
2. Select **Check for Updates**.

You should also confirm your device meets the [minimum requirements to run the Figma desktop app](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app#h_01HE5QD60DSQGZCAWE05Y7JE6R).

## The Desktop app isn’t connected

The Figma Desktop app runs a tool called **FigmaAgent** to open Figma links from your browser. If this tool isn’t connected and running, it will prevent links in your browser from opening in the Desktop app.

**Possible reasons and solutions**

Local network access is blocked

If you’re using Chrome 142 or newer, you’ll need to [allow local network access](https://help.figma.com/hc/en-us/articles/34458998159511-Local-network-access-in-Figma) to open links in the Desktop app.

To allow local network access:

1. Visit `figma.com` in Chrome.
2. Click the settings icon in the address bar.
3. Select **Site settings**.
4. Find **Local network access**.
5. Set it to **Allow**.
6. Refresh the page.

The Desktop app is installed but not connected

If you already have the Desktop app installed, connect to it with these steps:

1. Open a Figma file in your browser.
2. From the  main menu, go to **Preferences** > **Permissions and helpers**.
3. Under **Local network access**, check if your connection to the browser is **Blocked** or **Not connected**.

If the status is **Blocked** or **Not connected**, follow the prompts in the dialog to allow local network access in your browser and connect the Font Installer.

[Learn more about local network access in Figma](https://help.figma.com/hc/en-us/articles/34458998159511-Local-network-access-in-Figma).

## Figma’s Desktop app can’t open this link

**Possible reasons and solutions**

You’re logged in with a different account

If you’re logged in to the Figma Desktop app with a different account than Figma in your browser, you’ll receive an error message.

Make sure you’re [logged in to Figma](https://help.figma.com/hc/en-us/articles/360041064554-Log-in-or-add-accounts) using the same Figma account in both the browser and desktop app.

The Figma Desktop app isn’t installed

Download Figma for desktop:

- [Download Figma for macOS](https://www.figma.com/download/desktop/mac)
- [Download Figma for Windows](https://www.figma.com/download/desktop/win/)

The link you’re opening isn’t to a Figma file.

The **Open links in desktop app** preference and **Open in desktop** action in the **Actions** menu only apply to individual Figma files, not other parts of the Figma application like the file browser or Figma Community pages.

## Your browser is blocking the Desktop app

You’re using a browser that is blocking the redirect (Brave, Microsoft Edge)

Browsers with strict privacy settings may prevent the Figma desktop app from opening when you open a link to a Figma or FigJam file.

You can get this feature working by adjusting your privacy settings and adding an exception for `figma.com`.

- **Brave**: Add an exception for `[figma.com](<http://figma.com>)` to your shield settings. [Learn more in Brave’s Help Center](https://support.brave.com/hc/en-us/articles/360023646212-How-do-I-configure-global-and-site-specific-Shields-settings).
- **Microsoft Edge**: Add an exception for [figma.com](http://figma.com/) to **Strict mode** for `Figma.com`. [Learn how in Microsoft's help center](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-security-browse-safer).
