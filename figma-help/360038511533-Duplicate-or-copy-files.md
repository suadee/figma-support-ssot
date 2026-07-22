---
기술지원명: Duplicate or copy files
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Duplicate or copy files
출처링크: https://help.figma.com/hc/en-us/articles/360038511533-Duplicate-or-copy-files
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273)

You need at least view access to a file to duplicate it

**Want to copy a Community file?** **[Learn how to use files from the Community →](https://help.figma.com/hc/en-us/articles/360038510873)**

When you duplicate files, Figma will create a new copy of the original file. This copy doesn't include any [comments](https://help.figma.com/hc/en-us/articles/360041068574) or [version history](https://help.figma.com/hc/en-us/articles/360038006754) from the original file.

Your access to the file or project determines where the copy will live in your file browser:

- **Can view:** If you can only view the file, you will be able to send a duplicate copy of the file to your drafts. You can edit it in your drafts, or move it into a team project which you have `can edit` access to.
- **Can edit:** If you have edit access to the file, or the project its located in, Figma will create a copy of that file in its current location. You can edit it there, move it your drafts, or move it to another team or project.

There are a few places you can duplicate a file. If you don't see any of these options in your file, it means someone with `can edit` access to the file has [restricted people with can view access from copying or exporting the file's contents](https://help.figma.com/hc/en-us/articles/360040045574).

## File browser

Duplicate the file from anywhere in the file browser.

1. Right-click on the file in the file browser.
2. Select **Duplicate** from the options.
3. Figma will prefix the new file's name with `Copy of`, so you can distinguish between the original and the duplicate.

**Note:** You can also duplicate files from your deleted files folder. **[Learn how to duplicate and restore deleted files →](https://help.figma.com/hc/en-us/articles/360047512294)**

## From an open file

Duplicate a file when viewing the file in the editor:

1. Click on an empty spot in the canvas or use the keyboard shortcut to deselect any layers.
2. Click file name  to open the file menu and select **Duplicate**. If you only have view access to the file or project, you will see **Duplicate to drafts** here instead.![Navigate to your project name, then select Duplicate](https://help.figma.com/hc/article_attachments/26846753229975)
3. Figma will create a copy of the file based on your access and the original file's location.

## Browser address bar

You can also duplicate a file by adding `/duplicate` to the end of the file. This only works when you are viewing the full file URL.

If you have a specific frame or layer selected, Figma will add an ID for that node to the URL. For example: `?node-id=21%3A0`. You need to remove any node id's before adding `/duplicate` to the file's URL.
