---
기술지원명: Motion design fundamentals: Sequencing
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Sequencing
출처링크: https://help.figma.com/hc/en-us/articles/41239278373271-Motion-design-fundamentals-Sequencing
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Motion rarely happens in isolation. Most animations are part of a larger sequence, such as a group of objects entering the screen together, a multi-step transition, or a choreographed content reveal. Sequencing is how you control the timing and relationships between those animations to create motion that feels coherent rather than chaotic.

![](https://help.figma.com/hc/article_attachments/41239262523799)

## How delay creates rhythm

Delay adds a pause before an animation begins. It’s a useful tool for creating rhythm in a sequence.

When incorporating delays, it’s important that they feel like intentional pauses, not unexpected lag. If a delay is noticeable, it should be there for a clear reason. Reserve delays for objects that follow the first object in a sequence. For example, if a screen transition brings in a hero image followed by supporting content, the hero should animate first without delay. Delaying the primary object in a sequence can make the UI feel unresponsive rather than choreographed.

![](https://help.figma.com/hc/article_attachments/41239262524055)

## How offset distributes motion

Offset is what turns a group of animations into a deliberate sequence. Even a small offset between objects can create a sense of order and intentionality that simultaneous motion can’t achieve.

There isn’t a single correct offset value. The right offset depends on how long each individual animation lasts, how many objects are in the sequence, and the pace and tone of your product. As a general rule, offsets between objects should be significantly shorter than the duration of each animation. When offset and duration are close in value, the sequence starts to feel like a slow march rather than a clean ripple.

![](https://help.figma.com/hc/article_attachments/41239278372247)

In longer sequences, scale offsets to the number of objects in a sequence. Small offsets compound quickly across many objects. A 50ms offset across 10 objects means the last object doesn’t start animating until 450ms after the first, which may make your animation feel drawn out.

## How overlap unifies a sequence

When the offset between objects is shorter than the duration of the animation, objects will naturally overlap. Overlapping animations are important for creating flow and continuity. A sequence where each object waits for the previous one to finish before starting feels mechanical. Let your animations run concurrently and adjust the offset until the sequence feels like a single, unified motion rather than a series of individual animations.

The degree of overlap is controlled by the relationship between duration and offset. A small offset relative to the duration produces significant overlap and a fluid, fast-moving sequence. A larger offset produces less overlap and a more measured, deliberate pace. The right balance depends on the size and complexity of the objects, the length of the sequence, and the overall tone of the product.
