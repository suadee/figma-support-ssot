---
기술지원명: AI workflows collection: Build your own plugins inside Figma Design
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Build your own plugins inside Figma Design
출처링크: https://help.figma.com/hc/en-us/articles/41159704839831-AI-workflows-collection-Build-your-own-plugins-inside-Figma-Design
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

![](https://help.figma.com/hc/article_attachments/41406787388439)

**Story time!**

Rachel is designing a new icon set for Cheddar, a budgeting app. The team has simple line icons, but now each one needs a more branded treatment: a filled background shape, a two-color palette, consistent padding, centered vector artwork, and size variants for 16, 24, and 32 px.

Rachel duplicates an icon, adds the background shape, applies the right colors, scales the vector, adjusts the stroke, then adds each size back into the right component set.

Then she does it again. And again. Every icon needs the same treatment, and small styling changes means revisiting the whole set. If the team changes the icon scale, swaps circles for rounded squares, or updates the color treatment, Rachel has to manually update dozens of assets and hope nothing drifts out of alignment.

Generative plugins let you extend what you can do inside a Figma Design file without writing the plugin code yourself. You describe the tool you need, and the Figma agent builds a plugin that can run on the canvas.

In this article, we’ll step into Rachel’s shoes and use the agent to build a plugin for a deterministic icon-styling workflow. We’ll also explore other types of generative plugins you can use in your design workflows.

#### Before we begin: Should Rachel build a skill or a plugin for this workflow?

There are two approaches Rachel could take to this workflow: [create a skill](https://help.figma.com/hc/en-us/articles/41159668700311) or build a plugin. Which approach should she pick?

- A **plugin** works best when the workflow is **deterministic**: the same input should produce the same result every time.
- A **skill** is a good choice when you want an agent to interpret context, make judgment calls, or adapt its approach from prompt to prompt. With an agent involved, the workflow becomes **non-deterministic**: the same input may produce different results each time.

Rachel’s icon workflow has clear rules: Choose a background shape, apply a primary and accent color, scale and center the vector, generate the selected size variants, and add them to the component set.

Since those steps should run consistently every time, it makes sense to use the agent once to build a plugin, rather than calling on it for every conversion.

## Now you try: Build Cheddar’s icon transformation plugin

In this exercise we’ll use a detailed prompt below to try and create Rachel’s icon transformation as close as possible on the agent’s first try.

### 1. Copy the icons into a file

First, click **Copy design layers** on the image below and paste the icon layers from your clipboard into a [new Figma Design file](https://figma.new).

![](https://help.figma.com/hc/article_attachments/41406808540183)

### 2. Run the prompt with the agent

Click  **Agents** in the left navigation bar of your file, then paste the prompt below into the chat and set the agent to work.

```
Create a Figma plugin that turns the currently selected canvas icon into styled icon components matching the existing icon component sets.

Plugin UI:

- Selection section: show the selected icon name or preview.
- Style section: primary color, accent color, and background shape.
    - Primary default: #850056
    - Accent default: #FF91F2
    - Background options: circle or rounded square
- Sizes section: selectable buttons for 16, 24, and 32.

Transformation rules:

- Create one icon for each selected size.
- The output frame should be exactly the selected size.
- The background shape fills the full frame and uses the primary color.
- The selected icon vectors are scaled to 70% of the frame and centered directly inside the background.
- Do not wrap the icon vectors in an extra frame.
- Apply the accent color as both fill and stroke to every icon vector.
- Scale stroke weights proportionally for each output size.
```

**Tip**: A simpler prompt, like “Make a plugin that styles icons”, would likely take more back and forth with the agent to get to the same outcome.

In general, we recommend starting with the strongest prompt you can to ground the agent in what you want. Even with a detailed prompt, it might take a couple of tries for the agent to get it exactly right.

[Learn more about prompting generative plugins.](https://help.figma.com/hc/articles/41408020198935/)

### 3. Run the plugin

When the agent has finished, click **Run plugin** from the chat. Then select one of the unstyled icons as input for the plugin to work from and run it.

![](https://help.figma.com/hc/article_attachments/41406787391639)

Bonus: Think about other ideas you could extend this plugin. For example:

- Automatically add the generated icons to their component sets
- Apply a naming convention to the icons
- Hook into variables

**Note**: This exercise includes icons from [Lucide](https://lucide.dev/icons/), a free and open source icon library.

## Work with the agent to create your own plugins

Generative plugins truly let you push Figma into new territory and unlock new possibilities on the canvas. They give you finer control, deeper expressivity, and the freedom to build tools beyond what is available by default in Figma.

[Check out the quick start guide to learn more about creating agent-built plugins.](https://help.figma.com/hc/articles/41147702210071/)

**Tip**: Figma has lots of generative plugins for everyone to try. To find them:

1. Open a Figma design file, click **Tools** from the navigation bar.
2. Open the **Source** dropdown and select **From Figma**.
3. (Optional) Click the  **Filter** icon and select **Plugin**.

Generative plugins are indicated by a plugin icon and the **Agent-built** label upon hover of the card result.
