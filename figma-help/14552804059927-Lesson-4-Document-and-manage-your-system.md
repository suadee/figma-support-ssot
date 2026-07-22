---
기술지원명: Lesson 4: Document and manage your system
카테고리: 디자인
작성자: Figma
승인자: suadee
출처: Lesson 4: Document and manage your system
출처링크: https://help.figma.com/hc/en-us/articles/14552804059927-Lesson-4-Document-and-manage-your-system
게시일: 2026-07-22
검토일: 2026-07-22
---

## 내용

This is a written version of our [**Introduction to design systems: Lesson 4**](https://www.youtube.com/watch?v=_sTWtnNU1L0) video tutorial. Watch the video and follow along with the written course below.

Welcome back!

In the previous lesson, we saw the Habitz team build out aspects of their design system in Figma.

In this lesson, let’s learn a few ways to support the ongoing success of your design system, like:

- Effective documentation
- Improving your system through testing, feedback, and contributions
- How to manage updates
- How to make sure people are using it

## Chapter 1: Documentation

If you want to win the hearts of your design system consumers, effective documentation is a must.

### What is documentation?

[In the previous lesson](https://help.figma.com/hc/en-us/articles/14548865734679/), Kai and the Habitz team defined some naming conventions and wrote descriptions for styles and components. But documentation can go beyond this. For example, you could:

- Include examples for correct and incorrect uses of a pattern   
  ![](https://help.figma.com/hc/article_attachments/14794860860951)
- Use a change log to track component updates  
  ![](https://help.figma.com/hc/article_attachments/14794903407127)
- Add code examples or links to developer implementation  
  ![](https://help.figma.com/hc/article_attachments/14794943749527)

Effective documentation anticipates the needs of its consumers and is presented in a way that speaks directly to them. For example, developers might need to cross-reference tokens and properties, while writers need guidance on crafting error messages.

![](https://help.figma.com/hc/article_attachments/14794968997783)

Think about what parts of your system might need extra context. What might different audiences benefit from knowing?

### Where should documentation live?

Where your documentation lives, and how easy it is to find it, can also impact how effective it is. We often see design systems living on dedicated websites, like Google’s [Material Design](https://m3.material.io/) or [Atlassian’s Design System](https://atlassian.design/).

![](https://help.figma.com/hc/article_attachments/14794987609495)

Websites are great if you’re looking for something highly customizable, and can be necessary for larger companies with many products. However, they require resources to build and maintain. If you’re a small team, this may be a dealbreaker for you.

![](https://help.figma.com/hc/article_attachments/14795050652311)

Instead, using tools like [Storybook](https://storybook.js.org/) or [Notion](https://www.notion.so/), or housing documentation in the same place as your design system, might get you up and running sooner.

#### Add links to documentation

If your design system lives in Figma and its documentation lives elsewhere, you can [link to documentation from any component and component set](https://help.figma.com/hc/en-us/articles/7938814091287) for ease of access.![](https://help.figma.com/hc/article_attachments/14798113608599)

#### Habitz

Since the Habitz team is small, they’ve decided to use their existing design file to host both their assets and their design documentation. This suits their current workflow and keeps everything in one place.

![](https://help.figma.com/hc/article_attachments/14795132357783)

In their file, they’ve created pages for:

- **Foundations**—which includes things like spacing, typography, and colors;
- **Components**—for buttons, cards, toggles, and so on;
- **Patterns**—like the daySelector, navigation, and lists.

![](https://help.figma.com/hc/article_attachments/14795122425879)

Each collection of assets is placed in a frame with a label, and any additional notes or context.

![](https://help.figma.com/hc/article_attachments/14795151404055)

### Documentation in Figma

The Habitz team uses a modified version of an 8-point grid system. They want to explicitly communicate that information, outside of their styles and components.

![](https://help.figma.com/hc/article_attachments/14798084638615)

They’ve created some elements that capture their common spacing values. This lets designers know which values to use, and better aligns designs with code.

![](https://help.figma.com/hc/article_attachments/14795193075735)

You may have noticed that these spatial definitions aren’t components. That’s because these assets aren’t intended to be used in designs.

![](https://help.figma.com/hc/article_attachments/14795210339351)

Rather, they are illustrations for people to visualize empty space, and exist to document system decisions and give consumers a reference point.

![](https://help.figma.com/hc/article_attachments/14798081751703)

Spatial systems also set the basis for other things like layout guides, padding, and as this documentation suggests, nudge values in Figma.

**Note**: The Figma feature "layout grid" has been renamed to "layout guide" and may not match what you see in the video course.

![](https://help.figma.com/hc/article_attachments/14795264854039)

#### Use design linters

Design linters audit designs for areas that don’t meet design system requirements—like incorrect spacing or missing styles. Check out linters, like [Design Lint](https://www.figma.com/community/plugin/801195587640428208/Design-Lint) by Daniel Destefanis and  [Roller](https://www.figma.com/community/plugin/751892393146479981/Roller-%C2%B7-Design-Linter) by Contrast, from the Figma Community and see if they work for your system.

## Chapter 2: Improve your system

So you’ve built out solutions and created documentation. What’s next? It’s time to get it into the hands of your consumers to validate your design system and refine its solutions.

Testing and gathering feedback helps us understand what’s working and what needs improvement. This can be done at any point in your process, even while you’re building the system.

![](https://help.figma.com/hc/article_attachments/14795264268311)

Remember that design systems will evolve over time. The information you gather will be valuable even if you don’t have a finished system in place.

### Test with consumers

One of the most common testing methods is conducting [user interviews](https://www.figma.com/community/tag/user%20interview/files), which can be done one-on-one or in a group; virtual or in person.

Before you start, determine what you want to evaluate and what you’d like to get from your participants. Knowing this helps you select people who will provide the most valuable insights.

If you have multiple groups of participants, pay attention to user flows and problems unique to each one. Turn them into tasks for participants to complete—like recreating screens and modals, or testing the search experience.

![](https://help.figma.com/hc/article_attachments/14795286964759)

#### Testing tips

- When applicable, have participants complete the tasks twice: once using their current workflow and once using the design system or solution you built. After each round, have them compare the two experiences and quantify it with a grade.
- Notice how long it takes participants to find what they need, and whether assets are used as intended.
- See where they find documentation to be unclear or confusing.
- Lastly, notice when they detach components, or when components don’t behave the way you intended. This could indicate that documentation is lacking, components aren’t set up correctly, or other parts of the design system needs work.

![](https://help.figma.com/hc/article_attachments/14798086535191)

[**Learn more about design research →**](https://www.figma.com/resource-library/design-research/)

#### Habitz

Kai wants to test the design system by having designers build out the Habitz homepage on mobile—once without the system and a second time with it. The team noticed that designers completed the task about three times faster when using the design system.

![](https://help.figma.com/hc/article_attachments/14795344182039)

They also noticed that designers kept detaching the same component, because it didn’t reflow between screen sizes. So, the team revisited component and discovered that its constraints weren’t set up correctly. This is a quick fix!

### Ask for feedback

User testing is a proactive way to gather insights on design system performance. However, you may also benefit from establishing a channel for ongoing feedback, especially as your company grows.

Feedback can be collected in various ways. For example, surveys are great for asking targeted questions to gather the details you need. Or, people can drop comments in a design file, or vote on options in a FigJam file for asynchronous feedback.

![](https://help.figma.com/hc/article_attachments/14795461782551)

#### Habitz

The Habitz team decided to create a communication channel to collect feedback, so that others can engage in the discussion.

They also want to gain a higher volume of quality feedback by increasing awareness and usage of the design system. To do this, they [made the system available to the entire Habitz organization](https://help.figma.com/hc/en-us/articles/360040529593) to use in team files.

Choose the approach that works best for you and your company’s workflow.

Keep in mind that change can be difficult. If people express frustration, use that feedback as an opportunity to evolve your design system. Keep listening for ways to improve and encourage people to share their thoughts.

#### Track library usage

How do you understand the success of your design system? If you’re using Figma and you want to explore how your system is being used, check out the [Design System Analytics](https://help.figma.com/hc/en-us/articles/360039238353) feature to learn more!

### Manage contributions

Feedback is great at identifying issues but who implements the fixes? If you want to empower your design system's consumers to make improvements themselves, establish a contribution process.

A contribution process establishes a path for contributors to take their suggestions from proposal to implementation. It includes timelines, guidance on what to do, and information on how to align your solution to design system goals, visual requirements, and more.

An effective contribution process benefits your team by handling the onboarding and knowledge sharing to ensure that contributions are consistent with the design system.

The process you develop will depend on your company’s size and the needs of your team. Every system should have an internal contribution process, intended for those already maintaining the design system.

You may also want a process for people who aren’t on the design system team. This requires more guidance and resources and any feedback may require a more rigorous review. Enabling participation from people who actually use the system on a daily basis is a great way to support its success.

#### Habitz

Kai decided to build an internal contribution process to support a growing team.

They start by exploring a simple flow that communicates different parts of the process, and key decision points teammates will run into.

![](https://help.figma.com/hc/article_attachments/14795536140183)

As the team grows, Kai hopes to build on this process by including paths for making small, medium, and large contributions.

![](https://help.figma.com/hc/article_attachments/14795558825495)

Eventually, as the company grows and as the volume of feedback increases, they plan on creating an external contribution process to summon a wider array of ideas and solutions for the system.

![](https://help.figma.com/hc/article_attachments/14795567253271)

## Chapter 3: Updates and releases

### Versions and changelogs

Your design system is bound to go through iterations from all the testing, usage, and feedback you’re getting! Changelogsare a great way to track these updates.

Each version update gets its own change log entry with what’s new, what’s changed, bug fixes, and a version number to help reference specific iterations.

Version numbers should follow a versioning scheme for consistency and to convey information about the update.

![](https://help.figma.com/hc/article_attachments/14795593159191)

#### Semantic versioning

One of the most common schemes is **semantic versioning**, often recognized by its pattern of numbers separated by decimals: `1.6.2`.

They’re structured in the Major.Minor.Patch pattern, which refer to types of changes. Each type is represented by its own version number that increases by 1 anytime a relevant change happens.

![](https://help.figma.com/hc/article_attachments/14795607040535)

- **Major** changes refer to updates that break existing designs and are not backwards compatible. Like large changes in visual style, or removal of components.
- **Minor** changes are updates *without* breaking changes that can flow seamlessly into existing designs
- **Patches** refer to bug fixes without breaking changes. This could be incorrect padding values, component names that don’t match code, or bug fixes.

#### Be consistent and considerate

There are many schemes out there, but consistency is key, so choose one and stick to it. And keep in mind how often you release updates so you don’t overwhelm your consumers. Give people time to transition and adopt the changes!

### Branching and merging

When we make improvements, we need to be mindful of the impact this will have on anyone using the system.

If you’re working with a small team, with only a few contributors, you could coordinate those updates within your group. But if you’re in a larger organization, there are likely more people using the design system who will be impacted by changes or updates.

In software development, developers branch off from the main code base into a controlled environment to experiment, test new code, and make updates. This allows developers to explore solutions without any downstream impact.

Changes from a branch go through a review process, where they can be accepted or denied. Approved changes are then merged into the main code base and then deployed as a single version or release.

![](https://help.figma.com/hc/article_attachments/14798142273687)

We can follow this exact approach for our design system—make our changes in a separate environment so as to not disrupt those using the current version.

#### Habitz

If Kai’s team has two different teams working on different projects—such as dark mode and the integration experience, they can create branches to work on their respective projects without affecting the main design system. Then, they can send their changes off for review and approval, and deploy it in the next release.

![](https://help.figma.com/hc/article_attachments/14798129362967)

#### Plan requirements

If you’re using Figma, branching and merging is available in the Organization and Enterprise plans. [**Learn about branching and merging →**](https://help.figma.com/hc/en-us/articles/360063144053)

## Chapter 4: Advocate for your system

If you want people to use a design system, advocate for it by sharing, raising awareness, and educating others on its value. Get people excited and invested in its success by showing how it can help them.

Advocating for a design system can happen at various stages of the process, even before the first version is complete. In fact, we recommend starting early!

Gather information from different teams on what pain points they run into. Present your work-in-progress at all hands to generate excitement and to get interested people involved.

You can also find low-effort ways of raising awareness like mentioning it in conversation with coworkers or dropping a message in a wider channel.

By the time you finish your design system, you’ll have an audience that is already eager to adopt and advocate for it.

#### Summary

If this is your first time building a design system, remember that it’s a marathon, not a sprint.

Everything is iterative, including your learning process, so remain flexible especially when you’re tempted toward perfection.

As you continue this journey, you’ll discover that despite the enormous array of ideas, methods, and opinions, design systems are for people and yours will be unique to you.

Thanks for joining us on this journey, exploring what a design system is, and following Kai and the Habitz team as they built the first version of their design system.

What was your biggest take away? What do you want to learn about next? If you have an idea for another course you’d like to see, we’d love to hear that too.

[3: Build your system](https://help.figma.com/hc/en-us/articles/14548865734679) [Go back to the start](https://help.figma.com/hc/en-us/articles/14552901442839)
