---
기술지원명: Guide to SAML SSO
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Guide to SAML SSO
출처링크: https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360039957374)

Organization admins only

Single Sign On (SSO) allows users to log into many applications or websites using an **identity provider**. Security Assertion Markup Language (SAML) is a security standard for managing authentication and access.

In a SAML SSO set up, the identity provider manages the organization's user accounts and credentials. The **service provider** (Figma) is the app or website that provides services to the user or organization.

When using SAML SSO, members log in to their Figma organization using the organization's identity provider.

How SAML SSO works:

1. Member attempts to log in to Figma via SAML SSO
2. Figma sends a SAML request to the identity provider
3. The identity provider checks this member's credentials
4. The identity provider sends a response to Figma to verify the member's identity
5. Figma accepts the response and logs the member into their Figma account

**Note**: Figma uses **SAML 2.0** for all SAML SSO configurations. This includes configurations with supported identity providers and any custom configurations.

**Note**: Governance+ for Figma Enterprise supports multiple identify providers (IdPs).

[Learn more about Governance+ for Figma Enterprise](https://help.figma.com/hc/en-us/articles/31825370509591).

## Set up SAML SSO

The process for configuring SAML will depend on your specific identity provider. We've outlined the general process for implementing SAML SSO below.

SAML SSO only applies to members of a Figma organization. Guests can log in via Google SSO or their email and unique password, regardless of an organization's SAML SSO settings.

**For Figma for Government users:** All users using the [Figma for Government solution](https://help.figma.com/hc/en-us/articles/22932461365015) are required to use SAML SSO. Figma marketplace identity provider applications, such as Microsoft or Okta, are not compatible with Figma for Government. Please use the custom app SAML SSO setup flow, as described below, for your identity provider.

### 1. Confirm domains

Adding and verifying domains via [domain capture](https://help.figma.com/hc/en-us/articles/360045953273) lets us know who to treat as a member and who to treat as a guest.

For example: ACME Corp has three domains registered to their organization: `acme.org`, `acmecorp.org`, and `dev.acme.org`.

Anyone with an `acme.org`, `acmecorp.org`, or `dev.acme.org` email address is a member. Members can log in via SAML SSO.

Anyone with an email address that doesn't match those domains is a guest and can't log in via SAML. For example: `name@gmail.com` or `name@notyourdomain.com`

Note: If you plan on using SAML SSO, you need to register every domain you want to use in Figma with your identity provider. Email aliases do not work with SAML SSO.

Caution: To keep access to existing files and projects, members need to have an account registered to their company email. We recommend ensuring everyone is using the right emails in Figma before you set up SAML SSO.

### 2. Add Figma to your identity provider

When you add Figma to your identity provider, they will provide you with a **Metadata URL**. This is an XML link that Figma uses to connect to your identity provider and authenticate users when they login.

Figma supports dedicated integrations with the following identity providers:

- [Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413)
- [Okta](https://help.figma.com/hc/en-us/articles/360040532353)
- [OneLogin](https://help.figma.com/hc/en-us/articles/360040533373)
- [Google Workspace](https://help.figma.com/hc/en-us/articles/360040047614)
- [Active Directory Federation Services (AD FS)](https://help.figma.com/hc/en-us/articles/360048269533)

Note: You can also set up a custom SAML configuration with a provider that isn't on this list. This will involve setting up a custom app with your identity provider. [**Set up a custom SAML configuration →**](https://help.figma.com/hc/en-us/articles/360040047774)

### 3. Turn on SAML SSO in Figma

Next, you'll need to set up SAML SSO in Figma. This will:

- Turn on SAML SSO for your organization
- Connect your identity provider to your Figma account
- Let you choose what methods members can use to log in

You'll need to decide if logging in via SAML SSO is mandatory, or if users can still login via email address and password. We recommend you allow logging in via any method during the set up process.

If you want to set up Google SSO, all users must login via Google SSO. There is no way to make this optional or enable this for only some users. [**Set login or authentication method →**](https://help.figma.com/hc/en-us/articles/360052497994)

### 4. Set up SAML SSO in your identity provider

Complete the rest of the set up process with your identity provider.

- [SAML SSO with Okta](https://help.figma.com/hc/en-us/articles/360040532353-SAML-SSO-with-Okta "SAML SSO with Okta")
- [SAML SSO with Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413-SAML-SSO-with-Azure-Active-Directory "SAML SSO with Azure Active Directory")
- [SAML SSO with OneLogin](https://help.figma.com/hc/en-us/articles/360040533373-SAML-SSO-with-OneLogin "SAML SSO with OneLogin")
- [SAML SSO for AD FS](https://help.figma.com/hc/en-us/articles/360048269533-Set-up-SAML-SSO-for-ADFS "Set up SAML SSO for ADFS")
- [SAML SSO with Google](https://help.figma.com/hc/en-us/articles/360040047614-Authenticate-with-Google#SAML-SSO)
- [Set up a custom SAML configuration](https://help.figma.com/hc/en-us/articles/360040047774-Set-up-a-custom-SAML-configuration "Set up a custom SAML configuration")

**Note**: Besides the **username** or **nameid**, Figma supports four attributes in a SAML assertion: **givenName**, **familyName**, **displayName**, and **title**. Figma will ignore any additional attributes.

### 5. Set up SCIM provisioning (optional)

All SAML SSO configurations support "Just In Time" (JIT) or manual provisioning. JIT provisioning allows Figma to **create** and **update** users in Figma.

- When creating a user, Figma uses information from the four supported attributes in the SAML response from the identity provider.
- When updating a user in the identity provider, changes will apply when the user next logs in.

You can choose to enable automatic provisioning via SCIM. SCIM pushes changes immediately and allows you to **import** and **deactivate** users.

- **Supported identity providers**: you can enable provisioning via SCIM. We include instructions for setting up automatic provisioning via SCIM in each provider's article.
- **Custom SAML configuration**: you can set up SCIM with your chosen identity provider.[**Learn more about setting up a custom SCIM configuration →**](https://help.figma.com/hc/en-us/articles/360048514653)

On the Organization plan, it's not possible to assign a person's seat type outside of Figma. Figma gives everyone who joins the organization a free View seat. [Learn more about free and paid seats in Figma →](https://help.figma.com/hc/en-us/articles/360039960434)

On the Enterprise plan, you can set members' seats via SCIM. This allows you to set someone's seat before they join the organization.

Need to make changes to your SAML SSO settings? You can [edit your settings](https://help.figma.com/hc/en-us/articles/4420928740503/) at any time.

### 6. Let your users know about the change

When a member logs into Figma via SAML SSO, they may be asked to verify their email address. The verification email comes from SendGrid and contains a unique 6-digit code.

How often users are asked to verify depends on whether your organization's email domain is verified in Figma:

- **Unverified domain:** Members are prompted to enter a verification code the first time they log in via SSO on each new device or browser. Once verified, a device is remembered — but clearing browser cookies or using a new device will trigger verification again.
- **Verified domain:** Members are not required to complete email verification during sign-in.

To remove per-device verification for your users, [verify your organization's domain](https://help.figma.com/hc/en-us/articles/360045953273).
