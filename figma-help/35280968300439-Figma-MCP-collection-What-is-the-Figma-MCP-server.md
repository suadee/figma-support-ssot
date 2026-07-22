---
기술지원명: Figma MCP collection: What is the Figma MCP server?
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Figma MCP collection: What is the Figma MCP server?
출처링크: https://help.figma.com/hc/en-us/articles/35280968300439-Figma-MCP-collection-What-is-the-Figma-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## About MCP

The [Model Context Protocol ↗](https://www.anthropic.com/news/model-context-protocol), MCP for short, is an open-source standard for how different AI agents and applications talk to one another or to other external systems.

Companies and application owners, like Figma, can create their own MCP servers that follow this standard so their apps can interact with other products and systems that also use the MCP standard.

This way, all of your tools can communicate with each other and pass context to improve every step of your building process.

## Use Figma MCP and Figma Design

The Figma MCP server takes important context—like [variables](https://help.figma.com/hc/en-us/articles/15339657135383) and [components](https://help.figma.com/hc/en-us/articles/360038662654)—from your Figma Design files and brings it right into your development environment. This can help improve your workflows and keep your code consistent with your design components.

We packed the Figma MCP server with useful tools that let you take actions based on the content of your design files. You don’t need to know all of the tools available because when you write prompts in your AI client, it will automatically find the right tool for the job.

Your agentic tool should have a tools command that you can use to see the complete list of available tools, and check out our [developer documentation](https://developers.figma.com/docs/figma-mcp-server/) for the most up-to-date information.

## Use Figma MCP and Figma Make

The Figma MCP server also works with [Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231), Figma’s AI-powered prompt-to-app tool that turns your ideas into interactive prototypes and apps—all backed by real code. Figma Make is great for anyone, no matter their skill level or role, to create functional apps fast.

Pairing Figma Make with the Figma MCP server lets AI models view the underlying code behind your Figma Make files, and improves the quality of code generated in your AI-powered development tools.

[Learn more about Figma Make →](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make)

## Use Figma MCP and FigJam

You can also use the Figma MCP server with [FigJam](https://help.figma.com/hc/en-us/articles/15300412458647). Use FigJam’s diagramming tools—like shapes and connectors—to create flowcharts and other diagrams that illustrates the logic for the app you’re trying to build.

![](https://help.figma.com/hc/article_attachments/35924613139735)

Then, with the help of the Figma MCP server, your agentic development tools can reference the diagram to quickly write code and application logic for your products.

## Types of servers and integrations

Figma has a desktop MCP server that you can use with the Figma Desktop app, and a remote MCP server that is hosted by the Figma team for when you use Figma in your browser.

After setting up the Figma MCP server, you can integrate it with your favorite agentic tools like [VS Code](https://code.visualstudio.com/), [Claude Code](https://claude.com/product/claude-code), [Cursor](https://cursor.com/download), and [Windsurf](https://windsurf.com/). If you’re looking for a tool not covered in this collection, you can find the full catalog of supported tools in [Figma’s MCP catalog](https://www.figma.com/mcp-catalog). We also recommend that you check the documentation for the tool you’re using for the latest installation steps.

When prompting and writing code, these agentic tools are what generate the final code output, so you may find that some tools generate results closer to your vision than others. The Figma MCP server only sends the context and details of your design files—not any code.

When you’re ready to get started with Figma’s MCP server, you can check out our other lessons, or the Figma [developers documentation](https://developers.figma.com/docs/figma-mcp-server/), for step-by-step instructions on how to set up your MCP server in your favorite tools.

## How MCP improves workflows

After you set up the MCP server, you can do things like:

- Select a Figma frame and turn it into code with an agentic development tool.
- Pull in variables, components, and layout data directly into your prompt. This is especially useful for [design systems](https://help.figma.com/hc/en-us/articles/14552802134807) and component-based workflows.
- Gather code resources from Figma Make files and provide them to your agentic tools as context. This can help as you move from a prototype to a production-ready application.

## With Dev Mode and Code Connect

The Figma MCP server works even better when you connect your codebase to Figma with [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247) and [Code Connect](https://help.figma.com/hc/en-us/articles/23920389749655). Dev Mode is a developer-focused interface for inspecting and navigating designs. You can access Dev Mode from the toolbar. And Code Connect is the bridge that connects your component codebase to Dev Mode.

![720092c03c3c9ff23b8cf2827c2a195c4b262c46.gif](https://help.figma.com/hc/article_attachments/35818200570519)

After setting up Code Connect, you’ll be able to see real code that’s directly mapped to your codebase when inspecting them in Dev Mode. And with the Figma MCP server, your agentic development tools can generate code based on your designs and the connected codebase, making sure your code and design are always in sync.

For detailed instructions on how to set up Code Connect, check out our [developer documentation](https://developers.figma.com/docs/code-connect/code-connect-ui-setup/). And to learn more about Dev Mode, check out our [Intro to Dev Mode video on YouTube →](https://www.youtube.com/watch?v=__ABPkb0aF8&pp=ygUOZmlnbWEgZGV2IG1vZGU%3D)

## Wrap up

That’s it for this quick overview about what MCP is and how the Figma MCP server can…

- Bring the context of your design systems into your agentic development tools
- Use the Figma MCP server with Figma Make
- Boost your code output consistency through Code Connect while utilizing your existing design system components

Design systems can help your team design consistently at scale. Learn more about design systems in our [Introduction to design systems course →](https://help.figma.com/hc/en-us/articles/14552802134807)

If you’re excited to get started, check out our next lessons on how to setup the Figma MCP server for some of the most popular AI development tools like [Cursor](https://cursor.com/download), [VS Code](https://code.visualstudio.com/), and [Claude Code](https://claude.com/product/claude-code).

## Check your knowledge!
