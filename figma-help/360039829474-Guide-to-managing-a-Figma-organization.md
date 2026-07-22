---
기술지원명: Guide to managing a Figma organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Guide to managing a Figma organization
출처링크: https://help.figma.com/hc/en-us/articles/360039829474-Guide-to-managing-a-Figma-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

This guide is for customers on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Organization admins only

Organization admins have an extra item in their file browser sidebar called **Admin.** This is where you can manage high-level settings for your Figma organization, including:

- [Access](#h_01H00W4P0DQANRCBTNQC5SYTPG)
- [Members and guests](#h_01H00W4W9GQG51RM75QDBF2E9Y)
- [Teams](#h_01H00W5FXJZ4CKCFKVZFNP13J5)
- [Resources like fonts, plugins, and libraries](#h_01H00W5NTPBXN101AZ3PQRHHBS)
- [Workspaces (Enterprise plan only)](#h_01H00W5AAWS238MN5TP0M4MMP7)
- [Billing groups (Enterprise plan only)](#h_bg)
- [Additional security and privacy controls](#h_01H00W5WPDEPSWB8JYGHD3WSYM)
- [Billing](#h_01H00W62B6PWSN652QTV1HR5PR)

## Manage access to the organization

### **Claiming domains**

[Domain capture](https://help.figma.com/hc/en-us/articles/360045953273) lets you automatically add people with a company email address—like `@example.com`—to your Figma organization.. This helps admins keep all users at the company within a single Figma organization.

### Login and authentication

You can enable single sign-on (SSO) with an identity provider (IdP), and choose how users authenticate themselves.

- [Set login and authentication method](https://help.figma.com/hc/en-us/articles/360052497994)
- [Guide to SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333)

### Provisioning with SCIM

Figma supports SCIM provisioning, making it easier to manage large teams or changes in team membership. With SCIM, you can synchronize user data, such as names and emails, between your IdP and Figma. On the Enterprise plan, you can also set [seat types](https://help.figma.com/hc/en-us/articles/360039960434) using SCIM, which gives admins more control over cost changes between billing cycles.

- [Set up automatic provisioning via SCIM](https://help.figma.com/hc/en-us/articles/360048514653)
- [Set seat types via SCIM](https://help.figma.com/hc/en-us/articles/360048787534-Set-member-roles-via-SCIM)\*

\**Only available on the Enterprise plan*

## Manage members and guests

The  **People** tab is where you can view activity, manage access, and [review paid licenses](https://help.figma.com/hc/en-us/articles/360040328293) for every member and guest in your organization.

**Manage members and guests**

- [View members and guests](https://help.figma.com/hc/en-us/articles/4420842863255)
- [Manage seats in an organization](https://help.figma.com/hc/en-us/articles/360052677454.html)
- [Set approval settings for new seats](https://help.figma.com/hc/en-us/articles/4414038570007-Set-default-roles)
- [Manage drafts of deleted members](https://help.figma.com/hc/en-us/articles/4420549259799.html)
- [Remove people from an organization](https://help.figma.com/hc/en-us/articles/360040453453)
- [Make someone an organization admin](https://help.figma.com/hc/en-us/articles/4420115581079)
- [Add or remove workspace admins](https://help.figma.com/hc/en-us/articles/4409605157143.html)

**Manage guest-specific controls**

- [Invite guests to organization resources](https://help.figma.com/hc/en-us/articles/4410795216791)
- [View guest access](https://help.figma.com/hc/en-us/articles/4420556737175)
- [Restrict or prevent guest access](https://help.figma.com/hc/en-us/articles/4410793238167)\*
- [Accept guest access requests](https://help.figma.com/hc/en-us/articles/4420542281495)\*

**Tip**: Use the [Activity log](https://help.figma.com/hc/en-us/articles/360040449533) to review how people in the organization interact with files and resources.

## Manage teams

Organization admins can manage all open and visible teams, as well as any hidden teams they have been invited to.

- [Manage teams in an organization](https://help.figma.com/hc/en-us/articles/360053463173)
- [Manage who can create a team in an organization](https://help.figma.com/hc/en-us/articles/10386065399319)\*

\**Only available on the Enterprise plan*

## Manage resources

Resources like plugins, widgets, libraries, and fonts help streamline design and collaboration. You can also manage publishing for products like Figma Sites and Figma Make, and whether backend integration is implemented. You can control how these resources are used to match your company’s security and privacy requirements.

**Plugins and widgets**

Plugins and widgets are third-party scripts or applications that extend the functionality of Figma Design and FigJam.

- [Create private organization plugins](https://help.figma.com/hc/en-us/articles/4404228629655)
- [Manage plugins and widgets in an organization](https://help.figma.com/hc/en-us/articles/4404228724759-Approve-plugins-in-an-organization)
- [Save plugins for the organization](https://help.figma.com/hc/en-us/articles/4404239055127-Save-plugins-for-the-organization)

**Libraries**

As an organization scales, it can have tens, hundreds, or even thousands of published libraries available. Figma has several different ways organization and workspace admins can help people surface and use the best libraries for their work:

- [Manage a library for a workspace or organization](https://help.figma.com/hc/en-us/articles/21310245473815)

**Tip**: Every member of an organization, including organization admins, can [view library analytics](https://help.figma.com/hc/en-us/articles/360039238353-View-and-explore-library-analytics) to understand how libraries are used across the organization.

\**Only available on the Enterprise plan*

**Fonts**

Figma organizations can upload and share custom fonts to specific teams or across the organization. This removes the need to share, install, or update fonts for individual users. It also allows people using Chromebooks and Linux to access custom fonts.

- [Upload custom fonts to an organization](https://help.figma.com/hc/en-us/articles/360039956774-Upload-custom-fonts-to-an-organization)

**Publishing**

Figma Sites and Figma Make provide a way to publish sites, functional prototypes, and web apps to the public web. When published, individuals outside your organization can discover and interact with the published resources. You can control whether it's possible for these resources to be published to the public web. On the Enterprise plan, you can also require passwords on published sites and apps, and configure publishing settings at the workspace level.

- [Manage web publishing for an organization](https://help.figma.com/hc/en-us/articles/31242876956183)

**Backend integration**

When working with Figma Make, your users can integrate a backend in their files. The backend allows the functional prototypes and web apps created with Figma Make to do things like maintain an app's state across browsers, provide authentication flows, and store secrets, API keys, and tokens that are needed to make requests to different servers. You can manage whether Figma Make files are able to be integrated with a backend.

- [Manage backend integration for an organization](https://help.figma.com/hc/en-us/articles/34162517434007)

**Connecting to external data sources in Figma Make**

By default, members of your organization can [connect to external data sources via the Model Context Protocol (MCP) in Figma Make](https://help.figma.com/hc/en-us/articles/35440096186007). As an organization admin, you can disable these connectors to control data access while keeping Make-powered workflows available.

- [Manage connectors in Figma Make](https://help.figma.com/hc/en-us/articles/36343926263703)

## Manage workspaces

Workspaces are collections of teams, people, and resources within a Figma organization. They help companies with many business units, sub-brands, or design systems add structure to their Figma organization. Workspaces are only available on the **Enterprise plan** and are managed by [workspace admins](https://help.figma.com/hc/en-us/articles/4420557724439).

- [Launch workspaces in your organization](https://help.figma.com/hc/en-us/articles/4409676189207.html)\*
- [Manage workspaces in an organization](https://help.figma.com/hc/en-us/articles/7096698154519.html)\*

\**Only available on the Enterprise plan*

## Manage billing groups

Billing groups let you sort people in your organization according to internal budget sources. Each billing group has [billing group admins](https://help.figma.com/hc/en-us/articles/4420557724439) who manage free and paid seats in the group. Billing groups are only available on the **Enterprise plan**.

- [Launch billing groups in your organization](https://help.figma.com/hc/en-us/articles/19100885191191)\*
- [Manage billing groups in an organization](https://help.figma.com/hc/en-us/articles/19100486415255)\*

\**Only available on the Enterprise plan*

## Additional security and privacy controls

The security and privacy of your organization is extremely important to us. Figma has different controls for keeping your data secure:

- [Restrict access to content from outside your organization](https://help.figma.com/hc/en-us/articles/12080587805719-Restrict-access-to-content-from-outside-your-organization)\*
- [Require link expiration on design files](https://help.figma.com/hc/en-us/articles/5726756336791)\*
- [Require password protection on files](https://help.figma.com/hc/en-us/articles/5726756336791-Manage-public-link-sharing#require-passwords)\*
- [Disable open sessions in FigJam](https://help.figma.com/hc/en-us/articles/5726756336791)
- [Disable public links](https://help.figma.com/hc/en-us/articles/5726756336791)
- [Enable or disable audio for organization](https://help.figma.com/hc/en-us/articles/4420953557399-Enable-or-disable-audio-for-organization)
- [Disable cursor chat](https://help.figma.com/hc/en-us/articles/14564080039447)

\**Only available on the Enterprise plan*

## Manage billing

Figma has multiple products: Figma Design, FigJam, Dev Mode, and Figma Slides.

You assign a single seat for each user on your plan, and the seat type determines which products they have access to. Keep in mind that when you change someone’s seat type, you might also be changing their billing status.

- [Guide to billing at Figma](https://help.figma.com/hc/en-us/articles/29717597009431-Guide-to-billing-at-Figma)
- [Manage seats at Figma](https://help.figma.com/hc/en-us/articles/360039960434)
- [Manage billing on the Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328293)
