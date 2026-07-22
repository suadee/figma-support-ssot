---
기술지원명: Use slots to build flexible components in Figma
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Use slots to build flexible components in Figma
출처링크: https://help.figma.com/hc/en-us/articles/38231200344599-Use-slots-to-build-flexible-components-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available in Figma Design on all plans

Anyone with can edit access to a design file
can add slots to components.

New to creating components? Check out our
 [guide to components](https://help.figma.com/hc/articles/360038662654)
to get started.

Slots, a type of component property, are flexible areas placed inside main components that let you freely add, resize, and arrange content within an instance without having to detach it. Slots can be published to libraries and help maintain adherence to your team's design system.

You can also set preferred instances to guide designers on what assets are recommended for use within the slot, and set minimum or maximum number of layers that can be added to a slot.

**Migrate a library to use slots**

If you or your team have been using workarounds to 'recreate' slots and are ready to migrate to using Figma Design’s native slots feature, head over to our article on [migrating a library to use slots](https://help.figma.com/hc/articles/38607529833751/) where we cover the most common past workarounds and provide recommended migration workflows for each one.

## Common use cases

Use slots for:

- [**Repeating elements**](#h_01KJTQ4AFV1G7JADAGTK793133): Components that contain repeating items like task lists or tabs
- [**Freeform layouts**](#h_01KJTQ4AFWSV5K6JQWWNMMWPGY): Components such as cards or modals with varying layouts
- **Simplified and cleaner libraries**: Decrease the number of variants or hidden layers needed to represent the various ways an asset can look
- **Experimentation**: Allow for experimentation while maintaining adherence to accurate component usage
- **Healthier design systems**: Reduce occurrences of detached components so instances will continue receiving updates from the main component
- **Code**: Map closer to how slots behave in code, namely React

### Repeating elements

Components containing repeating elements—such as task lists, input fields on a form, and music playlists—might not have a fixed number of occurrences. When you create a component with slots, you can add as many repeating items as you need without detaching the instance from its main component.

![slots_bento-repeating-items.png](https://help.figma.com/hc/article_attachments/38801047970711)

### Freeform layouts

Certain base components have numerous permutations of what it can look like—such as modals and cards. They require flexibility in how a layout is arranged and in the types of content it contains. With slots, you can resize and rearrange items as needed and insert layers of all types—like instances, text, images, to name a few.

![slots_bento-freeform.png](https://help.figma.com/hc/article_attachments/38801047974039)

## Create a slot in a main component

Slot can be used on nested layers in main components or in variants of the same component set. You convert a frame to a slot, wrap layers in a slot, or apply an existing slot property to a frame.

You cannot bind a slot property to the top level layer of a component.

**Use slots on variants**: You can apply a slot property across variants within the same component set. To do this, use [multi-edit](https://help.figma.com/hc/en-us/articles/21635177948567-Edit-objects-on-the-canvas-in-bulk) to select multiple similar layers, then create and add the slot property to layers in bulk.

There are several ways to add slots to main components.

#### **Convert a frame to a slot**

Any frame in a main component can be converted to a slot. This is handy for when you’ve already pre-defined the area you wish to be a slot with a frame.

1. Select a nested frame inside a main component.
2. Choose from the following options:
   - Right-click and select **Convert to slot**.
   - Use the keyboard shortcut `⌘ Command` `⇧ Shift``S` (Mac) or `⌃ Control` `⇧ Shift``S` (Windows).
   - From the right sidebar, click **Convert to slot**. Select an existing slot property from the dropdown or choose to create a new one.

The frame will be converted to a slot, and a new slot component property will be created. From the **Properties** section of the right sidebar, click  **Edit slot property** to update the slot name, add a description, and set preferred instances. Learn more about [editing a slot property](#h_01KSTSXRZ36Q2XC542CNAMZFQT).

![slots-convert-frame.gif](https://help.figma.com/hc/article_attachments/38810869666071)

#### **Wrap objects in a new slot**

If you’re working with objects that are not frames—such as text layers, groups, instance components, or a selection of multiple objects—you can wrap them in a new slot.

1. From any main component, select a non-frame object or multiple layers.
2. Right-click, and select **Wrap in new slot**.

This will create a new slot and place your selection into it, and a new slot property will be created. From the **Properties** section of the right sidebar, click  **Edit slot property** to update the slot name, add a description, and set preferred instances. Learn more about [editing a slot property](#h_01KSTSXRZ36Q2XC542CNAMZFQT).

![slots-wrap-in-slot.gif](https://help.figma.com/hc/article_attachments/38810902787735)

#### **Create a slot property, then apply it to a layer**

You can also create a slot property from the right sidebar.

1. Select a main component on the canvas.
2. Click  **Create property** and choose **Slot** from the right sidebar.
3. A settings modal will appear, where you can update the slot name, add documentation, and edit other [slot settings](#h_01KSTSXRZ36Q2XC542CNAMZFQT).
4. This will create a slot property, but it will not define a slot area on your layers until you assign it to a frame. When you are ready to assign this slot property to a frame, select the frame click  **Convert to slot** in the right sidebar, then select the existing slot property from the dropdown.

![create-and-apply-slot.gif](https://help.figma.com/hc/article_attachments/40882337689623)

## Edit slot settings

You can leave a slot empty or add layers to it as default content. A slot can take on most of the same properties as a frame. For example, you can apply horizontal and vertical auto layout, minimum and maximum dimensions, color fills, effects, and variables, to name a few.

Components with slots can be published empty or with pre-populated, default content inside.

To adjust the settings and default options on a slot, select the main component and find the slot in the right panel. Then, hover over the slot property and click  **Edit property**. From there you can:

1. Update the slot property’s name and description
2. [Set minimum and maximum layer counts](#h_01KSTT2ED0HZB19R9SH2HZFJ0D)
3. [Set preferred instances](#h_01KSTT2ED2AACSMW5JF22W4GSH)
4. [Only allow preferred instances](#h_01KSTT2ED34KW3P115JCEC05B0)
5. [Display empty slots by default](#h_01KSTT2ED34QMA9JXKA76SEA53)
6. [Set items to fill container by default](#h_01KSTT4CJFGM6NG6SG7M94G9Y4)

![edit-slot-property-settings.png](https://help.figma.com/hc/article_attachments/40882337693719)

### Set minimum and maximum layer counts

There is no limit to the number of layers that can be added to a slot. However, there are cases where you may wish to guide your team to keep within a range of number of layers in a slot.

For example, consider an avatar group component that shows who’s active in a file. When the number of avatars exceeds five, the circles begin to crowd one another. Setting a maximum layer count of five on the avatar slot communicates this guidance to designers directly in the file, without needing them to check external documentation.

A minimum layer count can be useful on components used in workflows that require choice, like a radio group. Since a single radio button doesn’t allow users to make a selection, setting a minimum of two layers communicates the intended usage.

To set a limit on layer count on a slot, use the **Minimum layers** and **Maximum layers** fields to define it. You can use both fields to define a range, or use just one of the fields.

Once a limit is defined, anyone using an instance of the slot can see the limits from the right sidebar when the slot or its component. They can click the **Limits** label to view details about the limits and whether they’ve been met.

**Note**: Layer count limits are designed to guide your team, not restrict them. If a designer goes past a limit, a warning will appear at the bottom of the screen and the limit label will turn orange as a friendly nudge to keep designs on track, but they can continue working beyond the set limit.

[Learn how limits appear when consuming a slot.](#h_01KSTT9WFM6KBWFCH20C368KGN)

### Set preferred instances

Create a curated list of components for your team to choose from by setting preferred instances on a slot. This is an optional step that you can take to reduce guesswork by guiding designers toward recommended or commonly used components.

To set preferred instances on a slot, click  **Select preferred instances**. Check the boxes next to the instances you want to include.

### Only allow preferred instances

The **Only allow preferred instances** setting informs designers to add only instances from the preferred instances list.

For example, you may want to only allow use of preferred instances for an empty-state illustration slot where designers choose from a list of curated and approved illustrations.

Or, consider an input form component that must be compositional. It should be able to handle varying combinations of input types, and designers should be able to rearrange and reorder content. However, we want designers to know to use only certain assets for the form component—like text inputs, dropdowns, text areas, date pickers, and so on. So, we enable this setting.

[Learn how limits appear when consuming a slot.](#h_01KSTT9WFM6KBWFCH20C368KGN)

### Display empty slots by default

When you hover over a component containing a slot, the slot layer will be indicated by a pink box.

If you wish for the slot indicator to be persistent, you can do so for any empty slots by checking **By default, display empty slots** from the main component.

![default show empty slots.gif](https://help.figma.com/hc/article_attachments/40882337694999)

### Set items to fill container by default

When you toggle on **By default, fill items on slot’s counter-axis** on a slot, any items added to the slot will have **Fill container** applied to the resizing setting on the axis opposite of the slot’s flow direction.

For example, if a slot’s auto layout flow is set to **Vertical** (where layers run along the y-axis), then any objects added to that slot will be set to fill container on the x-axis. In other words, the slot will stretch their width to fill the available space.

Similarly, if a slot is set to **Horizontal** auto layout flow, then inserted objects will be set to fill container on the y-axis and stretch their height to fill the available space.

![before-and-after_slots-fill-container-counter-axis.gif](https://help.figma.com/hc/article_attachments/40882337695895)

## Work with slots in instances

Once a main component is set up with a slot, you can pull an instance of it and start adding content, rearranging layers, and removing objects from the slot as if the slot was a regular frame. You can clear a slot of all layers to start from scratch or reset overrides to go back to the slot’s default content.

### Add content

Any layer type can be added to a slot. Here are some ways you can insert content into a slot within a component instance:

- Use any tool to add layers directly into the slot.
- Duplicate layers within the slot.
- Drag objects from the canvas or **Assets** panel into the slot.
- From the canvas, hover over the slot and click **Add instances** from the canvas. Or, select the slot and hover over the slot property name in the right sidebar, then click  **Add instances**. A popup will appear with a list of components and libraries. If there are any preferred instances defined on the slot, the filter will be set to preferred by default.

![slots-add-content.gif](https://help.figma.com/hc/article_attachments/38812937072535)

### Apply changes

While you can make changes to content living within a slot of a component instance, there are some changes that can and cannot be made to the slot layer itself.

Visual properties like fill, stroke, opacity, and effects can be added or edited on the slot layer. You can also edit the layer name and manage its export settings.

However, it’s not possible to make changes to the underlying structure of an instance. Changes cannot be made to a slot’s position, auto layout flow, and constraints. These need to be updated from the main component.

### View limits

If there are any limits set on the slot—such as using only preferred instances, minimum layer count, or maximum layer count—they will be displayed in the right sidebar when the slot or its parent instance component is selected. Click on the label to view details about the slot’s limits.

A green checkmark will be displayed next to limit guidelines that have been met successfully, and an orange warning icon next to limits that have not been met. If the preferred instances only setting is enabled, you can click the **View layers** button to see them on the canvas.

![view-slot-limits.png](https://help.figma.com/hc/article_attachments/40882337697303)

**Note**: Layer count limits are designed to guide rather than restrict. If you go past a limit, a warning will appear at the bottom of the screen and the limit label will turn orange as a friendly nudge to keep designs on track, but you can continue working beyond the set limit.

### Reset a slot

When overrides have been made to a slot, its respective slot property will get a [Modified] tag in the properties panel.

To reset a slot and revert it back to how the slot looks in the main component:

1. Select the slot layer.
2. Click  **More actions** and choose  **Reset slot**.

You can also select the component instance in which the slot lives, click **More actions** > **Reset specific changes** > **Reset <slot name> property**.

### Clear a slot

Clearing a slot will remove all layers within the slot so that you can start fresh.

1. Select the slot layer.
2. Click  **More actions** and choose  **Delete contents**.

## Remove a slot

**Warning**: Removing a slot property from a main component is a destructive action. If an instance has been modified using slots and the slot property is removed from the main component, that instance’s slot area will be reset to its default state. For example, if you add layers to a slot in an instance, and then removed the slot from the main component, those added layers would be automatically removed from the instance.

We recommend testing slot removal in a separate branch before approving and publishing changes.

There are a couple of ways to remove a slot from a main component:

- To remove the slot property, select the main component and click  **Delete property** next to the slot property name. The slot frame and its contents will be retained.
- To remove the frame but keep the slot property and its contents, use the keyboard shortcut `⌘ Command` `⇧ Shift` `G` (MacOS) or `Ctrl` `⇧ Shift` `G` (Windows).

## Considerations

### Using component properties in slots

Component properties cannot be applied to layers from inside a slot.

However, you can apply component properties to main components, and then insert an instance into a slot. The component properties applied to it will persist and remain available.

For example, say we have a slot within a main component, and we want to add a frame and a text layer to the slot. We won’t be able to apply component properties to that frame and text layer.

![component-props-slots-error.png](https://help.figma.com/hc/article_attachments/40882337699479)

Similarly, if you grab a layer containing a component property from a main component and move it to a slot in a different main component, the component property will be removed.![component-props-in-slots.gif](https://help.figma.com/hc/article_attachments/40882315272471)

To maintain flexibility for layers in a slot of a main component, you can explore binding variables instead. Depending on your setup, it may also help to keep component property bindings outside the slot boundary. By binding variables to variants and colors, you can achieve the intended effect by changing modes rather than variant swapping.

Learn how to bind variables to variant instances from [this help center article](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables#h_01HMCXW0AWV7FCAVTBTXWNMXMM) and [this video](https://www.youtube.com/watch?v=6Z3EfejbCuY).

### Handoff to developers

Map structured content from a Figma component directly into your code examples using Code Connect. This makes it possible to represent flexible child content such as text, layers, or nested components, inside your code snippets.

[Learn more about Code Connect.](https://developers.figma.com/docs/code-connect/)

**Note**: MCP support is coming soon.

## Resources

Ready to continue your journey with slots? Check out these resources to learn more:

- Learn how to [migrate an existing library to use slots](https://help.figma.com/hc/articles/38607529833751/)
- Understand [the difference between slots, instance swap, and variants](https://help.figma.com/hc/articles/38741465279895)
- Get hands-on practice with the [Slots playground file](https://www.figma.com/community/file/1610367877471727305)
- See slots in action in this 4-minute [Slots video tutorial](https://www.youtube.com/embed/UjOVRUSdO14?si=AnLVrK_vOxPwFSXi)
- Read Figma's blogpost on [how to supercharge your design system with slots](https://www.figma.com/blog/supercharge-your-design-system-with-slots/)
