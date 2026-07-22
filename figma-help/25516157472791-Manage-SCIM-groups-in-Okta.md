---
기술지원명: Manage SCIM groups in Okta
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage SCIM groups in Okta
출처링크: https://help.figma.com/hc/en-us/articles/25516157472791-Manage-SCIM-groups-in-Okta
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Organizations using [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) in Okta can use SCIM to automatically assign users to a [workspace](https://help.figma.com/hc/en-us/articles/4409676189207) or [billing group](https://help.figma.com/hc/en-us/articles/19100885191191) in Figma.

To manage membership to workspaces and billing groups using Okta:

1. [Set up a workspace and billing group](#h_01J4T1R7V827XZAZR820X9FKCA)
2. [Create a group in Okta](#h_01J4T1R7V8XBTZCP2M2ARR678X)
3. [Add or unlink a push group from the Figma application](#h_01J4T1R7V8C8EKX1GW50WZTQ0M)
4. [View SCIM groups in Figma](#h_01J4T1R7V8GQ6NFYH847FDF31C)

Groups pushed to Figma via SCIM can be reused across multiple features, including workspace assignments, billing groups, and [user groups](https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups). Once a group is pushed from Okta, it becomes available anywhere Figma supports SCIM groups.

**Note:** Before you dive in, you’ll need:

- Administrative access to Okta with the scope to add and update groups and applications
- SCIM provisioning enabled

## 1. Set up a workspace or billing group

You must create at least one workspace or billing group before setting up the corresponding group in Okta.

- [Create a workspace](https://help.figma.com/hc/en-us/articles/4409612431383-Create-a-workspace)
- [Create a billing group](https://help.figma.com/hc/en-us/articles/19100486415255-Manage-billing-groups-in-an-organization)

## 2. Create a group in Okta

**Note**: The name of the group in Okta must match the name of the corresponding workspace or billing group.

![Okta Groups panel displays group names, number of people, and applications assigned to each group for management.](https://help.figma.com/hc/article_attachments/25516213798551)

1. Under **Directory > Groups**, click **Add group** and enter a name of the group.
2. Click **Assign People** to add users to the group.

## 3. Add a push group to the Figma application

Push groups in Okta let administrators push group membership from Okta to other applications.

**Tip**: Push groups do not provision user accounts. To assign a user to the Figma application, navigate to **Applications > Figma > Assignments.**

![Push Groups tab showing group sync between Okta and Figma, with active status for Designers, Engineering, Marketing, Product.](https://help.figma.com/hc/article_attachments/25516213801111)

When you add a push group, Okta will link the push group to any workspace or billing group with a matching name. All users in the push group will be assigned to the associated workspace or billing group once the push group status is active.

**Note:**

- Make sure you use separate groups for provisioning and group pushing. Using the same group for both app assignments and group push functions is [not currently supported in Okta](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-about-group-push.htm).
- Members of your organization won’t notice when they are assigned to a billing group. If they are assigned to a workspace, the workspace name will automatically appear in their sidebar in the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183).

1. Navigate to **Applications > Figma > Push Groups.**
2. Click **Push Groups > Find Groups by name.** Type in the name of the group created in the last section and click on the name when it appears. Click **Save.**
3. Locate the newly added group in the **Push Groups** tab. When the **Push Status** is set to **Active**, your push group has successfully pushed to Figma.

**Note:**

- If a user is included in multiple push groups, the first push group added to the Figma application in Okta takes precedence
- Depending on the group size, the workspace and billing group assignments may take up to 30 minutes
- Group sizes are limited to 5,000 users

### Unlink a push group

Unlinking a push group in Okta removes the SCIM group in Figma. All users managed by the push group will be unassigned from their respective workspace or billing group.

1. Navigate to **Applications > Figma > Push Groups.**
2. Locate the group you would like to unlink and click **Active > Unlink pushed group**.
3. Select **Delete the group in the target app** and click **Unlink.**

![Push Groups interface in Okta showing group management options like "Deactivate", "Unlink", and "Push now" for Figma.](https://help.figma.com/hc/article_attachments/25516251713943)

## 4. View SCIM groups in Figma

You can view the members of any SCIM group you’ve created in Figma.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar**.**
2. Select the  **People** tab.
3. Click the **SCIM group** filter and select a group to view members of the group.
