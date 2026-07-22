---
기술지원명: Add members or guests to an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Add members or guests to an organization
출처링크: https://help.figma.com/hc/en-us/articles/360040453113-Add-members-or-guests-to-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

There are a few ways to add members and guests to an organization:

- Domain capture: all Figma accounts with company emails are added to the organization
- Invite members or guests to teams, projects, or files
- Add members to the organization
- Add members to your identity provider (SAML SSO)

Some methods are only available to members of the organization and not guests.

|  |  |  |
| --- | --- | --- |
|  | Members | Guests |
| [Domain capture](#domain-capture) | ✓ | ✕ |
| [Add to the organization](#add) | ✓ | ✕ |
| [SAML SSO](#SAML-SSO) | ✓ | ✕ |
| [Invite to team, project, or file](#invite-resource) | ✓ | ✓ |

**Members** have an email address that matches any of the [organization's verified domains](https://help.figma.com/hc/en-us/articles/360045953273). Members can access shared resources in the organization, including teams, fonts, libraries, and plugins.

**Guests** are external users with an email address outside the organization. They can be contractors, agencies, clients, or external collaborators with external email addresses. Guests can only access the resources you explicitly invite them to.

## Domain capture

[Domain capture](https://help.figma.com/hc/en-us/articles/360045953273) makes sure anyone using Figma with a company email gets added to your organization. This applies to anyone with any existing Figma account, as well as anyone who creates a new Figma account using their company email.

## Invite people to teams, projects, or files

Invite a member or guest to a file, project, or team to add them to your organization. Any member or guest can invite someone to a resource at or below their permission level.

For example: someone with view access can only invite others with view access. Someone with edit access can invite someone with view or edit access.

- [Invite collaborators to a team](https://help.figma.com/hc/en-us/articles/360039481034)
- [Invite someone to a project](https://help.figma.com/hc/en-us/articles/360040530313#project)
- [Invite a collaborator to a file](https://help.figma.com/hc/en-us/articles/360040530313)

## Add to the organization

[Organization admins, billing group admins, and workspace admins](https://help.figma.com/hc/en-us/articles/4420557724439) can also invite members to the organization from **Admin**. Organization admins can also invite guests directly to the organization if the [guest membership setting](https://help.figma.com/hc/en-us/articles/4410793238167-Restrict-or-prevent-guest-access) is set to **Guests can only join the organization with admin approval**.

Figma will give everyone you invite via this process a [View](https://help.figma.com/hc/en-us/articles/360039960434#viewer) seat. You can update their seat type once they've accepted their invite.

Organization admins Billing group admins Workspace admins

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the sidebar.
2. Select the  **People** tab.
3. Click **Invite users** to open the invite modal.
4. Enter the member's company email address, choose their [seat](https://help.figma.com/hc/en-us/articles/360039960434), and click **Send invite**.
5. Figma will send an invite email to the member's email address.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the sidebar.
2. Select the relevant billing group in the sidebar.
3. Click **Add members** to open the invite modal.
4. Switch to the **Invite users** tab.
5. Enter the member's company email address, choose their [seat](https://help.figma.com/hc/en-us/articles/360039960434) and click **Send invite**.
6. Figma will send an invite email to the member's email address.

**Note**: Users will automatically get added to the billing group you invite them from.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the sidebar.
2. Select the relevant workspace in the sidebar.
3. Click **Add members** to open the invite modal.
4. Switch to the **Invite users** tab.
5. Enter the member's company email address, choose their [seat](https://help.figma.com/hc/en-us/articles/360039960434), and click **Send invite**.
6. Figma will send an invite email to the member's email address.

**Note**: Users will automatically get added to the workspace you invite them from.

## Add to identity provider (SAML SSO)

If you have configured SAML SSO in your organization, you can add members to your identity provider. When added to your identity provider, Figma will create a provisional account for them.

The documentation below has detailed instructions on how to add members to your identity provider:

- [Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413)
- [OneLogin](https://help.figma.com/hc/en-us/articles/360040533373)
- [Okta](https://help.figma.com/hc/en-us/articles/360040532353)
- [Google](https://help.figma.com/hc/en-us/articles/360040047614)
