---
기술지원명: Create and manage user groups
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Create and manage user groups
출처링크: https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on Organization and Enterprise plans.

Any organization member can create and manage user groups, unless limited by admin.

Organization admins can manage all user groups in the organization, even those they did not create.

Organization members can share files with and mention any existing user group. Guests can only share with or mention user groups they belong to.

User groups let admins organize people into named groups.

You can use user groups to:

- Organize members of your organization by team, department, or role
- Share files, projects, and teams with multiple people at once
- Mention groups in comments to notify everyone in the group
- Keep permissions up-to-date as groups change

User groups can be managed manually or synced from your organization’s identity provider.

## Create a user group

All organization members can create user groups, unless [limited by admin](#h_01KGN2KHSBQY1Y7MMV74KGMH1R).

To create a user group:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **All workspaces** or  **All teams.**
2. From the **User group** section of the right sidebar, click  the plus icon.
3. Enter a name and optional description for the group, then click **Continue**.
4. Search for and add any member or guest in the organization to the group.
5. Choose whether to notify people when they’re added to the group.
6. Click **Save**.

![Create a user group from the file browser by clicking the plus icon in the right sidebar.](https://help.figma.com/hc/article_attachments/38272778189463)

## Add or remove group members

Group creators or organization admins can add or remove group members at any time. Organization admins [can add or remove members from any group in the organization from the **Admin** dashboard](#h_01KGN2KHSB90RVT2T2ZXQPS1Y8).

To add a group member:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **All workspaces** or  **All teams.**
2. From the **User group** section of the right side bar, select a user group.
3. You can add members individually or in bulk:
   - To add users individually, use the search bar to enter an organization member or guest’s name, and click **Add**.
   - To add users in bulk, click  > **Add people.** Search for and add any members or guests, then click **Save**.

To remove group members:

1. From the file browser, click  **All workspaces** or  **All teams.**
2. From the **User group** section of the right side bar, select a user group.
3. You can remove members individually or in bulk:
   - To remove users individually, hover over a user’s name and click  **More > Remove from group.**
   - To remove users in bulk, click   **> Remove people**. Select all users you’d like to remove from the group, then click **Remove**.

![Add or remove users from a group by clicking the Edit icon on the user group modal.](https://help.figma.com/hc/article_attachments/38272755058839)

## Rename or delete a user group

Group creators and organization admins can rename or delete user groups. Organization admins [**can rename or delete any user group from the Admin dashboard**](#h_01KGN2KHSB90RVT2T2ZXQPS1Y8).

### Rename a group

To rename a user group:

1. From the file browser, click  **All workspaces** or  **All teams.**
2. From the **User group** section of the right side bar, select a user group.
3. Click  **Edit > Settings.**
4. Click **Edit**.
5. Enter an updated name and optional description.
6. Click **Save**.

### Delete a group

To delete a user group:

1. From the file browser, click  **All workspaces** or  **All teams.**
2. From the **User group** section of the right side bar, select a user group.
3. Click  **Edit > Settings.**
4. Click **Delete group**.
5. Confirm to delete the group.

Deleting a group removes it as an option from sharing and mentions, but doesn’t delete any files or users.

## Manage user groups as an admin

### Manage user groups from admin dashboard

Organization admins can access and manage user groups from the admin dashboard.

To manage user groups from the admin dashboard:

1. From the file browser, click  **Admin.**
2. Select the  **People** tab.
3. Select the **User groups** tab.

From the **User groups** tab, admins can view a list of all user groups, add or remove people from groups, create or delete groups, and edit group details.

![Admins can manage user groups from the People tab of their admin dashboard.](https://help.figma.com/hc/article_attachments/38272778194839)

### Manage who can create user groups

On the Enterprise plan, organization admins can change who can create and manage user groups in their organization.

By default, anyone in the organization can create and manage user groups.

To update this setting:

1. From the file browser, click  **Admin.**
2. Select the  **Settings** tab.
3. Under **Team and user group creation**, select **Creating user groups.**
4. Choose one of the following options:
   1. **Anyone**: Any member of the organization can create user groups.
   2. **Organization admins only**: Only organization admins can create user groups.
5. Click **Save**.

### Sync user groups from an identity provider

Enterprise plans that use [SCIM for automatic provisioning](https://help.figma.com/hc/en-us/articles/360048514653-Set-up-automatic-provisioning-via-SCIM) can sync user groups directly from their identity providers.

When a group is synced:

- Group membership is managed directly via SCIM
- Changes in your identity provider provisioning automatically update user groups in Figma
- Manual edits to group membership may be disabled in Figma

**Note**: Before you can sync user groups, your organization must already be pushing groups to Figma via SCIM from your identity provider. Enabling SCIM alone doesn’t automatically sync groups—admins need to explicitly assign or push groups from their identity provider to Figma.

Learn more about managing groups via SCIM in [Okta](https://help.figma.com/hc/en-us/articles/25516157472791-Manage-workspaces-and-billing-groups-via-SCIM-in-Okta) or [Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/37835780984215-Manage-SCIM-Groups-for-Microsoft-Entra-ID).

To create or sync groups from your identity provider:

1. From the file browser, click  **Admin.**
2. Select the **People** tab.
3. Select the **User groups** tab.
4. Click the **+ User group** button, then select **Sync from IdP** from the dropdown menu.
5. Select SCIM groups, then click **Create**.

Each SCIM group you select will synch to its own user group.

[Learn more about setting up automatic provisioning via SCIM](https://help.figma.com/hc/en-us/articles/360048514653-Set-up-automatic-provisioning-via-SCIM).

## Share files, projects, or teams with a user group

You can share files and projects with a user group the same way you share with individual people. Everyone in the group gets the selected edit or view permission. When someone joins or leaves the group, their access updates automatically.

To share a file with a user group:

1. Select the file, project, or team and click **Share**.
2. Enter the name of a user group in the invitation field.
3. Select a permission: **Can edit** or **Can view**.
4. Click **Invite**.

![Share files with user groups from the share modal. ](https://help.figma.com/hc/article_attachments/38272778196247)

[Learn more about sharing files](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes), [sharing projects](https://help.figma.com/hc/en-us/articles/360038006494-Create-a-new-project#h_01K6KKTA2RDX8XBMVJZ96XANVW), or [sharing teams](https://help.figma.com/hc/en-us/articles/360039481034-Invite-team-members).

## Mention a user group in comments

You can mention a user group in comments to notify everyone in the group.

1. Add a comment to a file.
2. Type `@` and start typing the group name.
3. Select the group from the list.
4. Post the comment.

All users in the group will receive notifications about the comment, based on their [comment notification settings](https://help.figma.com/hc/en-us/articles/360041547813-Manage-email-notifications-for-comments-on-files).

[Learn more about comments](https://help.figma.com/hc/en-us/articles/360039825314-Guide-to-comments-in-Figma).
