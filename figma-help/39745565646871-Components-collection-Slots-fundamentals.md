---
기술지원명: Components collection: Slots fundamentals
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Components collection: Slots fundamentals
출처링크: https://help.figma.com/hc/en-us/articles/39745565646871-Components-collection-Slots-fundamentals
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note:** Figma Design is always improving and some visual details shown in our videos may differ from the current version. Despite visual differences, the core functionality remains unchanged.

[Slots](https://help.figma.com/hc/en-us/articles/38231200344599-Use-slots-to-build-flexible-components-in-Figma) are a type of component property that create flexible areas inside components where you can freely add and arrange content directly inside an instance without having to detach it.

## Common use cases

You can use slots for:

- **Repeating elements:** Create components that contain items with a varying number of occurrences, such as lists or forms
- **Freeform layouts:** Create components with varying layouts, such as cards or modals
- **Simplified design libraries:** Decrease the number of variants or hidden layers needed to represent the various ways an asset can look
- **Healthier design systems:** Reduce the occurrence of detached components so instances will continue receiving updates from the main component
- **Experimentation:** Allow for design experimentation while maintaining accurate component usage
- **Alignment with code:** Create components that map closer to how slots behave in code

A slot can be applied to layers nested within a main component or within variants of the same component set. You cannot bind a component property to the top-level layer of a component.

Components with slots can be published empty or with pre-populated default content inside. You can also set preferred instances for a slot, which lets you curate a set of assets to choose from when inserting content. Specifying preferred instances doesn’t limit users to only inserting those assets, but it can help reduce guesswork by communicating which components are intended for that slot.

## Work with slots in instances

Once a main component is set up with a slot, you can pull an instance of it and start adding content into the slot. A pink border will appear around a slot when you select or hover over its top level component.

Any layer type can be added to a slot. Here are some ways you can insert content into a slot:

- Drag objects from the canvas or Assets panel into the slot.
- Hover over the slot and click **Add instances**. A popup will appear with a list of components and libraries. If there are any preferred instances defined on the slot, the filter is set to **Preferred** by default.
- Duplicate layers within the slot.
- Use any tool to add layers directly into the slot.

![](https://help.figma.com/hc/article_attachments/39745594755351)

## Additional resources

Ready to continue your journey with slots? Check out these resources to learn more:

- Community playground file: [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830)
- Help Center article: [Use slots to build flexible components in Figma](https://help.figma.com/hc/en-us/articles/38231200344599-Use-slots-to-build-flexible-components-in-Figma)
- Help Center article: [The difference between slots, instance swaps, and variants](https://help.figma.com/hc/en-us/articles/38741465279895-The-difference-between-slots-instance-swaps-and-variants)
- Community playground file: [Figma slots](https://www.figma.com/community/file/1610367877471727305)
- Blog post: [How to supercharge your design system with slots](https://www.figma.com/blog/supercharge-your-design-system-with-slots/)

**Continue the conversation on the Figma forum**  
Learning is better, together! Compare notes with others working through this collection on the [Figma forum](https://forum.figma.com/ask-the-community-7/components-collection-learn-with-others-53016).
