---
기술지원명: Manage seats via SCIM using Microsoft Entra ID
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Manage seats via SCIM using Microsoft Entra ID
출처링크: https://help.figma.com/hc/en-us/articles/22766770509591-Manage-seats-via-SCIM-using-Microsoft-Entra-ID
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/22766770509591-Manage-seats-via-SCIM-using-Microsoft-Entra-ID#h_01HV9HZ3S3WQS13P2SKTBJF31B:~:text=Available%20on%20the-,Enterprise%20plan,-Organization%20admins%20only)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

In this guide, you'll learn how to manage seats in Figma using Microsoft Entra ID—formerly known as Azure Active Directory or Azure AD. To get started, follow the steps below:

1. [Configure app roles for the Figma Entra Gallery app](#h_01JN4CN3YYDZBF8AGT9G0B25VE)
2. [Add the roles attribute to Figma schema](#h_01JN4CN3YYF6C5GWVHMS38R14J)
3. [Configure the roles attribute](#h_01JN4CN3YZ4VQNDGPP2S9Y3BPC)
4. [Set up security groups](#h_01JN4CN3YZGYZNXAMB5WYSYVWD)
5. [Map security groups to app roles](#h_01JN4CN3YZ00W397EYDCGFPJVM)
6. [Test user provisioning](#h_01JN4CN3YZRN7JCETJ8VHFFV0R)

**Before you start**

Make sure you have a SAML application for Figma set up in Microsoft Entra ID.

You can use the Figma application from the Microsoft Entra Gallery, or a custom SAML app that you’ve configured for Figma access.

## **Configure app roles for Figma Entra Gallery app**

- Go to the **Figma Enterprise App Template** in Entra ID under [**App registrations**](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade). You may have to select the ‘All applications’ tab to find Figma.

![Microsoft Entra ID portal overview for Figma app registration, showing application and directory IDs with navigation panel on the left.](https://help.figma.com/hc/article_attachments/30567572946199)

- Navigate to the **App Roles** section.

![Microsoft Azure App roles management interface showing configured roles for Figma with options to create new roles.](https://help.figma.com/hc/article_attachments/30567582347415)

- Create a new app role called **Figma Full,** set the **allowed member type** to users/groups, set the **Value** to **Full** and add a description.

![Creating an app role titled "Figma Full" in Microsoft Entra ID with full access settings for users and groups.](https://help.figma.com/hc/article_attachments/30567572948887)

- Click **Apply** to save the app role.
- Repeat this process for the other three **App Roles** for a total of four new app roles.

| **Display Name** | **Allowed Member Type** | **Value** | **Description** |
| --- | --- | --- | --- |
| Figma Full | User/Groups | Full | Full access to Figma’s product suite |
| Figma Dev | User/Groups | Dev | Developer focused access of Figma’s products |
| Figma Collab | User/Groups | Collab | Collaboration access of Figma’s products |
| Figma View | User/Groups | View | View and comment access only |

![Microsoft Azure interface displaying app roles configuration for Figma, listing roles like Figma Full, Dev, Collab, and View.](https://help.figma.com/hc/article_attachments/30567572951063)

## **Add custom attributes**

- **You must enable the creation of custom attributes** for the Figma Application on Microsoft Entra ID. To do so, use the following link to open the Microsoft Entra ID portal with the schema fully enabled: <https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AppAppsPreview/menuId~/null>
- Open the **Figma Enterprise App**.

![Microsoft Entra portal showing Figma Enterprise App overview with options for user assignment, single sign-on, and provisioning.](https://help.figma.com/hc/article_attachments/30567572953111)

- Navigate to the **Provisioning** section.

![Overview page in Microsoft Azure showing Figma provisioning status as 100% complete with 36 users.](https://help.figma.com/hc/article_attachments/30567572954647)

- Click **Edit attribute mappings**.
- Expand the **Mappings** section and select **Provision Azure Active Directory Users.**

![Provisioning configuration screen in Microsoft Entra for managing Figma user account synchronization settings.](https://help.figma.com/hc/article_attachments/30567582363031)

- Scroll to the bottom of the page and select **Show advanced options**.

![Attribute mapping interface showing Figma and Microsoft Entra ID attributes with options to create, update, delete, and add new mapping.](https://help.figma.com/hc/article_attachments/30567582364183)

- Select **Edit attribute list for Figma**. If these options are not available to you, open the Microsoft Entra ID portal using the following URL: [Microsoft Entra ID portal with schema fully enabled](https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true).
- Add a custom attribute called **roles,** set the data type to **string** and enable **multi-value.**

![Figma user attributes panel showing the addition of a "roles" attribute as a string with multi-value enabled.](https://help.figma.com/hc/article_attachments/30567572961687)

- Save the **new configuration**.

## **Configure the roles attribute**

- Open the **Figma Enterprise App**.

![Figma Enterprise app overview page in Microsoft Azure, showing options like assign users, set up single sign-on, and provision accounts.](https://help.figma.com/hc/article_attachments/30567572953111)

- Navigate to the **Provisioning** section.

![Microsoft Entra ID portal showing Figma app overview with current cycle status and provisioning options.](https://help.figma.com/hc/article_attachments/30567582368407)

- Click **Edit attribute mappings.**
- Expand **Mappings** and select **Provision Azure Active Directory Users.**

![Provisioning settings panel in Microsoft Entra, showing user account synchronization options for Figma.](https://help.figma.com/hc/article_attachments/30567582363031)

- Click **Add New Mapping**.

![Attribute mapping settings between Microsoft Entra ID and Figma, showing a list of attributes and options for editing mappings.](https://help.figma.com/hc/article_attachments/30567582364183)

- Set the **Mapping type** to **Expression** and set the **Expression** to *AppRoleAssignmentsComplex([appRoleAssignments])*.

![Microsoft Entra ID portal's Edit Attribute screen with mapping type set to Expression and target attribute selection required.](https://help.figma.com/hc/article_attachments/30567572966807)

- Set the **Target attribute** to **roles** and set **Apply this mapping** to **Always**.

![Expression mapping configuration screen with options for setting the target attribute to roles and applying the mapping always.](https://help.figma.com/hc/article_attachments/30567582373911)

- Click **OK** to save.

## **Set up security groups**

- Navigate to **Groups**.

![Microsoft Azure portal showing the "All groups" page, listing a security group named "All Users" with assigned membership.](https://help.figma.com/hc/article_attachments/30567582375703)

- Create a **New group** called **Figma Full**.

![Creating a new security group named "Figma Full" with full access to Figma’s product suite in Microsoft Azure.](https://help.figma.com/hc/article_attachments/30567572977303)

- Click **Create** to save the security group.
- Repeat this process for the other three security groups for a total of four new groups.

These are suggested groups based on Figma’s best practices:

| **Group Name** | **Group Type** | **Group Description** |
| --- | --- | --- |
| Figma Full | Security | Full access to Figma’s product suite |
| Figma Dev | Security | Developer focused access of Figma’s products |
| Figma Collab | Security | Collaboration access of Figma’s products |
| Figma View | Security | View and comment access only |

![Microsoft Entra interface showing a list of security groups including Figma Full, Figma Dev, Figma Collab, and Figma View.](https://help.figma.com/hc/article_attachments/30567572978583)

- Assign users to the four security groups.

![Microsoft Azure window displaying the process of adding members to the "Figma Full" security group.](https://help.figma.com/hc/article_attachments/30567582385943)

## **Map Security Groups to App Roles**

- Open the the **Figma Enterprise App.**

![Microsoft Entra ID interface displaying the Figma application overview with options to assign users and configure roles.](https://help.figma.com/hc/article_attachments/30567572953111)

- Navigate to **Users and groups.**

![Microsoft Azure UI for adding users and groups to app roles in Figma Enterprise application setup.](https://help.figma.com/hc/article_attachments/30567572982039)

- Click **Add user/group.**
- Set the **Users and groups** to the group **Figma Full.**

![Selecting the "Figma Full" group in Microsoft Azure to set user roles for Figma Enterprise App.](https://help.figma.com/hc/article_attachments/30567572983703)

- Set the **Select a role** to the app role **Figma Full.**

![Add Assignment panel in Microsoft Azure for Figma, showing role selection options like Figma Full and Figma Collab.](https://help.figma.com/hc/article_attachments/30567582396311)

- Click **Assign.**
- Repeat this process for the other three **Security Groups** and **App Roles.**

| **Security Group** | **App Roles** |
| --- | --- |
| Figma Full | Figma Full |
| Figma Dev | Figma Dev |
| Figma Collab | Figma Collab |
| Figma View | Figma View |

![Microsoft Azure portal displaying Figma user and group assignments with groups like Figma Full and Figma Dev listed.](https://help.figma.com/hc/article_attachments/30567572986135)

## **Test user provisioning**

**Note**: Before testing your mapping, remember to assign a test user to one of the groups.

- Open the **Figma Enterprise App**.

![Figma Enterprise App overview in Microsoft Entra ID with options for user and group management, single sign-on, and provisioning.](https://help.figma.com/hc/article_attachments/30567572953111)

- Navigate to the **Provisioning** section.

![Microsoft Entra ID portal showing Figma Enterprise app overview with provisioning status complete and user count.](https://help.figma.com/hc/article_attachments/30567582368407)

- Click **Provision on demand**.
- Select a user to test provisioning with.

![Provision on-demand page in Microsoft Azure showing the search for a user to test provisioning in Figma.](https://help.figma.com/hc/article_attachments/30567572990615)

- Click **Provision**.

![Provisioning success screen showing modified user attributes for Figma in Microsoft Entra ID.](https://help.figma.com/hc/article_attachments/30567572992407)
