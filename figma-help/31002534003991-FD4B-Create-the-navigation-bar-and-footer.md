---
기술지원명: FD4B: Create the navigation bar and footer
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Create the navigation bar and footer
출처링크: https://help.figma.com/hc/en-us/articles/31002534003991-FD4B-Create-the-navigation-bar-and-footer
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Lesson overview

In this lesson, we’ll apply everything we’ve learned so far to build the navigation bar and footer elements for our portfolio website. Along the way, we’ll see how duplicating objects can save us time and effort throughout the design process.

## Create the navigation bar

First, we’ll build the navigation bar, which we’ll call the **nav bar** for short. The nav bar will be the primary navigation menu for people visiting our portfolio and will include space for a wordmark, menu items that link to pages in our site, and a button to open a contact page or email form.

![Navigation bar with a wordmark on the left, a "Case studies" link, and a "Let's work together" button aligned on the right.](https://help.figma.com/hc/article_attachments/31381947266711)

### Add the nav bar frame

We'll start by creating a frame to hold our nav bar elements.

1. With the  **Frame** tool selected, create a frame that is `1440` X `80`.
2. Rename the frame to `Navigation`.

**Note**: We’re using `1440` since that’s how wide the desktop frame preset is, but we’ll change this fixed value to **Fill container** when we add it to the final design to ensure it always spans the full width of the website at any width.

### Create your wordmark

Now that we have a frame, we can create our wordmark. A wordmark is a stylized, text-based logo that identifies a person or brand. It’s common to see wordmarks prominently featured in the navigation elements of a website to boost brand recognition and also provide a handy way for visitors to return to the homepage.

We'll create a wordmark using a text layer:

1. Create a new text layer inside the **Navigation** frame.
2. Enter your name, then click and drag the text layer to the left side of the frame. Use the red guidelines to help you center the text layer vertically on the frame. No need to stress about the spacing. We’ll use auto layout to take care of that shortly.
3. We’re sticking with the default **Inter** font for our wordmark but this is a great time to explore other fonts and find what fits your personal brand.
4. To help the wordmark to stand out amongst the other content in the nav bar, so we’ll switch up some of the typography properties to increase its visual weight and hierarchy. Select the text layer and change the **font weight** to something heavier, like `Black` and the **font size** to `20`.

![](https://help.figma.com/hc/article_attachments/31381977668887)

### Add some menu items

Great! Now let's add some menu item links to the nav bar.

1. Add another text layer to the **Navigation** frame and type `Link` as a placeholder for now. We’ll come back and update the label shortly.
2. Style the link to be lighter weight since we want it to have less visual weight than the wordmark. Set the **Font weight** to `Medium` and the **font size** to `16`.
3. Align the text vertically within the **Navigation** frame.
4. Position it off to the right side of the frame. The exact position isn't important, but be sure to leave a little more space for the rest of the nav bar's content.

In this course, we’re keeping things simple with just one link for a single additional page, but you may eventually need several pages as your portfolio grows. So why not plan ahead? Let’s add a few extra menu items to help future-proof our nav bar. Don’t worry—later in this lesson, we’ll walk through how to hide these extra layers until you need them!

Instead of using the **Text** tool to create more text layers, we can duplicate the text layer we just added.

### About duplicating objects

Duplicating an object streamlines the copy and paste process into a single step, making it a fast and easy way to replicate objects like layers, frames, sections, or instances.

There are two primary ways to duplicate an object: using the modifier key or the keyboard shortcut.

To duplicate an object using the modifier key, select the object and drag your cursor while holding the key:

- **Mac**: `⌥ Option`
- **Windows**: `Alt`

You can then place the duplicated object anywhere on the canvas.

**Tip:** Once duplicated, you can use **Tidy up** and **Smart selection** to evenly space a selection of duplicated objects, adjust the horizontal or vertical spacing between objects, or rearrange objects into neat rows, columns, or grids.

To duplicate an object with the keyboard shortcut, select it and press:

- **Mac**: `⌘ Command` `D`
- **Windows**: `Control` `D`

When using the shortcut method on shapes, text layers, components, and child frames, the duplicated object is placed directly on top of the original. You can then click and drag it to move it to its new position. For top-level frames and sections, the duplicated object appears to the right of the original where there is space on the canvas.

If you immediately use the keyboard shortcut on a duplicated object, Figma will maintain the same distance used between the first and second objects. Similarly, if you duplicate an object, rotate the duplicated object, then continue duplicating the object using the shortcut, the new objects will maintain the degree of rotation. These are great ways to create repeating patterns and custom shapes.

![](https://help.figma.com/hc/article_attachments/31784076136471)

### Add additional menu items

We’ll use both duplication methods to create more menu items:

1. Select the text layer, hold the modifier key, and drag the duplicated layer to the right of the original.
2. Select the new layer use the keyboard shortcut to duplicate it again. Figma recognizes the pattern and places the third layer to the right of the second.
3. Hold `Shift` and select all three text layers.
4. Click **Align vertical centers** to make sure they’re all aligned.
5. Press `Shift` `A` to add them to a frame with auto layout applied.
6. Set the **Horizontal gap** to `24`.
7. Rename the frame to **Links**.

![](https://help.figma.com/hc/article_attachments/31381947268247)

### Hiding unused layers in an auto layout frame

Let’s pause for a moment and talk about the flexible nature of auto layout. Remember when we mentioned future-proofing our design elements? Well, by incorporating auto layout, we’re ensuring our designs can adapt to different configurations.

If we wanted to add more menu items, we could create another text layer and drag it into the **Links** frame. Or, we could select an existing text layer and duplicate it using the shortcut we just learned. Either way, the auto layout frame will automatically grow to accommodate these changes.

If we wanted to remove menu items, we could delete the extra layers. That method works but it is a permanent change. Later on, when we add instances of our navigation bar, we won’t be able to add additional menu items without changing the main component, which would impact every instance in the file.

Instead, we can **hide** layers we don’t immediately want to use. Hiding a layer toggles the visibility of that layer without removing it from the frame. Auto layout respects the hidden layer and adjusts the frame as if the layer were removed.

![](https://help.figma.com/hc/article_attachments/31381947269143)

To hide a layer:

- Toggle the  visibility icon in the layers panel. You can also click and drag down to toggle multiple layers at once.
- Or use the keyboard shortcut
  - **Mac:** `Command` `Shift` `H`
  - **Windows:**  `Control` `Shift` `H`

Later on, you can unhide the layer on individual instances where its needed and auto layout will accommodate the newly visible layer. Learn more about [toggling layer visibility](https://help.figma.com/hc/en-us/articles/360041112614-Toggle-visibility-to-hide-layers).

### Add an instance of the button

The nav bar is starting to come together! Now, let’s add a button. Head over to the **Assets** tab in the left sidebar and select **Local assets**. Remember that button component we created earlier? Let's add an instance of it to the nav bar:

1. Click and drag an instance of the button into the **Navigation** frame.
2. Place it just to the right of the **Links** frame and use the guide to center it.
3. Select both the button and the **Links** frame, and press `Shift` `A`. We’re making a new frame here, rather than adding the button to the **Links** frame, so we can independently control the spacing between the menu items and the button.
4. Adjust the **Horizontal gap** to `40`.
5. Set both resizing properties to **Hug contents**.
6. Rename the frame to **Extra content**.

![](https://help.figma.com/hc/article_attachments/31381977670167)

### Add the final touches

Remember when we created the elements for our case study page? We set the **Max width** to `1000`, so they’ll all remain aligned on the page. We want the nav bar’s content—the wordmark, menu items, and button—to line up with the rest of those elements, while still allowing the **Navigation** frame to span the full width of the website. To do that, we need to connect the wordmark layer with the rest of the nav bar content.

1. Select the wordmark layer and the **Extra content** layer.
2. Add auto layout with `Shift` `A`.
3. Rename the new frame to **Content**.
4. Set the **Max width** for the frame to `1000` and leave the height resizing property set to **Hug contents**.
5. Set the horizontal gap to **Auto**.

![](https://help.figma.com/hc/article_attachments/33993951278743)

**Note**: Setting a resizing property to **Auto** equally distributes the available distance within the parent frame between the child layers. Because we only have two sets of layers—our wordmark and the **Extra content** frame—**Auto gap** will push them to the edges of the frame, as far apart as possible.

### Add auto layout to the Navigation frame

Next, we'll apply auto layout to the **Navigation** frame.

1. Select the **Navigation** frame and press `Shift` `A`.
2. In the **Auto layout** section, set the height resizing to **Fixed** and make sure the value is set to `80`.
3. Set **Horizontal padding** to `24` and the **Vertical padding** to `0` (zero) and the frame’s alignment to **Center**.

![](https://help.figma.com/hc/article_attachments/33993951280279)

Now that the **Content** frame is inside a parent frame with auto layout applied, we can update its width resizing:

1. Select the **Content** frame inside the **Navigation** frame.
2. Make sure the **Width resizing** is set to **Fill container**.
3. Finally, set the **Content** frame’s alignment to **Center**.

![](https://help.figma.com/hc/article_attachments/33993956356375)

## Create the footer element

The nav bar looks great! Now it’s time to build the footer element. Taking a look at the final design, you’ll notice the footer looks very similar to the navigation bar. Let’s save ourselves a bunch of time and use the **Navigation** frame as the foundation of our footer.

![Portfolio footer with wordmark on the left and contact details, including email and phone number, aligned on the right.](https://help.figma.com/hc/article_attachments/31703930113559)

1. Duplicate the **Navigation** frame.
2. Rename the duplicated frame to **Footer**.
3. Unlike the nav bar, we don’t need a button in the footer. Locate the **Button** layer in the Layers section and delete it.
4. We want to keep the **Links** frame, but the **Extra content** frame is no longer doing anything so we can remove it. Select the **Extra content** frame, right-click, and select **Ungroup.** Ungrouping a frame removes it from the canvas and pushes its child layers up in the layer hierarchy.
5. We’ll use this space for our contact info so let’s rename the **Links** frame to `Contact`.

![](https://help.figma.com/hc/article_attachments/31703930114071)

## Customize the navigation bar

Because we want the content in the nav bar and footer to be the same on every page, let’s update the copy before turning them into components. That way, we won’t have to update the copy in every instance we add.

1. In the **Navigation** frame, update one of the menu item labels to `Case studies`.
2. Since we only need one link at the moment, we'll hide the other two text layers for now.
3. Update the button's label to give it a strong call to action like "Let's work together".

![](https://help.figma.com/hc/article_attachments/31703919801879)

## Customize the footer

1. Update the text layers to include your email address, phone number, or other contact information.
2. Hide the third text layer for now.

![](https://help.figma.com/hc/article_attachments/31703919802519)

## Turn each element into a component

When you're done customizing your navigation bar and footer, turn both of them into components. Then, move them to the **Components** page.

## Lesson wrap up

Excellent work! We just built a navigation bar and footer element using text, frames, instances, and auto layout. We then turned them both into components so we can reuse them on every page of our website.

In the next lesson, we’ll use boolean operations, vector edit mode, and the arc tool, along with auto layout, to create an element that showcases our skills to potential employers.
