---
기술지원명: Embed files and prototypes
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Embed files and prototypes
출처링크: https://help.figma.com/hc/en-us/articles/360039827134-Embed-files-and-prototypes
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273). Applies to FigJam, Figma Slides, and Figma Design.

Anyone with can view or can edit access to a file or prototype can copy the embed code.

You can embed live FigJam files, Figma Design files, and prototypes into other tools and resources. Embeds appear alongside other content, making them a seamless addition to any website or browser-based application.

- Add style and component libraries in your design system documentation
- Include detailed feature designs and explorations in PRDs, spec documents, or user stories
- Keep FigJam files alongside meeting notes
- Share presentations, templates, or resources
- Embed or share prototypes in testing environments

![Interactive Figma embed showing a waving hand icon with example prototype and visibility settings in the panel.](https://help.figma.com/hc/article_attachments/26000118509591)

**Caution:** It’s not possible to add embeds within a native/desktop applications, you can only add embeds in browser-based applications.

## Figma Design and FigJam files

When you embed a file, you have the option to link to a specific page or top-level frame within the file. We recommend [reviewing the file's link sharing settings](#public-private) before you embed it in a website or application.

1. Open the page and select the top-level frame you'd like the embed to show (optional).
2. Click **Share** in the right sidebar.
3. Update the audience settings for the file. Set both the audience and the permission level.    

   Note: If the file is only shared with members of your organization, they must be logged in to view the embed.
4. Click **Get embed code** to open the embed code window.
5. Click **Copy** to add the embed code to your clipboard.
6. Paste the embed code in your application of choice.

![Figma share window displaying options to invite collaborators, set access permissions, and copy the embed code.](https://help.figma.com/hc/article_attachments/26000086293399)

## Prototypes

You can have as many pages as you want within a file. Each of these pages can have multiple prototype flows within them.

When you embed a prototype, you need to choose which page you want to share. If you embed prototypes on a specific page, people can access all flows on that page. You can also embed a specific flow.

We recommend [reviewing the file's link sharing settings](#public-private) before you embed it an external website or application.

1. Open the file and page the prototype lives on. Click **Present** to open the prototype in presentation view and select a flow from the left sidebar.
2. Click **Share prototype** in the toolbar.
3. Update the audience settings for the prototype. Set both the audience and the permission level.    

   Note: If the file is only shared with members of your organization, they must be logged in to view the embed.
4. Click the **Get embed code** link to open the embed code window.
5. Click **Copy** to add the embed code to your clipboard.
6. Paste the embed code in your application of choice.

## Public or private embeds

People can interact with embeds based on the file’s default sharing settings, or a person’s permissions on the file:

- If the file is shared within an organization, they’ll need to log in to access the file.
- If the file is password protected, it **cannot** be accessed from an embed.
- If they don’t have permissions on the file, or the file is shared publicly, they can access the file based on the file’s link sharing settings. [Interact with embeds →](https://help.figma.com/hc/en-us/articles/360051741274)

If prompted, people must allow embedded content in order to use the embed.

## Share settings

Embeds respect the same Share settings you apply when you share Figma files and prototypes with others. This means you don’t have to manage access for everyone independently, and that access to the file remains consistent across all surfaces. [Share files and prototypes: Access and permissions →](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes#h_01HWXCDSW2W2XAM58QK7YBX71C)

## Add Figma embeds to other applications

Some applications will allow you to embed a Figma file or prototype using just the Figma URL. Embed Figma files and prototypes into the browser-based version of these applications:

- [Coda and Figma](https://help.figma.com/hc/en-us/articles/360045485973)
- [Notion and Figma](https://help.figma.com/hc/en-us/articles/360046037373)
- [Jira and Figma](https://help.figma.com/hc/en-us/articles/360039827834)
- [Dropbox and Figma](https://help.figma.com/hc/en-us/articles/360039827514)
- [Confluence and Figma](https://help.figma.com/hc/en-us/articles/360053110673)
- [P2 and Figma](https://help.figma.com/hc/en-us/articles/1500002613622)
- [StoriesOnBoard and Figma](https://help.figma.com/hc/en-us/articles/360060797533)
- [Storybook and Figma](https://help.figma.com/hc/en-us/articles/360045003494)
- [Zeroheight and Figma](https://help.figma.com/hc/en-us/articles/360039829314)

[Explore all app integrations →](https://help.figma.com/hc/en-us/sections/360006538974)

**Caution:** It’s not possible to add or use these embeds within a native or desktop application. You can only add and use embeds in the browser-based version of these applications.

## Embed API

Figma provides Embed Kit 2.0, including the Embed API, to support programmatically embedding Figma files, prototypes, and slides in your sites and web apps. For more information, see Figma's developer documentation: [Embed Figma files →](https://www.figma.com/developers/embed)
