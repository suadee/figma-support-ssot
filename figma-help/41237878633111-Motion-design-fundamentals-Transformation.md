---
기술지원명: Motion design fundamentals: Transformation
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Transformation
출처링크: https://help.figma.com/hc/en-us/articles/41237878633111-Motion-design-fundamentals-Transformation
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Transformation describes how an object changes its visual properties over the course of an animation. While easing, timing, and sequencing govern when and how objects move through time, transformation governs how an object’s properties shift from one state to another.

Every animation includes at least one transformation. An object might move across the screen, scale up as it enters, fade in from transparent, or rotate into position. The combination of transformations applied to an object determines its overall visual character.

![An animation demoing different ways a objects can transform.](https://help.figma.com/hc/article_attachments/41237878629911)

## Choosing the right transformation

Every transformation tells a story about where an object came from and where it’s going. A new screen entering as part of an onboarding sequence should move in the direction the flow is going. A notification should drop in from the top of the screen. An overlay that doesn't enter from a specific direction should fade into view. When the transformation matches the spatial context, the motion feels inevitable. When it doesn’t, the motion feels strange.

![An animation that demos how an element entering from the wrong direction can make the motion feel strange.](https://help.figma.com/hc/article_attachments/41237878630679)

*When elements enter from different directions, the motion loses its sense of direction. The example on the right shows how quickly an inconsistent transition can make an interface feel off.*

Most animations combine more than one transformation, and that’s where the object’s story comes together or falls apart. A confirmation screen that slides up and fades in simultaneously feels grounded because both properties support the same story. Compound transformations create richer motion than a single transformation alone, but only when every property change pulls in the same direction.

The most common mistake is adding a transformation that doesn’t contribute to the narrative. A bottom sheet rising into view while rotating creates a contradiction. The two transformations pull against each other, and the motion feels confused. Every property in a compound transformation should earn its place. If you can't articulate what a transformation contributes to the story, consider removing it.
