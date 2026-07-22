---
기술지원명: Invite guests to organization resources
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Invite guests to organization resources
출처링크: https://help.figma.com/hc/en-us/articles/4410795216791-Invite-guests-to-organization-resources
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

 

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

**Guests** are external users with email addresses that doesn't match any of the [organization's domains](https://help.figma.com/hc/en-us/articles/360045953273). They could be contractors, agencies, clients, or external collaborators.

Guests have limited access to the organization. They can't browse organization teams or [access shared resources](https://help.figma.com/hc/en-us/articles/360052679454) like fonts, plugins, or library analytics. You can only invite guests to individual teams, projects, and files in the organization.

## Guest access

Guests can have the same seat types and team permissions as members.

- **Seats**: Guests can have any [seat type](https://help.figma.com/hc/en-us/articles/360039960434): Full, Dev, Collab, or View. [Seat approval settings](https://help.figma.com/hc/en-us/articles/4414038570007) apply to guests.
- **Permissions:** You choose their permissions when you invite them to a file, project, or team. You can give them different permissions on different resources.

Note: On the Enterprise plan, organization admins can [restrict or disable guest access](https://help.figma.com/hc/en-us/articles/4410793238167). If guest access is restricted, workspace or organization admins need to approve guests before they can access any resources.

## Invite guests

Invite someone from outside your organization to a file, project, or team. They'll only be able to access the specific resources you invite them to.

You can only invite someone at or below your permission level on the resource. For example, if you have view access, you can only invite someone with view access. If you have edit access, you can invite someone with either view or edit access.

You also must have [explicit permissions to a resource](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions) in order to invite someone to it.

### Team

[Invite them to a team](https://help.figma.com/hc/en-us/articles/360039481034) to give them access to all files and projects in that specific team. They can only access and use libraries shared within that team.

1. Open the team in the [file browser](https://help.figma.com/hc/en-us/articles/360041003114).
2. Click **Share**.

### Project

Invite them to a project to give them access to files in that project. Permissions determine what level of access they have on those files.

1. Open the team in Figma.
2. Select the project to view.
3. Click the **Share** button in the menu bar.

### File or prototype

[Invite them to a file or prototype](https://help.figma.com/hc/en-us/articles/360040531773). If you invite them to the file, they can view any prototypes in that file. If you invite them to the prototype, they can only access the prototype.

- With the file or prototype open, select **Share** in the toolbar.
- From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), right-click on the file or prototype and select **Share**.

### Confirm guest details

1. Enter the collaborator's email address in the **Email** field. To invite multiple people, enter their email addresses separated by a comma.

   **Tip:** Figma will identify any email addresses with external domains as a (guest). You'll see this next to their email address when inviting them.
2. Select the [permissions](https://help.figma.com/hc/en-us/articles/1500007609322) you want to give them.
   - Select **Can view** to give them view access.
   - Select **Can edit** to give them edit access.
3. Click **Send invite**.

If your organization is on the Enterprise plan, the organization's guest membership setting will let you know if you can invite external users. There are three options:

1. If there are no restrictions, Figma will ask you to confirm the external invite. Select **Share** to confirm and send an invite email to the guest.
2. If admin approval is required, Figma will still send an invite to the external guest. To accept the invite and view the file/project/team, the guest needs to then request access.

   This sends a request to workspace admins (Enterprise only) and organization admins, which they can **Dismiss** or **Add**. If the request is approved, the guest can reload the page to access the resource.

   Figma will also send them an email to let them know they've been added to the organization.
3. If guest access is disabled, an email won't be sent. Figma will let you know that the external user can't be invited to the resource.

![The invite guest dialog depends on the guest membership setting](https://help.figma.com/hc/article_attachments/4421251597719)
