---
기술지원명: Guide to merging organizations
카테고리: 관리
작성자: Figma
승인자: suadee
출처: Guide to merging organizations
출처링크: https://help.figma.com/hc/en-us/articles/13843533972119-Guide-to-merging-organizations
게시일: 2026-07-22
검토일: 2026-07-22
---

## 내용

Before you start

Who can use this feature

Available on the
[Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Only organization admins can request merges

Working with Figma’s support team, you can merge the users, files, projects,
teams, and plugins from one Figma organization into another.

During a merge, one organization becomes the **parent**, and the
other the **child**.

- The **parent** organization keeps its existing users, content
  and settings.
- All users and content from the **child** organization move into
  the parent organization. At the end of the process, Figma removes the child
  organization.

## What happens during a merge?

- All
  [domains](https://help.figma.com/hc/en-us/articles/360045953273)
  associated with the child organization are added to the parent organization.
- Figma automatically prefixes teams from the child organization with the child
  organization name. For example: `Acme-[team name]`.
- All users from the child organization keep their existing
  [seat types](https://help.figma.com/hc/en-us/articles/360039960434)
  when joining the parent organization, unless they are explicitly restricted
  in the parent organization.
- All users from the child organization have their
  [customized sidebars](https://help.figma.com/hc/en-us/articles/12399143113111)
  reset to a default state.
- Organization admins in the child organization become members in the parent
  organization.
- [Activity logs](https://help.figma.com/hc/en-us/articles/360040449533)
  from the child organization are not included in the merge and are deleted
  after the merge is complete.
- Shared fonts from the child organization are not included in the merge and
  will need to be re-added to the parent organization.
- If the parent organization is on the Organization plan and the child organization
  is on the Enterprise plan, any active Enterprise plan features will get deactivated
  and won't be available after the merge.
- If the parent organization is on the Enterprise plan with
  [guest controls enabled](https://help.figma.com/hc/en-us/articles/4410793238167),
  guests in the child organization won't get included in the merge. We
  recommend manually inviting guests to the parent organization before
  the merge.
- If both organizations are on the Enterprise plan with workspaces enabled,
  workspaces in the child organization won't be included in the merge. All
  teams and users from the child organization will move to
  **Unassigned** in the parent organization.
- During the merge process, users in the parent organization may temporarily see a message indicating an update is in progress. This is expected and will resolve once the merge is complete.

## What happens after a merge is complete?

- The parent organization’s settings will apply, including those for domain
  capture, SAML, SCIM, public links, and approved plugins.
- Users from the child organization will need to login with the parent organization’s
  identity provider and will use the parent organization moving forward.

## Things to check before requesting a merge

- Will users from the child organization be able to authenticate using the
  parent organization’s identity provider? If login via SSO is enforced on
  the parent organization, users who join the organization via a merge might
  not be able to sign in if they haven't been provisioned with access to Figma
  through your identity provider. If the parent organization uses SCIM to create
  users, we recommend discussing your options with our team.
- Will you need to bulk update users’ email addresses as part of this process?

## Request a merge

To request a merge, please email `admin-support@figma.com` with the
following:

- Any questions about the merge behavior detailed above.
- An organization admin from both organizations copied on the thread.
- The URL and name of both organizations and which is the parent organization
  and child organization.
- Will users from the child organization be able to authenticate using the
  parent organization’s identity provider?
- Will you need to bulk update users’ email addresses as part of this process?

Please note we need approval from organization admins at both organizations to
start a merge.

Tip: Here’s how to get the URL of your organization:

1. Log in to your organization in a web browser.
2. From the
   [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **All teams** or **All workspaces**.
3. Copy the entire URL in your browser address bar.
