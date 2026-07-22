---
기술지원명: Create and use custom MCP connectors in the Figma agent and Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Create and use custom MCP connectors in the Figma agent and Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/38147204302743-Create-and-use-custom-MCP-connectors-in-the-Figma-agent-and-Figma-Make
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

Custom connectors allow you to connect the Figma agent and Figma Make to any remote [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) server. This lets you use data from external apps as context for your app or prototype. You can connect to public MCP servers or to your own private internal servers.

For example:

- Use a company’s official MCP server that isn’t on [Figma’s list of verified partner servers](https://help.figma.com/hc/en-us/articles/35440096186007)
- Use an open source MCP server when a company hasn’t released an official one
- Connect to a private documentation or design systems server

### Before you begin

Before creating a custom connector, you'll need:

- The MCP server URL, like `https://company.com/mcp`. If you're new to MCP servers, see the [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/getting-started/intro).
- A name, icon, and description for the connector.
- A plan for authentication. Custom connectors support [multiple authentication methods](#h_01KH7K1NXAMBWQNFRZA2TSXFD3) for connecting to third-party MCP servers.

## Create a custom connector

A custom connector is visible only to its creator. On Organization and Enterprise plans, admins can [publish custom connectors to the organization](https://help.figma.com/hc/en-us/articles/36343926263703).

1. In the prompt box in a chat, click **Add context.** Hover over  **Connectors**, then select **Manage.**
2. Navigate to the **Created by you** tab and click  **Create.**
3. Enter a **Name**. The **Icon**, **Tagline**, and **Description** fields are optional.
4. Enter the **MCP server URL**, then click **Create**. If you leave **Advanced settings** empty, Figma attempts to authenticate using the server’s supported method. If needed, click **Advanced settings** and enter the relevant details to [customize authentication](#h_01KH7K1NXAMBWQNFRZA2TSXFD3).
5. Click **Connect** on the connector to authenticate.
6. Review the available **Read** and **Write** tools and enable the ones you want to use.
7. Test your connector by [using it in a chat](#h_01KH7K1NXANCDX2EW0SH5129JD).

**Note:** On Organization and Enterprise plans, if you don’t have the option to **Add connector**, an admin may have [disabled this feature for your organization](https://help.figma.com/hc/en-us/articles/36343926263703).

## Use a custom connector in chat

You can use custom connectors you’ve created, or—on the Organization and Enterprise plans—connectors that have been [published to your organization by an admin](https://help.figma.com/hc/en-us/articles/36343926263703).

![](https://help.figma.com/hc/article_attachments/38515162046487)

When a connector and its tools are enabled for the current chat, you can call it naturally within the conversation.

1. To explicitly reference a connector, type **@** in the chat to see a list of connected connectors. Select the one you want to use and it will appear as a pill above your message. This ensures the agent only uses the specified connectors for the current task.
2. You can also enter a prompt that references the connector. For example, paste an Asana link and write "Use the specs in this project to create a first-draft prototype".
3. If your prompt requires a connector, the agent shows which connector and tool it plans to call and asks for consent. Click **Run** to proceed. You can [manage individual tools and their permissions from the connector settings](https://help.figma.com/hc/en-us/articles/35440096186007#h_01KAC4Y0E7GCJ7SQMS7GRW2H1P).

If the source content changes, just run the connector again to pull in the latest context.

**Note:** The tools available depend on what your MCP server provides. You can view and manage available tools in the connector settings.

## Manage a custom connector

![](https://help.figma.com/hc/article_attachments/38515191178263)

### Edit a custom connector’s details

1. From the chat box, click **Add context.** Hover over  **Connectors**, then select **Manage.**
2. Navigate to the **Created by you** tab and click  **More** on the connector.
3. Click **Edit**.
4. Update the name, icon, tagline, description, or custom headers, then save your changes.

### Edit a custom connector’s tools

Some connectors include multiple MCP tools that perform different actions, such as fetching data, sending updates, or managing content.

You can control which tools are available in Figma. For example, you might enable tools that fetch content while disabling tools that write back to the external source.

**Note:** Tools that can write to external sources are disabled by default. You must manually enable them before you can send content back to the connected service.

Each tool supports the following permission settings:

| Setting | How it works | When to use it |
| --- | --- | --- |
| **Ask to run** | Figma always asks your permission before running the tool | You want control every time the agent runs a tool in the conversation |
| **Always run** | Figma runs the tool when needed without asking for permission | You trust the external source and the available data |
| **Never run** | Figma won’t attempt to run the tool | Use this setting for tools you don’t need; it can help speed up the agent by giving it a smaller set of tools to choose from |

**Caution**: Be wary of prompt injection risks when pulling in context from external sources.

1. From the chat box, click **Add context.** Hover over  **Connectors**, then select **Manage.**
2. Navigate to the **Created by you** tab and click **Manage** on the connector.
3. Enable or disable the **Read** or **Write** tools, or set permissions for individual tools within that connector.

### Disconnect a custom connector

Disconnecting a connector stops Figma from reading or writing data through it. It doesn’t delete the connector or any data in the external tool, and you can reconnect later by re-authenticating.

1. From the chat box, click **Add context.** Hover over  **Connectors**, then select **Manage.**
2. Navigate to the **Created by you** tab and click **Manage** on the connector.
3. At the bottom of the modal, click **Disconnect**.

### Delete a custom connector

Deleting a connector disconnects it and removes it from the **Personal** tab. You won’t be able to reconnect to the MCP server without creating the connector again.

1. From the chat box, click **Add context.** Hover over  **Connectors**, then select **Manage.**
2. Navigate to the **Created by you** tab and click  **More** on the connector.
3. Click **Delete** and confirm your choice.

## Supported authentication methods

Custom MCP connectors support the following authentication methods. The best option depends on how your server manages access and permissions.

### OAuth 2.0 (default)

If the MCP server supports OAuth, the agent uses the server's declared OAuth flow by default.

- You authorize access through a standard OAuth flow after creating the connector
- Permissions are determined by the provider's default OAuth behavior

**Best for:** Quick setup where default OAuth permissions are sufficient.

**Note:** When registering your OAuth app, enter `https://www.figma.com/oauth/mcp/callback` as the callback URL.

### OAuth with client credentials

Uses OAuth with a **client ID** and **client secret** from your own OAuth app.

- You authorize access by providing credentials from the service you're connecting to
- You typically control scopes, permissions, and access rules

**Best for:** Working with sensitive data sources where access needs to be controlled.

**Note:** When registering your OAuth app, enter `https://www.figma.com/oauth/mcp/callback` as the callback URL.

### Custom request headers

Uses static headers sent with every request to authorize.

- You provide API keys or personal access tokens when creating the connector
- No OAuth flow is required; credentials are attached directly to requests

**Best for:** Servers that don't support OAuth, including internal services, or machine-to-machine authentication.

**Note:** When an organization admin [publishes a custom connector](https://help.figma.com/hc/en-us/articles/36343926263703) that uses custom request headers, the headers are published with it. Individual users won't need to provide their own credentials.

### No authentication

Some MCP servers don't require authentication.

- Requests are sent without credentials
- Access control, if any, is handled entirely by the server

**Tip:** We recommend reviewing the MCP server’s documentation to determine the appropriate authentication method.

| If the docs say… | Best authentication method |
| --- | --- |
| • Log in with… • Sign in… • Authorize | OAuth 2.0 |
| • Create an OAuth app… • Client ID • Client secret | OAuth with client credentials |
| • API key • Personal access token • Send this header with every request… | Custom request headers |

### Security best practices

When creating custom connectors, we recommend following a few security best practices:

- Only connect to MCP servers you own or trust completely. Wherever possible, use official servers and check the [list of verified partner connectors.](https://help.figma.com/hc/en-us/articles/35440096186007)
- Understand which tools are available and what data the server can read or write
- Prefer OAuth authentication over embedding credentials in URLs
- Never share OAuth client secrets in public repositories or documentation

## Troubleshooting

Why isn’t my connector doing anything?

If your connector connects successfully but doesn’t respond in chat, make sure at least one tool is enabled and is set to **Ask to run** or **Always run**.

Why am I getting errors from my server?

If your server requires API keys, personal access tokens, or non-default OAuth scopes, you must [configure authentication](#h_01KH7K1NXAMBWQNFRZA2TSXFD3) in **Advanced settings** before connecting. You may need to contact the server owner to get the information you need.

- If your server expects API keys, use **Custom headers**
- If your OAuth provider requires scopes, use OAuth with client credentials

Why didn’t the agent pull from my connector?

If Figma AI doesn’t use your connector automatically, try explicitly referencing it with **@[Connector name]** in the chat.

Why can’t I connect to my local MCP server?

The Figma agent and Figma Make don't support local (`localhost`) or `stdio` MCP servers. Custom connectors must connect to a publicly accessible MCP server over HTTPS. If you’re testing locally, deploy your MCP server to a hosted environment with a secure URL before connecting it to Figma.
