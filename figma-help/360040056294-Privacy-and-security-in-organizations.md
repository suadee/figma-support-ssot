---
기술지원명: Privacy and security in organizations
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Privacy and security in organizations
출처링크: https://help.figma.com/hc/en-us/articles/360040056294-Privacy-and-security-in-organizations
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only organization admins can manage an organization's security settings.

Organizations give you greater control over what's shared within your business.

## Privacy and security by design

Security is part of everything we do. It’s top of mind in how we work, treat customer data, and develop our product.

Figma has completed a **SOC 2 Type II audit**. SOC 2 is a security compliance standard for software companies in the United States. Its guidelines and policies help businesses, like Figma, [protect customer data](https://www.figma.com/blog/keeping-your-data-in-figma-safe-and-secure/#we-re-ready-for-our-european-customers).

Learn more about Figma's [Privacy](https://www.figma.com/privacy/) and [Security](https://www.figma.com/security/) policies.

## File and draft ownership

The organization has ownership over all the files created within the organization. This includes files within a member's drafts. When you [remove a member,](https://help.figma.com/hc/en-us/articles/360040453453) all their teams, files and projects will stay in the organization.

Figma will also move files in a deleted member's drafts to a shared folder in the organization. Organization admins can [access these files and delete or redistribute them](https://help.figma.com/hc/en-us/articles/4420549259799).

## Configure share settings in a file

There are a few ways members can get access to files in an organization:

- A member invites them to the file
- They are a member of the team or project
- They open a link to a Figma file (link sharing)

Use link sharing settings to define who can open the file, and whether they have view or edit access. This includes members of the organization and guests outside of the organization. Guests of an organization can only access files and teams to which they have been invited. [Learn more about managing public link sharing and open sessions.](https://help.figma.com/hc/en-us/articles/5726756336791)

You can update the link sharing settings for each file. The default settings are **Anyone at organization with link** and **can view**.

### Who can access the file

To open the share modal from any file, open the file and click **Share** in the top-right.

- Choose  **Anyone** to allow people inside and outside the organization to access the file. This includes both members of the organization and Guests who have the link.
- Choose  **Organization** access to allow anyone in the organization to access the file. Use this setting for library files you want to share with the whole organization. Guests of the organization won't be able to access these files unless you invite them to the file or team.
- Choose  **Only invited people** if you only want team members or people you explicitly invite to the file to access it.

### What can they do

Choose what level of access other members of the organization have, once they open the file.

- Choose **can edit** to give anyone who opens the file the option to edit.
- Choose **can view** to allow people to view the file without being able to make any edits.

![The share settings modal allows you to choose who can view or edit this file.](https://help.figma.com/hc/article_attachments/31530004504599)

To choose your organization's prototype access level, [open the prototype](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes) and click **Share prototype** in the top right to make those changes.

It's possible to disable public link sharing in an organization. This prevents anyone outside the organization from accessing files via the file link.

Organization admins can turn link sharing off and on on the **Settings** tab of the organization's Admin. [Learn more about organization admin.](https://help.figma.com/hc/en-us/articles/360039829474-Guide-to-Organization-Admin#Settings)

## Permissions

In an organization, every member and guest has a [seat type](https://help.figma.com/hc/en-us/articles/360039960434) that determines which Figma products they can access.

In a team, [permissions](https://help.figma.com/hc/en-us/articles/360039960434) determine how members can interact with its files and projects.

- [Register official company domains](https://help.figma.com/hc/en-us/articles/360045953273-Manage-domain-capture-for-an-organization) for email addresses
- [Invite members to your organization](https://help.figma.com/hc/en-us/articles/360040453113-Add-members-or-guests-to-an-organization) as members or guests. Guests can only access resources you invite them to.
- Set and update permissions at any time.
- Set different levels of [organization access levels](https://help.figma.com/hc/en-us/articles/360040452973) for teams.

[Learn more about permissions in an organization.](https://help.figma.com/hc/en-us/articles/360039960434)

## Activity logs

Activity Logs provide a record of how users are interacting with files and resources. This allows you to track what's happening within your organization:

- See who is accessing, copying and sharing Files
- Track changes made to teams, projects and file permissions
- View activity for individual members
- Track changes made by organization admins
- Identify and prevent misuse of organization Resources

[Learn more about activity logs](https://help.figma.com/hc/en-us/articles/360040449533).

## SAML SSO

Organizations that need enhanced security requirements can configure SAML SSO.

**Security Assertion Markup Language (SAML)** is a security standard for logging into applications.

**Single Sign On (SSO)** allows users to log into many applications or websites via one set of login details.

Figma has integrations with the following providers:

- [Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413)
- [Okta](https://help.figma.com/hc/en-us/articles/360040532353)
- [OneLogin](https://help.figma.com/hc/en-us/articles/360040533373)
- [Google Workspace](https://help.figma.com/hc/en-us/articles/360040047614-Authenticate-with-Google#SAML-SSO)

You can also [set up a custom SAML configuration](https://help.figma.com/hc/en-us/articles/360040047774) with a provider that isn't on this list.

[Learn more about SAML SSO.](https://help.figma.com/hc/en-us/articles/360040532333)

## Two-factor authentication

If you don't have SAML or Google SSO enabled, members of your organization can add extra security via two-factor authentication (2FA).

When enabled, members will need to confirm their identity every time they log in to Figma.

Members will need to set this up individually, in their account **Settings**. There isn't a way to enable 2FA or make it mandatory across an entire organization.

If you're using SAML SSO, you may be able to enable 2FA with your identity provider.

[Learn more about two-factor authentication.](https://help.figma.com/hc/en-us/articles/360039817634)

## Restricted access

Enterprise organizations can [restrict access to external content](https://help.figma.com/hc/en-us/articles/12080587805719) to prevent data loss.

[Learn more about additional security controls for your organization.](https://help.figma.com/hc/en-us/articles/360039829474-Guide-to-managing-a-Figma-organization#h_01H00W5WPDEPSWB8JYGHD3WSYM)
