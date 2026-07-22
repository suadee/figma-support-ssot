---
기술지원명: AI workflows collection: Cut down on busywork
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Cut down on busywork
출처링크: https://help.figma.com/hc/en-us/articles/41159765402007-AI-workflows-collection-Cut-down-on-busywork
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

Rachel is starting to wrap work on Cheddar’s weekly insights screen. The hard decisions are behind her and she's happy with the layouts, the hierarchy, and the edge cases. It's time to start cleaning up so the developers at Cheddar have a clear path to implementation.

As she starts diving in, Rachel spots lots of things she'll need to update. Those one-off components, a few color experiments detached from the existing variables, placeholder copy that doesn't communicate intent super well, and hidden layers galore.

Each of these things is relatively easy to fix, but she'd much rather spend the time working on the next design problem.

Design work tends to leave a trail of loose ends behind it—a natural side effect of moving fast while shaping the work into something great.

When the time comes for cleanup, files can contain a bunch of extra work that has piled up behind the scenes. None of it is especially hard to fix, but it quietly drains time and attention away from the work only you can do.

We’ve heard from designers that leaning on the agent for some of this busywork is one of the most satisfying use cases in design workflows. We hope it helps you, too!

## Make bulk edits

Bulk edits and cleanup tasks tend to be tedious not because they're hard, but because there are a lot of them and they're spread across the file. The agent is good at finding everything that matches a condition and acting on all of it at once.

**Example prompts**

- Find every text layer in the insights screen that's using a hardcoded font size rather than a text style variable
- Generate color variables from all colors in this design, organized into semantic groups
- Select all layers with text larger than 14 but smaller than 20 and change the typeface to Cheddar's primary sans-serif
- Select all layers using a serif font and change them to Cheddar's primary typeface
- Set all spending category chip components to their active state
- Delete all invisible layers across the weekly insights screen frames
- Apply auto layout to all nested frames in the category breakdown section
- Replace all instances of the insight summary card in this grid with the "Insight Card / Default" component created in this file
- Remove all shadow styles from the transaction list rows
- Remove all corner radii from the container frames — keep them on the cards and interactive elements
- Create a dark mode variable mode using Cheddar's color scale and apply it to this design

## **Populate realistic content**

It can feel hard to evaluate a design with placeholder copy that doesn't communicate intent and empty image slots that make it hard to evaluate hierarchy. You can ask the agent to fill these in quickly.

**Example prompts**

- Fill these insight cards with realistic weekly spending totals and category breakdowns
- Add realistic merchant names and transaction amounts to this transactions list
- Generate realistic weekly spending data for this insights dashboard — a typical week for someone slightly over budget on food and dining out
- Add a "you've unlocked a new insight" nudge card to this weekly summary for a user who hit a new savings milestone
- Add realistic spending category labels and icons to the empty category breakdown frame
- Add 3 more transactions to this list — include at least one recurring subscription or utility bill
- Replace all the content in this weekly summary with data for a different week — one where the user came in under budget across all categories
