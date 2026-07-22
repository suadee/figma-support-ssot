---
기술지원명: Manage domain capture for an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage domain capture for an organization
출처링크: https://help.figma.com/hc/en-us/articles/360045953273-Manage-domain-capture-for-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Domain capture lets you automatically add people with a company email address—like `@example.com`—to your Figma organization. This helps all your employees join the right organization and avoid accidentally working in silos.

### What to expect from domain capture

|  | Without domain capture | With domain capture |
| --- | --- | --- |
| New users | People can create Figma accounts without knowing there is a centralized organization available. | People who sign up for Figma from verified domains are automatically added as members to your organization. They can still create or join other Starter and Professional teams, or join other organizations. |
| Existing users | Existing Figma users may be spread across multiple organizations and teams. | Existing users with email addresses from your domains will get added to your organization.   - Any files in a user’s temporary **Drafts to move** space will automatically move into their **Drafts** in your organization. - Any files they’ve created in a Starter or Professional team will remain where they are. |

**Note**: Domain capture doesn’t prevent users from your domains from joining and working in external teams or organizations. However, with domain capture enabled, you can [restrict access to content from outside your organization](https://help.figma.com/hc/en-us/articles/12080587805719) on the Enterprise plan.

> #### **Example**
>
> ACME Corp has three domains registered to their organization: `acme.org`, `acmecorp.org`, and `dev.acme.org`. With domain capture turned on, anyone with an email address from those domains who makes a Figma account will join the ACME organization as a member. Anyone with an email address that doesn't match those domains—like `name@gmail.com` or `name@otherdomain.com`—can get invited to the organization as a guest.
>
> Domain capture wouldn’t be a good fit for ACME if they wanted to create multiple Figma organizations with members from the same email domains.

## Enable or disable domain capture

To enable domain capture, you need to specify the top-level domains or subdomains you’d like to capture, then [verify them](#h_01J3RESBMNAZX741MQD3BF49RM) by adding a unique code as a TXT record to the DNS records managed by your domain provider.

**Note:** It’s important to verify top-level domains and subdomains if they are both used in email addresses. For example, verifying `example.com` won’t capture people with `brand.example.com` email addresses.

When you enable domain capture, Figma immediately adds Figma accounts with matching domains as members to your organization. Each person will:

- Receive an email letting them know they’ve been added to the organization
- Join the organization with a View seat
- Keep access to other teams or organizations they’ve joined

Enable domain captureDisable domain capture

**Note:** Before you can enable domain capture,
you
must
[verify all the domains you’ve added](#h_01J3RESBMNAZX741MQD3BF49RM).

1. From the file browser, click
   **Admin**
   in the left sidebar.
2. Select the **Settings** tab.
3. Under **Login and provisioning**, click
   **Manage domains**.
4. Click the **Domain capture** banner.
5. Move the toggle into the on position.
6. Click **Save**.

To disable domain capture, we ask that you
[contact our support team](https://help.figma.com/hc/en-us/requests/new?ticket_form_id=360001731233)
to walk through the process together.

## Add and verify a domain

Before domain capture is enabledAfter domain capture is enabled

If domain capture is disabled—or you’re setting it up for the first time—you’ll
need to add domains in Figma, then verify them by adding a TXT record
to
your DNS records via your domain provider.

1. From the file browser, click
   **Admin**
   in the left sidebar.
2. Select the **Settings** tab.
3. Under **Login and provisioning**, click
   **Manage domains**.
4. Click **+ Domain**.
5. Enter one or more domains or subdomains and click **Add**.

Newly added domains appear on the **Domains** page with
**Unverified** status.

**Tip:** You can add domains and leave them unverified
if you don’t plan on using domain capture. In this case, anyone
invited
to your organization from these domains will join as a member
rather
than a guest.

**Note**: If your organization enforces SAML SSO
and
has unverified email domains, members will be prompted to verify
their email address on each new device or browser they use to
sign
in. To remove this extra step, verify your domain.

![Domains management interface with verified and unverified domains listed, illustrating domain status in Figma.](https://help.figma.com/hc/article_attachments/25203176748055)

To verify each domain:

1. Click the **Unverified** status on the relevant domain.
2. Copy the text snippet.
3. Log in to your domain provider and create a new TXT record.
4. Return to the **Domains** page in Figma, click
   **Unverified** on the relevant domain, then click
   **Verify**. The **Unverified** status will
   change to **Verified**.

**Note**: If you're not sure how to create a new
TXT
record in your domain provider, we recommend contacting a member
of your IT team for help.

If domain capture is enabled, you must verify and add domains in a single
step.

1. From the file browser, click
   **Admin**
   in the left sidebar.
2. Select the **Settings** tab.
3. Under **Login and provisioning**, click
   **Manage domains**.
4. Click **+ Domain**.
5. Copy the text snippet.
6. Log into your domain provider and create a new TXT record for each
   domain
   or subdomain.
7. Enter the domains or subdomains and click
   **Verify and add**.

**Note**: If you're not sure how to create a new
TXT
record in your domain provider, we recommend contacting a member
of your IT team for help.

**Note**: Once domain capture is enabled, you won’t
be able
to add a domain to your organization if it is already used in another
organization.

## Remove a domain

When you remove a captured domain, Figma converts everyone in your organization with accounts from that domain from members to guests.

**Warning**: [Guests have limited access to a Figma organization](https://help.figma.com/hc/en-us/articles/4420557314967), so removing a domain can be very disruptive to affected users. We recommend letting people know in advance about the change and how it may affect their access to Figma.

**Note**: Organization admins can’t remove the domain associated with their own Figma account. For example, `tyler@acme.org` won’t be able to remove the `acme.org` domain.

1. From the file browser, click  **Admin** in the left sidebar.
2. Select the **Settings** tab.
3. Under **Login and provisioning**, click **Manage domains**.
4. Hover over the domain you’d like to remove and click the  **More** menu.
5. Click **Remove**.
