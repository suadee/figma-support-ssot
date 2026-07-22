---
기술지원명: Restrict or prevent guest access
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Restrict or prevent guest access
출처링크: https://help.figma.com/hc/en-us/articles/4410793238167-Restrict-or-prevent-guest-access
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273).

Only organization admins can manage guest membership settings.

The **guest memberships** setting allows organizations to determine if existing members and guests can share organization files, projects, and teams with external users.

This setting applies to guest invitations, as well as guests who open and access files using a shared link.

What are guests?

Guests are external users with email addresses that don't match any of the organization's domains. They could be contractors, agencies, clients, or external collaborators.

[Learn more about guests](https://help.figma.com/hc/en-us/articles/4420557314967).

## Guest membership settings

The guest membership setting offers greater control over who is joining the organization, and extra peace of mind when it comes to privacy and security.

There are three available options:

- External users can join the organization without restrictions
- External users can only join the organization with admin approval
- No external users can join your organization

### Allow guest access

With the **External users can join the organization without restrictions** setting enabled, existing member or guests can invite guests to files, projects, or teams without restrictions.

When a guest joins your organization, they join with a free View seat. You can change a guests [seat type](https://help.figma.com/hc/en-us/articles/360039960434) at any time, and a guest can [make a seat request](https://help.figma.com/hc/en-us/articles/360040453433) to change their seat type.

Guests can still only access the resources you specifically invite them to.

If public link sharing is enabled, guests can also open organization files if an existing member or guest shares the file link with them.

When you invite an external user to an organization resource, Figma lets you know that the invitee is a guest: ![Confirmation dialog for sharing with an external email address outside the organization, with cancel and share options.](https://help.figma.com/hc/article_attachments/4421243655575)

### Require admin approval

With the External users can only join the organization with admin approval setting enabled, existing members or guests can invite the external user to files, projects, or teams. When the inviter clicks Send, Figma informs them that admin approval is required.

![Admin approval required prompt for external user access to Figma organization file, connecting with admin for assistance.](https://help.figma.com/hc/article_attachments/4421243565207)

When the guest first opens an organization resource they can **Ask to be added** to the organization. They won't be able to access the file, project, or team their request is accepted.

![Access restricted message asking the user to join the organization via admin approval.](https://help.figma.com/hc/article_attachments/4421243556375)

Requests are sent to the relevant workspace admin to [accept or ignore](https://help.figma.com/hc/en-us/articles/4420542281495). If the file or invitee is outside of a workspace, Figma sends the request to an organization admin.

When a guest joins your organization, they join with a free View seat. You can change a guests [seat type](https://help.figma.com/hc/en-us/articles/360039960434) at any time, and a guest can [make a seat request](https://help.figma.com/hc/en-us/articles/360040453433) to change their seat type.

**Note:** Figma only requires approval the first time you invite the guest to an organization resource. Once approved, people won’t need further approval to invite that guest to other resources.

### Prevent guest access

With the No external users can join your organization setting enabled, existing members and guests aren't able to invite external users to the organization. When someone tries to invite an external user to an organization resource, Figma informs them guest access is disabled.

**Note:** If public link sharing is enabled, external users may still be able to view content through a link if the individual file permissions allow it. Organization admins can disable public link sharing settings.

![Sharing with external users is disabled; invite to external email was not sent due to organization settings.](https://help.figma.com/hc/article_attachments/4421243707415)

## Adjust guest membership setting

Organization admins can control guest membership from the organization's **Admin**.

1. Open the organization in Figma and select **Admin** in the sidebar.
2. Select **Settings** from the header.
3. In the **External access** section, select **Guest membership**.
4. Select who can invite external users to files, projects, and teams:
   - External users can join the organization (default)
   - External users can only join with admin approval
   - No external users can join the organization  
     ![Guest membership settings panel showing options for external user access and a note on public link sharing permissions.](https://help.figma.com/hc/article_attachments/4483130665751)
5. Select **Save** to apply your changes.
