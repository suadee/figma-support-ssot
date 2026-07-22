---
기술지원명: Prompting tips for generative plugins and shaders
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Prompting tips for generative plugins and shaders
출처링크: https://help.figma.com/hc/en-us/articles/41408020198935-Prompting-tips-for-generative-plugins-and-shaders
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Generated plugins and shaders are currently in open beta.** Features may change and you may experience performance issues as we continue to improve generated plugins and shaders. Learn more about [what's included in the beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

Whether you are a seasoned builder or you're writing your very first prompt, getting a great plugin or shader usually comes down to describing what you want to the [Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799). Luckily, the agent understands natural language well, so you don’t need to know code or technical language to achieve this!

In this article, we’ll cover tips on how to better prompt the Figma agent to get to the plugin or shader tool that you want.

![gen-resources-from-figma-banner-no-labels.png](https://help.figma.com/hc/article_attachments/41455874876055)

**New to generative plugins and shaders?** Check out our [quick start guide](https://help.figma.com/hc/en-us/articles/41147702210071) to learn more.

## Tips for prompting plugins

![banner-plugin.png](https://help.figma.com/hc/article_attachments/41456360607767)

### Tip 1: Tell the agent you want a plugin

If you’re looking to generate a plugin, it’s important tell the agent explicitly. That way, it knows to write code for a tool that you can reuse.

**For example**

✅  “Build me a plugin that generates button variants.” This tells the agent that you want a plugin that you can use again and again.

❌ “Create button variants.” The agent creates layers on the canvas rather than building you a plugin.

### Tip 2: Describe what the plugin should do

Tell the agent what the plugin should do from a user-facing perspective, such as the user flow, end results, or deliverable. No need to tell the agent how to build the plugin.

The more concrete your description, the fewer back-and-forth rounds. Here are a few things to consider including:

- **What will the plugin act on?** Perhaps it will act on a current selection, a specific layer type, or the whole document.
- **What will the plugin produce?** Perhaps it will build a chart, create a component set, or rename layers.
- **If any, what does the user journey look like**?

**For example**

✅ **Descriptive**: ”Build a plugin that finds all text nodes using a specific font and replaces them with another font I choose.”

❌ **Vague:** "Make a text replacement plugin.”

✅ **Descriptive:** “The plugin should include a button that runs on the current selection and resets all stroke widths to 1px.”

❌ **Vague:** "The plugin should fix strokes.”

## Tips for prompting shaders

![banner-shader.png](https://help.figma.com/hc/article_attachments/41456314460823)

### Tip 3: Use the correct trigger word

If you want a shader with controls that you can reuse, tell that to the agent explicitly.

**For example**

✅  “Build me a shader that creates mesh gradients.” This tells the agent that you want a shader with controls to generates the mesh gradient.

❌ “I want a mesh gradient.” The agent may insert a single layer with a mesh gradient applied instead of building you a shader tool.

### Tip 4: Reference real-world analogies

Real-world analogies are easy for the Figma agent to understand and interpret as they are often more specific than a paragraph of abstract description. For example, you can say:

- “like a CRT monitor from the 80s”
- “like a duotone risograph print”
- “like a heat haze”

You can also reference other experiences and examples such as:

- Real life textures or scenes, such as “the look of an oil slick on wet pavement”
- Mood or feelings, such as “dreamy and a little out of focus, like a memory”
- Where it’ll be used, such as “a calming background for a meditation app screen”

### Tip 5: Describe what you want to see

If you ever describe what you *don’t* want (negative descriptions), make sure to also describe what you *do* want (positive descriptions) to the agent. Negative descriptions, like ”nothing too busy” or “not too loud”, are vague, which makes it challenging for the Figma agent to act on. The positive version of what you want is more specific and actionable.

- Instead of saying "not too harsh,” try saying "subtle and diffuse, like light through frosted glass"
- Instead of saying "make it look cool,” try saying "a soft pink glow that fades out over about 40px from the layer edge"

### Tip 6: Identify what should stay the same

Shader effects are applied to the entire layer by default, which can lead to accidental over-processing of a layer and losing important properties that should persist.

When building and iterating, tell the agent which visual properties should survive the treatment, and call out anything that's off-limits.

**For example**

- **Legibility:** “The text should still be clearly readable at small sizes. Don't let the effect obscure the letterforms."
- **Shape:** "Keep the edges crisp and preserve detail in the line work. No feathering or soft falloff at the layer boundary.”
- **Color:** "Don't shift the color—just add texture on top of the existing colors."
- **Transparency:** "The transparent areas should stay transparent"
- **Brand:** "The fill colors should stay within the brand palette. You can shift the lightness or saturation, but don't change the hue.”

### Tip 7: If you’re stuck on wording

If you can picture the shader you want but don't know how to describe it, try dropping in a reference image and asking the agent: *"Can you describe the visual effect in this image so I can use it to build a shader?"* The agent will translate the visual into descriptive language you can then refine and use as your prompt.

## Additional tips

![banner-combined-plugin-shader.png](https://help.figma.com/hc/article_attachments/41456314462999)

### Tip 8: Work with the agent to figure out controls

You don’t need to explain upfront what controls you want for your plugin. If you’re not sure, the agent can always provide recommendations for you to choose from.

If you have an idea of the controls you want for your plugin, but you don’t know what mechanics are needed to make them happen, tell the agent what the plugin user should be able to do.

**For example**

- “I want to be able to select the number of variants in this component set generator”
- “Let me control how blurry the vignette gets”

### Tip 9: Explore available controls

The Figma agent can build a number of in-panel and on-canvas controls for your plugins and shaders. Knowing what is available can help you ask for the right ones.

Some of the most commonly used controls in agent-built plugins and shaders include:

- Color picker
- Slider
- On/off toggle
- Dropdown
- Number input
- On-canvas handle

[See a full list of available controls](https://help.figma.com/hc/en-us/articles/41306719221143).

### Tip 10: Plan to iterate

Your first result won't always be your final one, and that's normal. Each prompt teaches you a bit more about how to describe what you want. If something looks off, tell the agent what to change and try again. Small, clear adjustments usually get you closer than starting over.

## Put it all together

### Plugin example

**Prompt**

> *"Build me a plugin that scans the current page for text layers using a font that isn't in the local library. For each one, place a small colored flag next to the layer on the canvas: red for a missing font and yellow for a missing weight or style. Then show a summary panel that lists those layers by name, with a 'Select' button next to each so I can jump right to it. Add a toggle so I can scan just my current selection instead of the whole page."*

**Breakdown**

| Part of the prompt | Tip it's applying |
| --- | --- |
| "Build me a plugin that…" | Tell the agent you want a plugin |
| "scans the current page" | What the plugin acts on |
| "place a small colored flag… show a summary panel" | What the plugin produces |
| "a 'Select' button next to each so I can jump right to it" | What the user journey looks like |
| "Add a toggle so I can scan just my current selection" | Work with the agent to figure out controls |

### Shader example

**Prompt**

> *"Build me a shader that adds a grain and noise texture, like the surface of high-quality uncoated paper. The grain should feel dense and fine, not chunky. The texture should sit on top of whatever color I apply to the layer, not replace it. Let me control the grain density and overall opacity."*

**Breakdown**

| Part of the prompt | Tip it's applying |
| --- | --- |
| "Build me a shader that…" | Use the correct trigger word |
| "like the surface of high-quality uncoated paper" | Reference real-world analogies |
| "dense and fine, not chunky" | Describe what you want to see |
| "sit on top of whatever color I apply, not replace it" | Identify what should stay the same |
| "Let me control the grain density and overall opacity" | Work with the agent to figure out controls |
