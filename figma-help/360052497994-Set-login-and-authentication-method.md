---
기술지원명: Set login and authentication method
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Set login and authentication method
출처링크: https://help.figma.com/hc/en-us/articles/360052497994-Set-login-and-authentication-method
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on the [Organization and Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only organization admins can adjust the organization's log in and authentication settings.

Organization admins can choose what method members can use to log in to the organization. These settings will apply to any member that has an email address that matches your organization's domain(s).

You can update these settings at any time. If you want to make change to your SAML SSO configuration, you will need to temporarily update these settings to allow members to log in via any methods.

SAML SSO only applies to members of an organization. Guests can always log in to an organization using Google SSO or their email and password.

## Available methods

The authentication methods you can choose from in an organization are:

- Members may log in with any method, including email and password (default)
- Members **must** log in with a Google account
- Members **must** log in with SAML SSO

### Any method

When authentication is set to "Members may log in with any method (default)", members can log in using any method. This includes Google SSO, SAML SSO, or a company email and unique password.

To allow members to log in via SAML SSO, you still need to [configure SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333) for your organization.

You can also use this setting to prevent members being locked out during the configuration process. This is handy when you're setting up or updating your SAML SSO settings, or switching to another identity provider.

### Enforce Google SSO

If you are using Google Workspaces to manage your company email, you have two approaches available for authentication.

- **[Google SSO](https://help.figma.com/hc/en-us/articles/360040047614#sso):** Use Google's traditional single sign on (SSO) process. This allows members to log in using their Google managed email address and password.
- **[Google SAML SSO](https://help.figma.com/hc/en-us/articles/360040047614#SAML-SSO):** You can use Google as your identity provider to authenticate and provision users. Figma supports SAML SSO initiated from both Google and Figma.

### Enforce SAML SSO for members

Organizations with enhanced security requirements can configure SAML SSO.

SAML SSO lets you connect your external identity provider—like Google Workspace, Okta, OneLogin, or Microsoft Entra ID—to Figma. Members can then log in and authenticate using a third-party provider.

This also allows you to pre-provision members to Figma via SCIM. If you're on the Enterprise plan, you can also [set member seat types via SCIM](https://help.figma.com/hc/en-us/articles/360048787534).

Once you have configure SAML SSO, you can choose if this is optional or required:

- Select **Members must log in with SAML SSO** to make logging in via SAML SSO mandatory for members.
- Select **Members may log in with any method, including email and password** to make SAML SSO optional.

When you make SAML SSO mandatory, Figma will require members to use SAML SSO when they next log in. Guests can still use their company email address and password to access Figma.

## Set authentication method

Adjust the authentication method in the organization's admin settings.

1. Open the organization in Figma.
2. Select **Admin** in the sidebar.
3. Select the **Settings** tab at the top of the screen.
4. In the **Login and provisioning** section, click the **Authentication** setting.![Authentication option highlighted in the Login and Provisioning section of the Settings page](https://help.figma.com/hc/article_attachments/360086502913)
5. Select your desired method and click **Done** to apply.![Authentication modal with the methods available in an Organization](https://help.figma.com/hc/article_attachments/360085306814)
