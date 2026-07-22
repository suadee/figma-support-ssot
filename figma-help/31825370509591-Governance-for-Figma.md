---
기술지원명: Governance+ for Figma
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Governance+ for Figma
출처링크: https://help.figma.com/hc/en-us/articles/31825370509591-Governance-for-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Governance+ is available as an add-on for [Figma Enterprise](https://help.figma.com/hc/en-us/articles/31825370509591-Governance-for-Figma-Enterprise) and [Figma for Government](https://help.figma.com/hc/en-us/articles/22932461365015). While most features are identical across both solutions, a small number differ—or are available on one plan only—due to the compliance requirements of the Figma for Government environment. See the table in [What's included](#h_01JT8V6JBDDQSAZRPZQEWT6T5X) for a full comparison.

If your organization has unique security or compliance needs, Governance+ provides the specialized tools you need to manage your data, ensure safe access, and stay compliant.

With Governance+, you’ll get:

- **Centralized control:** Make sure all Figma activity by your employees happens in the right instance and on your approved networks, where your policies apply. With features like **IP Allowlist** and **Network Access Restrictions (NAR)**, you can minimize the risk of data slipping into unauthorized spaces or accounts.

- **Account security:** Protect your organization’s data by enforcing secure authentication requirements. With **Enforced** **Two-Factor Authentication (2FA)**, **Extended Idle Session Timeout**, and **Multiple Identify Provider (IdP)** support, you can reduce the risk that accounts with approved access to your organization’s content are compromised.

- **Data governance:** Stay compliant with your organization’s data standards. Governance+ gives you visibility into Figma activity through tools like the **Discovery Pipeline**, helping you meet electronic communication retention policies and support legal discovery requirements.

With Governance+, you can confidently scale Figma while meeting your organization’s security and compliance standards. It’s built to help you make Figma a compliant workspace where your team can focus on what matters most—creating together.

## What’s included in Governance+?

| Feature | Description | Figma Enterprise | Figma for Government |
| --- | --- | --- | --- |
| [Restrict file exporting](#restrict-file-exports) | Prevent view-only users from copying, saving, or exporting files | ✓ | ✓ |
| [Network access restrictions (NAR)](#h_01JT8V6JBED0TAGY0PGZ580WHG) | Restrict unauthorized account access while on your network | ✓ | ✓ |
| [IP allowlist](#h_01JT8V7QE3T8P7NPQT0MMBW0ET) | Ensure employees can only access their Figma account from the organization's network | ✓ | ✓ |
| [Discovery pipeline](#h_01JT8V7QE3K693HEN53X8GE51Z) | Log all text edits in Figma files to meet electronic communication retention requirements | ✓ | ✓ |
| [Extended idle session timeout](#h_01JT8V7QE3RXYNGQ0C0QMSEHKP) | Get more granular control over when inactive users are logged out | ✓ | — ‡ |
| [Enforced 2FA](#h_01JT8V7QE37XJMKJ7YQ05Z1SSF) | Require additional authentication for guests using any login method | ✓ | ✓ |
| [Multiple IdP support](#multipleidps) | Connect more than one identity provider and map domains to the right provider | ✓ | ✓ |
| [Internal policies](#h_01K7228JJBDF29PGGCVQ52M2X2) | Require users to agree to customer-provided policies before accessing content | ✓ | ✓ |
| [Enterprise Key Management (EKM)](#h_01KFKN8VNWBAH642JZ033VDXTH) | Encrypt certain Figma file data at rest using your organization's AWS KMS key | ✓ | ✓ |
| [Guest expiration](#guestexpiration) | Set a default lifetime for newly invited guests and manage individual expiration dates | ✓ | ✓ |
| [AI hosting controls](#aihostingcontrols) | Manage where AI traffic is sent and where AI features can be used | ✓ | — ‡ |
| [Developer Logs API](#h_01KSJPZ7VSCZQZ3YY2AN4KSMBJ) | Fetch a granular log of API calls made to the REST API or MCP server | ✓ | ✓ |

The Governance+ feature details may vary between Figma Enterprise and Figma for Government. See the relevant section for details.

‡ Not part of Governance+ for Figma for Government. These features are already included in the Figma for Government baseline environment.

For pricing and packaging details, contact your sales representative.

## Restrict file exporting

By default, anyone with view-only access to a file can export assets from it, save a local copy of it to their computer, or copy its contents from one file to another.

While users can [restrict these actions on individual files](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files), organization admins can enable the file export setting to create a consistent policy across the organization or selected workspaces.

When active, this setting restricts users with view-only access from copying, saving, or exporting files. Any actions related to saving, copying, or exporting are hidden or disabled for affected users.

![File menu with "Export" option grayed out, indicating restricted access.](https://help.figma.com/hc/article_attachments/33560252505879)

The available options for this setting are:

- **Allow exporting by all viewers.** This is the default setting and allows all users to copy, save, and export from a file.
- **Prevent exporting by guest viewers.** [Guests](https://help.figma.com/hc/en-us/articles/4420557314967-Members-versus-guests#guests) with view access aren’t allowed to copy, save or export. [Members](https://help.figma.com/hc/en-us/articles/4420557314967-Members-versus-guests#guests) of your organization with view-only or edit access—or guests with edit access—can still perform these actions.
- **Prevent exporting for all viewers.** Anyone with view-only access can’t copy, save, and export. People with edit access to the file will still be able to perform these actions.

**Note**: Users can still [disallow viewers from copying, saving, and exporting on a per-file basis](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files)—even if the organization has a more permissive file export setting enabled.

If your organization uses workspaces, an organization admin can apply the file export settings at the workspace level, not just the organization level. Workspace-level settings will take precedence over the organization-level settings.

### Enable file export restrictions

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin.**
2. Select the **Settings** tab.
3. Navigate to the **External access** section and click **File exporting**.

## Network access restrictions

Organization admins can ensure secure collaboration by enabling the **Restrict external account access on this network** setting. This feature prevents users from accessing personal or unauthorized Figma accounts while connected to your corporate network.

Before NAR can be enabled, your organization must pass a **shadow mode testing** period. During this time, Figma monitors traffic at the provided IP ranges to verify that the majority of Figma users from those IP ranges are already members or guests in your organization's plan. NAR can only be enabled once this condition is confirmed.

If multiple Figma organizations use the same network, Figma can configure the same IP range as a co-owned NAR range. When a range is co-owned, users can access Figma on that network with an authorized account from any of the co-owning organizations. At least one of the co-owning organizations will have to go through shadow mode testing; if both organizations are being NAR-enabled at the same time, they'll both need to go through shadow mode testing.

Once enabled, users can only access Figma on the corporate network if:

- They log in with an account associated with your organization’s domain.
- They are guests in your organization.
- For co-owned IP ranges, they log in with an account associated with one of the co-owning organizations, or are guests in one of those organizations.

**Note**: If an external user has a pending invite to join the organization, they won’t be able to accept the invitation while on the corporate network.

If someone tries to use an unauthorized Figma account while they're on the corporate network, they'll be prompted to switch to their work account:

![Network prompt to switch to a corporate Figma account, ensuring secure access and compliance with organizational policies.](https://help.figma.com/hc/article_attachments/31825394466711)

For co-owned ranges, they may be prompted to switch to an account from any of the authorized organizations.

When the person rejoins an external network, they can resume access to their other Figma accounts.

### Enable or disable network access restrictions

To turn on this setting, provide the IP range(s) for your network and proof of ownership, such as a letter, email, or invoice from your ISP confirming the IP range assignment.

To get in touch with support:

- **Figma Enterprise:** Contact the support team via the [support request form](https://help.figma.com/hc/en-us/requests/new).
- **Figma for Government:** Email [support-figgov@figma.com](mailto:support-figgov@figma.com).

The process will take about two weeks to complete. You can find this setting by following the instructions below.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin.**
2. Select the **Settings** tab.
3. Navigate to **External access** and click [**Contact support**](https://www.figma.com/contact/).

## IP allowlist

**Note:** All organization domains must be verified via technical [domain verification](https://help.figma.com/hc/en-us/articles/360045953273-Manage-domain-capture-for-an-organization#h_01J3RESBMNAZX741MQD3BF49RM) (i.e., you must add a TXT record to your DNS records via your domain provider) before you can enable IP allowlist.

The IP allowlist ensures secure access to your organization’s Figma account by limiting access to users connected to approved corporate networks. With this feature enabled, members of your organization can only authenticate and use their Figma accounts when they’re within the specified IP ranges.

Once enabled, the IP allowlist enforces these rules:

- **Applies to members only**: Members are users with accounts on your organization’s domain. Guests and organization admins are exempt.
- **IP-based access checks**: Figma examines all requests from members. If the request originates from an approved IP range, access is granted. Otherwise, members are prompted to switch networks or accounts. Only IPv4 addresses are supported.

### Setting up the IP allowlist

To enable the IP allowlist for your organization:

1. Verify your domains via technical [domain verification](https://help.figma.com/hc/en-us/articles/360045953273-Manage-domain-capture-for-an-organization#h_01J3RESBMNAZX741MQD3BF49RM).
2. Add allowed IP ranges in the admin console:
   - Go to **Admin → Settings → Login and provisioning → IP allowlist**.
   - Enter your allowed addresses as a comma-separated list. You can include single IPv4 addresses (e.g. `203.0.113.10`) and IPv4 CIDR blocks (e.g. `203.0.113.0/24`) in the same list. Hyphenated ranges (e.g. `203.0.113.10-203.0.113.20`) aren't supported—express these as one or more CIDR blocks instead.
3. Keep IP ranges updated. If your corporate network changes, update the IP ranges in the admin console.

## Discovery pipeline

The **Discovery API** helps meet compliance requirements by letting organizations extract all edits to text persisted in Figma files on a go-forward basis.

- Logs events whenever users edit text in comments, shapes, stickies, text boxes, component documentation, Dev Mode links, and more. Also captures the user-authored portion of prompts to AI features.
- Data is made available to customers via secure, short-lived downloadable files that are accessed by hitting a url that’s returned via an API endpoint.

In Governance+ for Figma for Government, only the user-authored portion of Make prompts is captured (Figma Make is currently the only AI feature in Figma for Government). The Discovery API is accessed at <https://api.figma-gov.com> instead of <https://api.figma.com>.

Discovery pipeline data is only retained and available for querying for 30 days. To meet your data retention requirements, you should regularly query the endpoint and download the files from the provided links.

For setup and implementation, refer to the [Discovery API developer documentation](https://developers.figma.com/docs/rest-api/discovery/).

- **Figma Enterprise:** [developers.figma.com](https://developers.figma.com/docs/rest-api/discovery/)
- **Figma for Government:** [developers.figma-gov.com](https://developers.figma-gov.com/docs/rest-api/discovery/)

**Note:** The discovery pipeline feature and API are not enabled by default with Governance+. To activate this feature, you must contact Figma Support.

## Extended idle session timeout

This Governance+ feature is additive for Figma Enterprise only. Figma for Government includes idle session timeout as part of its baseline environment.

By default, Figma automatically logs users out after 21 days of inactivity. For added security, organization admins can configure an **idle session timeout** to log out inactive users earlier. With Governance+, timeouts can be set as short as 15 minutes.

### How it works

- Idle session timeouts apply only to organization members, not guests.
- When a session times out, users are logged out across all platforms, including web browsers, desktop apps, mobile apps, embeds, and integrations (e.g., Microsoft Teams).
- Users receive a prompt to stay logged in when they are less than one minute away from timing out. If they don’t respond, they must log back in to regain access.
- If a user belongs to multiple organizations with session timeouts, the shortest timeout applies.

**Note**: Figma’s activity log captures changes to the session timeout policy and logs when members are logged out due to a timeout. Timeouts are logged immediately for open web browsers or desktop apps; background timeouts are logged the next time the user accesses Figma.

### Set an idle session timeout

1. From the file browser, click **Admin**.
2. Select the **Settings** tab.
3. Under **Login and provisioning**, click **Session timeout**.
4. Click **Custom timeout**.
5. Choose a timeout length and click **Save**.

**Note**: Setting a new timeout resets inactivity for all users in your organization. Users will only be logged out after exceeding the newly defined timeout period.

If anyone in your organization cannot log back in after a timeout, please ask them to contact support.

## Enforced 2FA

With **Enforced 2FA**, Enterprise organizations can restrict access to their content for guests who do not have **two-factor authentication** enabled. This feature enhances security by ensuring only properly authenticated users can access content.

2FA settings are available for guests.

To help manage guest access, the admin console now includes:

- **CSV Export**: The members table CSV export now has a 2FA\_enabled column, indicating whether guests who use username/password have 2FA enabled.
- **Blocked Badge**: Guests without 2FA will display a **Blocked** badge next to their name once 2FA is enabled.

### Enforced 2FA for guests

**Who is impacted**:

- Applies to all supported login methods
- Affected guests must **enable 2FA** to regain access.

Enforced 2FA restricts access to all Figma content across web, desktop, and mobile platforms. Open sessions remain unaffected until the guest logs out or their session expires.

Your organization's admins can configure this feature through the administration portal in your Figma account. It is a self-service feature.

1. Go to the **Admin console**.
2. Click the **Settings** tab.
3. Select **Guest Membership** and locate the toggle for 2FA for Guests.
4. Review the number of guests who will be blocked, then click **Save**.

Once activated, Org admins will receive an email notification and affected guests will receive an email prompting them to enable 2FA to regain access to files within their organization. Affected users are blocked from content access right away, so we recommend activating 2FA for Guests during non-peak hours.

### Invite new guests to an organization where 2FA for guests is enabled

- **Guests with 2FA enabled**: Receive and accept invitations as usual.
- **Guests without 2FA**: Can accept invitations but won’t access files until they enable 2FA on their account.

By enforcing 2FA for guests, organizations can safeguard sensitive data while maintaining a seamless collaboration experience for properly authenticated users.

## Multiple identity provider (IdP) support

Admins can connect more than one identity provider (IdP) to their organization. This allows you to:

- Support multiple authentication methods across different business units or regions
- Run parallel IdPs during migration or consolidation projects
- Offer flexibility for hybrid IT environments

### How it works

- Admins can configure multiple IdPs directly in their admin settings.
- Domain-based routing: Figma routes users to the correct IdP based on their email domain. Each domain maps to exactly one IdP at a time, and a single IdP can serve multiple domains.

### Set up multiple IdPs

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser), select  **Admin** in the sidebar.
2. Click the  **Settings** tab.
3. In the **Login and provisioning** section, click select **Manage identity providers (IdP)**.
4. Click **+ Add IDP** to add a new provider.
5. In the modal, select **Edit configuration** to update the identify provider and SAML Single Sign On (SSO) configuration details.
   1. Choose your provider type.
   2. Provide IdP details (such as metadata URL, entity ID, or signing certificate). For more information on setting up identify providers, see [Guide to SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO).
   3. Select one or more domains whose members should authenticate with this IdP.
   4. Test sign-in using an email on a mapped domain to confirm it’s working correctly.
   5. Repeat for additional IdPs as needed.

The **Identity providers** table will show each IdP and its mapped domains.

- Select an identify provider from the table to edit IdP details or domain mappings.
- To remove an IdP, hover over an IdP on the table and select  **More > Remove**. Be sure to remap domains first (either all to one IdP or to different IdPs) to prevent login disruption.
- Users on unmapped domains won’t be able to sign in with SSO.
  - **Figma Enterprise:** If your organization allows any login method, those users can still sign in with other methods.
  - **Figma for Government:** Invited users can sign in with a magic link.

## Set internal policies for your organization

Internal policies let you require people in your organization to review and agree to custom policies before accessing content. For example, you can require members to review and agree to your company’s internal privacy policy before continuing to work in Figma.

To enable internal policies for your organization, [contact Figma’s support team](https://help.figma.com/hc/en-us/requests/new?&chatStartExpanded).

When you contact support, include the following details:

- **Audience**: Who must agree to the policy (members, guests, or everyone)
- **Cadence**: How often users must agree to the internal policy (once per year, or once per user lifetime)

When an internal policy is enabled, users in the selected audience will be blocked by a modal containing the policy the next time they navigate to any content or page in the organization. Users must agree to the policy before they can continue. If the policy cadence is set to once per year, users will be required to agree to the policy again each year.

![A modal showing an internal policy that user must agree to before continuing to work in Figma.](https://help.figma.com/hc/article_attachments/37541263256855)

### Review if internal policies are enabled or disabled

Admins can review if an internal policy is set for an organization.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**
2. Select the  **Settings** tab.
3. In the **Other** section, review if **Internal policies** are enabled or disabled

**Note:** To change this setting and or to update the content of your internal policy, you’ll need to reach out to [Figma’s Support team](https://help.figma.com/hc/en-us/requests/new?&chatStartExpanded). Whenever a policy is enabled or disabled, organization admins will receive an email that includes the policy’s enabled or disabled date, cadence, audience, policy title, and the full policy text.

## Enterprise Key Management (EKM)

Enterprise Key Management (EKM) allows eligible organizations to encrypt certain Figma file data at rest using the organization’s own AWS Key Management Service (KMS) key. This provides additional control over data at rest—you can grant, monitor, and revoke Figma’s access to the encryption key at any time.

To request EKM for your organization, [contact the Figma team](https://help.figma.com/hc/en-us/requests/new). After you share the required details, our team will coordinate the setup on Figma’s side.

### What data is encrypted with EKM?

EKM applies to file data stored in Figma’s backend that’s stored in AWS S3, including:

- File checkpoints (shapes, text, frames, layers, etc.)
- Images and videos uploaded to files

The following data is not encrypted using EKM:

- Metadata
- Comments
- Component definitions stored in databases

For a full list of data that stored locally, see [Enabled localized file hosting](https://help.figma.com/hc/en-us/articles/15643274574871-Enable-localized-file-hosting).

### Request EKM setup

To set up EKM, [contact Figma](https://help.figma.com/hc/en-us/requests/new). You’ll receive instructions to create AWS KMS keys and grant access to Figma’s AWS account. After you provide the details below, Figma’s team will configure EKM for your organization and confirm when it’s active.

Include the following in your request:

- Primary AWS KMS key ARN
- Replica AWS KMS key ARN (for disaster recovery replication)
- Confirmation that Figma’s AWS account has been granted the required permissions for both keys

Note: Once enabled, EKM automatically applies to all new files in your organization. Existing files will be encrypted gradually in the background, and do not require any modifications to your workflows.

### Monitor key usage

You can monitor key activity through AWS CloudTrail, which logs encryption, decryption, and key access events performed by Figma’s IAM roles.

### EKM and localized file hosting

Figma supports using EKM alongside data locality. If your organization uses data locality, we recommend configuring data locality first and then enabling EKM.

### Important considerations

- **AWS KMS only:** Currently, only AWS KMS is supported.
- **One key per organization:** EKM uses one AWS KMS key for all encrypted file data in the organization. Different keys per workspace, project, or team aren’t supported.

Caution: If Figma loses access to your AWS KMS key (for example, if permissions are revoked or the key is unavailable), all users in your organization will be logged out and Figma will be inaccessible until access is restored.

Note: At this time, Figma doesn’t fully support offboarding from EKM. If EKM is disabled, existing files remain encrypted with your key and you’ll need to maintain access to that key for future decryption.

## Guest access expiration

[Guest](https://help.figma.com/hc/en-us/articles/4420557314967-Members-versus-guests) expiration helps organization admins control how long external collaborators can access their organization.

By default, guests don’t expire and can remain in the organization indefinitely. With Governance+, admins can choose to add expiration dates for guests—either individually or by setting a plan-wide default that applies to new guests going forward.

### How it works

Guest access expiration includes two related controls:

- Per-guest expiration: By default, guests have no expiration date. Admins can add, update, or remove an expiration date for guests at any time, individually or in bulk.
- Plan-wide default (optional)**:** Organization admins can set a default number of days that applies to newly invited guests.
  - This setting only affects guests who join after the default is set.
  - A guest’s expiration countdown begins when they join the organization.

Here are some additional details about guest expiration:

- When a guest reaches their expiration date, they’re automatically removed from the organization and any paid seat they occupied returns to the available pool of seats for others to use.
- Expiration dates appear in the [**People** tab](https://help.figma.com/hc/en-us/articles/4420842863255-View-members-and-guests) of your admin, and all expiration-related changes are recorded in the [activity log](https://help.figma.com/hc/en-us/articles/360040449533-View-and-export-activity-logs).
- Guests that are within two weeks of their expiration date see an in-product banner that indicates how much time remains before their access ends.

### Set default duration for guest access

Organization admins can optionally set a default duration (in days) that applies to newly invited guests.

To set a default guest expiration:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the  **Settings** tab.
3. Under **External access**, open **Guest membership**.
4. Find **Set default duration for guest access**, enter a number of days, and click **Save**.

### Change a guest’s expiration date

Admins can manage expiration dates for guests directly from the admin dashboard. They can apply expiration dates individually or in bulk.

**Organization admins**

To change a guest’s expiration date:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**
   and select the
    **People**
   tab.
2. Locate and select the guest to open the side panel with member details.
3. Under **Guest access expiration date**, click
   **Change**. Enter a date and click **Save**.
   To make a guest permanent, select
   **Remove expiration date**
   instead. You can re-add an expiration date at any time.

![change a guests expiration date from the flyout in the people tab.](https://help.figma.com/hc/article_attachments/38140828424727)

To bulk apply or remove expiration dates:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**
   and select the
    **People**
   tab.
2. Select the checkboxes next to the guests you want to update.
3. In the bulk action bar, select
   **Set guest expiration date**.
4. Enter a date and click **Save**.
   To make a guest permanent, select
   **Remove expiration date**
   instead. You can re-add an expiration date at any time.

**Workspace admins**

Workspace admins can manage guest expiration for users in workspaces
they
manage.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**
   in the left sidebar.
2. Select the relevant workspace in the sidebar.
3. Select the **Members** tab.
4. Locate and select the guest to open the side panel with member details.
5. Under **Guest access expiration date**, click
   **Change**. Enter a date and click **Save**.
   To make a guest permanent, select
   **Remove expiration date**
   instead. You can re-add an expiration date at any time.

To bulk apply or remove expiration dates:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click **Admin**
   in the left sidebar.
2. Select the relevant workspace in the sidebar.
3. Select the **Members** tab.
4. Select the checkboxes next to the guests you want to update.
5. In the bulk action bar, select
   **Set guest expiration date**.
6. Enter a date and click **Save**.
   To make a guest permanent, select
   **Remove expiration date**
   instead. You can re-add an expiration date at any time.

## AI hosting controls

FedRAMP limits access to particular models in Bedrock, so this feature is not available in Figma for Government.

AI hosting controls lets Governance+ organization admins choose how AI traffic is routed.

When enabled:

- For all features governed by the AI toggle, when the feature needs to leverage an AI model, we route the request to a multi-tenant Amazon Web Services account that Figma owns
- We then process the request on Amazon Web Services (AWS) using models hosted in Figma's AWS environment, including Amazon Bedrock and Amazon SageMaker. AI data won't be sent to non-AWS providers. This means AI data won't be sent to APIs outside of Figma’s AWS environment e.g. OpenAI, Anthropic, or Google Cloud Platform etc.

### Enable AI hosting controls

Organization admins can restrict AI traffic for an entire organization:

1. From the admin, go to **settings.**
2. Under in the AI section, click on **AI controls.**
3. In the AI features modal, if AI is enabled anywhere in the organization (i.e. at the plan-level and/or for any workspace), you can choose to restrict AI traffic by toggling on **Restrict AI traffic to Figma’s AWS environment**. This control governs all traffic in the plan, regardless of where it originated. If AI is disabled everywhere, you cannot restrict AI traffic.

Be aware that when traffic is restricted, output quality may vary and some AI features will not be available. The list of unavailable AI features may change over time:

1. Remove Object
2. Separate Layers
3. Boost Resolution
4. Edit Image
5. Expand Image
6. Vectorize

## Developer Logs API

The **Developer Logs API** lets you fetch a granular log of API calls made to the REST API or MCP server within your organization. This is a companion to the more low-volume, high-signal security and compliance logs available through Activity Logs.

For setup and implementation, refer to the Developer Logs API documentation:

- **Figma Enterprise:** [developers.figma.com](https://developers.figma.com/docs/rest-api/developer-logs/)
- **Figma for Government:** [developers.figma-gov.com](https://developers.figma-gov.com/docs/rest-api/developer-logs/)
