---
기술지원명: FD4B: Auto layout fundamentals
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Auto layout fundamentals
출처링크: https://help.figma.com/hc/en-us/articles/31351261703063-FD4B-Auto-layout-fundamentals
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Lesson overview

With the introduction of grid in May 2025, the auto layout section differs from what's shown in this video. We've also updated the terminology from "auto layout direction" to "auto layout flow". Learn more about the [updated auto layout settings](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout).

In this chapter, we’ll use auto layout to build a responsive button element that automatically grows and shrinks as its label changes. We’ll then turn the button into a main component so we can reuse it in other designs.

![Responsive button design with text label, demonstrating auto layout for dynamic resizing.](https://help.figma.com/hc/article_attachments/31718188686743)

Here’s the button we’re going to build. To recreate this design, it seems like we could use a rectangle for the background, a text layer for the label, and a frame to keep it all together. The outcome might look ok, but it won’t really work if we need to change the button label in the future.

Instead, we’ll use auto layout to create a frame around our text layer and give it a fill to act as the surface of the button.

## Auto layout fundamentals

[Auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties) helps you organize, arrange, and space out design elements so that they adjust automatically as you make changes, saving you time and making your designs responsive and adaptable.

You can apply auto layout to a frame or a selection of layers using the keyboard shortcut `Shift` `A`. This adds the selected layers to a parent frame with auto layout applied. We can then use auto layout to determine how the parent frame interacts with its child layers.

We can set the **Direction** of the frame’s child layers to flow vertically, horizontally, or allow layers to wrap to a new line.

![three sets of designs, all with the same elements: three circles, one pink, one yellow, one green. The first set of circles are placed in a vertical direction. The second set of circles are placed in a horizontal direction. The third set of circles are wrapped, with the pink and yellow circles in the first row, and the green circle in the second row.](https://help.figma.com/hc/article_attachments/31718188690583)

We can adjust the left, top, right, and bottom **Padding** of our design to create visual spacing between the child layer and their parent frame.

![A light-green blog card asset containing a title, description, and a read more button. Auto layout is applied to this asset. The keyboard shortcut for changing padding on all sides displays below it. A cursor uses that keyboard shortcut while clicking and dragging the top pink handle of the auto layout frame.](https://help.figma.com/hc/article_attachments/31718188696087)

We can also adjust the spacing, or **Gap**, between child layers and choose how those layers are **Aligned** within the parent frame. And, we can control how an object’s **height** and **width** **resizes** when changes occur.

![In a Figma Design file, a frame contains a blog post card. Within it is a pink rectangle, title text, description text, and three topic tags. The topic tags are in their own auto layout frame, set to wrap. A cursor clicks into the horizontal gap between field in the right panel and changes it to Auto. The topic tags spread out horizontally to fill its parent container.](https://help.figma.com/hc/article_attachments/31718176386711)

A parent frame can have a **Fixed** height or width, or it can be set to **Hug** its child layers so that it grows or shrinks as those layers change. A child layer’s height and width can be **Fixed**, set to **Fill** its parent frame or, if it contains its own child layers, set to **Hug** those layers instead.

![a layer inside a mobile frame is selected. A box highlights the resizing section of the right panel.](https://help.figma.com/hc/article_attachments/31718188699031)

You can combine different resizing options to customize how a layer behaves. For example, imagine an app notification. To make sure the notification frame stays a consistent width while accommodating a longer message, you can set its width to **Fixed** and its height to **Hug contents**.

Together, these auto layout properties help your designs be more flexible as changes happen throughout the design process and beyond. Learn more about [auto layout properties](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties).

### Try it out!

Try getting hands on and use the interactive sandbox below to learn how auto layout works. Keep in mind this doesn’t fully replicate how auto layout works in Figma Design and is meant for learning purposes only.

## Check your knowledge
