---
기술지원명: Create FigJam diagrams with Claude
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Create FigJam diagrams with Claude
출처링크: https://help.figma.com/hc/en-us/articles/37883260397975-Create-FigJam-diagrams-with-Claude
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on any Figma plan

Available for FigJam

You must have an existing Figma account to use this integration

[Learn more about who can access AI features in Figma](https://help.figma.com/hc/en-us/articles/24039793359767).

When you use Claude with the Figma Connector, you can turn prompts into structured diagrams—including flowcharts, decision trees, Gantt charts, sequence diagrams, and state diagrams.

The Claude integration currently supports FigJam only. You can’t use Claude to create files for Figma’s other products.

![A FigJam diagram generated in Claude, with an Edit in Figma button to open the diagram in FigJam.](https://help.figma.com/hc/article_attachments/37883547220631)

Note: This integration behaves different in Claude and Claude Code. In Claude, you can generate diagrams inline and riff on them through additional prompts before opening them in FigJam. In Claude Code, you can generate a FigJam diagram link, but all additional edits happen in FigJam.

## Connect Figma to Claude

To generate FigJam diagrams from Claude, you’ll need to connect your Figma account using the Figma Connector.

To connect Figma to Claude:

1. Open Claude.
2. In Claude, Navigate to [Settings > Connectors](https://claude.ai/settings/connectors).
3. Look for the **Connectors** section and click **Browse connectors**.
4. Select the Figma Connector and click **Connect** to begin the setup process.
5. Follow the authentication prompts to grant Claude access to your account.
6. Configure any specific settings or permissions as needed.

If you don’t have a Figma account, you'll be prompted to [create one](https://help.figma.com/hc/en-us/articles/360039811114-Create-a-Figma-account) when setting up the connection.

Tip: You can also search for Connectors directly from a chat in Claude by clicking the **Search and tools** button on the lower left of your chat interface.

Once connected, Claude can create FigJam files directly in response to your prompts.

Check out the [Claude Help Center](https://support.claude.com/en/articles/11724452-using-the-connectors-directory-to-extend-claude-s-capabilities) to learn more about setting up Connectors.

## Generate FigJam diagrams in Claude

After connecting Figma, you can ask Claude to generate diagrams directly from your conversations.

1. Open a conversation in Claude.
2. Ask Claude to create a diagram. This can be a direct prompt (where you specifically mention Figma or FigJam) or an indirect prompt (where Claude will decide based on context if a FigJam diagram will be useful.). For example:
   - “Create a flowchart for our user onboarding process.”
   - “Turn this PDF into a system architecture diagram in FigJam.”
   - “Use this screenshot to create a process diagram in FigJam.”
3. Claude generates a FigJam diagram based on your prompt and embeds a preview in the conversation.

Tip: If you’re having trouble getting Claude to generate a diagram, try mentioning Figma or FigJam explicitly in your prompt. This is the most reliable way to ensure Claude creates a diagram.

In the embedded view, you can pan, zoom, and open a full-screen view.

### How prompting works

You can provide context in your prompts using:

- Text prompts
- PDFs or documents
- Images or screenshots

Claude analyzes this information and creates a FigJam diagram with shapes, connectors, and labels that represent the concepts you described.

Diagrams generated in Claude are designed to be a structured starting point. You can ask Claude to make broad updates (like changing colors or adjusting the layout) through additional prompts, which update the existing diagram and generate a new preview. You can also ask Claude to regenerate a new diagram, or continue refining layout, content, and visuals directly in FigJam.

## Open and edit the file in FigJam

Select **Edit in Figma** from the embedded preview to continue working in FigJam.

- If you’re signed in to a Figma account, you can claim the file and add it to your drafts (and select a team if you belong to more than one).
- If you’re not signed in, you can log in or create a new account to claim the file and add it to your drafts.

Files created from Claude that haven’t been claimed are public and viewable by anyone with the link. Once you log in, sign up, or add the file to your drafts, it becomes private to you.

Once the file is created in FigJam, it behaves like any other FigJam file—you can move objects, add content, and share it with your team.

Note: We recommend using FigJam on desktop (app or browser). Editing isn't supported on mobile.
