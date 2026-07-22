---
기술지원명: Manage MCP connectors for the Figma agent and Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage MCP connectors for the Figma agent and Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/36343926263703-Manage-MCP-connectors-for-the-Figma-agent-and-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma agent is currently available to try for free in open beta. [Learn more.](https://help.figma.com/hc/en-us/articles/34932042346775)

Who can use this feature

Available on [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Members of your organization can use connectors in the Figma agent and Figma Make to access external data sources via the Model Context Protocol (MCP). There are two types of connectors available:

- [**Featured connectors**](https://help.figma.com/hc/en-us/articles/35440096186007) are integrations vetted by Figma and include MCP servers from Notion, Asana, Linear, GitHub, Atlassian, and more.
- [**Custom connectors**](https://help.figma.com/hc/en-us/articles/38147204302743) let users connect to any MCP server, including internal tools and private data sources. These connectors aren’t vetted by Figma. By default, only organization admins can create custom connectors, but you can change this setting to allow members to create them as well. [Learn more about security best practices for creating custom connectors.](https://help.figma.com/hc/en-us/articles/38147204302743)

### How it works

- If [AI features are disabled](https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization#h_01J0SNQBZ9JXM4T45V5QWZ2QFZ) in your organization, connectors aren’t available in the agent and Figma Make.
- Organization admins can enable or disable featured connectors and custom connectors for the entire organization. Workspace-level controls aren’t yet available on the Enterprise plan.
- When a connector type is disabled, all related UI elements for adding or managing that connector type are removed.
- Disabling either type of connector immediately prevents new connections to the associated third-party data sources. Previous tool calls are hidden from chat history, but any data already used in a file remains. For example, a dashboard created using a Notion or Asana connector will continue to display existing data even after the connector is disabled.
- Only admins can [publish custom connectors](#h_01KH7HNZC3FN8TRAX46X0XF3BC) to make them available organization-wide.

## Enable or disable featured connectors

[Featured connectors](https://help.figma.com/hc/en-us/articles/35440096186007) are vetted integrations maintained by Figma's partners. To enable or disable featured connectors:

1. From the file browser, click  **Admin**, then select  **Settings**.
2. Go to the **AI** section and click **MCP connectors in Figma**.
3. Toggle **Allow featured connectors** on or off.

**Caution**: Changes to this setting take effect immediately for all files in your organization. The setting can’t be applied at the workspace or team level.

## Enable or disable custom connectors

[Custom connectors](https://help.figma.com/hc/en-us/articles/38147204302743) let users connect to any MCP server beyond Figma’s partner integrations, including public servers or private internal tools.

For example, if a product manager wants to reference content from a tool that isn’t supported by featured connectors, they can connect to that tool using its MCP server.

**More details:**

- When **Allow custom connectors** is enabled, you can control who can create them—whether that's admins-only or everyone in the organization
- Custom connectors are visible only to their creator unless published organization-wide.
- Only organization admins can publish custom connectors

To enable or disable custom connectors:

1. From the file browser, click  **Admin**, then select  **Settings**.
2. Go to the **AI** section and click **MCP connectors in Figma**.
3. Toggle **Allow custom connectors** on or off.
4. If needed, update **Who can create connectors** to **Anyone in the organization**, or **Admins only**.

**Caution:** Changes to this setting take effect immediately for all files in your organization.

## Publish a custom connector to your organization

As an organization admin, after you [create and connect a custom connector](https://help.figma.com/hc/en-us/articles/38147204302743), you can publish it to everyone in the organization.

![](https://help.figma.com/hc/article_attachments/38515235577751)

Once published, a connector appears in the connector modal under the tab with your organization name. If authentication is required, users can do so with their own API keys or OAuth tokens.

**More details:**

- Users can access the full set of read and write tools exposed by the MCP server and can enable or disable individual tools as needed.
- Only the organization admin who publishes a connector can unpublish it.
- When you publish a custom connector that uses [custom request headers](https://help.figma.com/hc/en-us/articles/38147204302743), the headers are published with it. Individual users won’t need to provide their own credentials.

### Publish a connector

1. In the prompt box in a chat, click  **Add context**, then  **Connectors**.
2. Go to the **Created by you** tab. If it’s empty, you’ll need to [create a custom connector](https://help.figma.com/hc/en-us/articles/38147204302743) first.
3. If needed, click **Connect** to ensure the connector shows a **Connected** status.
4. Click  **Connector options**, then select **Publish.**
5. Review the connector details, check the confirmation box, then click **Publish.**

The connector will immediately appear for all users in your organization.

**Note**: After publishing, you can edit the connector’s name, icon, tagline, and description—all without needing to republish. [Learn more about editing a connector.](https://help.figma.com/hc/en-us/articles/38147204302743)

### Unpublish a connector

Unpublishing a connector removes it for all users except the organization admin who published it. All files using the connector will lose access to its tools. [Deleting a custom connector](https://help.figma.com/hc/en-us/articles/38147204302743) will also unpublish it.

1. In the prompt box in a chat, click  **Add context**, then  **Connectors**.
2. Go to the tab with your organization’s name.
3. Click  **Connector options** for the custom connector you want to unpublish.
4. Select **Unpublish.**
