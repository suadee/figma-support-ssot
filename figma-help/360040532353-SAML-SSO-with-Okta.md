---
기술지원명: SAML SSO with Okta
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: SAML SSO with Okta
출처링크: https://help.figma.com/hc/en-us/articles/360040532353-SAML-SSO-with-Okta
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans.](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Organization admins only.

You will need to have an existing [Okta account](https://www.okta.com/) to set up SAML SSO with Okta.

Organizations that have stricter security requirements can configure SAML SSO. [**Learn more about SAML SSO in Figma →**](https://help.figma.com/hc/en-us/articles/360040532333)

You can use Okta as your identity provider to authenticate and provision users. Figma supports SAML SSO initiated from both Okta (identity provider) and Figma (service provider).

## Add the Figma app to Okta

To connect Figma and Okta, you will first need to add the Figma app to your Okta account. This will generate a **IdP Metadata URL**, which you'll need to configure SAML SSO in Figma.

1. Log in to your Okta account and head to the **Applications** page.
2. Select **Add Application** from the options.
3. Search for Figma and click the **Add button** to add Figma to your account.
4. Once installed, go to the **Sign On** page.
5. Right click on the **Identity Provider Metadata** link and choose **Copy link address**. The link should look like this: [`https://example.okta.com/app/abc123/sso/saml/metadata`](https://example.okta.com/app/abc123/sso/saml/metadata)

## Set up SAML SSO in Figma

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin**.
2. Select **Settings** at the top of the screen.
3. In the **Login and provisioning** section, click **SAML SSO**.
4. Click **Configure SAML** and select **Okta** from the options.
5. Enter the **IdP Metadata IRL** from Okta and click **Review**.
6. Check the box to confirm **This information is correct...** and click **Configure SAML SSO**.
7. Click the **Copy** link next to your **Tenant ID**. You'll need this to complete the set up process in Okta.

You need to decide if logging in via SAML SSO is mandatory, or if users can still login via email address and password. **[Learn more about authentication options →](https://help.figma.com/hc/en-us/articles/360046005913)**

## Set up Figma in Okta

Now you have your **Tenant ID**, you can complete the configuration process in Okta. You will need to configure the Figma app and mapping user attributes between applications.

### Configure SAML SSO

1. Open the Figma app in Okta.
2. Go to **Sign On** tab and click **Edit**.
3. Scroll down to the **Advanced Sign-On Settings** section.
4. Enter your **Tenant ID** in the field provided.
5. In the **Application username format** field, select **Email** from the options.
6. Click **Save** to complete the process.

Log in via Figma (service provider initiated SSO) To start the SAML SSO process from Figma's end, head to the following URL: [https://www.figma.com/saml/[TenantID]/start](https://www.figma.com/saml/%5BTenantID%5D/start)

Make sure to replace `[Tenant ID]` with your Organization's actual Tenant Id!

### Assign users to the application

Now you can start assigning users to the application. As part of this process, you may be asked to provide additional information about each user.

Figma supports some basic attributes, as well as attributes only available to SCIM Enterprise users.

Start adding users to the application in the **Assignments** tab on the far right.

#### Supported Basic Attributes

| Variable Name | External Name | External Namespace | Suggested Mapping |
| --- | --- | --- | --- |
| givenName | givenName | urn:ietf:params:scim:schemas:core:2.0:User | user.firstName |
| familyName | familyName | urn:ietf:params:scim:schemas:core:2.0:User | user.lastName |
| displayName | displayName | urn:ietf:params:scim:schemas:core:2.0:User | user.displayName |
| title | title | urn:ietf:params:scim:schemas:core:2.0:User | user.title |
| externalId | externalId | urn:ietf:params:scim:schemas:core:2.0:User | user.getInternalProperty("id") |

#### Supported SCIM Enterprise User Attributes

| Variable Name | External Name | External Namespace | Suggested Mapping |  |
| --- | --- | --- | --- | --- |
| employeeNumber | employeeNumber | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.employeeNumber |
| costCenter | costCenter | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.costCenter |
| organization | organization | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.organization |
| division | division | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.division |
| department | department | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.department |
| managerValue | manager.value | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.managerId |
| managerDisplayName | manager.displayName | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.manager |

Note: Missing the SCIM Enterprise user attributes? Figma applications added in Okta prior to June 2019 may need to be upgraded. Please [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new) for assistance.

1. Select **Account and file management** from the list of issues.
2. Select **Managing users and teams**.
3. Under **Subject,** type in 'SSO / SAML' and provide details of your request in the description box.

## Set up automatic provisioning with SCIM

Okta supports automatic provisioning with SCIM. To set up SCIM you will need to generate an API token in Figma then add this to Okta.

**Tip**: You can also use SCIM in Okta to [manage seats for members in your organization](https://help.figma.com/hc/en-us/articles/360048787534) and [assign billing groups or workspaces](https://help.figma.com/hc/en-us/articles/25516157472791).

### Generate an API token in Figma

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin** .
2. Select **Settings** at the top of the screen.
3. In the **Login and provisioning** section, click **SCIM provisioning**.
4. Click **Generate API Token** in the dialog.
5. Copy the API token to your clipboard. You'll need this to complete the process in Okta.

### Configure automatic provisioning in Okta

Make sure the following functions are enabled in Okta:

- Create users
- Update user attributes
- Deactivate users

**Warning**: If a user is **deactivated** in Okta, this will **remove** their Figma account from your organization and they will lose all permissions. If you reactivate the user in Okta and re-add them to your organization, someone will need to manually add them to their previous teams, projects and files.

1. Open the Figma app in Okta.
2. Go to the **Provisioning** tab in the Figma app.
3. Click the **Configure API Integration** button.
4. Check the box next to **Enable API Integration**.
5. Enter the **API Token** in the field provided.
6. Click **Test API Credentials** to ensure it's set up correctly.
7. When you get a success message, click **Save** to apply.
8. A few more options will now appear under the **Provisioning** section. Select **To App** in the left-hand menu.
9. Click **Save** to apply.

## Let your users know about the change

The first time a user logs into Figma using SSO, or after they are provisioned via SCIM, they'll receive a verification email from SendGrid. This email contains a unique 6-digit pin, which they'll use just once as an additional security measure during their initial login.

To make sure users don't mistake the email for spam or a phishing attempt, you may wish to let them know about this extra step in advance.
