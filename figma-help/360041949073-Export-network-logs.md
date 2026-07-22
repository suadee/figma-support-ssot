---
기술지원명: Export network logs
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Export network logs
출처링크: https://help.figma.com/hc/en-us/articles/360041949073-Export-network-logs
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**What:** Use the developer tools to view and capture any problems connecting to the network.

**Why:** The network log will highlight any connection issues. This is useful if you're experiencing issues with loading times, image quality, or importing and exporting assets.

## Open developer tools

Open the **Developer tools** using the keyboard shortcut. This works in both the Figma desktop app and in the browser.

- **Mac:**  `Command` `Option` `I`
- **Windows:**  `Ctrl` `Alt` `I`

Or, head to **Help** in the menu bar and selecting **Toggle Developer Tools:**

![Menu showing "Toggle Developer Tools" highlighted for accessing developer tools.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d77319404286364bc8ee9b5/file-zMrOVkox1o.png)

## Export network log

The Network log will highlight any connection issues. This is useful if you're experiencing issues with loading times, image quality, or importing and exporting assets.

1. From the Developer Tools window, select the **Network** tab: ![Developer Tools window with Network tab open, showing network requests and response details for troubleshooting Figma connection issues.](https://help.figma.com/hc/article_attachments/360058965894)
2. Perform the action you're experiencing an issue with. This could be importing an image, interacting with an object, or performing a multi-player action.
3. The Network tab will show details of any interactions between your Figma account and the network.
4. Click the down arrow `⇩` in the toolbar to **Export HAR** file: ![Network tab in developer tools showing connection details and export button for capturing a HAR file.](https://help.figma.com/hc/article_attachments/360058966014)
5. Attach any files to your conversation with Figma's support team.

When you submit an HAR file, we recommend sanitizing it before sharing. You can do this by using [Cloudflare's open source HAR sanitizer](https://har-sanitizer.pages.dev/). Please be aware that while Cloudflare is not associated with Figma, no data leaves your computer during this process. As an added measure of safety, you can also disconnect from the internet before uploading your HAR file.
