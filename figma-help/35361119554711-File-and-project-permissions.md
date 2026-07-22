---
기술지원명: File and project permissions
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: File and project permissions
출처링크: https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on all plans

Only owners and those with `can edit` permissions on a file or project can make changes to permissions on that file or project.

In Figma, you work in files, and files can be organized into projects. Projects are organized by team.

[Learn more about sharing and permissions in Figma](https://help.figma.com/hc/en-us/articles/1500007609322).

## Project permissions

Permissions define who can access a file, project, or team—and what they can do with it. On a project, users can be assigned the following permissions:

- **Can edit**: Users can create and edit files in this project.
- **Can view**: Can only view the project. They cannot create files. Access to individual files is determined by file-level permissions.
- **Owner**: The person who created the project. They can create and edit files within it.

You can invite individuals to a project and assign them `can edit` or `can view` permissions.

Example

The **Fruit Project** contains two files: **Apple** and **Banana**.

Jesse is invited to the **Fruit Project** with `can view` project permissions. This means he cannot create new files in **Fruit Project**. His access to the individual files depend on his individual file permissions.

- He has `can edit` permissions in the **Apple** file, so he can edit that file.
- He has `can view` permissions in the **Banana** file, so he can only view that file.

On the other hand, Jules is invited to **Fruit Project** and given `can edit` permission on the project. He can create new files in **Fruit Project**, and can edit both the **Apple** and **Banana** files by default.

**How can I see what permissions a user has on a project?**

To view a user’s project permissions:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, click the  Figma menu > **Back to files.**
2. Open the project page.
   - On the Starter or Professional plan, select  **All projects** from the left sidebar. Then, select a project.
   - On the Organization or Enterprise plan, select  **All teams** from the left sidebar. Select a team, then select a project.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab. Select a project in that team.
3. Click **Share** to open the share modal, which lists all users and their project permissions.

**If I change a user’s permission on a project, does that impact my subscription or bill?**

No. Project permissions do not impact your Figma subscription. Your Figma subscription is determined by both your plan type, and the number of seats on your plan.

[Learn more about billing at Figma](https://help.figma.com/hc/en-us/articles/29717597009431-Guide-to-billing-at-Figma) and how to use [seat approval settings to manage incoming seat requests](https://help.figma.com/hc/en-us/articles/4414038570007-Set-approval-settings-for-new-seats).

### Team access to projects

Projects live within teams and inherit team-level permissions by default.

Example

**Fruit Project** is in the **Produce** team.

- John has `can edit` team permissions on the **Produce** team. By default, he is given `can edit` project permissions on **Fruit Project**.
- Jeanie has `can view` team permissions on the **Produce** team. By default, she is given `can view` project permissions on **Fruit Project**.

You can change the team-level access to a project by doing the following:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, click the  Figma menu > **Back to files.**
2. Navigate to the list of team projects:
   - Starter or Professional plans: Select  **All projects** from the left sidebar.
   - Organization or Enterprise plans: Select  **All teams** from the left sidebar. Then, select a team.
   - Enterprise plan with workspaces enabled: Select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab.
3. Select a project.
4. Click **Share**.
5. From the share modal, select the team access level (labelled “Anyone in [Team Name]”).
6. Click **Change access**.
7. Select a new team access option for the project:
   - **Same as the team**: Project permissions are inherited from team permissions. If a user has `can edit` team permissions, they will have `can edit` project permissions. If a user has `can view` team permissions, they have `can view` project permissions.
   - **View-only**: All team members can view the project, but can’t create new files. Access to individual files depend on file permissions.
   - **Disable**: Team members have no access unless individually invited.

![Change the default team access setting from the project share modal.](https://help.figma.com/hc/article_attachments/35363054295191)

**Note:** On the Starter plan, team access to projects is set to **Same as the team** by default. If you want to make projects with more private team access settings, you need to [upgrade to a paid plan](https://help.figma.com/hc/en-us/articles/360046216313).

**How can I see a user’s team permissions?**

To see a user’s team permissions:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, click the  Figma menu > **Back to files.**
2. Open the team page.
   - On the Starter or Professional plan, select  **All projects** from the left sidebar.
   - On the Organization or Enterprise plan, select  **All teams** from the left sidebar. Select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab.
3. Select  **Open team dropdown** next to the team name.
4. Click **View members** to view a list of team members and their team permissions.

### Organization access to projects

On the Organization and Enterprise plans, projects are created within teams, and teams are created within organizations.

When you create a project, you can set the organization access level to the project from the **Who can access** dropdown:

- **Only those invited:** Only people you've directly invited can access the project
- **[Workspace name]** (Enterprise plan only): Allows workspaces members to access the project via link or through the file browser.
- **[Organization name]**: Allows organization members to access the project via link or through the file browser

If organization or workspace access is allowed, choose a permission level under **What they can do**:

- **View:** Organization or workspace members can view and comment on files in this project.
- **Edit:** Organization or workspace members can create and edit files in this project, add members, and change members’ edit permissions.

**How can I change organization access level to a project?**

To change organization access to a project:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, click the  Figma menu > **Back to files.**
2. Open the project page.
   - On the Organization or Enterprise plan, select  **All teams** from the left sidebar. Select a team, then select a project.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab. Select a project in that team.
3. Click **Share**.
4. From the share modal, select the organization access level (labelled “Anyone in [Organization name]” or “Only invited people”).
5. Select a new organization access level for the project.
   - **Only those invited**: Only people you've directly invited can access the project.
   - **[Organization name]:** Select your organization name to allow members to access the project via link or through the file browser. If you allow organization access to the team, you must set a permission level (”What they can do”):
     - **View**: Organization members can view and comment on files in this project.
     - **Edit**: Organization members can create and edit files in this project, add members to the project, and change members’ project permissions.

## File permissions

The following file permissions determine what actions someone can take within a file:

- **Can edit**: Full editing capabilities.
- **Can view**: View-only access.
- **Owner**: Has `can edit` access.

Use the table below to understand the difference between `can edit` and `can view` file permissions.

| **Action** | **Can Edit** | **Can View** |
| --- | --- | --- |
| Modify designs/components | Included | Not included |
| Add comments | Included | Included |
| View layer properties | Included | Included |
| Copy/export assets | Included | Included (unless [copying and exporting is restricted)](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files) |

**Tip:** Review the “Who can use this feature” box at the top of each Figma Learn article to understand access for individual features.

By default, each resource inherits permission levels from their parent. This means that a file will inherit the permissions set on the project level, and a project will inherit permissions set on the team level.

However, you can override inherited permissions:

- Project-level changes override team settings
- File-level changes override project settings

Example

James has `can view` permissions on the Product team. His manager, Vanessa, invites him to a specific file with `can edit` access.

With explicit edit access to the file, James is able to make edits to that file. He only has view access to other files and projects in that team.

### Access to files

File access determines who can open a file. Access is set when you share a file and can apply to individuals, or to broader audiences like a team, workspace, or organization.

[Learn more about file access and sharing files](https://help.figma.com/hc/en-us/articles/360040531773).

**How does a user’s seat type impact their permissions?**

Seats are separate from permissions.

In Figma, a person's [seat](https://help.figma.com/hc/en-us/articles/360039960434) determines which Figma products they have access to. For example, a user with a Collab seat has access to FigJam and Figma Slides.

Permissions determine which files and projects they can edit.

For a user to be able to edit a file, they need both the appropriate seat and permissions.

Example

Ernie is a part of an organization, and has a Collab seat. The Collab seat gives Ernie access to FigJam and Figma Slides.

Ernie is invited to three files.

- Ernie is invited to File A, a Figma Design file, with **can edit** file permissions. Since his seat type does not give him access to Figma Design, he does not have edit access to the file. He would need to [make a seat request](https://help.figma.com/hc/en-us/articles/360040453433-Make-a-seat-request) in order to access the Figma Design file.
- Ernie is invited to File B, a FigJam file, with **can edit** file permissions. He can edit File B, since his seat gives him access to FigJam, and he also has **can edit** file permissions.
- Ernie is invited to File C, a FigJam file, with **can view** file permissions. He can only view File C, since he only has **can view** permissions on the file. He would need to request to edit the file in order to make changes.

**How can I view file permissions?**

To view permissions on an individual file:

1. Open the file.
2. Click the **Share** modal.

From the share modal, you can view a list of invited users and their file permissions.
