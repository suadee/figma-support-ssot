---
기술지원명: Find users with Figma accounts outside your organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Find users with Figma accounts outside your organization
출처링크: https://help.figma.com/hc/en-us/articles/27503664218391-Find-users-with-Figma-accounts-outside-your-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you begin

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

If you're not using [domain capture](https://help.figma.com/hc/en-us/articles/360045953273) to automatically add users to your organization when they sign up for Figma, you can manually find and add them instead.

This helps your employees join the correct organization and avoid accidentally working in silos.

When you manually add an employee to your organization, they become a member of your organization in Figma. They’ll still have access to any other organizations or team they’re already a part of and can [switch between accounts](https://help.figma.com/hc/en-us/articles/1500005165741) as needed.

### 1. Add and verify a domain

Before finding Figma users from your domains, you need to verify the top-level domains or subdomains you manage. This involves adding a unique code to the DNS records managed by your domain provider.

[Learn how to add and verify a domain.](https://help.figma.com/hc/en-us/articles/360045953273-Manage-domain-capture-for-an-organization#h_01J3RESBMNAZX741MQD3BF49RM)

**Note**: Verifying top-level domains won't capture users with subdomain email addresses. For example, verifying [example.com](http://example.com/) won’t include people who signed up for Figma using [brand.example.com](http://brand.example.com/) email addresses.

### 2. Find users on the domain with Figma accounts outside your organization

![Domains panel displaying verified and unverified domains with a list of uncaptured Figma users for manual addition to an organization.](https://help.figma.com/hc/article_attachments/30653946073879)

Once you’ve verified domain, you can access a list of everyone with an active Figma account on that domain who is not currently in your organization.

**Note:** The list of uncaptured users will always be empty if you have [domain capture](https://help.figma.com/hc/en-us/articles/360045953273) enabled.

To view the list:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Click **Settings**.
3. In the **Login and provisioning** section, click **Manage domains**.
4. For each verified domain, click  **More** at the end of the row, then select **Manage domain**.
5. Select one or more users and click **Add to [Organization name]** from the menu that appears.

**Tip**: This list won’t include people with inactive Figma accounts who have previously been removed from your organization.
