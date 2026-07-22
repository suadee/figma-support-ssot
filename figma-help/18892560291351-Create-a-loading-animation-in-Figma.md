---
기술지원명: Create a loading animation in Figma
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a loading animation in Figma
출처링크: https://help.figma.com/hc/en-us/articles/18892560291351-Create-a-loading-animation-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Shape tool](https://help.figma.com/hc/en-us/articles/360040450133-Basic-shape-tools-in-Figma-design), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [instances](https://help.figma.com/hc/en-us/articles/360039150173-Create-and-insert-component-instances), [smart animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames), [after delay](https://help.figma.com/hc/en-us/articles/360040035834-Prototype-triggers), [frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma), [rotation](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-and-position), [inline preview](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes)
- **Difficulty**: Intermediate
- **Length**: 20 minutes

In this project, we’ll be making a loading animation. Adding loading animations can help your prototype look more realistic. If you follow along step-by-step, your final prototype will look like this:

![An animation demonstrating the final loading animation.](https://help.figma.com/hc/article_attachments/24970044660759)

To achieve this design, we’ll do the following:

1. [Create a frame and four ellipses](#h_01HENJ1R2FY0ZSTQEA7ZH1W0GS)
2. [Duplicate the frame and rotate the ellipses](#h_01HENJRNJYNCYJKPEJ2Y1SD6VZ)
3. [Duplicate the second frame and resize the ellipses](#h_01HENKAJWWZ8VV05E77JA9PPPV)
4. [Add prototype connections](#h_01HENKMSFG0JZVKR5AXPA1NEM4)
5. [Create a component set](#h_01HENM0NRVD1SKE59A7YC09AGH)
6. [Add an instance to a new frame](#h_01HENMCJP9E7SBG89D7XKY8E6Z)

## Create a frame and four ellipses

To start, select the **Frame** tool in the toolbar or press `F` and click on the canvas to add a frame with 100 x 100 dimensions. Double-click the frame name and rename it to “loading/1”.

We’ll make the animation pop by making the background dark. Select the frame and change the color to `#000000` using the **Fill** setting in the right sidebar.

Now, let’s add four ellipses to the frame.

![An animation demonstrating how to add a new frame to the canvas. ](https://help.figma.com/hc/article_attachments/24794089080983)

1. From the **Shape tools** dropdown in the toolbar, select **Ellipse** or press `O`.
2. In the **loading/1** frame, hold `Shift` and then click and drag your cursor to create a 24 x 24 ellipse.
3. Duplicate the ellipse and place it on the right side of the original ellipse. Use the red guides to help with the alignment.
4. Repeat the steps ‌until you have four ellipses in the frame. Place your ellipses in the ‌top-left, top-right, bottom-left, and bottom-right corners respectively.
5. Select the **loading/1** frame and navigate to the **Selection colors** section in the right sidebar. Update the `#D9D9D9` color to `#FFFFFF`.

![](https://help.figma.com/hc/article_attachments/24794089084695)

We want to make sure the ellipses are equally distributed both horizontally and vertically, as well as center-aligned to the frame. We can do this with Smart selection.

Smart selection lets you quickly adjust the arrangement or spacing between two or more layers. Learn more about [smart selection →](https://help.figma.com/hc/en-us/articles/360040450233-Arrange-layers-with-Smart-selection)

1. Hold `Shift` and click each ellipse to select all four at once.
2. Pink handles will appear when you hover over the selection, indicating a **Smart selection** has been created.

   **Tip**: If you don’t see pink handles, use the **Tidy up** tool to rearrange the ellipses and create a Smart selection.![](https://help.figma.com/hc/article_attachments/24794089087767)
3. Click and drag the pink handles to set the vertical and horizontal spacing between ellipses to 24.
4. Click and drag the selection to snap the ellipses to the center of the frame using the red alignment guides.

![](https://help.figma.com/hc/article_attachments/24794089092247)

## Duplicate the frame and rotate the ellipses

Now, let’s create a second frame by duplicating the current frame.

1. Select the **loading/1** frame and use the duplicate shortcut to create a copy.
2. Rename the new frame to **loading/2**.
3. Select **loading/2**, and press **Enter** to select all nested layers. In this case, all four ellipses will be selected.
4. Hover your mouse near the object’s corner until the  **rotate** icon appears.
5. Hold **Shift** on your keyboard, then click and drag clockwise to rotate the ellipse's positions by -90 degrees. You can check the rotation amount in the right sidebar using the  **Angle** input field.

![](https://help.figma.com/hc/article_attachments/24799985202839)

**Note**: The frames may look identical but they aren’t! While you won’t be able to see a visual difference, you can select each ellipse to see how it’s moved locations between **loading/1** and **loading/2**. For example, the ellipse named **Ellipse 1** is placed at the top-left corner in the **loading/1** frame, and is placed at the top-right corner in the loading/2 frame. As we’ll see shortly, rotating the ellipses is a crucial step for our loading animation to work. ![](https://help.figma.com/hc/article_attachments/24799998347927)

## Duplicate the second frame and resize the ellipses

Let’s create the final frame that will tie it all together.

1. Duplicate the **loading/2** frame.
2. Rename the new frame to **loading/3**.
3. Select **loading/3**, and press **Enter** to select all ellipses.
4. Update the size of the ellipses to **60 W** and **60 H** using the settings in the right sidebar.
5. Use the  **Align horizontal centers** and the  **Align vertical centers** settings in the alignment controls panel to center all four ellipses.
6. With all four ellipses still selected, drag to place them in the center of the frame.

![](https://help.figma.com/hc/article_attachments/24799998351639)

## Add prototype connections

Now that the setup is complete, we’ll add prototype connections to get our loading animation moving.

1. Click the **Prototype** tab on the right sidebar.
2. Select the **loading/1** frame, then hover over the edge of the frame until you see the  blue plus sign.
3. Click and drag the connection to the **loading/2** frame. This opens the **Interaction details** modal.
4. From the dropdown menu, set the trigger to **After delay** and set the duration to `100ms`.
5. Set the action to **Navigate to** and the destination to **loading/2**.
6. Set the prototype animation to **Smart animate**.
7. From the animation type dropdown menu, select **Custom bezier** and set the duration to `300ms`.
8. In the Bézier curve input field, enter `0.5, -0.1, 0.5, 1.1`**.**

![](https://help.figma.com/hc/article_attachments/24799998355095)

Nice! Now we can connect the remaining frames.

1. Click and drag a prototype connection from **loading/2** to **loading/3.**
2. Set the trigger to **After delay** and duration to `100ms`. Figma remembers the previous prototype animation settings, so you don’t have to set up the animation from scratch again.
3. Create a prototype connection from **loading/3** back to **loading/1** to make a looped animation.
4. Set the trigger to **After delay** and duration to `100ms`.

Now it’s time to see our animation in action. Click the flow starting point button next **loading/1** frame to open inline preview.

![](https://help.figma.com/hc/article_attachments/24800411588119)

Looks wonderful! With just a few frames, shapes, and prototype connections, we created a loading animation. If you’re interested in using this animation on multiple pages, keep reading to learn how to turn it into a reusable component set.

**Note**: If you want to make adjustments to your loading animation, you can click the prototype connections to open the interaction details modal and adjust the curve. The inline preview will reflect the changes immediately. Hold **Shift** and select all the connections to edit them all at once.![](https://help.figma.com/hc/article_attachments/24800411591191)

## Create a component set

The loading animation looks great! But having to recreate it every time you want to use it would be a pain. Luckily, we can create a component set so you can reuse the animation again and again.

What is a component? Components are elements you can reuse across your designs. They help to create and manage consistent designs across projects. [Learn more about components →](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma)

1. Hold `Shift` on your keyboard and select all three frames.
2. From the toolbar, open the  **Create component** dropdown menu.
3. Select **Create component set**.

![](https://help.figma.com/hc/article_attachments/24801617329687)

Because our frames were named **loading/1**, **loading/2**, and **loading/3**, they are automatically turned into a component set called “loading” with three variants called “1”, “2”, and “3”. If we weren’t consistent with our naming, the component set would simply be called “Component 1”.

Let’s remove the background fill on the variants so they can be used over other designs.

1. Hold `Shift` on your keyboard, and then click on each variant to select all three.
2. Click the minus button under **Fill** in the right sidebar.

## Add an instance to a new frame

Now that we have a component set, we can add an instance of it to a new frame.

1. Click the  **Frame** icon from the toolbar, or press `F`.
2. From the **Design** tab in the right sidebar, select the **iPhone 14 Pro** preset size.
3. Update the fill to `#1D1D1D`.
4. Select the **1** variant.
5. Hold `⌥ Option` (Mac) or `Alt` (Windows) and drag the variant to create an instance. Place the instance in the center of the frame.
6. Click the  **Present** button in the toolbar to test it out.

![](https://help.figma.com/hc/article_attachments/24970044664727)

There are a few other ways to create instances in Figma. Learn more about [creating instances →](https://help.figma.com/hc/en-us/articles/360039150173-Create-and-insert-component-instances)

## What's next?

Congratulations! You’ve created a loading animation with just a few frames. If you’re looking for another challenge, try making some tweaks to the animation, adding other frames and colors like this one below.

![](https://help.figma.com/hc/article_attachments/24802509742999)

If you’re interested to learn how to create the podcast card design or the loading animation, check out the following mini projects:

- [Create a responsive card with auto layout and constraints](https://help.figma.com/hc/en-us/articles/18894664907287)
- [Create an onboarding flow with advanced prototyping](https://help.figma.com/hc/en-us/articles/18888057155991)
