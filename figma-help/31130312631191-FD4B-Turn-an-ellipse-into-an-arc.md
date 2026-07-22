---
기술지원명: FD4B: Turn an ellipse into an arc
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Turn an ellipse into an arc
출처링크: https://help.figma.com/hc/en-us/articles/31130312631191-FD4B-Turn-an-ellipse-into-an-arc
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

![](https://help.figma.com/hc/article_attachments/31130343603479)

On to our final shape. Let’s take a look at the design we’re recreating. As with many things in Figma Design, there are multiple ways to achieve this shape. Using boolean operations or drawing it from scratch using the **Pen** tool could work but would be a bit of a hassle. Let’s save ourselves some time and modify the ellipse’s [arc properties](https://help.figma.com/hc/en-us/articles/360040450173-Arc-tool-create-arcs-semi-circles-and-rings) instead!

The arc properties let you turn a solid ellipse into other shapes like rings or wedges. It’s a handy feature to have in your back pocket when building custom icons or illustrations.

## Create the slice shape

1. Add a `40` x `40` ellipse to the **Shape 5**frame.
2. Hover your cursor over the ellipse until you see the **Arc** handle appear. You'll use this handle to control the sweep of the arc.
3. Click it and drag it on the path of an arc to access the arc properties.
4. Two additional handles will appear: the **Start** handle, which controls where the arc begins, and the **Ratio** handle, which allows you to change the ellipse into a ring. The same settings also become available in **Appearance**section of the right sidebar.
5. Select the ellipse and use either method to change the properties:

- - **Start** to `180`
  - **Sweep** to `25`
  - **Ratio** to `15`

![](https://help.figma.com/hc/article_attachments/31402349732887)

### Bounding box for shapes and arcs

You may notice that the ellipse’s bounding box is still `40` x `40`, even though the shape itself now visually takes up just a small portion of that space. This isn’t something we’ve run into before so let’s dig into what’s going on here.

![](https://help.figma.com/hc/article_attachments/31402349734167)

Changing the ellipse’s arc properties only altered its appearance on the canvas, not the shape’s actual dimensions. Similar to boolean operations, changing the arc properties of an ellipse is a non-destructive action. The shape’s bounding box stayed the same size to preserve space in case we wanted to change the arc again. The same principle applies when changing the number of points on a polygon or star. Learn more about [modifying shape layers](https://help.figma.com/hc/en-us/articles/360040450133-Shape-tools).

## Flatten the shape

While our shape looks nice, it would be helpful if the bounding box better fit the shape’s geometry when we go to position it next to other layers. To achieve this, we can flatten the layer.

1. Right-click on the layer and select **Flatten**. Great! Now the bounding box hugs the new shape.
2. The shape is still too small so lets resize it to `40` x `40` using the **Dimension** fields in the right sidebar.
3. Center the shape inside the frame if you need to.
4. Rename the frame to `Slice`.

![](https://help.figma.com/hc/article_attachments/31402339470615)

### About flattening objects

[Flattening](https://help.figma.com/hc/en-us/articles/30101373312279-Flattening-objects) an object merges its layers into a single vector layer, simplifying the design, reducing the file size, and improving asset compatibility

You can flatten a selection of vector layers to merge them into a complex vector shape. Or, flatten a text layer to customize aspects of a typeface for logos or wordmarks. Flattening a container layer, like frames or sections, will merge its child layers together and remove the container layer from the canvas.

Flattening is a **destructive** action. Once an object is flattened, its individual layers cannot be separated again. To flatten an object, right-click on it and select **Flatten** or use the keyboard shortcut. If you flatten something by mistake, you can use the Undo shortcut or use the file’s version history to restore a previous version.

## Clean up and create components

Our custom shapes look great! Let’s do a few things to start cleaning them up so they're ready to use in the skill list:

1. Select all of the frames then click the  **minus** in the **Fill** section to remove the frames' fill.
2. With the frames still selected, use **Create multiple components** from the right sidebar.
3. Right click on the components and choose **Move to Page** > **Components** to move them to the components page.
