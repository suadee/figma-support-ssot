---
기술지원명: Motion design fundamentals: Create a bouncy square animation
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Create a bouncy square animation
출처링크: https://help.figma.com/hc/en-us/articles/41523076548503-Motion-design-fundamentals-Create-a-bouncy-square-animation
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: [Figma Motion](https://help.figma.com/hc/en-us/articles/41274629073303)
- **Topics**: [Keyframes](https://help.figma.com/hc/en-us/articles/41307938657559), [easing](https://help.figma.com/hc/en-us/articles/41414048690839), [animated components](https://help.figma.com/hc/en-us/articles/41307940738967)
- **Difficulty:** Beginner
- **Length**: 15 minutes

In this project, you’ll use Figma Motion to create a bouncy square animation, then turn it into a reusable component to create a staggered animation. Along the way, you’ll get hands-on practice adding animations to the timeline, previewing your work, and creating animated components.

![](https://help.figma.com/hc/article_attachments/41523068213271)

## Create the square

Let’s start by designing the square we’ll animate.

1. Use the  **Frame** tool to add a **200** X **200** frame to the canvas.
2. Double-click the frame name and rename it to `animation`.
3. Use the  **Rectangle** tool to create a **100** X **100** square and center it inside the frame. Rename this layer to `square`.
4. Select the `square` layer, set its  **Corner radius** to **12**, and change its fill to any color you’d like. We’re using `#4D49FC`.
5. Select the `animation` frame and click the  minus in the **Fill** section to remove its fill.

Your square should look similar to the following:

![width=](https://help.figma.com/hc/article_attachments/41523068213783)

## Animate the square

Now that the square is designed, let’s use Figma Motion to bring it to life.

### Open Figma Motion

To open Figma Motion, switch the toolbar toggle to  **Motion**. Once enabled, you’ll see the timeline across the bottom of your screen.

![imageTemplate (1) (1).png](https://help.figma.com/hc/article_attachments/41523076536727)

### Change the timeline duration

Select the `square` layer inside the `animation` frame and take a look at the timeline controls. By default, the timeline is set to `2000 milliseconds` for new animations. That’s longer than we need so update the value in the **Duration** field to `1000`.

**Becoming familiar with the timeline controls**

If you're new to working with the timeline, here's a quick explanation of each setting:

![](https://help.figma.com/hc/article_attachments/41523076537623)

A. **Play:** Click **Play** or press `Spacebar` to preview your animation. Click **Pause** or press `Spacebar` again to stop the playback.

B. **Auto-keyframe:** When enabled, any change you make to an object is automatically recorded as a keyframe on the timeline.

C. **Current time:** Shows the playhead's current position on the timeline. Enter a value to jump to a specific point in time.

D. **Duration:** Shows the total length of the timeline. Enter a value to increase or decrease it.

E. **Time unit:** Shows the time unit displayed on the timeline. Click to toggle between seconds and milliseconds.

F. **Playback:** Controls how the animation repeats. Click to cycle between once, loop, and ping-pong.

G. **Collapse layers:** Collapses or expands all layers on the timeline.

### Create the scale animation

We want our square to scale from 0% to 100% over 400 milliseconds. We’ll build this animation backwards, starting with the final state.

1. Move the playhead to the **400 millisecond** mark by clicking and dragging it, or by typing **400** in the **Current time** field.
2. Select the `square` layer. In the right sidebar, click  **Add keyframe** next to the **Motion scale X** and **Motion scale Y** fields to add a new keyframe to the timeline. Since this is our end state, leave the value set to `100%`.
3. Move the playhead back to the **0 milliseconds** mark.
4. Click  **Add keyframe** next to **Motion scale X** and **Motion scale Y** again, then change the value to `0%`. Setting the scale to `0%` will hide the `square` layer until you preview the animation.
5. Click  **Play** or press `Spacebar` to preview your animation.

![](https://help.figma.com/hc/article_attachments/41523068219671)

### Update the easing curve

Your square should now be scaling from 0% to 100% over the course of 400 milliseconds. Let’s update the easing to give the animation a bit of playfulness.

**What is easing?**

Easing is what makes motion feel organic and real. In nature, nothing moves at a perfectly uniform speed due to friction, gravity, or air resistance. Objects gain momentum as they start moving and lose it as they come to a stop. Easing replicates that physical logic by controlling whether an object accelerates or decelerates across the duration of an animation. Without easing, motion feels robotic and mechanical. Learn more about [easing](https://help.figma.com/hc/en-us/articles/41414048690839).

1. Click the line that appears between the two keyframes to access the **Easing** menu.
2. The easing is currently set to a custom Bézier curve. Open the **Easing** menu and select **Ease in and out back**. This will add a small wind-up and overshoot to the motion, giving our animation a bit of bounciness.
3. Click  **Play** or press `Spacebar` to preview your animation.

![](https://help.figma.com/hc/article_attachments/41523076538263)

## Turn the animation into a main component

Animations don’t have to be rebuilt from scratch every time you want to use them. You can turn your animations into main components to reuse again and again throughout your designs.

To create a main component:

1. Switch the toolbar toggle to  **Design**.
2. Select the `animation` frame and click  **Create component** in the right sidebar or use the shortcut:
   - **Mac:** `Option` `Command` `K`
   - **Windows:** `Ctrl` `Alt` `K`
3. Switch the toolbar toggle back to  **Motion**.

## Use instances to create a staggered animation

Now that your animation is a main component, you can add instances of it to create more complex animations.

1. Add a new **800** X **800** frame to the canvas.
2. Select your `animation` main component and duplicate it to create an instance using the shortcut:
   - **Mac:** `Command` `D`
   - **Windows:** `Control` `D`
3. Click and drag the instance into the new frame you just created.

Take a look at the timeline. You’ll notice that animated instances look a bit different than other layers. Instances appear as purple layer tracks on the timeline. You can click and drag the layer track to reposition it, but you cannot change its duration or any animations applied to it. You’ll need to make those changes at the main component level.

![](https://help.figma.com/hc/article_attachments/41523068221207)

Add as many instances as you’d like and play around with staggering their start times. Here are a few ideas to spark your inspiration.

![](https://help.figma.com/hc/article_attachments/41523076542871)![](https://help.figma.com/hc/article_attachments/41523076543127)![](https://help.figma.com/hc/article_attachments/41523076544407)

## What’s next?

Great job! You just created a bouncy square animated component using shapes, keyframes, and easing! If you’re looking for another challenge, try adding some additional animations to your main component to increase the complexity of the animation.

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the [Figma Community.](https://www.figma.com/community)
