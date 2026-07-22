---
기술지원명: Figma for Government
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Figma for Government
출처링크: https://help.figma.com/hc/en-us/articles/22932461365015-Figma-for-Government
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma Make is now available for Figma for Government. Learn more about [how AI works with the Figma for Government solution](#h_01J0C1R46DM9N2CHD01GJFA76H).

Figma for Government is a solution for government agencies to brainstorm, design, and build digital experiences using Figma.

Figma for Government maintains the following security standards:

- FIPS 140-2 validated encryption
- DNSSEC secure domain name system
- FedRAMP Moderate ATO

If you would like more information, please reach out to [fedramp-interest@figma.com](mailto:fedramp-interest@figma.com) or request our security package on the [FedRAMP Marketplace](https://marketplace.fedramp.gov/products/FR2311345531).

## Features

Figma for Government is available for Figma's products.

Figma for Government gives teams the full capabilities of Figma’s [Enterprise plan](https://help.figma.com/hc/en-us/articles/13840245466391) in a dedicated, government-compliant environment. It’s designed to meet federal security and compliance standards while maintaining the power and flexibility of Figma’s collaborative tools.

To maintain compliance certifications, a few Enterprise features aren’t included:

- [Audio chat](https://help.figma.com/hc/en-us/articles/1500004414622-Use-audio-to-chat-with-your-team)
- [Partner integrations](https://help.figma.com/hc/en-us/sections/360006538974-Integrations-and-applications), such as Figma for Zoom, Figma for Jira, etc.
- [Figma for Government mobile app](#h_01J0C1R46D49V04JM0570XABG6) (secure, but currently not FedRAMP compliant)
- [UI Kits](https://help.figma.com/hc/en-us/articles/24037724065943)
- [Figma AI image, text, and workflow tools](https://help.figma.com/hc/en-us/articles/24039793359767) outside of Figma Make

Additionally, Figma for Government does not have access to features that are [currently in beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

All users using the Figma for Government solution are required to use [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333). This keeps authentication management centralized and secure, while providing a simple login experience for users. Email + password logins and Figma marketplace identity provider applications, such as Microsoft or Okta, are not compatible with Figma for Government.

See a full breakdown of the similarities and differences between Figma’s Enterprise plan and the Figma for Government solution:

### Available design, development, and collaboration features

|  |  |  |
| --- | --- | --- |
|  | **Enterprise plan** | **Figma for Government** |
| File and project organization | [Multiple teams](https://help.figma.com/hc/en-us/articles/360039957374-Get-started-with-organizations) and [workspaces](https://help.figma.com/hc/en-us/articles/4409676189207) | [Multiple teams](https://help.figma.com/hc/en-us/articles/360039957374-Get-started-with-organizations) and [workspaces](https://help.figma.com/hc/en-us/articles/4409676189207) |
| [Version history](https://help.figma.com/hc/en-us/articles/360038006754) | Unlimited | Unlimited |
| [Audio conversations](https://help.figma.com/hc/en-us/articles/1500004414622) | ✓ |  |
| [Auto layout](https://help.figma.com/hc/en-us/articles/5731482952599) | ✓ | ✓ |
| [Components](https://help.figma.com/hc/en-us/articles/360038662654) | ✓ | ✓ |
| [Libraries for components, styles, and variables](https://help.figma.com/hc/en-us/articles/360041051154) | ✓ | ✓ |
| [Variable modes](https://help.figma.com/hc/en-us/articles/14506821864087#variable_modes) | Unlimited modes with [extended collections](https://help.figma.com/hc/en-us/articles/36346281624471) | Unlimited modes with [extended collections](https://help.figma.com/hc/en-us/articles/36346281624471) |
| [REST API for variables](https://www.figma.com/developers/api#variables) | ✓ | ✓ |
| [Prototypes](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma) | ✓ | ✓ |
| [Video in prototypes](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes) | ✓ | ✓ |
| [Variables](https://help.figma.com/hc/en-us/articles/14506587589399), [expressions](https://help.figma.com/hc/en-us/articles/15253194385943), and [conditional logic](https://help.figma.com/hc/en-us/articles/15253220891799) in prototypes | ✓ | ✓ |
| [Inspect design and prototype properties](https://help.figma.com/hc/en-us/articles/360039832014) | ✓ | ✓ |
| [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247) | ✓ | ✓ |
| [Shared fonts](https://help.figma.com/hc/en-us/articles/360039956774) | ✓ | ✓ |
| [Branching and merging](https://help.figma.com/hc/en-us/articles/360063144053) | ✓ | ✓ |
| [Organization-wide design systems](https://www.figma.com/design-systems/) | ✓ | ✓ |
| Community resources like [widgets](https://help.figma.com/hc/en-us/articles/4410047809431-Use-widgets-in-files), [plugins](https://help.figma.com/hc/en-us/articles/360042532714-Use-plugins-in-files), and [files](https://help.figma.com/hc/en-us/articles/360038510873.html) | ✓ | ✓  [with considerations](#h_01J0C1R46DJNAE7ZGKEHE8N3M7) |
| [Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231) | ✓ | ✓ |
| [Figma AI image, text, and workflow tools](https://help.figma.com/hc/en-us/articles/24039793359767) outside of Figma Make | ✓ |  |
| [Figma MCP server](https://help.figma.com/hc/en-us/articles/35280968300439) | ✓ | Desktop MCP only [with considerations](#how-mcp-works) |
| Code Connect | ✓ | ✓ |

### Available security and administration features

|  |  |  |
| --- | --- | --- |
|  | **Enterprise plan** | **Figma for Government** |
| FIPS 140-2 validated encryption |  | ✓ |
| DNSSEC secure domain name system |  | ✓ |
| [Single sign-on (SSO)](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) | ✓ | [Required](https://help.figma.com/hc/en-us/articles/360040532333) |
| [Prototype sharing controls](https://help.figma.com/hc/en-us/articles/360040531773) | ✓ | ✓ |
| [Password protection](https://help.figma.com/hc/en-us/articles/5726720100247-Add-password-protection-to-files) | ✓ | ✓ |
| [Default seat types](https://help.figma.com/hc/en-us/articles/4414038570007-Set-default-roles) | ✓ | ✓ |
| [Design system analytics](https://help.figma.com/hc/en-us/articles/360039238353-View-and-explore-library-analytics) | ✓ | ✓ |
| [Link access controls](https://help.figma.com/hc/en-us/articles/5726756336791) | ✓ | ✓ |
| [Centralized administration](https://help.figma.com/hc/en-us/sections/4403928823063-Teams-libraries-and-resources) | ✓ | ✓ |
| [Plugin and widget management](https://help.figma.com/hc/en-us/articles/4404228724759-Approve-plugins-in-an-organization) | ✓ | ✓ |
| [Domain capture](https://help.figma.com/hc/en-us/articles/360045953273-Domains-and-domain-capture) | ✓ | ✓ |
| [Activity logs](https://help.figma.com/hc/en-us/articles/360040449533-View-and-export-activity-logs) | ✓ | ✓ |
| [Seat assignment via SCIM](https://help.figma.com/hc/en-us/articles/360048787534-Set-member-roles-via-SCIM) | ✓ | ✓ |
| [Restrict access to external content](https://help.figma.com/hc/en-us/articles/12080587805719) | ✓ | ✓ |
| [Disable cursor chat](https://help.figma.com/hc/en-us/articles/14564080039447) | ✓ | ✓ |
| [Guest access controls](https://help.figma.com/hc/en-us/articles/4410793238167-Restrict-or-prevent-guest-access) | ✓ | ✓ |
| [Require password protection on links](https://help.figma.com/hc/en-us/articles/5726756336791#require-passwords) | ✓ | ✓ |
| [Set public links to expire](https://help.figma.com/hc/en-us/articles/16142157359255) | ✓ | ✓ |
| [Workspaces and workspace administration](https://help.figma.com/hc/en-us/articles/7096698154519-Manage-workspaces-in-an-organization) | ✓ | ✓ |
| [Default teams in workspaces](https://help.figma.com/hc/en-us/articles/4419450594455-Set-default-teams-for-workspaces) | ✓ | ✓ |
| [AI admin controls](https://help.figma.com/hc/en-us/articles/17725942479127) | ✓ | ✓ |

### How Figma Make and AI works for Figma for Government

Figma AI helps you work faster and bring ideas to life with products like Figma Make, our prompt-to-app product.

Figma for Government includes access to **Figma Make**, allowing teams to generate functional prototypes using natural-language prompts. [Learn how to get started with Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231).

Figma AI uses a credit system that is shared across all Figma AI features and products as they become available for Figma for Government.

[Learn more about how AI credits are consumed by feature](https://help.figma.com/hc/en-us/articles/33459875669015).

The following details apply specifically to Figma for Government:

- View, Collab, and Dev seats include 500 credits per month. These limits are currently enforced and are subject to change.
- Full seats include 4,250 credits per month. While Full seat users may reach their monthly limit, those limits are not strictly enforced. We’ll provide notice when enforcement begins.
- Additional AI credits are not available for purchase at this time. We’ll share updates if and when purchasing options become available.

There are a few differences for the Figma Make experience for Figma for Government accounts, to meet security requirements:

- [**Figma Make connectors**](https://help.figma.com/hc/en-us/articles/35440096186007): Figma Make connectors to external tools aren’t currently available.
- [**Figma Community**](https://help.figma.com/hc/en-us/articles/360038510693)**:** You can’t publish or remix Figma Make files to or from the public Figma Community.
- [**Some AI models**](https://help.figma.com/hc/en-us/articles/36400680326551): AI models that are not FedRamp compliant are not included in the model selector on Government solutions.
- [**Backend integrations**](https://help.figma.com/hc/en-us/articles/32640822050199): Supabase integrations aren’t currently supported.
- [**Push to GitHub**](https://help.figma.com/hc/en-us/articles/35463818346647)**:** Pushing Figma Make projects to Github is not currently supported.
- [**Apex domains**](https://help.figma.com/hc/en-us/articles/31414274019863): You can publish Figma Make files as a website and choose to give it a custom domain. However, apex domains are not currently supported. For example, [example.com](http://example.com) is an apex domain and not supported, but [www.example.com](http://www.example.com) is a supported www subdomain.

**Controlling AI access for Figma for Government teams or organizations**

Figma for Government includes controls that let admins enable or disable AI features at the organization or workspace level. Organization admins of a Figma for Government organization can enable or disable AI features from your admin settings. [Learn how in this article](https://help.figma.com/hc/en-us/articles/17725942479127).

Figma for Government automatically disables content training, so your team’s content will not be used to train AI models.

### How plugins and widgets work for Figma for Government

Plugins and widgets extend and enhance how you use Figma. Figma for Government users can only access third-party plugins and widgets approved by their organization admins to ensure security. It’s not currently possible to publish private plugins or widgets for those using Figma for Government.

If you need access to a plugin or widget, you can search for it directly within a Figma file and submit a request for approval. Learn more about [finding and running plugins in files →](https://help.figma.com/hc/en-us/articles/360042532714-Use-plugins-in-files#01H8M501RP16VGBZMW99YRY30K).

Admins can approve or deny plugin and widget requests from the **Admin > Resources** tab in their file browser. For more details, see [managing plugin and widget requests →](https://help.figma.com/hc/en-us/articles/4404228724759-Manage-plugins-and-widgets-in-an-organization#h_01HBHE0R6JP5YCPJW3XNZVN3RD).

**Caution:** Figma for Government users cannot request access to a resource directly from the Figma Community ([figma.com/community](http://figma.com/community)). Instead, they can search for the plugin or widget by name from the **Resources** tab of any file.

Users may also experience issues with plugins or widgets that rely on external services. This is because some government organizations enforce firewalls that block access to these services. For example, plugins like Unsplash (which fetches images from unsplash.com) or Jira (which connects to Atlassian's cloud services) may not function properly.

If you encounter issues with a plugin or widget that requires external services, it’s likely due to firewall restrictions. For further assistance, speak with your IT team or reach out to support-figgov@figma.com.

### How the REST API works for Figma for Government

The [Figma REST API](https://developers.figma.com/docs/rest-api/) supports access and interactions with Figma's different products. This gives you the ability to do things such as view and extract any objects or layers, and their properties from files, get usage data, or listen for events with webhooks, among other things.

The primary difference between the common Figma REST API and the Figma for Government version is the base URL you'll use to make requests. For Figma for Government, the base URL is `https://api.figma-gov.com`.

### How the Figma MCP server works for Figma for Government

The [Figma MCP server](https://help.figma.com/hc/en-us/articles/35280968300439) brings context from your Figma files directly into your development environment, helping AI agents generate accurate, design-informed code.

Figma for Government supports the desktop MCP — the same desktop-based flow as the standard Figma desktop MCP, running through the Figma for Government desktop app.

**Note:** MCP services for Figma for Government are not included in the FedRAMP audit.

The following MCP capabilities are not currently available for Figma for Government:

- Remote MCP
- Write to Canvas
- Code to Canvas
- Code Connect UI
- Agent skills

### How the Figma Community works for Figma for Government

The Figma Community is a space where people, teams, and organizations can publish files, plugins, and widgets, and others can duplicate and use them. Community files are snapshots of Figma or FigJam files that have been published to the Community. [Learn more about the Figma Community →](https://help.figma.com/hc/en-us/articles/360038510693-Guide-to-the-Figma-Community)

Figma for Government users cannot directly duplicate Community files.

In order to use files from the Figma Community, Figma for Government users can do the following:

1. Create a free Figma account, not associated with your Figma for Government organization.
2. Open the Community file in that account.
3. [Save the file as a .fig file](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files).
4. Log in to your Figma for Government account and [import the .fig file as a new file](https://help.figma.com/hc/en-us/articles/360041003114-Import-files-to-the-file-browser).

### Using Figma for Government on the Figma desktop app

Figma for Government is supported on the Figma desktop app. The desktop app has been assessed as part of the FedRAMP boundary. Two types of installers are available:

#### Self-updating installers

These versions will automatically check for updates and prompt users when a new version is available:

- [Mac (Apple Silicon)](https://desktop.figma.com/mac-arm/gov/FigmaGov.zip)
- [Mac (Intel)](https://desktop.figma.com/mac/gov/FigmaGov.zip)
- [Windows (Intel)](https://desktop.figma.com/win/gov/FigmaGovSetup.exe)
- [Windows (ARM)](https://desktop.figma.com/win-arm/gov/FigmaGovSetup.exe)

#### Enterprise installers

These versions do not update automatically. Organizations using enterprise deployment tools will need to distribute updates manually:

- [Windows MSI installer feed](https://desktop.figma.com/win/gov/releases.xml)
- [MacOS PKG installer feed](https://desktop.figma.com/mac-universal/gov/releases.xml)

Admins can also find these installers by going to **Admin** > **Settings.**Under **Other**, you can select either the Windows or MacOS Enterprise installer.

**Note:** If your organization is using the Enterprise installers, please work with your IT team to install and manage updates.

The desktop app includes the [Figma font installer](https://help.figma.com/hc/en-us/articles/360039956894). If you see a Chrome prompt asking to “Allow figma.com to look for and connect to devices on your local network,” choose **Allow**. This permission is safe and required for the Figma desktop app to access local fonts, [spell check](https://help.figma.com/hc/en-us/articles/27323589692055), and the ability to [open links in the desktop app](https://help.figma.com/hc/en-us/articles/360039824334).

By downloading a Figma application, you agree that our [Terms of Service](https://www.figma.com/legal/tos/) apply to your use of that application. If you have entered a different agreement with Figma that covers our applications, that agreement will apply instead.

### Download the Figma for Government mobile app

The Figma for Government mobile app is currently secure, but not FedRAMP compliant. A Figma for Government account is required to login to the app.

The Figma for Government mobile app allows you to securely preview designs and prototypes, leave comments, and manage file permissions directly from your iOS and Android devices.

- Securely access Figma Design files, FigJam boards, and Slides decks
- Review comments and reply to feedback on the go
- Mirror your designs from desktop to your mobile device
- Validate prototyping flows and interactions

The features in the Figma for Government mobile app are consistent with the [Figma mobile app](https://help.figma.com/hc/en-us/articles/1500007537281), with the exception that the Figma for Government mobile app does not offer multi-account support and push notifications at this time.

You can download the Figma for Government mobile app from the App Store or Play Store:

- [Download the Figma for Government for iOS and iPad.](https://apps.apple.com/us/app/figma-for-government/id6756397299)
- [Download the Figma for Government for Android.](https://play.google.com/store/apps/details?id=com.figma.mirror.gov&hl=en_US)

**Note**: The mobile app allows you to edit FigJam boards if using an iPad device. A desktop device is needed to edit other file types.

## Administration and billing

The Figma for Government plan is paid for annually, in advance. To learn more, review your order form or [contact our sales team](mailto:fedramp-interest@figma.com) for more information.

Since the Figma for Government billing and total number of seats are handled in advance, admins will not need to manage billing tasks within the product.

However, admins in your organization will still be able to use Figma’s admin settings to perform actions related to how seats, files, and your organization are used and managed, such as [managing files and projects](https://help.figma.com/hc/en-us/sections/360006050633-Manage-files-and-projects), [managing teams](https://help.figma.com/hc/en-us/sections/360006457394-Manage-a-team), and [using the file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser).

**Note:** To successfully access a Figma for Government organization as a guest, guests must first be invited via the organization’s Members page before being invited to any other resources, such as workspaces, teams, files, or projects.

## Migrate to Figma for Government

### Set up SAML SSO (required)

Setting up SAML SSO is the first step of your Figma for Government implementation and should be completed within the first week of getting started.

All users of the Figma for Government solution are required to use SAML SSO. This keeps authentication centralized and secure while providing a simple login experience for users. Email + password logins and identity provider applications like Microsoft or Okta are not compatible with Figma for Government.

You can follow the step-by-step directions to set up SAML SSO in our [guide to SAML SSO →](https://help.figma.com/hc/en-us/articles/360040532333).

**Note:** You'll also need to designate someone to be an organization admin. Organization admins are members with extra administrative rights within the organization. Every organization must have at least one organization admin. [Learn how to make someone an organization admin](https://help.figma.com/hc/en-us/articles/4420115581079).

### Using magic links to sign in

While configuring SAML SSO, users can sign in to Figma for Government using magic links. Magic links are one-time, short-lived access to link to sign in to your Figma for Government organization. If you’ve been invited to the organization under **Admin > Members** and SAML has not yet been enabled, you will receive a one-time access link to sign in via email.

Magic link sign ins will be disabled once SAML is fully configured. Ensure that all users have been assigned Figma via SAML SSO before enabling for your organization. However, guests can continue using magic link sign ins unless they belong to another Figma for Government organization that has SAML enabled.

### Moving to Figma for Government from an existing Figma account

You can migrate content from an existing Figma account to your Figma for Government account by exporting and re-uploading files.

1. [Save a copy of the design files to your computer](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files) from your existing Figma account.
2. [Import the files](https://help.figma.com/hc/en-us/articles/360041003114-Import-files-to-the-file-browser) to your Figma for Government account.

Migrated files do not carry over:

- Version history or comments
- Existing sharing permissions
- Library component references

Along with migrating content to the Figma for Government solution, also have your IT team allow <http://figma-gov.com/> over port 443 to avoid firewall issues.

## Get support with Figma for Government

Browse [Figma Learn](https://help.figma.com/hc/en-us) for more information about Figma’s features. Generally, all articles related to the Enterprise plan are relevant to Figma for Government users, with the exception of:

- Audio chat
- Partner integrations
- Figma mobile app
- UI Kits
- Billing management, which is not applicable to Figma for Government administration

To get in touch with our support team, please use our dedicated email for Figma for Government users at [support-figgov@figma.com](mailto:support-figgov@figma.com)

Please be mindful to avoid including sensitive information when submitting support requests to the above address.
