---
기술지원명: View members and guests
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: View members and guests
출처링크: https://help.figma.com/hc/en-us/articles/4420842863255-View-members-and-guests
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Members are available on all [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan). Guests are available on the Organization and Enterprise plans.

On the Professional plan, only team admins can view and manage members.

On the Organization plan, only organization admins can view and manage members and guests.

On the Enterprise plan, organization admins can view and manage everyone in the organization. Workspace admins can view and manage people in workspaces they manage. They can also view and claim people that aren’t assigned to a workspace. Billing group admins can view and manage users in their billing group.

View users from your team or organization on the **People** page. User filters to help sort through people by their billing or user activity.

## View members and guests

To view members and guests:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, you can access the file browser by clicking  the Figma menu > **Back to files** from the left sidebar toolbar.
2. Click  **Admin**.
3. Select the  **People** tab.

![The People tab of your admin dashboard shows all users in a table, with other user details like seat type, billing group, and last active timestamp](https://help.figma.com/hc/article_attachments/39745859046551)

From the **People** page, you can:

- View the name, avatar, and email address of each person.
- View and sort people by their assigned [**Seat type.**](https://help.figma.com/hc/en-us/articles/360039960434)
- View and sort people by [paid AI credit access status](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits#h_01KHPZ72P92DG0K7CZBFAABYZC).
- View and sort people by their billing cycle (monthly or annual). Professional annual plan only.
- View and sort people by [**Billing group.**](https://help.figma.com/hc/en-us/articles/19100486415255) Enterprise plan only.
- View and sort people by their **Last active** date. This is the last time each person performed an action in Figma—such as moving or renaming a file, publishing a library, or viewing a file in Dev Mode. This may not reflect their most recent login date.
- Use the available  [filters](#sort-and-filter) to refine your search results.
- Download a CSV file  of all member and guest information. Organization and Enterprise plans only.
- View current seat count on your team or organization, with the option to filter by specific seat type.
- Search for people by name.
- Select the **User groups** tab to view and manage all [user groups](https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups) in the organization Organization and Enterprise plans only.

**Note:** Organization admins can click on a user to view the date they joined the organization and the specific action that prompted them to join.

## Sort and filter results

To apply a filter to your list of members and guests, select  **Filter**. Choose from the following filters to sort and refine your results:

- **Seat type**:
  - Full
  - Dev
  - Collab
  - View
- [**Paid AI credits**](https://help.figma.com/hc/en-us/articles/35865276858647)
  - All access types
  - Access enabled
  - Access disabled
- **Billing cycle** (available on Professional annual plans)
  - All billing cycles
  - Monthly
  - Annual
- **Charged** (available on Organization and Enterprise plans, once you’ve finalized your first invoice)
  - All charges
  - New charges since last invoice
- **Billing groups** (Enterprise plan only): Filter users by [billing group](https://help.figma.com/hc/en-us/articles/19100486415255)
- **User type** (Organization and Enterprise plans only)
  - [Admin](https://help.figma.com/hc/en-us/articles/4420557724439)
  - [Member](https://help.figma.com/hc/en-us/articles/4420557314967): People in the organization that have an email address that matches any of the organization's domains
  - [Guest](https://help.figma.com/hc/en-us/articles/4420557314967): External users with email addresses that don't match any of the organization's domain
  - Pending:
    - Users that have been provisioned for Figma, but haven't logged in via SAML SSO yet
    - Users that haven’t redeemed their invitation to join Figma
  - Unverified: User has not completed the email verification process for their Figma account
- **Last edit** (Organization and Enterprise plans only)
  - All time
  - More than 3 months ago
  - More than 6 months ago
  - More than a year ago
- **Last active** (Professional plan only)
  - All time
  - More than 3 months ago
  - More than 6 months ago
  - More than a year ago
- **Workspace** (Enterprise plan only): Filters users by their [workspace](https://help.figma.com/hc/en-us/articles/7576392133527)

Click on any of the column headers to sort results using that column. Click again to switch between ascending and descending order.

Note: If you have [configured SCIM](https://help.figma.com/hc/en-us/articles/360048514653-Set-up-automatic-provisioning-via-SCIM), you can sort members based on your SCIM member data, like cost center, organization division, or department.

## Perform actions in bulk

Use the checkboxes next to each person to select more than one person. You can then perform any of the following actions in bulk:

- Copy emails to your clipboard
- [Change AI credit access](https://help.figma.com/hc/en-us/articles/35865276858647)
- [Add to user group](https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups) (Organization and Enterprise only)
- [Change workspace](https://help.figma.com/hc/en-us/articles/7576392133527) (Enterprise plan only)
- [Change billing group](https://help.figma.com/hc/en-us/articles/19100486415255) (Enterprise plan only)
- [Remove users from the organization](https://help.figma.com/hc/en-us/articles/360040453453)

![Select multiple users from the People tab to enable the bulk actions menu.](https://help.figma.com/hc/article_attachments/30567583160343)
