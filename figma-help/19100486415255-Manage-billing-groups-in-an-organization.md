---
기술지원명: Manage billing groups in an organization
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Manage billing groups in an organization
출처링크: https://help.figma.com/hc/en-us/articles/19100486415255-Manage-billing-groups-in-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the Enterprise plan

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) and [billing group admins](https://help.figma.com/hc/en-us/articles/4420557724439)

Billing groups let you sort people in your organization according to internal budget sources. Each billing group has billing group admins, who can:

- Assign or unassign users from the group
- Manage upgrade requests
- Move people between seat types
- Monitor AI credit usage for members in their billing group, where available

**Tip**: [What's the difference between billing groups and workspaces?](https://help.figma.com/hc/en-us/articles/19202489035543) Billing groups are for **accounting** and organizing people by cost center. Workspaces are for **collaboration** and organizing work by departments, product areas, or other categories.

## Who can manage billing groups?

Only organization admins and billing group admins can manage billing groups.

- Organization admins can create billing groups and assign billing group admins to each group. They can manage every billing group in the organization.
- Billing group admins manage seats in billing groups where they are an admin.

**Note**: Someone can be both a workspace admin and a billing group admin. [Learn more about the different types of admins in Figma →](https://help.figma.com/hc/en-us/articles/4420557724439)

**Tip**: You don't need to pay for someone to be a billing group admin. Admins who don't work in Figma can use a free View seat.

## Billing group settings and permissions

| Action | Billing group admin | Organization admin |
| --- | --- | --- |
| [View billing groups in the organization](#h_01HGKWWWE27D7MF536A4ZYMJD7) | Can view billing groups they manage | ✓ |
| [Add or remove people from a billing group](#h_01HGKWWWE2TAQKVZWSA0KQ8R6D) | Billing groups they manage | ✓ |
| [Change people’s seat types](#h_01HGKWWWE2Y5BE7X1A7QKS993R) | Billing groups they manage | ✓ |
| [View AI credit usage](https://help.figma.com/hc/en-us/articles/35865276858647) | Billing groups they manage | ✓ |
| [Add or remove a billing group admin](#h_01HGKWWWE2CT3YHZ098SFYYN6H) | X | ✓ |
| [Create a billing group](#h_01HGKWWWE2AG6XHMBBW3ZT8QHB) | X | ✓ |
| [Rename a billing group](#h_01HGKWWWE246B2RB9FA85V725N) | X | ✓ |
| [Delete a billing group](#h_01HGKWWWE2AB7Y9WCR3AXKZABW) | X | ✓ |

## View billing groups in the organization

**Billing group admins**

Billing group admins can only view billing groups they manage.

1. From the
   [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**.
2. Select the relevant billing group in the sidebar.

**Organization admins**

Organization admins can view all billing groups in the organization.

1. From the
   [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**.
2. Select the **Billing** tab.
3. Select the **Billing Groups** tab.

## Add or remove people from a billing group

People can only belong to one billing group at a time. When someone isn’t part of a billing group, they have the **Unassigned** label. Any organization admin or billing group admin can move someone who is unassigned into a billing group. You can also remove people from a billing group at any time by unassigning them.

**Note**: Organization admins receive upgrade notifications and requests for anyone with the **Unassigned** label. When a person is moved to a billing group, the billing group admins in that group become responsible for managing that person’s [paid status](https://help.figma.com/hc/en-us/articles/360039960434).

To move someone between billing groups, you’ll need to be an organization admin or a billing group admin in both groups.

**Note**: Guests are automatically added to the billing group of the person who invited them. If the person who invited them isn’t assigned to a billing group, the guest is also **Unassigned**.

**Billing group admins**

1. From the
   [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**.
2. Select the relevant billing group in the sidebar.
   1. To assign someone, click **Add members** and
      search for the person you'd like to add.
   2. To unassign someone, search in the table for the person you’d
      like to unassign. In the **Billing group** column,
      click the
      dropdown menu to change their billing group.

**Organization admins**

1. From the
   [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**.
2. Select the **People**
   tab.
3. Search for the person you’d like to manage.
4. In the **Billing group** column, click the dropdown
   menu
   to change their billing group.

**Tip**: You can manage people in bulk by hovering over each name and marking the checkbox that appears. Once you’ve selected multiple people, click **Change billing group** at the bottom of the screen.

## Change people’s seat types

Billing group admins and organization admins can manage members’ paid status at any time. This includes:

- [Approving or denying upgrade requests](https://help.figma.com/hc/en-us/articles/1500003870721.html)
- [Managing seats](https://help.figma.com/hc/en-us/articles/360052677454.html)

### View AI credit usage

Where available, billing group admins can view AI credit usage for members in the billing groups they manage from the AI credits tab of a billing group page.

![Billing group admins can view AI credit usage across their billing group](https://help.figma.com/hc/article_attachments/39913226793111)

Organization admins can view AI credit usage across the organization. Organization admins can also set aside AI credits to use for each billing group.

[Learn more about managing AI credits for billing groups](https://help.figma.com/hc/en-us/articles/39663732696087).

## Add or remove a billing group admin

An organization admin can add or remove billing group admins from any group. It’s possible to make someone an admin of more than one billing group.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Billing** tab.
3. Select the **Billing Groups** tab.
4. Find the billing group you'd like to manage, and click  the three dot menu.
5. Click **Edit details**.
6. Add or remove the name of the person you'd like to add/remove as a billing admin.
7. Click **Save changes**.

**Tip**: If you’d like someone to be a billing group admin who isn’t in your Figma organization yet, you’ll need to invite them first. If they don’t need to use Figma, make sure they have a View seat.

## Create a billing group

After you create a billing group, you can [add people to it](#h_01HGKWWWE2TAQKVZWSA0KQ8R6D).

**Tip:** The steps below outline how to create a billing group manually. Alternatively, organizations using [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) in Okta can use [SCIM to automatically manage groups](https://help.figma.com/hc/en-us/articles/25516157472791). You must create at least one billing group before setting up the corresponding group in Okta.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Billing** tab.
3. Click **Billing groups.**
4. Click  **Billing group**.
5. Give the billing group a name and add people from your organization as admins.

## Rename a billing group

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Billing** tab.
3. Select the **Billing Groups** tab.
4. Find the billing group you’d like to manage, and click  the three dot menu.
5. Click **Edit details**.
6. Update the name of the billing group and click **Save changes**.

## Delete a billing group

Deleting a billing group will move all members of the billing group to **Unassigned.** An organization or billing group admin can re-assign these members.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Billing** tab.
3. Select the **Billing Groups** tab.
4. Find the billing group you’d like to manage and click  the three dot menu.
5. Click **Delete**.

**Tip**: You can delete multiple billing groups at once by hovering over the name of each group and marking the checkbox that appears. Once you've selected multiple groups, click **Delete billing groups** at the bottom of the screen.
