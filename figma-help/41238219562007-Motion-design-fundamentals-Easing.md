---
기술지원명: Motion design fundamentals: Easing
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Motion design fundamentals: Easing
출처링크: https://help.figma.com/hc/en-us/articles/41238219562007-Motion-design-fundamentals-Easing
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Easing is what makes motion feel organic and real. In nature, nothing moves at a perfectly uniform speed due to friction, gravity, or air resistance. Objects gain momentum as they start moving and lose it as they come to a stop.

Easing replicates that physical logic by controlling whether an object accelerates or decelerates during an animation. Without easing, motion feels robotic and mechanical.

![An animation demoing the difference between linear motion and motion with easing](https://help.figma.com/hc/article_attachments/41238243370647)

Linear motion gets the job done, but easing makes the interaction feel human.

## How easing works

Every easing curve is built on a relationship between acceleration and deceleration.

**Ease in:** Creates an animation that starts slowly and accelerates toward the end. The object builds speed as it moves, committing more forcefully as it reaches the end of its duration. This feels natural for objects that are leaving the screen. The slow start gives the eye a moment to register the departure, and the fast exit feels decisive.

**Ease out:** Creates an animation that starts fast and decelerates toward the end. The object arrives quickly and settles into place. This feels natural for objects entering the screen. The fast start gets the object into position, and the gentle deceleration makes it feel like it’s landing rather than stopping abruptly.

**Ease in and out:** Creates an animation that starts slowly, accelerates in the middle, and slows as it reaches the end. Both the departure and arrival are cushioned, which makes it great for objects moving from one position to another within the screen. Since the object stays visible throughout, both ends of the motion need to feel smooth.

**Linear:** Creates uniform motion from start to finish. It has no acceleration or deceleration and feels mechanical in almost every context. It’s best used for objects where a consistent rhythm is expected, such as spinners or progress indicators.

**Hold:** Creates an animation that immediately jumps to its final position and stays there for the full duration. Holds are useful for multi-step sequences where an object needs to pause at an intermediate state before continuing, such as a loading screen that snaps into place and holds before the content fades in. Holds can also be used to create rhythmic animations where the timing needs to feel deliberate and precise.

### Understanding Bézier curves

Every easing curve is built on a Bézier curve, a mathematical model that maps how an animation progresses.

A Bézier curve is defined by four values, representing two control points. Each control point has an x and y coordinate. The x-axis represents the progression of time. The y-axis represents the progression of the animation. A straight diagonal line from corner to corner is linear motion. Curves that bow toward the top left produce ease out behavior. Curves that bow toward the bottom right produce ease in behavior.

When a control point’s y axis goes outside the 0 to 1 range, the animation travels beyond its starting or ending value, creating the wind-up and overshoot behavior present in the back curve presets.

![An animation demoing how to use the curve editor to create custom bezier curves](https://help.figma.com/hc/article_attachments/41238416717207)

**Note:** You can create custom easing curves and spring animations and save them as variables to be reused across your entire design system. Learn more about [creating custom curves](https://help.figma.com/hc/en-us/articles/41414048690839-Adjust-an-animation-s-easing#h_01KVRP7GC04ZVPNYJY3ZCMS8XS).

## What easing communicates

Knowing how each curve behaves is only half the picture. The other half is understanding what that behavior says to the viewer.

At its most functional, easing communicates the physical story of an object. As a general rule, objects entering the screen should decelerate as they arrive. Objects leaving the screen should accelerate as they exit. When the curve contradicts the story, the motion feels strange.

Easing can also add personality to motion. A steep, snappy deceleration feels confident and energetic. A long, gradual deceleration feels calm and considered. Being intentional about your easing curve choices will reinforce the broader character of your product.

![An animation demoing the difference between linear motion and motion with easing on a toggle element.](https://help.figma.com/hc/article_attachments/41238416719639)

Easing also plays a role in leading the viewer’s eye. The way an object accelerates or decelerates affects where the viewer’s attention goes and when. An object that decelerates slowly draws the eye to its final position, holding attention there as it settles. An object that arrives quickly and locks into place directs attention forward. In a choreographed sequence, easing can be used alongside timing and offset to guide the viewer through the content in a deliberate order.

## How easing builds expectation

The curve you choose also shapes what the viewer expects to happen next through anticipation and follow through.

Anticipation is the preparatory movement that precedes a main action. Before an object commits to its primary motion, it moves briefly in the opposite direction. Follow through is the continuation of motion after the primary action has ended. These principles give animated objects a sense of mass, intent, and physical believability.

In UI motion, both are expressed through easing. Back curves build physical expression directly into the easing. An ease in back dips briefly in the opposite direction before the object commits to its exit. An ease out back carries the object past its target before settling. An ease in and out back does both.

Spring animations achieve a similar effect through physics. Instead of a predetermined curve, a spring oscillates around the final position before coming to rest. The result feels less like a designed curve and more like a physical response.

Both back curves and spring animations add believability by implying that objects have mass and momentum. How much anticipation or follow-through is appropriate depends on the weight of the object, the tone of your product, and the importance of the moment. The same curve that feels alive and confident in one context can feel overdone in another.

![overshoot and anticipation.gif](https://help.figma.com/hc/article_attachments/41238416720791)

A little wind-up and overshoot goes a long way toward giving motion personality.
