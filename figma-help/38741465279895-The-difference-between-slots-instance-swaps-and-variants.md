---
기술지원명: The difference between slots, instance swaps, and variants
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: The difference between slots, instance swaps, and variants
출처링크: https://help.figma.com/hc/en-us/articles/38741465279895-The-difference-between-slots-instance-swaps-and-variants
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available in Figma Design on all plans

Anyone with can edit access to a design file can add slots to components.

New to creating slots? Learn how [slots brings flexibility to components](https://help.figma.com/hc/articles/38231200344599/).

## Slots vs instance swap

When it comes to building assets for a design system, there is a spectrum of freedom or guardrails an asset needs.

On one end of the spectrum are components that require rigidity and guardrails around how much an asset can be configured. Instance swapping is great in these situations.

For example, let’s say we have a browser tab component that is limited to one website icon at a time. The icon must stay fixed to the right of the tab text and can be swappable for another icon. Applying an instance swap property to the icon indicates to designers that this icon can be swapped and limits them to having, at most, *one* instance at a time. It also prevents designers from making layout changes to nested layers, such as dimensions and position.

On the other end of the spectrum are components that require flexibility and freeform designs that still maintain adherence to design system guidelines. Slots is a great solution for this.

For example, let’s say we use modals across various areas in our product for messaging, settings, and confirmation windows. We want various properties—like padding, border radius, and drop shadows—to remain consistent across all modals, no matter their use case. A slot provides designers with the freedom to customize the modal with the type of content they needed while allowing their modal instance to still receive library updates if changes to the main component get published.

## Slots vs variants

Both slots and variants are types of component properties that increase the number of variations and layouts that a reusable and customizable component can have.

While variants would previously be used by teams as workaround to replicate slots—especially for assets that required repeating items—the primary function of variants is to manage varying states or types of an asset.

For example, a button may have different action states—like default, hover, clicked, and disabled—so you’d create a variant for each state. In addition to action states, the button might also have varying sizes based on the device type it’s being used—like mobile and desktop.

Slots, on the other hand, are used to increase the flexibility of a base component by defining an area where you can add, edit, and rearrange content as desired.

**Tip**: If you are currently using variants as a workaround to imitate slots, learn how to [migrate to using to Figma's native slot feature](https://help.figma.com/hc/articles/38607529833751/).
