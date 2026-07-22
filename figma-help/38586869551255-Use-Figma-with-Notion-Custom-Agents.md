---
기술지원명: Use Figma with Notion Custom Agents
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Use Figma with Notion Custom Agents
출처링크: https://help.figma.com/hc/en-us/articles/38586869551255-Use-Figma-with-Notion-Custom-Agents
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on all Figma plans

You must be on Notion’s Business or Enterprise plan to use Custom Agents

You can connect Figma to Notion Custom Agents to bring FigJam into your automated workflows.

When connected to Figma, a Notion Custom Agent can generate a structured FigJam diagram from Notion content, or turn FigJam boards into documentation inside Notion.

This integration currently supports FigJam. You can’t use this integration to create files for Figma’s other products.

## Connect Figma to a Notion Custom Agent

To use Figma with Custom Agents, you’ll need to connect your Figma account inside Notion.

To connect Figma to a Custom Agent:

1. Open Notion on desktop or web.
2. Navigate to **Agents** in the left sidebar.
3. [Create a new Custom Agent](https://www.notion.com/help/custom-agent) or open an existing one.
4. Open **Settings**.
5. In the **Tools & Access** section, select **Add connection**.
6. Follow the authentication prompts to grant Notion access to your Figma account.
7. Save your Agent.

Tip: Need help getting started? Check out Figma’s example [Custom Agent from the Notion Marketplace](https://www.notion.com/@figma). Copy the template into your workspace to use it as a starting point.

## Generate FigJam diagrams from Notion

Once connected, your Custom Agent can create FigJam diagrams using your Notion content as context.

To generate a diagram:

1. Open your Custom Agent.
2. In the chat section, describe the diagram or what you want to visualize. Reference specific pages or databases that the Agent has permission to access.

Note: The Agent can only access Notion content [you’ve explicitly granted permission to use](https://www.notion.com/help/custom-agent#connect-notion-web-and-external-apps).

**Example prompts:**

- “Create a flowchart in FigJam based on this product requirements document.”
- “Generate a Gantt chart from our roadmap database.”
- “Turn this weekly update page into a structured project diagram in FigJam.”

The generated file is designed to be a structured starting point. You can continue refining layout, content, and visuals directly in FigJam.

### Open and edit the file in FigJam

When a Custom Agent generates a FigJam diagram, it creates a new FigJam file in your Figma account. The Custom Agent provides you a link to the file. Click the link to open the file.

- If you’re signed in, the file appears in your drafts or selected team.
- If you’re not signed in, you’ll be prompted to log in or create a Figma account.

Files that haven’t been claimed are public and viewable by anyone with the link. Once you log in, sign up, or add the file to your drafts, it becomes private to you.

Once created, the file behaves like any other FigJam file—you can edit content, collaborate with teammates, and share it.

**Note:** We recommend using FigJam on desktop (app or browser). Editing isn’t supported on mobile.

## Bring FigJam context into Notion

You can also use a Custom Agent to convert structured FigJam boards into Notion pages or database entries.

To convert a FigJam file:

1. Open your Custom Agent.
2. Prompt the Agent to summarize or transform a FigJam board.

**Example prompts:**

- “Summarize this FigJam board and create a Notion doc with key decisions and action items.”
- “Add the tasks from this FigJam board into our sprint planning database.”
- “Turn this brainstorming board into a structured project brief.”
