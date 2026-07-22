---
기술지원명: Create FigJam diagrams with Slackbot
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Create FigJam diagrams with Slackbot
출처링크: https://help.figma.com/hc/en-us/articles/41842203241623-Create-FigJam-diagrams-with-Slackbot
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on all Figma plans

You can connect Figma to Slackbot to generate FigJam diagrams directly from your Slack conversations.

When connected, Slackbot can turn messages, threads, channels, and canvases into a structured FigJam diagram — no need to leave Slack to start a new file.

This integration currently supports FigJam. You can't use it to create files for Figma Design, Figma Slides, or Figma's other products.

## Connect Figma to Slack

If your workspace doesn't already have the Figma app installed, a workspace owner will need to add it first. To connect Figma to Slack:

1. Go to the Figma app page in the Slack Marketplace, or search for **Figma** from the Apps section in Slack.
2. Select **Add to Slack**.
3. Follow the authentication prompts to sign in and grant access to your Figma account. Once connected, open Slackbot and mention `@Figma` to generate a diagram.

**Note:** If the Figma app was installed to your Slack workspace before June 18, 2026, a workspace owner needs to re-authorize the app before members can use the diagram generation feature.

## Generate FigJam diagrams from Slackbot

After connecting Figma, you can ask Slackbot to create a diagram directly from your conversation.

To generate a diagram:

1. Open Slackbot from your Apps section, or DM it directly.
2. Mention `@Figma` followed by a description of the diagram you want to create.
3. Reference a specific message, thread, or canvas if you want Slackbot to use it as context.
4. Slackbot generates a FigJam file and replies with a link to open it.

**Example prompts:**

- "`@Figma` create a flow chart for a user signup and login flow. Include account verification and two-factor authentication."
- "`@Figma` turn this Slack canvas into a flowchart for our customer onboarding process."
- "`@Figma` use this thread to create a process diagram in FigJam."

Slackbot can create structured diagrams like flowcharts, Gantt charts, sequence diagrams, and state diagrams based on your prompt and any referenced Slack content.

The generated file is designed to be a structured starting point. You can continue refining layout, content, and visuals directly in FigJam.

## Open and edit the file in FigJam

When Slackbot generates a diagram, it creates a new FigJam file in your Figma account and shares a link in Slack.

To continue editing:

1. Click the link Slackbot provides.
2. If you're signed in, the file appears in the drafts of your selected team.
3. If you're not signed in, you'll be prompted to log in or create a Figma account to claim the file.

Files that haven't been claimed are public and viewable by anyone with the link. Once you log in, sign up, or add the file to your drafts, it becomes private according to your sharing settings.

Once created, the file behaves like any other FigJam file. You can:

- Move and edit objects
- Add sticky notes, shapes, and connectors
- Invite collaborators
- Share with your team

**Note:** We recommend using FigJam on desktop (app or browser). Editing isn't supported on mobile.

## Stay on top of Figma activity in Slack

Beyond generating diagrams, the Figma app for Slack keeps your team updated on design work happening across Figma and FigJam. You'll get notified when:

- You're tagged in a file
- Someone replies to one of your comments
- New comments are made in files you're subscribed to
- You're invited to a new file
- When a user requests a seat upgrade (admins only)

You can reply to file comments directly from Slack, and choose to receive notifications in real time or as hourly or daily digests.

To get updates in a specific channel, [add Figma to any Slack channel](https://help.figma.com/hc/en-us/articles/360039829154#h_01FXKNJK0DF0DCSGM0V73V9EM0).
