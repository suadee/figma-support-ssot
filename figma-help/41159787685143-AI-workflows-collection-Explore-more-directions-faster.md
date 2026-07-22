---
기술지원명: AI workflows collection: Explore more directions, faster
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Explore more directions, faster
출처링크: https://help.figma.com/hc/en-us/articles/41159787685143-AI-workflows-collection-Explore-more-directions-faster
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

Rachel is three days into designing a new feature for Cheddar, a budgeting app. The brief is clear: build a weekly insights screen that keeps users coming back after week two, when most of them drop off.

She has a direction she's been exploring. The layout is clean and the hierarchy makes sense. But something is nagging at her. She's been iterating the same structure since day one, and she's not sure it's actually going to solve the retention problem.

Going back to explore other approaches feels like losing ground...but she also has a design review in two days!

Design education puts a lot of emphasis on **divergent thinking**. The underlying insight is that your first idea is almost never your best one, and committing too early means missing the chance to explore options you haven't thought of yet.

As Rachel's story shows, time pressure can collapse that process in professional practice. It's hard to give time and space to explore alternatives on the canvas when everything is moving so quickly.

Bringing AI into your workflow can help you open up the solution space on the canvas and explore more possibilities to a particular design problem. It can help you spark ideas, get inspired, and consider fresh alternatives that you can build upon.

Here are three best practices for working with AI to explore more directions, faster.

1. [Write detailed prompts that embrace divergent thinking](#h_01KVPN11P0GXN6977ZVPN325FV)
2. [Connect your design system to ground AI outputs](#h_01KVPN11P0TVPTQEVTRCSJ2P8Y)
3. [Add additional context](#h_01KVPN11P0RGJJQJGE1PJ836FR)

## 1. Write detailed prompts that embrace divergent thinking

![image (1).png](https://help.figma.com/hc/article_attachments/41390624904855)

The more detail you give in your prompts, the more relevant and actionable the outputs will be. This helps you avoid generic concepts and generate directions you can actually build upon.

**Tip**: When prompting, imagine explaining the design problem to a fellow designer who is hearing about it for the first time. What would you say to help them understand what you're working on?

You don’t need to capture every detail, but it helps to check whether your prompt includes some of the following elements:

- **Ask for more than one generation** and **push for divergence**. Using words like ‘distinct’ or ‘completely different’ encourages the agent to broaden its scope.
- **Tell the agent what kind of variance you’re after**, whether that's layout, information architecture, or style.
- **Select the right context before prompting:** a single screen, a component instance from your library, or nothing—each produces different output.
- **Include the goal**, not just the task. ‘Increase two-week retention’ is stronger than ‘design a weekly insights screen’.
- **Add the constraint** or tension that makes the problem interesting, like ‘…where most users drop off because they don't feel a sense of progress’.

### Check your knowledge

## 2. Connect your design system to ground AI outputs

By grounding the agent with your existing design system, you can push it towards outputs that better reflect your brand.

Compare the below examples from the same prompt: “I’m designing a Weekly Insights screen for a budgeting app to increase 2+ week retention, where most users drop off because they don’t feel a sense of progress. Generate 3 distinct design directions that motivate users to come back.”

One output was connected to a design system, and the other one wasn’t. Can you guess which is which?

![image (2).png](https://help.figma.com/hc/article_attachments/41390624904983)

**Tip**: If there are specific parts of the design system you want the agent to use, you can mention them in conversation.

**Tip**: If you don’t have an existing design system to work from, [custom skills](https://help.figma.com/hc/en-us/articles/41159668700311) can offer a shortcut to encoding repeatable style intent without having to connect a library.

Skills let you package a workflow or context into a reusable set of instructions for an AI agent. Instead of rewriting long prompts and re-explaining conventions each time, a skill gives a design agent a stable sequence of steps to follow, which improves consistency across runs. You can even create a skill from the design properties of a single screen.

**Example:**

```
Use Neobrutalism
---
name: use-neobrutalism
description: Apply a bold neobrutalist aesthetic using high contrast, chunky shapes, hard edges, loud colors, and raw layouts.
---

Create or revise designs using a neobrutalist visual style: bold, playful, direct, and intentionally unpolished.

Use chunky geometric shapes, thick black borders, hard shadows, flat color fills, oversized type, and simple grid-based layouts. Favor high-contrast color combinations such as black, white, neon yellow, hot pink, electric blue, lime, and red. Avoid subtle gradients, glassmorphism, delicate shadows, muted palettes, and overly polished corporate styling.

Design directives:
- Use thick 3–6px borders, usually black.
- Use hard offset shadows, such as 6px 6px 0 #000000.
- Prefer square or lightly rounded corners, 0–8px radius.
- Use oversized headings and blunt, direct copy.
- Keep layouts simple, loud, and easy to scan.
- Layer cards, stickers, callouts, and buttons like physical cutouts.
- Embrace asymmetry, intentional awkwardness, and playful imbalance.
- Make interactive elements feel tactile, obvious, and slightly exaggerated.
```

[Learn more about creating reusable skills to use in design workflows.](https://help.figma.com/hc/en-us/articles/41159668700311)

## 3. Add additional context

The agent can also work with context beyond the canvas. Attaching files, connecting external tools, and pulling in web content gives it more to work from and gets you closer to outputs that reflect the specifics of your design challenge.

- [Attach files and other designs](https://help.figma.com/hc/en-us/articles/31304529835671): Attach different file types to provide additional context, data, or reference material.
- [Use MCP connectors to connect to third party tools:](https://help.figma.com/hc/en-us/articles/35440096186007) Connect to external tools via the Model Context Protocol (MCP), so you can use documents, tasks, and data from other apps as context.
- [Give the agent URLs or ask it to search the web](https://help.figma.com/hc/en-us/articles/39715554287255): Search the web and fetch content from URLs to ground your designs in real-world, up-to-date information.
