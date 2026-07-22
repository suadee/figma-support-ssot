---
기술지원명: Create a reusable list component
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create a reusable list component
출처링크: https://help.figma.com/hc/en-us/articles/39749003039511-Create-a-reusable-list-component
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Auto layout](https://help.figma.com/hc/en-us/articles/5731482952599-Using-auto-layout), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants), [component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties)
- **Difficulty:** Intermediate
- **Length**: 25 minutes

In this project, we’ll create a reusable list component that can be customized to fit a variety of different designs.

We’ll start by creating the avatar, metadata, and checkbox components, which we’ll nest inside the list item component. Then, we’ll create a list component that can group multiple list items together with two variants: one with a container and one without. This flexible design will enable users to use the component in many different contexts, such as a leaderboard or a filter list.

![](https://help.figma.com/hc/article_attachments/39748997169815)

## Create the avatar component

We’ll start by creating an avatar component, which we’ll be able to nest inside the list item component.

To create the avatar component:

1. Use the  **Frame** tool to add a **24** X **24** frame to the canvas.
2. Double-click on the frame name and rename it to `avatar`.
3. Change the  **Corner radius** to `1000`.
4. Click  **Add stroke** in the **Stroke** section.
5. Use the settings to configure the stroke to the following:
   - **Fill:** `#E9DFDB`
   - **Position:** `Inside`
   - **Weight:** `1`
6. Click the color swatch in the **Fill** section to open the color picker menu.
7. Select  **Image** and upload an image from your computer as the avatar.
8. Click  **Create component** in the right sidebar or use the keyboard shortcut:
   - **Mac:** `Option` `Command` `K`
   - **Windows:** `Ctrl` `Alt` `K`

![](https://help.figma.com/hc/article_attachments/39748997170711)

## Create the trailing items

Next, we’ll create some trailing items for the list item: a checkbox component and a metadata component. These components will be placed on the right side of the list item component, and can be swapped out when using across different screens. For example, you can use the metadata component in a leaderboard to showcase user day streaks, or use the checkbox component in a filter menu.

![](https://help.figma.com/hc/article_attachments/39749003033623)

### Create the checkbox component default state

Let’s start by creating the checkbox component set with two variants: `default` and `selected`.

We’ll start with the default state:

1. Use the  **Frame** tool to add a **24** X **24** frame to the canvas.
2. Double-click on the frame name and rename it to `checkbox/default`.
3. Press `Shift` `X` to swap the rectangle’s fill and stroke.
4. Use the **Stroke** section of the right sidebar to configure the stroke to the following:
   - **Fill:** `#000000`
   - **Position:** `Inside`
   - **Weight:** `1`
5. Change the  **Corner radius** to `8`.
6. Select the frame and click  **Create component** in the right sidebar or use the keyboard shortcut:
   - **Mac:** `Option` `Command` `K`
   - **Windows:** `Ctrl` `Alt` `K`

![](https://help.figma.com/hc/article_attachments/39765652680471)

### Create the check icon for the checkbox selected state

Before we create the selected checkbox variant, we need to create a check icon.

1. Use the  **Frame** tool to add a **16** X **16** frame to the canvas.
2. Double-click on the frame name and rename it to `check`.
3. Use the  **Rectangle** tool to add a `5` X `10` rectangle to the center of the frame.
4. Press `Shift` `X` to swap the rectangle’s fill and stroke.
5. Use the **Stroke** section of the right sidebar to configure the stroke to the following:
   - **Fill:** `#000000`
   - **Position:** `Center`
   - **Weight:** `1`
6. Open the  **Advanced stroke settings** and change the **Join** to `Round`.
7. With the rectangle still selected, press `Enter` to open vector edit mode.
8. Select the top-left node of the rectangle and press `Delete` to remove it.
9. Press `Enter` again to close vector edit mode.
10. In the **Stroke** settings, set the **Start point** and **End point** to `Round`.
11. Enter `-45` in the **Rotation** field in the **Position** section of the right sidebar to rotate the layer.
12. Right-click and select **Flatten** from the menu or use the keyboard shortcut:
    - **Mac:** `Option` `Shift` `F`
    - **Windows:** `Alt` `Shift` `F`
13. Click and drag the check icon to make sure it’s centered in the frame.
14. Select the `check` frame and click the  minus in the **Fill** section to remove the frame’s fill.
15. Click  **Create component** in the right sidebar or use the keyboard shortcut:
    - **Mac:** `Option` `Command` `K`
    - **Windows:** `Ctrl` `Alt` `K`

![](https://help.figma.com/hc/article_attachments/39749096637847)

### Create the checkbox selected state

Now that we’ve created the check icon, we can move on to creating the `selected` state for the checkbox component.

1. Select the `checkbox`component you created previously and click  **Create variant** in the right sidebar.
2. With the new variant selected, click on the property name (currently called **Property 1**) in the **Current variant** section of the right sidebar and rename it to `state`.
3. Click on the property value (currently called **Variant2**) and change it to `selected`.
4. With the `selected` variant still selected, click the  plus in the **Fill** section to add a new fill.
5. Change the fill color to `#FA8891`.
6. Select the `check` icon component and hold the shortcut while dragging your cursor to create an instance:
   - **Mac:** `Option`
   - **Windows:** `Alt`
7. Drag the instance into the `selected` variant, and place it in the center of the frame. Be sure to check the Layers panel to make sure the check icon is inside the `selected` variant, not just visually on top of it on the canvas.

![](https://help.figma.com/hc/article_attachments/39749164842775)

### Create the metadata component

Now let’s create the metadata component:

1. Select the  **Text** tool, click on the canvas, and type `metadata`.
2. Use the **Typography** section of the right sidebar to change the **Font family** to `Outfit`, the **Font style** to `Regular`, and the **Font size** to `12`.
3. Update the fill to `#605957`.
4. Press `Shift` `A` to apply auto layout.
5. Double-click on the layer name and rename it to `metadata`.
6. Change the  Horizontal padding and the  Vertical padding to `0`.
7. Click  **Create component** in the right sidebar or use the keyboard shortcut:
   - **Mac:** `Option` `Command` `K`
   - **Windows:** `Ctrl` `Alt` `K`

![](https://help.figma.com/hc/article_attachments/39749213292311)

## Create the list item component

Great! Now that we’ve created all the leading and trailing components, we’re ready to create the list item component.

1. Select the  **Text** tool, click on the canvas, and type `List item`.
2. Use the **Typography** section of the right sidebar to change the **Font family** to `Outfit` , **Font style** to `Regular`, and the **Font size** to `16`.
3. Select the `avatar` icon component and hold the shortcut while dragging your cursor to create an instance:
   - **Mac:** `Option`
   - **Windows:** `Alt`
4. Drag the instance to the left side of the text layer we created.
5. Select both the `avatar` instance and text layer, and press `Shift` `A` to apply auto layout.
6. Double-click on the new frame name and rename it to `contents`.
7. Select the text layer inside the `contents` frame, and change its width resizing to `Fill container`.
8. Select the `contents` layer and set the **Gap** to `12` in the **Auto layout** section.
9. Change the  Horizontal padding and the  Vertical padding to `0`.
10. Select the default state of the `checkbox` component and hold the shortcut while dragging your cursor to create an instance:
    - **Mac:** `Option`
    - **Windows:** `Alt`
11. Drag the instance to the canvas, on the right side of the `contents` frame.
12. Select both the `contents` frame and `checkbox` instance, and press `Shift` `A` to apply auto layout. The spacing might look a bit off right now, but we’ll fix it in a few steps.
13. Double-click on the layer name and rename it to `list item`.
14. In the **Auto layout** section of the right sidebar, change the **Width** of the frame to `350` .
15. Change the **Gap** to `12`.
16. Set **Alignment** to `Align left`.
17. Change the  **Horizontal padding** to `0` and the  **Vertical padding** to `16`.
18. Click  **Add stroke** in the **Stroke** section to add a new stroke and configure it to the following:
    - **Fill:** `#E9DFDB`
    - **Position:** `Outside`
    - **Weight:** `1`
19. Click  **Individual strokes** and choose **Bottom** to apply the stroke along the bottom of the frame.
20. Select the `contents` layer, and change its resizing to `Fill container`.
21. Select the `list item` frame and click  **Create component** in the right sidebar or use the keyboard shortcut:
    - **Mac:** `Option` `Command` `K`
    - **Windows:** `Ctrl` `Alt` `K`

Your component should look similar to the following:

![](https://help.figma.com/hc/article_attachments/39749368936599)

## Apply component properties

The list item component is looking great! However, you may want to switch between different leading and trailing components, or you may not always need both items when reusing the component across different designs.

Instead of creating multiple variants to fit every possible combination, we can:

- Apply a boolean property to the leading and trailing components that will allow us to toggle their visibility on or off as needed
- Add an instance swap property to the trailing items that will let us easily switch between them
- Add text properties to the label and metadata that will create editable surfaces in the right sidebar that we can use to update the content

![](https://help.figma.com/hc/article_attachments/39749629831831)

### Apply the boolean properties

We’ll start by applying a boolean property to the leading and trailing items:

1. Select the `avatar` instance inside the `list item` component.
2. In the **Appearance** section of the right sidebar, click  **Apply variable/property**.
3. Click the  plus to add a new property and configure it to the following:
   - **Create:** `Property`
   - **Name**: `has leading`
   - **Value:** `True`
4. Click **Create property**.
5. Next, click the `checkbox` instance and repeat the process, configuring the new property to the following:
   - **Create:** `Property`
   - **Name**: `has trailing`
   - **Value:** `True`
6. Click **Create property**.

![](https://help.figma.com/hc/article_attachments/39749585089303)

### Apply the instance swap property

Next, we’ll add the instance swap property for the trailing components.

1. Select the `checkbox` layer inside the `list item` component.
2. Near the top of the right sidebar, click  **Create instance swap property**.
3. Set the name to `trailing item` and keep the value as the `checkbox` component.
4. Click the  plus next to **Preferred instances** to add the `metadata` component as a preferred instance.
5. Close the menu and click **Create property**.

![](https://help.figma.com/hc/article_attachments/39749585090071)

### Apply the text properties

Finally, we’ll a text property to the list item label and the text inside the metadata component.

We’ll start with the list item label:

1. Select the text layer inside the `list item` component.
2. Next to the **Content** field at the top of the right sidebar, click  **Apply variable/property**.
3. Click the  plus to add a new property and configure it to the following:
   - **Create:** `Property`
   - **Name**: `label`
   - **Value:** `List item`
4. Click **Create property**.

Next, apply a text property to the text inside the `metadata` component:

1. Locate the metadata main component and select the text layer inside.
2. Next to the **Content** field at the top of the right sidebar, click  **Apply variable/property** next to the content input field.
3. Click the  plus to add a new property and configure it to the following:
   - **Create:** `Property`
   - **Name**: `textvalue`
   - **Value:** `metadata`
4. Click **Create property**.

![](https://help.figma.com/hc/article_attachments/39749585090583)

## Expose nested instance

To wrap things up here, we’ll expose the nested `checkbox` instance to reveal its properties alongside the list item component.

#### Why expose nested instances?

Exposing nested instances helps users discover nested instances and their associated component properties without having to deep-select individual layers to find them. It’s a small, but impactful, way to make your design system assets easier to use.

When you select a top-level instance with exposed nested instances, a list of component properties for the top-level and nested instances will appear in the right panel. When hovering over a property row, a purple highlight appears around the corresponding object on the canvas so you know what you’re editing.

[Expose nested instances](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties#exposed-instances)

1. With `list item` component selected, click  plus in the **Properties** section of right panel and choose **Nested instances** under **Expose properties from**.
2. Select `checkbox` and close the menu.

When you select the list item component, you’ll now see the new boolean properties and nested instance in the **Properties** section of the right sidebar.

![](https://help.figma.com/hc/article_attachments/39749661155607)

## Create the list component

Now that we’ve created our list item component, we’re ready to build the list component. You might be wondering why we need to create an additional list component when we already have a list item component. Because list items are often used in repeating sets, a list component can help provide a consistent structure for layout and spacing.

To make the list component flexible enough to accommodate varying lengths, we’ll apply the slot property. This gives designers the freedom to control how many items appear in the list while preserving a consistent arrangement.

We’re going to create two variants for the list component: one with a container, and one without a container.

![](https://help.figma.com/hc/article_attachments/39750126359063)

### Create the variant with a container

We’ll build the container variant first:

1. Select the `list item` component and hold the shortcut while dragging your cursor to create an instance:
   - **Mac:** `Option`
   - **Windows:** `Alt`
2. Drag the instance to the canvas.
3. With the instance still selected, duplicate it using the keyboard shortcut:
   - **Mac:** `Command` `D`
   - **Windows:** `Ctrl` `D`
4. Select both instances, and press `Shift` `A` to apply auto layout.
5. Double-click on the layer name and rename it to `slot`.
6. In the **Auto layout** section of the right sidebar, change the **Gap** to `0` and check the **Clip content** box.
7. Now with the `slot` layer still selected, and press `Shift` `A` to apply auto layout again.
8. Double-click on the layer name and rename it to `list/yes`.
9. In the **Auto layout** section of the right sidebar, change the **Gap** to `0`.
10. Change the  **Horizontal padding** to `16` and the  **Vertical padding** to `8`.
11. Click the  plus in the **Fill** section to add a `#FFFFFF` fill.
12. Click the  plus in the **Stroke** section to add a new stroke.
13. Configure the stroke to the following:
    - **Fill:** `#E9DFDB`
    - **Position:** `Inside`
    - **Weight:** `1`
14. Change the  **Corner radius** to `16`.
15. Click  **Create component** in the right sidebar or use the keyboard shortcut:
    - **Mac:** `Option` `Command` `K`
    - **Windows:** `Ctrl` `Alt` `K`
16. Select the `slot` layer inside the component, and click **Convert to Slot** in the right sidebar or use the keyboard shortcut:
    - **Mac:** `Shift` `Command` `S`
    - **Windows:** `Shift` `Ctrl` `S`
17. Click **Create property**.

![](https://help.figma.com/hc/article_attachments/39750105745943)

### Create the variant without a container

Now let’s create the variant without a container.

1. Select the `list/yes` component you just created and click  **Create variant** in the right sidebar.
2. In the **Current variant** section of the right sidebar, click on the property name (currently called **Property 1**) and change it to `has container`.
3. Click on the property value (currently called **Variant2**) and change it to `no`.
4. Update the following auto layout settings:
   - **Gap:** `0`
   - **Horizontal padding:** `0`
   - **Vertical padding:** `0`
5. Change the  **Corner radius** to `0`.
6. Click the  minus in the **Fill** section to remove the frame’s fill.
7. Click the  minus in the **Stroke** section to remove the frame’s stroke.
8. Select the `slot` layer and uncheck the **Clip content** settings to reveal the bottom stroke of the last list item.

![](https://help.figma.com/hc/article_attachments/39750126359063)

## Test your list component

Our component set is now completed and now you can use it across different screens. With the slot property, users are able to add and arrange new list items directly without detaching your component. This gives more flexibility to design system consumers and allows healthier design systems.

![](https://help.figma.com/hc/article_attachments/39750126361623)

## What’s next?

Great work! You just created a list component using auto layout, variants, component properties, and nested components! From here, you can keep refining it by adding more nested components like icons, switches, or radio buttons.

Ready for a different challenge? Check out the the [Create an onboarding flow with advanced prototyping project](https://help.figma.com/hc/en-us/articles/18888057155991-Create-an-onboarding-flow-with-advanced-prototyping) or the [Figma Design for beginners](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners) course for more hands-on practice.

## Check your knowledge

## Additional resource

Grab a copy of the [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830) file for hands-on practice with examples and other projects from Figma's components collection.
