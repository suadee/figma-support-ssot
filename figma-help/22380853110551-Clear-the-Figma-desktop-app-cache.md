---
기술지원명: Clear the Figma desktop app cache
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Clear the Figma desktop app cache
출처링크: https://help.figma.com/hc/en-us/articles/22380853110551-Clear-the-Figma-desktop-app-cache
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

If you experience an issue while using the Figma desktop app, we recommend clearing the app’s cache. This is a common solution for performance or technical issues that you're only experiencing on the desktop app.

There are two ways to clear the app’s cache: from the Figma desktop app, or from your computer's operating system.

## Figma desktop app menu

If you are still able to access and use the desktop app, you can clear the cache from the **Help** menu.

MacWindows

You can access the **Help** menu from the application
[menu bar.](https://support.apple.com/en-gb/guide/mac-help/mchlp1446/mac)
This is the menu next to the Apple menu bar at the top of your screen,
not
a menu within the Figma application.

1. Click **Help** in the Apple menu bar.
2. Select **Troubleshooting** >
   **Reset Figma and Restart**:![Help menu open in Mac, highlighting "Reset Figma and Restart" under Troubleshooting for clearing cache.](https://help.figma.com/hc/article_attachments/25019060982551)

You can access the **Help** menu from the toolbar at the
top
of your screen.

1. Click the
   toggle arrow in the toolbar at the top right of your screen.
2. Go to **Help** > **Troubleshooting**
   >
   **Reset Figma and Restart**:![Figma desktop app menu open on Windows, highlighting the path: Help > Troubleshooting > Reset Figma and Restart.](https://help.figma.com/hc/article_attachments/25019083033111)

## Operating system tools

If the Figma desktop app has become unresponsive and you're unable to interact with the app, you can clear the desktop app cache using tools from your computer's operating system.

MacWindows

Use the
[terminal on Mac](https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)
to clear the desktop app cache.

1. Force quit the Figma desktop app.
2. Open the **Terminal** app.
3. Enter the following command:

   ```
   rm -rf "$HOME/Library/Application Support/Figma"
   ```
4. Launch the desktop app.

Run a command from the Windows start menu to clear the desktop app cache.

1. Force quit the Figma desktop app.
2. Open the **Start** menu.
3. Enter the following command:

   ```
   %APPDATA%\Figma
   ```
4. In the window that opens, delete the Desktop and DesktopProfile
   folders,
   the `font\_cache` file, and the `settings` file if they exist.
5. Launch the desktop app.

If you’re still experiencing issues, [check out our troubleshooting checklist →](https://help.figma.com/hc/en-us/articles/360040523973-Troubleshooting-checklist)
