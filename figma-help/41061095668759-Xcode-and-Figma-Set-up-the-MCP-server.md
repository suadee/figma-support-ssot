---
기술지원명: Xcode and Figma: Set up the MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Xcode and Figma: Set up the MCP server
출처링크: https://help.figma.com/hc/en-us/articles/41061095668759-Xcode-and-Figma-Set-up-the-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server gives Xcode structured access to Figma files and tools. It can read design context such as components, variables, layout data, FigJam content, and Make resources, generate code from selected frames, use Code Connect to stay aligned with real components. When moving from Xcode to Figma, you can also write directly to the canvas to create or update native Figma content, and send live web interfaces to Figma as editable layers.

[Jump to the setup instructions →](#h_01KPPEJMXTZGNJS32R62SCME0S)

**Note:** The Figma MCP server is only supported in the Xcode 27 beta app. See Apple's Dev Tools announcement.

This article describes how to set up the Figma MCP server in Xcode. To learn more about the features of the Figma MCP server and how to use it, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

Figma also includes a SwiftUI skill to use with the Figma MCP server in Xcode. See Figma skills for MCP.

## Set up the remote Figma MCP server

**Note:** Make sure to install Xcode before you set up the server: [Download and install Xcode 27 beta](https://developer.apple.com/download/all/?q=Xcode%2027%20beta). The Figma MCP server is only supported by Xcode 27 beta.

The recommended way to set up the Figma MCP server in Xcode is by installing the Figma plugin, which includes MCP server settings as well as Agent Skills for common workflows.

First, make sure that the Xcode 27 beta app is open.

To install the Figma plugin, use Xcode's one-click setup and authorize the MCP
server for your Figma account: [One-click setup](xcode://agent-plugin-clone?repo=https%3A%2F%2Fgithub.com%2Ffigma%2Fmcp-server-guide)

Once added, click **Sign in...** next to the Figma plugin entry to authorize your Figma account.

If you want to confirm the plugin is installed: In Xcode, go to **Settings**, and then click **Intelligence**. The Figma plugin will be listed in the **Plug-ins** section.

### Manually set up the remote Figma MCP server

If you prefer, you can manually set up the remote Figma MCP server. There's no difference in functionality if you follow the manual steps.

In Xcode:

1. Go to **Settings**, and then click **Intelligence**.
2. Install an agent such as Claude Agent, Codex, or Gemini.
3. Click **Plug-ins**.
4. Click **Add plug-in**.
5. Choose **Add from URL**.
6. Enter the following in the URL field: [`https://github.com/figma/mcp-server-guide`](https://github.com/figma/mcp-server-guide)
7. Choose the **Figma Plug-in**.
8. Once added, authorize your Figma account to use the MCP server in Xcode.

## What's next?

If you're coming from the Figma MCP collection, [jump back into the previous article](https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server-preferred#h_01K6BEK6DD4A2HHRYXVH6KSS3M).

For more about using the Figma MCP server, see:

- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)
- [Other Figma MCP server articles in our Help Center](https://help.figma.com/hc/en-us/sections/39166717350935-Figma-MCP-server)
- [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server/)
