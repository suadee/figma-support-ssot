---
기술지원명: Manage plugins and widgets in an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage plugins and widgets in an organization
출처링크: https://help.figma.com/hc/en-us/articles/4404228724759-Manage-plugins-and-widgets-in-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Organization admins only

Plugins and widgets are third-party applications that run in Figma's products. By default, members can [find and use plugins and widgets](https://help.figma.com/hc/en-us/articles/360042532714) in their files without approval from an admin.

Since plugins and widgets have access to information about members and files, organization admins can restrict access to them by [requiring approval](#h_01HBHE0R6JP5YCPJW3XNZVN3RD) before they can be used.

|  | Organization plan | Enterprise plan |
| --- | --- | --- |
| [Require approval for plugins and widgets](#h_01HBHE0R6JP5YCPJW3XNZVN3RD) | ✓ | ✓ |
| [Approve plugins and widgets](#h_01HBHEA7NPNYSW57GQECPQWAXM) | Applies to the whole organization | Applies to the whole organization or on a workspace-by-workspace basis |
| [Manage approved plugins and widgets](#h_01HBHEC99YMVMPWBQPBV0NMYMK) | Managing means removing access for the entire organization | Can remove access for the entire organization or adjust which workspaces have access |
| [Review plugin and widget usage](#h_01HBHEC99YB0K6ZQ64HYV34D7B) | X | ✓ |

**Note:** Figma [reviews the overall quality of every plugin and widget](https://help.figma.com/hc/en-us/articles/360039958914) published to [Figma Community](https://www.figma.com/community).

## Require approval for plugins and widgets

When enabled, members can only use plugins and widgets that have been approved by an organization admin.

You can choose to let members request approval when they find plugins or widgets in Figma Community they want to use.

Require plugin approval Require widget approval

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Click the **Settings** tab.
3. Under **Extensions**, click **Plugin approval**.
4. Select **Only admin-approved plugins.**

If you leave **Allow members to request plugins** checked, members can request access to unapproved plugins. [Learn more about managing plugin requests](#h_01HBHEA7NPRA2PF1MC7TGPTXMC).

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Click the **Settings** tab.
3. Under **Extensions**, click **Widget approval**.
4. Select **Only admin-approved widgets.**

If you leave **Allow members to request widgets** checked, members can request access to unapproved widgets. [Learn more about managing widget requests](#h_01HBHEA7NPRA2PF1MC7TGPTXMC).

**Note**: These settings don't apply to [private plugins or widgets](https://help.figma.com/hc/en-us/articles/4404228629655) published by people in your organization. Private plugins and widgets are available to every member in your organization and don't require approval.

## Approve plugins and widgets for the organization

When you approve a plugin or widget for the organization, members can use it right away.

### **Approve a plugin or widget**

Organization plan Enterprise plan

1. In [Figma Community](https://www.figma.com/community), navigate to the plugin or widget you’d like to approve.
2. Click **Copy link** in the **Share** section to add the plugin URL to your clipboard.
3. Select  **Admin** in the sidebar.
4. Select **Resources**, then select **Plugins**.
5. Click  **Add plugin** or  **Add widget** at the top right of the page.
6. Paste the link in the field provided and click **Add** to confirm.

1. In [Figma Community](https://www.figma.com/community), navigate to the plugin or widget you’d like to approve.
2. Click **Copy link** in the **Share** section to add the plugin URL to your clipboard.
3. Select  **Admin** in the sidebar.
4. Select **Resources**, then select **Plugins**.
5. Click  **Add plugin** or  **Add widget** at the top right of the page.
6. Paste the link in the field provided and click **Add** to confirm.
7. Select one or more workspaces, or approve the plugin or widget for the whole organization.

**Note:** Updates to approved plugins or widgets don't require re-approval. But organization admins will get notified via email if an update to a plugin or widget includes changes to its [network access](https://help.figma.com/hc/en-us/articles/360042532714.html#01H8M501RQ5KFB7BSAVSQ48SVV) or the optional [security disclosure](https://help.figma.com/hc/en-us/articles/16354660649495-Security-self-assessment).

**Tip**: As an organization admin, you can also [save each plugin or widget](https://help.figma.com/hc/en-us/articles/4404239055127). This promotes it to the **Saved** section of the plugin or widget list in everyone's files.

## Manage plugin and widget approval requests

If you [allow members to request plugins and widgets](#h_01HBHE0R6JP5YCPJW3XNZVN3RD), they can request access to any plugin or widget in [Figma Community](https://www.figma.com/community) that hasn't been approved yet.

Each time a member makes a request, every organization admin gets notified in Figma and via email. As an organization admin, you can approve or decline these requests.

Here’s what it looks like to review a request:

![Review window for a Figma plugin approval request showing plugin details, user requests, and options to try, decline, or approve.](https://help.figma.com/hc/article_attachments/28287138082711)

Overview Request history Try it out Decline Approve

This section is made up of multiple components:

- A quick summary from the plugin or widget’s Figma Community page. Click **Open in Community** at the bottom of the modal to view the full listing.
- Information about the plugin or widget’s security practices. Developers can complete an optional [security disclosure form](https://help.figma.com/hc/en-us/articles/16354660649495-Security-self-assessment) to get a **Data security info available** badge on the listing for their plugin or widget. They also can provide information about its [network access](https://help.figma.com/hc/en-us/articles/360042532714.html#01H8M501RQ5KFB7BSAVSQ48SVV).
- How the plugin or widget is licensed.

A history of requests for the plugin or widget, including whether it has previously been approved or declined.

**Try it out** creates a new Figma Design or FigJam draft in a team outside the organization with the plugin or widget available for use.

**Note**: If you decline the request after clicking **Try it out**, the plugin or widget will continue to be available only in that draft file. To remove the plugin or widget completely, [delete the file from your drafts](https://help.figma.com/hc/en-us/articles/360047512294-Delete-and-restore-files).

![Decline plugin request modal with reason provided.](https://help.figma.com/hc/article_attachments/28287191792535)

When you click **Decline**, you’ll have the option to provide a reason. This helps the person who requested the plugin or widget understand why the request has been declined, and gives other organization admins context if someone requests approval for the plugin or widget in the future.

On the Organization plan, clicking **Approve** will give everyone in the organization access to the plugin or widget.

On the Enterprise plan, you can choose to approve the plugin or widget for the whole organization, or for individual workspaces. Approving for individual workspaces will prevent members from using the plugin or widget in drafts.

When you approve a request, the person who made the request will get notified in Figma and via email.

## Manage or remove **an approved plugin or widget**

Organization plan Enterprise plan

On the Organization plan, managing an approved plugin or widget means removing access for everyone in the organization.

1. Select  **Admin** in the sidebar.
2. Select **Resources**, then select **Plugins** or **Widgets**.
3. Click the plugin or widget you’d like to remove from the organization.
4. Click **Remove**.

Removing access to a plugin or widget from the approved list will immediately prevent members from using them in files. An organization admin can always re-approve it again later.

On the Enterprise plan, you can remove access for everyone in the organization, or manage access on a workspace-by-workspace basis.

1. Select  **Admin** in the sidebar.
2. Select **Resources**, then select **Plugins** or **Widgets**.
3. Click the plugin or widget you’d like to manage or remove from the organization.
4. Click **Edit approvals.**
5. Use the toggles to adjust access to the plugin or widget within the organization.

## Review plugin or widget usage Enterprise

On the Enterprise plan, you can see how many times an approved plugin or widget has been run, which people are using it, and which workspaces are using it the most.

1. Select  **Admin** in the sidebar.
2. Select **Resources**, then select **Plugins** or **Widgets**.
3. Select a plugin or widget.
4. Click the **Usage** tab.
