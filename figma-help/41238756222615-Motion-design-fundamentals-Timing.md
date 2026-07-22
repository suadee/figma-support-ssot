---
기술지원명: Motion design fundamentals: Timing
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Timing
출처링크: https://help.figma.com/hc/en-us/articles/41238756222615-Motion-design-fundamentals-Timing
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Timing is one of the most consequential decisions in motion design and one of the easiest to get wrong. Too short, and an animation become imperceptible. Too long, and an animation become an obstacle. Good timing is almost invisible. It gives users just enough time to register what happened without making them wait for it.

Timing is made up of two closely related concepts: duration and speed. Duration is how long an animation lasts. Speed is how fast an object moves within that duration.

![An animation demoing how different durtations can impact animations.](https://help.figma.com/hc/article_attachments/41238740687511)

The right timing means users notice the motion without waiting for it to finish.

## Choosing the right duration

Duration is the length of an animation, measured in milliseconds. It’s the most direct way timing is expressed in design tools and code, and it’s usually the first value you set when building an animation.

The right duration depends on several factors working together: the size and visual weight of the object, the distance it travels, the easing curve it uses, and the overall pace and tone of the product.

When setting the duration for your animation, consider:

- **Larger objects need more time**: A full-screen transition requires more time to feel natural than a small notification appearing at the top of the screen. Large movements that happen too fast are hard to follow and feel jarring.
- **Functional animations should be quicker than expressive ones:** A loading state should be quick and unobtrusive. An onboarding illustration animating into place can take a little more time. The more attention an animation demands, the more duration it can justify.
- **Duration and easing work together:** The duration you set should match the character of the curve. Applying a long duration to a steep easing curve will make the animation feel sluggish.

![](https://help.figma.com/hc/article_attachments/41238740688151)

## Choosing the right speed

Speed is how fast an object moves within its duration. Two objects can share the same duration but feel completely unique if they're traveling different distances or carrying different visual weight.

Speed is closely tied to the perceived weight of an object. Heavier, more prominent objects feel more natural moving at a slower speed. Their visual mass suggests that they take more effort to start and stop. Lighter, smaller objects can move more quickly because their low visual weight suggests they respond easily to force.

It may be tempting to make all functional animations as fast as possible to minimize friction, but motion that moves too fast can be just as disorienting as motion that moves too slow. Users need enough time to register a transition. If an animation moves too fast, they may lose their spatial context entirely.
