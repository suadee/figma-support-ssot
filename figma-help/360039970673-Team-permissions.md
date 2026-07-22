---
기술지원명: Team permissions
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Team permissions
출처링크: https://help.figma.com/hc/en-us/articles/360039970673-Team-permissions
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on all plans

Team admins, owners, and anyone with `can edit` team access can adjust team permissions

Teams are dedicated spaces for organizing and collaborating on projects and files.

![Graphic showing hierarchy of resources in Figma - files sit in projects, which sit in teams, which sit in workspaces (enterprise only), which sit in an organization (organization and enterpris only).](https://help.figma.com/hc/article_attachments/35463257692823)

This article reviews team permissions. To learn more about file permissions, project permissions, or sharing files in Figma, check out [Guide to sharing and permissions](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions).

## Team permissions

Team permissions define what actions someone can take at the team level—such as creating projects, inviting members, or changing team settings.

In addition to `can view` and `can edit` permissions, a team member can be an owner or an admin:

- **Admin**: Admins are team members that have extra administrative right within the team. This allows them to manage any team settings, including any shared libraries. On the Professional plan, team admins also manage the team's subscription.
- **Owner**: Every team, project, or file has an owner. There is only one owner per team. The owner is the person that created the team, but [ownership can also be transferred](https://help.figma.com/hc/en-us/articles/360039481134-Transfer-ownership-of-a-team).

The table below outlines which team actions are available for each permission level:

| **Action** | **Can view** | **Can edit** | **Team admin/Owner** |
| --- | --- | --- | --- |
| [Invite others to the team](https://help.figma.com/hc/en-us/articles/360039481034) | With can view permissions only | Included | Included |
| [Create projects](https://help.figma.com/hc/en-us/articles/360038006494) | Not included | Included | Included |
| [Move files and projects](https://help.figma.com/hc/en-us/articles/360038511573) | Not included | Included | Included |
| [Delete team files](https://help.figma.com/hc/en-us/articles/360047512294) or [projects](https://help.figma.com/hc/en-us/articles/360038511833) | Not included | Included | Included |
| [Update team names or descriptions](https://help.figma.com/hc/en-us/articles/360039480614) | Not included | Included | Included |
| [Remove members from the team](https://help.figma.com/hc/en-us/articles/360040530793) | Not included | Included | Included |
| [Change the team name, icon, or description](https://help.figma.com/hc/en-us/articles/14949911189399-Change-a-team-name-or-icon) | Not included | Included | Included |
| [Update collaborator permissions on the team](https://help.figma.com/hc/en-us/articles/360040530793) | Not included | Included | Included |
| [Manage Community profile for team](https://help.figma.com/hc/en-us/articles/4404108672663) | Not included | Not included | Included |
| [Choose default libraries for the team](https://help.figma.com/hc/en-us/articles/360039234953) (paid plans) | Not included | Not included | Included |
| [Transfer ownership of the team](https://help.figma.com/hc/en-us/articles/360039481134) | Not included | Not included | Only the team owner can transfer ownership |
| [Delete team](https://help.figma.com/hc/en-us/articles/360039482174) | Not included | Not included | Included |
| [Upload and manage team fonts](https://help.figma.com/hc/en-us/articles/360039956774) (Organization and Enterprise plans only) | Not included | Not included | Included |
| [Manage seats](https://help.figma.com/hc/en-us/articles/360039960434) (billing status) | Not included | Not included | Included Team admins, Professional plan only |
| [View, manage, and upgrade the team's subscription](https://help.figma.com/hc/en-us/articles/360046216313) | Not included | Not included | Included Starter and Professional plan only |

### Inherited vs. explicit permissions

By default, when someone is invited to a team, their file and project permissions inherit from their team permissions.

Example

**Fruit Project** is a project within the **Produce** team.

- John has `can edit` team permissions on the **Produce** team. He can create new projects in that team, and is given `can edit` access to **Fruit Project** by default.
- Jeanie has `can view` team permissions on the **Produce** team. She cannot create projects in that team, and is given `can view` access to **Fruit Project** by default.

You can override someone's inherited permissions by editing their permissions on that file.

Example

James has `can view` permissions on the **Produce** team. His manager, Vanessa, invites him to a specific file within that team with `can edit` access.

With explicit edit access to the file, James is able to make edits to that file. He only has `can view` access to other files and projects in that team.

### Change team permissions

To change a user’s team permissions:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. Navigate to the team:
   - On the Starter or Professional plan, select  **All projects** from the left sidebar.
   - On the Organization or Enterprise plan without workspaces enabled, select  **All teams** from the left sidebar. Then, select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab.
3. Next to the team name, click  **Open team dropdown**.
4. Select **View members**.
5. Use the dropdown next to each user to update their team permissions. Click **Remove** to remove a member from the team.

![View team members from the dropdown menu next to the team name.](https://help.figma.com/hc/article_attachments/35463302810007)

## Organization access to teams

On the Organization and Enterprise plans, teams are created within organizations.

When you create a team, you’ll choose how others in your organization can access it via the **Who can access** dropdown.

- **Only those invited**: Only people you explicitly invite can access the team. Then, control if people in your team who haven’t been invited can discover the file by setting team visibility:
  - **Visible**: Members can discover and request access in the file browser.
  - **Hidden**: The team cannot be found by search. Members must be invited by an existing member.
- **[Workspace name]**(Enterprise plan only): Allows workspaces members to access the project via link or through the file browser.
- **[Organization name]:** Select your organization name to allow members to access the team via link or through the file browser.

If organization or workspace access is allowed, choose a permission level under **What they can do**:

- **View**: Organization or workspace members can view and comment on files in this team.
- **Edit**: Organization or workspace members can create/edit files, add members, and manage team permissions.

![When you create a team, you can set the organization access level to the team.](https://help.figma.com/hc/article_attachments/35463257697687)

### Change organization access to a team

To change the organization access level to a team:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. Open a team page.
   - On the Organization or Enterprise plan without workspaces enabled, select  **All teams** from the left sidebar. Then, select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Select a workspace, then select a team.
3. Click  **Open team dropdown** next to the team name and select **View settings**.
4. In the **Access** section, click **Change** to open the **Access settings** modal.
5. Set new access settings and click **Save**.

![View team settings to change organization access to the team.](https://help.figma.com/hc/article_attachments/35463257698711)

## Team permission FAQs

**How does a user’s seat type impact their permissions?**

Seats are separate from permissions.

In Figma, a person's [seat](https://help.figma.com/hc/en-us/articles/360039960434) determines which Figma products they have access to. For example, a user with a Collab seat has access to FigJam and Figma Slides.

Permissions determine which files, projects, and teams they can edit.

For a user to be able to edit a file, they need both the appropriate seat and permissions.

**If I change a user’s team permissions, does that impact my subscription or bill?**

No, team permissions do not impact your subscription or bill. Your bill is determined by your plan and the number of paid seats you purchase.

[Learn more about billing at Figma](https://help.figma.com/hc/en-us/articles/29717597009431-Guide-to-billing-at-Figma).

**How can I see a user’s team permissions?**

To view a user’s team permissions:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, you can access the file browser by clicking the  Figma menu > **Back to files.**
2. Open a team page.
   - On the Starter or Professional plan, select  **All projects** from the left sidebar.
   - On the Organization or Enterprise plan without workspaces enabled, select  **All teams** from the left sidebar. Then, select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab.
3. Next to the team name, click  **Open team dropdown**.
4. Select **View members**.

**If I have** `can edit` **permissions on a team, does that mean I have** `can edit` **access to all projects in that team?**

By default, a user’s project permissions are inherited from their team permissions. This means that if a user has `can edit` team permissions, they would have `can edit` project permissions for all projects within that team.

However, you can change the team access level for each project.

[Learn more about managing team access on projects](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions).
