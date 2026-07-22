---
기술지원명: FD4B: Create the button
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Create the button
출처링크: https://help.figma.com/hc/en-us/articles/30981948843927-FD4B-Create-the-button
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Now that we know more about auto layout, let's use it to create a button.

![Responsive button design with text label, demonstrating auto layout for dynamic resizing.](https://help.figma.com/hc/article_attachments/31358283683479)

## Create a text layer

We’ll start by adding a new text layer that will serve as our button’s label.

1. Enable the  **Text** tool.
2. Click on the canvas and type `Button`.
3. Leave the font family set to **Inter** or choose another font you like.
4. Use the **Typography** section to change the following:
   - Set the **Font weight** to `Semi Bold`
   - Set the **Font size** to `18`
   - Set the **Line height** to **Auto**
   - Set the **Alignment** set to **Center**

![](https://help.figma.com/hc/article_attachments/31353677639063)

## Add auto layout

Now we're ready to apply auto layout.

1. Select the text layer.
2. Press `Shift` `A`. Figma will automatically create a new frame around the text layer with auto layout applied.
3. Double-click on the frame name and rename it to **Button**.

![](https://help.figma.com/hc/article_attachments/33971554939031)

## Style the button

We’ll adjust the auto layout properties shortly, but first let’s style our button:

1. Select the text layer inside the **Button** frame.
2. Type `F` in the field next to the color swatch in the **Fill** section, and press `Enter`. Figma will take the single `F` we entered, and assume we want to set the hex code to `#FFFFFF`, which sets the fill to pure white.
3. Select the **Button** frame.
4. Click the **plus**  in the **Fill** section to add a fill.
5. Type `0` (zero) in the field and press `Enter`. Just like before, Figma takes the zero we entered and fills out the rest of the field with zeroes, which changes the fill to black.
6. Change the **Corner radius** to `8` in the **Appearance** section of the right sidebar.

![](https://help.figma.com/hc/article_attachments/31353677653271)

**Tip:** Interested in learning more about button design best practices? Check out our [Design your first button](https://help.figma.com/hc/en-us/articles/14078912322199-Design-your-first-button) project.

## Adjust the auto layout properties

When you select the **Button** frame, you may notice that the section in the right sidebar changed to **Auto layout** and includes some additional properties. The **Dimensions** fields also changed and are now **Resizing** fields.

In addition to being able to set a fixed width and height for the frame, we now have the option to set the parent frame to **Hug contents**, which means that it will automatically resize as the button label grows or shrinks. Because we’ll use this button element again in different contexts, we’ll leave the resizing properties set to **Hug contents** for maximum flexibility. That way, if we need to change the button’s label, or translate it into a different language, we wont have to worry about manually resizing it.

**Test it!** See what happens when you change the button label to “Continue” or “Next”.

![An animation demonstrating how the button resizes as its label changes. ](https://help.figma.com/hc/article_attachments/31353677654039)

We'll adjust some of the other auto layout properties to customize how our button looks:

1. Set the **Horizontal gap between objects** to `10`.
2. Set the **Horizontal padding** to `16` and the **Vertical padding** to `10`.

![](https://help.figma.com/hc/article_attachments/33971584349847)

You may be wondering why Figma set the padding to `10` when we added auto layout. Figma automatically used our **Big nudge** preference, which is set to `10`. If we had an existing frame around the text layer before applying auto layout, Figma would maintain the distance we had between the text layer and frame instead. Learn more about [nudge settings](https://help.figma.com/hc/en-us/articles/4404575206295-Set-small-and-big-nudge-values).

## Turn the button into a main component

Since our final design will include several buttons, we'll turn this button into a main component.

1. Select the **Button** frame.
2. Click  **Create component** in the right sidebar.

![](https://help.figma.com/hc/article_attachments/33971554940567)

You’ll notice the button is now inside a purple bounding box and the icon in the Layers section has also changed to a four diamonds icon. This indicates the layer is a main component. In the next chapter, we'll learn more about components and how we can use them to speed up our design workflows.

## Check your knowledge
