---
기술지원명: AI workflows collection: Bonus: Turn designs into prototypes (and prototypes into designs)
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Bonus: Turn designs into prototypes (and prototypes into designs)
출처링크: https://help.figma.com/hc/en-us/articles/41159751397783-AI-workflows-collection-Bonus-Turn-designs-into-prototypes-and-prototypes-into-designs
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

![](https://help.figma.com/hc/article_attachments/41416796132759)

**Story time!**

Rachel is working on a new chat feature in Cheddar, the budgeting app.

When someone asks about their spending, Cheddar can return a breakdown by category and suggest useful follow-up questions.

The static designs are in a good place, but Rachel is still unsure about the interactions. Should the breakdown expand inside the chat thread or open into a focused view? Should suggested questions appear right away or change based on the category someone taps? The ideas make sense in her head, but she wants to try them in context before committing.

She needs something she can click through, adjust, and bring back to the canvas before she feels she can commit to an approach.

There's a ceiling to what you can learn from looking at static frames on the canvas. It might be a whole screen or series of screens you want to validate—or a single component or micro-interaction you want to play with. Either way, the only way to know if something works is to try it out.

In this article, we're going to explore how designs can go through a roundtrip journey from design to prototype and back again using Figma Design and the agent in Figma Make.

**Tip:** At Config 2026 in June, we announced [code layers in Figma Design](https://www.figma.com/blog/config-2026-recap/#code-on-the-canvas). This feature streamlines the roundtripping journey from design to code and back again, and we’ll update this article as soon as it launches!

## Take your design into Figma Make

There are two main ways to get a design into Figma Make.

Send to MakeAttach a design

![](https://help.figma.com/hc/article_attachments/41416833393559)

Use **Send to Make** when you don't have an existing Make
file and
want to kick off a new prototype using the current selection on the canvas.

![](https://help.figma.com/hc/article_attachments/41416833393687)

Start by
[attaching your design](https://help.figma.com/hc/en-us/articles/31304529835671)
to a Make prompt. You can do this in a fresh Figma Make file, or one
you've been
working on for a while.

The easiest way is to copy frames directly from your design file and
paste them
into the prompt box.

**Tip**: If available, you can also start from a [template](https://help.figma.com/hc/en-us/articles/34716344138519%5D). Templates let your remix an existing Make file, including the interactions, states, and any Make kit that was applied, so you can pick up where someone left off.

## Add more context to your designs

Once your design is attached to a Make prompt, you can add more context to the prototype.

### Apply a Make kit

![](https://help.figma.com/hc/article_attachments/41416833393943)

A [Make kit](https://help.figma.com/hc/en-us/articles/39241689698839) bundles your design system — npm packages, library styles, and usage guidelines — so Make builds using your actual components and tokens. Without it, Make falls back on generic web defaults. Your first output will be closer if the kit is in place from the start.

If your team has published one, select it before prompting.

### Connect external context

![](https://help.figma.com/hc/article_attachments/41416833394455)

If the component ties back to a spec or PRD, connect the relevant source using an [MCP connector](https://help.figma.com/hc/en-us/articles/35440096186007). Paste a Notion link and tell Make to use it as the brief — if the spec updates, run the connector again and Make will incorporate the changes. The Figma Make connector library includes Notion, Jira, Confluence, Linear, and others. You can also [create a custom connector](https://help.figma.com/hc/en-us/articles/38147204302743) to connect any MCP server your team runs.

## Keep iterating

Once the initial build lands, keep prompting. Ask for specific interactions, edge states, loading behavior. Make remembers what you've attached, so you can build on it step by step rather than re-explaining the design each time.

**How’s the interaction looking?**

[](https://help.figma.com/hc/article_attachments/41416784913431)

Working through an interaction in Make tends to surface things that don't show up in static frames. For example, an edge state you hadn't designed for or a transition that feels off at real speed.

In this case, Rachel’s been inspired by the auto-suggestions that pop up above the chat box. She’d like to explore that idea a bit more on the canvas.

## Bring it back to design

When you're ready to take something from the prototype back into Figma Design, you have two options depending on what you need to do with it.

Copy as design layersEmbed the live prototype

[
](https://help.figma.com/hc/article_attachments/41416799269527)

[**Copy as design layers**](https://help.figma.com/hc/en-us/articles/35060759685015)
when you want to explore an idea from a prototype back on the canvas. Navigate to the state you want in Make's preview,
then
click **Copy design**. Paste the layers onto a Figma Design
canvas
and you have editable frames — ready to refine, annotate, or share with
teammates.
The layers aren't connected to the Make file and aren't automatically
linked
to your design system, so treat them as a starting point for the next
round of
design work.

[
](https://help.figma.com/hc/article_attachments/41416799271063)

[**Embed the live prototype**](https://help.figma.com/hc/en-us/articles/37617790464535)
when you want to show others, or keep the prototype as a live reference
on the
same canvas as your designs. Paste the Make file URL into a Figma Design
file,
FigJam board, or Slides deck. The prototype becomes playable in place:
teammates
can click through flows, trigger transitions, and see exactly how it
behaves
without leaving the file.
