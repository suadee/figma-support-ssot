---
기술지원명: Claude Code and Figma: Set up the MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Claude Code and Figma: Set up the MCP server
출처링크: https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server gives Claude Code structured access to Figma files and tools. It can read design context such as components, variables, layout data, FigJam content, and Make resources, generate code from selected frames, use Code Connect to stay aligned with real components. When moving from Claude Code to Figma, you can also write directly to the canvas to create or update native Figma content, and send live web interfaces to Figma as editable layers.

[Jump to the setup instructions →](#h_01KPPEJMXTZGNJS32R62SCME0S)

This article describes how to set up the Figma MCP server in Claude Code. To learn more about the features of the Figma MCP server and how to use it, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

Figma provides two versions of the Figma MCP server: remote and desktop. The remote Figma MCP server is the version most users need and has the broadest set of features. The desktop version is for specific organization and enterprise use cases. Generally, you should use the remote Figma MCP server.

**Note:**
Make sure to install Claude code in your terminal before the setup.
[Install Claude Code →](https://claude.com/product/claude-code)

## Set up the remote Figma MCP server (preferred)

The recommended way to set up the Figma MCP server in Claude Code is by installing the Figma plugin, which includes MCP server settings as well as Agent Skills for common workflows.

![Scene_setup in claude code.gif](https://help.figma.com/hc/article_attachments/39888612462999)

To set up the Figma MCP server in Claude Code:

1. Open your terminal, and run the following command into your terminal:

   ```
   claude plugin install figma@claude-plugins-official
   ```

   **Caution:** If the plugin install command fails, it's likely because your organization has blocked plugin installation, either for all plugins or the Figma plugin specifically. In your own organization, you should reach out to your Claude administrators for help.
2. Press **Enter** to start the installation process.
3. Restart Claude code if it was running.
4. Type `/plugin` and press **Enter** to open the Plugin marketplace.
5. Use the right arrow key on your keyboard to navigate to the **Installed** tab.
6. Use the arrow key to navigate to the `figma` server and press **Enter** to start the authorization page.
7. Press **Enter** again to begin the authentication process. An external page will open.
8. Then click **Allow access** to authenticate and allow Claude Code to access your Figma account.
9. After you finished the authentication, head back to the terminal and enter the `/plugin` command again.

Under the **Installed** tab, the `figma` server should now display as connected, and you’re ready to start prompting in Claude Code.

## Set up the desktop Figma MCP server

Figma provides the local desktop version of the Figma MCP server for some specific organization and enterprise use cases, but we strongly recommend using the [remote version of the Figma MCP server](#h_01KPPEJMXTZGNJS32R62SCME0S). The remote version of the server provides the broadest set of features.

Instructions for the desktop Figma MCP server

**First, enable the desktop MCP server in Figma:**

1. Install and open the Figma desktop app.
2. Open a Figma Design file.
3. With nothing selected on canvas, click the toggle switch in the toolbar to switch to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247).
4. Then, click to enable the MCP server in the right sidebar.
5. Figma will display a confirmation message at the bottom of the screen letting you know the server is enabled and running, and you’ll see a button to copy the address for the server.
6. Click copy URL, and keep it handy for your configuration in the next step.

**Then, configure the desktop MCP server in Claude Code:**

1. Open your terminal and run the MCP add command for the Claude CLI `claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp`.
2. Restart Claude Code to make sure the configuration changes are picked up.
3. You should then see newly available figma commands as well as the Figma MCP server when you run the `/mcp` command.

## What's next?

If you're coming from the Figma MCP collection, [jump back into the previous article](https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server-preferred#h_01K6BEK6DD4A2HHRYXVH6KSS3M).

For more about using the Figma MCP server, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)
- [Other Figma MCP server articles in our Help Center](https://help.figma.com/hc/en-us/sections/39166717350935-Figma-MCP-server)
- [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server/)
