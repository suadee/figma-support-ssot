---
기술지원명: FD4B: Create the card and container system
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Create the card and container system
출처링크: https://help.figma.com/hc/en-us/articles/30987538800023-FD4B-Create-the-card-and-container-system
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

In this chapter, we’ll use auto layout to build a responsive card element for our portfolio’s landing page. Then, we’ll revisit the elements we built in the previous lessons and apply auto layout to them to build a container system for our portfolio. Finally, we’ll wrap things up by turning all of the elements into reusable components.

## Create the card element

We’ll start by building the card element. Cards are used to present bite-sized chunks of content in a way that encourages viewers to interact with it to see more details. The name “cards” comes from their resemblance to physical cards—like playing cards.

Even if the term is new to you, you probably interact with card elements every day—whether you’re browsing a streaming service, shopping online, or scrolling through your social media feed. Thanks to their modular and flexible nature, cards have quickly become a popular pattern in modern product design.

![](https://help.figma.com/hc/article_attachments/31356380654359)

Our card will be used to showcase past work and give readers an entry point to another page where they can learn more about the project.

The card will include:

- An **image** to give a visual preview of our work
- A **heading** for the project name
- A short **text description** of the project
- A call to action **button**

![Responsive card element with image placeholder, project title, brief description, and call-to-action button.](https://help.figma.com/hc/article_attachments/31356380656151)

### Create the card title and description

We'll start by creating the card's title layer:

1. Create a new text layer.
2. Type `Project title` as placeholder text for the title.
3. Adjust the following properties:
   - Set the **Font family** to `Inter`
   - Set the **Font weight** to `Semi Bold`
   - Set the **Font size** to `25`
   - Set the **Line heigh**t to `38`
   - Set the **Alignment** to `Left`

![](https://help.figma.com/hc/article_attachments/31356380657175)

Next, we'll create the card's description.

1. Select the layer you just created and use the keyboard shortcut to duplicate it:
   - Mac: `⌘ Command` `D`
   - Windows: `Ctrl` `D`
2. Move the new text layer below the title. Don't worry about precise spacing for now.
3. Adjust the following properties:
   - Font weight to `Medium`
   - Font size to `20`
   - Leave the other properties the same
4. Add a short bit of placeholder text for the description.

![](https://help.figma.com/hc/article_attachments/31356380658455)

### Add an instance of the button

Now let’s add our button. Instead of using the main component, we’ll add an instance of that component to the canvas.

There are a few different ways you can create an instance of your component:

- Select the main component on the canvas and duplicate it using the keyboard shortcut
  - Mac: `⌘ Command` `D`
  - Windows: `Ctrl` `D`
- Hold down the modifier key and click and drag the main component to duplicate it
  - Mac: `⌥ Option`
  - Windows: `Alt`
- Open the **Assets** panel in the left sidebar, and click and drag a component onto the canvas

Whichever method you choose, place the instance below the description text layer and make sure the layers are left aligned. The spacing between layers doesn’t need to be perfect—we’ll fix it using auto layout.

![](https://help.figma.com/hc/article_attachments/31356380659479)

### Add an image placeholder

Next, we'll create a rectangle which we'll use as an image placeholder.

1. Use the **Rectangle** tool to click and drag to create a rectangle to the left of the other layers.
2. Change its height to `350`. Don't worry about the width for now.
3. Click the color swatch in the fill section of the properties panel to open the color picker
4. Select **Image** at the top.
5. Rename the layer to **Thumbnail**.

![](https://help.figma.com/hc/article_attachments/31356380660375)

## Add auto layout to the card element

Now that we have all the pieces of our card element, it’s time to put them together using auto layout.

### Apply auto layout to the description

1. Select the text and button layers.
2. Press `Shift` `A` to add them to an auto layout frame.
3. Rename this new frame to **Description**.
4. Make sure the **Direction** is set to **Vertical** the **V****ertical gap** is set to `16`. Leave the rest of the auto layout properties as they are.

![](https://help.figma.com/hc/article_attachments/33973695362839)

### Add the layers to a parent frame

Now we need to add all of our layers to a parent frame.

1. Select both the **Description** frame and the **Thumbnail** layer.
2. Press `Shift` `A` to create a new auto layout frame.
3. Rename the frame to `Content`.

You might be wondering why we added the text and button layers to their own frame instead of including everything in a single parent frame. Auto layout frames can only flow in one direction. But our card content has elements that need to flow both horizontally and vertically. Nesting auto layout frames within other auto layout frames lets us create multi-dimensional layouts with elements that flow in different directions.

This nested structure also allows us to set different padding values between objects. We already set the vertical padding between our text and button layers, so now let’s set the horizontal padding between the **Thumbnail** and **Description** frame:

1. Select the **Content** frame
2. Change the **Horizontal gap** to `32`.

![](https://help.figma.com/hc/article_attachments/33973657648151)

When adding auto layout to existing layers, the auto layout properties are determined by how the child layers are arranged on the canvas. When we applied auto layout to the text and button layers, Figma automatically set the frame’s direction to **Vertical** because the layers were arranged in a vertical stack. Because the Thumbnail and Description layers are positioned side-by-side, Figma automatically set the **Content** frame’s direction to **Horizontal**.

A child layer’s position on the canvas also determines what the parent frame’s alignment is set to when auto layout is applied. If your **Description** frame was aligned with the horizontal center of the **Thumbnail** layer, your alignment may be set to **Align left**. Make sure the **Content** frame’s alignment is set to **Align top left** instead.

### Give the parent frame a maximum width

We also need to give the **Content** frame a maximum width, so that our card element takes up the same amount of horizontal space as the other elements in our portfolio design.

1. Select the **Content** frame.
2. In the **Auto layout** section, open the **Width** **resizing** dropdown menu.
3. Select **Add max width**.
4. Enter `1000` in the **Max width** field. This means that the frame can only ever reach a maximum of 1,000 pixels wide regardless of the content inside.

![](https://help.figma.com/hc/article_attachments/31356424220695)

Depending on the length of your text layers, your **Description** frame may be spreading beyond the Content frame’s bounding box. Let’s fix that.

1. Select the **Description** frame and change the **Width resizing** to **Fill container**.
2. Leave the height resizing as-is, we don't need to adjust that yet.
3. Do the same for the **Thumbnail** layer. This will allow our description to grow and shrink, while making sure the width of the text content matches the width of the image.
4. We'll also lock the thumbnail's  aspect ratio so that its dimensions can scale proportionally.

![](https://help.figma.com/hc/article_attachments/31356424221207)

**Note:** If your text layers are still going beyond the **Content** frame’s boundaries, you may need to adjust the two text layer’s width resizing directly. Select the two text layers and check to make sure their **Width resizing** properties are set to **Fill container**.

## Create the container system

We want to add several cards to our portfolio’s landing page, so we’ll turn our card into a component. But before we do that, let’s compare what we’ve created to the finished portfolio design.

![](https://help.figma.com/hc/article_attachments/31704175629591)

The **Content** frame in our final design is nested inside another frame with auto layout applied. And if we keep looking, we can see that the same can be said for most of the other portfolio elements, including the landing page hero, the text block, and the image block. Let’s explore why we’ve structured them this way.

![](https://help.figma.com/hc/article_attachments/31704175630359)

By adding an additional frame around an element, we can create a container system for our portfolio. A container system turns each element into discrete blocks, making it easy for us to add, reorder, and swap blocks as we build our designs.

We can still change aspects of individual blocks—like updating the content, adding a background fill, or adjusting the top and bottom padding—without worrying how these changes will impact the rest of the content on the page.

Let’s walk through an example to better understand the benefits of using a container system. Imagine a layout with several card elements, and we want to add a background fill behind one card to help emphasize content we want to draw the visitor’s eye to.

If we were to apply the fill directly to the **Content** frame, the fill will only extend to the frame’s boundary. By adding the element to a container frame, we can ensure the background fill spans the entire page width without impacting the element’s responsiveness, or its alignment on the page.

![](https://help.figma.com/hc/article_attachments/31704169946263)

Now that we know more about container systems, we’ll revisit the elements we built earlier and apply auto layout to them. We’ll also turn each element into a component so they’ll be ready for when we build our final portfolio design.

### Finish the card element

We’ll start by completing the card element we were working on in the previous chapter.

1. Select the  **Frame** tool.
2. Click and drag to create a new frame around the **Content** frame. Check the layers section in the left sidebar to make sure the **Content** frame is inside the new frame.
3. Rename the new frame to **Project card.**
4. Press `Shift` `A` to add auto layout.
5. Change the following auto layout properties:
   - Set the **Alignment** to **Center**.
   - Set the **Horizontal padding** to `24`.
   - Set the **Vertical padding** to `56`.
   - Set the **Height resizing** to **Hug contents**.
   - Leave the **Width resizing**  set to **Fixed**. We'll eventually set this to **Fill content** when we build our final designs.

![](https://help.figma.com/hc/article_attachments/33973695363863)

### Revisit the other elements

Alright, it’s time to add the rest of our portfolio elements to containers! Revisiting past work might feel a little repetitive, but design is all about iteration. The time and effort invested now will pay off when we put our final designs together later.

As we update each element in this next section, you’ll notice the auto layout configurations follow a similar pattern. Most elements will have a **M****ax width** of `1000`their **Horizontal padding** set to `24` and their **Vertical padding** to `56`

However, a few key elements will have some slight adjustments to help them stand out, this includes the:

- Landing page hero
- Section heading
- Impactful text block
- Quote block

With that in mind, let's walk through how we'll add this container system to the other elements we've just designed.

Tip: Get your keyboard shortcut hand ready to hit `Shift` `A` to add auto layout!

### Update the landing page hero

First, we revisit the landing page hero.

1. Select the **Landing page hero** frame and press `Shift` `A` to add auto layout.
2. Set the **M****ax width** to `1000`.
3. Set the **Vertical gap** to `24`.
4. Set both **padding** options to `0` (zero).

![](https://help.figma.com/hc/article_attachments/33973657649943)

Next, we’ll add the container frame.

1. With the  **Frame** tool enabled, click and drag to add a new frame that surrounds the **Landing page hero** frame.
2. Rename this new frame to **Personal bio**.
3. Select the frame and apply auto layout.
4. Change the **Alignment** to `Center`
5. Set the **Horizontal padding** to `24` and the **Vertical padding** to `104`. The extra vertical padding emphasizes the bio’s importance, helping it stand out from the other elements.
6. Select the **Landing page hero** frame (that's the inner frame in case you're a bit lost) and change the **Width resizing** to **Fill container**.

![](https://help.figma.com/hc/article_attachments/33973657650327)

### Update the section heading

We’ll tackle the section heading next.

1. Select the **Section heading** text layer and press `Shift` `A`.
2. Rename the new frame to `Section heading`.
3. Select the text layer inside the frame.
4. Give the layer a max width of `1000`.
5. Set both resizing properties to `Fill container`.

To create a strong visual relationship between the section heading and the content that follows it, we’ll use different padding values on the top and bottom of the frame.

1. Select the **Section heading** frame.
2. Select **Individual padding** in the auto layout section and set the padding values:
   1. Left and right padding to `24`.
   2. Top padding to `72`.
   3. Bottom padding to `0` (zero).

![](https://help.figma.com/hc/article_attachments/33973695365271)

### Update the paragraph text

We’re making progress!

1. Next, select the paragraph text layer and press `Shift` `A`.
2. Rename the new frame to `Text block`.
3. Select the text layer inside the frame and give it a **Max width** of `1000`.
4. Set the width resizing to `Fill container`.
5. Select the **Text block** frame.
6. Set the **Horizontal padding** to `24` and the **V****ertical padding** to `56`.

![](https://help.figma.com/hc/article_attachments/33973657651223)

### Update the quote block

Great job so far! We'll update quote block next.

1. Select the **Quote** text layer and add auto layout using `Shift` `A`.
2. Rename the frame to `Quote block`.
3. Select the text layer and give it a max width of `570`. Recall that we gave this text layer a specific width of `570`. That’s because we want the quote block to act as a visual break on the page.
4. Set the **Width resizing** to **Fill container**.
5. Select the **Quote block** frame and change the **Horizontal padding** to `24` and the **Vertical padding** to `56`.

![](https://help.figma.com/hc/article_attachments/33973695365655)

### Update the image

We’re down to our last two elements!

1. Select the **Image** layer and add auto layout with `Shift` `A`.
2. Rename the new frame to `Image block`
3. Change the **Horizontal padding** to `24` and the **Vertical padding** to `56`.
4. Select the nested image layer, set the **Max width** to `1000` and the **Width resizing** to **Fill container**.

![](https://help.figma.com/hc/article_attachments/33973695366039)

### Update the impactful text

We're almost done! For this final element, we actually won't be using the container system since it is already designed to span the full width of the website. We still have a few steps to do though:

1. Select the **Impactful text** frame and add auto layout with `Shift` `A`.
2. Change the **Horizontal padding** to `24` and the **Vertical padding** to `128`. Like in the **Personal bio** element, this extra chunky vertical padding will help offset this prominent element from other content on the page.

![](https://help.figma.com/hc/article_attachments/33973695366167)

## Create multiple components

Our portfolio elements not only look great, but are now responsive. Now comes the fun part—turning them into components!

Instead of creating individual components, we can create components in bulk. You can create up to 100 components at once, which comes in handy right about now.

1. Select all of the elements.
2. Click the arrow next to **Create component** in the right sidebar.
3. Choose **Create multiple components**.

![](https://help.figma.com/hc/article_attachments/33973657652503)

## Move components to the Components page

To keep our file organized, we’ll move our main components over to the Components page. To do this:

1. Click and drag to select all of the components we just created plus the Button component we created earlier.
2. Right-click on the selection, hover over **Move to page**, and select **Components**.

![](https://help.figma.com/hc/article_attachments/31704175635735)

Now that we’ve moved our elements, the **Case study desktop frame** preset we added earlier should be empty. We won’t be using it again so you can either delete it or save it to use for your own future explorations.

## Lesson wrap up

Excellent work! Not only did we use auto layout to design a card element, we also revisited the other portfolio elements and added them to a container system. We finished the lesson by turning our portfolio elements into reusable components and moving them to our dedicated Components page.

Coming up next, we’ll apply what we learned about auto layout and components to build navigation bar and footer elements for our website.
