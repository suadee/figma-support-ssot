---
기술지원명: Use skills with the Figma MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Use skills with the Figma MCP server
출처링크: https://help.figma.com/hc/en-us/articles/39287396773399-Use-skills-with-the-Figma-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

After you've [set up the Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/#enabling-the-remote-mcp-server), you can start using MCP skills to help your agent complete more specific workflows. Skills give your MCP client extra guidance for tasks that may take multiple steps, require the right order of operations, or depend on following consistent conventions. They can help reduce the amount of prompting you need for common workflows and make your results more reliable over time.

## Before you begin

Before you get started with skills you'll need to make sure:

- Your MCP client is supported
- You've set up the remote Figma MCP server
- You have access to the Figma skills

If your agentic tool supports plugins and you followed the steps to set up the remote Figma MCP server, you should already have the Figma skills installed. If your agentic tool doesn't support plugins, you'll need to download the skills.

To check if you have access to the Figma skills, try to type a `/`. For many agentic tools, this is an easy way to list the skills you have installed. You can also ask your agent: "What Figma skills do I have installed?"

To learn more about the MCP skills provided by Figma and how to get them, see [Figma skills for MCP](https://help.figma.com/hc/en-us/articles/39166810751895).

## Try out skills

The fastest way to get comfortable with skills is to try one directly. Figma provides some helpful skills that support common design use cases. Check out the [full list of skills here](https://help.figma.com/hc/en-us/articles/39166810751895).

In clients that support direct invocation, you can usually type `/` followed by the skill name and a short request. For example:

- `/figma-use Create a new page called "Skill test" and add a simple pricing card with a title, three feature rows, and a primary button using auto layout.`
- `/figma-generate-design Use my design system to create a mobile account settings screen with profile, notifications, and security sections.`
- `/figma-generate-library Create a starter component library with buttons, inputs, and badges, each with size and state variants.`

These examples are intentionally simple. They're a good way to confirm that a skill is installed, that your MCP client can invoke it, and that the client can follow the workflow the skill defines.

If your client doesn't use slash commands, you can usually ask for the same outcome in plain language and let the client decide whether to apply a relevant skill automatically.

For a deeper dive into skills, keep reading!

## What is a skill?

A skill is a predefined, reusable set of markdown instructions and supporting files (scripts, assets, and other data) that teaches an MCP client how to complete a specific task. Instead of relying on a single prompt alone, a skill gives the client more structure about what to do, what context to gather, and what steps to follow. This is especially useful for workflows that are too detailed or repetitive to explain from scratch every time.

In practice, skills can help your MCP client work more consistently with your Figma files and design systems. For example, a skill might help the client implement a design, create a new file, build a library, or follow a more specific process for working with components and variables. Since skills are reusable, they can help teams package best practices into something an agent can apply again and again.

## What's the difference between skills and tools?

Skills and tools work together, but they are not the same thing.

A **tool** is a capability your MCP client can use. With the Figma MCP server, tools let the client access information from a Figma file or take actions using that connected context. Tools are the building blocks that make work possible.

A **skill** is a set of instructions and supporting context like scripts and assets that tell a client how to use one or more tools to complete a larger workflow. In other words, tools are what the client can do, while skills help explain how and when to do it.

If a tool is like having access to a specific function, a skill is more like having a proven workflow for using that function well.

Let's compare the differences between tools and skills in a real life scenario.

If you want to design a card inside a Figma Design file using only tools, you'll have to give specific instructions like "Create a 240x160 frame" or "Set paddings to 16" in your prompts.

On the other hand, if you have a predefined skill for card creation workflow, you can simply enter "Create a card in Figma" in your prompt and your agent will know what steps and requirements are needed to create a card. A skill can help speed up your code generation while making sure it's following the design system or patterns.

## How to use a skill in prompts

If your agentic tool supports skills, it may automatically apply a relevant skill when your prompt matches that skill's description. This means you can often just describe what you want to do in plain language. For example, you might ask your client to implement a screen from a Figma file, create a new design file, or use a design system workflow. If the request matches an installed skill, the client can load that skill and follow its instructions while working through the task.

This approach is useful when you want the interaction to feel natural and conversational. Instead of remembering the exact name of a skill, you can focus on the outcome you want. Your MCP client can then decide whether a skill is relevant based on the request and the skill's description.

## How to invoke a skill directly

Some MCP clients also let you invoke a skill directly.

In clients that support direct invocation, you can usually type `/` followed by the skill name to explicitly call that skill. This is helpful when you already know which skill you want to use and want to be more specific about the workflow the client should follow. Direct invocation can also be useful for testing that a skill is installed and working as expected.

Keep in mind that the exact way skills are invoked can vary depending on the MCP client you're using. Some clients treat skills as slash commands, while others may surface them in a skills menu or apply them automatically based on the conversation. If you're not sure, check the setup instructions for your specific client.

## Wrap up

MCP skills help your client go beyond individual tool calls by adding reusable instructions for more complex workflows. They make it easier to work consistently, reduce repetitive prompting, and help your agent use the right steps for the job. Whether you use them through normal conversation or invoke them directly, skills can help you get more reliable results when working with the Figma MCP server.

## Check your knowledge!
