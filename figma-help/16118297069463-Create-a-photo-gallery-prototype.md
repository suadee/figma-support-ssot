---
기술지원명: Create a photo gallery prototype
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a photo gallery prototype
출처링크: https://help.figma.com/hc/en-us/articles/16118297069463-Create-a-photo-gallery-prototype
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma), [shapes](https://help.figma.com/hc/en-us/articles/360040450133-Basic-shape-tools-in-Figma-design), [text](https://help.figma.com/hc/en-us/articles/360039956474-Create-and-edit-text), [adding and replacing images](https://help.figma.com/hc/en-us/articles/360040028034-Add-images-to-design-files), [renaming layers in bulk](https://help.figma.com/hc/en-us/articles/360039958934-Rename-Layers), [prototyping](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma), [smart animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames)
- **Length**: 20 minutes

In this project, we’ll learn about prototyping and the power of smart animate.

To do so, let’s build a simple photo gallery app. The gallery app has three images. Clicking an image opens an expanded view so you can view the image full screen. From the expanded view, you can click **Back** to bring you back to the gallery view. This project will be a low-fidelity mockup—we’ll focus more on building interactive elements to show how the app works, and less on design and style.

![An animation demonstrating the final photo gallery prototype. ](https://help.figma.com/hc/article_attachments/25316886617495)

## Create a wireframe with frames, shapes, and text

To start, we’ll use the following objects for our wireframe:

- Two frames, one for a gallery view page and one for an expanded view page
- Squares and rectangles with image fills
- Text layers for the back button

### Create a file

Let’s begin by creating a new design file.

1. Log in to your Figma account from [figma.com](https://figma.com/).
2. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Drafts**.
3. Click **New design file**.

**Tip:** You can visit <figma.new> from your web browser to quickly create new design files.

### Set up frames

Let’s add the gallery view frame in our file.

#### **What is a frame?**

[Frames](https://help.figma.com/hc/en-us/articles/360041539473) are the main building blocks of Figma. A frame is a container that holds design elements such as shapes, text, and images. You can use them to organize and structure design elements on the canvas.

A frame can be any size and can contain any number of design elements. Frames can also be nested within other frames to create complex designs with multiple levels of hierarchy.

[Frames](https://help.figma.com/hc/en-us/articles/360041539473)

1. Click the  **Frame** icon from the toolbar or press `F`.
2. From the **Design** panel on the right sidebar, select the **iPhone 14 & 15 Pro** preset size.

![create-a-frame.gif](https://help.figma.com/hc/article_attachments/25310094669335)

Let’s rename the frame to make it more descriptive.

1. Hover over the frame you just created on canvas, and double-click on the name of the frame.
2. Rename the frame **gallery-view** and press `return` (Mac) or `enter` (Windows).

![](https://help.figma.com/hc/article_attachments/25310107733399)

Now let’s make another frame for the expanded view. It will have the same size as the gallery view, so we can create the new frame by duplicating the existing frame.

1. Select the **gallery-view** frame, and press `Command` + `D` (Mac) or `Control` + `D` (Windows) to duplicate.
2. Rename the new frame to **expanded-view** and press `return` (Mac) or `enter` (Windows).

![](https://help.figma.com/hc/article_attachments/25311674073239)

### Add squares and image fills

Now let’s add images in the gallery view frame. You will need to have the images downloaded to your computer to upload them. For our example, we have prepared three plant images to upload.

**Tip:** Figma doesn't have a specific layer type for images. Instead, images are a type of fill. This allows you to add images to any shape or vector network. [Learn more about images →](https://help.figma.com/hc/en-us/articles/360041090073-Upload-an-image-as-a-fill)

Let’s create a square in the **gallery-view** frame.

1. Select the **Rectangle** tool or press `R`.
2. While holding `Shift` on the keyboard, click and drag on the **gallery-view** frame to create a square with a width of 200 and height of 200. You can use the **Width** and **Height** fields in the right sidebar to view and adjust pixel values.

   **Tip:** Holding  `Shift`  while creating a shape will constrain the proportion of the shape, which keeps the width and height the same.
3. Let’s align the square to the center of the frame. We’ll click and drag the square towards the center of the frame until we see a red line appear on the frame, indicating the square is center-aligned to the frame.

![](https://help.figma.com/hc/article_attachments/25311677340567)

Then add an image to the square as a fill:

1. With the square selected, click on the **Fill** swatch in the right sidebar to open the color picker.
2. Select  **Image** from the panel.
3. A placeholder image of black and white checks will be applied to the shape. Hover over the preview image, click **Swap image** and **Upload new**.
4. Select the first image you want to upload from your computer and click **Open** to apply.

The image will be added to your shape as a fill.

![](https://help.figma.com/hc/article_attachments/25311677346967)

### Duplicate to add more squares

Now let’s add two more squares by duplicating the first square.

1. Select the square, and press `Command` + `D` (Mac) or `Control` + `D` (Windows) to duplicate.
2. The new square is placed directly on top of the first rectangle. Click and drag the second rectangle to the middle of the frame.
3. Then, duplicate the square again by pressing `Command` + `D` (Mac) or `Control` + `D` (Windows).

**Tip:** When duplicating an object, Figma will try to maintain the same x and y positions within the destination frame relative to its position in the group or frame it was copied from. This helps when you need to quickly duplicate objects with even spacing between them.

![](https://help.figma.com/hc/article_attachments/25312961370263)

### Replace image fills

Now that we have three identical images inside the frame, we need to replace two of them. Like adding an image, we can replace an image from the **Fill** swatch.

1. Select the second image, and click on the **Fill** swatch in the right sidebar to open the color picker.
2. Select the  image from the panel.
3. Hover over the image preview, click **Swap image** button and select **Upload new**.
4. Select the second image from your computer and click **Open** to apply it as a new fill.

![](https://help.figma.com/hc/article_attachments/25314611651863)

Nice! We’ll do the same for the third image. When you’re done, you should have your low-fidelity photo gallery design with three different images:

![](https://help.figma.com/hc/article_attachments/25314611657239)

### Add text

Now that the **gallery-view** frame is done, let’s move on to the next frame. We’ll add a back button in the **expanded-view** frame.

1. Select the  **Text** tool from the toolbar, or press `T`.
2. Click on the top left of the **expanded-view** frame and type “Back”.
3. With the text layer selected, set text size to 24 and change its weight to **Semi Bold**.

Nice!

![](https://help.figma.com/hc/article_attachments/25314626187159)

### Add a rectangle for expanded view

Now, let’s mock up the expanded view of our photo gallery app. We want this to show a bigger version of the image if a user selects it.

First, we’ll create the basic structure of the **expanded-view** design by adding a rectangle.

1. Select the **Rectangle** tool or press `R` and click inside the **expanded-view** frame.
2. Use the **Width** and **Height** fields in the Layout section to enter in pixel values for the shape. We’ve set the width of our rectangle to 393, and the height to 700.
3. Arrange the rectangle underneath the back button and align it to the center of the frame.

![create-rectangle-in-expanded-view.gif](https://help.figma.com/hc/article_attachments/25316843321239)

### Duplicate frame

Since we need an expanded view frame for each image, let’s duplicate the frame we just made so we have three **expanded-view** frames in total.

1. Select the **expanded-view** frame, and press `Command` + `D` (Mac) or `Control` + `D` (Windows) to duplicate.
2. Repeat the command again so that we have three **expanded-view** frames.
3. Let’s rename the frames to **expanded-view-1**, **expanded-view-2**, and **expanded-view-3** accordingly.

### Copy image fills

We already have images added for the gallery view, but now we need to add those same images to the expanded view frames. We can do that by copying the image fills from the squares in the **gallery-view** frame:

1. Select the first image from the **gallery-view** frame.
2. In the **Fill** section of the right sidebar, select the area just to the left of the image preview.
3. Copy the fill using the keyboard shortcut:
   - Mac: `Command` + `C`
   - Windows: `Control` + `C`
4. Then, select the rectangle in **expanded-view-1** frame and paste the image fill using the keyboard shortcut:
   - Mac: `Command` + `V`
   - Windows: `Control` + `V`

![](https://help.figma.com/hc/article_attachments/25316886627607)

Nice! Now let’s repeat the steps and add the rest of the images. When you’re done, your design should look something like this:

![](https://help.figma.com/hc/article_attachments/25316886635031)

### Rename layers in bulk

It’s almost time to add prototype interactions! Before we can start prototyping, let’s take a moment to rename our layers—matching layer names will be important for our prototyping interactions.

Each image on the **gallery-view** frame should have the same name as it’s matching image on the **expanded-view** frames. We can rename them together using the bulk renaming feature.

1. While holding `Shift` on the keyboard, select the first image in the **gallery-view** frame and the image in **expanded-view-1** frame.
2. Press `Command` + `R` (Mac) or `Control` + `R` (Windows) to open the rename layer modal.
3. In the modal, enter "image-1" in the **Rename to** input field.
4. Click the **Rename** button to confirm the change.

Great! Now let’s repeat the steps for the rest of the images.

We’ll rename the second image in **gallery-view** frame and the image in **expanded-view-2** frame to image-2, and the third image in **gallery-view** frame and the image in **expanded-view-3** frame to image-3.

![](https://help.figma.com/hc/article_attachments/25316886637591)

## Add prototyping

We’ve finished creating a wireframe for our gallery. Now let’s add prototyping interactions.

![A prototype flowchart. Each image opens up an expanded view, and each expanded view routes back to the gallery view.](https://help.figma.com/hc/article_attachments/16121836207639)

When a user clicks on an image in the **gallery-view** frame, it will direct us to its **expanded-view** frame accordingly. Clicking on the back button will redirect us back to the **gallery-view** frame.

Let’s see how we can do that.

First, we’ll add a connection between image-1 in the **gallery-view** frame to the **expanded-view-1** frame.

1. Switch to prototype mode using the `Shift` + `E` keyboard shortcut, or by clicking the **Prototype** tab in the right sidebar.
2. Hover over the image-1 layer in the **gallery-view** frame.
3. Click the  blue plus sign on the edge of the button, then drag the connection to **expanded-view-1** frame. This opens up the **Interaction details** modal.
4. From the dropdown menu, set the trigger to **On click**.
5. Set the action to **Navigate to**. From the dropdown menu, set the destination to **expanded-view-1** frame.
6. From the **Animations** dropdown menu, select **Smart Animate**.

Smart animate looks for matching layers that exist across multiple frames. Figma takes into account both the layer's name and where it sits within the hierarchy. Since we have renamed our image layers previously, we’re able to create smooth transitions when we are moving across frames.

[Learn more about smart animate →](https://help.figma.com/hc/en-us/articles/360039818874-Create-advanced-animations-with-smart-animate)

“On tap” or “on click”? These two triggers work the same way. If you set the prototype device to a phone, the trigger will change to “on tap” from “on click”.

![](https://help.figma.com/hc/article_attachments/25316886647959)

Let’s repeat the actions for image-2 and image-3 in the **gallery-view** frame accordingly. When you’re done, you should have image-2 in the **gallery-view** frame to the **expanded-view-2** frame, and image-3 in the **gallery-view** frame to the **expanded-view-3** frame.

Awesome! Now we want to add the connection from the back button to **gallery-view** frame.

1. Switch to **Prototype** mode using the `Shift` + `E` keyboard shortcut.
2. While holding `Shift` on the keyboard, select the back buttons in all the expanded view frames.
3. Click the  blue plus sign on the edge of the selection, then drag a connection to the **gallery-view** frame.
4. In the **Interaction details** modal, set the trigger to **On click**.
5. Set the action to **Navigate to**. From the dropdown menu, set the destination to **gallery-view** frame.
6. From the **Animations** dropdown menu, select **Smart Animate**.

![](https://help.figma.com/hc/article_attachments/25316886656535)

Once you’re done, close the **Interaction details** modal. Press the  **Present** button to test it out.

![](https://help.figma.com/hc/article_attachments/25316886617495)

Congratulations, you’re all done!
