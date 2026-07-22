---
기술지원명: Manage seats via SCIM
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Manage seats via SCIM
출처링크: https://help.figma.com/hc/en-us/articles/360048787534-Manage-seats-via-SCIM
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Organizations using [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) can use SCIM to make sure that users have the correct permissions and billing status in Figma. To manage seat types via SCIM, you’ll need:

- Administrative access to your identity provider
- Automatic provisioning enabled

## Configure seat setting

The exact process for setting a seat type depends on your identity provider. If you use **Microsoft Entra ID** or **Okta**, please use the following guides:

- [Manage seats via SCIM using Okta](https://help.figma.com/hc/en-us/articles/22773906477591)
- [Manage seats via SCIM using Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/22766770509591)

If you use a different identity provider, we recommend using our [SCIM API guide](https://www.figma.com/developers/api#scim-api-guide) to set up seat management via SCIM.

**Note**: SAML SSO and SCIM only applies to [members](https://help.figma.com/hc/en-us/articles/4420557314967) of an organization, not [guests](https://help.figma.com/hc/en-us/articles/4420557314967).

Note: In March 2025, Figma introduced updates to how seats and other billing features work. If you previously managed seats via SCIM, you may need to take steps to [migrate your seats to the updated billing model](https://help.figma.com/hc/en-us/articles/30836745725975). You have until March 2026 to update your SCIM configuration to use the new seat types.
