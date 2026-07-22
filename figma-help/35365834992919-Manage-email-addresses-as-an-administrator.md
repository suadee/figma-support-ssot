---
기술지원명: Manage email addresses as an administrator
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage email addresses as an administrator
출처링크: https://help.figma.com/hc/en-us/articles/35365834992919-Manage-email-addresses-as-an-administrator
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Admins might need to change member email addresses for various reasons, such as a new domain, company rebrand, or a member's marriage. There are several ways to do this, and you only need to choose one.

## Before you begin

No matter which method you choose, Figma requires [domain verification](https://help.figma.com/hc/en-us/articles/360045953273-Manage-domain-capture-for-an-organization#h_01J3RESBMNAZX741MQD3BF49RM) for all domains involved in the email change. For example:

- If changing from dylan@domain.com to dylanfield@domain.com, domain.com needs to be verified
- If changing from dylan@olddomain.com to dylan@newdomain.com, both olddomain.com and newdomain.com need to be verified

Also, the new email address must be available and not currently used by any other Figma accounts. If an account with the new email already exists, you'll get an "email change conflict" error. If you own the account with the desired email address, please use our [support form](https://help.figma.com/hc/en-us/requests/new) for assistance.

## Methods for Changing Email Addresses

### Google SSO (for Professional, Organization, and Enterprise plans)

- If your members use Google SSO, you can change their email addresses through Google Workspace. Their email address will get updated upon their next Google SSO login.
- The member must have previously logged in using Google SSO so Figma can identify them with the new email.
- This method is ideal for plans that exclusively use Google SSO for member logins.

### SAML SSO (for Organization and Enterprise plans)

- Plans using SAML SSO can change member email addresses via their Identity Provider.
- Admins must have configured a unique identifier for the user using the SAML attribute externalId. Refer to our [SAML SSO setup guide](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) for detailed instructions.
- With a unique externalId, Figma can identify the same user after their first login and update their email address upon subsequent SAML SSO logins.
- This method is best for plans that exclusively use SAML SSO for member logins.

### SCIM (for Organization and Enterprise plans)

- Plans with SCIM configured can use their Identity Provider to change member email addresses.
- This method doesn't require members to log in, as the email change is updated via the SCIM API, while still adhering to the prerequisites mentioned above.

### Figma Support (for Professional, Organization, and Enterprise plans)

- If none of the above methods are suitable, admins can use our [support form](https://help.figma.com/hc/en-us/requests/new) to get help.
- The support team can initiate an email change procedure once verification is complete.
