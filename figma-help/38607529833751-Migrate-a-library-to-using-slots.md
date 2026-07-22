---
기술지원명: Migrate a library to using slots
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Migrate a library to using slots
출처링크: https://help.figma.com/hc/en-us/articles/38607529833751-Migrate-a-library-to-using-slots
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available in Figma Design on all plans

Anyone with can edit access to a design file
can add slots to components.

New to creating slots? Learn how
[slots brings flexibility to components](https://help.figma.com/hc/articles/38231200344599/).

This guide is for design system teams and maintainers who have previously set up placeholder slots in their components.

Your team may have been using workarounds like:

- Creating placeholder frames labeled `Content`, `Swap or replace me` or `Insert here`
- Exposing nested instances through instance swap properties

These patterns worked as temporary solutions but are difficult to scale and maintain.

**Slots** in Figma replaces all of these patterns with a simpler, native way to define where content can go. In this article, we’ll cover:

- How to migrate placeholder slots to using Figma’s native slots feature.
- Different migration paths, and the pros and cons of each approach

## Step 1: Audit your library for placeholder slots

Begin your migration by reviewing your library to find components that use placeholder slots.

Look for components that:

- Are main components labeled ‘Slot’ that have been reused across multiple components
- Contain layers or instances named ‘Slot’ or something similar
- Include frames used as placeholders for content, especially if it has an instance swap property applied

**Tip**: Use `⌘ Command` `F` (Mac) or `⌃ Control` `F` (Windows) to search for the word “Slot” in your file. This is a quick way to surface all components, frames, or instances that might be acting as placeholder slots.

## Step 2: Choose a migration path

There are a few ways to migrate to using Figma’s slots feature, but the right path will depend on *how* your components are structured. Each option will have different trade-offs in level of effort it requires and the impact on existing components.

The following workflows are two of the most common migration paths. Keep in mind you may find a process that works best for your team beyond what has been listed on this page.

## Migration path 1: If using a ‘slot placeholder’ component across multiple components

![migrate-slots-placeholder.png](https://help.figma.com/hc/article_attachments/38827139829015)

**Does your set up look something like this?** You’ve created a dedicated main component called “Slot” or something similar that contains a placeholder inside. You then nest instances of this ‘Slot’ component inside other main components, along with instructions for designers to swap it with a local component using the instance swapper.

In practice, it looks something like this:

- The ‘slot’ is built as its own main component and acts as a reusable placeholder
- Other components include the ‘slot’ it as a nested instance to indicate the area where content can go
- Designers replace the placeholder by manually swapping the nested instance
- If there is no instance swap property configured, swapping happens by using local components

### Recommendation

If you’re using a ‘slot placeholder’ component across multiple parent components, we recommend replacing those placeholder instances with native slots inside each parent component. Rather than maintaining a central slot placeholder, each parent component should now have its own frame with a slot property assigned.

#### **Pros**

- Aligns with how native slots are designed to work (each component owns its own slot)
- Frees you from dependency on a shared placeholder component
- Easier to manage visual styles and behaviors per component

#### **Cons**

- Requires editing multiple main components
- If designers have customized instances of the ‘slot placeholder’, the overrides on the parent component won’t carry over
- Requires communicating with your team that the shared ‘slot placeholder' component is deprecated and will no longer update

### How to migrate

1. Open each parent component that includes a nested instance of the ‘slot placeholder.’
2. Select the ‘slot placeholder’ instance, then either detach the instance if you wish to keep its properties and contents, or delete it.
   - If you deleted the ‘slot placeholder’ instance, insert a new frame in its place and adjust it to match the original slot placeholder’s layout and size.
3. Right-click the frame and select **Convert to Slot.**
4. Edit the slot’s name, description, and optionally define the preferred values.
5. Repeat this process for other components that previously nested the shared ‘slot placeholder’.
6. Test with different component insertions to ensure layout, constraints, and resizing work as expected.
7. Once all main components have their own slots, deprecate the old shared ‘slot placeholder' by placing it in a different page or section, and hiding it from publishing.
8. Publish the updates to your team library.

## Migration path 2: If using a variant-based slot placeholder

![migrate-slots-variant.png](https://help.figma.com/hc/article_attachments/38827150599447)

**Does your set up look something like this?** You have a component set called “Building Block/Content,” or something similar, and it contains at least two variants—one variant with existing content and one “slot” variant. The slot variant may contain a visual placeholder along with instructional text.

This component set also contains an **instance swap property** called something like “Slot swap” where the **value** is set to the “slot” variant. This lets authors “swap in” that slot variant wherever they need a freeform container.

In other main components—such as in cards, modals, and lists—an instance of the “Building Block/Content” component is added. This exposes the “Slot swap” instance swap property, which allows designers to swap the “slot” variant with other instances.

Structurally:

- The **component set** acts as a “slot container”
- The **slot variant** acts as a placeholder visual for guidance.
- The **instance swap property** controls which variant is shown.

### **Recommendation**

If you’re using variants and the instance swap property, this pattern cannot be converted directly because the instance swap property and variant logic will disappear once you convert the area into a a slot. We recommend that you rebuild the asset using Figma’s native slots feature.

#### **Pros**

- Uses native slots: no hacks or property bindings needed
- Designers can insert any content, not just predefined components
- Preferred values give you the same ‘guided’ swapping experience but cleaner
- No more variants needed

#### **Cons**

- This is effectively a rebuild
- Variant driven placeholder logic is lost
- Existing Slot swap bindings will break, so instances won’t auto update
- Needs careful documentation for downstream teams during transition

### How to migrate

1. Open each parent component that uses an instance from the “builder” component set.
2. Remove the nested instance of the builder from the parent component.
3. Insert a new frame in its place and adjust it to match the original slot placeholder’s layout and size.
4. Right-click the frame and select **Convert to Slot.**
5. Edit the slot’s name, description, and optionally define the preferred values.
6. Test with different component insertions to ensure layout, constraints, and resizing hold up.
7. Deprecate the old builder component set by placing it in a different page or section, and hiding it from publishing, and update documentation.
8. Publish a new version of the component.
