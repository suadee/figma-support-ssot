---
기술지원명: Create a reusable icon grid
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a reusable icon grid
출처링크: https://help.figma.com/hc/en-us/articles/18770195788951-Create-a-reusable-icon-grid
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma), [layout grids](https://help.figma.com/hc/en-us/articles/360040450513-Create-layout-grids-with-grids-columns-and-rows), [shapes](https://help.figma.com/hc/en-us/articles/360040450133-Basic-shape-tools-in-Figma-design), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma)
- **Difficulty**: Beginner
- **Length**: 10 minutes

In this project, we’ll be creating a reusable 24 x 24 icon grid in Figma Design. An icon grid is a prepared frame that gives you consistent guidelines for designing icons. Since icons typically exist in a set, it’s important to maintain visual consistency from one icon to another. To learn more about using icon grids, check out [System icons](https://m2.material.io/design/iconography/system-icons.html) from Material Design.

To build our icon grid, we’ll do the following:

1. [Create a frame](#h_01HE8QK68XM6Y84VZ2KEYWZH5R)
2. [Enable the layout grid](#h_01HE8QQATF3XR3YK9Z4BDFASBW)
3. [Draw the orthogonals lines](#h_01HE8QZPNJN23Z00H0BY74P0NH)
4. [Add the key shapes](#h_01HE8RNKKCXVWS16RZRAA0BVYG)
5. [Turn the icon grid into a component](#h_01HE8S544R4XMWYRVWA0395HP5)

When we're done, the final layout grid will have a 20 x 20 pixel safe area for your icon designs with a two pixel wide trim area. Let’s get started!

## An image of the final icon grid. Create a frame

The frame is our icon grid’s foundation. It’s the containing element where the icon designs will live. Icons that aren’t contained within the icon grid’s frame may be cropped or misaligned so it’s important that your designs stick to a consistent size. Frame size requirements vary between different icon sets. For this icon grid, our frame is going to be a 24 x 24 square.

To create the frame:

1. Click the  **Frame** tool in the toolbar or press `F`.
2. Click and drag the **Frame** tool while holding `Shift` to create a 24 W x 24 H frame. You can also use the **Height** and **Width** settings in the right sidebar to adjust the size.
3. Double-click the frame name and rename it to “Icon grid”.

## Enable the layout grid

Layout grids help align objects within a frame. They also provide visual structure to help keep designs logical and consistent across different platforms and devices. For our icon grid, the layout grid will be a 1:1 match with a pixel grid.

To enable the layout grid:

1. Select the **Icon grid** frame.
2. Click the  **plus** next to **Layout grid** in the right sidebar to enable the grid.
3. Click  **Layout grid settings**.
4. Change the grid size to `1`. If desired, you can also change the grid’s opacity and color.

Before moving on, let’s make sure we have a few settings enabled that will make the rest of the tutorial much easier.

**Enable the snap to settings**

When resizing objects, moving layers, or moving vector points, we can use the **snap** **to** settings to help us align them to other elements on the canvas. When enabled, a red guide appears on the canvas as a visual indicator.

To enable the **snap to** settings:

1. Click the  **Main menu**.
2. Hover over **Preferences** and make sure there’s a check next to each **snap to** setting.

**Change small nudge value**

You can use your arrow keys to nudge objects on the canvas. By default, the small nudge is set to `1`. For this tutorial, we’ll set it to `0.5` to give us more control.

To change your small nudge value:

1. Click the  **Main menu**.
2. Hover over **Preferences** and click **Nudge amount**.
3. Type `0.5` in the **Small nudge** field and close the modal.

## Draw the orthogonal lines

Orthogonals are lines that help us align icons against common angles to maintain symmetry and visual balance.

### Create a line sample

To ensure that our orthogonal line values are consistent, we’re going to draw a line above the Icon grid frame. We’ll be able to copy the line’s properties and apply them to different objects later in the tutorial to save some time.

1. Select the  **Pen** tool from the toolbar or press `P`.
2. Click on the canvas in two places to create a line above the **Icon grid** frame.
3. Close the **Pen** tool by clicking **Done** in the toolbar or by double-pressing `Esc`.
4. Select the line you just drew and adjust the properties in the **Stroke** section in the right sidebar to match the following:
   - **Fill:** `FF0000`
   - **Opacity:** `100%`
   - **Position:** `Center`
   - **Weight:** `0.2`

When you’re done, it should look similar to the following:

![](https://help.figma.com/hc/article_attachments/25275795219863)

### Add the orthogonal lines

1. Using the **Pen** tool, create two points inside the Icon grid frame and then close the **Pen** tool.
2. Select the  **Move** tool from the toolbar or press `V` and drag the points to the upper-left and lower-right corners of the frame.
3. Select the line and duplicate it using the shortcut:
   - **Mac:** `⌘ Command` `D`
   - **Windows:** `Control` `D`
4. With the duplicated line still selected, use the `Shift` `H`shortcut to flip it horizontally. Drag it to the upper-right and lower-left corners to form a large “X” in the frame.
5. Enable the **Pen** tool again and create two more points. This will be our vertical center line. Use the **Move** tool to drag the points to the edge of the frame.
6. Duplicate the line twice and move one line three pixels to the right and the other line three pixels to the left of the center line.
7. Duplicate the three vertical lines and hold `Shift` while rotating them until they are horizontal.

Before moving on, check to make sure your frame looks similar to the following:

![](https://help.figma.com/hc/article_attachments/25275795234327)

## Add the key shapes

Our icon grid is almost done but we have one more important step: adding key shapes. Key shapes are predefined objects that help you maintain consistent visual proportions as you design an icon set. The key shapes will consist of one ellipse, one square, one portrait rectangle, and one landscape rectangle. These common shapes provide a standard template you can use for designing icons.

### Add the ellipse

1. From the **Shape tools** dropdown in the toolbar, select **Ellipse** or press `O`.
2. Click to add an ellipse to the Icon grid frame. The default size will be way too big, so use the **Height** and **Width** settings in the right sidebar to resize the ellipse to 20 W x 20 H.
3. Drag the ellipse to the center of the frame. This will give us two pixels of padding on each side for the trim area.

Here’s where the line style we created earlier comes in handy. We can copy its properties and paste it to our ellipse.

To copy the line properties:

1. Select the red line above the Icon grid frame
2. Use the following copy properties shortcut to copy the style:
   - **Mac:** `⌘ Command` `Option` `C`
   - **Windows:** **Windows:** `Control` `Alt` `C`
3. Select the ellipse in the Icon grid frame and use the paste properties shortcut to paste the style:
   - **Mac:** `⌘ Command` `Option` `V`
   - **Windows:** `Control` `Alt` `V`

![](https://help.figma.com/hc/article_attachments/25277247712407)

### Add the rectangles and square

1. From the **Shape tools** dropdown in the toolbar, select **Rectangle** or press `R`.
2. Click and drag inside the frame to draw a 16 W x 20 H rectangle. You can also use the **Height** and **Width** settings in the right sidebar to manually resize the rectangle.
3. Drag the rectangle to the center of the frame.
4. Use the same process to apply the line style properties to the rectangle.
5. Change the  **Corner radius** to `1`.
6. Duplicate the rectangle and hold shift while rotating it 90 degrees.
7. Duplicate the first rectangle again.
8. Use the **Height** and **Width** settings in the right sidebar to change it to 18 W x 18 H and center it in the frame.

Before moving on, check to make sure your icon grid looks similar to the following:

![](https://help.figma.com/hc/article_attachments/31229201104919)

### Create a union

Our icon grid is looking great! However, each piece of the grid is an individual layer. We’ll use the [union selection boolean operation](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations) to combine them.

1. Select the **Icon grid** frame and press `Enter` to select all of the objects inside.
2. Click  **Union selection** in the right sidebar. You’ll notice that the **Icon grid** frame now only displays one nested layer in the **Layers** panel.
3. With the layer selected, set the opacity value of the `FF0000` fill to 10%.

## Create a component

Our icon grid is complete! Because we want this to be a reusable asset, let’s turn it into a component.

1. Select the **Icon grid** frame.
2. Click  **Create component** in the toolbar.

Congratulations! You just created a reusable icon grid. To use the icon grid, simply create an instance of the component, detach it, and start designing. If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.

![](https://help.figma.com/hc/article_attachments/25277503276439)
