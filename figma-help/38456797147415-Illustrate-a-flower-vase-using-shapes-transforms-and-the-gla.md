---
기술지원명: Illustrate a flower vase using shapes, transforms, and the glass effect
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Illustrate a flower vase using shapes, transforms, and the glass effect
출처링크: https://help.figma.com/hc/en-us/articles/38456797147415-Illustrate-a-flower-vase-using-shapes-transforms-and-the-glass-effect
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Draw
- **Topics**: [Shapes](https://help.figma.com/hc/en-us/articles/360040450133-Shape-tools), [transforms](https://help.figma.com/hc/en-us/articles/31440427042839-Create-patterns-with-transforms), [boolean operations](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations), [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers)
- **Difficulty:** Intermediate
- **Length**: 25 minutes

In this project, we’ll create an illustration featuring a glass vase with three flowers. We’ll start by building a background for our scene, then use shapes, gradients, and the glass effect to create a transparent vase. Finally, we’ll fill our vase with a bundle of sweet red flowers, created using shapes, transforms, and effects.

![Final flower vase illustration](https://help.figma.com/hc/article_attachments/38456862969623)

## Open Figma Draw

We’ll be using Figma Draw to create this illustration. Figma Draw is a set of visual design tools within the Figma Design editor. To switch to Figma Draw, select **Draw** in the toolbar. Learn more about [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw).

![The Figma Draw toggle in the toolbar](https://help.figma.com/hc/article_attachments/38456862972311)

## Create the background

We’ll start by creating a moody background for our illustration.

1. Select the  **Frame** tool in the toolbar, then add a **600** X **750** frame to the canvas.
2. Change the frame’s fill to `#303030`.
3. Use the  **Rectangle** tool to add a **600** X **500** rectangle to the frame.
4. Set the rectangle’s fill to a  **Linear gradient** with two stops in the following positions:
   - 0% with a fill of `#303030` at `100%` opacity
   - 100% with a fill of `#232323` at `100%` opacity
5. In the left sidebar, click the  **Lock** icon next to the rectangle layer to lock it. This prevents the layer from being accidentally moved while we continue working inside the frame.

![Create a background frame](https://help.figma.com/hc/article_attachments/38456901491991)

## Create the vase

Next, we’ll use a combination of shape layers to build our vase.

### Create the shape layers

1. Use the  **Ellipse** tool to add a **272** X **272** circle to the canvas.
2. Use the  **Rectangle** tool to add a **65** X **65** rectangle and a **120** X **25** rectangle to the canvas.
3. Select the **120** X **25** rectangle, then click  **Individual corners** in the **Corner radius** setting. Change the radius of the bottom two corners to `12`.

![Change the corner radius](https://help.figma.com/hc/article_attachments/38457044688151)

### Combine the shape layers

Now that we have all the parts of our vase, let’s put them together.

1. Center the larger rectangle at the top of the circle and the smaller rectangle at the bottom, ensuring that the shapes overlap slightly. Use the red guidelines to help you align the shapes.
2. Hold `Shift` and select all three shapes, then use the  **Union** boolean operation to combine them.
3. Use the **Position** settings to move the vase to the following coordinates:
   - **X-position:** `164`
   - **Y-position:** `318`

![Screen Recording 2026-02-06 at 1.37.02 PM.gif](https://help.figma.com/hc/article_attachments/38457163862039)

### Apply a gradient fill

Our vase is looking great! We’re ready to add color and effects to give it a translucent, glass-like look.

First, we’ll change the vase’s fill:

1. Select the vase layer and change its fill to a  **Linear gradient** with two stops in the following positions:
   - 0% with a fill of `#00C4A6` at `5%` opacity
   - 100% with a fill of `#000000` at `100%` opacity
2. Drag the darker stop to the bottom-left and the lighter stop to the top-right corners of the vase.

![Add a linear gradient to the vase](https://help.figma.com/hc/article_attachments/38457318592279)

### Apply a glass effect

Next, we’ll add a glass effect to the vase for that translucent look:

1. Select the vase layer, then open the dropdown menu in the **Effects** section of the right sidebar and select  **Glass**.
2. Change the **Glass** settings to the following:
   - **Light angle:** `66°`
   - **Light intensity:** `60%`
   - **Refraction:** `76`
   - **Depth:** `98`
   - **Dispersion:** `100`
   - **Frost:** `0`
   - **Splay:** `100`
3. Applying a glass effect to a layer automatically changes the layer’s fill opacity to `20%`. Let’s use the **Fill** section in the right sidebar to bump up the fill opacity to `40%`. Learn more about [using the glass effect](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers#h_01K0ACM7R5BDE3BQ9DXFRJ3DAP).

![Add the glass effect](https://help.figma.com/hc/article_attachments/38457387779607)

### Create the lip of the vase

Next, we’ll give the vase a rounded lip.

1. Add a **74** X **16** rectangle to the canvas.
2. Instead of manually adjusting the fill or adding effects, you can copy the properties you already configured on the vase and paste them onto this new layer. Right-click on the vase and navigate to **Copy/paste as** > **Copy properties**, then click on the new rectangle and navigate to **Copy/paste as** > **Paste properties**. Learn more about [copying properties between layers](https://help.figma.com/hc/en-us/articles/4412765442967-Copy-and-paste-properties-between-layers).

![Copy and paste properties between layers](https://help.figma.com/hc/article_attachments/38457828761495)

3. Click on the gradient fill in the right sidebar and adjust the stop placement so they touch the left and right center of the rectangle.

![Adjust the graident stops on the vase lip](https://help.figma.com/hc/article_attachments/38457828763671)

4. Set the  **Corner radius** for all corners to `3`.
5. Reposition the rectangle so that it slightly overlaps the neck of the vase.

![](https://help.figma.com/hc/article_attachments/38457846753943)

### Give the vase a shadow

Before we wrap up our vase, let’s add a shadow to give the illustration some depth.

1. Add a **210** X **19** ellipse to the canvas.
2. Set the ellipse’s fill to a linear gradient with two stops in the following positions:
   - 0% with a fill of `#000000` at `0%` opacity
   - 100% with a fill of `#000000` at `100%` opacity

![Add a shadow to the vase](https://help.figma.com/hc/article_attachments/38458026334871)

3. Use the dropdown in the **Effects** settings to apply a  **Layer blur** effect to the ellipse.
4. Set the **Blur** amount to `4`.

![Add a blur to the shadow](https://help.figma.com/hc/article_attachments/38458026336151)

5. In the left sidebar, reorder the ellipse layer so that it is below the other vase shapes.
6. Use the **Position** settings to move the shadow to the following coordinates:
   - **X-position:** `99`
   - **Y-position:** `635`

![Reposition the shadow](https://help.figma.com/hc/article_attachments/38458026337175)

### Add all vase layers to a frame

To wrap up our vase, we’ll add all three layers to a frame to keep things organized.

1. Hold `Shift` and select the rectangle, union, and ellipse layers.
2. Right-click on the selection and choose **Frame selection** or use the keyboard shortcut:
   - **Mac:** `Option` `Command` `G`
   - **Windows:** `Control` `Alt` `G`
3. Rename the frame to `Vase`.

![The layer order for the flower vase](https://help.figma.com/hc/article_attachments/38458099517463)

## Create the flowers

Great work so far! In this next section, we’ll create a bundle of cheerful flower stems to fill our vase.

### Create the flower head

1. Add a **17** X **17** ellipse to the canvas.
2. Hover your cursor over the ellipse, then click and drag the [arc tool](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings) handle to change the sweep to `-50%`.
3. With the ellipse layer selected, select  **Linear repeat** from the **Additional transform modifiers** menu in the right sidebar.
4. Select the **Repeat** transform you just added to open the **Transform** settings, then change the **Count** to `4` and the **Gap** to `1 unit`.

![](https://help.figma.com/hc/article_attachments/38459614492311)

5. Create another **17** X **17** ellipse and use the arc tool to change its sweep to `-50%`.
6. Duplicate the ellipse using the shortcut:
   1. **Mac:** `Command` `D`
   2. **Windows:** `Control` `D`
7. Position one ellipse on the left edge of the linear repeat group and one on the right edge.
8. Use the  **Rotation** field to set the rotation of the left ellipse to `-60°` and the rotation of the right ellipse to `60°`.

![](https://help.figma.com/hc/article_attachments/38459614493335)

9. Use the  **Polygon** tool to add a **98** X **98** triangle to the canvas.
10. Right-click on the triangle and select **Flip vertical** or use the shortcut `Shift` `V`.
11. Align the triangle to the bottom edge of the linear repeat group.

![](https://help.figma.com/hc/article_attachments/38459614496151)

12. Select the triangle and press `Enter` to open [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers).
13. Select the bottom point of the triangle and set its  **Corner radius** to `30`.
14. Press `Enter` again to close vector edit mode, then select all of the shapes and use the  **Union** boolean operation to combine them.

![](https://help.figma.com/hc/article_attachments/38459632292503)

### Add color and effects

Our flower is taking shape. Next, we’ll apply color and effects to really make it pop!

1. Select the flower and use the **Fill** section in the right sidebar to change its fill to `#FF6868`.
2. Use the **Effects** section to apply an  **Inner shadow** effect and change the settings to the following:
   - **X position:** `-11`
   - **Y position:** `-7`
   - **Blur:** `3`
   - **Color:** `#CB3F3F` at `100%` opacity
3. Apply a  **Texture** effect and change the settings to the following:
   - **Size:** `1`
   - **Radius:** `41`
   - **Clip to shape**: `Enabled`

![Give the flower a fill and texture](https://help.figma.com/hc/article_attachments/38459813779607)

### Create a second layer of petals

Next, we’ll add a second layer of petals to give our flower some depth.

1. Add a **17** X **20** ellipse to the canvas and use the arc tool to change the sweep to `-50%`.
2. Apply a linear repeat transform and set the **Count** to `5` and the **Gap** to `1 unit`.
3. Set the fill to `#B12626`.
4. Apply an  **Inner shadow** effect with the following settings:
   - **X position:** `2.5`
   - **Y position:** `3`
   - **Blur:** `3`
   - **Color:** `#E14141` at `100%` opacity
5. Apply a  **Texture** effect and change the settings to the following:
   - **Size:** `0.5`
   - **Radius:** `18`
   - **Clip to shape:** `Enabled`

![Create a second layer of petals](https://help.figma.com/hc/article_attachments/38459940712727)

6. Align the second layer of petals with the first row of petals, then move the layer below the existing flower shape in the layers panel.

![](https://help.figma.com/hc/article_attachments/38459940714519)

### Create the base of the stems

Next, we'll add a stem base to our flower. We'll use this base to connect our stems in the next section.

1. Use the  **Polygon** tool to add a **25** X **25** triangle to the frame.
2. Right-click on the triangle and select **Flip vertical** or use the shortcut `Shift` `V`.
3. Change the  **Corner radius** to `2`.
4. Position the layer at the base of the flower, so the layers just slightly overlap.
5. Leave the fill as-is for now. We’ll come back to it when we create the stems.

![](https://help.figma.com/hc/article_attachments/38460098996887)

### Create the yellow center

Before we move on, let's add one final touch to our flower: a cheerful yellow center!

1. Add a **25** X **25** ellipse to the canvas and change its fill to `#FFBF00`.
2. Apply an  **Inner shadow** effect with the following settings:
   - **X position:** `-11`
   - **Y position:** `-10`
   - **Blur:** `3`
   - **Color:** `#DF9705` at `100%` opacity
3. Apply a  **Texture** effect and change the settings to the following:
   - **Size:** `1`
   - **Radius:** `18`
   - **Clip to shape:** `Enabled`

![Create the yellow center](https://help.figma.com/hc/article_attachments/38460093114647)

4. Position the yellow circle at the horizontal center of the flower with the top just slightly above the petals, then reorder its layer position so that it is between both sets of petals.
5. Select all four layers of the flower and add them to a frame.
6. Rename the frame to `Flower`.

![](https://help.figma.com/hc/article_attachments/38460245077271)

### Add flowers to the illustration

Great work! Now we're ready to add our flowers to the illustration frame.

1. Select the flower frame and duplicate it twice using the shortcut:
   - **Mac:** `Command` `D`
   - **Windows:** `Control` `D`
2. Arrange the three flowers around the vase. Exact placement is not important so feel free to play around with different positions and rotations.

![Add flowers to the illustration](https://help.figma.com/hc/article_attachments/38460228203031)

## Create the stems

To finish our illustration, we’ll use the **Pen** tool to draw some stems.

1. Select the  **Pen** tool in the toolbar.
2. Set the **Stroke weight** to `6`, then click inside one of the stem bases you added in the previous section to add your first point.
3. Continue to reposition the **Pen** tool and clicking to add additional points until you reach the bottom of the vase.
4. Enable the  **Bend** tool and click on each point to curve the path for a more natural looking stem. You can then use the  **Move** tool to adjust the bézier handles and change the length and slope of the curve.

![](https://help.figma.com/hc/article_attachments/38460309020951)

### Add colors and effects

1. Select the stem base and the stem, then use the  **Union** boolean operation to combine them.
2. Set the **Fill** to `#8DBB52`.
3. Apply an  **Inner shadow** effect with the following settings:
   - **X position:** `-4`
   - **Y position:** `-5`
   - **Blur:** `4`
   - **Color:** `#537F2A` at `100%` opacity
4. Apply a  **Texture** effect and change the settings to the following:
   - **Size:** `1`
   - **Radius:** `30`
   - **Clip to shape:** `Enabled`

![Create the stems](https://help.figma.com/hc/article_attachments/38460706734999)

5. Create the other two stems. Remember that you can copy and paste properties between layers to save time!

![create all three stems (1) (1).png](https://help.figma.com/hc/article_attachments/38460706735895)

### Place the flowers in the vase

Once you’re happy with your flower arrangement, it’s time to place them inside the vase.

1. Select all three **Flower** layers in the left sidebar.
2. Click and drag them below the **Vase** layer in the layer order.

Notice how the glass effect distorts and bends the layers beneath it, creating a realistic illusion that our flower stems are submerged in a glass vase filled with water!

![](https://help.figma.com/hc/article_attachments/38461053553175)

## What’s next?

Excellent work! You just created a stunning flower vase illustration using shapes, transforms, and effects. If you're looking for another challenge, use the skills you learned during this tutorial to create different flowers, add leaves to your stems, or switch up the background.

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the [Figma Community.](https://www.figma.com/community)

![Alternative flower vase illustration](https://help.figma.com/hc/article_attachments/38503064077975)
