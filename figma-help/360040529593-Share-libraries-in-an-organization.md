---
기술지원명: Share libraries in an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Share libraries in an organization
출처링크: https://help.figma.com/hc/en-us/articles/360040529593-Share-libraries-in-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Supported on [Organization and Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)s.

Members can publish a library to the team or the organization. Members need can edit access to a file to publish it.

Team admins can enable any library that has been shared with the organization, for their specific team(s).

Only organization admins can choose which libraries are available to all teams by default.

Libraries are design files that include styles and components that are reused across a brand, product, or project. Learn more from our [guide to libraries](https://help.figma.com/hc/en-us/articles/360041051154).

There are three levels of library sharing in an organization:

1. Publish styles and components from a file to a library. Anyone with access to that file can use that library.
2. Publish libraries within a specific team. Members of that team can access those libraries and team admins manage default libraries for the team.
3. Share a published library with everyone in the organization. This allows anyone in the organization to access and use that library. Organization admins can [make these libraries default libraries](https://help.figma.com/hc/en-us/articles/360040530413).

**Note:** Guests can only access libraries you invite them to. Invite guests to the original file to give them access to those styles and components across organization files.

## Publish file as a library

Publish styles and components from organization files as libraries. Anyone with **can edit** access to the file can publish it.

Publish a library within a team, or share the library with the entire organization.The file's link sharing settings determine who can access and use a library.

You can set a [file's link sharing settings](https://help.figma.com/hc/en-us/articles/360040044834) when you first publish the library, or when you publish an update.

Every time you publish a library, Figma will add a checkpoint to the file's version history. You can identify these events with the  icon.

### Share within a team

**Caution:** If you choose to publish the library to the team only, only direct members of that team can access those styles and components. The file has to be shared with the organization to allow anyone from outside the team to access it. This includes people with access to individual files and projects in that team.

1. From the open file, open the **Assets** panel in the left sidebar.
2. Click  **Libraries** to open the **Libraries** modal. The tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. Click **Publish** next to the **Current file**.
4. Enter a summary of your changes in the field provided. This description will appear in the file's version history.
5. Leave the **Allow any member of the organization to access the file** setting unchecked.
6. Click **Publish** to share the library and update the file's link sharing settings.

![Publishing modal in Figma showing change summary options, invalid components, and publish button for sharing libraries.](https://help.figma.com/hc/article_attachments/27999040214807)

### Share with organization

Share the file with the organization to allow anyone in the organization to access those files.

1. From the open file, open the **Assets** panel in the left sidebar.
2. Click  **Libraries** to open the **Libraries** modal. The tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. Click **Publish** next to the **Current file**.
4. Enter a summary of your changes in the field provided. This description will appear in the file's version history.
5. Check the box next to **Allow any member of `organization name` to access the file**. This updates the file's link sharing settings to "Anyone at `organization`"
6. Click **Publish** to share the library and update the file's link sharing settings.

**Tip!** If a library is already published, you can update the file's link sharing settings instead. To share the library with the organization, set this to **Anyone at `organization`**. Learn more about [link sharing](https://help.figma.com/hc/en-us/articles/360040044834#Link_sharing_settings).

## Manage default libraries

If a library is shared across the organization, both team and organization admins can manage these libraries.

**Tip!** Track how members of your organization are using components, styles, and variables with design system analytics. Learn more about [library analytics](https://help.figma.com/hc/en-us/articles/360039238353).

### Team libraries

Team admins can manage default libraries for their team. Team admins can make any library shared with the organization a default library. This includes libraries from another organization team.

Team admins can choose to turn libraries on for **FigJam** files, **Design** files, or **All files**. Anyone who is a member of that team will see that library by default in team files.

[Learn how to enable a library for a team.](https://help.figma.com/hc/en-us/articles/360039234953)

### Organization libraries

Organization admins can make libraries available to all teams in the organization. They can turn libraries on for **FigJam** files, Figma **Design** files, or **All files**.

If the library isn't already shared with the organization, organization admins can update organization access as part of that process. Learn how to [manage a library for a workspace or organization](https://help.figma.com/hc/en-us/articles/21310245473815).

## Remove libraries

We mentioned above that there are three steps or tasks related to sharing libraries in an organization:

- Publish the styles and components to a library
- Make that library available to members of the organization
- Manage default libraries for the organization

To remove libraries in an organization, you can reverse any or all of those steps, depending on the outcome you want:

- [Unpublish the library](#unpublish-library) to remove these styles and components from the **Libraries** modal for everyone. This breaks the connection between the main components and any instances.
- [Remove organization access](#remove-access) to update a published library so that its only shared within a specific team in the organization.
- [Turn off organization library](#turn-off-default) to remove it as a default library in all organization files. Members can still enable this library manually in the library modal of specific files or teams.

### Unpublish libraries

Unpublish the library to remove everyone's access to the library. This removes the library at both the team and organization levels.

This doesn't remove styles and components from organization files, but those styles and components won't receive any further updates.

1. Open the file you want to remove.
2. Open the **Assets** tab in the left sidebar and click  **Libraries**. The tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. In the Library modal, click on the library in the **Current file**.
4. Click the **Unpublish** button at the bottom of the modal:.
5. Click **Remove file from library** to confirm.
6. Figma will return you to the file. The status bar will indicate that Figma has removed the file from the library.

![Library modal showing an active library. The cursor is hovering over the unpublish button](https://help.figma.com/hc/article_attachments/27999055860375)

### Remove organization access

Adjust the file's link sharing settings to prevent members of the organization from finding and using the file. This removes the library from organization members, while keeping it published to a specific team.

Only members of the team can access and use that library. If people have access to individual files and projects in that team, but aren't a member of the team, they can't access that library.

1. Click the **Share** button in the menu bar.
2. Click the  next to the existing  link access. This will be set to **Anyone at `organization name`.**
3. Select **Only people invited to this file** from the options.
4. Close the file sharing modal.

![Share modal in an organization file, link sharing setting with Only people invited to this file highlighted.](https://help.figma.com/hc/article_attachments/27999055862807)

**[Share files in an organization →](https://help.figma.com/hc/en-us/articles/360040044834)**

### Turn off organization library

Organization admins can turn off a library so that it's no longer a [default library in organization files](https://help.figma.com/hc/en-us/articles/360040530413). Team admins can still enable this library for their teams and members can still access the library in organization files.

1. Select **Admin** in the sidebar.
2. Select the **Resources** page and then select the **Libraries** tab.
3. Click **Off** next to the library to adjust.
