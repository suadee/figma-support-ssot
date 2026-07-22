---
기술지원명: Set up OIDC for Okta XAA
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Set up OIDC for Okta XAA
출처링크: https://help.figma.com/hc/en-us/articles/41992841175959-Set-up-OIDC-for-Okta-XAA
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans.](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Organization admins only.

Normally, the Figma MCP server requires each user to follow an OAuth login flow to get access. However, you may want to manage this access centrally, so members sign in once through your identity provider and aren't interrupted by repeated login and consent prompts.

You can do this with **Cross App Access (XAA)**. XAA enables enterprise-managed authorization, a way to centralize MCP access in Okta and remove sign-in friction. Instead of each member authorizing the Figma connector on their own, access is brokered by Okta: a member signs in once through Okta, and Claude can then work across approved MCP servers without asking that member to authorize again.

To set up OIDC for Okta XAA:

1. Set up [SAML SSO with Okta](https://help.figma.com/hc/en-us/articles/360040532353) for your organization.
2. Follow Anthropic's guide to [configure MCP connectors for a whole organization](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization) and obtain your OIDC issuer URL.
3. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin**.
4. Select **Settings** in the left sidebar.
5. In the **Login and provisioning** section, click **OIDC Issuer URL.**
6. Paste the issuer URL you received following Anthropic's guide.
7. Click **Save**.
