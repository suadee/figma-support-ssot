---
기술지원명: Use plan mode in Figma Make
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Use plan mode in Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/40830441709719-Use-plan-mode-in-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on paid plans

Plan mode is an optional mode in Figma Make that helps you clarify your intent and create a structured plan before generation starts. Make analyzes your project and generates a plan you can review and refine before any code is written or files are changed.

## Turn on plan mode

You can switch on plan mode in two ways:

- In the prompt box, click the mode dropdown and select **Plan**.
- Type `/plan` in the chat

![Select plan mode or build mode from the dropdown in the chat window.](https://help.figma.com/hc/article_attachments/40937071492375)

To switch back to build mode, click the mode dropdown in the prompt box and select **Build.**

**Note**: At this time, plan mode is only available when using the default model or Claude Opus 4.7. It is not available on Gemini models.

## How to use plan mode

For best results, use plan mode on the first turn of a conversation, before any code has been generated. You can still switch to plan mode mid-session, but starting fresh gives Make the clearest view of what you're trying to build.

Plan mode works best for complex tasks where getting aligned before building tends to produce better results. For example, if you're building a multi-section layout, working from a detailed spec, or importing a Figma design you want to translate closely, a plan helps Make understand the scope before it starts generating.

**Note**: Plan mode usually helps produce higher quality results for larger, more complex tasks, but consumes more AI credits than build mode. If you only need to make small or quick changes, stick with build mode.

[Learn more about how AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work).

### Explore and clarify

When you activate plan mode, Make reads your project to understand what you're working with. This can include your existing code, any attached designs, and the context from your prompt.

You can add context or attach Figma designs at this stage.

### Generate and refine

Once it has what it needs, Make generates a structured plan in real time. The plan appears in the chat and creates a plan markdown file, which opens automatically when the plan is ready.

Before anything gets built, you can edit the plan until it looks right:

- Open `plan.md` to adjust the structure, add details, or remove sections
- Continue the conversation in the chat to ask Make to revise the plan

There's no limit to how many times you can refine before approving.

### Approve and build

When the plan looks right, click **Build** in the chat. Make will execute the plan and begin generating code for your project.

![After finalizing the plan, click Build to start generating the code.](https://help.figma.com/hc/article_attachments/40937026713495)
