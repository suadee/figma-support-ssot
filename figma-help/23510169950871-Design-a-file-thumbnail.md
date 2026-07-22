---
기술지원명: Design a file thumbnail
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Design a file thumbnail
출처링크: https://help.figma.com/hc/en-us/articles/23510169950871-Design-a-file-thumbnail
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma) , [Community files](https://help.figma.com/hc/en-us/articles/360038510873-Duplicate-Community-files), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [text](https://help.figma.com/hc/en-us/articles/360039956434-Guide-to-text)
- **Difficulty:** Intermediate
- **Length**: 25 minutes

In this project, we’re going to create a file thumbnail. Every design file has a thumbnail that shows a preview of the file’s contents. By default, Figma will use the contents of the first page of the file for the thumbnail. However, you can specify a frame to be used as the thumbnail instead. This gives you more control over what people will see when they view the file in the file browser. If you’re publishing files to the [Figma Community,](https://help.figma.com/hc/en-us/articles/360038510693-Guide-to-the-Figma-Community) a well-designed file thumbnail can also be a great way to help your work stand out and attract more users.

When designing a file thumbnail, you want the contents of the thumbnail to reflect the contents of the file. For this project, we’re going to create a thumbnail for a tooltip component set. We’ll be using the tooltip component for part of the thumbnail design. If you’d like to learn how to create this component set for yourself, check out [this hands-on project](https://help.figma.com/hc/en-us/articles/22690735962263-Create-a-tooltip-component-set). If you’re short on time, you can grab a copy of the finished component set from the [Figma Community](https://www.figma.com/community/file/1372670137883100002) instead.

This project will cover using components, modifying text, and creating basic patterns. After you complete this project, your final thumbnail will look similar to the following:

![An image showing the final thumbnail design.](https://help.figma.com/hc/article_attachments/23510215253527)

## Create the thumbnail frame

The first thing we need to do is create the frame we’ll use for our thumbnail. 1920x1080 pixels is the recommended size for file thumbnails. Instead of manually resizing a frame, we can use the frame preset to automatically add a frame of the correct size.

1. Select the  **Frame** tool in the toolbar or press `F`.
2. In the right sidebar, select **Plugin / file cover** under Figma Community. A new frame is automatically added to the canvas.

![](https://help.figma.com/hc/article_attachments/23510479340823)

3. Select the frame you just added.
4. In the Fill section of the right sidebar, change the frame’s fill to `#FFB801`.
5. Double-click on the frame’s name and rename it to `Thumbnail`.
6. Right-click on the frame and select **Set as thumbnail**.

## Create the background pattern

Now that we have the foundation of our thumbnail, it’s time to add the visual elements. We’ll start by creating a basic pattern for our background. To create the pattern, we first need to make a simplified tooltip icon.

1. Select the **Rectangle** tool from the **Shape tools** dropdown menu.
2. Click to add a rectangle to the canvas.
3. Change the rectangle’s width to `30` and height to `20` using the settings in the right sidebar.
4. Select the **Polygon** tool from the **Shape tools** dropdown menu.
5. Click to add a triangle to the canvas.
6. Change the triangle’s width and height to `10` using the settings in the right sidebar.
7. Select the triangle and hold `Shift` while rotating it until it is pointing down.
8. Center the triangle on the bottom of the rectangle.

![An animation demonstrating how to create the tooltip shape. ](https://help.figma.com/hc/article_attachments/23511011198615)

The icon is starting to come together. Now we need to combine both shapes.

1. Click and drag your cursor over the triangle and rectangle to select both layers.
2. Click  **Union selection** in the toolbar to combine the shapes.
3. Click the  plus in the **Stroke** section to add a stroke.
4. Select **Outside** from the dropdown menu and change the stroke’s width to `3`.
5. Click the  minus in the **Fill** section to remove the fill.
6. Change the  corner radius to `1`.

Before moving on, check to make sure your icon looks similar to the following:

![](https://help.figma.com/hc/article_attachments/23511301518359)

Looking good! Now we can build our pattern.

1. Select the icon and duplicate it using the following shortcut:
   - **Mac:** `⌘ Command` `D`
   - **Windows:** `Control` `D`
2. Drag the duplicated icon to the right of the original icon. Don’t worry about spacing for now. We’ll fix that in a bit.
3. Duplicate the new icon using the same keyboard shortcut. You’ll notice that Figma follows a consistent spacing pattern each time you duplicate the layer.
4. Keep using the duplicate shortcut until you have a row of 20 icons.
5. Click and drag your cursor to select all of the icons.
6. Change the  **Horizontal spacing** to 100.
7. With the icons still selected, use the keyboard shortcut to group them:
   - **Mac:** `⌘ Command` `G`
   - **Windows:** `Control` `G`

![](https://help.figma.com/hc/article_attachments/23511427550743)

We’re going to use a similar process to build the pattern out vertically:

1. Select the group and duplicate it using the same keyboard shortcut.
2. Select the new group and drag it below the original group. Again, don’t worry about the spacing for now.
3. Continue duplicating the group until you have 15 rows.
4. Click and drag your cursor to select all of the groups.
5. Change the  **Vertical spacing** to 100.
6. With all of the rows selected, group them using the keyboard shortcut:
   - **Mac:** `⌘ Command` `G`
   - **Windows:** `Control` `G`
7. Select the group and rename the layer to `Background pattern`.

Our pattern is looking great. We just need to apply a few final styling touches before we can call it good.

1. Select the **Background pattern** layer.
2. In the **Stroke** section, change the stroke transparency to `20%`.
3. With the group still selected, change the **Rotation** to `-30%` using the setting in the right sidebar.
4. Drag the pattern into your thumbnail frame. Check the right sidebar to make sure it’s nested under the Thumbnail frame.
5. Click  **Lock** to lock the layer.

Before moving on, check to make sure your Thumbnail frame looks similar to the following:

![](https://help.figma.com/hc/article_attachments/23511687868951)

## Add the text

Our thumbnail is really starting to come together. Now, let’s add the text elements. This is where we’ll start using the tooltip component set so if you haven’t created one yet, go ahead and grab a copy of the [Community playground file](https://www.figma.com/community/file/1372670137883100002).

First, we need to add a copy of the tooltip component set to our file.

1. In the playground file, select the tooltip component set.
2. Copy it using the keyboard shortcut:
   1. Mac: `⌘ Command` `C`
   2. Windows: `Control` `C`
3. Navigate back to the file where your in-progress thumbnail is located and paste the component set using the keyboard shortcut:
   1. Mac: `⌘ Command` `V`
   2. Windows: `Control` `V`

Now we’ll be able to access the component in our working file.

We’ll use an instance of the tooltip component for our main heading.

1. In the **Assets** panel in the left sidebar, locate the tooltip component under **Created in this file**.
2. Click and drag the component onto the canvas to create an instance.
3. In the right sidebar, change the arrowDirection property value to bottom using the dropdown menu.
4. Double-click on the tooltip’s text and enter `Web Tooltips`.
5. Select the text and change it to bold.

It looks good but it’s far too small to use in our thumbnail. Luckily, we can scale up the size.

1. Select the tooltip again and press `K` to open the **Scale** tool.
2. Change the  **Scale** to `9`.
3. Double-click on the tooltip layer name and change it to Title.
4. Add the Title layer to the left side of the Thumbnail frame and lock it.

![](https://help.figma.com/hc/article_attachments/23512204414103)

Now let’s add the subheading.

1. Select the **Text** tool in the toolbar or press `T`.
2. Type out `Easy, Customizable, Scalable`, pressing `Enter` after each comma to add a line break. We’re using the default Inter font for this project but feel free to choose something else.
3. In the **Text** section of the right sidebar, change the font size to `104` and make sure the text is bold.
4. Double-click on the layer name and change it to `Subheading`.
5. Click and drag the Subheading layer up into the Thumbnail frame below the Title layer and lock it.

Before moving on, make sure your thumbnail looks similar to the following:

![](https://help.figma.com/hc/article_attachments/23512666788503)

## Add the preview elements

Our thumbnail is almost done. But the right side of the frame is looking a little bare. We’ll use the tooltip component set again to add some visual interest and give people a preview of what the tooltips could be used for.

1. From the **Assets** panel in the left sidebar, add another instance of the tooltip component to the canvas.
2. We want to add some personality to the thumbnail. Here’s where you can get creative. Duplicate the instance a few times. Play around with the layout and use the variant properties in the right sidebar to change the direction of the arrows. Double-click on the text layer in each tooltip and change it to something different. Ours will be a mix of common tooltip copy with a few fun ones thrown in. Don’t worry too much about spacing but try to keep things relatively consistent.

![](https://help.figma.com/hc/article_attachments/23512666807959)

3. When you’re happy with your layout, select all of the tooltips and group them using the same keyboard shortcut we learned earlier.
4. Select the tooltip again and press `K` to open the scale tool.
5. Change the  **Scale** to `9`.
6. Change the **Rotation** to `20%`.
7. Drag the group to the right side of the Thumbnail frame. Feel free to play around with the positioning until you’re happy with how it looks.
8. Double-click on the group name and rename it to `Tooltip preview`.
9. Click  **Lock** to lock the layer.

Your final thumbnail should look similar to the following:

![](https://help.figma.com/hc/article_attachments/23512787491223)

## What’s next?

Congratulations! We hope you can apply what you learned in this project to your own file thumbnails. Remember that thumbnails are endlessly customizable. Have fun with the design process and don’t be afraid to try out something new. If you design something you're extra proud of, we'd love to see it! Mention us on X (formerly Twitter) @Figma or publish it to the Figma Community.
