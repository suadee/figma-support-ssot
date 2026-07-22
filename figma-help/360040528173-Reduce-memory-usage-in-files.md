---
기술지원명: Reduce memory usage in files
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Reduce memory usage in files
출처링크: https://help.figma.com/hc/en-us/articles/360040528173-Reduce-memory-usage-in-files
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available on all plans

Anyone with `can edit` access can enter recovery mode and reduce memory usage in a design file.

If you're working with large files or libraries in Figma, you may run into memory limitations. In this article, we'll outline some of the ways you can adapt your files so they work within these limitations.

- [What is memory](#memory)
- [Explore memory usage alerts](#alerts)
- [Reduce memory usage in files](#reduce)
- [Access locked or crashed files](#locked)

# What is memory?

We use the general term “memory” throughout this article to explain and address the memory alerts you’ll see in Figma.

In this article, we’re referring to a specific type of memory: WASM memory (WebAssembly Memory). Figma uses WASM memory to render layers and objects on the canvas and deliver a collaborative multiplayer experience.

Every browser has its own active memory limit. This can differ across devices, but the general understanding is there's an **active memory limit of 2GB per browser tab**.

As Figma is built on browser-based technologies, these limitations apply even when you’re using Figma’s desktop applications.

Figma employs a few methods to try to ensure you do not run out of memory
while working. For example,
[Figma loads pages and layers in a file only as needed](https://help.figma.com/hc/en-us/articles/1500005554982#h_01HHDQ77YC3D3NK7K9DEE3SQKQ)
to help keep memory usage as low as possible. However, as we explain later
in the article, some situations can still lead to a file running out of memory.

# Manage memory

Figma measures your memory usage as a percentage of available memory in your
browser or device. Memory usage is only tracked for
[pages that have loaded in a file](https://help.figma.com/hc/en-us/articles/1500005554982#h_01HHDQ77YC3D3NK7K9DEE3SQKQ).

To view memory usage indicators for the contents of your file:

1. Select the  Main menu and hover over **View.**
2. Select **Memory usage**. The memory usage will appear as a meter in your left sidebar.
3. Click **Manage memory.**
4. From the Manage memory modal, toggle **Show memory in layers panel**. This allows you to view how much memory your layers and components are using.

**Tip:** You can also view **Memory-reduction tips** in the modal for best practices to manage your file's memory.

## Memory usage alerts

To keep you informed of your memory usage, and any potential issues that may arise, Figma displays banners and alerts at certain thresholds:

**Note:** You may not see all these alerts in order. If memory usage increases in a short space of time, you may not receive an alert at all.

90 % usage100 % usage

When you reach `90%` of your memory limit, Figma will show a red alert tile in the left sidebar. You cannot dismiss this alert.

### View only access

![Memory usage warning at 92%, advises contacting file owner; edit access needed to manage memory.](https://help.figma.com/hc/article_attachments/16616255987223)

### Edit access

![Memory usage alert at 92.3%, recommending moving pages or deleting content to prevent losing file access. Manage memory button shown.](https://help.figma.com/hc/article_attachments/16616255990167)

You can still make changes to the file, but we recommend taking immediate action to protect your work. Failure to reduce memory usage now will increase the possibility of data loss.

Click **Learn more** to view suggestions for reducing memory usage or follow the [**tips we've outlined below ↓**](#reduce)

If your file reaches `100%` of your memory limit, Figma will lock the file and inform you that there's no available memory.

### Experience when you have view-only access to the file

Those with view access to the file will have the option to reload the file. Sometimes, reloading the file will free up enough memory for you to continue viewing the file.

### Experience when you have edit access to the file

Those with edit access to the file will have the option to reload the file. Sometimes, reloading the file will free up enough memory for you to continue viewing the file.

Otherwise, you’ll be prompted to enter recovery mode if you’re on a supported browser version and have edit access to the file. Recovery mode is supported on the following browser versions:

- Firefox 89+
- Chrome 83+
- Safari 15.2+
- Microsoft Edge 93+

If your current browser version isn’t supported, you’ll be asked to update the browser version, or to open the file in the desktop app.

[Install the Figma desktop app.](https://www.figma.com/downloads/)

### Recovery mode

Recovery mode allows you to reduce memory usage and return your file to an editable state without losing your work.

Upon entering recovery mode, all pages of the file will load and the manage memory modal will open. Memory usage must be reduced to below 90% to exit recovery mode.

**Note:** The file will reload once you exit recovery mode.

# Tips for reducing memory

There are a number of factors that contribute to memory. Unfortunately, there isn’t a specific number of layers, data, or resources you can look out for. This means we can’t give you a one-size-fits-all approach to reducing memory. If you’re experiencing high memory usage, use the following solutions to help troubleshoot the issue.

## Hidden layers

Hidden layers are a big contributor to memory usage. This is because Figma needs to store and render information about those layers even when they're not visible.

### Solutions

**Use boolean component properties**

[Boolean properties](https://help.figma.com/hc/en-us/articles/5579474826519#Boolean_property) are a type of component property that allows you to toggle a property, such as layer visibility, on and off. Even though this method uses hidden layers, it reduces the number of variants and layers needed in a design system, improving the file’s memory usage.

Tip: To delete a layer, select it in the canvas or Layers panel in the left sidebar. Then press the `delete` or `backspace`key to remove it.

**Note:** Figma only loads layers on pages that you open. Navigating across pages requires loading any remaining content on those pages, which can result in memory and number of layers increasing in the memory panel.

## Large component or variant libraries

The number of components and variants can contribute to memory usage. You may still run into memory limits if you have only a few component sets, but they have thousands of variants.

### Solutions

**Use component properties**

If a library has a large number of variants or a file is near the memory limit, consider using [component properties](https://help.figma.com/hc/en-us/articles/5579474826519) to reduce the number of components and variants needed.

This improves memory usage because Figma loads all components in a component set. This allows you to quickly switch between variants. If you use component properties and have less variants, there’s less components Figma needs to load.

**Break up large library files**

If your library file is still near the memory limit after making these adjustments, you may need to divide it into smaller libraries.

[Move published components and component sets](https://help.figma.com/hc/en-us/articles/4404848314647) between files, without breaking links to instances. This is a two-part process: cut and paste the components, then publish the changes.

There are lots of different ways you could divide up your library, the best approach is the one that meets the needs of your library's users. For more guidance on how to organize your library files, check out [Lesson 3 in our Introduction to design systems course](https://help.figma.com/hc/en-us/articles/14548865734679/).

## Large files with multiple images and pages

If you have a large file with a significant number of pages, or lots of high resolution images, you may experience performance or memory issues.

If this causes browser-level crashes, Figma won't display the memory usage banners. This is something to think about when working in files with a large number of high-resolution images.

### Solutions

**Split up large files into smaller files**

There are different approaches to organizing your library files. One place to start is create new files for each page in your current file. For more guidance on how to organize your library files, check out [Lesson 3 in our Introduction to design systems course](https://help.figma.com/hc/en-us/articles/14548865734679/).

1. Create a new file in your Figma account. In a separate tab, open the original file and view the page you want to move.
2. Use the **Select all** shortcut to select everything on the page.
   - Mac: `⌘ Command` `A`
   - Windows: `Ctrl` + `A`
3. Use the **Copy** shortcut to copy the page's contents to your clipboard.
   - Mac: `⌘ Command` `C`
   - Windows: `Ctrl` + `C`
4. Return to the new file in a separate tab. Use the **Paste** shortcut to paste the contents of your clipboard:
   - Mac: `⌘ Command` `V`
   - Windows: `Ctrl` + `V`
5. In the original file: open the page list in the left sidebar. Right-click on the page name and select **Delete page**.

**Compress your image files**

The [Downsize plugin](https://www.figma.com/community/plugin/869495400795251845/Downsize) allows you to compress large images on the canvas.

## Large assets

Importing large amounts of text, images, or complex vectors with many points can also impact your memory usage. You may need to reduce the number or quality of assets you import, or reduce the size of the files you're importing:

- Break large files into smaller files.
- Compress high resolution images.
- Import complex SVGs in smaller parts.

[**Learn how to import files into Figma →**](https://help.figma.com/hc/en-us/articles/360041003114)

Note: Image decoding uses JS memory, which isn't included in the memory percentage or banner alerts. Images can still contribute to WASM memory as they are rendered on the canvas.

# Access locked files

If your file reaches `100%` of your memory limit, Figma will lock the file and inform you that there's no available memory. There are two things you can try:

- [Restore the file to a version](https://help.figma.com/hc/en-us/articles/360038006754#Restore_from_version) that uses less memory. If you aren’t able to access version history from the file, you can still perform this action in the file browser.
- If you see a white screen, your file may have crashed due to image memory. In this state, you won’t be able to access the file or the file’s version history. You can try [open the file with images in thumbnail mode ↓.](#h_01GSZ65XKDHVXYF8AXSWS3PQKN)

## Restore previous version

1. Open the project where the file is located.
2. Hold down the modifier keys and click on the file:
   - **Mac:** `⇧ Shift` `⌃ Control` `⌥ Option`
   - **Windows:** `Alt` `Shift`
3. Select **Restore from version**.
4. Click **Restore** next to the appropriate version.

## Open file in thumbnail only mode

You may be able to access the file again using **thumbnail-only mode**. This loads the file with low-resolution images.

To access thumbnail-only mode, add a `?thumbnails-only=1` query parameter (also known as a [query string](https://en.wikipedia.org/wiki/Query_string)) to the end of the file URL.

- If the link doesn’t include existing parameters, the link ends with the file name. You can add a new `?thumbnails-only=1` query string to the end of the link. The final URL will look like this:

  ```
  https://figma.com/file/Xhi0lg09reehpFWk4f9NQh/file-name?thumbnails-only=1
  ```
- If the link already has parameters, like a `?node-id` parameter, you need to add `&thumbnails-only=1` instead. Use an `&` delimiter when adding more parameters to a query string. The final URL will look like this:

  ```
  http://figma.com/file/Xhi0lg09reehpFWk4f9NQh/file-name?node-id=211-2665&t=D5QnxlouJ9sKF1dM-0&thumbnails-only=1
  ```

You can now try [any approaches to reduce memory usage ↑](#reduce).
