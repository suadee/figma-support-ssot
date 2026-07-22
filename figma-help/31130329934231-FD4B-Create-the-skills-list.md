---
기술지원명: FD4B: Create the skills list
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Create the skills list
출처링크: https://help.figma.com/hc/en-us/articles/31130329934231-FD4B-Create-the-skills-list
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Great work! Now we’re ready to combine our custom shapes with some text layers to build the skills list.

![And example of the skills list with custom icons and bold text arranged in an auto layout frame.](https://help.figma.com/hc/article_attachments/31405179401623)

## Build the skills list

1. Add a new text layer to the canvas and enter a short bit of placeholder text, something like `Skill name` is fine for now.
2. We’re sticking with the `Inter` font but feel free to choose something else.
3. Change the font's properties:
   - Set the **Font weight** to something heavier like `Bold` or `Black`.
   - Set the **Font size** to `48`.
   - Se the **Line height** to **Auto.**
4. From the **Assets** tab in the left sidebar and find the `Inchworm` component, and add an instance of it to the frame and align its vertical center with the text layer.
5. Select and duplicate both layers. Then, move the new layers to the right of the original.

![](https://help.figma.com/hc/article_attachments/31405150379543)

## Swap instances

We need to replace the `Inchworm` shape with an instance of the **Diamond** shape. Instead of locating and adding instances from the **Assets** tab, we can simply [swap in a new instance](https://help.figma.com/hc/en-us/articles/360039150413-Swap-components-and-instances).

![](https://help.figma.com/hc/article_attachments/31405150382359)

To swap instances:

1. Select the duplicated shape layer.
2. Open the **Swap instance** menu in the right sidebar. From here, you can access our other shape components and insert instances of them directly into our design, in place of the selected instance.
3. Select the **Diamond** component from the instance swap menu.
4. Figma will automatically replace the shape layer on the canvas with a new instance.
5. Duplicate the text and shape layer again and repeat the process with the next shape.
6. Once the row includes three sets of text and shapes, start a second row below the first until you’ve used all five shapes.

![](https://help.figma.com/hc/article_attachments/31405179412887)

## Apply auto layout to the skill list

Now it’s time to revisit our old friend auto layout!

1. Click and drag your cursor to select all of the text and shape layers.
2. Press `Shift` `A` to add them to an auto layout frame.
3. Rename this frame to `Content`.
4. Give it a **Max width** of `1000`.
5. Since our layers were already arranged into multiple rows, Figma automatically set the **Direction** to **Wrap**.
6. Update your placeholder text with skills that highlight our strengths, and see how auto layout responds.
7. Now that the direction is set to **Wrap**, the frame has both a **Horizontal** and **Vertical gap** property. Set both gaps to `8`.
8. Set the **Padding**  `0` (zero).
9. Set the **Alignment** to **Align left**.

![](https://help.figma.com/hc/article_attachments/33994848751127)

### Use selection colors to change fills

We want our shapes to be the same color as the text. Instead of changing each shape’s fill individually, we can use the **Selection colors** section in the right sidebar to change them all at once. Like the name implies, [Selection colors](https://help.figma.com/hc/en-us/articles/360042553434-View-and-adjust-colors-in-a-mixed-selection) displays all of the solid color or gradient fills used in your current selection.

1. Select the auto layout frame with all of the text and shape layers
2. Use the field next to the gray color swatch in the **Selection colors** to change the fill to `#000000`.

## Add the container frame and create a component

Awesome! Now we just need to add this element to a container frame like we did for all of our other components earlier.

1. Draw a new frame around the **Content** frame.
2. Add auto layout to it with `Shift` `A.`
3. Rename the frame to `Skills list`.
4. Remove the frame’s fill.
5. Update the following auto layout properties:  
   - Set the **Height resizing** to **Hug contents**
   - Set the **Alignment** to **Center**
   - Set the **Horizontal padding** to `24`
   - Set the **Vertical padding** to `80`
6. Turn the **Skills list** frame into a main component.
7. Move the new component to the **Components** page.

![](https://help.figma.com/hc/article_attachments/33994848752919)

## Lesson wrap up

Awesome work! We just created five custom shapes by merging basic shapes using boolean operations, editing the vector path of a rectangle, and changing the arc properties of an ellipse. We then combined our shapes with text layers and auto layout to build a responsive skills list element. We finished the lesson by turning the element into a main component and moving it to the Components page.

Our individual portfolio elements are now complete! In the next lesson, our hard work will pay off as we put all of the elements together to build our portfolio design.
