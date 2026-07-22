---
기술지원명: Motion design fundamentals: Create a chat bubble animation
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Create a chat bubble animation
출처링크: https://help.figma.com/hc/en-us/articles/41837837143831-Motion-design-fundamentals-Create-a-chat-bubble-animation
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: [Figma Motion](https://help.figma.com/hc/en-us/articles/41274629073303)
- **Topics**: [Preset animations](https://help.figma.com/hc/en-us/articles/41307886266135-Quickly-add-motion-with-preset-animations), [anchor points](https://help.figma.com/hc/en-us/articles/41352588622615-Move-a-layer-s-anchor-point), [exporting animations](https://help.figma.com/hc/en-us/articles/41307983648407-Export-animations-from-Figma)
- **Difficulty:** Beginner
- **Length**: 10 minutes

In this project, we’ll use Figma Motion to create an animated chat bubble. Along the way, you’ll get hands-on practice using preset animations, moving a layer’s anchor point, and exporting animations.

![](https://help.figma.com/hc/article_attachments/41838080815127)

## Create the chat bubble

We’ll start by creating a quick chat bubble design.

1. Use the  **Text** tool to add a new text layer to the canvas and enter a short message like ‘Hello there!’.
2. Use the **Typography** section to style the text. We’re using:
   - **Font family**: `Inter`
   - **Font size**: `20`
   - **Font weight**: `Regular`
3. Select the text layer and press `Shift` `A` to apply auto layout.
4. Rename the frame to `Chat bubble`.
5. Click the  plus in the **Fill** section to give the `Chat bubble` frame a fill and set it to `#1E1E1E`.
6. Set the text layer fill to `#FFFFFF`.
7. In the **Auto layout** section of the right sidebar, configure the auto layout settings:
   - **Alignment:** `Center`
   - **Horizontal padding:** `16`
   - **Vertical padding:** `12`
8. In the **Appearance** section of the right sidebar, click  **Individual corners**, then set the corner radius to the following:
   - **Top left corner radius:** `16`
   - **Top right corner radius:** `16`
   - **Bottom right corner radius:** `16`
   - **Bottom left corner radius:** `0`

Your chat bubble should look similar to the following:

![An image showing the finished chat bubble design](https://help.figma.com/hc/article_attachments/41838064158103)

### Add the chat bubble to a top-level frame

Next, we’ll add the chat bubble to a new top-level frame so we can export the animation after we build it.

1. Use the  **Frame** tool to add a **240** X **135** frame to the canvas.
2. Rename the top-level frame to `Animation`.
3. Click and drag the `Chat bubble` frame and align it in the center of the new frame.

![](https://help.figma.com/hc/article_attachments/41838118938775)

## Animate the chat bubble

Now that we’ve built our chat bubble, we can switch to Figma Motion and start animating!

### Open Figma Motion

To open Figma Motion, switch the toolbar toggle to  **Motion**. Once enabled, you’ll see the timeline across the bottom of your screen.

![](https://help.figma.com/hc/article_attachments/41838122627479)

### Move the layer’s anchor point

Because we want the chat bubble to scale up from the bottom left corner, we’ll need to move its anchor point. Rotation and scale transformations occur around an object’s anchor point. By default, the anchor point is located at the center of the object but you can move it to another location.

1. Select the `Chat bubble` frame.
2. Click **Edit anchor point** in the **Transform** section of the right sidebar or use the shortcut to reveal the anchor point target:
   - **Mac:** `Option` `R`
   - **Windows:** `Alt` `R`
3. Click and drag the target to the bottom left corner of the frame.

![](https://help.figma.com/hc/article_attachments/41838140139287)

### Add a scale animation

Now that our anchor point is set, we’re ready to start adding animations.

First, we’ll add a scale animation:

1. Select the `Chat bubble` frame.
2. Click the  plus in the **Animations** section to add a new animation.
3. Select  **Scale** from the dropdown menu, then configure the following settings:
   - **Type:** `Scale in`
   - **Amount:** `0%`
   - **Delay:** `0ms`
   - **Duration:** `250ms`
4. From the **Easing** dropdown menu, choose **Custom bezier**, then enter `0, 0, 0.3, 1.4` in the **Bezier** field to configure the custom curve.

![](https://help.figma.com/hc/article_attachments/41838163702423)

### Add a rotation animation

Next, we’ll add a rotation animation to give the chat bubble a slight wiggle as it scales in.

1. Select the `Chat bubble` frame.
2. Click the  plus in the **Animations** section to add a new animation.
3. Select  **Rotation** from the dropdown menu, then configure the following settings:
   - **Type:** `Rotate in`
   - **Direction:** `Clockwise`
   - **Amount:** `2°`
   - **Delay:** `100ms`
   - **Duration:** `180ms`
4. From the **Easing** dropdown menu, choose **Custom bezier**, then enter `0.65, -0.25, 0.44, 1.3` in the **Bezier** field to configure the custom curve.

![](https://help.figma.com/hc/article_attachments/41838234380567)

## Play your animation

Nice job! To play your animation, click  **Play** or press `Spacebar`.

![](https://help.figma.com/hc/article_attachments/41838304545431)

## Export your animation

The animated chat bubble looks great! You can export your animation to share with others or to save a copy outside of Figma.

1. Select the `Animation` frame.
2. In the **Export** section of the right sidebar, switch the tab to **Animated**.
3. Use the settings to configure your export.

**Note:** If you don’t see the **Animated** tab in the **Export** section, make sure you’re selecting the top-level `Animation` frame. Only top-level frames can be exported as animations.

![](https://help.figma.com/hc/article_attachments/41838287926295)

## What’s next?

Great work! You just created an animated chat bubble using text, frames, and preset animations. If you’re looking for another challenge, switch up the timing of your animations or try a different easing curve.

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the [Figma Community.](https://www.figma.com/community)
