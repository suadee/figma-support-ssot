---
기술지원명: Components collection: Tips for component management
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Components collection: Tips for component management
출처링크: https://help.figma.com/hc/en-us/articles/39747637290263-Components-collection-Tips-for-component-management
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

As you spend more time creating components in Figma Design, you’ll soon discover that building components and *managing* components are two very different things. Creating a button component can be simple, but it’s much harder to maintain a design library that scales effectively as your project grows.

Whether you’re working solo or as part of a team, component management is an important part of the design process. Fortunately, most of what makes a design system work well comes down to a handful of habits: consistent naming, clear documentation, and proactive maintenance. In this article, we’ll walk through our top tips for managing and organizing components so you can build a sustainable design library that your team will be excited to use.

## Be intentional when naming components

Implementing a consistent naming convention is one of the best things you can do to reduce friction for design library users. Clear, consistent naming helps designers find what they need faster, gives developers additional context when interpreting handoff specs, and increases the likelihood that AI tools will be able to accurately parse your file’s structure and organization.

### Give components and properties clear and obvious names

Component names should be immediately obvious. You don’t want someone spending time wondering if what they’re looking for is called a `Badge`, `Chip`, or `Tag`.

A common naming mistake is describing what a component currently looks like rather than what it is. A name like `blue-large-button` becomes a liability the moment the color or size changes. Instead, name components what they *are*, not how they currently appear.

The same naming discipline that applies to components also applies to component properties. Inconsistencies across your design library, such as using `Size`, `Scale`, and `Dimensions` to describe the same property, can create unnecessary confusion.

It’s much easier to establish naming conventions at the start than to fix them later. There’s no single correct convention, the right one is simply whatever works best for you and your team. Before your library grows, make a few key decisions:

- **Casing:** Will you use Title Case, lower case, or camelCase?
- **Abbreviations:** Will you shorten some words? If so, which ones?
- **Terminology:** Is it `modal` or `dialog`? `Icon` or `symbol`? `Notification` or `toast`?
- **Boolean phrasing:** Are they phrased as `Has Icon`, `Show Icon`, `Icon Visible`?
- **Values:** Are sizes `SM`, `MD`, `LG` or `Small`, `Medium`, `Large`? Are states `Hover` or `Hovered`?

#### **Align names with your codebase**

One of the most practical things you can do when naming components is align with what developers call things in code. Developers inspecting your designs in [Dev Mode](https://help.figma.com/hc/en-us/articles/22012921621015-Guide-to-inspecting#h_01HRSPSSENR958HVP3WYSJ0W9C) will see your component and property names in the right sidebar. When designers and developers share a vocabulary, handoff becomes much smoother.

For example, it’s much easier to translate designs into code when the design component is called `Button` and the code component is `<Button>`. When one is `CTA` and the other is `<Action>` every handoff risks translation errors.

### Use slash-separated naming to create structure in your files

Figma uses the [slash-separated naming convention](https://help.figma.com/hc/en-us/articles/360038663994-Name-and-organize-components) to organize components in a file. Each slash ( / ) in a component’s name creates another level of hierarchy. Using the slash-separated convention also groups related components together in the **Assets** tab and **Instance** menu and makes it immediately clear where a component lives in the broader design system.

For example:

- `button/primary/default`
- `button/primary/hover`
- `button/secondary/default`
- `button/secondary/hover`

**Note:** When you have slash-separated component names, you can enable the **Show subfolders** setting to display components in a nested folder structure that mirrors your naming hierarchy. This is a helpful way to navigate large design libraries.

![](https://help.figma.com/hc/article_attachments/39748177088919)

### Name the layers inside your components

The layers inside your components matter just as much as the components themselves, especially during development handoff or when Agentic tools attempt to parse your files.

Get in the habit of naming any layer that carries structural meaning. Layer names like `card-thumbnail` or `user-avatar` communicate purpose and function so much more than `Rectangle 4` or `Frame 22`. The upfront investment it takes to accurately name your layers will make a real difference when someone needs to understand how a component is built.

**Tip:** You can use [Figma AI](https://help.figma.com/hc/en-us/articles/24004711129879-Rename-layers-with-AI) to give your layers contextual names in just a few clicks.

## Build components that are easy to use

The success of your components relies on how easy they are to use. Using a well-built component should feel relatively frictionless, even for someone who didn’t build it.

### Use component properties to expose the right controls

Component properties and variants let you control how flexible a component should be. When building a component, consider which aspects people will need to change about it and what’s the easiest way to expose those controls.

Use [variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants) to handle visually or structurally distinct states. For example:

- **Style:** How prominent or interactive a component appears
- **Size:** How a component scales for different contexts
- **State:** How a component responds to user interaction

Use [component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties) to handle changes at the content-level, without multiplying the number of variants needed to capture each unique state. For example:

- **Boolean properties:** Show or hide an element
- **Instance swap properties:** Swap nested components for another
- **Text:** Expose editable text layers directly in the right sidebar
- **Slots:** Create flexible areas where content can be freely added and organized

![](https://help.figma.com/hc/article_attachments/39748221690519)

### Keep accessibility in mind from the start

Components can be a powerful tool for creating accessible designs at scale. When components are built with accessibility in mind, every instance of that component inherits those decisions automatically, meaning designers can create inclusive designs without having to remember accessibility requirements each time.

There are a few things to consider when building accessible components:

- **Color contrast**: Proper color contrast makes your designs more inclusive by improving readability for users with visual impairments. You can use the [color contrast tool](https://help.figma.com/hc/en-us/articles/360041003774-Update-fills-using-the-color-picker#h_01JQF1T71AC72G6VDXN27B77V0) to quickly check if a color combination meets accessibility guidelines.
- **Interaction states:** Interactive components should include documentation for every meaningful state, such as hover, focus, active, and disabled. Visible focus states are often overlooked in design, but are critical for keyboard and assistive technology users.
- **Use annotations:** [Accessibility annotations](https://help.figma.com/hc/en-us/articles/20774752502935-Add-measurements-and-annotate-designs#h_01JQF01V58B84YWTHPN9NGTMMV) let you communicate intended roles, labels, and reading order to developers during handoff. This can reduce the risk of accessibility being lost in translation between design and code.

## Document your decisions

Even if you work alone, creating clear documentation is a worthwhile habit. The decisions you make today may not be as obvious three months from now. Good documentation means that anyone accessing your design library will be able to use your components quickly and accurately.

### Add context to your components

When creating components, you can use the component settings to add a description. Descriptions don’t need to be long, but a few sentences explaining how the component should be used and any constraints to keep in mind can go a long way. For example, a label-less icon button component may include a description like:

*Icon buttons trigger an action using a single icon without a visible text label. Use an icon button when:*

- *The icon represents a widely recognized, universal action.*
- *Space constraints prevent the use of a text label.*
- *The same icon is consistently used across the product for the same action.*

*If the action is ambiguous, critical, or not universally understood, use a labeled button instead.*

Component descriptions appear in the **Assets** tab when someone selects a component and in the right sidebar when they select an instance. If your team hosts documentation outside of Figma, you can also include a link directly in the description to point people to more information. Learn more about [adding descriptions to components](https://help.figma.com/hc/en-us/articles/7938814091287-Add-descriptions-to-styles-components-and-variables).

![imageTemplate (20) (1).png](https://help.figma.com/hc/article_attachments/39748177092887)

### Include do’s and don’ts

For components that are commonly misused or have non-obvious constraints, explicit do/don’t guidance is one of the most effective things you can include in your documentation.

Keep do/don’t usage specific and pair it with a visual example where possible.

![imageTemplate (19) (1).png](https://help.figma.com/hc/article_attachments/39748221693847)

## Update components without breaking things

At some point, every component needs to be updated. Products evolve, branding changes, and edge cases emerge that the original component wasn’t designed for. Updates are a natural part of the design process, but unmanaged changes can break things in files that use the component and create more work than they save.

### Understand what makes a change breaking

Not all updates carry the same risk. A **non-breaking change** is one that updates the component without disrupting existing instances, such as:

- Adding a new optional property
- Visual refinements that don’t impact layout or overrides
- Internal layer restructuring that doesn’t change how properties behave

For example, adding a hidden-by-default boolean property for an optional supporting text string is a non-breaking change. The string won’t display unless a designer explicitly enables it, so the change can be published without fear of impacting existing instances.

![imageTemplate (18) (1).png](https://help.figma.com/hc/article_attachments/39748177096727)

A **breaking change** is one that can reset, invalidate, or alter existing overrides in instances, such as:

- Removing or renaming a property
- Restructuring variants in a way that changes how existing instances resolve
- Renaming layers that users may have overridden directly

Using the same example, if that new supporting text string is shown by default instead of hidden, the change becomes breaking. Any existing instances of the component will now display placeholder text in designs, even if the designer doesn’t want it to, requiring them to manually locate every instance and toggle the string’s visibility.

Before committing to a breaking change, consider whether a less disruptive path exists, such as adding an optional property or making a new variant available alongside the existing one during a transition period. If a breaking change is absolutely necessary, make sure the impact is understood before you publish. Unlike non-breaking changes, which can typically be published quietly, breaking changes require proactive communication with anyone using the component. Learn more about [publishing library updates](https://help.figma.com/hc/en-us/articles/360025508373-Publish-a-library).

### Test your changes before publishing

Before publishing any update to a shared library, we recommend taking time to test it first. Open a file that uses the component, swap an existing instance for the updated version, and check that everything works as expected. Cycle through the property combinations and confirm that there are no unexpected interactions.

**Note:** If you’re on the [Organization or Enterprise](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features) plan, you can also create a branch of your design library to safely test changes in an isolated environment before publishing. Learn more about [branching](https://help.figma.com/hc/en-us/articles/360063144053-Guide-to-branching).

### Communicate changes to your team

If you work with others using a shared library, a single published component change can potentially affect dozens of open files and impact the work of other designers. This is why communication is as important as the component update itself.

We recommend developing a communication process with your team. Consider creating a changelog that includes a running record of what changed, when, and why. This can live inside a Figma file or wherever your team documents decisions. Including clear labels such as `[UPDATE]`, `[BREAKING]`, or `[DEPRECATED]` in your changelog can help people quickly assess how much they need to pay attention.

![imageTemplate (17) (1).png](https://help.figma.com/hc/article_attachments/39748177098391)

**Note:** If you’re on the [Organization or Enterprise](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features) plan, you can view [analytics](https://help.figma.com/hc/en-us/articles/360039238353-View-and-explore-library-analytics) for your design library to get a holistic view of how design assets are being used before you commit to publishing changes. Knowing how widely used a component is can help you make better decisions about how much testing to do, how far in advance to communicate, and how long to leave a deprecation window open.

### Deprecate components gracefully

Sometimes a component may need to be retired rather than updated. Deprecated components should be clearly marked as such, both in the name and in the description, and should always point users toward what to use instead.

Give people time to migrate before removing components outright. Removing a component that’s actively being used without warning is one of the fastest ways to break trust in a design system.

## Learn more about design systems

If you're new to the world of design systems, we recommend taking our [Introduction to design systems](https://help.figma.com/hc/en-us/sections/14548397990423-Introduction-to-design-systems) course. This course will walk you through the entire design system journey—from fundamental concepts, to building and documenting your system. Throughout the course you'll explore real-world applications and discover tools to help you make meaningful decisions as you create and manage your own design system.

**Continue the conversation on the Figma forum**  
Learning is better, together! Compare notes with others working through this collection on the [Figma forum](https://forum.figma.com/ask-the-community-7/components-collection-learn-with-others-53016).
