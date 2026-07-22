---
기술지원명: Components collection: Nesting instances fundamentals
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Components collection: Nesting instances fundamentals
출처링크: https://help.figma.com/hc/en-us/articles/39723486706455-Components-collection-Nesting-instances-fundamentals
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Nest an instance into a component

Because components are often reused across different contexts, you may find yourself wanting to use components within other components—also called nested instances. Learn more about [relationships of nested layers](https://help.figma.com/hc/en-us/articles/360039959014-Parent-child-and-sibling-relationships).

For example, take this card design that allows users to log and track a habit. It includes text layers for the habit name, progress details, and notification time, an icon to visually represent the habit, and an icon button to log sessions.

![log-habit-card.png](https://help.figma.com/hc/article_attachments/39737812924567)

These icons *could* be inserted into the main card component as regular layers, but that would make it hard to swap out icons to fit various contexts. And what if the company goes through a branding update that impacts their icon library? Locating and updating every icon would be a tedious endeavor.

Building complex components with nested instances is a great way to maintain consistency and make design system management more sustainable. When changes need to happen, such as updating an icon, you can simply modify the icon component and that update will become available for every nested instance throughout your designs, eliminating the need for manual updates and reducing the risk of design inconsistencies.

## Swap an instance

Another situation you might find yourself in needing to swap one of the icons out for another icon to better suit the context of the card.

There are a couple ways to go about building the card components to be able to switch between icons.

**Without instance swap**: Limit icon choices to a predefined set where each icon is tied to specific use cases or meanings. In this case, you would create multiple card components, each with a different icon.

**With** [**instance swap**](https://help.figma.com/hc/en-us/articles/360039150413): Provide flexibility to component consumers to choose icons based on context, or when working with a larger set of icons. In this case, you’d create a base card component, and turn each icon into a component.

![without-instance-swap-vs-with-instance-swap.png](https://help.figma.com/hc/article_attachments/39737812925975)

## Check your knowledge

**Exercise**: If you were working on the main component shown in the image below, which elements would you turn into nested instances?

Hint: Think about which parts of this component will need to be reused and stay consistent across designs.

![drink-water-component.png](https://help.figma.com/hc/article_attachments/39737790687511)

Answer

![nested-instances-exercise-answer.png](https://help.figma.com/hc/article_attachments/39738648123287)

- OS status bar
- Header buttons
- Icon buttons
- Heading and subheading

**Note**: The answer above is not definitive, and is just one possibility of which nested layers can be instances. In practice, the layers that you turn into components will depend on the structure of your [design system](https://help.figma.com/hc/en-us/sections/14548397990423-Introduction-to-design-systems) and usage needs of your team.

## Additional resource

Learn more about nested instances and instance swapping with this additional resource:

- Community playground file: [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830)

**Continue the conversation on the Figma forum**  
Learning is better, together! Compare notes with others working through this collection on the [Figma forum](https://forum.figma.com/ask-the-community-7/components-collection-learn-with-others-53016).
