---
기술지원명: Guide to the Figma desktop app
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Guide to the Figma desktop app
출처링크: https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on
[any plan](https://help.figma.com/hc/en-us/articles/360040328273)

macOS: Must be running macOS 12 (macOS Monterey
released in October 2021) or later

Windows: Must be running Windows 10 or later
in a 64-bit environment

Learn more about
[Figma's browser requirements](https://help.figma.com/hc/en-us/articles/360039827194).

The Figma desktop app gives you access to the same features and functionality as using Figma in a browser. You can also:

- [Develop](https://help.figma.com/hc/en-us/sections/360011316734-Contribute) plugins and widgets for your organization or the Figma Community
- Access and use fonts installed on your device without needing the font installer

## Download the Figma desktop app

Figma has desktop apps available for macOS and Windows. Download the Figma app for a more native Figma experience.

**Note:** If you're using the Figma for Government solution, please refer to [this article](https://help.figma.com/hc/en-us/articles/22932461365015-Figma-for-Government#h_01K6134BQZTA6BJCNR8N6J76A9) to find and download the desktop app for government accounts.

### Check your system requirements

Check if your device meets the minimum operating system requirements for installing and using the Figma desktop app.

**macOS**

The Figma desktop app is optimized for Macs with Intel and Apple Silicon processors.

1. Click the Apple menu in the top-left corner.
2. Select **About this Mac**.

The version number will be displayed under the version name. You must be running **macOS 12** or later.

**Windows**

1. Click the **Start** button.
2. Enter **Computer** in the search field.
3. Right-click and select **Properties**.
4. Identify the version under the **Windows edition** field. You must be running **Windows 10** or later in a **64-bit** environment.

### Download and install desktop apps

1. Download Figma for desktop:
   - [Download Figma for macOS](https://www.figma.com/download/desktop/mac)
   - [Download Figma for Windows](https://www.figma.com/download/desktop/win/)
   - [Download Figma for Windows Arm](https://www.figma.com/download/desktop/win-arm)
2. Figma will download the desktop app to the location you have configured. Click on the downloaded file to run the installer.
3. Move the Figma icon from the **Downloads** folder to your **Applications** folder.
4. Delete the Installer from your **Desktop** or **Downloads** folder.
5. Open the Figma app to get started.

**Note**: The Figma font installer, FigmaAgent, has no interface to open. It runs silently in the background, automatically detecting fonts already installed on your computer and making them available in Figma.

Behind the scenes, FigmaAgent runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

### Updating the desktop app

We recommend keeping the desktop app updated to the latest available version. If you are not on the latest version, a message will display in the app prompting you to update. If your computer is managed by your company, you may need to contact your administrator to update the app.

Support for previous versions is removed six months after release.

### Beta version of the desktop app

Figma also has a beta version of the desktop app available.

By using the beta version of the app, you're helping Figma test bug fixes and performance improvements, before we release them to the general public. **The beta version does not give you access to features Figma hasn't released yet.**

You can install and use the Figma desktop app and the beta version at the same time. Both versions of the desktop app will offer the same core features and functionality.

You do not need to be logged into the same account on both versions.

### Download the beta version

**Caution:** The beta version of the desktop app is a test environment. If you notice issues or behaviors that need our attention, please [submit a bug report](https://help.figma.com/hc/en-us/articles/360041468234-Submit-a-bug-report). Switch to the regular version of the desktop app if needed.

1. Download the beta version of the Figma Desktop app:
   - [Beta version of desktop app for macOS](https://desktop.figma.com/mac-installer/FigmaBeta.zip)
   - [Beta version of desktop app for Windows](https://desktop.figma.com/win/beta/FigmaBetaSetup.exe)
2. Figma will download the app to the location you have configured. Click on the downloaded file to run the installer.
3. Move the Figma icon from the **Downloads** folder to your **Applications** folder.
4. Delete the Installer from your **Desktop** or **Downloads** folder.
5. Open the Figma Beta app to get started.

Once installed, app icons display as **Figma** for the regular desktop app and **Figma Beta** for the beta version.

![Image of the Figma and Figma Beta app icons highlighted on Mac Dock.](https://help.figma.com/hc/article_attachments/29044373313431)

## Log in to Figma

Log in to your Figma account using:

- [Email address and password](https://help.figma.com/hc/en-us/articles/360041064554-Log-in-or-add-accounts#email)
- [Google Single Sign On](https://help.figma.com/hc/en-us/articles/360041064554-Log-in-or-add-accounts#google)
- [Third-party identity provider (SAML SSO)](https://help.figma.com/hc/en-us/articles/360041064554-Log-in-or-add-accounts#SAMLSSO)

## File browser

When you open the Figma desktop app, you’ll see the file browser where you can explore and access drafts, teams, and resources in your account. Learn more about the [file browser and exploring your account](https://help.figma.com/hc/en-us/articles/14381406380183).

When viewing the Community through the desktop app, you can navigate back and forward using the arrow keys.

## View files

Viewing a file opens up a tab in the desktop app’s navigation bar. You can differentiate between file types using the default favicons next to the file name.

Emojis in file names are supported and will be used in the tab instead of the default favicon if it is included at the start of the file name.

![Figma file browser showing different icons in the upper toolbar, representing different files.](https://help.figma.com/hc/article_attachments/30233285755159)

### Manage tabs

You can manage tabs from the desktop app and the tab menu, including pinning, muting, and closing tabs.

**Manage pinned tabs**

You can pin a tab to the navigation bar by right-clicking it and selecting **Pin tab** from the menu. A favicon will be used to indicate the pinned tab. Hover over the pinned tab to view the full file name.

To unpin a tab, right-click on the tab and select **Unpin tab**.

![](https://help.figma.com/hc/article_attachments/30233271767191)

The right-click menu has additional options for managing your tabs:

- **Close other tabs:** Closes other tabs except for the currently selected tab, including pinned tabs.
- **Close all tabs:** Closes all tabs including the currently selected tab.

**Manage tabs that are playing audio**

Some designs or prototypes play audio. When a tab is playing audio, it shows an audio icon.

- To mute a tab, click its audio icon—you don’t need to switch to that tab to mute it.
- Muting affects only that tab. To mute multiple tabs, mute each tab individually.

**Manage from the tab menu**

When you have more tabs open than fit on your screen, you can manage tabs in the tab menu from the top-right corner of the desktop app. From the tab menu, you can:

- View all open and recently closed tabs across any open Figma windows
- Scan file names, reopen recently closed tabs, and close tabs directly from the menu
- Mute a tab that's playing audio

A note about prototypes: When playing prototypes in [presentation view,](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes) tabs are hidden. If you'd like to show tabs in presentation view, select **View** > **Always Show Tabs When Presenting** from the toolbar. Always showing tabs when presenting prototypes is only available on Mac. For Windows, adjust your window size to include tabs in full screen.

### Tab groups

Stay organized across many open files without losing track of which file you’re looking for by grouping tabs.

**Add a tab to a tab group**

1. Right-click the tab and select **Add to Tab Group**
2. Choose **New Tab Group** or select an existing group

When you create a new tab group, you'll be prompted to give it a name and color to keep it organized. Collapse or expand a group to see what's inside at any time by clicking its name.

**Edit, ungroup, or delete a tab group**

Right-click the group name to rename it, change its color, ungroup it, or delete it.

- Ungrouping tabs removes the group, but keep all tabs open
- Deleting a group tab removes the group and closes the tabs within it

### Split tab view

Split tab view lets you access two files in the same window. You can enter split tab view with two different files, or with two instances of the same file.

- **Split two different files:** Click and drag a tab from the navigation bar to the right or left side of the canvas. A blue highlight indicates which side the tab will snap to.
- **Split the same file:** Right-click on the tab in the navigation bar and select **Open in Split Tab**.

  Note: When the same file is split into two tabs, any changes made in one tab automatically appear in the second tab.

While in split tab view, you can click and drag the center handle to resize the split.

To exit split tab view, right-click on the tab in the navigation bar and select **Separate tabs** or click the X to close one of the tabs.

![An animation of setting up a split view screen to see two tabs at the same time.](https://help.figma.com/hc/article_attachments/30233271769111)

### Multiple windows

You can open multiple windows at once using the desktop app. Click and drag a tab out of the current window to open a new one. You can also drag tabs between your open windows.

![An animation showing a cursor bringing one of two tabs from the desktop app to another window, so two tabs are visible in two windows at once.](https://help.figma.com/hc/article_attachments/30233285763607)

### Desktop notifications

Access your [Figma notifications](https://help.figma.com/hc/en-us/articles/360039813234-Manage-email-notification-preferences) from the Menu Bar on Mac or the System Tray on Windows. Notifications keep you in loop with your Figma files, Community activity, comments, and more.  
Available on the desktop app only.

![Notification center in the top of a Mac. Figma is selected, so Figma notifications are visible.](https://help.figma.com/hc/article_attachments/30233285765143)

## Trackpad haptic feedback

Haptic feedback is a physical response to a virtual action, such as a small vibration or other touch sensation.

On the Figma desktop app, you can enable trackpad haptics to receive feedback for actions such as creating prototype connections in Figma, using emotes and high-fives in FigJam, and more.

To turn on haptic feedback:

1. From any file, click on the Figma dropdown menu.
2. Select **Preferences**.
3. Toggle on **Trackpad Haptic Feedback**.

Haptic feedback is available for trackpads on macOS devices. In order to use this feature, make sure the **Force Click and haptic feedback** setting is enabled from your Mac’s **System Preferences > Trackpad** settings.
