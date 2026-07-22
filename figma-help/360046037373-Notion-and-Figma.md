---
기술지원명: Notion and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Notion and Figma
출처링크: https://help.figma.com/hc/en-us/articles/360046037373-Notion-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

[Notion](https://www.notion.so/) is an all-in-one workspace that combines your important work tools, like notes, docs, wikis, and project management, in one collaborative and customizable space.

Embedding a Figma file preview lets you add your Figma files to Notion. File previews are automatically synced with Figma so the latest changes will be reflected in Notion. This allows you to:

- View Figma files inside your meeting notes, project documentation, or design specs
- Share designs with teammates who may not have access to Figma
- Collect design feedback from collaborators

**Note**: [Embedded Figma files](https://help.figma.com/hc/en-us/articles/360039827134) only work in browser-based applications. To use embedded files in Notion, you must use Notion in the browser and not the desktop application.

# Embed a Figma file preview in Notion

You can embed a file preview for any Figma file or prototype. Anyone with access to the Notion doc will be able to view the file preview in Notion.

When you embed a file, you have the option to link to a specific page or top-level frame within the file by copying its link.

1. Open the page and select the top-level frame you'd like the embed to show (optional).
2. Click **Share** in the right sidebar.
3. Click **Copy link**.

![Figma share window with "Copy link" highlighted, allowing users to share or embed files in collaborative platforms like Notion.](https://help.figma.com/hc/article_attachments/27176868305815)

You can paste the link directly or use the **/figma** or **/embed** slash commands to add the embed in Notion.

1. Go to the Notion page where you’d like to share your Figma file preview.
2. Type **/figma** or **/embed** to add an embed block. Paste the URL you copied to add the embed.
   - Alternatively, you can simply paste the URL. If you paste the URL without using a slash commend, choose how you want the embed to show:
     - Select **Paste as preview** to display the file as an inline preview.
     - Select **Paste as mention** to link to the file using a stylized link.
     - Select **Paste as link** to link to the file using a standard URL.  
       ![Embed Figma in Notion: Type /embed, paste URL, choose Paste as preview for inline display.](https://help.figma.com/hc/article_attachments/5546271491223)

Notion may ask you to authenticate with Figma to access the file.

Tip! Learn more about Notion link previews in [this guide](https://www.notion.so/help/guides/visual-link-previews-streamline-collaboration) on Notion's [Help Center](https://www.notion.so/help/embed-and-connect-other-apps#link-previews).

The Notion integration was built using Figma's REST API. Check out [Figma's REST API documentation](https://www.figma.com/developers/api) to learn how to build your own.
