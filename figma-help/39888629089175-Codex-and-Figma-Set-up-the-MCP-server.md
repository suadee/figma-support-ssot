---
기술지원명: Codex and Figma: Set up the MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Codex and Figma: Set up the MCP server
출처링크: https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server gives Codex structured access to Figma files and tools. It can read design context such as components, variables, layout data, FigJam content, and Make resources, generate code from selected frames, use Code Connect to stay aligned with real components. When moving from Codex to Figma, you can also write directly to the canvas to create or update native Figma content, and send live web interfaces to Figma as editable layers.

[Jump to the setup instructions →](#h_01KPPFC952S5ZRG6KQCTVRAKCG)

This article describes how to set up the Figma MCP server in Codex. To learn more about the features of the Figma MCP server and how to use it, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

Figma provides two versions of the Figma MCP server: remote and desktop. The remote Figma MCP server is the version most users need and has the broadest set of features. The desktop version is for specific organization and enterprise use cases. Generally, you should use the remote Figma MCP server.

**Note:**
Make sure to install Codex on your computer before the setup.
[Download Codex →](https://openai.com/codex/get-started/)

## Set up the remote Figma MCP server (preferred)

![codex-plugin.png](https://help.figma.com/hc/article_attachments/39889902107415)

To set up the Figma MCP server in Codex:

1. In the upper-left corner of the Codex app, click **Plugins**.
2. Click **+** next to Figma.
3. Click **Install Figma** to begin the installation process.
4. Go through the authentication process. Click **Allow access** to authenticate and allow ChatGPT to access your Figma account.

Once you're done, head back to Codex. The Figma plugin should now be connected, and you’re ready to start using Figma in Codex.

## Set up the desktop Figma MCP server

Figma provides the local desktop version of the Figma MCP server for some specific organization and enterprise use cases, but we strongly recommend using the [remote version of the Figma MCP server](#h_01KPPFC952S5ZRG6KQCTVRAKCG). The remote version of the server provides the broadest set of features.

Instructions for the desktop Figma MCP server

**First, enable the desktop MCP server in Figma:**

1. Install and open the Figma desktop app.
2. Open a Figma Design file.
3. With nothing selected on canvas, click the toggle switch in the toolbar to switch to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247).
4. Then, click to enable the MCP server in the right sidebar.
5. Figma will display a confirmation message at the bottom of the screen letting you know the server is enabled and running, and you’ll see a button to copy the address for the server.
6. Click copy URL, and keep it handy for your configuration in the next step.

**Then, configure the desktop MCP server in Codex:**

1. In Codex, in the lower-left corner of the interface, click **Settings**, and then **Settings** again.
2. In the left sidebar, click **MCP servers**.
3. Above the list of servers, click **Add server**.
4. Change the server type from **STDIO** to **Streamable HTTP**.
5. In the **Name** box, enter: `figma-desktop`
6. In the **URL** box, enter: `http://127.0.0.1:3845/mcp`
7. In the lower-right corner, click **Save**.

While the Figma desktop app is open and the desktop MCP server is enabled, you can start using the desktop Figma MCP server in Codex.

## Troubleshooting

If you can't see the plugin or some of the tools in Codex, please check with your Codex administrator that third-party plugins are allowed, and that new tools are approved by the administrator.

## What's next?

If you're coming from the Figma MCP collection, [jump back into the previous article](https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server-preferred#h_01K6BEK6DD4A2HHRYXVH6KSS3M).

For more about using the Figma MCP server, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)
- [Other Figma MCP server articles in our Help Center](https://help.figma.com/hc/en-us/sections/39166717350935-Figma-MCP-server)
- [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server/)
