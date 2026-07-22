---
기술지원명: How many people can be in a file at once?
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: How many people can be in a file at once?
출처링크: https://help.figma.com/hc/en-us/articles/1500006775761-How-many-people-can-be-in-a-file-at-once
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma files are designed for sharing and collaboration. You can invite up to 500 collaborators to your files (of which 200 can edit at a time), so you can work and play with hundreds of your closest cursors at the same time.

Collaborating with large groups makes Figma perfect for large design critiques, workshops, meetings, or using Figma in the classroom. When you work with large groups in Figma, there are some behavior changes and limitations you may encounter.

## People editing or viewing the file

Before we jump into these limitations, a quick note about permissions:

Someone with **can view** permissions to a file can only view or comment on the file or prototype. People viewing a file explore different pages in the file, select layers and inspect properties, view prototypes, follow other collaborators, and add comments, emotes, or cursor chats.

Someone with **can edit** permissions to a file can modify it. They can do everything that people viewing the file can do, as well as make changes to any layers or objects.

You can join a file with **can edit** permission if:

- Link sharing is set to `can edit`
- You have `can edit` access to the team or project where the file lives
- You were invited to the file with `can edit` permissions

# File limits

There are three multiplayer limits when working in files. When the file reaches any of those limits, Figma will adjust the multiplayer experience to improve performance and maintain collaboration. The current multiplayer limits are:

- [200 cursors](#cursor)
- [200 people editing](#editor)
- [500 total participants](#participant) (both people editing and viewing the file)

## Cursors

To improve performance, Figma and FigJam will only show up to 200 multiplayer cursors to other users in a file at any one time (you'll always be able to see your own cursor). We will prioritize showing the cursors of people with **can edit** permission to the file.

Figma and FigJam will always show the cursors of anyone being followed by other participants. These cursors won’t contribute to the 200 cursor limit.

If you join any time after this limit is reached, we will notify you that your cursor is hidden to other participants. You’ll still be able to see your own cursor in the file.

**Tip:** If people follow you in a file, your cursor will be shown to everyone whether you have **can view** or **can edit** access to the file.

## People with edit access

Anyone that joins a file with the ability to edit it is included in the count of people who can edit the file. If the file has reached its 500-participant limit with people who have view-only access, up to 20 people with edit access can still join.

If you join after this limit is reached, Figma will show an alert to confirm you’ve been converted to view-only access. Click **Done** to dismiss the window.

If you have edit access to the file, this limitation only applies to the current multiplayer session. You'll be able to edit again once enough people leave the file.

People viewing the file can still take the following actions:

- [Follow someone in a file](https://help.figma.com/hc/en-us/articles/360040322673)
- [Play or preview prototypes](https://help.figma.com/hc/en-us/articles/360040318013)
- [Add or reply to comments on files or prototypes](https://help.figma.com/hc/en-us/articles/360039825314)
- [Add emotes to the board in FigJam files](https://help.figma.com/hc/en-us/articles/1500004290981)
- [Use cursor chat in FigJam files](https://help.figma.com/hc/en-us/articles/1500004414842)

## Participants

Once the file reaches 500 participants, anyone that joins the file will only see a static version of the file. It won't be possible to view any multiplayer actions, including other participants' cursors or any changes being made to the file.

If you join the file after this limit is reached, Figma will let you know that you have view-only access and any multiplayer cursors are hidden. Click **Open view-only** to open the view-only version of the file.

When participants start leaving the file, you can try refreshing the page to get access to it.
