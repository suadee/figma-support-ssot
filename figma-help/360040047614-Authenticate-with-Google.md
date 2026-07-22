---
기술지원명: Authenticate with Google
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Authenticate with Google
출처링크: https://help.figma.com/hc/en-us/articles/360040047614-Authenticate-with-Google
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Only organization admins can configure SSO.

If you are using Google Workspace to manage your company email, you have two approaches available for authentication.

- [**Google SSO**](#SSO): Use Google's traditional single sign on (SSO) process. This allows members to log in using their Google managed email address and password.
- [**Google SAML SSO**](#SAML-SSO): If you use SAML and SCIM with Google Workspace, you can set up a custom SAML SSO configuration with Figma.

# Google SSO

You can enable Google SSO in your Figma Organization under Admin > Settings > Login and provisioning > Authentication  . Members must use the **Log in with Google** option to log in using their Google-managed company email and password.

- Select **Members must sign in with a Google Account** to make Google SSO mandatory.
- Select **Members may log in with any method, including email and password** to make Google SSO optional.

Note: You can disable this requirement at any time, if required. Return to this page and select Members may sign in with any available method, including email and password instead. You will need to update your authentication method to this setting, if you want make changes to your SAML SSO or SCIM settings.

# Google SAML SSO

Organizations that have stricter security requirements can configure SAML SSO. [Learn more about SAML SSO in Figma →](https://help.figma.com/hc/en-us/articles/360040532333)

You can use Google as your identity provider to authenticate and provision users. Figma supports SAML SSO initiated from both Google (identity provider) and Figma (service provider).

## Add the Figma app to Google

To connect Figma and Google, you first need to add the Figma app to your Google Admin console. This will generate authentication details, which you'll need to configure SAML SSO in Figma.

1. Sign in to the Google Admin console as a super administrator.
2. Go to **Menu > Apps > Web and mobile apps**, then click **Add app**.
3. Search for **Figma** and select **Figma Web (SAML)** from the results.
4. Copy the **SSO URL** and **Entity ID**, and download the certificate from the Google Identity Provider details.
5. Leave the Google Admin console open; you’ll need it later to complete the setup.

## Set up SAML SSO in Figma

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin**.
2. Select **Settings** at the top of the screen.
3. In the **Login and provisioning** section, click **SAML SSO**.
4. Next to **Tenant ID**, click **Copy** and save this number—you’ll need it to finish setting up SAML in Google.
5. Click **Edit configuration**.
6. Under **Identity provider (IdP)**, select **Google Workspace**.
7. Paste the **Entity ID** from Google into the **IdP Entity ID** field.
8. Paste the **SSO URL** from Google into the **IdP SSO Target URL** field.
9. For **Signing certificate**, click **Choose file**.
10. Find and select the identity provider certificate you downloaded from Google.
11. Click **Review**, then check **This information is correct**.
12. Click **Configure SAML SSO** to save your settings.

Once you've set up SAML SSO, you can chose whether to require if for all members or allow other login methods. [Learn more about authentication options →](https://help.figma.com/hc/en-us/articles/360046005913)

## Set up Figma in Google

### **Complete the configuration in Google**

Now that SAML SSO is configured in Figma, you need to finish the setup in Google.

1. Return to the Google Admin console.
2. Enter the **ACS URL, Entity ID, and Tenant ID** from Figma.
3. Map Google directory attributes to Figma attributes (e.g., `givenName`, `familyName`, `email`). Click **Add Mapping** and select the additional fields you need.
4. To include group memberships:

   1. For **Group memberships,** click **Search for a group**, enter part of the name, and select it. There is a maximum of 75 groups.
   2. For **App attribute,** enter the corresponding groups attribute name for the service provider.

   The SAML response only includes groups the user is a member of. [Learn more about group membership mapping→](https://support.google.com/a/answer/11143403)
5. Click **Finish**.

### **Manage user access in Google Admin**

To turn a service on or off for certain users, you can organize their accounts into **organizational units** (to manage access by department) or **access groups** (to allow access across or within departments).

1. Sign in to the Google Admin console as a super administrator.
2. Go to **Menu** → **Apps** → **Web and mobile apps,** then click **Figma**.
3. Select **User access**.
4. To turn Figma on or off for everyone, select **On for everyone** or **Off for everyone**, then click **Save**.
5. To turn Figma on or off for a specific organizational unit:
   - On the left, select the **organizational unit**.
   - For **Service status**, select **On** or **Off**.
   - Choose one:
     - If the **Service status** is set to **Inherited**, click **Override** to keep the new setting even if the parent setting changes.
     - If the **Service status** is **Overridden**, click **Inherit** to revert to the parent setting, or click **Save** to keep the new setting.
6. To turn Figma **on for a specific group of users**, select an **access group**. [Learn how to customize service access using groups →](https://support.google.com/a/answer/9050643?sjid=17416331576959681013-NC)
7. Make sure your **Figma user account email domains match** the primary domain of your organization’s managed Google Account.

**Log in via Figma (service provider initiated SSO)** To start the SAML SSO process from Figma's end, head to the following URL: [https://www.figma.com/saml/[TenantID]/start](https://www.figma.com/saml/%5BTenantID%5D/start)

Make sure to replace `[Tenant ID]` with your Organization's actual Tenant Id!

## Verify SSO

Figma supports both identity provider-initiated and service provider-initiated SSO.

### Verify identity provider-initiated SSO

1. Sign in to the **Google Admin console** as a super administrator.
2. Go to **Menu** → **Apps** → **Web and mobile apps**, then click **Figma**.
3. Click **Test SAML Login**.
4. Figma should open in a separate tab. If it doesn’t, troubleshoot the error message and try again. [Learn more about troubleshooting SAML errors →](https://support.google.com/a/answer/6301076)

### Verify service provider-initiated SSO

1. Close all browser windows and open the Figma sign-in page.
2. Click **Use single sign-on**.
3. Enter your Google Workspace email address and click **Log in**. You should be redirected to the Google sign-in page.
4. Enter your Google Workspace credentials.
5. After your credentials are authenticated, Figma should open.

## Set up automatic provisioning with SCIM

Google supports automatic provisioning with SCIM. To set up SCIM you will need to generate an API token in Figma then add this to Google.

**Tip**: You can also use SCIM in Google to [manage seats for members in your organization](https://help.figma.com/hc/en-us/articles/360048787534) and [assign billing groups or workspaces](https://help.figma.com/hc/en-us/articles/25516157472791).

### Get API token and Tenant ID in Figma

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin** .
2. Select **Settings** at the top of the screen.
3. In the **Login and provisioning** section, click **SCIM provisioning**.
4. Click **Generate API Token** in the dialog.
5. Copy the API token to your clipboard. You'll need this to complete the process in Google.
6. Go back to the **Login and provisioning** section and click **SAML SSO**.
7. Next to **Tenant ID**, click **Copy** and save this number. You'll need this to complete the process in Google.
8. Click **Done**.

### Configure automatic provisioning in Google

1. Sign in to the **Google Admin console** as a super administrator.
2. Go to **Menu** → **Apps** → **Web and mobile apps**, then click **Figma**.
3. Select **Configure autoprovisioning**.
4. For **Access token**, paste the API token that you copied from Figma.
5. Click **Continue**.
6. For **Endpoint URL**, replace **{tenant-id}** with the Tenant ID you copied from Figma.
7. For **App attributes**, verify that all mandatory attributes are mapped to Google directory attributes.
8. To map a seat type attribute to a [custom attribute](https://support.google.com/a/answer/6208725), go to [Manage seats via SCIM](https://help.figma.com/hc/en-us/articles/360048787534-Manage-seats-via-SCIM).
9. To limit autoprovisioning to specific groups of users, in **Search groups**, enter part of the group name, select the group, and choose a scope.

   If a group has users from a secondary domain or from outside of your organization, those users are not provisioned.
10. Decide how long users have access to the app after the app is turned off for them or their Google Workspace account is suspended or deleted.

    You can suspend and then hard delete their account in Figma, or just suspend or hard delete them. You can set the time frame individually for each option and choose within 24 hours or after one, 7, or 21 days. You can choose options for each of these settings:

    - **When an app is turned off for a user**
    - **When a user is suspended from Google**
    - **When a user is deleted from Google**
11. Turn on **Autoprovisioning**.
12. Click **Turn on** to confirm.

**Note:** If you encounter delays or errors when setting up SAML SSO with Google, such as a "Not a SAML app" error, we recommend trying again after a few hours. You can also refer to Google's troubleshooting guide for common SSO issues.

## Let your users know about the change

The first time a user logs into Figma using SSO, or after they are provisioned via SCIM, they'll receive a verification email from SendGrid. This email contains a unique 6-digit pin, which they'll use just once as an additional security measure during their initial login.

To make sure users don't mistake the email for spam or a phishing attempt, you may wish to let them know about this extra step in advance.
