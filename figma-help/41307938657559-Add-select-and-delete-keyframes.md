---
기술지원명: Add, select, and delete keyframes
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Add, select, and delete keyframes
출처링크: https://help.figma.com/hc/en-us/articles/41307938657559-Add-select-and-delete-keyframes
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Figma Motion is currently in open beta.** Features may change and you may experience performance issues as we continue to improve Figma Motion. Learn more about [what's included in the beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

Before you Start

Who can use this feature

Available on [any plan](https://figma.zendesk.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can add preset animations

Keyframes are the building blocks of motion design. A keyframe marks a point in time where you set a specific value for a layer property, such as opacity, position, or rotation.

To create motion, you need at least two keyframes: one for the initial state and one for the end state. Figma Motion will fill in the gaps between keyframes to create a smooth animation.

For example, to animate a square rotating `180` degrees over `500` milliseconds, you would add one rotation keyframe with a value of `0` at the `0` millisecond mark and a second rotation keyframe with a value of `180` at the `500` millisecond mark.

![keyframes demo.gif](https://help.figma.com/hc/article_attachments/41355675219735)

## Add keyframes

You can only add keyframes while in Figma Motion. Any property that supports keyframing shows a diamond icon next to its field in the right sidebar.

![imageTemplate (12).png](https://help.figma.com/hc/article_attachments/41355675220375)

### Add keyframes manually

1. Move the playhead to where you want your animation to begin.
2. Click  **Add keyframe** next to the property you want to animate. A corresponding keyframe will be added to the timeline.
3. Enter a value in the property field to set the starting state.
4. Move the playhead to where you want the animation to end.
5. Enter a new value in the property field to create a second keyframe. The two keyframes will be connected by a line on the timeline that you can click to change the animation’s easing curve. Learn more about easing curves.
6. Continue to move the playhead and add keyframes to build your animation.
7. Click  **Play** or press `Spacebar` to preview your animation.

### Use auto-keyframe

For quicker motion creation, you can enable auto-keyframe from the timeline controls. When active, keyframes are automatically added to the timeline as you make changes to your design.

Just be mindful that every change you make while auto-keyframe is active gets recorded, so an accidental value change in the wrong place will create an unintended keyframe.

To use auto-keyframe:

1. Select  **Toggle auto-keyframe** from the timeline controls. A red bar appears across the top of the timeline and on the playhead, and the auto-keyframe handle appears when you select an object.
2. Move the playhead to where you want your animation to begin.
3. Update a property value using the fields in the right sidebar or using the auto-keyframe handle directly on the canvas. Corresponding keyframes are added to the timeline automatically.
4. Continue to move the playhead and update property values to build your animation.
5. Click  **Play** or press **Spacebar** to preview your animation.
6. Click  **Toggle auto-keyframe** again to disable it.

![auto key 2.gif](https://help.figma.com/hc/article_attachments/41404781022999)

## Select keyframes

Unselected keyframes appear as a blue outline diamond. Selected keyframes appear as a blue filled diamond.

- To select an individual keyframe, click it on the timeline
- To move the playhead to a specific keyframe, double-click on it
- To select multiple keyframes, either hold `Shift` and click each one, or click and drag your cursor around the keyframes you want to select
- To select all keyframes for a specific layer, select it in the timeline layers

![](https://help.figma.com/hc/article_attachments/41404765733271)

## Move keyframes in time

An animation’s speed is determined by the distance between keyframes. The further apart they are, the slower the motion will be. You can select and move keyframes directly on the timeline.

To move keyframes:

1. Select one or more keyframes
2. Drag the selected keyframes to the desired time.

![move keyframe.gif](https://help.figma.com/hc/article_attachments/41405004146071)

### Move keyframes to a specific time

1. Move the playhead to the desired time.
2. Select one or more keyframes and hold `Shift` as you drag the keyframes to the playhead. As you drag over the playhead, the selected keyframes will snap to it. You can also use this method to align keyframes with other keyframes.

## Update a keyframe’s value

You can alter your motion by updating a keyframe’s associated property value.

1. Double-click on a keyframe to jump to it on the timeline.
2. Update the keyframe’s property value in the right sidebar.

![](https://help.figma.com/hc/article_attachments/41405141165335)

## Delete keyframes

To delete a single keyframe:

1. Select the keyframe on the timeline.
2. Press `Delete`.

To delete all keyframes for a specific property:

1. Select the property in the layer’s section of the timeline.
2. Press `Delete`.

**Getting started with animation?** Check out the [Motion design fundamentals collection](https://help.figma.com/hc/en-us/sections/41236726027287-Motion-design-fundamentals-collection) to learn the principles behind effective motion design and get hands-on practice creating animations in Figma Motion.
