---
기술지원명: Workflow lab: Code to canvas
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Workflow lab: Code to canvas
출처링크: https://help.figma.com/hc/en-us/articles/40219873508247-Workflow-lab-Code-to-canvas
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Overview

AI can help you build things faster than ever before. But speed alone doesn't guarantee you're building the right thing—one that solves real user problems, meets expectations, and delivers meaningful results. That's where design plays a critical role, and where Figma fits into agentic workflows.

This article explains key concepts like **agents**, **MCP**, **skills**, **write to canvas**, and walks through three workflows from the **May 2026 Release notes livestream** that show how agentic tools can accelerate the design and development process, starting from either code or the Figma canvas.

## Key concepts

#### What is an agent?

An **agent** is a software system that uses AI to pursue goals and complete tasks. In product development, agents can help plan projects, write code, interpret visuals, and orchestrate other agents to assist. Common examples include Cursor, Codex, and Claude Code.

#### What is MCP?

**MCP (Model Context Protocol)** is an open standard that defines how agents communicate with other software, like Figma. MCP servers allow agents to retrieve relevant context from external sources, helping them make better decisions and take more accurate next steps.

The **Figma MCP server** enables agents to:

- Translate code into Figma designs
- Create and manipulate designs on the canvas
- Translate designs back into code

This two-way bridge between design and code is what makes agentic coding with Figma so powerful.

#### Skills

A **skill** is a set of instructions an agent can learn and use to accomplish a task. Skills are stored as plain text files. Any repeatable task you'd otherwise re-prompt your agent to execute is a good candidate for a skill.

The skills featured in this article, including the one used in this workflow, are available on the [Figma Community skills page](https://figma.com/community/skills). Copy the GitHub link into your agent and ask it to download and install the skill.

#### Write to canvas

The `/figma-use` skill, also called **write to canvas**, lets an agent create and modify a real Figma design file using your existing components, variables, and styles. Like the skills in the workflows below, it comes pre-installed with Figma's MCP server.

## Set up MCP

You can connect the Figma MCP server in two ways:

- **Remote MCP server (preferred)**: Connects directly to Figma’s hosted endpoint at `https://mcp.figma.com/mcp`. [Learn how to install the remote MCP server.](https://help.figma.com/hc/en-us/articles/35281350665623)
- **Desktop MCP server**: Runs locally through the [Figma desktop app.](https://www.figma.com/downloads) [Learn how to install the desktop MCP server.](https://help.figma.com/hc/en-us/articles/35281186390679) The desktop MCP server is primarily for specific use cases for organizations and enterprises. For the broadest set of features, use the remote MCP server.

[Learn more about the Figma MCP server.](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server#h_01K25F7RBP00A3VH1733692QN2)

## Workflows

The following three workflows demonstrate how to use the Figma MCP server with agentic tools across different stages of design and development.

### Riff on vibe coded prototypes in Figma

If you've been building with AI-generated code and want to bring those interfaces into Figma, you can use the MCP server to capture your running UI as design layers on the Figma canvas. This lets you elevate rough, code-generated designs into something structured and editable, ready for refinement or handoff.

When to use this: Use this workflow when you have a working prototype in code and want to bring it into Figma design to review, iterate, or share with your team.

One emerging starting point for design teams is designing directly in code. This is often done in a prototype playground: a sandboxed environment with real code and screens from your production app, but in a low-stakes space where you can build, break, and tweak without affecting production code or final designs. If you don't have a prototype playground, that's fine, this workflow applies to anyone prototyping in code.

The goal of this workflow is to take a code-based prototype, bring it into Figma as editable design frames, and refine it on the canvas.

#### Step 1: Bring your prototype into Figma

Use the `/prototype-to-figma` skill to take a prototype running in your local environment and bring each unique screen onto the Figma canvas as a design frame connected to your design system.

To run the skill:

1. In your agent (for example, Cursor), type `/prototype-to-figma`.
2. Tell your agent to run the skill on the prototype running at your localhost URL.
3. Open your Figma file.

Each step in the prototype flow will appear on the canvas as a design frame, using your existing design system components and styles. The skill also generates a summary page and a styles page, so you have context about what was captured and why—not just the output, but the intent behind it.

**Note:** Make sure you’re running the latest version of the Figma MCP server.

#### Step 2: Review and refine on the canvas

Once your screens are in Figma, you can see the entire flow at once and evaluate it as a whole. A vibe-coded prototype is a solid starting point for validating an idea, but it often needs design refinement before it's ready for feedback or handoff.

Some things to look for during review:

- **Redundant UI elements:** For example, if a screen has both a step indicator and a progress bar, you likely only need one.
- **Opportunities to use design system components:** Replace ad-hoc elements with real components from your library—cards, buttons, layout primitives—to bring the design closer to your production standards.
- **Visual hierarchy:** Consider how illustrations, typography, and spacing can be used to create a clearer, more intentional composition.
- **Layout structure:** Adding auto layout to frames gives you a more accurate sense of spacing and helps the design scale correctly.

Iterating directly on the canvas, especially when co-designing with a teammate, is often faster than re-prompting your agent to make the same changes in code.

#### Step 3: Hand off or update the prototype

Once the design is refined, you have two options:

- **Share for feedback:** The design is now in a state that's ready to send to stakeholders or collaborators.
- **Push changes back to code:** Prompt your agent to update the prototype directly, using the refined Figma design as the source of truth.

#### Recap

In this workflow, you:

1. Started with a prototype built in code.
2. Used the `/prototype-to-figma` skill to bring all screens into Figma as a connected flow.
3. Refined the vibe-coded design on the canvas until it met your bar for craft.

### Connect design systems in code to design libraries in Figma

Keep your code and design in sync by linking your component codebase to your Figma design libraries. Using the MCP server alongside [Code Connect](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect), agents can pull in variables, components, and layout data from your Figma files directly into your development environment. This ensures the code your agent generates reflects your actual design system, not just the visual appearance of a design.

Note: When to use this: Use this workflow when you want your agentic tools to generate code that references real components and tokens from your design system.

Design systems let teams create consistent, cohesive experiences that scale. But when design work happens in code, like during a hack week, a quick experiment, or an AI-assisted sprint, those changes can end up stranded as real work that exists only in your codebase, disconnected from the design system in Figma.

This workflow shows how to bring a code-based design (along with its variables) onto the Figma canvas, evaluate and refine it, and push the updated tokens back to code. keeping design and development in sync.

#### Foundational skills

The `/figma-generate-design` and `/figma-generate-library` skills used in this workflow come pre-installed with Figma's MCP server. No manual installation is required.

#### Step 1: Bring your design and variables into Figma

If you've built out a new design direction in code, like a dark mode using color variables from your existing design system, you can use the pre-installed skills to capture it in Figma.

Run a prompt in your agent that calls the `/figma-generate-design` and `/figma-generate-library` skills.

This will:

- Place your screens on the Figma canvas (for example, light and dark mode side by side)
- Create a new variable collection in the variables panel that reflects the tokens used in your code

From here, you can evaluate the design at a glance and see how it holds up across screens, something that's difficult to assess when the design only exists in a running local environment.

#### Step 2: Evaluate and refine your variables

With your screens and variables on the canvas, review the design for issues that are hard to catch in code alone. Common things to look for:

- **Color intensity:** Brand accent colors that work well in light mode can appear overly saturated or neon in dark mode. Consider swapping to a different hue or tone from your palette that feels more balanced.
- **Text contrast:** Low-contrast text, particularly secondary labels like dates or captions, may not meet accessibility standards. If your team targets WCAG AAA, check these values carefully.

To make adjustments, open the variables panel and update the relevant tokens directly. Changes are reflected in real time across all components and style references on the canvas, giving you a clear birds-eye view of how token decisions affect the full design.

Tip: Seeing variables and their effects simultaneously, rather than updating a value in code and refreshing a browser, makes iteration significantly faster.

#### Step 3: Push refined tokens back to code

Once your variables are in a good place, prompt your agent to update the design system in your codebase with the refined tokens. This keeps your code and Figma files in sync, with Figma as the source of truth for design decisions.

#### Recap

In this workflow, you:

1. Used the `/figma-generate-design` and `/figma-generate-library` skills to bring a code-based design and its variables onto the Figma canvas.
2. Evaluated the design across screens and identified issues with color and accessibility.
3. Refined variable values directly in Figma, with changes reflected in real time.
4. Pushed the updated tokens back to code to keep design and development in sync.

The agent handled the tedious mapping work. The canvas made the design decisions faster and easier to get right.

### Go wide and deep with AI, right from Figma

Already have designs in Figma and want to explore new ideas? You can use an agent to generate alternative directions directly on the canvas, using your existing components, variables, and styles. Rather than starting from scratch, the agent builds with your real design system assets to produce new screens and variations.

Note: When to use this: Use this workflow when you want to rapidly explore or iterate on existing designs without leaving Figma.

For many teams, Figma is the source of truth. Designs already exist on the canvas and the challenge isn't starting from scratch, it's knowing how to move forward. When user research surfaces a problem with an existing screen, the hardest part of iteration is often making that first move.

This workflow shows how to use an agent to generate a rough starting direction using your real components, so you can react to something concrete and refine it on the canvas.

#### Step 1: Define the problem

Start with a clear problem statement, grounded in research or user feedback. The more specific your prompt, the more useful the agent's output will be.

For example: a customer revenue dashboard where renewal health is displayed as a plain text label at the end of each row. Research shows users miss it. The problem to solve is making renewal health more prominent and easier to act on.

There are often many valid approaches to a problem like this, like color coding, grouping rows by status, or introducing a new visual hierarchy. Seeing directions on the canvas is what moves the conversation forward.

#### Step 2: Generate a starting direction with the agent

In your agent, run the `/figma-use` skill. Include relevant context in your prompt, like user research insights, the specific problem, and any constraints, then ask the agent to explore an approach using your existing components.

The agent will produce a rough iteration directly on the canvas, built with your production components.

Note: The goal at this stage isn't a finished design. It's a concrete starting point you can react to and refine.

#### Step 3: Refine on the canvas

Review what the agent produced and use it as a starting point. A few things to evaluate:

- **Does the solution change the organizing principle of the layout?** Grouping or prioritizing information differently can make critical data the first thing a user sees, rather than something they have to scan for.
- **Are the right components being used?** The agent should be pulling from your design system. If it isn't, adjust your prompt or swap components manually.
- **What's working and what isn't?** React to what's in front of you. The agent gets you past the blank page; you and your team bring the design judgment.

Iterating directly on the canvas instead of re-prompting repeatedly lets you move from abstract discussion to specific, visible decisions quickly.

#### Recap

In this workflow, you:

1. Identified a design problem grounded in user research.
2. Used the `/figma-use` skill to generate a rough direction on the canvas using real production components.
3. Reacted to the output and refined it collaboratively, arriving at a stronger solution faster than starting from scratch.

### Putting it all together

Across all three workflows, the same pattern holds: whether you're starting in code or starting on the canvas, the agent handles the scaffolding. You spend your time on the work that requires a designer's eye.

| Workflow | Starting point | Key skill | Outcome |
| --- | --- | --- | --- |
| 1. Code to canvas | Prototype in code | `/prototype-to-figma` | Screens imported as design frames, ready to refine |
| 2. Design system sync | Dark mode built in code | `/figma-generate-design`, `/figma-generate-library` | Variables and screens in Figma, tokens pushed back to code |
| 3. Canvas exploration | Existing Figma design | `/figma-use` | Agent-generated direction using real components, refined on canvas |

## Keep learning

- [Get started with the Figma MCP server](https://help.figma.com/hc/en-us/articles/39216419318551)
- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Figma skills for MCP](https://help.figma.com/hc/en-us/articles/39166810751895)
- [Set up Code Connect](https://help.figma.com/hc/en-us/articles/14606897474647)
