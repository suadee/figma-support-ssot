---
기술지원명: Guide to sharing and permissions
카테고리: 관리
작성자: Figma
승인자: suadee
출처: Guide to sharing and permissions
출처링크: https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions
게시일: 2026-07-22
검토일: 2026-07-22
---

## 내용

Sharing in Figma lets you collaborate across teams, projects, and files. This guide gives you a high-level overview of how sharing and permissions work.

## What can you share?

You can share different kinds of assets in Figma: **files**, **prototypes**, **projects** and **teams**. If you're part of an organization, you can also invite people to the **organization**.

You can think of these as different levels of sharing—with the team or organization as the highest level and a file or prototype as the lowest or most granular.

In most circumstances, giving someone access at one level gives them access to the level below it.

For example: if you invite someone to a team, they’ll have access to the projects and files in that team, based on the permissions you give them (`can view` or can `edit`). If you invite someone to a specific file, but not the team, they get access to just that file but no other team projects and files.

![A visual hierarchy of resources in Figma: prototypes in files, which are in projects, which are in teams, which are in organizations.](https://help.figma.com/hc/article_attachments/35463302908055)

## How can you share?

There are three main methods for sharing resources in Figma:

- [Share a link to a resource](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions#links)
- [Invite people to a specific resource](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions#invite)
- [Embed a file or prototype outside of Figma](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions#embeds)

| **Method** | **Organization** | **Team** | **Project** | **File** | **Prototype** |
| --- | --- | --- | --- | --- | --- |
| Invite | [Only if domain capture is off](https://help.figma.com/hc/en-us/articles/360045953273) | Included | Included | Included | Included |
| Share link | [Members only](https://help.figma.com/hc/en-us/articles/360039960434#member) | Included | Not included | Included | Included |
| Embed | [Members only](https://help.figma.com/hc/en-us/articles/360039960434#member) | Not included | Not included | Included | Included |

### Share links

The fastest way to share your work with collaborators is to send them a link. You can copy and share links to files and prototypes, projects, and teams.

If they already have access to the team, project, or file they can interact with it based on those permissions. If they don't, the default link sharing settings will determine their access.

[Learn more about sharing files and prototypes](https://help.figma.com/hc/en-us/articles/360040531773).

Team admins can always reset or turn off invite links to remove unredeemed links. [Learn more about team invite links](https://help.figma.com/hc/en-us/articles/360039481034#Team_invite_links).

### Send invitations

You can invite someone to a file, a project, a team, or an entire organization. You’ll need the person's email address to invite them. They’ll receive an email invitation and a notification in their Figma account. To access the file, project, or team, they just need to accept the invitation.

- [Invite to files and projects](https://help.figma.com/hc/en-us/articles/360040531773#Send_invitations) to give them access to a single file, or all the files in a specific project.
- [Invite people to a team](https://help.figma.com/hc/en-us/articles/360039481034) to give them access to all files and projects in the team.
- [Add members and guests to an organization](https://help.figma.com/hc/en-us/articles/360040453113), or specific assets within the organization.

### Embed outside Figma

Embed files and prototype in a website or browser-based applications to bring your designs and prototypes to your team.

- Add style and component libraries in your design system documentation
- Include detailed feature designs and explorations in a PRD, spec document, or user story
- Keep your FigJam files alongside meeting notes
- Embed or share prototypes in testing environments

People can [interact with embeds](https://help.figma.com/hc/en-us/articles/360051741274) based on their permissions on that file. They’ll be prompted to log in to their Figma account if it’s a private file. [Embed files and prototypes →](https://help.figma.com/hc/en-us/articles/360039827134)

## Understanding permissions

Permissions control what collaborators can do:

- **Can view**: People with `can view` access can only perform certain 'read only' actions, like inspecting properties, following, and commenting.
- **Can edit**: People with `can edit` access can make changes to files and projects.

Permissions work at different levels:

- **At the file level**: Determines whether someone can view or edit that specific file.
- **At the project level**: Determines whether someone can create and edit files in the project, or only view it.
- **At the team level**: Determines what someone can do at the team level, such as creating projects, inviting members, or changing team settings.

Learn more:

- [File and project permissions](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions)
- [Team permissions](https://help.figma.com/hc/en-us/articles/360039970673)

### Inherited and explicit permissions

When you give someone access at a higher level, like a team or project, they’ll inherit permissions for everything inside it. For example, if a person has `can view` access to a project, they’ll inherit `can view` access for files inside that project.

You can also grant explicit permissions at a lower level. This allows you to give someone more access to a specific resource than they would inherit.

Example: James has `can view` access at the project level. If you invite him to a file in that project with `can edit` access, he’ll be able to edit that file, while still only viewing other files in the project.

### Permissions vs. seats

Seats are separate from permissions.

In Figma, a person's [seat](https://help.figma.com/hc/en-us/articles/360039960434) determines which Figma products they have access to. For example, a user with a Collab seat has access to FigJam and Figma Slides.

Permissions determine which files, projects, and teams they can edit.

For a user to be able to edit a file, they need both the appropriate seat and permissions.

## Troubleshooting access

If someone can’t access a resource, check these common causes:

- **Team vs. project access:** Being in a team doesn’t always guarantee project or file access. Confirm their permissions at the correct level:
  - [File and project permissions](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions)
  - [Team permissions](https://help.figma.com/hc/en-us/articles/360039970673)
- **Seats vs. permissions:** On paid plans, a collaborator needs both the correct seat and `can edit` access to edit a file. Users can request both file access and seats. Seats will only be approved according to admin’s seat approval settings.
  - [Request to edit a file](https://help.figma.com/hc/en-us/articles/4408435431319-Request-to-edit-a-file)
  - [Make a seat request](https://help.figma.com/hc/en-us/articles/360040453433-Make-a-seat-request)
  - [Set approval settings for new seats](https://help.figma.com/hc/en-us/articles/4414038570007-Set-approval-settings-for-new-seats)

## Related resources

- [Share files and prototypes](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes)
- [Invite team members](https://help.figma.com/hc/en-us/articles/360039481034-Invite-team-members)
- [Team permissions](https://help.figma.com/hc/en-us/articles/360039970673)
- [File and project permissions](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions)
- [Remove or adjust access](https://help.figma.com/hc/en-us/articles/360040530793-Remove-or-adjust-access)
- [Restrict copying and sharing](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files)
- [Add password protection to files](https://help.figma.com/hc/en-us/articles/5726720100247-Add-password-protection-to-files-and-prototypes)
