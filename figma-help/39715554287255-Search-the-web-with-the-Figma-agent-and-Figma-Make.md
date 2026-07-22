---
기술지원명: Search the web with the Figma agent and Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Search the web with the Figma agent and Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/39715554287255-Search-the-web-with-the-Figma-agent-and-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma agent is currently available to try for free in open beta. [Learn more.](https://help.figma.com/hc/en-us/articles/34932042346775)

Who can use this feature

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Users with Full seats can chat with the agent in Figma Design and Figma Make files

Users with View, Dev, or Collab seats can try the agent in Figma Design and Figma Make files in Drafts

Requires edit access to the file

**Important:** Currently, web search is supported only for the default and Claude Opus models in Figma Make. [Learn more about selecting AI models.](https://help.figma.com/hc/en-us/articles/36400680326551)

![](https://help.figma.com/hc/article_attachments/40446572371607)

In supported products, such as Figma Design and Figma Make, the Figma agent can search the web and fetch content from URLs, so you can ground your designs, prototypes, and web apps in real-world, up-to-date information.

For example, you can:

- Reference a public design system or documentation site and apply its styles to your design
- Pull in content from a specific page to populate your prototype
- Find real-world examples or design inspiration to inform the generated output

**Tip:** If you need to bring in content from a page that requires a login—like internal documentation or a private site—consider [setting up a custom MCP connector](https://help.figma.com/hc/en-us/articles/38147204302743) to connect the Figma agent directly to those sources.

## Search the web

The agent uses two complementary tools to access live web content:

1. **Web search** performs a search query and uses the results to help with your request. Citations are automatically included.
2. **Web fetch** retrieves the full content of a specific URL—for example, a documentation page or brand guidelines site. The agent can analyze the content and apply it to the generated output.

In Figma Design, you must first [enable web search](#h_01KQTFZED42Q0R6778XTZ5NBK5) in the agent. This setting persists through all of your chats and can be turned off again. In Figma Make, web search is enabled by default.

To search the web, write a prompt that requires real-world information. The agent decides autonomously whether to use web search, web fetch, or both, based on what your prompt requires. You can invoke the tools explicitly by mentioning "search the web" or "fetch this URL" if you need to.

If Figma can't reach a page, it will let you know. Keep in mind:

- **The agent can only access public pages.** You can only fetch content from pages that are open on the public web.
- **Some sites may not be retrievable.** Web fetch may fail if a site uses anti-scraping protections. If this happens, Figma will let you know, and you can try an alternative source.

## Enable and disable web search

Web search can be toggled on and off in the Figma agent.

In Figma Make, web search in the agent is *on* by default. Outside of Figma Make, such as in Figma Design, web search in the agent is *off* by default.

When you enable or disable web search, this setting persists across agent chats and Figma Make files.

In Figma Design:

1. In a chat with the agent, click + in the prompt box.
2. Select **Web search** to toggle search on and off. A ✓ next to the option indicates that web search is on.

In Figma Make:

1. Open a Figma Make file.
2. In the upper-right corner, click  **Settings**.
3. Under  **Chat preferences**, toggle **Access to live web data** to turn web search on and off.

**Note:** If the web search toggle isn't visible, your organization admin has [disabled web search](https://help.figma.com/hc/en-us/articles/39717296726679).
