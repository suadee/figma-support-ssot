---
기술지원명: Use approvals in Figma Buzz
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Use approvals in Figma Buzz
출처링크: https://help.figma.com/hc/en-us/articles/39288847137815-Use-approvals-in-Figma-Buzz
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the Organization and Enterprise plans

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439-Admins-in-Figma) can configure approval settings for their organization

Use approvals in Figma Buzz to request feedback, collect decisions, and confirm when assets are ready to use or export. Admins can optionally require approval before export to ensure assets meet team standards before they’re used.

## Configure approval settings

Admins can control how approvals work for their organization, including whether approvals are required before exporting assets.

To configure approval settings for your organization:

1. From the file browser, click  **Admin**.
2. Select the  **Settings** tab.
3. Find the **Resources** section.
4. Select **Asset approvals** to open the approval settings modal.

By default, approvals are turned off. When approvals are off, users won’t see the option to request reviews or use approval workflows.

Toggle on approvals to enable them for your organization.

When approvals are enabled, you can choose how strictly they’re enforced:

- **Approvals required**: Assets must be approved before they can be exported. Users won’t be able to export assets until a review is completed.
- **Approvals optional**: Users can request approvals, but approval is not required to export assets.

![Enable or disable approvals for your organization from admin settings](https://help.figma.com/hc/article_attachments/39289135787927)

### Configure workspace-level settings

On Enterprise plans, you can apply different approval settings to specific workspaces.

Use the **Custom settings for workspaces** field to select one or more workspaces, then define whether approvals are required or optional for those workspaces.

Workspaces not included in custom settings will follow the default organization-level approval behavior.

## Request an approval

Use approvals when you want others to review and sign off on your work.

To request an approval:

1. Open your Figma Buzz file.
2. Click  **Reviews** in the top right.
3. Click **+ New Review.**
4. Select the assets you want reviewed.
5. Add a title, reviewers, and any additional context. You can add reviewers by name or email. Reviewers must already have access to the file.
6. Click **Send for review.**

![Select assets in your file to send for review](https://help.figma.com/hc/article_attachments/39289135795095)

Figma Buzz creates a request that includes the selected assets and notifies reviewers. Reviewers receive an in-product notification and an email with a link to the request.

Assets that are part of an active review are labeled with an  **In review** tag.

## Manage your request

After sending a request, you can monitor progress and take action as reviewers respond.

Open the  **Reviews** panel to see the current status of your request, including who has reviewed, their decisions, and any comments left on assets.

If you need to make changes to the request—such as updating the asset selection or reviewers—you’ll need to cancel the request and create a new one.

### Cancel a request

Requesters can cancel a review at any time if they need to make updates or stop the review process.

To cancel a request:

1. Open your Figma Buzz file.
2. Click  **Reviews** in the top right.
3. Find the relevant request and click **Cancel review**.

![Cancel a review request from the Reviews panel](https://help.figma.com/hc/article_attachments/39289135798167)

When a request is cancelled, the original notification is updated to indicate that the request was cancelled. Assets are no longer marked as  **In review**.

### Review results

After reviewers complete a request, you’ll receive an in-product notification and email with the results.

Open the request from the  **Reviews** panel to see each reviewer’s decision, comments left on assets, and which assets were approved or need changes.

- If assets are approved, they are marked with an  **Approved** badge.
- If changes are requested, they are marked with a  **Changes needed** badge. These assets remain editable and may include comments to guide updates. You can review feedback directly on each asset and follow up with reviewers if needed.

If you need to resubmit any assets that weren’t approved, create a new approval request.

Once all assets in a request are approved, the approval request is marked as complete and you are ready to export your assets.

### Editing approved assets

Once an asset is approved, it’s considered final and ready for use or export. Approved assets are locked and can’t be edited unless you explicitly unlock them.

If you need to make changes to an approved asset:

1. Select the asset.
2. In the banner at the bottom of the file, click **Edit asset**.

Clicking **Edit asset** removes its approval status and makes it editable again. You’ll need to request approval again before exporting if your organization requires it.

![When you click an approved asset, there is a banner towards the bottom of the file where you can unlock it for further editing](https://help.figma.com/hc/article_attachments/39289149389079)

### Export assets

How approvals affect exporting depends on your [organization’s approval settings](https://www.notion.so/Approvals-in-Figma-Buzz-327b8b1f837c801291bcfc22a473a0a4?pvs=21).

- If **Approvals required** is enabled, you can only export assets that have been approved. If any selected assets are not approved, you’ll be prompted to request approval before exporting.
- If **Approvals optional** is enabled, you can export assets at any time, whether or not they’ve been reviewed. Approved assets will still show their approval status, but approval is not required.

![If approvals are required, you cannot export assets that have not yet been approved](https://help.figma.com/hc/article_attachments/39289135803671)

[Learn more about exporting assets from Figma Buzz](https://help.figma.com/hc/en-us/articles/31271832936343-Export-assets-from-Figma-Buzz).

## Review an approval request

If you’re added as a reviewer, you’ll receive both an in-product notification and an email prompting you to review the request.

To open a review request:

1. Open the Figma Buzz file.
2. Click  **Reviews** in the top right.
3. Click **Begin review** on the relevant request.

Once you begin, Figma Buzz guides you through each asset included in the request. The file will automatically pan and zoom so you can review assets one at a time.

![Review assets one by one, approving them or requesting changes](https://help.figma.com/hc/article_attachments/39289135811095)

For each asset, you’ll have the following options:

- **Approve**: Confirm the asset is ready to move forward
- **Request changes**: Indicate that updates are needed before approval
- **Add a comment**: Leave feedback directly on the asset. Comments behave like standard file comments, so you can reply, mention teammates, and resolve threads.

If you’ve already clicked **Approve** or **Request changes** on an asset, you can click **Edit decision** to update your choice.

When you’ve finished reviewing all assets, click **Mark as complete**.

Once a review is completed, the requestor is notified via email and in-product notification.
