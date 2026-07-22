---
기술지원명: SAML SSO with OneLogin
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: SAML SSO with OneLogin
출처링크: https://help.figma.com/hc/en-us/articles/360040533373-SAML-SSO-with-OneLogin
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Organization admins only

You need to have an existing OneLogin account

Organizations that have stricter security requirements can configure SAML SSO. [**Learn more about SAML SSO in Figma →**](https://help.figma.com/hc/en-us/articles/360040532333)

You can use OneLogin as your identity provider to authenticate and provision users. Figma supports SAML SSO initiated from both OneLogin (identity provider) and Figma (service provider).

## Add Figma to OneLogin

First, you'll need to add the Figma App to your OneLogin account.

1. Log in to your OneLogin account and go the **Administration** section.
2. Head over to the **Apps** page and select **Add Apps**.
3. Search for **Figma** in the **Find apps** field.
4. On the **Info** tab, click **Save** to add the app to your Company Apps.
5. You will then be able to access the additional configuration settings. Click on the **SSO** tab:
6. Copy the contents of the **Issuer URL** field:

   ![The SSO tab in the Figma app in OneLogin](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cdc67730428634b855943a4/file-EnBXDP73AQ.png)

## Set up SAML SSO in Figma

1. Open Figma in the file browser.
2. Click **Admin**.
3. Select **Settings** at the top of the screen.
4. In the **Login and provisioning** section, click **SAML SSO**.
5. Click **Configure SAML** and select **OneLogin** from the options.
6. Enter the **IdP Metadata IRL** from OneLogin and click **Review**.
7. Check the box to confirm **This information is correct...** and click **Configure SAML SSO**.
8. Click the **Copy** link next to your **Tenant ID**. You'll need this to complete the set up process in OneLogin.

You need to decide if logging in via SAML SSO is mandatory, or if users can still login via email address and password. **[Learn more about authentication options →](https://help.figma.com/hc/en-us/articles/360046005913)**

## Configure SAML SSO in OneLogin

Once you've received your confirmation and **Tenant ID**, you can complete the configuration process in OneLogin.

1. Go back to the Figma App in OneLogin (**Administration > Apps > Figma**)
2. Go to the **Configuration** Tab for the Figma app:

   ![The Configuration tab in the Figma app in OneLogin](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cdc66f70428634b8559439f/file-1Pup3gf33m.png)
3. Enter the **Tenant ID** that you copied from Figma.
4. Click **SAVE** to complete the process.

## Set up automatic provisioning via SCIM

To set up automatic provisioning you will need to:

1. [Generate an API Token in Figma](#h_47145034-57c1-484b-8401-799de23e9937)
2. [Configure Automatic Provisioning in OneLogin](#h_35882e7c-c16c-4df8-ad9f-1bf74422c0c5)
3. [Map Custom Attributes](#h_79a8e6e6-9568-47f6-9693-f3f0b3ca5148)

Tip! We recommend having both of these windows open at the same time, to make that process easier.

### Generate an API token in Figma

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin**.
2. Select **Settings** at the top of the screen.
3. In the **Login and provisioning** section, click **SCIM provisioning**.
4. Click **Generate API Token** in the dialog.
5. Copy the API token to your clipboard. You'll need this to complete the process in OneLogin.

### Configure SCIM in OneLogin

You'll need your **API Token** from Figma

1. Open the Figma app in OneLogin.
2. Go to the **Configuration** Tab for the Figma app.
3. Under **API connection**, enter your API token in the **SCIM Bearer Token** field.
4. Click **ENABLE**.
5. Go to the **Provisioning** tab and check the box next to **Enable Provisioning**.
6. Select which provisioning actions you want to require administrator approval for. You can choose to enable this for:
   - Create User
   - Delete User
   - Update User
7. Decide the appropriate action for **When user accounts are suspended in OneLogin**..

   ![The provisioning tab in the Figma app with the above settings in place and suspend chosen for the appropriate action](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cdc66eb0428634b8559439d/file-01oD48mjFL.png)

**Warning**: If a user is **deactivated** in OneLogin, this will **remove** their Figma account from your organization and they will lose all permissions. If you reactivate the user in OneLogin and re-add them to your organization, someone will need to manually add them to their previous teams, projects and files.

### Add custom attributes

Some Figma attributes are mapped to OneLogin attributes by default:

- `Email`
- `First Name`
- `Last Name`
- `NameID`
- `SCIM Username`
- `Title`
- `Manager`
- `Department`

Other SCIM Enterprise User attributes are optional. You will need to add these as custom user fields if you want to include them in your provisioning:

- `employeeNumber`
- `costCenter`
- `organization`
- `division`

To create a custom field in OneLogin:

1. Login to your OneLogin account.
2. Go to **Users > Custom User Fields** in the main menu:
3. Complete the **New User Field** inputs.
4. Click **SAVE** to apply your changes.

## Let your users know about the change

The first time a user logs into Figma using SSO, or after they are provisioned via SCIM, they'll receive a verification email from SendGrid. This email contains a unique 6-digit pin, which they'll use just once as an additional security measure during their initial login.

To make sure users don't mistake the email for spam or a phishing attempt, you may wish to let them know about this extra step in advance.
