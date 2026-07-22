---
기술지원명: AI workflows collection: Use the Figma agent to improve your design system
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Use the Figma agent to improve your design system
출처링크: https://help.figma.com/hc/en-us/articles/41159677390999-AI-workflows-collection-Use-the-Figma-agent-to-improve-your-design-system
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

Tom is the design systems manager at Cheddar. He wants to publish an update to the Cheddar UI kit library soon, and his to-do list includes writing documentation for dozens of components, cleaning up naming inconsistencies, and formalizing a handful of patterns the product team has been quietly using.

He'll get to all of it, but getting everything ready will take a lot of work. He'd rather spend time thinking about what's next for the Cheddar system.

The decisions encoded in a design system ripple through every part of the design process, from helping designers get started on new features, to helping developers implement them.

Those decisions bring a lot of work with them: writing documentation, creating or updating components, styles, and variables, and auditing for inconsistencies.

The Figma agent can take on some of that work, giving you more time for the strategic parts of the system. This article covers four areas where the Figma agent can help with the heavy lifting:

1. [Write documentation at scale](#h_01KVRS9EZ7TBR3BHNA5YYEE2JC)
2. [Update components, styles, and variables in bulk](#h_01KVRS9EZ7EBY4XXDZ18D43W06)
3. [Extract and systematize patterns from your designs](#h_01KVRS9EZ7Z657ZPK2D30232HT)
4. [Catch inconsistencies, gaps, and improvements before publishing](#h_01KVRS9EZ73MQRSZ37A8GXV3WQ)

## Write documentation at scale

The Figma agent can draft documentation directly on the canvas, using your existing components, styles, and variables as context.

**Tip**: The agent has a built-in skill for creating documentation, so you don't need to be too prescriptive with your prompts. If you have an existing documentation template, it's a good idea to provide that as context for the agent. If not, the agent will apply a basic template defined in the skill.

Good documentation has a compounding effect beyond the original use case of helping other designers use the design system.

As your documentation improves, it gets easier for the Figma agent to use the correct components and states when referencing the library to generate designs on the canvas. This means your fellow designers can work more efficiently and effectively when asking the agent for help with design tasks.

Here are some example prompts:

- Create documentation for all of the components on this page. Include design specs, variants, properties, and nested instances.
- Create a table of all color variables in this document. Include a 32×32px swatch with the color as the fill, the color name, hex value, and intended use.
- Document the button component set for a designer learning about the different states. Provide usage guidelines.

[Learn more about writing documentation that helps agents produce better outputs.](https://help.figma.com/hc/en-us/articles/38978644498199)

![](https://help.figma.com/hc/article_attachments/41415283130007)

**Tip:** You can write documentation on the canvas, edit it, then ask the agent to update the description of each component to match. Component descriptions are important because they provide critical context for both designers and agents when they’re building from the library.

## Update components, styles, and variables in bulk

When something needs to change across your library—property names, variant structure, sizing, or naming conventions—the agent can make those updates in bulk.

This overlaps with the general cleanup work covered in [Cut down on busywork](https://help.figma.com/hc/en-us/articles/41159765402007), but a few patterns are especially useful when working inside library files.

**Example prompts**

- Flatten these icons, rename each according to our icon component naming conventions, arrange them in alphabetical order, and create components for each.
- Duplicate this 24px icon set and create a new 16px set of the same icons, reducing the stroke width of each to 1px and updating the naming of each.
- Remove all shadow styles from components in this set.
- Standardize all layer names on this page to use kebab-case.

**Tip**: These kinds of update-related prompts can be a good way to bring new patterns into your design system. For example, you can bring a new component across from an existing design file and make sure it's well aligned with the design system.

## Extract and systematize patterns from your designs

Maintaining a design system means continuously evaluating what's happening across the product. The agent can help you audit designs, uncover recurring patterns, and translate them into reusable system assets. It can also help identify gaps and opportunities for new components or states.

**Example prompts**

- Based on the cards in these screens, give me a first pass on an updated card component.
- Audit the designs on this page and identify any values or patterns that aren’t in the connected design system.
- Extract the core colors from this screen and build out color variable scales that range from 0–1000 in increments of 100.
- Extract all the type size values on this screen and create a number variables collection out of them.
- Update the existing **Spacing** collection variables to be multiples of 12.

**Tip**: This approach can help address gaps when the codebase has drifted from the design system. For example, drop a list of CSS variables on the canvas and ask the agent to identify gaps between what's available in code in production and what's captured in the design system in Figma.

## Catch inconsistencies, gaps, and improvements before publishing

There are a lot of things to keep in mind when publishing an update to a library, like whether the work covers the right states, is built consistently with the rest of the system, and is documented clearly enough for someone to use correctly.

The agent can act as an initial reviewer, surfacing things that are easy to miss when you've been looking at a whole canvas of designs for a while.

**Example prompts**

- Review this component set. Are there any missing states or variants?
- Is the documentation for this component complete?
- Are there any opportunities to simplify? Either by merging components or simplifying naming?
- Look at the construction of this component and compare it to how similar components are built in this file. Are there any inconsistencies?
- What would you change before I publish?

![](https://help.figma.com/hc/article_attachments/41415262238487)

**Tip**: Before publishing an update, you can also use [Check designs](https://help.figma.com/hc/en-us/articles/39592284074263)—available on the Organization and Enterprise plans—to scan your design file for inconsistencies with your design system.

Check designs helps you identify:

- Incorrect colors
- Components, variables, and styles from incorrect libraries
- Hardcoded values that should be variables
