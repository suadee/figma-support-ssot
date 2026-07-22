---
기술지원명: Gemini CLI and Figma: Set up the MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Gemini CLI and Figma: Set up the MCP server
출처링크: https://help.figma.com/hc/en-us/articles/39889246888855-Gemini-CLI-and-Figma-Set-up-the-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server gives Gemini CLI structured access to Figma files and tools. It can read design context such as components, variables, layout data, FigJam content, and Make resources, generate code from selected frames, use Code Connect to stay aligned with real components. When moving from Gemini CLI to Figma, you can also write directly to the canvas to create or update native Figma content, and send live web interfaces to Figma as editable layers.

[Jump to the setup instructions →](#h_01KPPGHCQTQAC1KQSB1YS03ETE)

This article describes how to set up the Figma MCP server in Gemini CLI. To learn more about the features of the Figma MCP server and how to use it, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

Figma provides two versions of the Figma MCP server: remote and desktop. The remote Figma MCP server is the version most users need and has the broadest set of features. The desktop version is for specific organization and enterprise use cases. Generally, you should use the remote Figma MCP server.

**Note:**
Make sure to install Gemini CLI on your computer before the setup. 
[Install Gemini CLI →](https://geminicli.com/docs/get-started/installation/)

## Set up the remote Figma MCP server (preferred)

Install the Figma extension for Gemini CLI by running the following command:

```
gemini extensions install https://github.com/figma/mcp-server-guide
```

Once installed, authenticate with Figma by running `gemini` and then executing the following command within the CLI:

```
/mcp auth figma
```

To uninstall the extension:

```
gemini extensions uninstall figma
```

## Set up the desktop Figma MCP server

Figma provides the local desktop version of the Figma MCP server for some specific organization and enterprise use cases, but we strongly recommend using the [remote version of the Figma MCP server](#h_01KPPGHCQTQAC1KQSB1YS03ETE). The remote version of the server provides the broadest set of features.

Instructions for the desktop Figma MCP server

**First, enable the desktop MCP server in Figma:**

1. Install and open the Figma desktop app.
2. Open a Figma Design file.
3. With nothing selected on canvas, click the toggle switch in the toolbar to switch to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247).
4. Then, click to enable the MCP server in the right sidebar.
5. Figma will display a confirmation message at the bottom of the screen letting you know the server is enabled and running, and you’ll see a button to copy the address for the server.
6. Click copy URL, and keep it handy for your configuration in the next step.

**Then, configure the desktop MCP server in Gemini CLI:**

1. Open your terminal and run the MCP add command for the Gemini CLI: `gemini mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp`
2. Restart Gemini CLI to make sure the configuration changes are picked up.
3. In your terminal, run the MCP auth command: `gemini mcp auth figma-desktop`

Once authorized, you're ready to start using the desktop Figma MCP server.

## What's next?

If you're coming from the Figma MCP collection, [jump back into the previous article](https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server-preferred#h_01K6BEK6DD4A2HHRYXVH6KSS3M).

For more about using the Figma MCP server, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)
- [Other Figma MCP server articles in our Help Center](https://help.figma.com/hc/en-us/sections/39166717350935-Figma-MCP-server)
- [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server/)
