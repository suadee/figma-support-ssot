---
기술지원명: Troubleshoot the Figma Font installer
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Troubleshoot the Figma Font installer
출처링크: https://help.figma.com/hc/en-us/articles/32801027692183-Troubleshoot-the-Figma-Font-installer
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma Font installer lets you access fonts installed to your computer when using Figma on a browser. This article outlines how to check the status of or restart the Figma Font installer.

The Figma Font Installer is known as the **FigmaAgent** when listed in the operating system’s list of running processes.

## Download the Figma font installer

There are two ways to download, install, and run the Figma Font installer on your computer:

- [Download the Figma Desktop App,](https://www.figma.com/downloads/) which includes the Figma Font installer
- [Download the Font Installer](https://www.figma.com/downloads/) if you only want to use custom fonts with Figma in a browser

## Check your permissions

If you’re using Figma in a browser, you should first confirm the status of your connection to the Font Installer and permissions.

To do so:

1. Open the  main menu.
2. Go to **Preferences** > **Permissions and helpers**.
3. Under **Local network access**, check if your connection to the browser is **Blocked** or **Not connected**.

If the status is **Blocked** or **Not connected**, follow the prompts in the dialog to allow local network access in your browser and connect the Font Installer.

[Learn more about local network access in Figma](https://help.figma.com/hc/en-us/articles/34458998159511-Local-network-access-in-Figma).

## **Check and Restart FigmaAgent**

### **macOS (Activity Monitor)**

**Locate FigmaAgent**

1. Open Finder.
2. Navigate to **Applications** > **Utilities** > **Activity Monitor**.
3. In Activity Monitor, go to the **CPU** tab.
4. Search for **FigmaAgent** in the search bar.

If **FigmaAgent** is listed, it is currently running.

**Quit FigmaAgent**

1. Select **FigmaAgent** in the process list.
2. Click **X** (Stop) at the top of the window.
3. Choose **Force Quit** in the confirmation dialog.

**Restart FigmaAgent**

1. Open the Figma desktop application or download and run the font installer from [figma.com/downloads](http://figma.com/downloads).
2. The FigmaAgent process will automatically start in the background.

### **Windows (Task Manager)**

**Locate FigmaAgent**

1. Press `Ctrl` `Shift` `Esc` or right-click on the taskbar and select **Task Manager**.
2. In **Task Manager**, go to the **Details** tab.
3. Search for **figma\_agent.exe** in the name column.

If **figma\_agent.exe** is listed, it is currently running.

**Quit FigmaAgent**

1. Select **figma\_agent.exe** in the process list.
2. Click **End task**.

**Restart FigmaAgent**

1. Open the Figma desktop application or download the font installer from [figma.com/downloads](http://figma.com/downloads).
2. The FigmaAgent process should automatically start in the background.
