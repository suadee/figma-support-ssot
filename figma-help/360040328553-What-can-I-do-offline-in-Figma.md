---
기술지원명: What can I do offline in Figma?
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: What can I do offline in Figma?
출처링크: https://help.figma.com/hc/en-us/articles/360040328553-What-can-I-do-offline-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma is cloud-based, so you'll need to be connected to the internet to access the full functionality of Figma.

Working in the cloud means you don't have to worry about regularly saving or backing up your files. Figma does that for you. Unfortunately, the habit of routinely saving files takes a little longer to get used to.

That's not to say you're on your own when you find yourself without a connection. If you lose your connection to Figma while you're working, an icon will appear in the toolbar.

- The  icon lets you know that Figma is attempting to save your changes.
- The  icon lets you know that Figma considers you offline. There will also be a tooltip to confirm your connection status.

Only the [current page and any other pages that were loaded](https://help.figma.com/hc/en-us/articles/1500005554982#h_01HHDQ77YC3D3NK7K9DEE3SQKQ) during the session will be available to you. If you continue working, Figma will store any changes you make in your browser, and sync them when you're back online. You'll also see a notification at the bottom of your screen that your file has unsaved changes.

Note: Figma posts updates on any downtime or connectivity issues on our status page. You can subscribe to for updates via email, SMS, and RSS. Visit the Figma status page at <https://status.figma.com/>

## Use Figma offline

Figma is designed for the browser, and real-time collaboration is at the heart of what we do. We don't currently have plans to support a fully-featured offline mode.

We've put together a non-exhaustive list of which features and functions are available when you're offline.

### Available offline

- Create one new Figma file.
- The current page of your open files, as well as any additional [pages in those files that were loaded](https://help.figma.com/hc/en-us/articles/1500005554982#h_01HHDQ77YC3D3NK7K9DEE3SQKQ) while online.    

  Note: If you navigate away from an open file created while online, you will lose access to that file until you go back online.
- Create layers, including frames, basic shapes, boolean operations, and vector networks.
- Use components that are created in the current file.
- [Play preloaded prototypes](https://help.figma.com/hc/en-us/articles/26463081577367-Present-prototypes-offline).
- Make changes to layer properties, including fill, stroke, dimensions, position, layer order.
- Run plugins that don't rely on external browser APIs. You will only be able to use plugins that you have already open.
- Save your files to your computer in .fig format. This will save a copy of the file as it currently. exists, and doesn't include any comments or version history.

### Not available offline

- Open files that were created while you were online.
- Pages that haven’t loaded in files that you have open.
- Receive updates from other collaborators on files you have open.
- Search for components from libraries or insert instances from a library.
- Install new plugins, or run plugins that require external browser APIs.
- View a file's version history, or create new versions to save your changes to Figma.
- Use any multiplayer features, like seeing who is active in the file, observation mode, and multiplayer cursors.

**Note:** You can [save a copy of your file to your computer](https://help.figma.com/hc/en-us/articles/8403626871063). This is a snapshot of the current file, and doesn't include any unloaded pages, version history or comments. When you import the .fig into Figma, Figma will treat this as a new file. For this reason, we only recommend using this approach as a last resort.

## Figma autosave

**Caution:** Autosave is a safeguard in the event that something goes wrong, it's not a fully-featured offline mode. It significantly reduces the possibility of data loss, especially in the following circumstances:

- You have an unreliable internet connection, or unexpectedly lose your connection.
- There is a crash from either Figma, your browser, or your operating system.
- A browser error, machine restart, or power loss causes you to lose access to Figma.

If you lose internet connectivity and continue to make changes to your work, Figma will save any changes you make in your browser. This applies even if you close the tab or browser, or shut down your device entirely.

When your connection to Figma is restored, Figma will apply any changes you made to your file(s) while offline. If you've closed the affected files, you will need to reopen them to sync any offline changes.

- Autosave works even if there's more than one person working offline in the same file. Figma will prompt you to sync the file when you're back online.
- The same applies if you're working across multiple tabs. Figma will save pending changes in each tab, then merge them when you're back online.
- Figma only saves the changes you make to your file, not the entire file. These changes are saved locally to your browser's IndexedDB, and can't be accessed from another computer or device.

### Figma in the browser

If you try to close a tab or browser window with offline changes, you may get an alert from your browser. Unfortunately, Figma isn't able to control the message included in this dialog.

Figma will store your offline changes, even if you receive a "Changes you made may not be saved" message from your browser.

### Figma desktop app

Figma will give you the option to discard your changes if your try to close a tab, quit Figma, or log out of your account.

![Sync your offline changes modal with options to Discard & Log out, Cancel, or Show changes before logging out.](https://help.figma.com/hc/article_attachments/360092773954)

- If you choose to **Log out** or **Leave**, Figma will save your offline changes in the browser. You can then open any affected files to allow Figma to sync your offline changes.
- If you choose to **Discard** or **Discard and log out**, Figma will clear any offline changes it stored in the browser. This action can't be undone and you won't be able to retrieve those changes in the future.

## Offline changes not saved

There are a few scenarios where your changes won't be saved:

- You're using an unsupported browser, or version of a browser.
- Your cache or browsing data was cleared before you reconnected to Figma.
- Your browser was in private browsing or incognito mode. Or you used a shared computer or guest account, which automatically cleared browsing data.
- The browser's storage quota is already full and there's no room for Figma to save these changes.
- A browser extension prevented Figma from saving data in the browser.
- You made changes on a different browser than the one you reconnected to Figma on.

Which browser you are using will determine how long these changes will be saved in the browser. Most browsers allow Figma to store data for up to 30 days, while others store data for a shorter time. Supported browsers and timeframes are as follows:

- Google Chrome 58+ (30 days)
- Mozilla Firefox 51+ (30 days)
- Safari 10.1+ (7 days)
- Microsoft Edge 18+ (30 days)
- Opera 45+ (30 days)

**Note:** Autosave is not supported on any version of Internet Explorer. **[Learn more about Figma's browser requirements →](https://help.figma.com/hc/en-us/articles/360039827194-Figma-Browser-Requirements)**

## Sync offline changes

Figma saves any offline changes to your file(s) when your connection is restored. If you already have your file(s) open, Figma will apply your offline changes when you reload the tab.

If you open Figma in the file browser first, you'll see a blue notification at the bottom of your screen. You'll also see an **unsynced changes icon** on any files with offline changes.

![Unsynced offline changes notification in Figma with options to "Open to sync" or choose "Later."](https://help.figma.com/hc/article_attachments/31680228730647)

1. Click **Tap to review** on the banner to open the offline changes modal.
2. Figma will show you a list of any files with offline changes. Click **Open to sync** to open the file a new tab. ![Sync offline changes modal with options to open unsynced files. The unsynced files are listed in the modal, with an option to open each one to sync it.](https://help.figma.com/hc/article_attachments/360094995793)
3. File will load the file and apply any changes you made while you're offline. You'll see a notification to confirm your changes have been saved. ![Notification confirms offline changes synced with an option to dismiss, indicating successful data synchronization in Figma.](https://help.figma.com/hc/article_attachments/360092774014)
4. Return to the file browser and repeat the process for any other affected files.

**Note:** Figma only stores offline changes for up to 30 days, or 7 days for Safari users. If you try to sync older offline changes, Figma will let you know your changes can't be synced.

## Version history

As part of the autosave process, Figma will add two checkpoints to the file's version history. One before applying your offline changes, and one after. These checkpoints will look like other autosaved versions.

If you're working on a file with others, there may be some differences between the latest version of the file and your offline changes.

Figma will let you know if there are any conflicting changes via a notification. Click **Review** to open the file's version history, or **Dismiss** to ignore.

![Notification bar stating offline changes were synced, with options to dismiss or review for conflicts.](https://help.figma.com/hc/article_attachments/360092773874)

If something was synced incorrectly, or you don't want to keep the offline changes, you can restore a previous version of the file in the file's version history. **[Learn how to view and manage version history →](https://help.figma.com/hc/en-us/articles/360038006754-Version-History)**

## Clear autosave data

Clear your cache or browsing data to remove any offline changes from Figma. This applies to both Figma in the browser and the Figma Desktop app.

**Caution:** This will delete any offline changes and prevent you from saving them to Figma. Once you have cleared your browsing history, you will **not** be able to retrieved any unsaved changes.

### In the browser

- **Google Chrome:** Clear all your browsing data to remove offline changes from Figma: <https://support.google.com/accounts/answer/32050>
- **Safari:** lets you choose which websites you want to delete data from. You can use this feature to remove data from just Figma: <https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac>
- **Mozilla Firefox:** lets you choose which websites you want to delete data from. You can use this feature to remove data from just Figma: <https://support.mozilla.org/en-US/kb/storage>
- **Microsoft Edge:** Delete your browser history to remove any offline changes from Figma: <https://support.microsoft.com/en-us/help/10607/microsoft-edge-view-delete-browser-history>

### Figma desktop app

Even though the Figma desktop app is technically a browser application, the process is a little different. Clearing your cache on the Figma desktop app involves interacting with the Mac Terminal app, or the Windows command line.

#### Mac

Use the Terminal app to clear the cache.

1. Quit the Figma desktop app.
2. Open the Terminal.app and enter the following command:  `rm -rf "$HOME/Library/Application Support/Figma/"{Desktop,DesktopProfile}`
3. Try opening the Figma desktop app again.

#### Windows

Run a command line from the Start menu.

1. Close the Figma desktop app.
2. Open the **Start** menu and paste the `%APPDATA%\\Figma` command. Press the `Enter` key to submit.
3. In the window, delete the `DesktopProfile` folder.
4. Launch the Figma desktop app again.
