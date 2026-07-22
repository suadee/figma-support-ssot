---
기술지원명: FD4B: Combine shapes using boolean operations
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Combine shapes using boolean operations
출처링크: https://help.figma.com/hc/en-us/articles/31130266267287-FD4B-Combine-shapes-using-boolean-operations
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Lesson overview

In this lesson, we’ll learn a few ways to edit vector layers and craft a skills list to showcase our areas of expertise. For a personalized touch, we’ll start by creating some custom shapes which we’ll then combine with text layers in an auto layout frame. Finally, we’ll add the skills list to a container frame and turn it into a main component.

![Skills list featuring Web Design, Team Building, Conceptual Design, User Empathy, and Data-Driven Projects with custom icons.](https://help.figma.com/hc/article_attachments/31703972186007)

Figma Design is a vector-based design tool that can be used to create scaleable assets like icons, illustrations, and user interface elements. But what are [vectors](https://help.figma.com/hc/en-us/articles/360040450213-Vector-networks) exactly? Well, vectors are digital images that consist of points, lines, and curves, all defined by mathematical formulas. Unlike raster images—such as digital photographs—vectors can be resized infinitely without losing quality, making them perfect for designs that need to adapt to various sizes.

We’ll use vector layers to create the custom shapes for our skills list. Unique touches like this are a great way to leave a lasting impression on visitors to your portfolio. We’ll guide you through five example shapes, but feel free to experiment here!

## Add five frames to the canvas

We'll start by creating some frames which will contain our shapes:

1. Create a `48` X `48` frame.
2. Rename the frame to `Shape 1`.
3. Duplicate the frame 4 times. Because we’re duplicating an object with a number in the name, Figma will automatically name the new frames `Shape 2`, `Shape 3`, and so on.

![](https://help.figma.com/hc/article_attachments/31382906124311)

## Create the inchworm shape

![](https://help.figma.com/hc/article_attachments/31382906126359)

The first shape we’re going to build consists of three rectangles with rounded corners.

1. Add a `16` X `46` rectangle and center it inside the **Shape 1** frame.
2. Set the **Corner radius** to `24` to achieve a pill look. Because the rectangle is so small, changing the corner radius to `24` is enough to fully round the corners. If the rectangle were larger, we’d need to use a greater corner radius to achieve the same look.
3. Duplicate the rectangle and change the new layer’s dimensions to `15` X `29`.
4. Drag it to the left of the original and align the bottoms of both layers.
5. With the smaller rectangle still selected, click and drag your cursor while holding the modifier key to duplicate it.
6. Drag the new layer to the right of the original, aligning the tops of both layers. The edges of all three shapes should be touching.

![](https://help.figma.com/hc/article_attachments/31382909468183)

Even though the shape looks like a single object, it’s made up of three separate layers, each with their own properties. That means we can’t apply changes—like updating the fill—without selecting each layer and if we added a stroke, it would outline each layer individually instead of the shape’s outer path.

To treat the shapes as a single object, we’ll merge the layers using the **Union** boolean operation.

1. Hold `Shift` and select all three layers.
2. Then, choose  **Union selection** from the **Boolean operations** menu.

![](https://help.figma.com/hc/article_attachments/31382909469079)

Take a look at the layers section. The three rectangle layers are now nested under a new boolean group called **Union** and we can now change the fill of the entire shape.

To keep our shapes organized once we turn them into main components, we’ll give each of them a descriptive name. Rename this frame to `Inchworm`.

![](https://help.figma.com/hc/article_attachments/31382906128791)

## About boolean operations

[Boolean operations](https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations) let you combine multiple layers into a single object with shared properties called a boolean group. You can use boolean operations to create icons, logos, illustrations, and much more.

There are four different boolean operations and it can be helpful to organize them into two groups of opposites: **Union** and **subtract**, and **intersect** and **exclude**.

### Union

**Union** combines the selected layers. If the layers overlap, the new object’s outer path is created by merging the outer edges of all the layers. This means that any strokes or effects you add will only be applied to the object’s outer path.

![An animation demonstrating the union boolean operation. ](https://help.figma.com/hc/article_attachments/31405009336343)

### Subtract

The opposite of union is **subtract**, which removes the area of a layer from the layer below it. Similar to using a cookie cutter layers at the top of the layer hierarchy cut out the area where they overlap with the layer at the bottom of the current selection. If the resulting object has both an inner and outer edge, any strokes or effects you apply will appear along both edges.

![An animation demonstrating the subtract boolean operation. ](https://help.figma.com/hc/article_attachments/31405046967319)

### Intersect

Next is **Intersect**, which creates a new object from where the original layers overlap. Anything outside the overlapping area is removed, leaving just the areas where all layers intersect. If you apply intersect to non-overlapping layers, the layers will disappear from view on the canvas until you move them to where they can overlap.

![An animation demonstrating the intersect boolean operation. ](https://help.figma.com/hc/article_attachments/31405046970775)

### Exclude

The opposite of intersect is **Exclude**, which removes the overlapping area, keeping just the non-overlapping parts. Similar to subtract, any strokes or effects you add will appear on the inner and outer edges of the new object.

![An animation demonstrating the exclude boolean operation. ](https://help.figma.com/hc/article_attachments/31405046971927)

### Applying boolean operations

You can apply boolean operations to shape layers, vector paths, and text layers. You can’t apply boolean operations to container elements like sections or frames.

To apply a boolean operation, select at least two supported layer types, then choose an operation from the **Boolean operations** menu.

Boolean operations are non-destructive actions, which means you can still select, move, and resize the original layers. This flexibility allows you to keep iterating on designs without having to ungroup the layers or start over from scratch. Because layers in a boolean group share a single set of properties, changes made to the properties of an individual layer will have no effect until it is removed from the group. To break up a boolean group and revert the layers back into individual objects, right-click on the group and select **Ungroup**.

## Create the diamond shape

![](https://help.figma.com/hc/article_attachments/31703975540503)

Now that we know more about boolean operations, let's use them to build the second and third shapes.

To build the diamond shape:

1. Inside the **Shape 2** frame, create a `38` X `38` rectangle.
2. Place a `16` X `16` ellipse on top of it.
3. Align the centers of both shapes.
4. Select both shapes, then select the  **Subtract selection** boolean operation.
5. Select the **Subtract** layer and rotate it `45` degrees using the handle on the canvas or the **Rotation** field in the right sidebar. If you’re using the handle, you can hold `Shift` to rotate the layer in 15 degree intervals.
6. Change the **Corner radius** to `13` to round the corners.
7. Rename the frame to `Diamond`.

![](https://help.figma.com/hc/article_attachments/31703975541015)

The **Subtract** boolean operation cut the area of the ellipse out of the rectangle, meaning that any layers placed behind the rectangle will show through the hole that was created. Because boolean operations are non-destructive, you can still select and modify the ellipse layer to adjust the size and placement of the cutout.

## Create the flower shape

![](https://help.figma.com/hc/article_attachments/31703975542551)

For this next shape, we’re going to kick it up a notch by combining duplicated layers using the **Union** operation, and removing the center area with the **Subtract** operation.

1. Inside the **Shape 3** frame, add a `12` X `46` rectangle to the center of the frame and set its **Corner radius** to `13`.
2. Duplicate the rectangle and rotate the new layer `45` degrees. Remember how we learned that duplicating layers can be used to create rotating patterns? Let’s do that here!
3. With the duplicated layer still selected, duplicate it twice more using the shortcut. Notice how Figma applies the same rotation automatically?
4. Select all four layers and use the **Union** boolean operation to merge them into a flower shape.
5. Add a `12` X `12` ellipse to the center of the flower.
6. Select it and the  **Union** boolean group.
7. Just like we did with the `Diamond` shape, we’ll use the  **Subtract**boolean operation to punch a hole through the center of the flower.
8. Rename the frame to `Flower`.

![](https://help.figma.com/hc/article_attachments/31703969046167)

## Opportunities for more boolean operation exploration

In the next chapters, we’re going to set boolean operations aside and check out some other tools you can use to create custom shapes. We’ve only just scratched the surface, but hopefully you’re starting to see just how flexible and powerful boolean operations can be in your design workflow. If you’re looking for more practice, we’ve included some additional shapes and icons in the [Figma Design for beginners Community file](https://www.figma.com/community/file/1499455316701927850/figma-design-for-beginners-2025-course-assets). Try recreating them using what you’ve just learned. The more you experiment, the more intuitive boolean operations will become.
