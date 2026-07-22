---
기술지원명: Create an orange illustration using transforms, effects, and text on a path
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create an orange illustration using transforms, effects, and text on a path
출처링크: https://help.figma.com/hc/en-us/articles/32588834922391-Create-an-orange-illustration-using-transforms-effects-and-text-on-a-path
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Draw
- **Topics**: [Shape builder](https://help.figma.com/hc/en-us/articles/31616004109847-Create-custom-shapes-with-the-shape-builder-tool), [transforms](https://help.figma.com/hc/en-us/articles/31440427042839-Create-patterns-with-transforms), [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers), [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers)
- **Difficulty:** Beginner
- **Length**: 15 minutes

In this project, we’ll use basic shapes and transforms to illustrate some oranges, apply effects to add depth and texture, and use text on a path to add a little zest. Let’s get started!

![An image demonstrating the final orange illustration.](https://help.figma.com/hc/article_attachments/32590201116055)

Prefer to learn by watching? Follow along with the video tutorial below.

## Open Figma Draw

We’ll be using Figma Draw to create this illustration. Figma Draw is a set of visual design tools within the Figma Design editor. To switch to Figma Draw, select  **Draw** in the toolbar. Learn more about [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw).

![](https://help.figma.com/hc/article_attachments/32590291188631)

## Create the sliced orange

Our illustration features two oranges: a whole orange and one that’s been sliced in half. We’ll create the sliced orange first.

### Create a background for the slices

We’ll start by using the **Ellipse** tool to create a background for the orange slices:

1. From the **Shape tools** menu in the toolbar, select **Ellipse** or press `O` on your keyboard.
2. Click on the canvas to add a **100** X **100** ellipse.
3. Use the **Fill** section in the right sidebar to change the ellipse’s fill to a light orange color, like `FFE0BA`.

![](https://help.figma.com/hc/article_attachments/32590389687959)

### Create the orange slices

Let’s add some slices to the background:

1. Select the ellipse and duplicate it using the keyboard shortcut:
   - **Mac**: `Command` `D`
   - **Windows**: `Control` `D`
2. Change the new ellipse’s fill to a darker orange color, like `FBB15C`.
3. Use the **Dimensions** fields in the right sidebar to change the ellipse’s **Width** and **Height** to **80** X **80**.

**Tip:** Select  **Lock aspect ratio** before changing a layer’s dimensions. Once locked, changing the width or height will automatically update the other value to maintain the same proportions.

![](https://help.figma.com/hc/article_attachments/32590450803223)

The new ellipse isn’t looking very slice-like yet. We can use the [arc tool](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings) to change that:

1. With the ellipse selected, hover your cursor over it until the **Arc** handle appears.
2. Click and drag the **Arc** handle to change the **Sweep** to `15%`. You can also adjust this value using the **Arc** settings in the right sidebar.

![](https://help.figma.com/hc/article_attachments/32589049068311)

That’s a nice slice! Rather than duplicating the layer to add more slices, we can use a transform to quickly create a repeating pattern.

**What are transforms?**

Transforms offer ways to quickly alter layers in your designs. Similar to using boolean operations, transforms are non-destructive actions, meaning they don’t permanently alter the original layer. When you add a transform to a layer, the layer is added to a transform group. This preserves the original layer, allowing you to select and modify it at any time. You can also add additional layers to the transform group to increase the complexity of your design.

[Transforms](https://help.figma.com/hc/en-us/articles/31440427042839-Create-patterns-with-transforms) [Boolean operations](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations)

1. With the ellipse layer selected, click  **Radial repeat** in the right sidebar to apply a transform. If you look at the **Layers** section in the left sidebar, you’ll notice the slice layer is now nested within a transform group called **Repeat group 1**.
2. In the right sidebar, click the **Repeat** transform you just added to open the **Transform** settings.
3. Change the **Count** to `7` and the **Gap** to `0.1 Units`.

![](https://help.figma.com/hc/article_attachments/32589147138327)

Let's adjust the slices to make them look more realistic:

1. From the **Layers** section of the left sidebar, select the ellipse nested inside **Repeat group 1**.
2. Type `120` in the  **Rotation** field in the right sidebar to rotate the layer.
3. In the **Appearance** section if the right sidebar, change the  **Corner radius** to `2`.

Because the ellipse is nested inside a transform group, any changes you make to the original layer are automatically applied to the rest of the transform group.

![](https://help.figma.com/hc/article_attachments/32589321896855)

Before we align the layers, let’s give our sliced orange a white center:

1. Use the **Ellipse** tool to add a **10** X **10** ellipse to the canvas.
2. Change the fill to `FFFFFF`.
3. Select all three layers and use the **Alignment** settings in the right sidebar to align their  **Horizontal** and  **Vertical** centers.
4. Flatten the selection by right-clicking on the selection and selecting **Flatten**, or using the keyboard shortcut:
   - **Mac:** `Option` `Shift` `F`
   - **Windows:** `Alt` `Shift` `F`
5. In the **Layers** section of the left sidebar, you’ll notice that all three layers have been merged into a single layer called **Vector**. Double-click on the layer name and change it to **Slices**.

![](https://help.figma.com/hc/article_attachments/32589368209303)

**What does flattening an object do?**

Flattening an object merges all of its layers into a single vector layer, simplifying the design, reducing the file size, and improving asset compatibility You can flatten a selection of vector layers to merge them into a complex vector shape. Or, flatten a text layer to customize aspects of a typeface for logos or wordmarks. Flattening a container layer, like frames or sections, will merge its child layers together and remove the container layer from the canvas.

Flattening is a **destructive** action. Once an object is flattened, its individual layers cannot be separated again. If you flatten something by mistake, you can use the file’s [version history](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history) to restore a previous version or use the undo shortcut:

- **Mac**: `Command` `Z`
- **Windows**: `Control` `Z`

[Flatten](https://help.figma.com/hc/en-us/articles/30101373312279-Flattening-objects)

### Create the sliced orange’s peel

Now that we have our orange segments, let's create a peel to contain them:

1. Use the **Ellipse** tool to create another **100** X **100** ellipse.
2. Change the fill to `F89523`.
3. Double-click on the layer in the **Layers** section and rename it to **Peel**.
4. Click and drag the **Peel** layer below the **Slices** layer in the **Layers** section.
5. Select the **Slices** layer and change its **Height** to `55`. This will help create the sliced effect.
6. Select both layers, then use the **Alignment** settings to align their  **Horizontal** and  **Vertical** centers.

![](https://help.figma.com/hc/article_attachments/32589555966359)

### Use vector edit mode to modify the ellipse

We’re almost done with the peel. For this next part, we’ll use vector edit mode and the Shape builder tool to modify the ellipse’s vector network.

**What are vector networks?**

Vector networks are shape layers consisting of vector paths. These paths tell Figma how to render that shape on the canvas, including where to apply the layer’s stroke and fill properties. Vector networks can basic shapes, or custom vector paths drawn using the Pen, Brush, or Pencil tools. Many vector tools only allow you to draw vector paths in a single direction, often ending at the original starting point. Vector networks are unique in that they don’t require a specific direction. They can have multiple paths that branch out in various directions without the need for creating and combining separate paths. You can use vector edit mode to select and adjust the points and paths of a vector network to modify basic shapes, refine vector illustrations, and create custom icons or logos.

[Vector networks](https://help.figma.com/hc/en-us/articles/360040450213-Vector-networks) [Editing vectors](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers)

1. Select the **Peel** layer and press `Enter` to open vector edit mode.
2. Select the **Pen** tool in the toolbar or press `P`. The ellipse’s vector network currently has four points. We’ll use the **Pen** tool to connect the left and right points, creating a new path through the center of the orange.
3. Hover your cursor over the left point until it displays a dot . This indicates that we can add a new path to the existing vector network.
4. Click to begin drawing the path and move your cursor over to the point on the right. Click again to connect the path.

![](https://help.figma.com/hc/article_attachments/32589560157847)

Now that the ellipse is divided into two regions, we can use the Shape builder tool to remove the top part of the shape:

1. Select the  **Shape builder** tool from the secondary toolbar. If you don’t see the secondary toolbar, you may have exited vector edit mode. Select the ellipse and press `Enter` to open it again.
2. Hover over the top half of the ellipse to highlight the region, then hold the following modifier key and click to remove it from the shape:
   - **Mac:** `Option`
   - **Windows:** `Alt`
3. Press `Enter` to exit vector edit mode.

![](https://help.figma.com/hc/article_attachments/32589737951639)

Before moving on, let’s group our layers:

1. Select all of the layers and group them together using the keyboard shortcut:
   - **Mac:** `Command` `G`
   - **Windows:** `Control` `G`
2. Double-click on the layer name in the left sidebar and rename it to **Sliced orange.**
3. Type `-30` in the **Rotation** field to rotate the **Sliced orange** layer.

![](https://help.figma.com/hc/article_attachments/32589737952919)

### Apply an inner shadow

Our sliced orange is taking shape! To finish it up, we’ll apply an inner shadow to the orange’s peel to give it a little depth:

1. Select the **Sliced orange** layer.
2. In the **Effects** section of the right sidebar, select  **Inner shadow** from the dropdown menu.
3. When you add an effect to a layer, you can use the settings panel to configure how it appears. Use the effects settings to configure the inner shadow:
   - **X postion**: `4`
   - **Y position**: `-8`
   - **Blur**: `0`
   - **Color**: `000000`
   - **Opacity** `25%`

![](https://help.figma.com/hc/article_attachments/32589783434263)

The shadow still looks a bit harsh. We can use a blend mode to create a more subtle effect.

**What are blend modes?**

Blend modes let you define how a layer’s pixels interact with overlapping objects like other layers, strokes, or effects. They use mathematical calculations to blend the pixels together, producing unique results. When working with blend modes, consider how these key colors impact the equation:

- **Base color**: The original color of the underlying layer
- **Blend color**: The color of the object you’re applying the blend mode to
- **Result color**: The new color resulting from the blend

Each blend mode applies a specific formula to these color values and the type of blend mode you use determines what the resulting color will be.

When applying a blend mode, you can hover over each option to see a live preview of how it looks on the canvas. Experimenting with different blend modes can reveal unexpected color relationships and help you add visual interest to your designs.

[Blend modes](https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects)

1. From the effects settings panel, select  **Blend mode**.
2. Choose **Overlay** from the blend mode options. Overlay multiples dark colors. Because the base color is light orange and the blend color is black, the result color is a dark orange that looks more like a natural shadow.

![](https://help.figma.com/hc/article_attachments/32590140388631)

## Create the full orange

The sliced orange looks great! Let’s set it aside and create the full orange.

1. Select the **Ellipse** tool from the toolbar and click to add a 100 X 100 ellipse to the canvas.
2. Change the fill to `F89523`.
3. Double-click on the layer name and rename it to **Full orange**.
4. In the **Effects** section of the right sidebar, select  **Inner shadow** from the dropdown menu.
5. Use the effects settings panel to configure the inner shadow:
   - **X postion**: `20`
   - **Y position**: `-20`
   - **Blur**: `0`
   - **Spread:** `0`
   - **Color**: `000000`
   - **Opacity** `25%`
6. In the effects settings panel, click  **Blend mode** and choose **Overlay**.
7. Click and drag the **Full orange** layer on the canvas until it’s positioned slightly behind the sliced orange, then right-click and select **Send to back**.
8. Select both layers and use the shortcut to group them together:
   - **Mac:** `Command` `G`
   - **Windows:** `Control` `G`
9. Rename the group to **Oranges**.

![](https://help.figma.com/hc/article_attachments/32590178943639)

## Add texture to the illustration

Our illustration is coming together nicely! To give it a subtle, hand-drawn look, we'll use the Texture effect:

1. Select the **Oranges** layer.
2. In the **Effects** section of the right sidebar, select  **Texture** from the dropdown menu.
3. Use the effects settings to configure the texture:
   - **Size:** `2.5`
   - **Radius**: `0.8`

![](https://help.figma.com/hc/article_attachments/32590178944151)

## Add text on a path

Let's finish our illustration by adding a curved label using [text on a path](https://help.figma.com/hc/en-us/articles/360039956434-Guide-to-text-in-Figma-Design#h_01JTH0B6GEA7AVVXVS72X7ANHK). Text on a path lets you create text layers that follow the paths of a vector object, such as a shape or brush stroke.

When you add text to a path, the vector object’s fill and effects are transferred from the vector layer to the text layer, causing the vector object to disappear from the canvas. Because we want the text to curve around the full orange, we’ll duplicate the **Full orange** layer and use it as the path for our text.

1. Select the **Full orange** layer and duplicate it using the keyboard shortcut:
   - **Mac**: `Command` `D`
   - **Windows**: `Control` `D`
2. Select the duplicated layer and press `K` to open the  **Scale** tool.
3. In the **Scale** section of the right sidebar, change the layer’s width to `120`. The layer’s height will automatically update to `120`.
4. Select the  **Text** tool in the toolbar or press `T`.
5. Hover over the edge of the duplicated layer until you see the  text on a path icon appear near your cursor.
6. Click to add a new text layer and type `Fresh squeezed`. Notice how the vector layer’s fill and effects are automatically applied to the text layer. You can change these properties at any time using the settings in the right sidebar.
7. Select the text layer and change the font weight to something heavier, like **Bold** and the font size to **16**.
8. Use the handle to adjust the text’s placement on the curve until its right where you want it.

![](https://help.figma.com/hc/article_attachments/32590140392727)

## What’s next?

Great work! You just created an illustration using shapes, transforms, effects, and text on a path. We only scratched the surface of what’s possible in Figma Draw. If you’re looking for more ways to explore, try:

- Incorporating [brush strokes](https://help.figma.com/hc/en-us/articles/31440438150935-Draw-with-illustration-tools) to add a hand-painted, organic look
- Experimenting with different [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers) and [blend modes](https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects)
- Creating additional fruit illustrations to build a collection

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.
