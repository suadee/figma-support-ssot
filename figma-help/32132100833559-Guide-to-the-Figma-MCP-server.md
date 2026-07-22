---
기술지원명: Guide to the Figma MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Guide to the Figma MCP server
출처링크: https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

The remote server is available on [all seats and plans.](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

The desktop server is available on a [Dev or Full seat](https://help.figma.com/hc/en-us/articles/27468498501527-Updates-to-Figma-s-pricing-seats-and-billing-experience#h_01JCPBM8X2MBEXTABDM92HWZG4) for [all paid plans.](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

You must use a code editor or application that supports MCP servers (i.e. VS Code, Cursor, Windsurf, Claude Code, Codex). [See our MCP catalog for a full list of supported clients](https://figma.com/mcp-catalog).

---

For information about usage and rate limits, see [Plans, access, and permissions](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/) in the Figma developer documentation.

The Figma MCP server helps developers explore and implement designs quickly and accurately:

- Use your agentic tools to create and modify native Figma content directly in Figma Design, FigJam, and Figma Slides.

  **Note:** We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.
- Get design context and code from your Figma designs, FigJam, and Make files
- Capture your live UI as design layers, bringing the interfaces rendered by your code to Figma Design files
- Enhance the way you work with design components and Code Connect
- Use fonts uploaded to your account with the MCP Server and Figma Agent

**Note:** This guide is a high-level look at what's offered by the Figma MCP server. For specific instructions about using the server and example prompts, see:

- [Get started with the Figma MCP server](https://help.figma.com/hc/en-us/articles/39216419318551/)
- [Remote Figma MCP server installation](https://help.figma.com/hc/en-us/articles/35281350665623) (preferred)
- [Desktop Figma MCP server installation](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
- [Figma skills for MCP](https://help.figma.com/hc/en-us/articles/39166810751895)
- [Tools and prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
- [The Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

Detailed articles are also available in the [Figma developer documentation](https://developers.figma.com/docs/figma-mcp-server/).

The tools within Figma’s MCP server bring additional context from Figma into your workflow, so your code doesn't just match your existing systems, but your design, too.

MCP servers are part of a standardized interface for AI agents to interact with data sources using the [Model Context Protocol](https://modelcontextprotocol.io/introduction).

[See our Figma MCP Collection to learn more about the MCP server and bringing Figma into your workflow →](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

**Note:** This page is a general overview of the Figma MCP server. For detailed instructions and code samples, see the [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server).

With the server enabled, you can:

- **Let your agent write directly to the canvas in Figma Design and FigJam**

  Create and modify native Figma content directly from your MCP client. With the right skills, agents can build and update frames, components, variables, and auto layout in your Figma files using your design system as the source of truth.

  **Note:** This feature requires the [remote Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/). We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.

  This feature is continuously being improved. If you encounter issues, you can report the issues using [Fig, our support chatbot](https://help.figma.com/hc/en-us/articles/360041057214-Explore-Figma-s-help-and-support-resources#h_01KBJZP4HEVHZSHXBV6PFQBPH0), or by [emailing support (paid plans)](https://help.figma.com/hc/en-us/articles/360041057214-Explore-Figma-s-help-and-support-resources#h_01KBJZP4JHXDEZM922NWPF3P9D).

  [Learn more about writing to the canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)
- **Generate designs from the live UI of your web apps and sites**

  Turn live UI from your browser (production, staging, or localhost) into editable design layers in Figma. Send pages, elements, or whole flows to Figma Design for exploration, alignment, and refinement.

  **Note:** This feature requires the [remote Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) and is currently supported by select clients.

  This feature is continuously being improved. If you encounter issues, you can report the issues using [Fig, our support chatbot](https://help.figma.com/hc/en-us/articles/360041057214-Explore-Figma-s-help-and-support-resources#h_01KBJZP4HEVHZSHXBV6PFQBPH0), or by [emailing support (paid plans)](https://help.figma.com/hc/en-us/articles/360041057214-Explore-Figma-s-help-and-support-resources#h_01KBJZP4JHXDEZM922NWPF3P9D).

  [Learn more about generating designs from your interfaces](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/)
- **Generate code from selected frames**

  Select a Figma frame and turn it into code. Great for product teams building new flows or iterating on app features.
- **Extract design context**

  Pull in variables, components, and layout data directly into your IDE. This is especially useful for design systems and component-based workflows.
- **Retrieve FigJam resources**

  Access content from your FigJam diagrams and use it in your code generation workflow. Incorporate early-stage ideas, flows, or architecture maps directly into development.
- **Retrieve Make resources**

  [Gather code resources from Make files](https://developers.figma.com/docs/figma-mcp-server/bringing-make-context-to-your-agent/) and provide them to the LLM as context. This can help as you move from prototype to production application.
- **Keep your design system components consistent with Code Connect**

  Boost output quality by reusing your actual components. Code Connect keeps your generated code consistent with your codebase.

  [Learn more about Code Connect](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect)

## Set up the MCP server

You can connect the Figma MCP server in two ways:

- **Remote MCP server (preferred)**: Connects directly to Figma’s hosted endpoint at `https://mcp.figma.com/mcp`. [Learn how to install the remote MCP server.](https://help.figma.com/hc/en-us/articles/35281350665623)
- **Desktop MCP server**: Runs locally through the [Figma desktop app.](https://www.figma.com/downloads) [Learn how to install the desktop MCP server.](https://help.figma.com/hc/en-us/articles/35281186390679) The desktop MCP server is primarily for specific use cases for organizations and enterprises. For the broadest set of features, use the remote MCP server.

**Note:** The MCP server and Figma Agent can access fonts uploaded to your account. [Learn how to add a font to Figma.](https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma)

### Connect the MCP server to your editor

Follow instructions for your specific editor to connect to the Figma MCP server, either locally or remotely. Some clients also support [skills](#h_01KG5HNM2M3Y6RGBRK84FH1Z1E), which add agent-level instructions that help AI tools work more effectively with Figma designs:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Client** | **Desktop server support** | **Remote server support** | **Write to canvas (remote only)** | **Plugin/skills support** |
| [Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/qdev-mcp.html) | ✓ |  |  |  |
| [Android Studio](https://developer.android.com/studio/gemini/add-mcp-server) | ✓ | ✓ |  |  |
| [Augment Code](https://docs.augmentcode.com/setup-augment/mcp) | ✓ | ✓ | ✓ |  |
| [Claude Code](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server#h_01KPPEJMXTZGNJS32R62SCME0S) | ✓ | ✓ | ✓ | [Figma plugin](https://claude.com/plugins/figma) |
| [Claude Desktop](https://support.claude.com/en/articles/10065433-installing-claude-desktop) | ✓ | ✓ | ✓ | [Figma connector](https://claude.ai/directory/connectors/figma) |
| [Codex by OpenAI](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server#h_01KPPFC952S5ZRG6KQCTVRAKCG) | ✓ | ✓ | ✓ | [Codex Skills](https://github.com/openai/skills/blob/main/skills/.curated/figma-implement-design/SKILL.md) |
| [Copilot CLI](https://github.com/features/copilot/cli) | ✓ | ✓ | ✓ | [Figma plugin](https://awesome-copilot.github.com/plugins/#file=plugins%2Ffigma) |
| [Cursor](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server#h_01KPPGE8VQMJAXZ6CSZ0M32VHY) | ✓ | ✓ | ✓ | [Figma plugin](https://cursor.com/en-US/marketplace/figma) |
| [Factory](https://docs.factory.ai/cli/configuration/mcp#interactive-manager-%2Fmcp) | ✓ | ✓ | ✓ |  |
| [Firebender](https://docs.firebender.com/context/mcp/overview#installing-mcp-servers) | ✓ | ✓ | ✓ |  |
| [Gemini CLI](https://help.figma.com/hc/en-us/articles/39889246888855-Gemini-CLI-and-Figma-Set-up-the-MCP-server#h_01KPPGHCQTQAC1KQSB1YS03ETE) | ✓ | ✓ |  | [Extension](https://geminicli.com/extensions/?name=figmamcp-server-guide) |
| [Kiro](https://kiro.dev/docs/mcp/servers/#remote-mcp-servers) | ✓ | ✓ | ✓ | [Kiro Powers](https://kiro.dev/powers/) |
| [Openhands](https://docs.all-hands.dev/usage/mcp) | ✓ |  |  |  |
| [Replit](https://docs.replit.com/replitai/mcp/overview) |  | ✓ |  |  |
| [VS Code](https://help.figma.com/hc/en-us/articles/39890361040535-VS-Code-and-Figma-Set-up-the-MCP-server#h_01KPPGM2WBVB21ZYNEXJYDH16P) | ✓ | ✓ | ✓ | [Figma plugin](https://awesome-copilot.github.com/plugins/#file=plugins%2Ffigma) |
| [Warp](https://docs.warp.dev/knowledge-and-collaboration/mcp#adding-an-mcp-server) | ✓ | ✓ | ✓ |  |
| [Xcode](https://help.figma.com/hc/en-us/articles/41061095668759) (beta) |  | ✓ | ✓ | [Figma plugin](https://help.figma.com/hc/en-us/articles/41061095668759#h_01KPPEJMXTZGNJS32R62SCME0S) |

### About Skills

Skills provide guidance for how an agent should complete specific tasks, using a combination of MCP tool calls and detailed instructions.

While the Figma MCP server exposes individual tools, Skills help agents understand which tools to use, how to sequence them, and how to apply the results when working with Figma designs.

Skills can guide agents through workflows like:

- Connect Figma design components to code components using Code Connect
- Generate design system rules aligned to your codebase
- Translate designs into production-ready code

Skills don’t replace MCP connections or add new MCP capabilities. They reduce setup and guesswork by packaging recommended workflows into reusable instructions.

To learn more about skills:

- [Use skills with the Figma MCP server](https://help.figma.com/hc/en-us/articles/39287396773399)
- [Figma skills for MCP](https://help.figma.com/hc/en-us/articles/39166810751895)

**Note:** Skills are also available from the [Figma Community](https://www.figma.com/community/skills) and via community contributions in the [Figma community-resources repo](https://github.com/figma/community-resources/tree/main/agent_skills) on GitHub.

**Tip:** For the latest list of supported editors and clients, check out our [MCP Catalog](https://www.figma.com/mcp-catalog).

## Prompt your MCP client

The Figma MCP server introduces a set of tools that help LLMs translate designs in Figma. Once connected, you can prompt your MCP client to access a specific design node.

For a complete list of tools and examples, see [Tools and Prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/).

First, follow the instructions to install the Figma MCP server for your preferred MCP client. We provide instructions for:

- [Claude Code](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server#h_01KPPEJMXTZGNJS32R62SCME0S)
- [Codex by OpenAI](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server#h_01KPPFC952S5ZRG6KQCTVRAKCG)
- [Cursor](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server#h_01KPPGE8VQMJAXZ6CSZ0M32VHY)
- [Gemini CLI](https://help.figma.com/hc/en-us/articles/39889246888855-Gemini-CLI-and-Figma-Set-up-the-MCP-server#h_01KPPGHCQTQAC1KQSB1YS03ETE)
- [VS Code](https://help.figma.com/hc/en-us/articles/39890361040535-VS-Code-and-Figma-Set-up-the-MCP-server#h_01KPPGM2WBVB21ZYNEXJYDH16P)
- [Xcode](https://help.figma.com/hc/en-us/articles/41061095668759)

For other MCP clients, follow the instructions in your client's documentation for adding MCP servers. See the table under [Connect the MCP server to your editor](#h_01K25F7RBRZKCATVJHNXCS6KXW) for links.

### Example: Get design context

Getting design context and code from files is link-based. To get design context:

1. In Figma Design, select the layer you want to get design context for.
2. Right-click a frame or layer in Figma and select **Copy link to selection**.
3. In your MCP client, paste the URL and prompt your client to help you implement the design.

   ![MCP client with link-based prompt](https://developers.figma.com/assets/images/mcp-client-link-prompt-9d423d7411aa6f368abb1e71ad9fd93c.png)

Your client won't be able to navigate directly to the selected URL, but it will extract the node ID that is required for the MCP server to identify which object to return information about.

### Example: Send UI to Figma

**Note:** Currently available using the [remote Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) with certain clients. See the table under [Connect the MCP server to your editor](#h_01K25F7RBRZKCATVJHNXCS6KXW) for a list of supported clients.

Sending the live UI of your web app or site to Figma is done through conversation with your MCP client:

1. Prompt your MCP client: "Start a local server for my app and capture the UI in a new Figma file."
2. Follow the steps your client provides. Your client will open a browser window for you, or give you a link to follow.
3. Use the capture toolbar to capture pages, elements, and states of your web app or site.
4. Let your client know when you're finished. Your client will give you a link to open the Figma file that was created.
