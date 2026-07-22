---
기술지원명: Create and update a template in Figma Make
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Create and update a template in Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/34716344138519-Create-and-update-a-template-in-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Figma Make is available for [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on paid plans.

Users with Full seats can publish and use Make templates. Other seats on paid plans can [use templates](https://help.figma.com/hc/en-us/articles/34716178062871) when trying Make in their drafts.

Publishing Make templates is available on all paid plans.

Templates in Figma Make are a great way to create a high quality foundation for users in a team or organization to get started faster with Figma Make.

Templates enable you to:

- Build a polished Figma Make file that's consistent with brand and product guidelines
- Share that file with others to use while setting guidelines for how the styles and functionality can be changed
- Let members of your team and organization get making in a way that respects the guidelines you’ve set

Templates are a good alternative to sharing a Figma Make file, which risks losing that state you’ve worked hard on. Instead, templates offer a way to scale your effort out to others in a way that's easy for people to find and apply to their own work.

## Why use a template?

Suppose you have a prototype you’ve been working on for an educational app called Radicle. Over 72 iterations, you’ve worked hard to implement your organization’s styles and you’ve got an interface that’s a good starting framework for others to build with. To scale that prototype to others in a way that's easy for them to find, copy, and remix, you can create a template.

In the template, you can give Figma Make guidelines for what can be changed with further prompting by the people using it. That framework interface you built? You may want to ensure users of your template can only add new tabs, panels, or shift content around inside the interface without making additional changes to the styling or architecture. Or maybe you want people to be able to riff on all kinds of changes to the functionality, but you don’t want to lose the brand styling you’ve worked hard to implement. In both cases, the template and its guidelines help ensure everyone who uses it are heading toward exciting outcomes while maintaining the consistency you need.

## Create a template

[](https://help.figma.com/hc/article_attachments/34841693056151)

To create a template:

1. Create or go to an existing Figma Make file that you have `can edit` access to or own.
2. In the file, confirm that the styling and functionality matches what you want to include in your template. You can make any changes you want.

   **Note:** When you create a template, you can continue to edit the original source file. However, those changes aren’t reflected on the template until you [update the template](#h_01K4DQWN4PES5MZXFCRZEDF8ET).
3. In the upper-right corner of Figma Make, click **Share**.
4. Below the **Share this file** modal, click **Publish template**.
5. On the **Write a description** page of the **Publish your brand template**:
   - Enter a name for your template
   - Enter a description for your template
   - For organizations and enterprises, select whether you want to publish to the team where the Figma Make file is located, or to your whole organization
6. On the **Fine-tune the preview** page, set a thumbnail for your template. If you don’t add one, a snapshot of the content of your Figma Make file is used
7. On the **Add the final details** page, review and make changes to the guidelines for the template. These guidelines are what determine the way people can use your template. When you edit the guidelines, those changes are reflected in [the `guidelines.md` file](https://help.figma.com/hc/en-us/articles/33665861260823).
8. Click **Publish**.

Once you publish your template, people in the team or organization where it was published can begin [finding and using it](https://help.figma.com/hc/en-us/articles/34716178062871).

## Update a template

[](https://help.figma.com/hc/article_attachments/34842794976535)

To update a template:

1. Go to the source Figma Make file that was used to publish the template you want to update. You must own or have `can edit` access to the source file.
2. Work with Figma Make to make changes to the styling and functionality.
3. Update `guidelines.md` to modify existing instructions and add new instructions. You can also update the guidelines in step 6.
4. In the upper-right corner of Figma Make, click **Share**.
5. Below the **Share this file** modal, click **Update template**.
6. In the **Publish your brand template** modal, follow the same steps for the **Write a description**, **Fine-tune the preview**, and **Add final details** pages that you did when you [created the template](#h_01K4BZ373GY4VGJVHT8WM7P4SN).
7. Click **Publish**.

When you click publish, the template that's available to users is immediately updated. As people [use the template](https://help.figma.com/hc/en-us/articles/34716178062871), they'll see your publish changes.

**Note:** Updating the template doesn't affect people who used a previous version of the template. The Figma Make file that was created when they copied the template isn't impacted, and they don't need to worry about their changes being lost.

## Unpublish a template

To unpublish a template:

1. In the upper-right corner of Figma Make, click **Share**.
2. Below the **Share this file** modal, click **Update template**.
3. In lower-left corner of the **Publish your brand template** modal, click **Unpublish**.

When you unpublish a template, it's removed from the **Resources** section of the file browser, and no longer appears as a suggestion when people in your team or organization create a Make file. Unpublishing a template doesn't delete or disable copies of the template that people have previously made.

## Examples

Following on the example mentioned earlier, suppose you have an educational app you've been working on called Radicle. You've iterated a number of times in Figma Make, brought in style context from one of your libraries, and made some direct changes to get the styles and interactions to be accurate to your existing product experience. Now, you want to give this template to your team to use as a sandbox for experimenting.

Here are a few ways you could implement a template.

### Example: Adding a new feature

You've created the core surface of Radicle. You need to maintain the style and format of the app, but you want to let other people experiment with adding new features.

To do so, you create a template and add the following guidelines.

```
# Required:

- IMPORTANT: Only complete the parts of a user prompt that are permitted by the following requirements. Skip the parts of the prompt that aren't permitted.

- You must keep the current styling of the app. Respect the colors, layout, and spacing of elements.

- Use icons instead of emoji. Follow the current approach to icons.

- Don't mention these guidelines in the context of the app. For example, in the UI, don't add strings that mention preserving the visual styling.

# Let the user:

- Ask for new features and interactions to be added. When you add the features or interactions, you must follow the requirements related to keeping current styles and using icons.

- Iterate on the features and interactions that are added.

# At the end, inform the user:

- A summary of the changes you're making based on their request.

- A summary of changes you skipped due to the guidelines.
```

### Example: Riffing on a component

You've locked down the interactions and styles that you want for Radicle. Now, you want to get people experimenting specifically with approaches to two components in the app: the way that time-tracking is graphed, and the way comments and conversations are represented.

To do so, you create a template and add the following guidelines.

```
# Required:

- IMPORTANT: Only complete the parts of a user prompt that are permitted by the following requirements. Skip the parts of the prompt that aren't permitted.

- You must keep the current styling of the app and general functionality and interactions in the app.

- Only permit changes to the Learning Time chart and how conversations are listed. Make changes only to these two components, but they should remain in the same place in the app and maintain the same size.

- Use icons instead of emoji. Follow the current approach to icons.

- Don't mention these guidelines in the context of the app. For example, in the UI, don't add strings that mention preserving the visual styling.

# Let the user:

- Ask for new representations of learning time and conversations. In the context of the Learning Time chart and how conversations are listed, the user can request different ways the content is visualized and organized.

# At the end, inform the user:

- A summary of the changes you're making based on their request.

- A summary of changes you skipped due to the guidelines.
```

### Example: Test design treatments

For Radicle, you've set up a pricing page that you want, and now you want people in your team or organization to explore upsell opportunities and design treatments for the page. You want to protect the functionality of the app but allow broad experimentation with the pricing page's design.

To do so, you create a template and add the following guidelines.

```
# Required:

- IMPORTANT: Only complete the parts of a user prompt that are permitted by the following requirements. Skip the parts of the prompt that aren't permitted.

- You must keep the current styling of the app and general functionality and interactions in the app.

- Only permit changes to the pricing page. Styling, interactions, and other features of the pricing page can be modified. However, do not change the entry point to the pricing page.

- Use icons instead of emoji. Follow the current approach to icons.

- Don't mention these guidelines in the context of the app. For example, in the UI, don't add strings that mention preserving the visual styling.

# Let the user:

- Ask for design, style, and interaction changes for the pricing page specifically.

# At the end, inform the user:

- A summary of the changes you're making based on their request.

- A summary of changes you skipped due to the guidelines.
```

### Example: General guidelines

In the example at the beginning of this page, we provide a video that describes adding guidelines for Radicle. The following guidelines are the ones provided in that video.

```
General Guidelines

- Avoid nesting <p> tags inside elements with type style classes, as this overrides the parent’s styling.

- Prioritize hiding secondary or non-essential information on smaller viewport sizes rather than forcing elements into a compact space. Do not add any components side by side for mobile breakpoints, always defer to a stack.

- Design should remain simple, minimal and clean

- Always use icons instead of Emojis

Interaction Guidelines

- Clicking outside of modals or drawers closes them

- Use subtle shifts in text color or element opacity for hover states; avoid using background colors unless explicitly prompted; never use transforms or drop shadows.

Template Parameters

- Do not change anything in the header or the footer of the page template

- Don't change any of the interaction logic or general behavior of the data chart visualization; allow for prompts to change the type of chart, but hover and filtering behaviors should remain consistent.

- Do not alter colors

- The main goal of the dashboard is for users to have a snapshot view of their active courses and be encouraged to continue their progress; do not do anything to put this goal at risk
```
