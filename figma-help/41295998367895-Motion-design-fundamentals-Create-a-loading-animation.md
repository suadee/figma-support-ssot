---
기술지원명: Motion design fundamentals: Create a loading animation
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Create a loading animation
출처링크: https://help.figma.com/hc/en-us/articles/41295998367895-Motion-design-fundamentals-Create-a-loading-animation
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: [Figma Motion](https://help.figma.com/hc/en-us/articles/41274629073303)
- **Topics**: [Arc tool](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings), [keyframes](https://help.figma.com/hc/en-us/articles/41307938657559), [easing](https://help.figma.com/hc/en-us/articles/41414048690839)
- **Difficulty:** Beginner
- **Length**: 15 minutes

In this project, you’ll use Figma Motion to create two loading indicators: one with a smooth, linear rotation and one with a path trim animation that grows and shrinks as it spins. Along the way, you’ll get hands-on practice adding keyframes to the timeline, using the path trim feature, and previewing your work.  
![](https://help.figma.com/hc/article_attachments/41336075292567)

## Create the loading indicator design

We’ll start by designing the loading indicator.

1. Use the  **Frame** tool to add a **200** X **200** frame to the canvas
2. Double-click the frame name and rename it to `linear`.
3. Use the  **Ellipse** tool to add a **80** X **80** ellipse and center it inside the frame.
4. Select the ellipse and press `Shift` `X` to swap its fill and stroke, then update the **Stroke fill** to `#FFEEDA`.
5. Set the **Stroke position** to **Center** and the **Stroke weight** to `14`.
6. Rename the layer to `background`.
7. Select the ellipse and duplicate it using the shortcut:
   - **Mac:** `Command` `D`
   - **Windows:** `Control` `D`
8. Rename the new layer to `spinner`.
9. Select the `spinner` layer and set the stroke fill to `#FFA73C`.
10. Hover over the duplicated layer until you see the **Arc** handle appear. Click and drag the handle to set the arc sweep to `40%` and the ratio to `100%`. You can also set these values in the **Appearance** section of the right sidebar.
11. Set the stroke’s end points to **Round**.

![imageTemplate (8) (1).png](https://help.figma.com/hc/article_attachments/41336111679767)

## Create the linear loading indicator

Nice work! Of course, a loading indicator that doesn’t move is just a fancy circle. Next, we’ll switch to Figma Motion and start adding some movement.

### Open Figma Motion

To open Figma Motion, switch the toolbar toggle to  **Motion**. Once enabled, you’ll see the timeline along the bottom of your screen.

![](https://help.figma.com/hc/article_attachments/41336156416151)

### Change the timeline duration

By default, the timeline is set to `2000 milliseconds` for new animations which is a bit longer than we need. Select the `linear` frame and change the timeline to `1400 milliseconds` using the **Duration** field in the timeline controls.

![](https://help.figma.com/hc/article_attachments/41336220898071)

**Note:** If your timeline is showing seconds instead of milliseconds, click the label next to the **Duration** field in the timeline controls to toggle the time unit.

### Add the keyframes

Next, we’ll add keyframes to the timeline to build our motion.

**What are keyframes?**

Keyframes are the building blocks of motion design. A keyframe marks a point in time where you set a specific value for a layer property, such as opacity, position, or rotation.

To create motion, you need at least two keyframes: one for the start state and one for the end state. Figma Motion fills in the gaps between keyframes to create a smooth animation. Learn more about [keyframes](https://help.figma.com/hc/en-us/articles/41307938657559).

Rather than adding keyframes manually, we’ll use auto-keyframe to help us build our motion. When auto-keyframe is active, keyframes are automatically added to the timeline as you make changes to your design.

1. Select the `spinner` layer.
2. Click  **Toggle auto-keyframe** in the timeline controls. You’ll know it’s active when a red line appears across the top of the timeline and on the playhead.
3. Click and drag the playhead to the **1400 millisecond** mark.
4. In the right sidebar, enter `360` in the  **Motion rotation** field. Take a look at the timeline. Auto-keyframe automatically added two rotation keyframes to the timeline: one at the **0 millisecond** mark with a value of **0 degrees**, and another at the **1400 millisecond** mark with a value of **360 degrees**.
5. Click  **Toggle auto-keyframe** again to disable it.
6. Click  **Play** or press `Spacebar` to preview your animation.

![](https://help.figma.com/hc/article_attachments/41336429725719)

### Adjust the easing

Nice work! Next, we’ll adjust the easing so that the motion is linear.

**Why use linear motion?**

Most animations use easing to mimic the natural acceleration and deceleration of objects in the real world. However, loading indicators are designed to repeat indefinitely, making this one of the rare cases where uniform, linear movement actually feels right. Learn more about [easing](https://help.figma.com/hc/en-us/articles/41414048690839).

To update the easing:

1. Click the line that appears between the two keyframes to access the **Easing** menu.
2. The easing is currently set to a custom Bézier curve. Open the **Easing** menu and select **Linear**.
3. Click  **Play** or press `Spacebar` to preview your animation again.

![](https://help.figma.com/hc/article_attachments/41336501196823)

## Create the path trim loading indicator

The linear version looks great! But if you want something with a little more personality, path trim lets you build a loading indicator that grows and shrinks as it spins.

### Duplicate the linear loading indicator and update the arc sweep

1. Select the `linear` frame and duplicate it using the shortcut:
   - **Mac:** `Command` `D`
   - **Windows:** `Control` `D`
2. Rename the new frame to `trim path`.
3. Switch the toggle to  **Design**.
4. Select the `spinner` layer inside the `trim path` frame.
5. In the **Appearance** section of right sidebar, change the arc’s **Sweep** to `60%`.
6. Switch the toggle back to  **Motion**.

![imageTemplate (10) (1).png](https://help.figma.com/hc/article_attachments/41336644967447)

### Update the rotation keyframes

Because we duplicated the `linear` frame, the rotation keyframes we applied earlier were also duplicated. Let’s update them now.

1. Double-click on the keyframe at the **1400 millisecond** mark to jump to it on the timeline.
2. Change the **Rotation** value from `360` to `-185`.

![Screen Recording 2026-06-18 at 3.39.53 PM.gif](https://help.figma.com/hc/article_attachments/41336644968855)

### Add the path trim keyframes

Next, we’ll add new keyframes for the path trim properties.

**How does path trim work?**

Every vector path has a start and end point, each expressed as a percentage from 0-100%. Path trim lets you control how much of that path is visible at any given moment to create things like draw-on effects, erase effects, handwriting animations, and looping spinners.

**Note:** Path trim is only available for center-positioned strokes.

![](https://help.figma.com/hc/article_attachments/41336644970007)

1. Select the `spinner` layer inside the `trim path` frame.
2. Move the playhead to the **0 millisecond** mark.
3. Click  **Toggle auto-keyframe** in the timeline controls.
4. In the **Stroke section** of the right sidebar, enter `20%` in the  **Path trim end** field.
5. Move the playhead to the **750 millisecond** mark, then enter `100%` in the  **Path trim end** field.

**Tip:** You can move the playhead either by clicking and dragging it on the timeline, or by entering a time mark in the **Current time** field in the timeline controls.

![](https://help.figma.com/hc/article_attachments/41336722010775)

Next, set the trim path start keyframes.

1. Move the playhead to **650 millisecond** mark, then enter `20%` in the  **Path trim start** field.
2. Move the playhead to the **1400 millisecond** mark, then enter `80%` in the  **Path trim start** field.
3. Click  **Play** or press `Spacebar` to preview your animation. Your loading indicator should stretch and shrink as it rotates.

![](https://help.figma.com/hc/article_attachments/41336725593111)

## What’s next?

Great job! You just animated two loading indicators using keyframes, easing, and the arc tool! If you’re looking for another challenge, try using different animations to create another loading indicator variation.

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the [Figma Community.](https://www.figma.com/community)
