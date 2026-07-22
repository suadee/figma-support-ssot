---
기술지원명: Code to canvas with your design system
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Code to canvas with your design system
출처링크: https://help.figma.com/hc/en-us/articles/40287261761559-Code-to-canvas-with-your-design-system
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server lets AI agents read *and* write to your Figma canvas, using your actual design system as the source of truth. But what does that actually look like in practice?

In this lesson, we'll walk through how Amy, a technical designer at Earthling, uses the `use_figma` tool to move fluidly between the terminal and Figma canvas. You'll see how she uses the Figma MCP server and the agentic tool to generate a starting point, iterating the design in Figma, and implementing it back to the codebase.

## Start from the terminal

Earthling's codebase is mapped to their Figma Design file. Their design system lives in Figma, components are published to the library, and their AI agent has access to the Figma MCP server from the terminal.

With the MCP server connected, you can use the `use_figma` tool to create and edit frames, components, variables, and auto layout directly on the Figma canvas.

**Note:** To learn more about all available Figma MCP tools,
check out our
[developer docs](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/).

The Earthling team just kicked off a new feature, an empty state for the search screen, and Amy wants to iterate on a new version that includes suggested destinations.

![](https://help.figma.com/hc/article_attachments/40287563241495)

### Generate design from a prompt

Rather than starting from scratch in Figma Design, Amy can prompt the agent to generate a design as a starting point.

To prompt the agent:

1. Select the current search screen design in Figma.
2. Right-click and select **Copy/Paste as** -> **Copy link to selection**.
3. Switch to the terminal and enter the following prompt:

   ```
   "Using the Earthling design system, create an empty state for the search screen that shows suggested destinations with destination thumbnails and a heading. This will be the new empty state of this screen. [Insert Figma link]"
   ```

From this prompt, the AI agent will call `use_figma` under the hood, pulling in our components and variables to assemble the design.

![](https://help.figma.com/hc/article_attachments/40287761064855)

## Iterate in Figma

### Make edits to generated design

Now that the agent has created a design for the new search screen, Amy is ready to make some new iterations based on the design. The design generated is native, editable Figma content, so Amy is able to use it as a starting point to iterate on it further.

![generated-design.gif](https://help.figma.com/hc/article_attachments/40287736713495)

Once she’s done with the editing, she can loop in a collaborator to confirm the updated direction by leaving a comment on the canvas.

### Add annotation

She can also add annotations directly on the frame to communicate the interaction logic — what happens when a user taps on a destination card, and what the loading state should look like. Because annotations live right on the design, the AI agents can pull important design context right from the source.

To add an annotation:

1. Click **Annotation** in the toolbar or use the keyboard shortcut `Shift T`.
2. Click on the layer you’d like to annotate.
3. Write a note in the text field, or click + Property to select a property from the list. You can include both plain text and properties in an annotation.

![annotation.png](https://help.figma.com/hc/article_attachments/40287736713879)

## Implement back to code

Now that the design is ready to implement, Amy grabs the frame link and heads back to the terminal.

In the terminal, she prompts the agent to implement the changes:

```
Implement the search screen design from this Figma frame into our codebase. Use our existing components and follow our project's code conventions. [Insert Figma link]
```

The agent reads the design context, and generates code using the actual component library. And just like that, the codebase is updated, and design and code are in sync.

![localhost.gif](https://help.figma.com/hc/article_attachments/40287736719895)

## Wrap up

The Earthling example illustrates something broader about designing with the Figma MCP server. It removes the friction of starting from scratch and keeps the design system at the center of every iteration. AI agents read your library, follow your conventions, and contribute back to your system with your craft as a guide. The designer's expertise becomes more efficient and also more valuable.

## Additional resources

- Check out more Figma MCP use cases in the ["Release Notes 2026: May Edition"](https://youtu.be/11mdb7lLclM) video
- Explore custom skills in the [Figma Community](https://www.figma.com/community/skills)
