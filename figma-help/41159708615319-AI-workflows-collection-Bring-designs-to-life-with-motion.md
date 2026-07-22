---
기술지원명: AI workflows collection: Bring designs to life with motion
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Bring designs to life with motion
출처링크: https://help.figma.com/hc/en-us/articles/41159708615319-AI-workflows-collection-Bring-designs-to-life-with-motion
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

![Motion exercise 2.png](https://help.figma.com/hc/article_attachments/41438002597655)

Rachel is a product designer at Cheddar, a budgeting app with a playful, trend-forward aesthetic. Cheddar uses several different data visualization components across the app, and Rachel wants to bring them to life with motion.

That means figuring out how each chart should animate, what easing feels right for the brand, how the choreography should work when everything loads together.

And once those creative decisions are made, there's a whole other layer of work: applying that style consistently across every component, and going back to refine when something doesn't feel right.

When combined with motion design knowledge and some prompting know-how, Figma’s agent becomes a powerful sidekick for both motion design exploration and execution.

In this article, you'll learn how Figma’s agent can support 3 motion workflows:

- [Explore multiple motion variants to evaluate directions quickly](#h_01KVTWQJ851826GP8SEV2FCDVK)
- [Apply a consistent motion style across multiple elements at once](#h_01KVTWQJ8ENNQEH4XYBXTEQ7XK)
- [Make precise bulk edits to refine motion across an entire file](#h_01KVTWQJ8K2M2KNWJVAHWAPSC0)

You'll practice with hands-on exercises using the Cheddar chart designs along the way.

## Explore multiple motion variants with the Figma agent

One of the most powerful ways to use Figma’s agent for motion is to explore multiple variations at once. You might use this approach to compare distinct animation directions or evaluate different approaches to a specific motion detail.

When creating motion variants from scratch, consider including some of the following in your prompt:

|  | **What to include** | **Examples** |
| --- | --- | --- |
| Number of variants | How many different options do you want the agent to generate? | “Create 3 motion variants…” |
| Elements to animate | Which parts of the design should have motion, and which shouldn’t? | Mention specific frame or layer names |
| Intent | What are you trying to decide or explore? | Comparing different entry styles, testing whether the animation fits the product personality |
| Feel | How should the animation feel? | Snappy and energetic, slow and considered, playful, cinematic |
| Properties to vary | Which specific motion properties should differ between variants? | Easing curve, spring tension, duration, stagger interval |
| What stays constant | What should the agent hold fixed across all variants? | Total duration, entry direction, which elements animate |

You don't need to include all of these in your prompt, but they can provide a helpful starting point for the agent to work with.

## Now you try!

Let's try using the Figma agent to explore motion variants for this chart component.

### 1. Copy the chart component into a file

First, click **Copy design layers** on the image below and paste the **monthly spending chart design** from your clipboard into a [new Figma Design file](https://figma.new).

![](https://help.figma.com/hc/article_attachments/41437986659607)

### 2. Run the prompt with the agent

Click  **Agents** in the left navigation bar of your file, then paste the prompt below into the chat and set the agent to work.

```
Create 3 motion variants for this stacked bar chart. Animate the groups of colored bars as one shape, not the axes, gridlines, labels, or container. Each variant should have a distinct feel: one snappy and data-driven, one playful with a bounce, one cinematic and deliberate. Vary the easing and stagger between variants but keep the total duration consistent across all three.
```

Then, switch the toolbar toggle to  **Motion,** select each chart frame, and press play to view the results.

![Screenshot 2026-06-22 at 5.53.37 PM.png](https://help.figma.com/hc/article_attachments/41438002602647)

Narrowing from three options to one is usually faster than getting the first one right. From here, you might pick the variant that feels closest to right and dial in the timing, easing, and choreography until it feels exactly right.

[](https://help.figma.com/hc/article_attachments/41436257998103)

## Apply motion to several elements at once with Figma’s agent

Sometimes, you’ll need to apply the same, or similar, motion style across multiple elements in a design or component library. A single prompt can apply animation across several elements at once.

There are a few of ways you can guide the agent for bulk edits:

- **Reference existing motion:** Point the agent to a component that already has animation applied and it will use that as the source of truth.
- **Describe motion explicitly:** If nothing exists yet, describe what you want in motion terminology. The more specific you are with easing, duration, and spring values, the more consistent the results will be across every element.
- **Provide rules for how to adapt:** If the elements you’re animating vary in structure, tell the agent how to adapt. For example: *"Scale the movement distance based on each card's height."*

## Now you try!

We’ll build on the chart component from the previous example. Here, we want to apply the motion style we added to the first chart to other components in the set.

### 1. Copy the chart component into a file

First, click **Copy design layers** on the image below and paste the **chart designs** from your clipboard into your design file. The first chart has motion already applied, and the other charts don't have any keyframes.

**Tip**: Frames with motion applied have a  **Motion** icon on the canvas.

![](https://help.figma.com/hc/article_attachments/41437986661655)

### 2. Run the prompt with the agent

Click  **Agents** in the left navigation bar of your file, select **all** of the chart frames, then paste the prompt below into the chat and set the agent to work.

```
Apply the same animation style as the monthly spending chart to the other chart designs. For each chart, reveal the data in the direction it flows: vertical bars grow up from the baseline and horizontal bars grow left to right. Ensure that these all animate together on the same duration.
```

Then, switch the toolbar toggle to  **Motion,** select each chart frame, and press play to view the results.

[](https://help.figma.com/hc/article_attachments/41436241491735)

Notice how the agent applied the same motion style across the chart set while adapting the animation to fit each chart's structure.

**Tip**: To play all the charts at once: select them all, then right-click and select **Frame selection**. Press play on the parent frame to play all the child frames at once.

## Applying specific, targeted changes with Figma’s agent

Once you know the motion change you want to make, the agent can apply it consistently across an entire file. This is especially useful for large-scale refinements that would otherwise require editing dozens of keyframes manually.

As you spend time working with the agent in Motion, it's worth investing in the fundamentals so you can speak the language. The [Figma Motion design fundamentals collection](https://help.figma.com/hc/en-us/sections/41236726027287-Motion-design-fundamentals-collection) is a good place to start.

## Now you try!

We’ll build on our animated charts from the previous sections. Here, we’ll make a specific, targeted edit to all of them at once.

### 1. Copy the designs into a file

First, click **Copy design layers** on the image below and paste the **chart designs** from your clipboard into your file. Each of the charts has motion applied.

![](https://help.figma.com/hc/article_attachments/41437986663319)

### 2. Run the prompt with the agent

Click  **Agents** in the left navigation bar of your file, select **all** of the chart frames, then paste the prompt below into the chat and set the agent to work.

```
Change the easing on every keyframe across all selected frames to a custom spring with a bounce of 0.35. Keep all keyframe values and timing positions exactly as they are.
```

With this prompt, notice how the agent updates over 100 keyframes across multiple designs at once. Instead of manually adjusting each keyframe, you can describe the change once, and the agent takes care of the changes.

[](https://help.figma.com/hc/article_attachments/41436705547415)

Motion design involves a constant cycle of exploration, iteration, and refinement. Figma’s agent can help accelerate each stage of that process, making it easier to test ideas, compare approaches, and make changes at scale. That gives you more time to focus on evaluating the work and deciding what feels right for your product.
