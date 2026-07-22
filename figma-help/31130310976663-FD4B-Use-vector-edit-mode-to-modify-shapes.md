---
기술지원명: FD4B: Use vector edit mode to modify shapes
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Use vector edit mode to modify shapes
출처링크: https://help.figma.com/hc/en-us/articles/31130310976663-FD4B-Use-vector-edit-mode-to-modify-shapes
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

![](https://help.figma.com/hc/article_attachments/31130308393111)

## Create the squish shape

For this next shape, we’re going to explore using vector edit mode to modify a [vector path](https://help.figma.com/hc/en-us/articles/360040450213-Vector-networks).

1. Add a `46` X `48` rectangle inside the **Shape 4** frame.
2. Center it inside the frame.
3. To enter vector edit mode:
   - Select the rectangle and press `Enter`
   - Double-click on the rectangle
4. Hover your cursor over the center of the shape's top path. Figma will display a new point in the center of the path.
5. Click on it to add a new point to the path.

We want to move this point towards the center of the shape. There are a few ways to move points:

- Click and drag the point with your cursor
- Use your arrow keys to nudge it
- (**Recommended for this lesson**) Change the position values in the right sidebar

Let's walk through the third option together:

1. Select the point you just added.
2. In the **Y** field in the **Position**section of the right sidebar, type `+15`.
3. Press `Enter`.

The point will move 15 pixels toward the center of the shape.

![An animation demonstrating how to use math to change the position of a vector point on the canvas.](https://help.figma.com/hc/article_attachments/31405083069079)

To achieve the bowtie look we're going for, we need to do the same for the shape's bottom path:

1. Hover your cursor over the center of the shape's bottom path and click to add a new point
2. Select the point and type `-15` in the **Y** field, then press `Enter`.
3. Press `Enter` to exit vector edit mode.
4. Change the shape's **Corner radius** to `8`.
5. Rename the frame to `Squish`.

![](https://help.figma.com/hc/article_attachments/31405083073431)

### Using equations to adjust values

For this lesson, we recommended using math in the position field to move the vector point. In Figma Design, you can use math equations to change the values of some properties like position, dimension, and rotation. This is an extremely helpful workflow as it is precise and flexible for even larger calculations. Learn more about [using equations to adjust values](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-position-and-dimensions#h_01HNBH5565E4FPS2WX7DFD3XRM).

If the values we used seem a little backward, it's because unlike a traditional coordinate system, the Y-axis in Figma Design—and other design tools—is flipped, meaning an increase moves the node downward instead of upward. So **increasing** the Y value +15 moved the top point 15 pixels downwards and **decreasing** the Y value -15 moved the bottom point 15 pixels upwards.

## Check your knowledge
