---
기술지원명: AI workflows collection: Best practices to help Figma AI understand your design system
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Best practices to help Figma AI understand your design system
출처링크: https://help.figma.com/hc/en-us/articles/38978644498199-AI-workflows-collection-Best-practices-to-help-Figma-AI-understand-your-design-system
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma’s agent can use your design system as context when generating designs, prototypes and web apps.

The more structured and complete your design system is, the more accurately the agent can interpret and apply it. This helps produce outputs that look and feel like your product.

For example:

- [The agent in Figma Design](https://help.figma.com/hc/en-us/articles/37998629035799) can use your design system as the foundation for any designs it creates or edits.
- [The agent in Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231) can [use your design system](https://help.figma.com/hc/en-us/articles/33024539096471) to build prototypes with your real components, styles, and structure instead of generic defaults.

To help agents make the most out of your design system, follow the tips below:

1. [Build reusable blocks and patterns](https://help.figma.com/hc/en-us/articles/38978644498199-Best-practices-to-help-Figma-AI-understand-your-design-system#h_01KKFV30GE7M7PH1YPBCNXG07W)
2. [Give layers and components meaningful names](https://help.figma.com/hc/en-us/articles/38978644498199-Best-practices-to-help-Figma-AI-understand-your-design-system#h_01KKFV30GEKRVSSHMJP11AZBA6)
3. [Use auto layout to communicate structure and responsiveness](https://help.figma.com/hc/en-us/articles/38978644498199-Best-practices-to-help-Figma-AI-understand-your-design-system#h_01KKFV30GEKEQ7R0988MQY5PZS)
4. [Define your component properties and variants](https://help.figma.com/hc/en-us/articles/38978644498199-Best-practices-to-help-Figma-AI-understand-your-design-system#h_01KKFV30GFD0FV4FC0ZJTW7FFS)
5. [Use variables for colors, spacing, and typography](https://help.figma.com/hc/en-us/articles/38978644498199-Best-practices-to-help-Figma-AI-understand-your-design-system#h_01KKFV30GFRV0KMV2KGDJXQC12)
6. [Add descriptions to document your components, styles, and variables](#h_01KVPQVARVBNNH7VM9P8MJSWWZ)

**Note:** For agents to reference your design system, your library must be published. If you've made recent changes to your library, make sure to [publish those updates](https://help.figma.com/hc/en-us/articles/360025508373) so the agent can work with the latest.

**Tip:** Need a refresher on design systems concepts like components and variables? Check out Figma’s [Introduction to design systems course](https://help.figma.com/hc/en-us/sections/14548397990423-Introduction-to-design-systems).

## 1. Build reusable blocks and patterns

Design systems are typically built around atomic components—buttons, inputs, icons, and other small pieces. These are essential, but they're difficult for AI to compose into coherent layouts on their own.

AI tools work best when they can reference complete, higher-order compositions: reusable blocks like cards, headers, feature rows, and carousels that already encode the spacing, color, and layout logic for a full section.

When Figma’s agent has access to these blocks, it can reuse them consistently across generated layouts rather than guessing how individual atoms should fit together.

For example, instead of relying on separate button, text field, and image container components, a reusable **card** component groups all three with predefined spacing, typography, and color tokens. When AI references your design system, it can drop that card into any layout confidently—rather than assembling it from scratch each time.

A few things to keep in mind when building higher-order compositions:

- **Encode layout intent.** Use auto layout within your blocks so that spacing and arrangement are defined, not implied.
- **Keep blocks stackable.** Design sections so they can be combined with other sections in your system—consistent padding, margins, and alignment make this easier.
- **Apply variables where appropriate.** Make sure color, spacing, and typography variables are applied so these higher-order components carry their style context when they're reused.

![](https://help.figma.com/hc/article_attachments/40608889475607)

You can also show the agent directly how pieces of your design system fit together by providing example components in your library file. The examples should show realistic compositions—full layouts assembled from your components.

There are two ways to do this:

- **Use the**`_example`**suffix.** You can mark any component as an example by adding `_example` as a suffix to its name—for example, `Dashboard/HeroSection_example`. Use a descriptive name so the agent understands when and how to apply it.
- **Add an Examples page.** If a published library includes a page named **Examples**, the agent will use it to understand how to apply elements from your design system. Each design on this page should be a component.

**Note**: Figma’s agent can currently reference up to 200 examples in a file.

## 2. Give layers and components meaningful names

Figma’s agent reads the names of layers and components to understand what a design contains and how it's structured. This applies in two places:

**In your library**, component names tell the agent what each piece of your system is and where it belongs. Well-named components are also easier for the agent to find. A component called `Card/Product/Default` is immediately interpretable; a component called `Frame 42 copy` is not.

**In design files**, layer names tell the agent how individual elements relate to each other within a frame. Generic default names like `Group 7` or `Rectangle 3` give the agent nothing to work with. Semantic names like `HeroImage` or `PriceLabel` help it generate more accurate code and make better decisions when composing layouts.

Use a consistent naming convention across your library. Figma's slash notation—like `Button/Primary/Large`—creates nested groups that help both people and agents navigate large systems.

**Use Figma’s agent to rename layers in bulk**

When you [rename layers with AI](https://help.figma.com/hc/en-us/articles/24004711129879), Figma uses each layer's contents, position, and relationship to other layers to choose a meaningful name automatically.

To rename layers:

1. Select the layers you want to rename—or select a parent frame to rename everything inside it.
2. Right-click the selection and choose **Rename layers**.

The agent only renames layers that still use Figma's default naming convention, so any names you've already set will be preserved.

**Tip:** For more control over component naming, use [bulk rename](https://help.figma.com/hc/en-us/articles/360039958934) to apply prefixes, suffixes, or specific naming patterns across a selection of layers. This is useful for enforcing conventions like `Icon/Arrow` or `Input/Text/Error`.

## 3. Use auto layout to communicate structure and responsiveness

![](https://help.figma.com/hc/article_attachments/41390818084247)

Auto layout tells agents how elements in a design are meant to be arranged and how they should respond when content changes. Without it, a frame is a static snapshot—the agent has no way to tell whether a row of items should wrap, whether a container should stretch to fill its parent, or how spacing should shift when content is added or removed. With auto layout, that intent is encoded directly in the file.

This matters most at the component level, where the relationship between elements—the space between a label and an icon, the way a card's height grows with its content—defines how the component behaves in production.

When applying auto layout to your components, be intentional about sizing:

- Use **fill container** for components that should stretch to fill their parent, like full-width banners, table rows, or list items. This tells the agent the component is designed to be responsive to its context.
- Use **hug contents** for components that should shrink to fit their content, like buttons, chips, and tags. This tells the agent the component's size is determined by what's inside it.
- Use **fixed sizing** for components with strict dimensions that should never change, like avatar thumbnails or icon containers.
- Set **min and max widths** to constrain how a component scales between its smallest and largest meaningful sizes.

[Learn more about auto layout.](https://help.figma.com/hc/en-us/articles/360040451373)

**Did you know you can use a tool to apply auto layout automatically?** If you have existing components or designs that don't yet use auto layout, [**Suggest auto layout**](https://help.figma.com/hc/en-us/articles/5731482952599) can add it for you in one step.

Figma analyzes the objects in a frame or component and adds auto layout frames as needed to make the design responsive—without requiring you to work through each layer manually.

To use **Suggest auto layout:**

1. Select the frame or component you want to update.
2. Right-click and select **More layout options** > **Suggest auto layout**.

For large or complex designs, try working in sections rather than selecting everything at once.

## 4. Define your component properties and variants

![](https://help.figma.com/hc/article_attachments/40557713745047)

Component properties are one of the most useful signals you can give the agent in Figma. They define the full range of what a component can do—its available sizes, states, boolean toggles, and freeform slots—in a structured, machine-readable way. Without them, the agent has to infer a component's range of variation from visual inspection alone, which leads to incomplete or inconsistent results.

For example, a button component with defined variants for **size** (small, medium, large), **type** (primary, secondary, tertiary), and **state** (default, hover, disabled) gives the agent a complete schema to work from. It knows what's possible and what isn't, and can apply the right variant for the context.

This really pays off when your design system connects to code. It becomes much easier for the agent to build something like a React component when all the properties are defined.

[Learn more about component properties in Figma Design](https://help.figma.com/hc/en-us/articles/8883756012823).

**Tip**: Try [asking the agent](https://help.figma.com/hc/en-us/articles/37998629035799) for help adding component properties to a component set.

## 5. Use variables for colors, spacing, and typography

When your colors, spacing, corner radii, and typography are defined as variables, the agent can reference those tokens directly instead of working from raw values. This keeps generated outputs consistent with your system and makes it much easier to apply your brand reliably across layouts. [Learn more about variables in Figma](https://help.figma.com/hc/en-us/articles/15339657135383).

For example, when you [export your library to Figma Make](https://help.figma.com/hc/en-us/articles/33024539096471), Figma extracts your variables into a CSS file that Figma Make references when generating code. A well-structured variable system makes this extraction more complete and accurate.

A few things to keep in mind when setting up variables:

- **Use semantic names.** Names like `color/surface/primary` communicate how a value should be used, not just what it is. A variable called `blue-500` tells agents nothing about when to apply it; `color/brand/primary` does.
- **Organize variables into collections.** Group related variables (color, spacing, typography) into named collections so the structure is easy to navigate.
- **Use slash naming to create groups.** Figma uses `/` as a separator to create nested groups, which helps keep large token libraries organized.

**Tip:** If you're starting from scratch or want help adding variables to an existing design, you can ask Figma’s agent to create and apply variables to your designs.

## 6. Add descriptions to document your components, styles, and variables

Documentation gives agents the context they needs to choose the right asset and use it correctly. An agent can identify what a component looks like, but without documentation it may not understand when to use it, what states it supports, or how it differs from similar components.

This is especially important for components that look alike but serve different purposes—like a primary button and a destructive button, or a card used in a list versus a card used in a modal. Clear descriptions help the agent pick the right one.

You can [add descriptions to components, styles, and variables](https://help.figma.com/hc/en-us/articles/7938814091287) directly in Figma:

- **Components**: Explain the component's purpose and when to use it. Figma includes component descriptions in search results, so well-documented components are easier for both people and agents to find.
- **Styles**: Describe when a style should be applied, such as "Use for body text on light backgrounds only."
- **Variables**: Add context for values that aren't self-evident, like semantic color roles (`color/surface/danger`) or the intent behind spacing values.

**What makes good documentation for agents?**

Good documentation explains the *why*, not just the *what*. For each component, consider including:

- Its purpose and intended use case
- When to use it versus a similar component
- Its available variants and states (hover, focus, error, disabled)
- Any accessibility requirements, like color contrast minimums or keyboard interaction expectations

You might be inclined to document your system the way you'd present it to a teammate: a polished frame on the canvas with do and don't pairs, callouts, and annotated examples.

That works well for a person browsing the library, but when the agent encounters a documentation frame like that, it doesn't see your layout in the same way as a person.

Instead, it sees a tree of frames, text, and shapes, and it has to infer meaning from how those elements are arranged—guessing which parts are guidance, which are examples, and which are decoration. By using a description field is different, the agent gets the right context as plain text, exactly as written. The meaning is stated explicitly, not constructed from the layout on the canvas.

**Tip:** If you’re feeling stuck, [the agent in Figma Design](https://help.figma.com/hc/en-us/articles/37998629035799) can [write a first draft of component, style and variable documentation](https://help.figma.com/hc/en-us/articles/41159677390999) for you.
