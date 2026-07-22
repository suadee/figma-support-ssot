---
기술지원명: Best practices for optimizing AI credits in Figma Make
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Best practices for optimizing AI credits in Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/40097793879191-Best-practices-for-optimizing-AI-credits-in-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

AI credits in Figma Make are consumed each time you send a prompt, and the amount varies based on factors such as the model you use, the complexity of the task, and the volume of context the model processes to complete the task.

The practices in this article are not always about minimizing the number of credits used on each individual prompt. Instead, the goal is to help you avoid spending credits on rework. Some upfront investments, like building a reusable template or setting up a guidelines file, may cost more credits initially but tend to reduce overall spend over time by helping you get better results with fewer corrections.

For a full overview of how credits are consumed by feature, see [How AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015). To understand how to purchase additional AI credits for your team, see [Manage AI credits](https://help.figma.com/hc/en-us/articles/35865276858647).

## Key moments that affect credit consumption

Not all prompts carry the same cost. In practice, a handful of high-impact moments in a Make session account for most credit inefficiencies. A few of these moments to keep an eye out for are:

- **An unscoped first prompt**: When a first prompt is too vague or incomplete, follow-up prompts may cost more credits that a clearer starting point would have avoided. The first prompt sets the direction for everything that follows.
- **The wrong model for the job**: Using a heavier model than the task requires costs more than necessary. Match your task to the most appropriate model at hand.
- **A long prompt history**: As prompt history accumulates in a file, Make has more context to process on every prompt, even if the prompt itself is simple. Start fresh when you no longer need old context.

The sections below cover these patterns and additional optimizations in more detail.

## Before your credit session

### Check your credit balance

Before starting a Make session, check how many credits you have remaining and when they will reset. Knowing your credit balance before you start can help you make more deliberate choices, like which model to use, or when to invest in a reusable foundation that will pay off in future sessions.

To check your AI credit balance:

1. Open a file where you have edit access.
2. Open the  **Main menu** of the file.
3. Select **AI balance** to see how many credits you’ve used, how many remain, and when they reset.

[Learn more about tracking your individual credit usage](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work#trackusage).

### Start from a strong foundation

One of the most effective ways to optimize credit spend over time is to avoid rebuilding the same foundation repeatedly. The right starting point depends on how much setup you want to invest and what you’re building.

**Note**: Some options, like setting up a Make kit or publishing a template, require more credits upfront. This initial investment can pay off later as you and your teammates reuse the base, rather than generating the same foundation from scratch each time.

#### Make kits

Make kits are building blocks for any Make project. Each kit bundles an npm package, a Figma library, and a guidelines file—giving Make consistent design system context from the first prompt. Make kits provide a comprehensive starting point, especially for teams starting with an established system.

[Learn more about getting started with Make kits](https://help.figma.com/hc/en-us/articles/39241689698839).

#### Set up a guidelines file

A guidelines file (guidelines.md) is one of the most impactful changes you can make to your Make workflow. Guidelines are a part of Make kits, but you can also use guidelines on their own, as a part of any Make file.

When present, Make reads it automatically as part of its context on every prompt—so you don't have to re-state standing instructions each time.

A good guidelines file can cover:

- How to use your design system
- Naming conventions and patterns to follow
- Quality standards to aim for
- Where to find the right source of truth for common decisions

**Tip**: You can ask Make to draft a guidelines file for you—but keep in mind that generating or revising guidelines uses AI credits. Once you have a solid guidelines file, edit it directly rather than regenerating it each session.

Tips for structuring your guidelines file:

- **Use a parent file with smaller supporting files**. Rather than one large file, create a primary guidelines file that points to smaller, task-specific .md files. This keeps context targeted to what a given task actually needs.
- **Remove redundancy**. If context is already covered by your npm package, Figma library, or another context source, don’t repeat it in guidelines. Redundant context increases credit usage without adding value.
- **Ask the model to review your file**. Ask Make to critique your guidelines file—it can often identify redundancy, inconsistent naming, or vague instructions that make it work harder than necessary.

[Learn more about setting up guidelines files](https://help.figma.com/hc/en-us/articles/33665861260823).

#### Templates

Templates are specific Make files you publish so teammates can remix them. When you’ve built something worth reusing (such as a hero screen, a common flow, or a well-structured starting point), publish it as a template. Teammates can then start from a working build rather than from scratch.

[Learn more about Make templates](https://help.figma.com/hc/en-us/articles/34716344138519).

#### Duplicate existing files

When you want to explore a variation or build on an existing Make file, duplicate the file rather than starting a new one. Duplicating costs no additional credits, and is the fastest way to get a clean starting point without losing your current build state.

[Learn more about duplicating files](https://help.figma.com/hc/en-us/articles/360038511533).

## During your session

### Have a clearly defined first prompt

The first prompt acts as the brief your Make session works from. The more clearly it defines the scope, constraints, and end state you’re after, the less you’ll need to cover in follow-ups.

Every prompt costs credits, including the ones you send to fix a previous result. The most reliable way to reduce rework is to front-load your intent: clearer initial prompts mean fewer corrections.

Tip: For complex tasks where it's hard to scope your intent upfront, consider using plan mode. Plan mode generates a structured plan.md before any code is written. While plan mode uses additional credits up front, the cost is often far less than the cost of a build that needs to be corrected mid-way or started over. [Learn more about plan mode](https://help.figma.com/hc/en-us/articles/40830441709719).

For prompting techniques and examples, see [**Prompting best practices**](https://help.figma.com/hc/en-us/articles/31304485164695-Create-and-edit-a-Figma-Make-file#h_01JTEVBJ06KJ71H0XYVT2533YR).

### Use point-and-edit and direct code edits for small changes

Not every change requires a prompt. For small visual adjustments, bypassing the model entirely is faster and more credit-efficient.

**Point-and-edit** lets you select an element in the preview and make targeted adjustments using the toolbar or a focused prompt. Use it for visual properties like color, corner radius, spacing, and typography.

[](https://help.figma.com/hc/article_attachments/40107581951895)

[Learn more about point and edit](https://help.figma.com/hc/en-us/articles/31304485164695-Create-and-edit-a-Figma-Make-file#h_01JTEVBJ0527WJSQ40FDX87CRH).

**Direct code edits** are useful when you need to change something dynamic that isn’t easily accessible in the preview. Use **Code** to jump to the relevant code, then use cmd+F (Mac) or Ctrl+F (Windows) to find the specific element.

[](https://help.figma.com/hc/article_attachments/40107581952791)

[Learn more about direct code edits](https://help.figma.com/hc/en-us/articles/33649966245783-Edit-the-code-of-a-functional-prototype-or-web-app).

### Choose the right model for the task

Figma Make offers several models, and the one you use has an impact on both credit consumption and output. Consider what your overall goal is and how much detail it requires. You should consider which model to use on the task-level, and not necessarily on a prompt-by-prompt basis.

- **Auto (default)**: A useful starting point for most tasks if you’re unsure which model to select. Auto model selection balances quality and cost across a range of task types.
- **Claude Opus**: Best suited to complex tasks or when you’re building something that requires exactness—such as a detailed replica of an existing design, or other complex designs or functionality.
- **Gemini Flash**: Well suited to minor styling adjustments, quick iterations, and making targeted changes. The most credit-efficient option for straightforward tasks.

[Learn more about switching models in Figma Make](https://help.figma.com/hc/en-us/articles/36400680326551).

### Scope your context carefully

More context isn't always better. Every piece of context Make processes costs credits—including context that doesn't improve the output.

#### Frames vs. screenshots

Figma design frames carry precise metadata and are valuable for fidelity work. When working within your file, pointing to frames gives AI Assistant richer context to work from.

For tasks where pixel-perfect accuracy isn't required, a screenshot or annotated image is lighter and often just as effective.

#### Npm package vs. Figma library

These serve different purposes: npm packages provide component-level context; Figma libraries provide styling context. You often only need one. Use your guidelines file to explain how Make should apply whichever source you've chosen.

#### MCP connectors

Connectors give Make access to external tools like Notion, Linear, or Atlassian. When using them, point to the specific document, ticket, or file that's relevant—not a broad endpoint or workspace search. If you only need a short excerpt, paste it directly into the prompt instead of sending Make to retrieve it.

[Learn more about connectors in Figma Make](https://help.figma.com/hc/en-us/articles/35440096186007).

#### Avoid redundancy

If the same information exists in your guidelines file, your npm package, and your prompt, Make processes all three. Check that context isn't duplicated across sources before sending.

## Over time

Prompt history accumulates within a single Figma Make file. Over time, Make has more and more prior context to consider on each new turn—and that increases credit consumption per prompt, even for simple requests.

Signs it may be time to start fresh:

- You’re many prompts deep and the project scope has shifted significantly
- Simple prompts are consuming unexpectedly high credits
- You want to explore a meaningfully different direction from your current build

There are a few ways you can clear up your prompt history:

- **Duplicate the file**. Duplicating creates a new file with a clean prompt history while preserving the current state of your build.
- **Turn the project into a template**. If you want others to build on this foundation, save it as a template. This packages up the build state for reuse without the accumulated prompt history, and gives teammates a strong starting point.
- **Clear chat context.** Clearing your prompt history removes accumulated context, allowing you to keep building without re-processing history that's no longer relevant. Your files remain intact and your chat history is still viewable, but Make will not remember any chat history or context added from before you took the action to clear. [Learn more about clearing chat context](https://help.figma.com/hc/en-us/articles/39893099629975-Clear-chat-context-in-Figma-Make).

## Related resources

- [Learn more about working in Figma Make](https://help.figma.com/hc/en-us/categories/31304285531543-Figma-Make)
- [How AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015)
- [Manage AI credits](https://help.figma.com/hc/en-us/articles/35865276858647)
