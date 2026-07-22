---
기술지원명: Create a strawberry illustration using pattern fills, vector networks, and effects
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a strawberry illustration using pattern fills, vector networks, and effects
출처링크: https://help.figma.com/hc/en-us/articles/33025308147223-Create-a-strawberry-illustration-using-pattern-fills-vector-networks-and-effects
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Draw
- **Topics**: [Pattern fill](https://help.figma.com/hc/en-us/articles/31616030150167-Use-patterns-as-a-fill-or-stroke), [Pencil tool](https://help.figma.com/hc/en-us/articles/31440438150935-Draw-with-illustration-tools), [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers), [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers)
- **Difficulty:** Intermediate
- **Length**: 15 minutes

In this project, we’ll transform a basic ellipse into a sweet strawberry illustration that looks like it was sketched by hand. Along the way, we’ll use a pattern fill for the strawberry seeds, sketch out the leaves and stem with the Pencil tool, and use effects to add highlights and shadows. Let’s go!

![An image showing the final strawberry illustration. ](https://help.figma.com/hc/article_attachments/33025308140695)

Prefer to learn by watching? Follow along with the video tutorial below.

## Open Figma Draw

We’ll be using Figma Draw to create this illustration. Figma Draw is a set of visual design tools within the Figma Design editor. To switch to Figma Draw, select  **Draw** in the toolbar. Learn more about [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw).

![](https://help.figma.com/hc/article_attachments/33025312584087)

## Create the strawberry

We’ll start by modifying a basic ellipse to create the strawberry’s body:

1. From the **Shape tools** menu in the toolbar, select **Ellipse** or press O on your keyboard.
2. Click on the canvas to add a **100** X **100** ellipse.
3. Rename the layer to `Strawberry`.
4. Change the fill to a pinkish-red: `#E94E58`.
5. Select the ellipse and press `Enter` to open vector edit mode.
6. Select the bottom point of the ellipse and type `+20` in the **Y position** field in the right sidebar. This will move the point 20 pixels downward on the canvas.
7. With the bottom point still selected, click  **Mirror angle and length** in the right sidebar, then drag the handles to shorten the length, making the point slightly sharper. Learn more about [handle mirroring](https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers#h_01JTK1ZQM89CJ4QWXGJ34JJBTG).
8. Press `Enter` to close vector edit mode.

![](https://help.figma.com/hc/article_attachments/33025344171927)

**Using equations to adjust values**

Instead of eyeballing changes on the canvas or relying on mental math, you can use equations to quickly and precisely adjust layer values like position, dimension and rotation. You can change these values by **adding**, **subtracting**, **multiplying**, or **dividing** the existing value. You can also use **parentheses** ( ) within the field for more complex equations, or **carets** ^ for creating exponents.

If the values we used seem a little backward, it's because unlike a traditional coordinate system, the Y-axis in Figma Draw—and other design tools—is flipped, meaning an increase moves the point downward instead of upward.

[Adjusting layer values](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-position-and-dimensions#h_01HNBH5565E4FPS2WX7DFD3XRM)

### Create the seed

The berry is starting to come together, but we can’t strawberry without seeds! Let’s create those next.

1. Select the **Strawberry** layer and duplicate it using the keyboard shortcut:
   - **Mac**: `Command` `D`
   - **Windows**: `Control` `D`
2. Rename the new layer to `Seed`.
3. Resize the **Seed** layer to **4** X **8**.
4. Change the fill to a reddish-brown: `#632A0B`.

![](https://help.figma.com/hc/article_attachments/33025928224919)

### Apply a pattern fill

Now that we have our seed, let’s use a pattern fill to add them to the berry.

1. Select the **Strawberry** layer.
2. In the **Fill** section, click the  plus to add another fill and choose  **Pattern** as the fill type.
3. Click **Select source**, then select the **Seed** layer.
4. Use the settings to configure the pattern:
   - **Tile type:** `Hexagonal`
   - **Direction:** `Horizontal`
   - **Scale:** `100%`
   - **X spacing:** `370%`
   - **Y spacing**: `100%`
   - **Alignment:** `Center`
   - **Opacity** `100%`
5. Once you’re happy with the pattern, delete the **Seed** layer. Pattern fills persist even if the source layer is deleted.

![](https://help.figma.com/hc/article_attachments/33025942277399)

**Using pattern fills**

Pattern fills are a great way to add visual interest to your designs. The pattern’s source references another object on the canvas in the same file. This could be a single layer, or multiple layers in a group or frame.

Pattern fills are dynamic. If you update the pattern’s source, the pattern will automatically update on each layer where its used, enabling creative experimentation without disrupting your workflow.

[Pattern fills](https://help.figma.com/hc/en-us/articles/31616030150167-Use-patterns-as-a-fill-or-stroke)

### Add a stroke

The seed pattern looks great! Now, let’s add a stroke to the berry:

1. Select the **Strawberry** layer and click the  plus in the **Stroke** section to add a stroke.
2. Change the stroke weight to `2` and the fill to `#632A0B`.

![](https://help.figma.com/hc/article_attachments/33026047593495)

### Apply a texture effect

We’ll use a texture effect to help achieve the hand-drawn, organic look:

1. With the **Strawberry** layer selected, click the  plus in the **Effects** section and choose  **Texture** from the dropdown menu.
2. Use the effects settings to configure the texture:
   - **Size:** `20`
   - **Radius**: `1.5`

![](https://help.figma.com/hc/article_attachments/33026217774103)

## Create the leaves and stem

Let’s set the strawberry aside for a bit. Next, we’ll use the Pencil tool to create the line work for the leaves and the stem.

### Draw the leaves

1. Select the **Pencil** tool from the toolbar or press `Shift` `P`.
2. Set the stroke weight to `2` and change the fill to the same reddish-brown: `#632A0B`.
3. Click and drag your cursor to sketch out the leaves. Use the **Strawberry** layer as a guide to help you with size and placement of the leaves. Rough sketches are fine! We’ll learn how to smooth them out shortly.
4. Rename the layer to `Leaves`.

![](https://help.figma.com/hc/article_attachments/33026232142231)

### Verify the vector path is closed

Before moving on, let’s make sure the vector path we drew is closed. We’ll need a closed path in order to add a fill later on.

1. Select the **Leaves** layer and press `Enter` to open vector edit mode.
2. Select the  **Paint** tool and hover over center area. If the area is highlighted, the path is closed.
3. If the path is open, locate the start and end points of the path.
4. Click and drag one point over the other until you see a  dot appear on your cursor, then release to close the path.

![](https://help.figma.com/hc/article_attachments/33026327287191)

### Use delete and heal to simplify the path

When you create vector paths with the Pencil or Brush tool, vector points are automatically added as you draw. The number of points created is determined by the length and complexity of the path. This process may create more points than you want, which can make the path look rough. Luckily, you can use **delete and heal** to create smoother curves. This handy feature removes unwanted vector points and automatically calculates a smoother, more elegant curve in their place. The following image demonstrates how delete and heal can improve a bumpy path while maintaining the original shape’s integrity:

![An image demonstrating the before and after of using delete and heal.](https://help.figma.com/hc/article_attachments/33026374650135)

1. Make sure you’re still in vector edit mode. If you closed it, select the **Leaves** layer and press `Enter` to open it again.
2. Select the **Lasso** tool from the toolbar. Then click and drag to select a group of points. Keep in mind, every point you select will be involved in the path simplification process. Deleting and healing too many points can result in an over-simplified shape.
3. Hold `Shift` and press `Delete` to delete and heal the selected points.
4. Continue simplifying section of the path until you’re happy with the shape.
5. Press `Enter` to close vector edit mode.

![An animation demonstrating how to use delete and heal. ](https://help.figma.com/hc/article_attachments/33026360249623)

### Give the leaves a fill

Once you’re happy with the shape and position of your leaves, it’s time to give them a fill:

1. Select the **Leaves** layer.
2. Click the  plus in the **Fill** section and change the fill to a medium green, like `#0FA328`.
3. Position the **Leaves** layer on top of the strawberry.

![](https://help.figma.com/hc/article_attachments/33026458935831)

### Draw the stem

We’ll also use the Pencil tool to draw the stem:

1. Select the **Pencil** tool from the toolbar or press `Shift` `P`.
2. Sketch out a small triangle for the stem.
3. Make sure the path is closed using the method we learned above, then give the stem the same brown fill you used for the seed: `#632A0B`.
4. Reposition the stem on top of the strawberry.
5. Select all three layers and group them using the keyboard shortcut:
   - **Mac:** `Command` `G`
   - **Windows:** `Control` `G`
6. Enter `-30` in the **Rotation** field in the right sidebar to tilt the strawberry.

![](https://help.figma.com/hc/article_attachments/33026458937239)

## Apply the final effects

Nice work! Before we wrap things up, let’s add some polish with highlights, shadows, and texture.

### Add the highlight

We’ll start by applying a highlight effect to give our berry some shine:

1. Select the group. then select  **Inner shadow** from the dropdown menu in the **Effects** section.
2. Use the effects settings to configure the highlight:
   - **X position:** `6`
   - **Y position:** `4`
   - **Blur:** `0`
   - **Color**: `FFFFFF`
   - **Opacity:** `25%`
3. In the effects settings, select  **Blend mode**.
4. Choose **Soft light** from the blend mode options. This will diffuse the highlight, creating a more subtle effect.

![](https://help.figma.com/hc/article_attachments/33026550259991)

### Add a shadow

Next, we’ll use an inner shadow to give our berry some depth:

1. Select  **Inner shadow** from the dropdown menu in the **Effects** section of the right sidebar.
2. Use the effects settings to configure the inner shadow:
   - **X position:** `-11`
   - **Y position:** `-7`
   - **Blur:** `0`
   - **Color**: `000000`
   - **Opacity:** `25%`

![](https://help.figma.com/hc/article_attachments/33026646771863)

### Apply a texture effect

Finally, we’ll apply another texture effect to give the entire illustration the same hand-drawn look:

1. Select  **Texture** from the dropdown menu in the **Effects** section of the right sidebar.
2. Use the effects settings to configure the texture:
   - **Size:** `1`
   - **Radius**: `0.5`

![](https://help.figma.com/hc/article_attachments/33026646773527)

## What’s next?

Nice work! You just created an illustration using shapes, pattern fills, vector edit mode, and effects. Ready to jam on some more ideas? Consider:

- Making a [custom brush style](https://help.figma.com/hc/en-us/articles/31440438150935-Draw-with-illustration-tools#h_01JTGWWRYPVZ5CYYHVD5TMJ3BM) to add a unique flair
- Experimenting with [transforms](https://help.figma.com/hc/en-us/articles/31440427042839-Create-patterns-with-transforms) to create interesting patterns and using them as [pattern fills](https://help.figma.com/hc/en-us/articles/31616030150167-Use-patterns-as-a-fill-or-stroke)
- Creating additional fruit illustrations to build a collection

If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.
