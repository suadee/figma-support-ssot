---
기술지원명: Custom skills for the Figma agent and Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Custom skills for the Figma agent and Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/40283639496599-Custom-skills-for-the-Figma-agent-and-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma agent is currently available to try for free in open beta. [Learn more.](https://help.figma.com/hc/en-us/articles/34932042346775)

Who can use this feature

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Users with Full seats can chat with the agent in Figma Design and Figma Make files

Users with View, Dev, or Collab seats can try the agent in Figma Design and Figma Make files in Drafts

Requires edit access to the file

Skills let you package a repeatable workflow into a reusable set of instructions for an AI agent. Instead of rewriting long prompts and re-explaining conventions each time, a skill gives an agent a stable sequence of steps to follow, which improves consistency across runs. Fundamentally, skills are Markdown files that follow the [Agent Skills specification](https://agentskills.io/specification).

Everywhere the Figma agent is supported, such as Figma Design and Figma Make, custom skills enable the agent to perform tasks that ease how you work, like reviewing content or checking a UI against your team’s design standards. Once installed, a skill can be invoked explicitly with a slash command such as `/follow-ds-guidelines` or `/design-crit`. You can create a custom skill manually in the chat sidebar or upload a Markdown file for your existing skill.

Paired with [connectors](https://help.figma.com/hc/en-us/articles/35440096186007), skills can pull live context from the tools your team already uses, so a single skill can fetch your design system from Notion, your PRDs from Drive, and apply both to whatever you're building.

The results you get using custom skills with the Figma agent should very often be consistent. However, because the models that power the agent are inherently non-deterministic, the result may not be exactly the same each time you use the skill.

## Create a custom skill

Custom skills are created in the chat sidebar for the agent and in Figma Make. Though you create custom skills while in a new or existing file, your custom skills stay available across all files. There are two ways to create a custom skill:

- [Upload an existing skill](#h_01KR283FSA0EXZBHK1BMZJAB43)
- [Manually write the skill using Markdown](#h_01KR29NVFWKRNDES5445CE4QN6)

![](https://help.figma.com/hc/article_attachments/41460120369815)

### Upload an existing skill

If you have existing skills outside Figma that you want to use with the agent or in Figma Make, you can upload those skills. The skill must be a single Markdown (`.md`) file that follows the [Agent Skills specification](https://agentskills.io/specification). Custom skills *do not* support optional directories such as `scripts/`, `references/`, and `assets/`, which might sometimes be packaged with an agent skill.

To upload a skill:

1. In a chat, click  in the prompt box.
2. Select **Skills**, and then **Add skill**.
3. Drag in a skill file or click **Upload a file**.
4. Select the skill Markdown file you want to upload.
5. Review the name, description, and content of the uploaded skill. The name defines the slash command you'll use to invoke your skill.
6. Click **Add**.

After your skill is created, you're ready to start using it.

### Create a skill manually

You can create skills manually in Figma. To create a skill, you'll need to provide a name, description, and the instructions that teach the agent what to do when using the skill. You can use [Markdown](https://www.markdownguide.org/basic-syntax/) to format the instructions.

To create a skill manually:

1. In a chat, click  in the prompt box.
2. Select **Skills**, and then **Add skill**.
3. Click **Start from scratch**.
4. Enter the name, description, and instructions for the skill. The name defines the slash command you'll use to invoke your skill.
5. Click **Add**.

After your skill is created, you're ready to start using it.

## Use custom skills

After you've [created your custom skills](#h_01KR25YE07V3MRWB2DKZ6N4N1F), you're ready to start using them.

To use a skill with the Figma agent or in Figma Make, you must invoke the skill. Invoking the skill manually ensures the agent uses it during a step in a conversation. To invoke a skill, enter slash commands in the prompt box.

![](https://help.figma.com/hc/article_attachments/41460120371991)

If you prefer, you can also select a skill from the list of skills you've created:

1. In a chat, click  in the prompt box.
2. Select **Skills**, and then **Use skills**.
3. From the list of skills, select the skill you want to use.
4. Click  **Send**.

**Tip:** To further enhance how you use custom skills, take advantage of [connectors](https://help.figma.com/hc/en-us/articles/35440096186007). Your skills can reference your connectors and you can invoke a skill and reference a connector in the same prompt. This approach gives more context to a skill and guides the agent when it takes actions with your connectors. For example:

"Use the /build-from-prd skill to implement this PRD from @Notion https://www.notion.so/PRD-personal-information-page."

## Manage custom skills

After you've [created custom skills](#h_01KR25YE07V3MRWB2DKZ6N4N1F), you may want to manage the skills. You can:

- [Publish a skill to a team or organization](#h_01KR2BN09MG6YTA28GVYHHVD8S)
- [Update a published skill](#h_01KVE0QEQTWQPSX0HG6HHX0ET9)
- [Unpublish a skill](#h_01KVE4NCP3J9R98AGCXWKEX185)
- [Make changes to a skill's instructions](#h_01KVE2KY5MTPP0MRW1Z6KJHNEA)
- [Export a skill as a Markdown file](#h_01KR2C8NVFW4SPB7D3H9HXKTC5)
- [Enable or disable a skill](#h_01KR2CGTSNZH29MWA90NNJQJ85)
- [Delete a skill](#h_01KR2CQHCNRGYY0M7GMG4Y23ZX)

To manage a skill:

1. In a chat, click  in the prompt box.
2. Select **Skills**, and then **Manage skills**.

### Publish a skill

After you create a custom skill, you may want to share the skill with others in your team or organization. To share the skill, you can publish it.

![](https://help.figma.com/hc/article_attachments/41460096929559)

To publish the skill to a team or organization:

1. In the **Manage skills** modal, select the skill you want to publish.
2. In the upper-right corner, click  and then select **Publish**.
3. Edit the name and description of the skill as needed. If you change the name while publishing, only other users will see the new name. Your version of the skill will retain the existing name.
4. Click **Publish**.

**Note:** To publish a skill to a team, the file that you're publishing the skill from must be in that team. You can publish only to the team where the file is located or to the whole organization.

### Update a published skill

After publishing a skill, you may want to update make changes to the skill and share those changes with others. To share the updates, you can publish the changes to your skill.

![](https://help.figma.com/hc/article_attachments/41460120374551)

To publish changes to a skill:

1. In the **Manage skills** modal, select the published skill you want to update.
2. In the upper-right corner, click  and then select **Manage skill**.
3. Click **Publish changes**.
4. Edit the name and description of the skill as needed. If you change the name while publishing, only other users will see the new name. Your version of the skill will retain the existing name.
5. Click **Publish**.

### Unpublish a skill

After publishing a skill, you may want to unpublish it. Unpublishing a skill retains the skill for your use, but makes it unavailable to others in the team or organization where it was previously published.

![](https://help.figma.com/hc/article_attachments/41460096931095)

To unpublish a skill:

1. In the **Manage skills** modal, select the skill you want to publish.
2. In the upper-right corner, click  and then select **Manage skill**.
3. Click **Unpublish skill**.

### Edit instructions

After you create a custom skill, you may want to edit the instructions. This is useful for iterating the functionality of the skill as you use it.

![](https://help.figma.com/hc/article_attachments/41460096931607)

To edit the instructions of a custom skill:

1. In the **Manage skills** modal, select the skill you want to edit.
2. In the upper-right corner, click  and then select **Edit**.
3. Edit the name, description, and instructions for the skill as needed.
4. Click **Save**.

### Export skill

After you start using custom skills, you may want to export a skill so you can use it with your own agents.

![](https://help.figma.com/hc/article_attachments/41460120381975)

To export a custom skill:

1. In the **Manage skills** modal, select the skill you want to export.
2. In the upper-right corner, click  and then select **Export**.

### Enable or disable a skill

If you want to temporarily stop a skill from appearing in the list of skills without deleting it, you can turn the skill off. At any time you can turn the skill back on again following the same steps. When a skill is disabled, it cannot be invoked automatically in chat or directly.

**Note:** If your skill is published, disabling it only disables the skill for your account. If you want to remove access to your skill, you'll need to unpublish it or [delete it](#h_01KR2CQHCNRGYY0M7GMG4Y23ZX).

![](https://help.figma.com/hc/article_attachments/41460120383127)

To turn a custom skill off or on:

1. In the **Manage skills** modal, select the skill you want to turn off or on.
2. In the upper-right corner, click the **Disable skill** toggle.

### Delete a skill

If you're no longer using a skill, you can delete it. When you delete a custom skill, it is permanently removed. That means if you've made changes to a skill you uploaded or created a skill manually, your instructions will be lost. If you want to delete a skill but preserve the instructions, make sure you [export the skill](#h_01KR2C8NVFW4SPB7D3H9HXKTC5) first.

**Note:** If your skill is published, deleting the skill removes it for all users.

![](https://help.figma.com/hc/article_attachments/41460096935191)

To delete a custom skill:

1. In the **Manage skills** modal, select the skill you want to delete.
2. In the upper-right corner, click  and then select **Delete**.

## Known issues

Currently, there are some known issues to keep in mind while you're creating and working with custom skills.

- If you mention multiple skills in a single prompt, only the first skill used will be invoked.
- Figma Make only supports standalone skill files when you're uploading skills. You can't include additional files for the skill.
- In Figma Make, when you switch models during a session, you can't immediately invoke a skill in the first prompt that follows. Invoking skills in subsequent prompts after the first works as expected.
