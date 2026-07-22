---
기술지원명: Design a search icon
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Design a search icon
출처링크: https://help.figma.com/hc/en-us/articles/18886645808023-Design-a-search-icon
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma), [layout guides](https://help.figma.com/hc/en-us/articles/360040450513-Create-layout-grids-with-grids-columns-and-rows), [shapes](https://help.figma.com/hc/en-us/articles/360040450133-Basic-shape-tools-in-Figma-design), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma) [boolean operations](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations)
- **Difficulty**: Intermediate
- **Length**: 10 minutes

In this project, we’re going to make a search icon. If you follow along step-by-step, your icon will look like this:

![An image of the final search icon design. ](https://help.figma.com/hc/article_attachments/25258750638999)

## Before you begin

You’ll need a 24 x 24 icon grid to complete this tutorial. You can find icon grid templates on the Figma Community or you can check out our [Create a reusable icon grid mini project](https://help.figma.com/hc/en-us/articles/18770195788951) if you'd like to make your own.

You'll also want to make sure the **Pixel grid** and **S****nap to pixel grid** settings are enabled to help align the elements of the search icon.

1. Click the **Zoom/view options** in the upper-right corner of the toolbar.
2. Make sure there is a check next to the **Pixel grid** and **Snap to pixel grid**settings. If there isn't, click each setting to enable them.   
   ![](https://help.figma.com/hc/article_attachments/25251137521687)

## Create the search icon lens

Let’s start by creating an ellipse inside the frame:

1. From the **Shape tools** in the toolbar, select **Ellipse** or press `O`.
2. Hold `Shift`, click and drag to create a 16 W x 16 H ellipse.
3. Drag the ellipse to the top-right edge of the icon grid.

Tip: Holding `Shift` helps maintain the proportions of the shape. You can always manually update the size of your shape by selecting the shape and dragging the handles of the bounding box, or updating the height and width using the settings in the right sidebar.

### Add stroke and remove fill

1. Click the  **plus** in the **Stroke** section.
2. Change the stroke weight to `2`.
3. Click the  **minus** in the **Fill** section to remove the fill.

![](https://help.figma.com/hc/article_attachments/25254060726807)

## Create the search icon handle

1. Press `Command` `+` (Mac) or `Control` `+` (Windows) to zoom into the bottom-left of the icon grid.
2. Select the  **Pen** tool from the toolbar or press `P`.
3. Hover over the point where the orthogonal line intersects with the center of the ellipse stroke.
4. Click on the frame to create the first point of the line.
5. Move down the line 4 pixels, and click the frame again to add the second point.
6. Click  in the toolbar or press `Enter` to exit vector edit mode.
7. Change the stroke weight to `2`.
8. Change the end points of the line to **Round**.

![](https://help.figma.com/hc/article_attachments/25258517690519)

## Combine the shapes using a boolean operation

Now, let’s combine the lens and the handle so that they form a single shape.

1. Hold Shift and select both the lens and the handle.
2. Click  **Union selection** in the right sidebar. Notice that the two layers have been combined into a layer called **Union** in the left sidebar.
3. Center the object using the alignment settings in the right sidebar. Now the icon is centered to the frame, within equal paddings on all sides.

![](https://help.figma.com/hc/article_attachments/25258750641815)

Double-click on the frame name, rename it to “search-icon” and you’re all done!

**Why use a boolean operation instead of a group?** If you use a group to combine the layers, you’ll notice that something is off. When you select the grouped object, the bounding box does not include the stroke of the handle. This might not look like a big deal, but when you try to align the grouped object to the center of the frame, the padding is not equal on all sides. Using a [boolean operation](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations) ensures that all parts of the combined shape are contained within the bounding box.

![](https://help.figma.com/hc/article_attachments/25258743426839)

## What’s next?

Congratulations on creating your search icon! If you want to challenge yourself, try making this pencil icon using the same things you learned in this tutorial.

![](https://help.figma.com/hc/article_attachments/25258743428375)

If you want to learn more about the visual guidelines and best practices for icon design, check out Material Design's [icon documentation →](https://m3.material.io/styles/icons/overview)
