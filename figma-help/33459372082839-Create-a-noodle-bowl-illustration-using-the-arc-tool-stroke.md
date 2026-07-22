---
기술지원명: Create a noodle bowl illustration using the arc tool, stroke width profiles, and effects
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a noodle bowl illustration using the arc tool, stroke width profiles, and effects
출처링크: https://help.figma.com/hc/en-us/articles/33459372082839-Create-a-noodle-bowl-illustration-using-the-arc-tool-stroke-width-profiles-and-effects
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Draw
- **Topics**: [Arc tool](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings), [stroke width profiles](https://help.figma.com/hc/en-us/articles/360049283914-Apply-and-adjust-stroke-properties#h_01JYM3N7HRXNXXC6GP79P8T246), [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers), [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers)
- **Difficulty:** Intermediate
- **Length**: 15 minutes

In this project, we’re cooking up a stylish illustration featuring some noodles and chopsticks. We’ll start by creating the bowl using the arc tool, then dive into vector edit mode to create some wavy noodles. Next, we’ll explore stroke width profiles to build the chopsticks and wrap things up by applying effects to give the illustration some texture and depth. Ready to dig in? Let’s go!

![Final noodle illustration](https://help.figma.com/hc/article_attachments/33459517350295)

## Open Figma Draw

We’ll be using Figma Draw to create this illustration. Figma Draw is a set of visual design tools within the Figma Design editor. To switch to Figma Draw, select **Draw** in the toolbar. Learn more about [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw).

![Select Figma Draw from the toolbar](https://help.figma.com/hc/article_attachments/33459471151767)

## Create the bowl

We’ll start by using the arc tool to create the bowl shape:

1. Use the **Ellipse** tool to add a **180** X **180** ellipse to the canvas.
2. Select the ellipse and hover your cursor over it until you see the arc handle appear.
3. Use the arc handle to change the sweep of the ellipse to `50%`.
4. Change the fill to any color you like. We’re using `#778859`.

![Use the arc tool to change the sweep of the ellipse](https://help.figma.com/hc/article_attachments/33459517357591)

Next, we’ll build the base of the bowl:

1. Use the **Rectangle** tool to add a **40** X **12** rectangle to the canvas.
2. Position the rectangle at the bottom of the ellipse, then select both layers and click  **Align horizontal centers**.
3. Right-click on the rectangle and select **Send to back** or press `[` on your keyboard.

![Poition the rectangle at the bottom center of the ellipse](https://help.figma.com/hc/article_attachments/33459471154711)

### Apply an inner shadow effect

Next, we’ll use an inner shadow effect to give the bowl some depth:

1. Select the ellipse layer.
2. Click the  plus in the **Effects** section and choose  **Inner shadow** from the dropdown menu.
3. Use the effect settings to configure the inner shadow:
   - **X position:** `-20`
   - **Y position:** `-20`
   - **Blur:** `0`
   - **Spread:** `0`
   - **Color:** `#000000`
   - **Opacity:** `20%`
4. Select the rectangle and press `I` to open the Eyedropper tool, then click on the drop shadow to change the fill to the same color.

![Select the rectangle and use the eyedropper tool to change the fill to the same color as the drop shadow](https://help.figma.com/hc/article_attachments/33459471156503)

### Round the corners

Next, we’ll round the corners to give the bowl a smoother appearance.

1. Select both layers and group them using the keyboard shortcut:
   - **Mac:** `Command` `G`
   - **Windows:** `Control` `G`
2. Rename the group to `Bowl`.
3. Change the  **Corner radius** to `2`.

![Round the corners of the bowl](https://help.figma.com/hc/article_attachments/33459471157783)

### Apply a texture effect

We’ll add one more effect to complete the bowl:

1. Select the **Bowl** layer.
2. Click the  plus in the **Effects** section and choose  **Texture** from the dropdown menu.
3. Use the effect settings to configure the effect:
   - **Size:** `0.7`
   - **Radius**: `20`
   - **Clip to shape**: `Enabled`

![Apply a texture effect to the bowl](https://help.figma.com/hc/article_attachments/33459517369367)

## Create the noodles

Let’s set the bowl aside and create the noodles next.

### Build the noodle shape

To create our noodles, we’ll flatten a selection of basic ellipses, then use vector edit mode to modify the new shape’s vector path:

1. Use the **Ellipse** tool to add a **25** X **25** ellipse to the canvas.
2. Select the ellipse and duplicate it using the keyboard shortcut:
   - **Mac**: `Command` `D`
   - **Windows**: `Control` `D`
3. Drag the second ellipse below the first so that their edges touch but don’t overlap.
4. Duplicate the ellipse four more times for a total of six ellipses. When you immediately use the duplicate shortcut on a duplicated object, Figma maintains the same distance between each object.

![Duplicate the ellipse until you have 6 ellipses](https://help.figma.com/hc/article_attachments/33459728202263)

Now we’ll flatten the ellipses into a single vector layer and use vector edit mode to modify the vector’s path:

1. Select all of the ellipses and press `Shift` `X` to invert their fill and stroke.
2. Select  **Flatten** from the secondary toolbar or use the keyboard shortcut:
   - **Mac**: `Option` `Shift` `F`
   - **Windows**: `Alt` `Shift` `F`
3. The ellipses are now merged into a single layer called **Vector**. Rename the layer to `Noodle`.
4. Select the **Noodle** layer and press `Enter` to open vector edit mode.
5. Starting with the top ellipse, delete the right vector point. Work your way down, alternating between deleting the left and right vector points to create a wavy shape.
6. Press `Enter` to exit vector edit mode.

![Use vector edit mode to delete alternating left and right poins of the ellipses](https://help.figma.com/hc/article_attachments/33459728203799)

Next, we’ll modify the stroke to make it look a bit more noodle-like:

1. Change the layer’s **Width** to `14`.
2. Press `Enter` to open vector edit mode again.
3. Select the  **Bend** tool from the secondary toolbar, then click on each of the center points to create a smoother connection between each ellipse.
4. Press `Enter` to close vector edit mode.

![Use the bend tool to create smoother connections between each ellipse](https://help.figma.com/hc/article_attachments/33459698973207)

Use the **Stroke** section in the right sidebar to modify the stroke’s properties:

1. Change the stroke **Weight** to `4`.
2. Select **End cap round** from the **End points** options.
3. Change the stroke fill to `#FFDB98`.

![Modify the stroke properties](https://help.figma.com/hc/article_attachments/33459698974487)

### Apply an inner shadow effect

Next, we’ll apply an inner shadow effect to highlight our noodle’s curves:

1. Select the **Noodle** layer.
2. Click the  plus in the **Effects** section and choose  **Inner shadow** from the dropdown menu.
3. Use the effect settings to configure the inner shadow:
   - **X position:** `1`
   - **Y position:** `-2`
   - **Blur:** `0`
   - **Spread:** `0`
   - **Color:** `#EEAF3A`
   - **Opacity:** `100%`

![add an inner shadow to the noodle](https://help.figma.com/hc/article_attachments/33459698978583)

### Duplicate the noodle

The noodle is looking great! Next, we’ll copy the noodle using the duplication shortcut we learned earlier and use the new layer to help give the illustration a 3D look:

1. Select the noodle and duplicate it using the keyboard shortcut:
   - **Mac**: `Command` `D`
   - **Windows**: `Control` `D`
2. Change the duplicated layer’s **Weight** to `2`.
3. Change the fill to `#EEAF3A`.
4. Position the duplicated layer against the right edge of the original layer.
5. Select both layers and group them using the keyboard shortcut:
   - **Mac:** `Command` `G`
   - **Windows:** `Control` `G`

![Duplicate the noodle and move it against the right edge of the original](https://help.figma.com/hc/article_attachments/33459728214551)

### Apply a texture effect

We’ll use a texture effect to blend the noodle’s highlights and shadows:

1. Click the  plus in the **Effects** section and choose  **Texture** from the dropdown menu.
2. Use the effect settings to configure the effect:
   - **Size:** `0.4`
   - **Radius**: `4`
   - **Clip to shape**: `Enabled`

![Add a texture effect to the noodles](https://help.figma.com/hc/article_attachments/33459698982935)

### Add a linear repeat transform

Our noodles are almost done! To wrap things up, we’ll use the linear repeat transform to add the additional noodles:

1. Open the **Additional transforms modifies** menu in the right sidebar and select  **Linear repeat**. This adds the noodles to a transform group.
2. Rename the transform group to `Noodles`.
3. Click on the transform in the right sidebar and configure the settings:
   - **Direction:** `Horizontal`
   - **Count:** `6`
   - **Gap:** `0.8 Units`

![Add a transform to the noodles](https://help.figma.com/hc/article_attachments/33459728218007)

**Why use a transform?**

Although you could duplicate the layer to add more noodles, using a transform gives you more flexibility as you build your final design.

Transforms offer ways to quickly alter layers in your designs. Similar to using boolean operations, transforms are non-destructive actions, meaning they don’t permanently alter the original layer.

When you add a transform to a layer, the layer is added to a transform group. This preserves the original layer, allowing you to select and modify it at any time. You can also add additional layers to the transform group to increase the complexity of your design.

[Transforms](https://help.figma.com/hc/en-us/articles/31440427042839-Create-patterns-with-transforms)

To wrap up our noodles, let’s position the layer near the left side of the bowl. Right-click on the **Noodles** layer and select **Send to back** or press `[` on your keyboard so it looks like they are coming out of the bowl.

![Place the noodles in the bowl](https://help.figma.com/hc/article_attachments/33459698985879)

## Create the chopsticks

Awesome job so far! We’ll finish up our illustration by using the Pen tool to create a set of chopsticks.

1. Select the **Pen** tool from the toolbar.
2. Set the **Weight** to `8` and the fill to `#C1850C`.
3. Hold `Shift` and click to draw a straight line on the canvas.
4. Click  **Close** in the secondary toolbar.
5. Use the **Width** field in the right sidebar to set the line’s width to `200`.
6. Rename the layer to `Chopstick`.

![Draw a line using the pen tool](https://help.figma.com/hc/article_attachments/33460094153111)

Next, we’ll use a width profile to achieve the chopstick’s tapered look. Width profiles are preset configurations that help you convert uniform strokes into lines with smoothly tapered ends and varying thicknesses.

**Tip:** You can also use the [Variable width tool](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers#h_01JYM29VEN8ABWTDXJR529446R) to change the width of a stroke at any point along the path.

1. In the **Stroke** section of the right sidebar, select **End cap round** from the **End points** options.
2. Open the **Width profile** dropdown and select the third option from the top.
3. Click  **Flip width points** so that the tapered end is facing left.

![Apply a stroke width profile to the line](https://help.figma.com/hc/article_attachments/33460081890839)

### Apply an inner shadow and texture effect

Similar to how we designed our bowl, we’re going apply an inner shadow and texture effect so the chopstick matches the rest of the illustration.

We’ll start by adding the inner shadow:

1. Select the **Chopstick** layer.
2. Click the  plus in the **Effects** section and choose  **Inner shadow** from the dropdown menu.
3. Use the effect settings to configure the inner shadow:
   - **X position:** `-2`
   - **Y position:** `-2.5`
   - **Blur:** `0`
   - **Spread:** `0`
   - **Color:** `#92660D`
   - **Opacity:** `100%`

![add an inner shadow to the chopstick](https://help.figma.com/hc/article_attachments/33460081892503)

Now we’ll use a texture effect to soften the inner shadow’s effect:

1. Select the **Chopstick** layer.
2. Click the  plus in the **Effects** section and choose  **Texture** from the dropdown menu.
3. Use the effect settings to configure the effect:
   - **Size:** `0.5`
   - **Radius**: `4`
   - **Clip to shape**: `Enabled`

![add a texture effect to the chopstick](https://help.figma.com/hc/article_attachments/33460094165015)

### Position the chopsticks

Let’s wrap up our illustration by duplicating the chopstick and placing them next to the other elements:

1. Select the **Chopstick** layer and duplicate it using the keyboard shortcut:
   - **Mac**: `Command` `D`
   - **Windows**: `Control` `D`
2. Select one chopstick and use the **Rotation** field to rotate it `5` degrees, then right-click on it and select **Send to back** or press `[` on your keyboard.
3. Reposition your chopsticks until you’re happy with the placement.

![Position your chopsticks around the noodles](https://help.figma.com/hc/article_attachments/33460081900183)

## What’s next?

Congratulations! You just created an illustration using the arc tool, transforms, stroke width profiles, and effects. Looking for more ideas to noodle on? Try:

- Creating the chopsticks using a [mask](https://help.figma.com/hc/en-us/articles/360040450253-Masks) instead of an inner shadow effect
- Using the [Variable width tool](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers#h_01JYM29VEN8ABWTDXJR529446R) to create a different pasta shape
- Creating additional food illustrations to build a collection

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.
