---
기술지원명: Members versus guests
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Members versus guests
출처링크: https://help.figma.com/hc/en-us/articles/4420557314967-Members-versus-guests
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Supported on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273).

Everyone in an organization has an **account type**. A person's account type determines what they can access within the organization.

This includes organization-wide resources, like teams, libraries, plugins, and widgets. It also includes features and functionality, like branching, library analytics, and shared fonts.

There are two main account types we’ll explore in this article: **members** and **guests**.

![Visualization of difference between members and guests](https://help.figma.com/hc/article_attachments/4421067473559)

**Note:** Another type of account in Figma is an admin. Admins are members with extra administrative rights within the team or organization. [**Admins in Figma →**](https://help.figma.com/hc/en-us/articles/4420557724439)

## Members

Members are people in the organization that have an email address that matches any of the [organization's domains](https://help.figma.com/hc/en-us/articles/360045953273).

> Twigma has the `twigma.com` and `dev.twigma.com` domains registered to their organization. Anyone that joins the organization with a Twigma email address, for example: `name@twigma.com` or `name@dev.twigma.com`, is a member.

Members can access teams, libraries, and other resources shared within the organization.

- View and explore visible organization teams
- Access teams open to the organization or request to join visible teams set to **Only those invited**
- View activity for other members and guests
- Access styles and components from organization-wide libraries
- View library analytics (for libraries they can access)
- Access shared fonts in organization files
- Use private plugins in organization files

A member’s [seat type](https://help.figma.com/hc/en-us/articles/36003996043), and their [permissions on individual teams](https://help.figma.com/hc/en-us/articles/360039970673), impact how they can interact with those resources.

There are a few ways to add members to the organization:

- Add them to the organization itself
- Invite them to a specific team, project, or file
- Import members with existing Figma accounts using [domain capture](https://help.figma.com/hc/en-us/articles/360045953273)
- Provision and authenticate users via SAML SSO

📖   [**Add organization members →**](https://help.figma.com/hc/en-us/articles/360040453113)

## Guests

Guest refers to anyone in the organization that doesn't have a company email. They are external users with email addresses that don't match any of the organization's domains. They could be contractors, agencies, clients, or external collaborators.

> Twigma has the `twigma.com` domain registered to their organization. They work with an agency called DsgnSystm who they invite to a specific team in the organization. Collaborators from the agency have `dsgnsystm.com` emails, not `twigma.com` emails, so they are guests. They can't access any teams or resources outside the team they’re invited to.

Guests have limited access to the organization. They can only access the resources you invite them to. They can't browse organization teams or access shared resources like fonts, plugins, or library analytics.

Set permissions when [inviting guests to a team, file, or project](https://help.figma.com/hc/en-us/articles/4410795216791). Like members, they can have different permissions on each resource. Guests can also have any seat type.

Organization admins can [set seat approval settings](https://help.figma.com/hc/en-us/articles/4414038570007) for anyone joining the organization. Seat approval settings apply to both members and guests.

**Caution:** It's not possible to make a guest into a member. People need to have a email address that matches an [organization domain](https://help.figma.com/hc/en-us/articles/360045953273) to be a member.

| Action | Guests | Members |
| --- | --- | --- |
| Log in using SAML SSO | ✕ | ✓ |
| Access teams, projects, or files they have been invited to | ✓ | ✓ |
| Invite other members and guests to resources (if guest access is permitted) | ✓ | ✓ |
| Join FigJam open sessions | ✓ | ✓ |
| Access FigJam or Figma Design files via link sharing | Files set to Anyone with a link only | Files set to either Anyone with link, Anyone at organization, or Anyone at organization with link |
| View other members and guests | ✕ | Can search for members and guests in the organization |
| View all visible organization teams | ✕ | ✓ |
| Access or request to join organization teams | ✕ | ✓ |
| Create new teams in the organization | ✕ | ✓ |
| Use organization-wide libraries | If invited to source file | ✓ |
| Use an organization’s private plugins | ✕ | ✓ |
| Use organization shared fonts | ✕ | ✓ |
| View library analytics (for files they can access) | ✕ | ✓ |
| Be a team admin of an organization team | ✓ | ✓ |
| Publish to Community as organization | ✕ | ✕ |
| Become an organization admin | ✕ | ✓ |
