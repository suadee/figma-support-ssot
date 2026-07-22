---
기술지원명: Components collection: Component property fundamentals
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Components collection: Component property fundamentals
출처링크: https://help.figma.com/hc/en-us/articles/39636407507735-Components-collection-Component-property-fundamentals
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note:** Figma Design is always improving and some visual details shown in our videos may differ from the current version. Despite visual differences, the core functionality remains unchanged.

[Component properties](https://help.figma.com/hc/en-us/articles/39636407507735-Components-collection-Component-property-fundamentals) define which aspects of a component are intended to be customized. Rather than hunting through the Layers panel or clicking into instances on the canvas, users can access consolidated controls in the right sidebar that clearly indicate what’s meant to change and what isn’t.

Keep in mind, component properties don’t restrict access to other layers. They simply guide users by making the right controls easier to find.

![](https://help.figma.com/hc/article_attachments/39636453832471)

## Types of component properties

There are five different types of component properties:

- **Boolean properties:** Control which layers can be shown or hidden
- **Instance swap properties:** Define which nested instances can be replaced with preferred alternatives
- **Text properties:** Indicate which text content can be changed
- **Slot properties:** Create a flexible area where content can be freely added, edited, and rearranged
- **Variant properties:** Control how variants are organized within component sets

**Note:** We won’t be covering variant properties in this article, as they function a bit differently than other component properties. To learn more, check out the [Variant and component set fundamentals](https://help.figma.com/hc/en-us/articles/39636737843735) article.

### Boolean property

Boolean properties use true/false values to control layer visibility within instances, where `true` shows the layer and `false` hides it.

Boolean properties can make your components more modular. For example, imagine designing a card component that includes optional elements like an icon, status indicator, or button. Without boolean properties, you’d need separate components for every possible combination of optional elements, which could quickly become unmanageable as options multiply. Instead, you can use boolean properties to create a flexible component where users can toggle optional elements on or off as needed, directly from the right sidebar.

![](https://help.figma.com/hc/article_attachments/39636407504663)

### Instance swap property

Instance swap properties let you indicate which nested instances can be replaced and curate a list of suitable alternatives. For example, when designing a list item that includes an icon, you can apply an instance swap property to the icon and specify preferred icon alternatives. Users can then change icons directly from the right sidebar without clicking into the instance on the canvas.

![](https://help.figma.com/hc/article_attachments/39636407505943)

### Text property

Text properties let you specify which text layers can be edited and give users a direct way to update content from the right sidebar.

Text properties help eliminate confusion about which text layers are meant to be edited, and which should stay fixed. For example, in a toast notification, you might keep the heading fixed (such as “Success” or “Error”) while allowing the message text to be customized for different situations.

![](https://help.figma.com/hc/article_attachments/39636453834903)

### Slot property

Slots are flexible areas added to components that let you freely add and arrange content directly inside an instance without having to detach it, all while maintaining adherence to your design system.

For example, you may want to use slots for repeating elements that don’t have a fixed number of occurrences, such as lists or forms, or to create flexible content containers inside elements with varying layouts, such as cards or modals. We take a deeper dive into slots in the [Slots fundamentals](https://help.figma.com/hc/en-us/articles/39745565646871%20) article.

![](https://help.figma.com/hc/article_attachments/39636453835927)

## Check your knowledge

## Additional resources

Learn more about component properties with these additional resources:

- Community playground file: [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830)
- Help Center article: [Explore component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties)
- Community playground file: [Component properties](https://www.figma.com/community/file/1100581138025393004/component-properties-playground?q_id=00c1c1dd-010a-4582-83f3-282604623545)

**Continue the conversation on the Figma forum**  
Learning is better, together! Compare notes with others working through this collection on the [Figma forum](https://forum.figma.com/ask-the-community-7/components-collection-learn-with-others-53016).
