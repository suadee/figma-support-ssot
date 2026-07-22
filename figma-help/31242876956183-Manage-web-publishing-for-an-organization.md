---
기술지원명: Manage web publishing for an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage web publishing for an organization
출처링크: https://help.figma.com/hc/en-us/articles/31242876956183-Manage-web-publishing-for-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Figma offers two products that lets users with a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434) publish to the web:

- [Figma Sites](http://figma.com/sites) enables designers, marketers, and developers to build and publish high-quality websites, such as blogs, landing pages, and project showcases.
- [Figma Make](http://figma.com/make) is a prompt-to-app tool that turns ideas or Figma designs into interactive web apps and UI. Users can ideate, iterate, and publish by prompting AI or editing code directly.

By default, users can choose whether to publish their site or app on the open web, or restrict them to an internal audience. When publishing internally, members must be logged into your Figma organization to view the content.

For added security, admins on the Organization and Enterprise plans can disable external publishing entirely. On the Enterprise plan admins can also require passwords for all externally published sites and apps, or configure web publishing settings at the workspace level.

## Disable web publishing

When web publishing is disabled, members of your Figma organization can publish sites and apps so they are accessible only within the organization:

- **Logged in members** of your organization will be able to seamlessly access the site or app at its published domain URL
- **Logged out members** of your organization will need to log into Figma before they can access the site or app
- **Guests** or **people outside your organization** will not be able to access published sites or apps

Internal publishing is always enabled and cannot be turned off.

**Tip**: To help employees access internally published sites and apps, we recommend [enabling single sign on](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) and:

- [Enforce SSO for members](https://help.figma.com/hc/en-us/articles/360052497994-Set-login-and-authentication-method#:~:text=Enforce%20SAML%20SSO,to%20access%20Figma)
- [Set up SCIM with auto provisioning](https://help.figma.com/hc/en-us/articles/360048514653-Set-up-automatic-provisioning-via-SCIM)
- Assign Figma to all employees in your identity provider

When you disable web publishing, any currently published sites and web apps in your organization with the audience set to **Anyone on the web** will switch to your organization only. To disable web publishing, follow these steps:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin**.
2. Select the **Settings** tab.
3. In the **External access** section, click **Web publishing** and disable the feature.

## Require password protection on published sites and apps Enterprise

![](https://help.figma.com/hc/article_attachments/34669424178583)

When web publishing is enabled, admins can require a password for every published site or app.

With password protection, visitors must enter a password to view the content—including metadata like the page title or description. Members of your organization won't be able to publish their sites or web apps without adding a password. They also won't be able to publish their files to Community.

**Note:** Password protection applies only to the published version of the site or app at its \*.figma.site domain. The preview version—which displays with a Figma header at the top—is not password protected and follows standard file sharing permissions.

**Tip**: For stronger security, you can also [require auto-generated passwords](https://help.figma.com/hc/en-us/articles/5726756336791-Manage-public-link-sharing-and-open-sessions#h_01HES8ZXMPX8566YPJZFF4G6SN) rather than letting users pick their own.

To require password protection:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Settings** tab.
3. In the **External access** section, click **Web publishing**.
4. With web publishing enabled, click **Require passwords for publishing**, then press **Save**.

**Caution**: Enabling this setting affects currently published sites and apps:

- Any published sites or apps that don’t already have password protection will be immediately unpublished. People with edit access to the file will be prompted to add a password and republish when they next open the file.
- Any sites or apps [published to Community](https://help.figma.com/hc/en-us/articles/360040035974)—including those with password protection—will be immediately unpublished.

## Configure web publishing for a workspace Enterprise

On the Enterprise plan, you can override the organization-level web publishing setting for specific workspaces.

By default, all workspaces inherit the organization-level web publishing setting. When you add an explicit setting for a workspace, it overrides the organization default for all Sites and Make files in that workspace.

When you change the organization-level setting later, workspaces with an explicit override keep their override unchanged. Workspaces without an override automatically adopt the new organization setting.

To set up web publishing settings for a workspace:

1. From the file browser, click  **Admin**.
2. Select the  **Settings** tab.
3. In the **External access** section, click **Web publishing**.
4. In the **Web publishing settings** modal, under **Custom settings for workspaces**, search for and select a workspace.
5. Toggle **Publishing to anyone on the web** on or off for that workspace.
   - If enabled, choose whether to **Require passwords for publishing** or **Allow publishing without passwords**.
6. Click **Save**.

To remove a workspace override and return it to the organization default, select the workspace from the custom settings list and click **Remove custom settings**.

When a Sites or Make file moves to a workspace with a stricter publishing setting, its publish state automatically changes to match the new workspace:

- **Moving to a workspace with publishing disabled:** If the file is published to anyone on the web, it converts to internal publishing only.
- **Moving to a workspace that requires password protection:** If the file doesn't already have a password, it's immediately unpublished. People with edit access are prompted to add a password and republish when they next open the file.
