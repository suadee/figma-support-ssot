---
기술지원명: Create a social media post using Figma Draw
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a social media post using Figma Draw
출처링크: https://help.figma.com/hc/en-us/articles/33990671683607-Create-a-social-media-post-using-Figma-Draw
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Draw
- **Topics**: [Vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers), [arc tool](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings), [pattern fill](https://help.figma.com/hc/en-us/articles/31616030150167-Use-patterns-as-a-fill-or-stroke), [offset vector](https://help.figma.com/hc/en-us/articles/33792861450263-Offset-a-vector-path), [text on a path](https://help.figma.com/hc/en-us/articles/360039956434-Guide-to-text-in-Figma-Design#h_01JTH0B6GEA7AVVXVS72X7ANHK)
- **Difficulty:** Intermediate
- **Length**: 15 minutes

In this project, we’ll use Figma Draw to design a social media post for a baking class. Along the way, we’ll create some vector illustrations, add a pattern fill to a frame, and use text on a path to add creative flair. By the end of this tutorial, you’ll have the skills needed to create custom posts for your own upcoming events!

![An image showing the final social media post design. ](https://help.figma.com/hc/article_attachments/34050526646167)

## Open Figma Draw

We’ll be using Figma Draw to create this illustration. Figma Draw is a set of visual design tools within the Figma Design editor. To switch to Figma Draw, select  **Draw** in the toolbar. Learn more about [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw).

![](https://help.figma.com/hc/article_attachments/34050507334807)

## Create the utensil illustrations

We’ll start by creating three utensil illustrations that we'll use for a pattern fill later on.

![](https://help.figma.com/hc/article_attachments/34050507339287)

### Create the knife

1. Select the **Pen** tool from the toolbar.
2. Set the **Weight** to `12` and the fill to `#DFAF70`.
3. Hold `Shift` and click to draw a straight path on the canvas.
4. Click  **Close** in the secondary toolbar or press `Enter` to stop editing the path.
5. Set the **Height** to `170` in the right sidebar.
6. In the **Stroke** section of the right sidebar, select **End cap round** from the **End points** options.
7. With the path still selected, press `Enter` to open vector edit mode.
8. Select  **Variable width** from the secondary toolbar, then select the bottom point.
9. Type `20` in the pink box that appears to slightly increase the width of the path.
10. Click  **Close** in the secondary toolbar or press `Enter` to close vector edit mode.
11. Select the path and duplicate it using the keyboard shortcut:
    - **Mac**: `Command` `D`
    - **Windows**: `Ctrl` `D`
12. Select the duplicated layer and set its **Height** to `70`, then use the  **Rotation** field to rotate it `-10` degrees.
13. Move the duplicated layer slightly to the left of the original until their tops are aligned.

![](https://help.figma.com/hc/article_attachments/34050507341591)

### Create the fork

Set the knife off to the side for now. We’ll create the fork next:

1. Select the longer path from the knife illustration and duplicate it.
2. Change the stroke fill to `#FACB8F`.
3. Select the **Ellipse** tool from the toolbar or press `O`.
4. Add a **90** X **180** ellipse to the canvas.
5. Select the ellipse and hover your cursor over it until you see the arc handle appear.
6. Use the arc handle to change the sweep of the ellipse to `50%`, then change the ratio to `70%`.
7. Change the  **Corner radius** to `12`.
8. Right-click on the ellipse and select **Flatten**, or use the keyboard shortcut:
   - **Mac**: `Option` `Shift` `F`
   - **Windows**: `Alt` `Shift` `F`
9. Change the ellipse’s fill to `#FACB8F`.
10. Select both layers, then select  **Align horizontal centers** and  **Align top** in the **Alignment** section of the right sidebar.
11. Set the fork aside. We’ll finish it in a bit.

![](https://help.figma.com/hc/article_attachments/34050507345687)

**Why flatten the ellipse?** You might be wondering why we flattened the ellipse layer after modifying it with the arc tool. Changing an ellipse’s arc properties only alters its appearance on the canvas, not the shape’s actual dimensions. Since using the arc tool is a non-destructive action, the bounding box maintains the same size to preserve space in case we want to modify the arc again. The same principle applies when changing the number of points on a polygon or star.

Flattening a layer causes the bounding box to hug the shape’s new geometry, which is useful when aligning it with other layers. The following image demonstrates how a bounding box’s dimensions change when a layer is flattened:

![](https://help.figma.com/hc/article_attachments/34050628033047)

[Flatten layers](https://help.figma.com/hc/en-us/articles/30101373312279-Flatten-layers) [Arc tool](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings)

### Create the spoon

Now, we’ll build our final illustration: a spoon.

1. Select the longer path from the knife illustration and duplicate it again.
2. Change the stroke fill to `#F4A43B`.
3. Set the **Height** to `130` in the right sidebar.
4. Select the **Ellipse** tool from the toolbar or press `O` and create a **90** X **100** ellipse.
5. Click and drag the ellipse until its center aligns with the top of the longer path.
6. Change the ellipse’s fill to `#F4A43B`.

![](https://help.figma.com/hc/article_attachments/34052641053847)

### Finalize the illustrations

Our illustrations look great but they’re currently made up of separate layers. We’ll use the [Union boolean operation](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations) to combine each of them into single objects with shared properties.

1. Select both layers that make up the knife.
2. Choose  **Union** from the boolean operation options. If you look at the left sidebar, you’ll notice that both layers are now nested inside a boolean group called **Union**.
3. Repeat this process for the fork and the spoon.
4. Select all three layers and click  **Align vertical centers** in the right sidebar.
5. With all three layers still selected, right-click and choose **Frame selection** or use the keyboard shortcut:
   - **Mac**: `Option` `Command` `G`
   - **Windows**: `Ctrl` `Alt` `G`
6. Rename the frame to `Utensils`.

![](https://help.figma.com/hc/article_attachments/34052622185751)

## Design the social media post

Great work so far! Now that we have our illustrations, we can start designing our social media post.

### Add a frame using a frame preset

First, we’ll need a frame that will serve as the foundation of our post. Instead of creating a custom frame, we’ll use a [frame preset](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma-Design#h_01JH5Y0VVZJVB5AXYNYAHJRV3R). Frame presets are a collection of ready-made frame sizes that help you quickly create frames for popular dimensions.

1. Select the  **Frame** tool from the toolbar or press `F`.
2. When the **Frame** tool is enabled, frame presets appear in the right sidebar.
3. Open the **Social media** section and choose **Instagram post**.

![](https://help.figma.com/hc/article_attachments/34052622187543)

### Create the background

The new frame is blank but not for long! Let’s start by using a [pattern fill](https://help.figma.com/hc/en-us/articles/31616030150167-Use-patterns-as-a-fill-or-stroke) to give the post an interesting background.

1. Select the frame and change its fill to `#FAF3E8`.
2. Click the plus in the **Fill** section to add another fill.
3. Choose  **Pattern** from the fill options.
4. Click **Select source**, then choose the **Utensils** frame we created earlier.
5. Use the settings to configure the pattern:
   - **Tile type:** `Hexagonal`
   - **Scale:** `100%`
   - **X spacing:** `20%`
   - **Y spacing:** `20%`
   - **Alignment:** `Center`
   - **Opacity:** `20%`

![](https://help.figma.com/hc/article_attachments/34052622188695)

### Create the image layer

The background looks great! Now, let’s add a space for our image.

1. Select the **Ellipse** tool from the toolbar or press `O` and create a **880** X **650** ellipse.
2. Center the ellipse inside the frame, then press `Enter` to open vector edit mode.
3. Adjust the points and bezier handles until you’re happy with the overall shape. We recommend enabling  **Mirror angle** to ensure a smooth curve when adjusting the bezier handles. Learn more about [editing vector layers](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers).
4. Select the existing fill and choose  **Image** as the new fill type.
5. Select an image from your computer or leave it as an image placeholder for now. You can crop an image to reposition it inside the shape. Learn more about [cropping images](https://help.figma.com/hc/en-us/articles/360040675194-Crop-an-image).
6. Press `Enter` again to close vector edit mode.

![](https://help.figma.com/hc/article_attachments/34052622190103)

### Create the title and tagline

Nice job! Next, we’ll use [text on a path](https://help.figma.com/hc/en-us/articles/360039956434-Guide-to-text-in-Figma-Design#h_01JTH0B6GEA7AVVXVS72X7ANHK) to add the title and tagline for our event. Text on a path lets you create text layers that follow a vector path. The image layer we just created will serve as a great path for our title and tagline.

1. Duplicate the image layer you just created.
2. Select the duplicated layer and choose  **Offset vector** from the secondary toolbar.
3. Set the offset amount to `30`. [Offset vector](https://help.figma.com/hc/en-us/articles/33792861450263-Offset-a-vector-path) is a great way to evenly add space around a vector layer’s edge, giving us some breathing room between the text and the image.
4. Once your duplicated layer is configured, select the  **Text** tool from the toolbar or press `T`.
5. Hover your cursor over the duplicated layer until you see the  text on a path icon appear.
6. Click to add a new text layer and type: `Bake it till you make it`
7. This is a great opportunity for creative exploration, so feel free to experiment with different font styles, weights, and colors. To match our design, use the **Text** section in the right sidebar to set the following properties:
   - **Font:** `Kalnia`
   - **Weight:** `Bold`
   - **Size:** `60`
   - **Letter spacing:** `-4%`
   - **Letter case (found in the Type settings):** `Upper case`
   - **Fill:** `#53360C`
8. Use the blue handle to reposition the text along the path until you’re happy with the placement.

![](https://help.figma.com/hc/article_attachments/34052622192023)

Next, we’ll create the tagline:

1. Duplicate the text layer and select **Flip text orientation** in the right sidebar.
2. Update the text to read: `Join us for a hands-on pastry baking class. No experience needed—just your love for pastries!`
3. We want the tagline to have slightly less weight than the title, so we’ll update the text properties to the following:
   - **Font:** `Instrument Sans`
   - **Weight:** `Medium`
   - **Size:** `24`
   - **Letter spacing:** `0%`
   - **Letter case (found in the Type settings):** `As typed`
4. Use the blue handle to reposition the text along the path until you’re happy with the placement.

![](https://help.figma.com/hc/article_attachments/34052859495319)

### Create the badge

The post is really coming together! Next, we’ll add a badge that we can use to highlight important information.

1. Select the **Ellipse** tool from the toolbar or press `O` and create a **300** X **280** ellipse.
2. Change the fill to `#53360C`.
3. You can leave the ellipse as-is, or use vector edit mode to modify the path similar to what we did for the image layer.

For our baking class, we’ll add two text layers to this badge to showcase the class topic:

1. Use the **Text** tool to add a new text layer and type `This week:`.
2. Change the following font properties:
   - **Font:** `Instrument Sans`
   - **Weight:** `Medium`
   - **Size:** `24`
   - **Fill:** `#FAF3E8`
3. Duplicate the text layer and type `CUSTARD TARTS`.
4. Select both text layers and group them using the keyboard shortcut:
   - **Mac:** `Command` `G`
   - **Windows:** `Ctrl` `G`
5. Select the group and the badge layer and align their  **Horizontal** and  **Vertical** centers.
6. Right-click on the selection and choose **Frame selection**.
7. Position the frame near the top-right of the image layer, then use the  **Rotation** field to rotate it `-5` degrees.

![](https://help.figma.com/hc/article_attachments/34052859496983)

### Create text layers for the time and location

Our post is just about complete. We’ll wrap things up by adding a few final text layers for the time and location of our baking class.

1. Use the **Text** tool to create a new text layer and type a location.
2. Change the following text properties:
   - **Font:** `Instrument Sans`
   - **Weight:** `Medium`
   - **Size:** `32`
   - **Letter case:** `Upper case`
   - **Fill:** `#53360C`
   1. Position the text layer near the bottom of the post and align it with the left edge of the image layer.
   2. Duplicate the text layer and change the contents to the date and time of your event.
   3. Align the new text layer with the right side of the image and change the text alignment to  **Align right**.

![](https://help.figma.com/hc/article_attachments/34052866118295)

## What’s next?

Nice job! You just designed a social media post using vector illustrations, pattern fills, and text on a path. Unlocking these skills is an important step toward creating your own custom social assets. If you’re looking for more ways to explore, try:

- Incorporating [brush strokes](https://help.figma.com/hc/en-us/articles/31440438150935-Draw-with-illustration-tools) to add a hand-painted, organic look
- Experimenting with different [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers) and [blend modes](https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects)
- Turning your design into a reusable [Figma Buzz template](https://help.figma.com/hc/en-us/articles/31271693614487-Create-and-publish-Figma-Buzz-templates)

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.
