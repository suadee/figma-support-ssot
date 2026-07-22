---
기술지원명: FD4B: Build your bio using text layers
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Build your bio using text layers
출처링크: https://help.figma.com/hc/en-us/articles/30938465113751-FD4B-Build-your-bio-using-text-layers
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Write your bio

Now that our avatar is complete, we'll use text layers to build our greeting and bio.

Text is a crucial component in design, and can be used to communicate information or encourage action. The way we style text within our designs can also help support visual hierarchy, convey the appropriate tone, and even make or break the accessibility of a design.

We'll use the **Text** tool to add text layers to the canvas.

### Add text layers

1. Select the  **Text**tool in the toolbar or press `T`.
2. Click on the canvas below the avatar and type your name. If you take a look at the left sidebar, you'll notice that the layer name reflects the string of text on the canvas. It will continue to do this until we rename the layer.
3. With the  **Text** tool still selected, click and drag your cursor to create a text box below the other layers. Make sure the text box is large enough to fit your content. Don't worry about its exact size; we'll refine that in a future lesson.

![](https://help.figma.com/hc/article_attachments/31326463558167)

As you type, you'll see that the text content stays contained within the text box, automatically wrapping to the next line instead of flowing off to the side. Why is this different from the other text layer?

**Text resizing**

Text layers have a resizing property that determines how the layer’s dimensions, indicated by the bounding box, will respond when its contents change. There are three text resizing options:

- **Auto width:** The text layer's width will grow and shrink as its contents change
- **Auto height**: The text layer's height will grow and shrink as its contents change
- **Fixed size**: The text layer's width and heigh will stay the same, regardless of its contents. Figma will wrap any additional text to prevent it form extending beyond the layer's horizontal bounds.

The text resizing property is automatically set based on how the text layer was created but you can update the setting in the **Layout** section of the right sidebar at any time. Learn more about [text resizing](https://help.figma.com/hc/en-us/articles/27378154668951-Adjust-text-dimensions-and-resizing#h_01JB9SGE9C9982902T505EK7ZQ).

### Align your layers

If your layers are looking a little wonky, you can align them using **Alignment**section in the right sidebar.

1. Click on a blank area of the canvas to deselect all layers.
2. Click and drag your cursor to select your avatar and the two text layers.
3. Click **Align left** to align the layer's left-most edge.

![](https://help.figma.com/hc/article_attachments/31326463559191)

### Style the text layers

The default text styling is a bit small, and hard to read. We can use the [text properties](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties) to create some visual hierarchy and help draw attention to a few key areas.

**Note:** We'll be sticking with Figma's default font family, **Inter**, throughout this course. Feel free to browse through the available fonts and choose something else but keep in mind, the font family you choose may not offer the same weight options we'll be using.

1. Select the text layer with your name, and take a look at the **Typography** section in the right sidebar.
2. To add more weight to this text layer, change the font weight to a bolder choice, like `Black`.
3. Change the font size to to `40`.

**Tip:** If your layers start to overlap, you can use your nudge options to quickly reposition them.

There are two nudge types in Figma:

- **Small nudge** uses arrow keys to reposition layers and moves layers in increments of **1** by default.
- **Big nudge** uses `Shift` with arrow keys, and moves layers in increments of **10** by default.

You can change your nudge values from the **Preferences** menu. Learn more about the [nudge settings](https://help.figma.com/hc/en-us/articles/4404575206295-Set-small-and-big-nudge-values).

We'll update the bio text layer next:

1. Select the text layer that contains your bio.
2. Update the font weight to `Medium` and the size to `28`.
3. Change the text resizing to **Auto height** to prevent content from bleeding over the bottom edge of the bounding box.
4. To give the content some room to breath, set the line height to `38` and the paragraph spacing to `16`.
5. You can also use text formatting like bold or italics to draw attention to your career highlights or other achievements.

![](https://help.figma.com/hc/article_attachments/31326463562135)

## Check your knowledge
