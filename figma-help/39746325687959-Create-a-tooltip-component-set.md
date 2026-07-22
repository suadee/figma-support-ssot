---
기술지원명: Create a tooltip component set
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a tooltip component set
출처링크: https://help.figma.com/hc/en-us/articles/39746325687959-Create-a-tooltip-component-set
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Auto layout](https://help.figma.com/hc/en-us/articles/5731482952599-Using-auto-layout), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants)
- **Difficulty:** Intermediate
- **Length**: 20 minutes

In this project, we’re going to design a customizable tooltip component set. Tooltips are brief, informative messages that appear when a user interacts with the object they are attached to, such as icons, text links, or buttons. They’re useful when you want to provide extra information about the paired object.

Once you’ve completed this project, you’ll have a tooltip component set that covers the four major positions (top, right, bottom, left), as well as the eight minor positions, such as top-right and bottom-left. The tooltip will also grow or shrink in size depending on the length of content inside. Your final component set will have 12 variants and will look similar to the following:

![An image shoring the final tooltip component set. ](https://help.figma.com/hc/article_attachments/39746325676567)

## Create the main tooltip component

To kick things off, we’ll create the main tooltip component. This component will consist of three layers:

- A text layer that will contain the tooltip’s content
- A triangle that will serve as the tooltip’s arrow
- A frame that will contain the arrow and text layers

### Create the text layer

1. Select the  **Text** tool in the toolbar, click on the canvas, and type “Tooltip”.
2. Select the text layer and change the font size to `13`in the **Typography** section of the right sidebar. We’re using the default **Inter** font for this tutorial but feel free to pick something else.
3. In the **Fill** section, change the font color to `#FFFFFF`.
4. With the text layer still selected, use the keyboard shortcut `Shift` `A` to apply auto layout.
5. Select the text layer inside the new frame and change the  **Horizontal resizing** to `Fill container` and the  **Vertical resizing** to `Hug contents` in the right sidebar.
6. Select the frame layer and rename the layer to `Content`.
7. Open the **Width** dropdown menu in the right sidebar and click **Add max width**.
8. Set the max width to `250`.

**Why add a max width?**

Tooltips are meant to be concise and helpful. Tooltips can span multiple lines, but keep your lines short and scannable. Adding a max width to the Content layer prevents the tooltip from stretching across the screen and blocking other content.

Learn more about:

[Resizing](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties#h_01HB9Q1371C7FP7ZPSEHDN1A9B)

9. With the **Content** layer still selected, set the auto layout properties to the following:
   - Set the  **Horizontal resizing** and  **Vertical resizing** to `Hug contents`
   - Change the **Flow** to `Vertical`
   - Change the **Alignment** to `Align left`
   - Change the **Vertical gap between items** to `4`
   - Change the **Horizontal padding** to `12`
   - Change the **Vertical padding** to `8`
10. Style the frame by adjusting the following settings:
    - Click the  plus in the **Fill** section to add a fill
    - Change the fill color to `#000000`
    - Change the  corner radius to `7`

Before moving on, check to make sure your frame looks similar to the following:

![](https://help.figma.com/hc/article_attachments/39746333029527)

### Create the arrow

1. From the **Shape tools** dropdown in the toolbar, select **Polygon**.
2. Click on the canvas to add a polygon.
3. Select the polygon and press `Enter` to open vector edit mode.
4. Select the top point of the triangle and change the  corner radius to `1`.
5. Press `Enter` again to exit vector edit mode.
6. Change the triangle’s **width** to `12` and **height** to `8`.
7. Change the triangle’s fill color to `#000000`.
8. Rename the layer to `Arrow`.
9. Hold `Shift` and rotate the arrow 90 degrees.
10. Center the arrow on the left side of the **Content** layer.

![](https://help.figma.com/hc/article_attachments/39746325678359)

### Add the layers to a frame

You’ll notice that the **Arrow** and **Content** layers are not grouped. If we turned these layers into components now, each layer would become an individual component. To connect the layers, we will add the layers to a frame:

1. Select both layers, then right-click on the selection and choose **Frame selection**.
2. Rename the frame to `Tooltip/left`.

Before moving on, check the left sidebar to make sure the **Arrow** and **Content** layers are nested under the new **Tooltip/left** layer.

![](https://help.figma.com/hc/article_attachments/39746325679511)

Now we need to apply auto layout to the **Tooltip/left** frame.

1. Select the **Tooltip/left** frame and press `Shift` `A` to apply auto layout.
2. Make sure the **Clip content** checkbox is deselected in the right sidebar.
3. Set the following auto layout properties:
   - Set the  **Horizontal resizing** and  **Vertical resizing** to `Hug`
   - Change the **Flow** to `Horizontal`
   - Change the **Alignment** to `Align center`
   - Change the  **Horizontal gap between items** to `0`
   - Change the **Horizontal padding** to `0`
   - Change the **Vertical padding** to `0`
4. Style the frame:
   - Click the  plus in the **Effects** section to add a drop shadow
   - Select the drop shadow and change the blur to `16`

8. With the frame still selected, click  **Create component** to turn the tooltip into a main component.

**Why add a drop shadow?**

Applied correctly, drop shadows create a sense of depth and hierarchy on the screen. They can help gently guide the user’s eye to interactive or important elements.

You might be wondering why we applied the drop shadow to the parent frame, rather than to the **Arrow** and **Content** child layers. Drop shadows on parent-level frames are applied evenly to the child layers inside the frame, making it appear as if the layers are a single object. If we were to apply a drop shadow to each child layer, or to a group of layers, the effect would be much less seamless.

![Tooltip comparison: left shows tooltip with even drop shadow applied to a frame; right shows tooltip with less seamless shadow on a group.](https://help.figma.com/hc/article_attachments/39746333032215)

[Efects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-shadow-or-blur-effects)

Before moving on, check to make sure your tooltip looks similar to the following:

![](https://help.figma.com/hc/article_attachments/39746333032855)

## Create the major direction tooltip variants

Now that we have our main component, we can use it to add the `top`, `bottom`, and `right` tooltip variants to our component set.

First, we’ll configure the `right` variant:

1. Select the component you just created.
2. Click  **Add variant** in the toolbar to add a variant.
3. In the new variant, select the **Arrow** layer.
4. Drag the arrow to the right of the **Content** layer or press the right arrow key on your keyboard.
5. Right-click on the arrow and select **Flip horizontal** or use the keyboard shortcut `Shift` `H`.
6. Select the new variant again. In the **Current variant** section in the right sidebar, type `arrowDirection` in the **Property** field and `right` in the **Value** field. Now, all variants added to this component set will have the `arrowDirection` property.

![](https://help.figma.com/hc/article_attachments/39746325683351)

Now we need to create the `top` and `bottom` variants.

1. Select the component set and click the purple plus to add another variant.
2. Select the new variant.
3. In the **Auto layout** section in the right sidebar, change the layout flow to `Vertical layout`.
4. Select the arrow and hold `Shift` while rotating it until it points down.
5. Select the variant and change the `arrowDirection` property value to `bottom`.
6. Repeat the process for the `top` variant.

Before moving on, make sure your component set has four variants.

![](https://help.figma.com/hc/article_attachments/39746333034263)

## Create the minor direction tooltip variants

All that setup we went through will make it a lot easier for us to create the eight additional variants needed to complete our component set. Creating the minor direction variants will involve moving the arrow’s position and changing the corner radius.

1. Select the `left` variant.
2. Click the purple plus below it to add another variant.
3. Select the new variant.
4. Type `leftTop` in the **arrowDirection** property value field.
5. In the **Auto layout** section, change the alignment to `Align top left`.

Now, we need to modify the corner radius in the top-left corner so that the arrow blends in with the **Content** layer.

1. Select the **Content** layer in the new variant.
2. Select  **Independent corners** in the right sidebar.
3. Change the top-left corner’s radius to `0`.

The variant looks much better without that rounded corner.

![](https://help.figma.com/hc/article_attachments/39746325684375)

Now we can add the final variant for the left-facing tooltips.

1. Select the `leftTop` variant and click the purple plus to add another variant.
2. Select the new variant and type `leftBottom` in the **arrowDirection** property value field.
3. In the **Auto layout** section, change the alignment to `Align bottom left`.
4. Select the **Content** layer of the new variant and click  **Independent corners** in the right sidebar.
5. Change the top-left corner radius to `7` and the bottom-left corner to `0`.

Repeat the process for the remaining variants. As you add new variants, be sure to add corresponding values to the **arrowDirection** property value field. For example, `topRight`, `bottomLeft`.

Your final component set should look similar to the following:

![](https://help.figma.com/hc/article_attachments/39746325676567)

## What’s next?

Congratulations! Your customizable tooltip component set is ready to be used in your designs. If you’re looking for another challenge, modify your component set to include another variant property for an optional description field. If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.

## Additional resource

Grab a copy of the [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830) file for hands-on practice with examples and other projects from Figma's components collection.
