---
기술지원명: Components collection: Variants and component set fundamentals
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Components collection: Variants and component set fundamentals
출처링크: https://help.figma.com/hc/en-us/articles/39636737843735-Components-collection-Variants-and-component-set-fundamentals
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note:** Figma Design is always improving and some visual details shown in our videos may differ from the current version. Despite visual differences, the core functionality remains unchanged.

As you build your design system, you’ll likely need components that serve the same purpose but vary in appearance. For example, you might need multiple button components with different types, sizes, and interactive states. You could create individual components for each variation, but that would quickly result in a messy and overwhelming design library.

![An animation demonstrating how messy a design library can get without variants](https://help.figma.com/hc/article_attachments/39636737839127)

## Build component sets with variants

This is where variants come in. A variant is a specific version of a component that differs from other versions in predictable ways. When you create a variant, Figma automatically organizes it into a structured container called a component set, identified by a dashed purple border on the canvas.

![](https://help.figma.com/hc/article_attachments/39636706940055)

Component sets use **variant properties** to define how variants differ from each other. You can add and customize as many properties as you need. You can even map properties and values to code components in your design system to help with the development handoff.

We recommend using individual properties to control specific, named differences, rather than one property to control multiple changes. For example, instead of creating a single “Style” property with values like “Primary Large, Secondary Small”, create separate “Type” (Primary, Secondary) and “Size” (Small, Large) properties. This approach gives users more flexibility to mix and match variations and will make your design assets easier to navigate.

![](https://help.figma.com/hc/article_attachments/39636706943255)

Component sets become increasingly valuable as your design system grows. They transform scattered components into organized, navigable systems that help you and your team quickly find and use the right components, reducing errors and maintaining design system integrity across projects.

## Check your knowledge

## Additional resources

Learn more about variants with these additional resources:

- Community playground file: [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830)
- Help Center article: [Create and use variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants)
- Help Center article: [The difference between slots, instance swaps, and variants](https://help.figma.com/hc/en-us/articles/38741465279895-The-difference-between-slots-instance-swaps-and-variants)
- Community playground file: [Variants](https://www.figma.com/community/file/903303571898472063/figma-variants-playground?q_id=087aeeca-03cc-49d7-81b5-f6a986829eda)

**Continue the conversation on the Figma forum**  
Learning is better, together! Compare notes with others working through this collection on the [Figma forum](https://forum.figma.com/ask-the-community-7/components-collection-learn-with-others-53016).
