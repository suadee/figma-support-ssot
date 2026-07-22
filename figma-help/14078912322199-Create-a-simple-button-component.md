---
기술지원명: Create a simple button component
카테고리: 디자인
작성자: Figma
승인자: suadee
출처: Create a simple button component
출처링크: https://help.figma.com/hc/en-us/articles/14078912322199-Create-a-simple-button-component
게시일: 2026-07-22
검토일: 2026-07-22
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Text](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties), [auto layout](https://help.figma.com/hc/en-us/articles/5731482952599-Using-auto-layout), [color](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker), [effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers), [components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma)
- **Length**: 10 minutes

In this project, we’re going to design a stylish button component that automatically resizes based on the length of its label. Buttons are common UI elements and this project will give you hands-on experience using text, applying auto layout, and creating components that you can reuse throughout your designs.

![An animation showing the button we'll be building in this project](https://help.figma.com/hc/article_attachments/38750833440279)

## Add a text layer

We’ll begin by adding a text layer.

1. Enable the  **Text** tool from the toolbar or press `T` on your keyboard.
2. Click anywhere on the canvas and type `Button` to create a new text layer.

In the left sidebar, you’ll notice the **Layers** panel now has a new text layer called `Button`. Double-click on the layer and rename it to `Label`.

#### **Why name layers?**

Naming layers in Figma Design is an optional, but beneficial practice. Naming your layers helps you find and modify layers faster, improves collaboration, and makes it easier for agentic tools like [Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make) to read and interpret your designs.

When you add a text layer, the layer name automatically matches what you typed on the canvas until you rename it. For other object types, the default names are less descriptive. For example, each frame you add to a design file will be called “Frame 1”, “Frame 2”, and so on. Consider giving these layers descriptive names to improve your workflow and file organization.

If you’re running short on time, try using [Rename Layers](https://help.figma.com/hc/en-us/articles/24004711129879-Rename-layers-with-AI) to give your layers contextual names in just a few clicks using Figma AI.

[Rename layers](https://help.figma.com/hc/en-us/articles/360039958934-Rename-Layers)

Next, we’ll update the font family and change the font size:

1. Select the `Label` layer and use the settings in the **Typography** section of the right sidebar to change the font family to `Outfit`.
2. Change the font size to `16`.

![](https://help.figma.com/hc/article_attachments/38750833441559)

#### **How to choose a font size?**

When designing digital experiences, it’s useful to establish a foundation for your type system.

You can do this by creating a typography hierarchy that determines the scale of your fonts, from smallest to largest. Start by deciding the size of the body text font, since that’s what you’ll use most often throughout your designs. It’s good practice to set your body copy between 16px and 18px, depending on the font family you choose.

Keep in mind, it’s important to consider the context of your overall design when building your hierarchy. For example, if you were designing buttons for a car touchscreen, the font scale may need to be increased to fit buttons with larger clickable surfaces.

If you’re new to design systems, we recommend taking our [Introduction to design systems](https://help.figma.com/hc/en-us/sections/14548397990423-Introduction-to-design-systems) course for tips on building and managing a design system.

[Typography](https://help.figma.com/hc/en-us/sections/360006606853) [Introduction to design systems](https://help.figma.com/hc/en-us/articles/14552901442839-Overview-Introduction-to-design-systems)

## Apply auto layout

Our button isn’t looking too button-like yet, but we’re about to change that using auto layout!

[Auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout) helps you organize, arrange, and space out design elements so that they adjust automatically as you make changes, saving you time and making your designs responsive and adaptable.

To apply auto layout:

1. Select the `Label` layer.
2. Right-click on it and select **Add auto layout** or use the shortcut `Shift` `A`. This will add the text layer to a frame with auto layout applied.
3. In the **Auto layout** section of the right sidebar, make sure the **Horizontal resizing** and **Vertical resizing** settings are both set to **Hug contents**. Setting the resizing to **Hug contents** ensures that the button frame will automatically grow or shrink when the label changes.
4. Double-click on the new frame in the left sidebar and rename it to `Button`.

![](https://help.figma.com/hc/article_attachments/38750817443351)

**Tip:** Check out our [Figma Design for beginners](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners) course for more hands-on learning opportunities.

## Style the button

When we applied auto layout, the existing text layer was added to a frame. This allows us to add visual properties like color, strokes, and effects to give our button some style.

### Add a fill and a stroke

1. Select the `Button` frame and click the  plus in the **Fill** section of the right sidebar to add a fill.
2. Use the color picker to change the color to `#DEB0FB`.
3. Click the  plus in the **Stroke** section of the right sidebar to add a stroke.
4. Use the settings to configure the stroke:
   - **Fill:** `#000000`
   - **Position:** `Inside`
   - **Weight:** `1`

![](https://help.figma.com/hc/article_attachments/38750817444247)

### Round the corners

1. Select the `Button` frame.
2. In the right sidebar, set the  **Corner radius** to `1000` px.

![](https://help.figma.com/hc/article_attachments/38750817446423)

#### Why round button corners?

Rounded corners may seem like a small thing, but it can have a large impact on the look and feel of your final designs. Rounded corners soften the aesthetics of your design, making it feel friendlier and more approachable than objects with sharp edges.

Beyond aesthetics, it’s common for interactive elements in modern digital interfaces to have rounded corners. This means that your users are more likely to understand that they can click your button if its design matches other interfaces they use.

To full round a frame’s corners, the corner radius value must be at least half the height of the frame. For example, if our frame was `40` px high, we’d need to set the corner radius to a minimum of `20` px to achieve fully rounded corners.

You may be wondering why we set the button’s corner radius to `1000` px when a lower value would produce the same effect. Using a higher corner radius value helps future-proof components and ensures that the corners stay fully rounded, even if the height of the frame changes later.

[Corner radius](https://help.figma.com/hc/en-us/articles/360050986854)

### Apply a drop shadow

Applying drop shadows to buttons is an optional design choice, but one that can help enhance the clickable feel of a digital button.

To add a drop shadow:

1. Select the `Button` frame.
2. Click the plus in the **Effects** section of the right sidebar and choose **Drop shadow** from the dropdown menu.
3. Use the settings to configure the drop shadow:
   - **X-position:** `-2`
   - **Y-position:** `4`
   - **Blur:** `0`
   - **Color:** `#000000` at `100%` opacity

![](https://help.figma.com/hc/article_attachments/38750833452183)

### Refine the padding

When we applied auto layout, it automatically added padding between the frame’s boundary and the text layer inside. Right now, the padding is equal on all sides. Let’s update those values to create a chunkier button that will be easier to tap once we add it to our designs.

1. Select the `Button` frame.
2. In the **Auto layout** section of the right sidebar, change the  **Horizontal padding** to `32` and the  **Vertical padding** to `24`.

![](https://help.figma.com/hc/article_attachments/38750833455511)

## Test out your button

The button looks great! Best of all, because we used auto layout, the button will resize based on the length of the label inside it. Test this for yourself by double-clicking on the text layer and typing `Sign up` or `Continue`.

![](https://help.figma.com/hc/article_attachments/38750817451927)

## Turn the button into a main component

It would be a shame to only use this beautiful button once. Luckily, we can turn it into a [main component](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma) and reuse over and over again!

To create a main component:

1. Select the `Button` frame.
2. Click  **Create component** in the right sidebar or use the shortcut:
   - **Mac:** `Option` `Command` `K`
   - **Windows:** `Ctrl` `Alt` `K`

If you take a look at the left sidebar, you’ll notice the Button layer is now identifiable by the purple  component icon. Now you’ll be able to add instances of your button from the **Assets** tab in the left sidebar whenever you need! Learn more about [using components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma).

![](https://help.figma.com/hc/article_attachments/38750833461015)

## What’s next?

Congratulations! You just designed a responsive button using auto layout. If you’re looking for another challenge, check out our [Design an interactive button](https://help.figma.com/hc/en-us/articles/20953528101783-Design-an-interactive-button) project or the [Figma Design for beginners](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners) course to get more hands-on experience with auto layout and components.

## Check your knowledge

## Additional resource

Grab a copy of the [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830) file for hands-on practice with examples and other projects from Figma's components collection.
