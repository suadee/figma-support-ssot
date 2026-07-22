---
기술지원명: Set up automatic provisioning via SCIM
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Set up automatic provisioning via SCIM
출처링크: https://help.figma.com/hc/en-us/articles/360048514653-Set-up-automatic-provisioning-via-SCIM
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Organization admins only

You can set up SCIM on our supported providers ([Google Workspace](https://help.figma.com/hc/en-us/articles/360040047614-Authenticate-with-Google#SAML-SSO), [Okta](https://help.figma.com/hc/en-us/articles/360040532353), [OneLogin](https://help.figma.com/hc/en-us/articles/360040533373), and [Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413)), or a [custom SAML SSO set up](https://help.figma.com/hc/en-us/articles/360040047774).

All [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333) configurations in Figma support Just In Time (JIT) provisioning. This is manual provisioning, which only applies any changes when a user next logs into their account, not when an admin makes the changes. JIT supports **creating** and **updating** users in Figma.

You can choose to enable automatic provisioning with SCIM. SCIM pushes any changes you make to Figma, as soon as they happen. SCIM also supports importing and deactivating users, managing members’ seat types, and syncing groups from your identity provider for use in features like [workspaces](https://help.figma.com/hc/en-us/articles/7576392133527-Guide-to-workspaces), [billing groups](https://help.figma.com/hc/en-us/articles/19100885191191-Launch-billing-groups-in-an-organization), and [user groups](https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups).

## Get your API token and SCIM URL from Figma

To set up automatic provisioning you'll need to an API token in Figma and a SCIM URL. To make the set up process easier, we recommend having both Figma and your identity provider open at the same time.

### Generate an API token

You can generate an API token in your organization's admin settings:

1. Open Figma in the file browser and select **Admin** in the sidebar.
2. Select the **Settings** tab and navigate to the in the **Login and provisioning** section.
3. In the **Login and provisioning** section, click **SCIM provisioning**.
4. Click **Generate API token**.
5. Copy the **API token** value.

Note: If you’re using Governance+ for Figma Enterprise with multiple identify providers (IdPs), you’ll generate and manage SCIM API tokens from the **Identity providers** page instead. Each IdP configuration includes its own API token, which admins can generate or revoke directly from the Identity providers table in **Admin > Settings > Login and provisioning > Manage identify providers**.

[Learn more about Governance + for Figma Enterprise and multiple IdPs](https://help.figma.com/hc/en-us/articles/31825370509591).

### Find your Tenant ID

Your identity provider will need a SCIM base URL to configure SCIM. Your Tenant ID will make up part of this URL. You can find your Tenant ID in your organization's admin settings:

1. Open Figma in the file browser and select **Admin** in the sidebar.
2. Select the **Settings** tab and navigate to the in the **Login and provisioning** section.
3. In the **Login and provisioning** section, click **SAML SSO**.
4. Copy the **Tenant ID**.
5. Use your Tenant ID to create the SCIM base URL:
   - `https://www.figma.com/scim/v2/[tenantID]` (Figma organizations)
   - `https://figma-gov.com/scim/v2/[tenantID]` (Figma for Government organizations)

## Set up SCIM with your identity provider

The process for setting up provisioning depends on your identity provider.

### Configure SCIM

If you're using one of our **supported identity providers**, you can follow our help articles:

- [SAML SSO with Google Workspace](https://help.figma.com/hc/en-us/articles/360040047614-Authenticate-with-Google#SAML-SSO)
- [SAML SSO with Okta](https://help.figma.com/hc/en-us/articles/360040532353)
- [SAML SSO with Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413)
- [SAML SSO with OneLogin](https://help.figma.com/hc/en-us/articles/360040533373)

If you're using an **identity provider we haven't listed here**, you can still set up SCIM with Figma.

You'll need to [set up SAML SSO configuration](https://help.figma.com/hc/en-us/articles/360040047774) with your identity provider, before you can configure SCIM. This may require you to set up a custom application.

We aren't able to provide documentation for custom configurations. Please reach out to your identity provider for any assistance with a custom configuration.

**IMPORTANT**

As part of the set up process with your identity provider, you'll need to choose which provisioning functions to use. Make sure the following functions are enabled:

- Create Users
- Update User Attributes
- Deactivate Users

### Assign users to the application

When you set up automatic provisioning, you will be asked to assign users to the application.

As part of this process, you may be asked to provide additional information about each user. Figma supports the following common basic attributes, as well as some optional extras.

#### Basic attributes

*Scroll to view table*

| Variable Name | External Name | External Namespace | Suggested Mapping |
| --- | --- | --- | --- |
| givenName | givenName | urn:ietf:params:scim:schemas:core:2.0:User | user.firstName |
| familyName | familyName | urn:ietf:params:scim:schemas:core:2.0:User | user.lastName |
| displayName | displayName | urn:ietf:params:scim:schemas:core:2.0:User | user.displayName |
| title | title | urn:ietf:params:scim:schemas:core:2.0:User | user.title |

#### Advanced attributes

*Scroll to view table*

| Variable Name | External Name | External Namespace | Suggested Mapping |
| --- | --- | --- | --- |
| employeeNumber | employeeNumber | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.employeeNumber |
| costCenter | costCenter | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.costCenter |
| organization | organization | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.organization |
| division | division | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.division |
| department | department | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.department |
| managerValue | manager.value | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.managerId |
| managerDisplayName | manager.displayName | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User | user.manager |

**Tip:** On the Enterprise plan, you can [manage seats via SCIM](https://help.figma.com/hc/en-us/articles/360048787534) to make sure everyone has the correct billing status in each product.

### Display SCIM member metadata

When you have SCIM set up, you can choose which of these attributes you want to access in Figma. That attribute will be shown in the **People** tab alongside Figma's default data.

1. Open **Admin > Settings**
2. In the **Other** section, click **Member metadata**.
3. Choose from Cost center, organization, division, or department.
4. Figma will show this data in the **People** tab. You'll be able to sort your member list based on this column.

[**Guide to organization admin →**](https://help.figma.com/hc/en-us/articles/360039829474#settingss)

## SCIM API reference

Figma provides a detailed reference for the [Figma SCIM API](https://www.figma.com/developers/api#scim-api-guide) on Figma's developer site. Use the SCIM API as another way to manage SCIM users and groups. The API reference includes the available endpoints, the supported schemas, and some example requests.
