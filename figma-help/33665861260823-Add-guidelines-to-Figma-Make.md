---
기술지원명: Add guidelines to Figma Make
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Add guidelines to Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/33665861260823-Add-guidelines-to-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Figma Make is available for [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on paid plans.

You can try Figma Make on [other seats and plans](https://help.figma.com/hc/en-us/articles/31722591905559-Figma-Make-FAQs#h_01JZQX7SQ7RX4SJ65DHDTYS2EK).

Providing guidelines helps Figma Make to create a functional prototype or web app that better meets your needs and expectations. They contain instructions that describe how you want Figma Make to behave in terms of coding and personality, and how to use things like style context.

To add guidelines to Figma Make, you can [add your own](#h_01KQJ6K2WNNXYN6Q3CBKZ0F9FP) or [ask Make to generate them](#h_01KQJ78NRKP7FGE2NZQWZVDHBW) for you.

### Content of the Guidelines.md file

When you create something with Make, an empty `Guidelines.md` file is also added. Instructions, best practices, and examples of how to use the guidelines file are included in the file itself. For convenience, the content of the file is available in the following section.

```
System Guidelines

Use this file to provide the AI with rules and guidelines you want it to follow.
This template outlines a few examples of things you can add. You can add your own sections and format it to suit your needs

TIP: More context isn't always better. It can confuse the LLM. Try and add the most important rules you need

# General guidelines

Any general rules you want the AI to follow.
For example:

* Only use absolute positioning when necessary. Opt for responsive and well structured layouts that use flexbox and grid by default
* Refactor code as you go to keep code clean
* Keep file sizes small and put helper functions and components in their own files.

--------------

# Design system guidelines
Rules for how the AI should make generations look like your company's design system

Additionally, if you select a design system to use in the prompt box, you can reference your design system's components, styles, and variables.
For example:

* Use a base font-size of 14px
* Date formats should always be in the format “Jun 10”
* The bottom toolbar should only ever have a maximum of 4 items
* Never use the floating action button with the bottom toolbar
* Chips should always come in sets of 3 or more
* Don't use a dropdown if there are 2 or fewer options

You can also create sub sections and add more specific details
For example:

## Button
The Button component is a fundamental interactive element in our design system, designed to trigger actions or navigate
users through the application. It provides visual feedback and clear affordances to enhance user experience.

### Usage
Buttons should be used for important actions that users need to take, such as form submissions, confirming choices,
or initiating processes. They communicate interactivity and should have clear, action-oriented labels.

### Variants
* Primary Button
  * Purpose : Used for the main action in a section or page
  * Visual Style : Bold, filled with the primary brand color
  * Usage : One primary button per section to guide users toward the most important action
* Secondary Button
  * Purpose : Used for alternative or supporting actions
  * Visual Style : Outlined with the primary color, transparent background
  * Usage : Can appear alongside a primary button for less important actions
* Tertiary Button
  * Purpose : Used for the least important actions
  * Visual Style : Text-only with no border, using primary color
  * Usage : For actions that should be available but not emphasized
```

## Add your own guidelines

To add your own guidelines, you can upload them in the form of one or more markdown files or you can write guidelines directly in Make using the `guidelines.md` file provided.

### Upload a markdown file

If you have an existing markdown (.md) file containing guidelines instructions, you can upload it directly into the **Guidelines** folder in Make.

1. At the top of Figma Make, click **Code**.
2. In the file explorer at the left side of the code editor, and open the **guidelines** folder.
3. Select **Upload**, or click and drag the .md file from your desktop directly into the folder.

Figma Make will update any existing designs with the newly uploaded guidelines and continue using the guidelines in future iterations.

**Note**: You can upload multiple markdown files if desired. We suggest that you audit the markdown files to identify conflicting information, and to specify within your guidelines how Make should use markdown file.

### Write guidelines in Make

You can use the `guidelines.md` file in your Make to write guidelines.

1. At the top of Figma Make, click **Code**.
2. In the file explorer at the left side of the code editor, and open the **guidelines** folder.
3. Select the file `guidelines.md`, and use the code editor to write the guidelines and instructions—such as how to use a component and what variants to apply depending on the usage..

You can add additional guidelines folders and files by right-clicking the guidelines folder and choosing **Create file** or **Create folder**.

## Prompt Make to generate guidelines

Prompt Figma Make to analyze your npm packages and library styles and write comprehensive guidelines for you. Make will create one or more markdown files covering components, styles, tokens, and general design system rules. You can review what Make generated from the guideline files, and refine them with specific use cases and edge cases.

This option uses [AI credits](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work). Learn [best practices for optimizing AI credits in Figma Make](https://help.figma.com/hc/en-us/articles/40097793879191).

**Note**: It may take a few minutes for Make to analyze and generate comprehensive guidelines.

## Guidelines for Make kits

Make kits are a way of sharing library styles and design system packages with your teammates. A critical part of Make kits are guidelines, which allow Figma Make to use your Make kit to create high quality, reliable output.

Because guidelines for Make kits require a specialized approach based on how you're assembling your Make kit, we cover best practices in two articles:

- For library styles, see [Guidelines for library styles](https://help.figma.com/hc/articles/39241689698839#h_01KMNQRFPC8J0SHQPKE9YXM0KJ) in [Get started with Make kits](https://help.figma.com/hc/en-us/articles/39241689698839).
- For design system packages, see [Write design system guidelines for Make kits](https://developers.figma.com/docs/code/write-design-system-guidelines/) in our developer documentation.
