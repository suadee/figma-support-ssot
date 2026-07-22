---
기술지원명: Create a responsive card with auto layout and constraints
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a responsive card with auto layout and constraints
출처링크: https://help.figma.com/hc/en-us/articles/18894664907287-Create-a-responsive-card-with-auto-layout-and-constraints
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [auto layout](https://help.figma.com/hc/en-us/articles/5731482952599-Using-auto-layout), [constraints](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [shape tools](https://help.figma.com/hc/en-us/articles/360040450133-Basic-shape-tools-in-Figma-design), [frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma)
- **Difficulty**: Intermediate
- **Length**: 20 minutes

In this project, we’ll be creating a responsive card design for a podcast app. If you follow along step-by-step, your final prototype will look like this:

![An image showing the final card design. ](https://help.figma.com/hc/article_attachments/24632682490775)

To create this design, we’ll do the following:

1. [Create a play button](#h_01HENN6GVJ3ER1S73HSWF76V5F)
2. [Create the album art](#h_01HENNWWPMJQ8WWK7JN6K2DFFA)
3. [Create two text layers for metadata](#h_01HENPJCJH7J8PVAX0AY8VXM8M)
4. [Add auto layout to album art and metadata](#h_01HENQ67XD7DKDXEENCW6V4WAS)
5. [Apply minimum and maximum dimensions](#h_01HENQ9WNXY5GY70XQWJB12SKQ)
6. [Turn the card design into a component](#h_01HENQJP7YV675Q81W92C9FS6F)

Before you begin, have an image ready on your computer as we’re going to use an image as our album art.

## Create a play button

Let’s start by creating the play button’s background first:

1. Create a 40 W x 40 H frame.
2. Change the fill to `132745`.
3. Change the  corner radius to `100`.
4. Rename it to “play-button”.
5. Click the  **plus** sign in the **Effects** section to add a drop shadow to the frame.
6. Click  **Effect settings** to open the **Drop shadow** panel.
7. Change the Y position to `0`, the Blur to `12`, and the opacity to `16%`.

![](https://help.figma.com/hc/article_attachments/24632833622807)

Next, let’s add a play icon to the play-button frame.

1. From the **Shape tools** in the toolbar, select **Polygon**.
2. Click and drag inside the play-button frame to create a 16 W x 16 H triangle.
3. Hover over the object’s corner until the  **rotate** icon appears.
4. Hold `Shift` and rotate the triangle 90 degree clockwise.
5. Change the fill to `FFFFFF`.
6. Align it to the center of the play-button frame.

You’ll notice a space between the triangle shape and the bounding box. This allows the bounding box to remain a consistent shape or size, and is a helpful tool to achieve an optical alignment.

![](https://help.figma.com/hc/article_attachments/24632890332055)

To test this theory, let’s do a quick experiment:

1. Duplicate the play-button frame.
2. Select the triangle.
3. Right-click and select **Flatten**.
4. Align the triangle with the  **Align horizontal centers** settings from the right sidebar.

Now, compare the two buttons. What do you notice? Even though the flatten triangle is technically centered, it doesn’t look centered due to the uneven distribution of the triangle’s area.

![](https://help.figma.com/hc/article_attachments/24632833635607)

We can turn our play button into a component so it can be reused in multiple designs.

1. Select the play-button frame.
2. Click  **Create component** from the toolbar bar.

## Create the album art frame

1. Select  **Frame** from the toolbar or press `F` to create a 360 W x 240 H frame.
2. Rename the frame to “album-art”.
3. Change the  corner radius to `4`.
4. Open the **Color picker** in the **Fill** section.
5. Select  **Image** from the fill options.
6. Select **Choose image** to add an image from your computer.

You can use the new [Make images](https://help.figma.com/hc/en-us/articles/24004542669463-Make-an-image-with-AI) AI feature to create images in Figma Design.

1. Select the album-art frame.
2. Open the  **Actions** menu and select **Make an image**.
3. Enter a prompt in the text field. Try to include as much context as possible.
4. Click **Make it** or press `Return` / `Enter`.

![](https://help.figma.com/hc/article_attachments/24635471447191)

### Add play-button instance to the frame

1. Select the play-button component.
2. While holding `Option``Alt` (Windows), click and drag a play-button instance into the album-art frame.
3. Hold `Option` (MacOS) or `Alt` (Windows) and use the arrow key to align the instance to the bottom-right corner of the album-art frame so that it is 16px to the right and bottom edge of the frame.

![](https://help.figma.com/hc/article_attachments/24632946342039)

### Add gradient fill to the album-art frame

You may notice that the play button is blended in with the image (especially when you use a darker image). We want to increase the visibility of the play button against the image. To do that, we can add a gradient fill on top of the image.

1. Select the album-art frame.
2. Click  the plus icon in the **Fill** section to add another layer fill.
3. Update the fill opacity from `20%` to `100%`.
4. Click the layer fill and select **Gradient** from the color picker panel.
5. Select the left color stop in the panel and update its opacity to `0%`.
6. Select the right color stop in the panel and update its opacity to `60%`.
7. Hold `Shift` and drag the top white handle to adjust the size of the gradient.

![](https://help.figma.com/hc/article_attachments/24633118186135)

### Apply constraints to the play button

When you resize the album-art frame, you’ll notice that the play button is not responsive to its parent frame.

We can fix this by applying constraints to the play button.

![](https://help.figma.com/hc/article_attachments/24633118190615)

1. Select the play-button instance.
2. Select   **Constraints** to open the Constraints menu.
3. Change the horizontal constraint to **Right** and the vertical constraint to **Bottom**.

Now when you resize the album-art frame, the play button will remain at the bottom-right corner of its parent frame. Nice!

![](https://help.figma.com/hc/article_attachments/24633751490711)

## Create two text layers for metadata

Next, we’ll create two text layers for the podcast title and the podcast creators.

To create a text layer for the podcast title:

1. Select  **Text** from the toolbar or press `T`.
2. Click on canvas to create a text layer.
3. Enter the podcast title. In our example, we’ll use “Tasty Bites: Exploring Culinary Delights” for our title.
4. In the **text properties** panel, update the typeface to `Lato`, font weight to `Bold` and font size to `16`.
5. Update the fill to `132745`.
6. Press `Command` `R` (Mac) or `Control` `R` (Windows) to rename the layer to “title”.

Let’s also create a text layer for the podcast creator.

1. Duplicate the **title** layer to create a new text layer for the podcast creators.
2. Double-click to edit the new text layer. In our example, the podcast creators will be “FoodieFiends”.
3. In the **text properties** panel, update the font weight to `Medium` and font size to `12`.
4. Press `Command` `R` (Mac) or `Control` `R` (Windows) to rename the layer to “creator”.

### Add auto layout to text layers

Now that our text layers are created, let’s wrap them in an auto layout frame.

1. Hold `Shift` and select both the title and creator layers.
2. Press `Shift` `A` to add auto layout.
3. Rename the new frame to “metadata”.
4. Change the **Gap between vertical items** settings to `4`.

Sometimes when we resize the metadata frame’s width, the text layers is not resizing with their parent frame. That is because the text layers are set to “hug content”, meaning they will only resize if the width of the text changes.

![](https://help.figma.com/hc/article_attachments/24638790556695)

Let’s update the settings:

1. Select the **metadata** frame.
2. Press `Enter` to select both text layers.
3. In the right sidebar, update the horizontal resizing to “Fill container”.

Now, try resizing the metadata frame’s width again. This time, the text layers resize with the parent frame. Great!

![](https://help.figma.com/hc/article_attachments/24638790562711)

You’ll notice that the text is pushed to multiple lines when the metadata frame’s width is shorter than the length of the text. In our design, we want to keep our text layer to one line and truncate the extra text.

1. Select both the **title** and **creator** layers.
2. Click  **Type settings** in the **Text** section.
3. Click  **Truncate text** to enable text truncation.
4. Set **Max lines** to `1`.

![](https://help.figma.com/hc/article_attachments/24638790569879)

## Add auto layout to the album art and metadata

1. Select both **album-art** and **metadata** frames.
2. Press `Shift` `A` to add auto layout.
3. Click the  plus in the **Fill** section.
4. Update the **Gap between vertical items** setting to `12`.
5. Hold `Command` (Mac) or `Ctrl` (Wins) and click on the **Horizontal padding** field to enable **All padding** field.
6. Enter `12` in the field.
7. Rename the frame to “card”.
8. Change the corner radius to `8`.

The card design looks great! But when you resize the card frame, you’ll notice that its child layers are not very responsive. Let’s update the resizing options to fix the issue.

![](https://help.figma.com/hc/article_attachments/24638775180823)

1. Select the **album-art** frame.
2. Set both **Horizontal resizing** and **Vertical resizing** to “Fill container”.
3. Select the **metadata** frame.
4. Set **Horizontal resizing** to “Fill container”, and **Vertical resizing** to “Fixed height”.

You may be wondering why the vertical resizing options are set differently on the two frames. That is because we want to keep the height of the metadata frame to two lines, and only the album art frame should stretch to fill the height of the card frame. If you set both the vertical resizing of both frames to fill container, they will both stretch to fill the card frame which is not something we want to achieve.

Try resizing the card again to see how response everything is!

![](https://help.figma.com/hc/article_attachments/24638775182871)

## Apply minimum and maximum dimensions

Applying a minimum and maximum width and height to the card will help us avoid funky designs like this:

![](https://help.figma.com/hc/article_attachments/24638790582039)

1. Select the card frame.
2. Select the **Width** field and choose **Add min width**.
3. Set the minimum width to `200`.
4. Select the **Width** field again and choose **Add max width**.
5. Set the maximum width to `400`.
6. Repeat the steps in the **Height** field, and set the minimum height to `240` and maximum height to `320`.

Now if you resize the card frame, it will stop resizing when it reaches its minimum or maximum dimensions.

![](https://help.figma.com/hc/article_attachments/24638790584343)

## Turn the card into a component

Let’s turn the card design into a component so it can be reused in our designs.

1. Select the card frame.
2. Click  **Create component**.

## What's next?

Our card component is done! Try creating some instances, updating the content, and adding some responsive designs. Have fun!

![](https://help.figma.com/hc/article_attachments/24638790587159)

If you’re interested to learn how to create the podcast card design or the loading animation, check out the following mini projects:

- [Create a loading animation](https://help.figma.com/hc/en-us/articles/18892560291351)
- [Create an onboarding flow with advanced prototyping](https://help.figma.com/hc/en-us/articles/18888057155991)
