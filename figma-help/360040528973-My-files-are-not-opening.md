---
기술지원명: My files are not opening
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: My files are not opening
출처링크: https://help.figma.com/hc/en-us/articles/360040528973-My-files-are-not-opening
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

There are several reasons why a file may not open. In this guide, we’ll explore some common situations and possible fixes.

## What are you seeing?

### 404 page or “You don’t have permissions”

If you open a file link and get a 404 page, the two most common explanations for this are:

- You don't have access to the file
- The file has been deleted

We recommend the following:

- When possible, save the URLs of files that you're experiencing issues with. If you need to work with support, having the file URLs can be helpful.
- Confirm you're logged in on the correct account
- Confirm you've accepted the invitation to view or edit the file under the correct account
- Check your deleted files to see if you can locate the file there
- Reach out to the file owner to [regain access to the file](https://help.figma.com/hc/en-us/articles/360040531773)

### Memory alerts or errors

Every browser has its own active memory limit. This can differ across devices, but the general understanding is there's an **active memory limit of 2GB** for each tab in a browser.

Figma measures your memory usage as a percentage of your available memory. To keep you informed of your memory usage, Figma displays banners and alerts at certain thresholds: 60%, 75%, and 100%.

If your file reaches `100%` of your memory limit, Figma will lock the file and inform you that there's no available memory. To access affected files, you will need to [reduce your memory usage →](https://help.figma.com/hc/en-us/articles/360040528173)

### Something else

Are you seeing a blank page or canvas, or something else entirely? Jump ahead to the next section!

## What can you try?

If you're not getting a 404 message or a memory alert, there are some actions you can take to improve performance.

### Make sure you’re connected

Figma requires access to a reliable and stable internet connection. While there are [some activities you can do offline](https://help.figma.com/hc/en-us/articles/360040328553), Figma doesn't have a dedicated offline version or mode.

If you’re offline, you can’t:

- Open your existing files, unless you opened them while online
- Access pages that hadn’t loaded while online
- Receive updates from other collaborators on open file
- Search for components from libraries or insert instances from a library
- Install new plugins, or run plugins that require external browser APIs
- View the version history of a file, or create new versions to save your changes to Figma
- Use any multiplayer features

### Check the Console log

The Console log in Chrome's developer tools records any actions the browser has performed. If any of these actions fail, they will show as red in the Console log.

If there are any errors there, you can [share a copy of the Console log](https://help.figma.com/hc/en-us/articles/19818634038935-Export-console-logs) with Figma's Support team. This information can help the Support team find and diagnose any error messages.

Open the **Developer tools** in the browser or desktop app using the shortcut:

- Mac: `Command` `Option` `I`
- Windows: `Ctrl` `Shift` `I`

![Console log displaying multiple failed resource load errors with red HTTP error codes 403 and 429.](https://help.figma.com/hc/article_attachments/4406279642007)

[**Export network or console log →**](https://help.figma.com/hc/en-us/articles/360041949073)

## Share the file with support

When you've confirmed that you can't resolve issues opening a file, we encourage you to reach out to us through our [Support Hub](https://help.figma.com/hc/en-us/requests/new). Our support team will often ask further questions to help troubleshoot and identify any issues.

If the issue is happening with a specific file, please include the link to the affected Figma file when you submit a bug report. If you're having trouble locating the link, such as if the browser tab containing the file has been closed, you can try looking for the link in other places:

- In the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser), if the file that you can't open appears there, try to right-click on the file and select **Copy link**
- Check your browser history
- Review places where a link to the file may have been shared, such as other Figma files, email, documents, and chat conversations

If you have checked the console log and have identified errors there, please include an export of the console log in your bug report.

When working with support, if you can see the file that won't open in the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) and want to share it with them, try to right-click on the file and select **Share**. The support team doesn’t have access to your files by default. You can [share the file publicly](https://help.figma.com/hc/en-us/articles/360040531773), or invite the support team to the file. They will give you specific instructions for how to do this when you contact them. You won’t be charged for any Figma employees that have access to your account.
