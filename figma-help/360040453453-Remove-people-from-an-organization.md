---
기술지원명: Remove people from an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Remove people from an organization
출처링크: https://help.figma.com/hc/en-us/articles/360040453453-Remove-people-from-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

On the Organization plan, only organization admins can remove members and guests from the organization

On the Enterprise plan, organization admins, billing group admins, and workspace admins can remove members and guests from the organization

Removing people from an organization prevents them from accessing any teams, projects, files, libraries, and other resources in the organization.

- **Organization** admins can remove any member or guest
- **Billing group admins** can only remove people from billing groups they manage
- **Workspace admins** can only remove people from workspaces they manage

## What to expect

Figma uses  [organization domains](https://help.figma.com/hc/en-us/articles/360045953273) to determine who can join an organization. Members are accounts with email addresses that match an organization domain. Guests are accounts with external email addresses and can still access their Figma account outside the organization. This includes any other teams or organizations they belong to.

### Existing teams, files and projects

When you remove a member, Figma keeps their contributions to organization teams, projects, and shared files.

While not required, we recommend you **transfer ownership** of the member's teams and projects before you remove them.

- [Change the owner of a team](https://help.figma.com/hc/en-us/articles/360039481134)  
  If you don't transfer ownership of a team before removing the team owner from your organization, the team won't have an owner. Organization admins can claim ownership of the team from the **Teams** tab in **Admin**. Team admins can continue to manage a team regardless of whether there is an owner assigned.
- [Transfer ownership of projects](https://help.figma.com/hc/en-us/articles/360038512093)  
  If you don't transfer ownership of **projects** before removing the owner, they won't have a new owner until one is assigned.

**Note**: When a member is removed, their files will not be given a new owner. Any person with `can edit` access to the files can continue to make changes or move them.

### Drafts

When you remove a member or guest from your organization, their [draft files become accessible to organization admins in **Admin**](https://help.figma.com/hc/en-us/articles/4420549259799). This helps prevent important work from getting lost when someone leaves.

### Drafts in teams outside the organization

What happens to a member’s teams and drafts in Starter or Professional teams outside the organization depends on the organization's [domain capture](https://help.figma.com/hc/en-us/articles/360045953273) and SAML SSO settings.

- **Domain capture on:** Members will no longer have access to the Figma account under their company email. They will lose access to their drafts and any teams, files, and projects in teams outside the organization.
- **Domain capture off:** Figma detaches their email address from the organization. This allows them to keep a Figma account registered under their company email. They won’t be able to access the organization, but may be able to access drafts, teams, and projects in teams outside the organization.
- **SAML SSO on:** If you remove members from your identity provider, they won’t be able to log in to Figma using their company email. They won’t be able to access anything in their organization or teams outside the organization.

## Remove a user in Figma

Organization admin Billing group admin Workspace admin

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Click the  **People** tab.
3. Use the search field to find the member or guest.
4. Click  and select **Remove**.
5. Check the box next to **I understand that this action isn't reversible** and click **Remove member**.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Select the relevant billing group in the sidebar.
3. Use the search field to find the member or guest.
4. Click  and select **Remove**.
5. Check the box next to **I understand that this action isn't reversible** and click **Remove member**.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Select the relevant workspace in the sidebar.
3. Select the  **People** tab.
4. Use the search field to find the member or guest.
5. Click  and select **Remove**.
6. Check the box next to **I understand that this action isn't reversible** and click **Remove member**.

## Remove a user via SAML SSO or Google SSO

If your organization members are configured via SAML SSO, you will also need to remove the user from your [identity provider](https://help.figma.com/hc/en-us/articles/360040532333).

This isn't something that we can help you with directly, but we've rounded up some documentation from our supported providers below.

- Microsoft Entra ID (formerly Azure Active Directory): [How to create, invite, and delete users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users) (third-party documentation)
- OneLogin: [Suspending or Deleting Users in OneLogin](https://onelogin.service-now.com/support?id=kb_article&sys_id=b75a9d43db109700d5505eea4b961976) (third-party documentation)
- Okta: [Deactivate and delete users accounts](https://help.okta.com/en/prod/Content/Topics/users-groups-profiles/usgp-deactivate-user-account.htm) (third-party documentation)
- GSuite: [Delete a user from your organization](https://support.google.com/a/answer/33314?hl=en) (third-party documentation)

**Note:** If you remove or deprovision a user via your identity provider, this may prevent them from accessing any Starter or Professional teams they've joined outside the organization.
