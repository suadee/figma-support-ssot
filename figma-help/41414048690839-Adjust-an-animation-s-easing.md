---
기술지원명: Adjust an animation's easing
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Adjust an animation's easing
출처링크: https://help.figma.com/hc/en-us/articles/41414048690839-Adjust-an-animation-s-easing
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Figma Motion is currently in open beta.** Features may change and you may experience performance issues as we continue to improve Figma Motion. Learn more about [what's included in the beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

Before you Start

Who can use this feature

Available on [any plan](https://figma.zendesk.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can adjust an animation's easing

In nature, nothing moves at a perfectly uniform speed. Friction, gravity, and air resistance mean objects gain momentum as they start moving and lose it as they come to a stop.

You can use easing to replicate that physical logic by controlling whether an animation accelerates, decelerates, or both.

There are two types of easing:

- [Bézier curves](#h_01KVRNX138GNWAM549SBBB8Q97)
- [Spring animations](#h_01KVRP6DF1M6DZH4HKF6KBQ23B)

## Types of Bézier curves

### Linear

![](https://help.figma.com/hc/article_attachments/41414065214359)

Creates an animation that is uniform in speed throughout.

**Best used for:** Objects where a consistent, mechanical rhythm is expected, such as spinners or progress indicators.

### Ease in

![](https://help.figma.com/hc/article_attachments/41414236026263)

Creates an animation that starts slowly and accelerates as it reaches the end of its duration.

**Best used for:** Objects that are leaving the screen or being dismissed. The slow start gives users a moment to register the movement, and the fast exit feels decisive.

### Ease out

![](https://help.figma.com/hc/article_attachments/41414236026519)

Creates an animation that starts fast and decelerates as it reaches the end of its duration.

**Best used for:** Objects that are entering the screen or appearing. The fast start gets the element into position quickly, and the slow deceleration helps it feel like it’s settling into place.

### Ease in and out

![](https://help.figma.com/hc/article_attachments/41414236027543)

Creates an animation that starts slowly, accelerates in the middle, and slows as it reaches the end of its duration.

**Best used for:** Objects moving from one position to another within the screen. Since the object stays visible the whole time, both the departure and arrival need to feel smooth

### Ease in back

![](https://help.figma.com/hc/article_attachments/41414236027671)

Creates an animation that winds up in the opposite direction before accelerating toward its end position. This creates a bounce in the animation that builds anticipation and prepares the viewer for the main action.

**Best used for:** Objects exiting the screen in contexts where a little expressiveness is appropriate. The anticipation gives the exit a sense of intention and playfulness.

### Ease out back

![](https://help.figma.com/hc/article_attachments/41414236028311)

Creates an animation that starts fast and overshoots the target position slightly before settling back into place. This adds a bounce to the animation that creates a smooth ending transition for the main action.

**Best used for:** Objects entering the screen in expressive or playful contexts. The overshoot gives the landing a sense of energy and confidence.

### Ease in and out back

![](https://help.figma.com/hc/article_attachments/41414236028951)

Creates an animation that winds up slowly, then accelerates quickly before slowing down and overshooting its end position. This creates an anticipatory bounce at the start, a quick motion, with a rebounding motion before the final state.

**Best used for:** Objects moving from one position to another within the screen in expressive or playful contexts.

### Hold

![](https://help.figma.com/hc/article_attachments/41414236029591)

Unlike the other easing curves, holds don’t create a gradual transition as the object moves from one point to another. When a hold is applied between two keyframes, the object immediately jumps to its final position and stays there for the full duration before the next keyframe begins.

Holds are useful for multi-step sequences where an object needs to pause at an intermediate state before continuing, such as a loading screen that snaps into place, and holds before the content fades in. Holds can also be used to create rhythmic animations where the timing needs to feel deliberate and precise.

## Types of spring animations

Spring animations are used to create dynamic and bouncy animation that mimics the behavior of a physical spring being stretched and released.

![](https://help.figma.com/hc/article_attachments/41414269056663)

You can choose from the following preset springs or create your own:

- **Gentle:** Creates a slow, soft spring with minimal overshoot
- **Quick:** Creates a fast, responsive spring with a short settle time
- **Bouncy:** Creates a high-energy spring with noticeable overshoot and oscillation before settling
- **Slow:** Creates a steady spring with a longer settle time and minimal overshoot

## Create custom easing curves and springs

Preset easing curves and springs are designed to work across a wide range of scenarios, but that universality can also limit the amount of personality you can add to your animation.

Custom curves let you go beyond standard motion and create distinctive movement that matches your brand’s personality. For example, a steep, snappy deceleration feels energetic and confident. A long, gradual deceleration feels calm and measured. When custom curves are used consistently, that rhythm becomes part of your brand’s motion language.

**Note:** Custom curves and springs can be saved as variables, making them reusable across your entire design system. Learn more about [easing variables](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes).

### Create a custom easing curve

You can use the curve editor to adjust the curve of an existing preset, or to create a custom curve.

A Bézier curve is defined by four values, representing two control points. Each control point has an x and y coordinate. The x axis represents the progression of time. The y axis represents the progression of the animation. A straight diagonal line from corner to corner is linear motion. Curves that bow toward the top left produce ease out behavior. Curves that bow toward the bottom right produce ease in behavior.

When a control point’s y axis goes outside the 0 to 1 range, the animation travels beyond its starting or ending value, creating the wind-up and overshoot behavior present in the back curve presets.

![](https://help.figma.com/hc/article_attachments/41414236030615)

To create a custom easing curve:

1. From the **Easing** menu, select **Custom bezier**.
2. Click and drag the handles of the curve editor, or enter a cubic-bezier value directly into the field.
3. The curve editor includes points in the lower-left and upper-right corners that indicate the start and end state of the animation. You can reset the curve editor by clicking one of these points.

### Create a custom spring animation

Custom springs give you precise control over the bounciness of your motion.

![](https://help.figma.com/hc/article_attachments/41414236031127)

To create a custom spring:

1. From the **Easing** menu, select **Custom spring**.
2. Use the spring editor or enter a value in the **Bounce** field to configure the spring.

## Adjust an animation’s easing

You can adjust an animation’s easing from the **Easing** menu. How you access the **Easing** menu depends on the type of animation you’re modifying.

### Adjust easing on a preset animation

1. Click the animation on the timeline or in the **Animations** section of the right sidebar. This will open the animation settings.
2. Choose an option from the **Easing** menu.

![](https://help.figma.com/hc/article_attachments/41414269057815)

### Adjust easing between keyframes

1. Click the line between two keyframes.
2. Choose an option from the **Easing** menu.

![](https://help.figma.com/hc/article_attachments/41414236032663)

**Getting started with animation?** Check out the [Motion design fundamentals collection](https://help.figma.com/hc/en-us/sections/41236726027287-Motion-design-fundamentals-collection) to learn the principles behind effective motion design and get hands-on practice creating animations in Figma Motion.
