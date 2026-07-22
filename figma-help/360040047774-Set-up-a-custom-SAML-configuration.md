---
기술지원명: Set up a custom SAML configuration
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Set up a custom SAML configuration
출처링크: https://help.figma.com/hc/en-us/articles/360040047774-Set-up-a-custom-SAML-configuration
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only Organization Admins can set up SAML SSO.

You must use SAML 2.0 to set up SAML SSO with Figma.

Organizations that have stricter security requirements can configure SAML SSO. **[Learn more about SAML SSO in Figma →](https://help.figma.com/hc/en-us/articles/360040532333)**

If you do not use one of our supported identity providers, you can set up a custom SAML configuration. You must use SAML 2.0, Figma doesn't support earlier versions of SAML.

Note: you will need the following information from your identity provider to set up SAML SSO in Figma:

- **IdP Entity Id:** This lets us know which Identity Provider you are using.
- **IdP SSO Target URL:** We will use this link to connect to the Identity Provider when someone from your Organization attempts to login via SAML SSO.
- **Signing Certificate:** Usually called the X509 certificate. We use this to verify your Organization via your Identity Provider.

## Set up SAML SSO in Figma

You need to decide if logging in via SAML SSO is mandatory, or if users can still login via email address and password. **[Learn about authentication options →](https://help.figma.com/hc/en-us/articles/360046005913)**

1. Open Figma in the file browser and select **Admin** in the sidebar.
2. Select **Settings** at the top of the screen.
3. In the **Log in and provisioning** section, click **SAML SSO**.
4. Figma will generate the information you need to complete the process with your identity provider. Find this in the **Your configuration details are** section.
5. In the **Identity provider** section, select **Other**.
6. Enter the details from your identity provider:
   - **IdP Entity ID**
   - **IdP SSO Target URL**
7. Upload your **Signing certificate** and click **Review**.
8. Check the box to confirm **This information is correct...** and click **Configure SAML SSO**.

## Complete the set up with your identity provider

1. View the details of your SAML SSO configuration in Figma. You'll need these to complete the configuration process with your Identity Provider:
   - The **SP Entity ID**
   - The **SP ACS URL**
2. Make sure to configure the **NameId** using the following format:  `Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"`

Tip: You can address any typos, or update your SAML SSO configuration at any time. Return to these settings and click the **Edit configuration** button. [**Learn more about editing your SAML SSO settings →**](https://help.figma.com/hc/en-us/articles/360040532333)

## Let your users know about the change

The first time a user logs into Figma using SSO, or after they are provisioned via SCIM, they'll receive a verification email from SendGrid. This email contains a unique 6-digit pin, which they'll use just once as an additional security measure during their initial login.

To make sure users don't mistake the email for spam or a phishing attempt, you may wish to let them know about this extra step in advance.
