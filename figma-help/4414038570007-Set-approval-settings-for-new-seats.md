---
기술지원명: Set approval settings for new seats
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Set approval settings for new seats
출처링크: https://help.figma.com/hc/en-us/articles/4414038570007-Set-approval-settings-for-new-seats
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

In March 2025, Figma introduced updates to how seats and other billing features work. This article describes the updated billing model.

[Learn more about the transition to the updated billing model](https://help.figma.com/hc/en-us/articles/27468498501527).

Who can use this feature

Available on the [Professional, Organization, and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

On the Professional plan, team admins or owners can set approval settings for anyone joining the team

On the Enterprise and Organization plans, organization admins can set approval settings for anyone joining the organization

Every member or guest in an organization or team has a seat, which determines the Figma products they have access to.

Members or guests can [make seat requests](https://help.figma.com/hc/en-us/articles/360040453433). As admin, you can use seat approval settings to automatically manage these new seat requests.

[Learn more about managing seats in Figma](https://help.figma.com/hc/en-us/articles/360039960434).

Note: If you are on the Enterprise plan, you can use role setting via [SCIM](https://help.figma.com/hc/en-us/articles/360048787534) to assign seats to users. Seat approval settings do not apply to users whose seats are set by SCIM.

## Seat approval settings

For each seat type, admins can choose from the following seat approval settings:

- **Manually approve seats**: All seat upgrade requests must be manually approved by an admin.
- **Manually approve, unless seat is available** (default): People who request a paid seat are automatically granted one if it is available.
- **Auto-approve seats**: All seat upgrade requests are automatically granted. If there are no seats available, a new seat will be purchased.

A [seat is available](https://help.figma.com/hc/en-us/articles/360039960434#view-available-seats) if it has been purchased in advance, but no one is currently assigned to it.

Note: For customers on an ELA (Enterprise License Agreement), requests for all paid seats default to the **Auto-approve seats** setting. The setting **Manually approve, unless seat is available** is disabled, since this option doesn’t apply on an ELA.

Admins can [approve or decline seat requests](https://help.figma.com/hc/en-us/articles/1500003870721) that require manual approval from the **Dashboard**.

Which admins can approve or decline seat requests?

- Professional plan: Team admins or owners
- Organization plan: Organization admins
- Enterprise plan: Organization admins and billing group admins (if billing groups are enabled)

### What happens while a user waits for their request to be reviewed?

To ensure users aren’t blocked from collaborating while admins review their seat request, they’ll be able to use the functionality of the seat they requested temporarily for up to three days.

During that time, they can create new files and edit files that their teammates have granted them edit access to. They can't edit files without edit access.

The temporary access ends immediately if the request is denied or expires.

## Adjust seat approval settings

Here’s how you can adjust seat approval settings:

From billing settings From seat requests

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the  **Settings** tab.
3. In the **Billing** section, click **Seat approval settings**.
4. In the popup modal, select an approval setting for each seat type.

![Find seat approval settings in the Settings tab of Admin.](https://help.figma.com/hc/article_attachments/30567582879127)

1. From the file browser, click  **Admin**.
2. Click **View all** on the seat requests table.
3. Click **Approval settings**.
4. In the pop up modal, select an approval setting for each seat type.

![Open seat approval settings from the Approval settings button on your admin Dashboard.](https://help.figma.com/hc/article_attachments/30567573499543)
