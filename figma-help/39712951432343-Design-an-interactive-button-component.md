---
기술지원명: Design an interactive button component
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Design an interactive button component
출처링크: https://help.figma.com/hc/en-us/articles/39712951432343-Design-an-interactive-button-component
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Auto layout](https://help.figma.com/hc/en-us/articles/5731482952599-Using-auto-layout), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants), [prototyping](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma)
- **Difficulty:** Intermediate
- **Length**: 20 minutes

In this project, we’re going to design a reusable button component that changes as you interact with it. To do this, we’ll build a button component set using variants, then configure prototyping connections to add interactivity.

![](https://help.figma.com/hc/article_attachments/39712951355671)

## Create the save icon

To start, we’ll create a simple save icon that we’ll add to our button later.

1. Use the  **Frame** tool to add a **24** X **24** frame to the canvas.
2. Double-click on the frame name and rename it to `icon`.
3. Click the  minus in the **Fill** section to remove the frame’s fill.
4. Use the  **Rectangle** tool to add a **12** X **18** rectangle to the center of the frame.
5. Press `Shift` `X` to swap the rectangle’s fill and stroke.
6. Use the **Stroke** section of the right sidebar to configure the stroke to the following:
   - **Fill:** `#000000`
   - **Position:** `Inside`
   - **Weight:** `2`
7. Change the  **Corner radius** to `1`.
8. Select the rectangle and press `Enter` to open vector edit mode.
9. Hover over the bottom of the rectangle and click to add a new vector point.
10. Select the point and change the **Y-position** value to `17`.
11. Press `Enter` again to close vector edit mode.
12. Select the frame and click  **Create component** in the right sidebar or use the keyboard shortcut:
    - **Mac:** `Option` `Command` `K`
    - **Windows:** `Ctrl` `Alt` `K`

![](https://help.figma.com/hc/article_attachments/39712967071767)

### Create the icon component set

Nice work! Next, we’ll create a filled variant of our save icon that will display when the button is pressed.

Select the component you just created and click  **Create variant** in the right sidebar.

When you add your first variant, Figma will make an identical component with the same properties applied and add both to a component set, identified by a dashed purple border. Because our original component was named `icon`, the component set is automatically named `icon`. If you take a look at the right sidebar, you’ll notice a new component property called **Property 1** is available, with `default` and `Variant2` as available values. Let’s update this property and configure the rest of our icon component set.

![](https://help.figma.com/hc/article_attachments/39712951357719)

1. Select the original component at the top of the component set.
2. In the **Current variant** section of the right sidebar, click on the property name (currently called **Property 1**) and change it to `Has fill`.
3. Click on the property value (currently called **default**) and change it to `false`.
4. Next, click on the second variant in the component set and change its `Has fill` property value to `true`.
5. Select the vector inside the **Has fill=true** variant, click the  plus in the **Fill** section and change its fill to `#000000`.

Your icon component set should look similar to the following:

![](https://help.figma.com/hc/article_attachments/39712951358743)

**Tip:** You can also find pre-made icon sets on the [Figma Community](https://figma.com/community/icons?resource_type=files).

## Create the button main component

Next, we’ll create the button main component.

1. Select the  **Text** tool, click on the canvas, and type `Save`.
2. Double-click on the layer name and rename it to `label`.
3. Use the **Typography** section of the right sidebar to change the font family to `Outfit` and the font size to `16`.
4. Select the text layer and press `Shift` `A` to apply auto layout.
5. Set the **Horizontal resizing** and the **Vertical resizing** to `Hug Contents`.
6. Click the  plus in the **Fill** section of the right sidebar and change the fill to `#DEB0FB`.
7. Click the  plus in the **Stroke** section of the right sidebar and configure the stroke to the following:
   - **Fill:** `#000000`
   - **Position:** `Inside`
   - **Weight:** `1`
8. Change the  **Corner radius** to `1000` px.
9. Click the  plus in the **Effects** section of the right sidebar, choose **Drop shadow** from the menu, and configure the effect to the following:
   - **X-position:** `-2`
   - **Y-position:** `4`
   - **Blur:** `0`
   - **Color:** `#000000` at `100%` opacity
10. In the **Auto layout** section of the right sidebar, change the  **Horizontal padding** to `32` and the  **Vertical padding** to `24`.
11. Select the frame and click  **Create component** in the right sidebar or use the keyboard shortcut:
    - **Mac:** `Option` `Command` `K`
    - **Windows:** `Ctrl` `Alt` `K`
12. Double-click on the frame name and rename it to `button/default/unsaved`.

Before moving on, check to make sure your button component looks similar to the following:

![](https://help.figma.com/hc/article_attachments/39712951359511)

### Add an icon instance to the button

We’re now ready to add an instance of the save icon to our button component.

1. Select the **Has fill=false** icon variant in the component set and hold the shortcut while dragging your cursor to create an instance:
   - **Mac:** `Option`
   - **Windows:** `Alt`
2. Drag the instance into the button frame, to the left of the label. Because the frame has auto layout applied, it automatically adjusts to fit the icon.
3. In the **Auto layout** section, set the **Gap** to `12`.

![](https://help.figma.com/hc/article_attachments/39712967075479)

### Apply boolean properties to the icon and label

The button is looking great! However, you may not always need both an icon and a label when reusing this component across different designs. For example, you may want to use an icon-only button when screen space is limited or when the action is universally recognized, such as a **Like** button. Instead of creating multiple button variants, we can add a boolean property to the icon and label that will allow us to toggle their visibility on or off as needed.

To apply a boolean property:

1. Select the `label` layer inside the button component.
2. In the **Appearance** section of the right sidebar, click  **Apply variable/property**.
3. Click the  plus to add a new property and configure it to the following:
   - **Create:** `Property`
   - **Name**: `Show label`
   - **Value:** `True`
4. Click **Create property**.
5. Next, click the icon layer inside the button component and repeat the process, configuring the new property to the following:
   - **Create:** `Property`
   - **Name**: `Show icon`
   - **Value:** `True`
6. Click **Create property**.

When you select the button component, you’ll now see the new boolean properties in the **Properties** section of the right sidebar.

![](https://help.figma.com/hc/article_attachments/39712951362711)

You can test out these properties by creating an instance of your button component and using the toggles to show or hide the icon and label.

![](https://help.figma.com/hc/article_attachments/39712951363479)

## Create the button variants

Now that we have our main button component, we’ll use it to create variants and build our component set.

### Configure the unsaved variants

First, we’ll add our unsaved variants:

1. Select the button component and click  **Add variant** in the right sidebar.
2. Click the purple plus below the new variant to add a third variant. You should have three buttons in total.

![](https://help.figma.com/hc/article_attachments/39712967079575)

Next, we’ll configure the default, hover, and pressed states:

1. Select the original variant at the top of the component set. In the **Current variant** section of the right sidebar, you’ll see that this variant has two properties: **Property 1** with a value of `default` and **Property 2** with a value of `unsaved`.
2. Click on **Property 1** and rename it to `state`, then click on **Property 2** and rename it to `status`.
3. Select the middle button variant. Next to the **state** property, type `hover` in the value field to add a new value. Then use the **Fill** section to change the variant’s fill to `#EFD9FF`.
4. Select the third variant. Next to the **state** property, type `pressed` in the value field. Then use the **Fill** section to change the variant’s fill to `#C48FE5`.

Before moving on, check to make sure your component set looks similar to the following:

![](https://help.figma.com/hc/article_attachments/39712951366935)

### Configure the saved variants

Our component set is coming together! Next, we’ll add the **saved** variants.

1. Click the purple plus at the bottom of your component set to add another variant.
2. With the new variant selected, type `saved` in the **status** property field.
3. Select the `icon` frame inside the button and switch the **Has fill** property to `true`.
4. Double-click on the text layer inside the new variant and type `Saved`.

![](https://help.figma.com/hc/article_attachments/39712951368087)

Now we’ll add two more variants:

1. Select the new saved variant and add two more variants.
2. Select the middle variant and change the **state** property value to `hover` and the fill to `#EFD9FF`.
3. Select the third variant and change the **state** property value to `pressed` and the fill to `#C48FE5`.

Before moving on, check to make sure your component set looks similar to the following:

![](https://help.figma.com/hc/article_attachments/39712951370135)

## Add prototype connections to your button

We’ll finish our button by adding prototype connections to make our component interactive.  If you’re new to prototyping, check out the glossary in our [Guide to prototyping](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma#h_01HHN4WWN3YDJ27498DVE6K3E1) to learn more about the terms used in this section.

#### Planning out prototype connections

Before adding prototype connections, it’s important to plan out what you want the interaction experience to be.

When recreating common UI elements (like buttons), look at how they behave in real products or design systems. Pay attention to how they look and respond to interactions, and try matching those actions with corresponding prototype triggers in Figma, such as `while hovering`, `on click`, `mouse enter`, etc.

For more complex components, consider creating a flowchart to help breakdown the interaction into more digestible steps. Figma integrates with AI tools like [Claude](https://help.figma.com/hc/en-us/articles/37883260397975-Create-FigJam-diagrams-with-Claude) and [ChatGPT](https://help.figma.com/hc/en-us/articles/35326636109975-Use-ChatGPT-with-Figma), making it easy to turn prompts into structured diagrams in FigJam.

For this button, our interactions will look like this:

- When a cursor is **hovering** over the button, we want our variant to change from the `default` state to the `hover` state
- When a cursor **presses down** on the button, we want our variant to change to the `pressed` state
- If the cursor **leaves** the button surface while pressing down, we want the variant to remain in the `default` state
- When the unsaved button is **pressed**, we want the variant to change to `saved`
- When the saved button is **pressed**, we want the variant to change to `unsaved`

[Prototyping](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma)

### Add the hover trigger

1. Switch to the **Prototype** tab in the right sidebar.
2. Hover over the `default, unsaved` variant. Then click and drag the blue plus to the `hover, unsaved` variant.
3. Configure the interaction settings to the following:
   - **Trigger:** `While hovering`
   - **Action:** `Change to`
   - **Animation:** `Smart animate`
   - **Transition:** `Ease in and out`
   - **Duration:** `150 ms`
4. Apply an identical prototype connection between the `default, saved` and `hover, saved` variants.

Your first two connections should look like this:

![](https://help.figma.com/hc/article_attachments/39712967085975)

#### **Why set the animation duration to 150 ms?**

Animations bring joy to digital interactions and can be used to communicate intended behavior. When animating your designs, make sure that it enhances the user experience without delaying people from reaching their goal. For web-specific content, it’s common practice to have animations to land in the 150-300 ms range. Animations in this range will allow users to notice the interaction but will not prevent them from moving forward in a timely manner.

### Add the mouse down trigger

1. Select the `hover, unsaved` variant, then click and drag the blue plus to the `pressed, unsaved` variant.
2. Configure the interaction settings to the following:
   - **Trigger:** `Mouse down`
   - **Action:** `Change to`
   - **Animation:** `Smart animate`
   - **Transition:** `Ease in and out`
   - **Duration:** `150 ms`
3. Apply an identical prototype connection between the `hover, saved` and `pressed, saved` variants.

Your connections should look like this:

![](https://help.figma.com/hc/article_attachments/39712951373975)

### Add the mouse leave trigger

1. Select the `pressed,unsaved` variant, then click and drag the blue plus to the `default, unsaved` variant.
2. Configure the interaction settings to the following:
   - **Trigger:** `Mouse leave`
   - **Action:** `Change to`
   - **Animation:** `Smart animate`
   - **Transition:** `Ease in and out`
   - **Duration:** `150 ms`
3. Apply an identical prototype connection between the `pressed, saved` and `default, saved` variants.

Your connections should look like this:

![](https://help.figma.com/hc/article_attachments/39712967092119)

### Add the mouse up trigger

We need to add two final connections so that the unsaved button switches to the saved button when pressed, and vice versa.

1. Select the `unsaved, pressed` variant, then click and drag the blue plus to the `default, saved` variant.
2. Configure the interaction settings to the following:
   - **Trigger:** `Mouse up`
   - **Action:** `Change to`
   - **Animation:** `Smart animate`
   - **Transition:** `Ease in and out`
   - **Duration:** `150 ms`
3. Apply an identical prototype connection between the `pressed, saved` and `default, unsaved` variants.

Your final connections should look like this:

![](https://help.figma.com/hc/article_attachments/39712967093015)

## Test your button

Awesome job! Our component set is complete and it’s time to see your button in action!

1. Use the  **Frame** tool to add a frame large enough to fit your button to the canvas.
2. Navigate to the **Assets** tab in the left sidebar and drag an instance of your button into the frame.
3. With the new frame selected, open the **Prototype view** dropdown in the right sidebar and select  **Preview** or press `Shift` `Space` to launch the inline preview.
4. Use your cursor to interact with your button.

![](https://help.figma.com/hc/article_attachments/39712967097111)

## What’s next?

Congratulations! You just created an interactive button using a component set and prototyping. If you’re looking for another challenge, check out our [Create a responsive card](https://help.figma.com/hc/en-us/articles/18894664907287-Create-a-responsive-card-with-auto-layout-and-constraints) project or the [Figma Design for beginners](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners) course for more hands-on learning opportunities.

## Check your knowledge

## Additional resource

Grab a copy of the [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830) file for hands-on practice with examples and other projects from Figma's components collection.
