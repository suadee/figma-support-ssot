---
기술지원명: Use verified partner MCP connectors with the Figma agent and Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Use verified partner MCP connectors with the Figma agent and Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/35440096186007-Use-verified-partner-MCP-connectors-with-the-Figma-agent-and-Figma-Make
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

The Figma agent and Figma Make can connect to external tools via the [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP), allowing you to work with documents, tasks, and data from other apps as context for your designs, apps, and prototypes.

![User prompts Figma Make to fetch and implement Dog & Bean Club PRD from Notion; tasks confirmed via notion-search and notion-fetch MCP tools.](https://help.figma.com/hc/article_attachments/35704752258455)

For example, you might connect Figma Make to Notion to import a product requirements document (PRD) directly into Figma’s chat and ask Make to use it as the source for building a prototype. If the PRD changes, simply run the connector again to refresh the context and update the prototype. You can also write content back to Notion—like generating a list of acceptance criteria—by [enabling the write tools in the connector’s settings](#h_01KAC4Y0E7GCJ7SQMS7GRW2H1P).

**What’s the difference between MCP connectors in Figma and the Figma MCP server?**

When you connect external tools in the agent or Figma Make, it acts as an **MCP client**. The client calls tools hosted on an **MCP server**—for example, the Notion or Asana connectors—to read or write data from that source. Based on your prompt, the agent decides which connector and tools to use.

By contrast, the [Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server) includes a list of tools that makes your file data available to other MCP clients.

## Add a connector

Each person needs to add and authenticate the connectors they’d like to use.

To add a connector, you’ll first need to authenticate. For example, when adding Notion, you’ll select your workspace and approve access permissions.

1. From the chat box, click  **Add context.**
2. Select  **Connectors** .
3. Browse the list of available connectors.
4. Click **Connect** next to the connector you want to use.
5. Follow the prompts to authenticate through the external tool’s OAuth flow.
6. Once connected, click  **Add context** to confirm the connector appears in the list.

**Tip**: If you don't see a prompt to authenticate, your browser may be blocking popups. Check your browser's address bar for a popup blocker icon and allow popups for Figma.

**Note:** If **Connectors** isn't an option in the menu, an admin may have [disabled this feature for your organization](https://help.figma.com/hc/en-us/articles/36343926263703).

## Use a connector in chat

![](https://help.figma.com/hc/article_attachments/38194020077975)

When a connector and its tools are enabled for the current chat, you can call it naturally within the flow of conversation.

1. To explicitly reference a connector in your prompt, type **@** in the chat to see a list of your connected connectors. Select the one you want to use, and it will appear as a pill above your message. This makes sure the agent only uses specific connectors for the current task.
2. Type a prompt that references the connector. For example, paste an Asana link and write "Use the specs in this project to create a first-draft prototype".
3. If your prompt requires a connector, the agent will show which connector and tool it plans to call and ask for consent. Click **Run** to proceed. You can [manage individual tools and their permissions from the connector settings](#h_01KAC4Y0E7GCJ7SQMS7GRW2H1P).

If the source content changes, just run the connector again to pull in the latest context.

## What featured connectors are available

Figma currently supports a limited set of verified connectors. These featured MCP servers have been vetted by our team to ensure they meet Figma’s security and privacy standards.

**Note**: You must have an account with the external service to use the related connector. Availability may depend on your plan, seat, role, or access within that service.

Figma provides the following featured connectors:

[Amplitude](#h_01KHC3VXX371CHYQDMDGQ4J943)[Asana](#h_01KAC6008DSVC6P4G7NGZNSX02)[Askable](#h_01KS6KE7MNASR0CDAA0PWH0Y6)[Atlassian](#h_01KAC61FJH0T48NNGG73QYFMRM)[Box](#h_01KHC3VXX3RSNEVBC6D3Y3B4H2)[Contentsquare](#h_01KK8YK46QYJS3P048E1HZ7BF)[Dovetail](#h_01KHC3VXX3S44QQXD5NNC2V30H)[Granola](#h_01KHCJ6YM9XX59NBVC74BWABA8)[GitHub](#h_01KAC61CP6A0QVY74P65S8GPJ0)[Hex](#h_01K1W5HQ0T4VF2QGPN3BJKX9J)[Linear](#h_01KAC616NCHWS8BRDXY0953QN6)[Marvin](#h_01KHC3VXX35GTFKPH4PGNVQMX8)[monday.com](#h_01KAC619KR0N0AV4GK6AGKW284)[Notion](#h_01KAC5ZX2T66T1G5XTAPZZB9YN)[Slack](#h_01KJK9D238A1941N00SGRVQHA)[Sprig](#h_01KJB9QTRHRD3YB8J9YM9B01T)[Twilio](#h_01KPG45QZM04Z5169QPDPJHZ2)[Zapier](#h_01KPV7NRXXMGJ1G5H920XBXCE5)[zeroheight](#h_01KHC3VXX38F547B8TYRAP13GS)

**Tip**: Need to connect to an MCP server that’s not on this list? You can [create your own custom MCP connector](https://help.figma.com/hc/en-us/articles/38147204302743).

#### **Amplitude**

- Access Amplitude user trends, funnels, and experiments within Figma to generate designs and prototypes with product context.
- Create and test design variants to track impact on user behavior.

#### **Asana**

- Access Asana tasks and projects from Figma to track progress and team priorities in real time.
- Create and manage Asana tasks, so you can keep projects aligned from concept to completion.

#### **Askable**

- Access your research findings from Askable inside Figma.
- Query your evidence and ground prototypes in what verified participants actually said and did.

#### **Atlassian**

- Access and edit Confluence pages and documentation directly from Figma to keep specs, decisions, and design work connected.
- Access, create, and transition Jira issues and epics without context switching, so teams can move smoothly from design to development.
- Access, create, and update Compass components, services, and scorecards to keep designs and prototypes linked to your engineering ecosystem.

#### **Box**

- Access hubs and content from Box during your design process, while enforcing existing Box security and access policies.
- Extract key insights and query all of your content, to ground your prototypes in your enterprise context.

#### **Contentsquare**

- Access Contentsquare analytics from Figma, including user journeys, funnels, and page metrics.
- Query how people use your live product to ground design decisions in real behavior. The connector is read-only.

#### **Dovetail**

- Access Dovetail customer data in Figma to inform design decisions.
- Search across your Dovetail workspace to find relevant projects, data and docs.

#### Granola

- Connect Figma to your meeting history in Granola
- Search through your meeting notes, find specific topics discussed in past meetings, extract action items or decisions from your notes, answer questions based on your meeting history and more.

#### **GitHub**

- Access public or private GitHub repositories, issues, and pull requests to keep design work tied to your codebase.
- Create and summarize GitHub issues and PRs from within Figma, so design changes translate directly into development action.

#### **Hex**

- Bring in Hex dashboards and data apps, and ask data questions via Hex threads.
- Build data into your presentations, designs, and boards.

#### **Linear**

- Access Linear issues, projects, and documents from Figma to generate designs and prototypes with relevant context.
- Create and manage Linear issues and projects, so you can turn your designs and prototypes into planned work.

#### **Marvin**

- Access Marvin directly within Figma to ground your designs in real user feedback and data.
- Generate summaries of customer knowledge, so you can design with confidence and validate prototypes faster.
- Requires Marvin Enterprise plan and Contributor or Admin role in Marvin.

#### **monday.com**

- Access monday.com boards and items from Figma to stay aligned with team planning and priorities.
- Create and manage updates, so your work stays visible and connected across every team.

#### **Notion**

- Access Notion pages and databases directly from Figma to bring context, specs, and notes into your design flow.
- Create and update Notion docs, so your design documentation stays organized and always in sync.

#### **Slack**

- Search and read Slack messages, threads, channels, users, and files.
- Take action by sending messages and creating canvases and channels.

#### **Sprig**

- Access customer surveys within Figma to ground designs and prototypes in evidence.
- Create and launch Sprig studies to test designs, concepts, and prototypes created with Figma and measure how users respond to them.

#### **Twilio**

- Access Twilio's API documentation from Figma to build communication features like messaging, voice, and verification into your prototypes.
- Generate accurate, up-to-date code for Twilio APIs without leaving your design flow. The connector provides API knowledge and does not send messages or access your account data.

#### Zapier

- Connect to Google Drive, Microsoft Office, Zoom, Jira, HubSpot, Slack, and 9,000+ other apps through a single connection.
- Bring the context from your tools directly into your design and prototyping workflow: pull a requirements doc, a spreadsheet with real data, or meeting summaries. Then go further and create tasks, send messages, and trigger workflows across your entire tool stack from a single prompt.

#### **zeroheight**

- Power Figma with design system context from your zeroheight styleguide to generate on-system prototypes in seconds
- Use the Figma to stress-test your zeroheight docs. AI misinterpretations can reveal unclear guidance and help you prioritize improvements.
- Requires zeroheight Enterprise plan and access to the DS team with an Editor or Admin seat. Documentation viewers can [create a custom connector](https://help.figma.com/hc/en-us/articles/38147204302743) to access the zeroheight MCP server.

**Note**: Interested in connecting your product to Figma? We’re currently collecting expressions of interest for new partnerships. If that sounds like you, please [share a few details about your product and use case with us](https://form.asana.com/?k=34zEs7g-ootZdNmVYtSiaQ&d=10497086658021).

## Manage connector settings

![Notion connector settings in Figma Make showing read tool permissions for workspace integration.](https://help.figma.com/hc/article_attachments/36444591030807)

Some connectors include multiple MCP tools. These tools perform different functions within the connector, such as fetching data, sending updates, or managing content.

You can control which tools are available in Figma; for example, you may want to allow a tool that fetches content, but disable tools that send content back to the external source.

**Note:** Tools that can write to external sources are disabled by default. You’ll need to manually enable them before you can send content back to the connected service.

You can also control each tool’s permissions within a connector. The available options are:

| Setting | How it works | When to use it |
| --- | --- | --- |
| **Ask to run** | Figma always asks your permission before running the tool | You want control every time the agent runs a tool in the conversation |
| **Always run** | Figma runs the tool when needed without asking for permission | You trust the external source and the available data |
| **Never run** | Figma won’t attempt to run the tool | Use this setting for tools you don’t need; it can help speed up Figma AI by giving it a smaller set of tools to choose from |

**Caution**: Be wary of prompt injections from external sources when pulling in context.

You can also temporarily disable connectors to ensure they aren’t used in the current conversation.

1. From the chat box, click  **Add context.** Hover over  **Connectors**, then select  **Manage.**
2. Click **Manage** on the connector.
3. Enable or disable the read or write tools, or set permissions for individual tools within that connector.

**Tip**: Only enable the relevant connectors—and their tools—to help the agent work faster.

## Disconnect a connector

Disconnecting a connector stops the Figma agent and Figma Make from reading or writing data through it. It doesn’t delete any data in the external tool, and you can reconnect later by adding and authenticating it again.

1. From the chat box, click  **Add context.** Hover over  **Connectors**, then select  **Manage.**
2. Click **Manage** on the connector.
3. At the bottom of the modal, click **Disconnect**.
