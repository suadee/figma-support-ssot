---
기술지원명: FD4B: Create the image and the hero
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Create the image and the hero
출처링크: https://help.figma.com/hc/en-us/articles/30979234412567-FD4B-Create-the-image-and-the-hero
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Next, we'll create the remaining elements for our case study page: the image and hero.

![](https://help.figma.com/hc/article_attachments/31350256501143)

## Create the image

We'll create an image block that we can use to visually showcase our work throughout the case study.

![](https://help.figma.com/hc/article_attachments/31350268097687)

1. Select the **Rectangle** tool or press `R`, and draw a rectangle inside the **Case study explorations** frame.
2. Set the layer's width to `1000`. This will match the width of our text layers, so they'll stay consistent with each other.
3. Set the height to `562`.
4. Open the color picker in the **Fill** section of the right sidebar
5. Select **Image** at the top. Figma will change the fill to a grey and white checkerboard pattern to indicate an image placeholder. We'll update these placeholders in a later lesson.
6. Rename the layer to `Image`.

![](https://help.figma.com/hc/article_attachments/31350268100119)

## Create the hero

![](https://help.figma.com/hc/article_attachments/31350256502935)

Before creating the hero, select all of the elements in the **Case study explorations** frame and move them down at least 400 pixels inside the frame.

**Tip:** You can check how far from the edge the selected layers are by pressing the keyboard shortcut for measuring distances and hovering your mouse over the space between the layer and the edge:

- Mac: `Option`
- Windows: `Alt`

### Add a text layer

Now that we have room to work, we'll create the hero element.

1. Use the **Text** tool to create a text layer at the top of the **Case study explorations** frame.
2. To help this element stand out, increase the font size to `76`, the font weight to `Bold`, and the line height to **Auto**. When you set line height to auto, Figma will use the default line height set by the font. This means line height will vary depending on the font you're using.
3. Set the text alignment to **Align center**.
4. In the **Alignment** section, click **Align horizontal centers** to center the layer inside the frame.

![](https://help.figma.com/hc/article_attachments/31772403827351)

### Add the text layer to a frame

It would be great to add a background to this hero, to help it stand out more. To achieve this, we'll add the text layer to a frame with an image fill.

In a previous lesson, we learned how to draw a frame around existing layers. This time, we'll use another method to add a new frame.

1. Select the text layer.
2. Right-click on the selection and choose **Frame selection** or use the keyboard shortcut:
   - Mac: `⌘ Command` `⌥ Option` `G`

     Windows: `Control` `Alt` `G`
3. Use the **Fill** section to change the fill to a placeholder image.
4. Then, make the frame bigger by clicking and dragging the left and right sides of the new frame’s bounding box. You can hold the modifier key to resize opposite sides in one go.

   - Mac: `Option`
   - Windows: `Alt`
5. Resize until the side snaps to the sides of the parent frame—indicated by the red X. To do this, you’ll need to have **Snap to objects** toggled on in your file preferences.
6. Then, set the height of the frame to `440`.
7. Rename the frame to `Impactful text`.

![](https://help.figma.com/hc/article_attachments/31350268104727)

### Set the text layer's constraints

When you resize this frame, the title text stays anchored to the top, but we want it to anchor to the center. We'll use [constraints](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize) to change this behavior

1. Select the text layer inside the **Impactful text** frame.
2. Change the layers constraints to **Center** and **Center**.
3. Click **Align horizontal center** and **Align vertical center** to center the text inside the frame.

Now when we resize the frame, the text layer stays centered.

![](https://help.figma.com/hc/article_attachments/31350268106647)
