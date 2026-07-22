---
기술지원명: Manage SCIM Groups for Microsoft Entra ID
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage SCIM Groups for Microsoft Entra ID
출처링크: https://help.figma.com/hc/en-us/articles/37835780984215-Manage-SCIM-Groups-for-Microsoft-Entra-ID
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Organization admins only

You need an existing [Microsoft Entra ID](https://azure.microsoft.com/en-us/services/active-directory/) account.

This guide describes how to set up SCIM using a Microsoft Entra ID custom application. The instructions help you provision both Users and Groups via SCIM. If you are interested only in provisioning Users via SCIM, you can configure [Microsoft Entra ID using the Figma application](https://help.figma.com/hc/en-us/articles/360040532413-SAML-SSO-with-Microsoft-Entra-ID).

Organizations using [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333-Guide-to-SAML-SSO) in Microsoft Entra ID can use SCIM Groups to automatically assign users to a [workspace](https://help.figma.com/hc/en-us/articles/4409676189207) or [billing group](https://help.figma.com/hc/en-us/articles/19100885191191) in Figma. SCIM groups can also be synced to [user groups](https://help.figma.com/hc/en-us/articles/38020006913943).

You must configure a custom application in order to use the SCIM Groups functionality. For ease of management, if you use the custom application to manage SCIM Groups, we recommend you also manage SCIM Users in the custom application. If you were previously using the Figma application to manage Users, you should stop and use the custom application instead.

While you can continue to use the Entra ID Figma application to manage your SAML SSO, you can also migrate SAML SSO configuration to the custom application.

We recommend having both Figma and Entra ID open in separate tabs. This allows you to switch between them throughout the setup process.

You must configure SCIM in an active organization. Microsoft recommends testing SAML/SCIM configurations in a sandbox environment. However, there isn’t a way to create a sandbox or test environment in Figma. We recommend testing the custom application with a test user, such as yourself, or a small group of users first.

## Set up automatic provisioning with SCIM

### Generate an API token

You can generate an API token in your organization's admin settings:

1. Open Figma in the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183) and select **Admin** in the sidebar.
2. Select the **Settings** tab and navigate to the in the **Login and provisioning** section.
3. In the **Login and provisioning** section, click **SCIM provisioning**.
4. Click **Generate API token**.
5. Copy the **API token** value.

### Find your Tenant ID

Your identity provider will need a SCIM base URL to configure SCIM. Your Tenant ID will make up part of this URL. You can find your Tenant ID in your organization's admin settings:

1. Open Figma in the file browser and select **Admin** in the sidebar.
2. Select the **Settings** tab and navigate to the in the **Login and provisioning** section.
3. In the **Login and provisioning** section, click **SAML SSO**.
4. Copy the **Tenant ID**.
5. Use your Tenant ID to create the SCIM base URL:
   - `https://www.figma.com/scim/v2/[tenantID]` (Figma organizations)
   - `https://figma-gov.com/scim/v2/[tenantID]` (Figma for Government organizations)

### Add a Custom Application to Entra ID

1. Open Entra ID in the overview page.
2. Select **Enterprise applications**.
3. Go to the **All applications** section.
4. Click **+ New application**.![](https://help.figma.com/hc/article_attachments/37842665138711)
5. Click **+ Create your own application**.
6. Enter a name for your application, such as "Figma Custom App", select the **Integrate any other application you don't find in the gallery (Non-gallery)** option, and click **Create**.

### Configure SCIM in Entra ID

You'll need your Tenant ID and API Token from Figma. Remember to swap the `<TENANT ID>` placeholder in the URL below with the Tenant ID Figma generated.

**Note:** These instructions are modified from Microsoft's Entra ID Tutorial. Check out [Configure Figma for automatic user provisioning](https://docs.microsoft.com/en-us/Azure/active-directory/saas-apps/Figma-provisioning-tutorial) for screenshots and detailed explanations.

1. In your Entra ID Portal go to **Enterprise Applications > All Applications**
2. Select the Figma Custom app.
3. Go to the **Manage** section and select **Provisioning**.
4. Set the **Provisioning Mode** to **Automatic**.  
   ![](https://help.figma.com/hc/article_attachments/37844451440023)
5. Enter the following details in the **Admin Credentials** section:
   - Enter the URL in the **Tenant URL** field: `https://www.figma.com/scim/v2/<TenantID>`
   - Enter the API Token in the **Secret Token** field.
   - Click **Test Connection** to make sure that Entra ID can connect to Figma.
6. Enter the desired email address in the **Notification Email** field.
7. Check the box next to **Send an email notification when a failure occurs** and click **Save** to apply.
8. In the **Mappings** section, select **Provision Microsoft Entra ID Users** to Figma, set **Enabled** to yes.
9. In the **Attribute Mappings** section, review the Entra ID Attribute and the corresponding Figma Attribute.
10. Click the Save button to apply any changes.
11. In the **Mappings** section, select **Provision Microsoft Entra ID Groups**, if you plan to provision groups to Figma, set **Enabled** to yes.
12. Click **Save** to apply any changes.
13. Under **Settings**, toggle the **Provisioning Status** to on.
14. Define which users and/or groups you would like to provision to Figma. Choose from:
    - Sync all users and groups
    - Sync only assigned users and groups
15. Click **Save** to apply your provisioning settings.

**Caution:** If a user is deactivated in Entra ID, this will remove their Figma account from your organization and they will lose all permissions. If you reactivate the user in Entra ID and re-add them to your organization, someone will need to manually add them to their previous teams, projects and files.

### Assign a test user/group

Assign a test user and/or group to the Figma Custom App in Entra ID. This allows you to complete the SCIM setup process and test the application.

1. Select **Assign users and groups** from the options.
2. Click **+ Add user/group** to open the assignments page.
3. Click **Users and groups**, then click **None selected**.
4. Search for the test user/group.
5. Click to add and return to the assignments page.
6. Click **Assign** to return to application page.

### Test the application

With both Figma and Entra ID configured you can test the application. You’ll need to test this process with the user you added earlier.

If you skipped this step, you’ll need to assign a user to Figma first. We recommend adding your own account.

## Provision a Workspace or Billing Group with a SCIM group

To provision a workspace or billing group:

1. [Set up a workspace or billing group.](#h_01KFHC0MF8F5Y4YQ0C2GRKNSMM)
2. [Create a group in Microsoft Entra ID.](#h_01KFHC1Y447E62QKB81Y4F8Q1M)
3. [Assign the group to the Figma Custom application.](#h_01KFKJVKSM57XDY38DRM5AQ1B7)

You can also [unassign a group](#h_01KFKK6MD2V5MVNJKGR7XGA5BT) and [view SCIM groups in Figma](#h_01KFKK7Y94226A900A9JJQ5W35).

### Set up a workspace or billing group

You must create at least one [workspace](https://help.figma.com/hc/en-us/articles/4409676189207) or [billing group](https://help.figma.com/hc/en-us/articles/19100885191191) before setting up the corresponding group in Microsoft Entra ID.

- [Create a workspace](https://help.figma.com/hc/en-us/articles/4409612431383-Create-a-workspace)
- [Create a billing group](https://help.figma.com/hc/en-us/articles/19100486415255-Manage-billing-groups-in-an-organization)

### Create a group in Microsoft Entra ID

**Note:** The name of the group in Microsoft Entra ID must match the name of the corresponding workspace or billing group.

![](https://help.figma.com/hc/article_attachments/37867613126807)

1. Under **Manage > Groups**, click **New group** and enter a name of the group.
2. Click **All groups**, search for the new group, and then click it.
3. Click **View group members**.
4. Click **Add members** to add member.

### Assign the group to the Figma Custom application

1. In your Entra ID Portal go to **Enterprise Applications > All Applications**.
2. Select the Figma Custom app.
3. Under **Manage > Users and groups**, click **Add user/group**.
4. Click **None Selected** under **Users and groups**, then choose a group to add.
5. Click **None Selected** under **Select a role**, then choose an AppRole.

When you add a group to the Figma Custom app, Microsoft Entra ID will link the group to any workspace or billing group with a matching name. All users in the group will be assigned to the associated workspace or billing group once the group status is active.

Note:

- Members of your organization won’t notice when they are assigned to a billing group. If they are assigned to a workspace, the workspace name will automatically appear in their sidebar in the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183).
- If a user is included in multiple groups, the first group added to the Figma Custom application in Microsoft Entra ID takes precedence.
- Depending on the group size, the workspace and billing group assignments may take up to 30 minutes.
- Group sizes are limited to 5,000 users.
- While a group name has to match a Workspace name or a Billing group name when first provisioning, its name can be changed afterwards after the first provisioning, which links the SCIM group with the corresponding Workspace or Billing group.

### Unassign a group

Unlinking a group in Microsoft Entra ID removes the SCIM group in Figma. All users managed by the group will be unassigned from their respective workspace or billing group.

1. In your Entra ID Portal go to **Enterprise Applications > All Applications**.
2. Select the Figma Custom app.
3. Under **Manage > Users and groups**, choose a group.
4. Click Remove.

![](https://help.figma.com/hc/article_attachments/37867613130391)

### View SCIM groups in Figma

You can view the members of any SCIM group you’ve created in Figma.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Select the  **People** tab.
3. Select  **People table filters** to select and view members by SCIM group.

![Add a filter for scim group from the people tab of admin](https://help.figma.com/hc/article_attachments/41068344712343)

## Seat Management and SCIM group management

If you manage Figma seats via the deprecated figma permissions using `SingleAppRoleAssignment` to manage attribute mapping, you may run into an `SingleAppRoleAssignment` conflict, since the Seats and SCIM groups are both managed by Entra groups.

If you encountered a **MultipleGrantsNotSupported** error on `SingleAppRoleAssignment`, please follow these steps to correct the error message. These instructions map custom attributes to AppRoles using a different expression language statement.

**Note:** It is safe to ignore these instructions if you do not see a **MultipleGrantsNotSupported** error message.

### Configure the member role for Figma

1. Open the Figma Enterprise App.
2. Navigate to the **Provisioning** section.  
   ![](https://help.figma.com/hc/article_attachments/37867580681111)
3. Click **Edit attribute mappings**.
4. Expand **Mappings** and select **Provision Microsoft Entra ID Users**.  
   ![](https://help.figma.com/hc/article_attachments/37867613132951)
5. Click **Edit** for the `urn:ietf:params:scim:schemas:extension:figma:enterprise:2.0:User:figmaPermission` attribute.
6. Set its expression to:

   ```
   IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "FigmaFull", , )>"0", "", IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "FigmaViewerRestricted", , )>"0", "viewerRestricted", "full"))
   ```
7. Click **OK** to save
8. Click **Edit** for the `urn:ietf:params:scim:schemas:extension:figma:enterprise:2.0:User:figjamPermission` attribute.
9. Set its expression to:

   ```
   IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "FigJamFull", , )>"0", "full", IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "FigJamViewerRestricted", , )>"0", "viewerRestricted", ""))
   ```
10. Click **Edit** for the `urn:ietf:params:scim:schemas:extension:figma:enterprise:2.0:User:devModePermission` attribute.
11. Set its expression to:

    ```
    IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "DevModeFull", , )>"0", "full", IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "DevModeViewerRestricted", , )>"0", "viewerRestricted", ""))
    ```
12. Click **OK** to save.
13. Back on the **Attribute Mapping** page, click **Save** to confirm your changes.  
    ![](https://help.figma.com/hc/article_attachments/37867613134359)
