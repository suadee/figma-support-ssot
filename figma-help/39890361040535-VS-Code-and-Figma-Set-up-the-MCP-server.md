---
기술지원명: VS Code and Figma: Set up the MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: VS Code and Figma: Set up the MCP server
출처링크: https://help.figma.com/hc/en-us/articles/39890361040535-VS-Code-and-Figma-Set-up-the-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server gives VS Code structured access to Figma files and tools. It can read design context such as components, variables, layout data, FigJam content, and Make resources, generate code from selected frames, use Code Connect to stay aligned with real components. When moving from VS Code to Figma, you can also write directly to the canvas to create or update native Figma content, and send live web interfaces to Figma as editable layers.

[Jump to the setup instructions →](#h_01KPPGM2WBVB21ZYNEXJYDH16P)

This article describes how to set up the Figma MCP server in VS Code. To learn more about the features of the Figma MCP server and how to use it, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

Figma provides two versions of the Figma MCP server: remote and desktop. The remote Figma MCP server is the version most users need and has the broadest set of features. The desktop version is for specific organization and enterprise use cases. Generally, you should use the remote Figma MCP server.

**Note:**
Make sure you have VS Code installed on your computer, and enabled
GitHub Copilot in order to set up the Figma MCP server.
[Download VS Code →](https://code.visualstudio.com/)

## Set up the remote Figma MCP server (preferred)

![HC_setup in VS code.gif](https://help.figma.com/hc/article_attachments/39890336188055)

To set up the Figma MCP server in VS Code:

1. Open the command palette using the shortcut:
   - **Mac:** Cmd + Shift + P
   - **Windows:**  Ctrl + Shift + P
2. Search for **MCP: Open User Configuration**.
3. Inside the `mcp.json` file, paste the following code:

   ```
   {
      "inputs": [],
      "servers": {
        "figma": {
          "url": "https://mcp.figma.com/mcp",
          "type": "http"
        }
      }
    }
   ```
4. Save the file using the shortcut:
   1. **Mac:** Cmd + S
   2. **Windows:**  Ctrl + S
5. You’ll then see a **Start** button above the Figma MCP server name, select it to start the authentication process.

Go through the authentication process with your Figma account in an external window. Once you’re done, you should see that the Figma MCP server is now running in VS Code.

## Set up the desktop Figma MCP server

Figma provides the local desktop version of the Figma MCP server for some specific organization and enterprise use cases, but we strongly recommend using the [remote version of the Figma MCP server](#h_01KPPGM2WBVB21ZYNEXJYDH16P). The remote version of the server provides the broadest set of features.

Instructions for the desktop Figma MCP server

**First, enable the desktop MCP server in Figma:**

1. Install and open the Figma desktop app.
2. Open a Figma Design file.
3. With nothing selected on canvas, click the toggle switch in the toolbar to switch to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247).
4. Then, click to enable the MCP server in the right sidebar.
5. Figma will display a confirmation message at the bottom of the screen letting you know the server is enabled and running, and you’ll see a button to copy the address for the server.
6. Click copy URL, and keep it handy for your configuration in the next step.

**Then, configure the desktop MCP server in VS Code:**

1. Make sure you have [GitHub Copilot](https://github.com/features/copilot) enabled. This is required to use the Figma MCP server.
2. Open the command palette and search for “Add server”.
   1. macOS: `Shift` `Command` `P`
   2. Windows: `Shift` `Ctrl` `P`
3. Select **HTTP**.
4. Paste the server URL ``http://127.0.0.1:3845/mcp` in the search bar, then hit **Enter**.
5. Type in “Figma MCP” when it asks for a server ID, then hit **Enter**.
6. If you have a workspace open, select whether you want to add the server globally or only for the workspace.
7. Once confirmed, you'll see a configuration like this in your `mcp.json` file.

## What's next?

If you're coming from the Figma MCP collection, [jump back into the previous article](https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server-preferred#h_01K6BEK6DD4A2HHRYXVH6KSS3M).

For more about using the Figma MCP server, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)
- [Other Figma MCP server articles in our Help Center](https://help.figma.com/hc/en-us/sections/39166717350935-Figma-MCP-server)
- [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server/)
