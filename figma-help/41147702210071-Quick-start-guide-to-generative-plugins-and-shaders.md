---
기술지원명: Quick start guide to generative plugins and shaders
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Quick start guide to generative plugins and shaders
출처링크: https://help.figma.com/hc/en-us/articles/41147702210071-Quick-start-guide-to-generative-plugins-and-shaders
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Generated plugins and shaders are currently in open beta.** Features may change and you may experience performance issues as we continue to improve generated plugins and shaders. Learn more about [what's included in the beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

Before you Start

Who can use this feature

Available in Figma Design to [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with access to the [Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799) can generate plugins and shaders

Figma uses WebGPU to render shaders. Make sure your [system and browser meet the minimum requirements](https://help.figma.com/hc/en-us/articles/360039827194-What-are-the-system-requirements-for-Figma).

Extend what's possible in your design files by building custom plugins and shaders through prompting the [Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799-Work-with-the-Figma-agent-in-design-files). No need to understand code or technical terminology—you explain it, the Figma agent will build it.

In this quick start guide, we’ll give you an overview of what generative plugins and shaders are, walk you through prompting the Figma agent to build your own, provide basic tips for prompting, and ways to use them alongside other Figma features.

## What are generative plugins?

Plugins are applications that extend the functionality of Figma’s products using Figma’s Plugin API. Generative plugins are as their name suggests—they are built by prompting the Figma agent and the agent writes the code for you so that you don’t have to. You can even build plugins for Figma Draw and Motion.

![Plugins detail 3 -_ press kit.png](https://help.figma.com/hc/article_attachments/41750812656279)

### Types of generative plugins in Figma

There are three types of generative plugins that the Figma agent can help you build:

#### A plugin that **creates** content.

These plugins generate layers and vectors and adds them to the canvas. For example: a soundbar visualizer, a device component variant generator, 3D wireframe generator.

#### A plugin that **modifies** layers.

These plugins modifies existing layers on the canvas. For example: a plugin that restyles icons in bulk, creates a skeleton screen version of a design, or generates a type ramp.

#### A plugin that is a **file utility**.

File utility helps to manage and organize your file. For example: a plugin that batch-rename layers, organizes layers on the canvas, checks for broken prototype flows.

### Make your own plugin

**Note**: While in beta, generative plugins will not cost AI credits to build and iterate. Plugins never cost credits to run.

To build your own plugin using the Figma agent:

1. Open a Figma Design file.
2. Click  **Agents** in the navigation bar to open the Figma agent and start a new chat.
3. In the prompt box, type `Build me a plugin` and describe what you want the plugin to do. If you’re not sure where to start, try out one of the prompts below to start!
4. Test your plugin, and [iterate with the agent](https://help.figma.com/hc/en-us/articles/41408020198935) as needed.

#### **Try these prompts**

![example-plugin-prompt-density-variants.png](https://help.figma.com/hc/article_attachments/41434428874135)

```
 Density mode switcher: Build a plugin that takes my selected frames and produces compact, default, and spacious versions—scaling spacing tokens proportionally so I can present three density options to stakeholders without duplicating the work manually.
```

![example-plugiin-layer-hygiene-linter.png](https://help.figma.com/hc/article_attachments/41434428875543)

```
Layer hygiene linter: Build a plugin that audits all layers in my file for unnamed layers, hidden orphan layers, empty groups, redundant nesting, near-duplicate components, and file complexity. Before scanning, let me choose which categories and which pages to audit. Show results as collapsible sections with an Ignore button per row, and let me return to settings to re-configure and re-scan.
```

![example-plugin-prompt-contrast-fixer.png](https://help.figma.com/hc/article_attachments/41434451797783)

```
Accessibility checks: Build a plugin that audits designs for WCAG contrast failures (with AA/AAA toggle, selection vs. page scope, and a show-only mode) and suggests fixes from the file's local color variables. Each failing layer should show two fix options—one for the text fill and one for the background fill — each with a color swatch preview, a Fix button, and a "Browse variables…" fallback picker if no compliant variable exists. After the first audit, re-audit automatically in real time whenever a fill changes.
```

**Note**: The Figma agent is building you a fully coded plugin and may take a few moments to finish.

### Explore plugins built by Figma

The Figma team has built dozens of plugins—like chart generators and ASCII art transformers—for everyone use in their design files. To browse Figma's full plugin offering:

1. Open the **Tools** tab from your design file and filter the source by **From Figma**.
2. Click the  **Filter** icon and select **Plugins**.

Plugins built by Figma are free to use.

[Learn about how to use a specific plugin built by Figma.](https://help.figma.com/hc/en-us/articles/41409034424215)

## What are shaders?

Shaders are miniature customizable programs that give you precise control over the visual appearance of everything rendered on a screen. They’re fast at producing complex visual effects, like realistic fire and distortions, and are widely used across industries—from web design and augmented reality to game development and architectural design.

If you've ever added a blur, blend mode, gradient overlay, or glassy distortion effect in Figma, shader technology is what make those effects possible. Learn more about [effects in Figma Design](https://help.figma.com/hc/en-us/articles/360040667874).

![Shaders detail 3 -_ press kit.png](https://help.figma.com/hc/article_attachments/41750812661527)

### Types of shaders in Figma

There are two types of shaders that the Figma agent can help you build:

#### Shader fills

Shadows are standalone visuals such as patterns, gradients, and procedural textures—like marble, fire, and water.

#### Shader effects

Shader effects modify existing visuals with things such as blurs, distortions, grain, pixelation, dithering, and color adjustments.

### Make your own shader

**Note**: While in beta, shaders will not cost AI credits to build and iterate. Shaders never cost credits to run.

To build your own shader using the Figma agent:

1. Open a Figma Design file.
2. Click  **Agents** in the navigation bar to open the Figma agent and start a new chat.
3. In the prompt box, type `Build me a shader` and describe what you want the plugin to do. If you’re not sure where to start, try out one of the prompts below to start!
4. Test your shader, and [iterate with the agent](https://help.figma.com/hc/en-us/articles/41408020198935) as needed.

#### **Try these prompts**

![shader-example-topography.png](https://help.figma.com/hc/article_attachments/41455189837335)

```
Topographic contours: Build me a shader fill made of topographic contour lines, like the elevation rings on a hiking map. I want controls for line spacing, line thickness, and how rugged or smooth the terrain looks, plus separate line and background colors. Keep the pattern seamless so it tiles cleanly across large frames.
```

![shader-example-foil.png](https://help.figma.com/hc/article_attachments/41455227336599)

```
Holographic foil: Create a holographic foil shader effect with a liquid chrome style. Colors should flow along the edges and contours of the layer using luminance gradients, not a flat directional sweep. Controls: hue offset, color range, angle (rotates the gradient direction), band frequency, sheen intensity, saturation, and blend amount.
```

**Note**: The Figma agent is building you a fully coded shader and may take a few moments to finish.

### Explore shaders built by Figma

The Figma team has built dozens of shaders—like pixel stretching images and adding metallic effects to layers—for everyone use in their design files. To browse Figma's full shaders offering:

1. Open the **Tools** tab from your design file and filter the source by **From Figma**.
2. Click the  **Filter** icon and select **Shader effects** and **Shader fills**.

Shaders built by Figma are free to use.

[Learn about how to use a specific shader built by Figma.](https://help.figma.com/hc/en-us/articles/41409034424215)

## Basic tips for prompting

Whether you are a seasoned builder or you're writing your very first prompt, getting a great plugin or shader usually comes down to describing what you want to the [Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799).

- **Be explicit that you want to "build a plugin" or "build a shader."** If you tell the agent to “make you a mesh gradient,” you might end up with a standard image fill without the controls to customize it.
- **Describe what you want to see.** You don't need to know how shaders and plugins work or any technical terminology—just describe what you want to see. "A soft pink glow that fades toward the edges" typically works better than "use a radial gradient blur."
- **Name the controls you want.** If you know you'll want to adjust a specific property, specify that to the agent. For example, "I want to be able to customize the intensity of the glow" or "include a slider for blur amount and a color picker."
- **Use real-world references.** "Like a risograph print," "like a CRT monitor," "like heat haze" is more concrete to the agent than abstract adjectives. One strong reference often beats a paragraph-long description.

[Get even more prompting tips.](https://help.figma.com/hc/articles/41408020198935/)

## Extend to other Figma surfaces

Plugins and shaders are not limited to just UI frames that you’re working on—you can also extend them to other surfaces in Figma, such as:

#### Motion

Shader fills and effects can be keyframed directly in the motion timeline, making it possible to animate your fills and effects with precise timing and placement. You can also use motion to export the animation to .mp4, .webp, and .gif files. Learn more about [motion in Figma](https://help.figma.com/hc/en-us/articles/41274629073303).

#### Figma Draw

Use the Figma agent to generate procedural shapes, patterns, or layout structures directly into your illustrations. You can build a plugin that tiles a custom botanical motif across a frame, or one that generates a stipple-dot pattern from a selected path. Or build a shader fill to wrap a noise texture or gradient mesh around your artwork. Learn more about [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143).

#### Figma Make

Export shaders to Make via MCP to bring your visual effects directly into a live, coded prototype. Note that exported instances won't stay connected to the original shader yet. Learn more about [Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231).

#### Design systems

Any shader fill or effect can be saved as a style and published to your team library. Shaders can also be stacked and combined. Learn how to [create styles](https://help.figma.com/hc/en-us/articles/360038746534) and [publish styles to the team library](https://help.figma.com/hc/en-us/articles/360039820134-Manage-and-share-styles#publish-styles).

## Continue your learning journey

### Playground file

Want more hands on practice with generative plugins and shaders? Grab a copy of the [Config 2026 playground file](https://www.figma.com/community/file/1647513942386018246) and check out the **Generative plugins and shaders** page:

### Help center articles

For more information on how to build generative plugins and shaders, check out:

- [About building plugins](https://help.figma.com/hc/en-us/articles/41407987481879)
- [Prompting tips for generative plugins and shaders](https://help.figma.com/hc/en-us/articles/41408020198935)
- [Manage and update generated plugins and shaders](https://help.figma.com/hc/en-us/articles/41408937853463)
- [AI collection: Build your own shaders fills and effects](https://help.figma.com/hc/en-us/articles/41159710233623)

For information on how to use plugins and shaders in your designs, check out:

- [Use plugins in files](https://help.figma.com/hc/en-us/articles/360042532714)
- [Use shaders in designs](https://help.figma.com/hc/en-us/articles/41175721167767)

### Build even more

Want more ideas on what to ask the agent to build? Here are a few more ideas for you to try:

> *Build a plugin that finds all text layers with missing or mismatched font styles (in other words, the text using a font not in my local library) and highlights them with a colored overlay.*

> *Build a shader fill that looks like crumpled paper or fabric.*

> *Make a duotone shader effect that looks like a screen-printed poster. I want to remap the layer to two colors that I choose—one for shadows, one for highlights.*

> *Create a Voronoi pattern shader fill where I can control cell density, edge thickness, and whether it looks organic or geometric.*

## FAQ

#### What is the difference between generative plugins and classic plugins?

There are a few differences between generative plugins and classic plugins such as environment in which their built, third-party API support, and UI customization. Using the agent to build plugins is a great option if you don’t want to write the code yourself, while the classic way of building plugins is great if you want more control over the code.

To learn more, check out the article [About building plugins in Figma](https://help.figma.com/hc/en-us/articles/41407987481879).

#### What does this mean for creators of classic plugins?

You do not need to change the way you build or host plugins today. We don’t expect the introduction of generative plugins to change the usage of your plugins.

We’re continuing to invest in APIs and developer resources for partners and individuals who want to build plugins in their individual development environment and host plugins locally.

If you would like to migrate your plugin to be hosted by Figma and maintained through the agent, we will make this option available soon.

#### Do generative plugins and shaders cost AI credits?

Only when you are building and editing them using the Figma agent will you be charged [AI credits](link). It does not cost AI credits to run plugins and shaders.

#### How do I share an generative plugin?

Generative plugins live in your file and travel with it. If you run a plugin, editors in the file can also run the plugin from the **Tools** section of the right sidebar when nothing is selected.

Publishing to the Figma Community and private generative plugins for organizations are coming soon.

#### How do I share a shader?

Any shader fill and shader effect can be turned into a [style](https://help.figma.com/hc/en-us/articles/360039238753) and [published to team libraries](https://help.figma.com/hc/en-us/articles/360025508373). Shaders can also be stacked on top of another and turned into styles.

Publishing shaders to the Figma Community is coming soon.

#### Can I export to code?

Not yet, but we are actively working on making this available.

#### How do I export shaders using the MCP?

To learn more about how to export shaders via the Figma MCP, check out the [Tools and prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/) article from Figma’s developer docs.

#### Can I monetize plugins and shaders?

You can [monetize classic plugins in the Community](https://help.figma.com/hc/en-us/articles/360040035974), but it’s not yet possible to monetize generative plugins and shaders.
