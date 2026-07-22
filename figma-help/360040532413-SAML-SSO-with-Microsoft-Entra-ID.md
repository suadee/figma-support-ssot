---
기술지원명: SAML SSO with Microsoft Entra ID
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: SAML SSO with Microsoft Entra ID
출처링크: https://help.figma.com/hc/en-us/articles/360040532413-SAML-SSO-with-Microsoft-Entra-ID
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Supported on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only organization admins can set up SAML SSO.

You need an existing [Microsoft Entra ID](https://Azure.microsoft.com/en-us/services/active-directory/) account

Organizations that manage users with Microsoft Entra ID can configure [SAML SSO in Figma](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO). Figma supports both identity (Entra ID) and service (Figma) initiated configurations.

We recommend having both Figma and Entra ID open in separate tabs. This allows you to switch between them throughout the setup process.

**Configure SAML in an active organization**

Microsoft recommends testing SAML configurations in a sandbox environment. However, there isn’t a way to create a sandbox or test environment in Figma. We recommend testing the Figma application with a test user, such as yourself, or a small group of users first.

To make sure existing users can still access Figma during the set up process, [set the login and authentication method](https://help.Figma.com/hc/en-us/articles/360052497994) to **Members may log in with any method, including email and password (default)**.

Once everything is up and running, you can update this setting to **Members must log in with SAML SSO**. Learn more in Microsoft's tutorial: [Microsoft Entra SSO Integration with Figma](https://docs.microsoft.com/en-us/Azure/active-directory/saas-apps/Figma-tutorial).

# Set up SAML SSO

## Open SAML in Figma

Open your organization's SAML SSO settings in Figma. We'll come back to this page to configure SAML SSO in Figma, later on in the process.

1. Open the organization in Figma.
2. In the sidebar, select  **Admin.**
3. Select the **Settings** tab.
4. In the **Login and provisioning** section, click **Authentication**.
5. Make sure authentication is set to **Members may log in with any available method..**. Click **Done**.
6. From the **Login and provisioning** section, click **SAML SSO**.
7. Figma opens a modal dialog with some key information for the SAML process.
   - **Tenant ID**: `123456789123456789`
   - **SP entity ID**: `https://www.figma.com/saml/123456789123456789`
   - **SP ACS URL**: `https://www.figma.com/saml/123456789123456789/consume`

Figma uses your Tenant ID to generate your **SP identity ID** and **SP ACS URL**. You’ll need these when configuring SAML in Entra ID. You’ll use the **SP entity ID** to create a URL for service-provider initiated authentication.

## Add Figma to Entra ID

Add Figma to your Entra ID portal.

1. Open Entra ID in the overview page
2. Select **Enterprise applications**
3. Land on the **All applications** section
4. Click **Add application** to browse Entra ID Gallery
5. Search for Figma and select the correct result
6. Click **Create** to add the application to Entra ID
7. Entra ID will show a success message and redirect you to the Figma application overview: ![Figma application added successfully message](https://help.figma.com/hc/article_attachments/6729415584407)

## Assign a test user

Assign a test user to Figma in Entra ID. This allows you to complete the SAML setup process and test the application.

1. Select **Assign users and groups** from the options.
2. Click **+ Add user/group** to open the assignments page.
3. Click **Users and groups**, click **None selected**.
4. Search for test user. We recommend using your own account so that you can test the login at the end of the setup process.
5. Click to add and return to the assignments page.
6. Click **Assign** button to return to application page.

## Configure SAML in Entra ID

Set up SAML in Entra ID. You’ll need the Tenant ID Figma provides to complete the process.

We recommend having both Figma and Entra ID open in separate tabs. This allows you to switch between them throughout the setup process.

1. Select **Single sign-on** in panel
2. Select **SAML** from options
3. Under **Basic SAML Configuration**, click **Edit** to make changes
4. *Switch to the Figma tab in your browser.*
5. Next to the **Tenant ID**, click **Copy**
6. *Switch to the Entra ID tab in your browser.*
7. Under **Identifier (Identity ID)**, click **Add identifier**
8. Type in `https://www.figma.com/saml/` in the field provided, then paste your Tenant ID to complete the URL.
9. Copy the entire URL from the field to your clipboard.
10. Under **Reply URL (ACS link)**, click **Add reply URL**.
11. Paste the identity URL in the field, then add `/consume` to the end of the link.
12. In the **Sign on URL (Optional)** field, paste the identity URL again, then add `/start` to the end of the link.
13. Click **Save** at the top of the screen: ![Save icon and label under Basic SAML Configuration heading](https://help.figma.com/hc/article_attachments/6729438996503)
14. Click **X** in the top-right corner to return to the Figma application page.

## Configure SAML in Figma

Now you can configure SAML in Figma. You’ll need the metadata link from Entra ID to complete the process in Figma.

1. Open the Figma application in Entra ID.
2. Scroll down to the **SAML Signing Certificate** section.
3. Next to the **App Federation Metadata URL**, click **Copy**.
4. *Switch to the Figma tab in your browser.*
5. Click **Configure SAML** in the dialog.
6. Select **Microsoft Entra ID** from the options.
7. Paste the link in the **IdP metadata URL** field.
8. Click **Review** to make sure the details are correct.
9. Check the box next to **This information is correct**.
10. Click **Configure SAML SSO**. Figma will return you to the **Settings** tab where you’ll see SAML SSO is now enabled: ![Settings page in organization Admin with SAML SSO enabled](https://help.figma.com/hc/article_attachments/6729440614295)

## Map user attributes

Map your user attributes between Figma and Entra ID.

Figma expects certain attributes in the SAML response. Some of these are required attributes and some are pre-populated but optional. You can review and adjust the optional attributes.

1. Switch to the Entra ID tab in your browser and make sure you’re on the **SAML sign-on** page.
2. Find the **Attributes & Claims** section. Click the pencil icon to edit these attributes.
3. You can review and adjust any optional attributes. Make sure you don’t remove or adjust any required attributes.

| Name | Source attribute | Required |
| --- | --- | --- |
| GivenName | user.givename | Required |
| Surname | user.surname | Required |
| Emailaddress | user.mail | Required |
| Name | user.userprincipalname | Required |
| Unique User Identifier | user.userprincipalname | Required |
| displayName | user.displayname | Pre-populated (Optional) |
| title | user.jobtitle | Pre-populated (Optional) |
| emailaddress | user.mail | Pre-populated (Optional) |
| familyName | user.surname | Pre-populated (Optional) |
| givenName | givenName | Pre-populated (Optional) |
| userName | user.userprincipalname | Pre-populated (Optional) |
| externalId | user.objectId | Pre-populated (Optional) |

## Test the application

With both Figma and Entra ID configured you can test the application. You’ll need to test this process with the user you added earlier.

If you skipped this step, you’ll need to [assign a user to Figma ↑](#assign-test-user) first. We recommend adding your own account.

1. Switch to the Entra ID tab in your browser and make sure you’re on the **SAML sign-on** page.
2. Select **Test this application** at the top of the page. ![Test application icon and button in row of menu items](https://help.figma.com/hc/article_attachments/6729449129111)
3. Click the **Test sign in** button. Entra ID will open a new tab and log you into Figma using SAML SSO.

## Make SAML SSO mandatory

If the test process was successful, you can now allow other members to log in using their SAML SSO credentials. If you want to make log in via SAML mandatory for members, you can update the [organization's authentication settings](https://help.figma.com/hc/en-us/articles/360052497994).

1. Open the organization in Figma.
2. In the sidebar, select  **Admin** and go to the **Settings** tab.
3. In the **Login and provisioning** section, click **Authentication**.
4. Make sure authentication is set to **Members may log in with any available method..**. Click **Done**.

# Set up automatic provisioning with SCIM

You'll need an API token from Figma to set up SCIM in Entra ID. We recommend having both Figma and Entra ID open to make it easier to copy between them.

### Generate Figma API token

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select **Settings** at the top of the screen.
3. In the **Login and provisioning** section, click **SCIM provisioning**.
4. Click **Generate API Token** in the dialog.
5. Copy the API token to your clipboard. You'll need this to complete the process in Entra ID.

### Configure SCIM in Entra ID

You'll need your **Tenant ID** and **API Token** from Figma. Remember to swap the `<TENANT ID>` placeholder in the URL below with the **Tenant ID** Figma generated.

Note: These instructions are modified from **Microsoft's Entra ID Tutorial**. Check out [Configure Figma for automatic user provisioning](https://docs.microsoft.com/en-us/Azure/active-directory/saas-apps/Figma-provisioning-tutorial) for screenshots and detailed explanations.

1. In your Entra ID Portal go to **Enterprise Applications > All Applications**
2. Select the **Figma** app.
3. Go to the **Manage** section and select **Provisioning**.
4. Set the **Provisioning Mode** to **Automatic**.
5. Enter the following details in the **Admin Credentials** section:
   1. Enter the URL in the **Tenant URL** field: `https://www.figma.com/scim/v2/<TenantID>`
   2. Enter the **API Token** in the Secret Token field.
   3. Click **Test Connection** to make sure that Entra ID can connect to Figma.
6. Enter the desired email address in the **Notification Email** field.
7. Check the box next to **Send an email notification when a failure occurs** and click **Save** to apply.
8. In the **Mappings** section, select **Synchronize Entra ID Users to Figma**.
9. In the **Attribute Mappings** section, review the **Entra ID Attribute** and the corresponding **Figma Attribute**.
10. Click the **Save** button to apply any changes.
11. Under **Settings**, toggle the **Provisioning Status** > **On**.
12. Define which users and/or groups you would like to provision to Figma. Choose from:
    - Sync all users and groups
    - Sync only assigned users and groups
13. Click **Save** to apply your provisioning settings.

**Warning**: If a user is **deactivated** in Entra ID, this will **remove** their Figma account from your organization and they will lose all permissions. If you reactivate the user in Entra ID and re-add them to your organization, someone will need to manually add them to their previous teams, projects and files.

# Let your users know about the change

The first time a user logs into Figma using SSO, or after they are provisioned via SCIM, they'll receive a verification email from SendGrid. This email contains a unique 6-digit pin, which they'll use just once as an additional security measure during their initial login.

To make sure users don't mistake the email for spam or a phishing attempt, you may wish to let them know about this extra step in advance.
