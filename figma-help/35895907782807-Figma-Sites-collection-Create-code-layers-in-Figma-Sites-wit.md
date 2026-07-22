---
기술지원명: Figma Sites collection: Create code layers in Figma Sites with AI
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Figma Sites collection: Create code layers in Figma Sites with AI
출처링크: https://help.figma.com/hc/en-us/articles/35895907782807-Figma-Sites-collection-Create-code-layers-in-Figma-Sites-with-AI
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Code layers use AI and a prompting interface to help anyone, no matter their skill level, create custom functionality for their sites using real code.

**Note**: AI tools are available on paid Figma plans.
You can see which AI tools you can access in each of Figma's products
depending on your seat type in our
[About Figma AI article](https://help.figma.com/hc/en-us/articles/24039793359767-About-Figma-AI).
Interested in testing AI features?
[Learn how to upgrade your plan here](https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan).

## Use code layers

In this lesson, we'll use code layers to create an animated background for a header block. You can do something similar with an empty frame that you add to your breakpoint, just like we did in an earlier lesson.

To follow along, you could use a prompt like this one below:

```
Make a subtle gradient animation on the parent frame's fill. It should use pastel colors. Make the animation speed configurable via a property.
```

1. Select the header block, navigate to the right sidebar and select Make code from design.
2. The header block is now turned into a code layer. From the Make window, enter the prompt we provided above, or try one of your own that describes an experience you'd like to create from the design.
3. Once Figma is done generating, you can see an interactive preview and can also view and edit the resulting code.
4. Back on the canvas, we can check our results from the the full preview or inline preview.
5. Iterate! If you’re not getting the result you expected, double click the code layer to re-enter Make view and explore guiding the AI with new prompts and directions.

[Learn more in our guide to code layers →](https://help.figma.com/hc/en-us/articles/31242824165143-Guide-to-code-layers-in-Figma-Sites)

## Try it out!

Code layers give anyone, no matter their role or skill level, the ability to create engaging interactions powered by code. Try thinking of an interesting behavior that you’d like to see on your site, and craft a prompt describing the behavior.

If you’re not sure how to start or what to make, try using one of these prompts!

### Repel text from mouse

![](https://help.figma.com/hc/article_attachments/36112368261015)

```
When someone mouses over this frame, move the individual letters of the large headline text away from the mouse cursor as if the letters are being repelled by the mouse.
```

### Cycle through my skills

![](https://help.figma.com/hc/article_attachments/36112368261911)

```
This header in this hero section of my portfolio site contains information about myself. It says “I’m Krystal and I’m a [blank]”. The [blank] should animate and cycle through these words [Product Designer, Product Manager, Maker, Creative, Musician, Singer, Gamer]. Cycle through the options one at a time. Each time the word cycles to a new word, that word should be a different color—cycle between  #FF7C83, #FFDD7C, #8D7CFF and #789496. Don’t repeat colors back-to-back.
```

### Make a digital whiteboard

![](https://help.figma.com/hc/article_attachments/36112424156311)

```
Within this frame, add a subtle dotted grid background pattern. Inside of this frame, let users draw with a colorful marker tool using their mouse. The color should be random but choose from these colors:  #FF7C83, #FFDD7C, #8D7CFF and #789496. The marks should begin to fade away after 5000ms and should fade away over 3000ms.
```

**Note**: Prompting is a skill and it might take you several tries to get the results you’re looking for. Remember to be descriptive and write your prompts as clearly as possible. You got this!

## Up next: Accessibility

Making your websites accessible to people who use assistive technology is an important step before publishing your website. We'll show you where to find these settings in the next lesson.

## Additional resources

[Code layers with Lauren Byrne](https://help.figma.com/hc/en-us/articles/35896245862423) (recommended) — Watch this extra credit lesson that we’ve included at the end of this collection to see Lauren create a few different code layers using Figma AI.

[Explore Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make) — Figma Make is an AI-powered, prompt-to-app tool that lets you bring ideas and existing Figma designs to life as functional prototypes, web apps, and interactive UI. It’s for anyone, no matter their skill level.

[Figma Sites playground file](https://www.figma.com/community/file/1543020893913814047) — Our Figma Sites playground file has exercises to learn more about Figma Sites.
