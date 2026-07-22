---
기술지원명: Manage seats via SCIM using Okta
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Manage seats via SCIM using Okta
출처링크: https://help.figma.com/hc/en-us/articles/22773906477591-Manage-seats-via-SCIM-using-Okta
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

In this guide, you'll learn how to manage seats in Figma using Okta. To get started, follow the steps below:

1. [Things to check before you start](#h_01JN4EBTP0MB9G84SCF62S9X11)
2. [Create Okta Groups for provisioning](#h_01JN4EBTP0FH43WPBY537MQXG1)
3. [Disable your Okta provisioning and deprovisioning service](#h_01JN4EBTP03NRJZ0EGFSKF73SF)
4. [Add custom attribute mappings for seatType](#h_01JN4EBTP0YSNCKEN75X8D49QX)
5. [Map custom attributes to Okta assignment groups](#h_01JN4EBTP0NSTZF65ETKVHD57Q)
6. [Re-enable your Okta provisioning service](#h_01JN4EBTP192YW3S802915PXCX)
7. [Test user provisioning](#h_01JN4EBTP1THGVGETA2BCYA2A3)
8. [Re-enable your Okta deprovisioning service](#h_01JN4EBTP1Z7PWT7XBAQN2C3CN)

## Things to check before you start

- Make sure you have a SAML application set up for Figma in Okta. This guide assumes you’ve already completed your SAML configuration (either using the Figma app from the Okta App Catalog or a custom SAML app).
- Make sure you are an Okta Administrator who has scopes to Add/Update Groups and Applications as well as create custom attributes.
- Make sure you are an [Organization admin](https://help.figma.com/hc/en-us/articles/4420557724439) in Figma and are on the Enterprise plan.
- Complete the section on [’Setting up automatic provisioning via SCIM'](https://help.figma.com/hc/en-us/articles/360040532353-SAML-SSO-with-Okta#SCIM) in Okta.

## **Configure Okta Groups for provisioning**

Under **Directory>Groups,** you will need to create 4 different groups that represent all seat type combinations: Full, Dev, Collab, and View

![](https://help.figma.com/hc/article_attachments/30567583063319)

Here’s what each of these access groups represent:

| **Okta Group Name** | **Description** | **Recommended Titles** |
| --- | --- | --- |
| Figma | Full Seat | Users inherit access to Figma Design, Dev Mode, Figma Slides, and FigJam |
| Figma | Dev Seat | Users inherit access to Dev Mode, Figma Slides, and FigJam |
| Figma | Collab Seat | Users inherit access to Figma Slides and FigJam. |
| Figma | View Seat | Users inherit free, view and comment-only permissions to Figma products |

## **Disable your Okta provisioning and deprovisioning service**

Under **Okta Admin > Applications > Applications > Figma > Provisioning,** click **Edit. Disable** the settings **Create User, Update User Attributes > Deactivate Users** and click **Save**.

**![](https://help.figma.com/hc/article_attachments/30567583068439)**

## **Add custom attribute mappings for** seatType

- Navigate to **Applications > Figma > Provisioning > Figma Attribute Mappings.**
- Click **Go To Profile Editor.**

**![](https://help.figma.com/hc/article_attachments/30567583070487)**

- Click **Add Attribute.**
- You will need to create a single attribute for seatType using the following configuration details.

| **Display Name** | **Data Type** | **Variable Name** | **External Name** | **External Namespace** |
| --- | --- | --- | --- | --- |
| Seat type | string | seatType  Note that Okta will append 'figma.' to the front of the variable name AFTER saving. | roles.^[type=='seatType'].value | urn:ietf:params:scim:schemas:core:2.0:User |

- Specify the following **Enum Values**:

| **Display Name** | **Value** |
| --- | --- |
| Full | Full |
| Dev | Dev |
| Collab | Collab |
| View | View |

- Set the **Attribute Type** to **Group**. Click **Save**.

**![](https://help.figma.com/hc/article_attachments/30567573647383)**

## **Map custom attributes to Okta assignment groups**

- Navigate to the **Assignments** tab within your **Figma Application.**

**![](https://help.figma.com/hc/article_attachments/30567583073687)**

- Under the **Groups** filter. You will see assignment groups that will assign Figma for SSO (if configured) as well as for SCIM provisioning. Click the **Assign** drop-down menu and click **Assign to Groups.**
- Add the 4 groups you created in the **Configure Okta Groups for Provisioning** step.
- For each of the 4 groups, click the **pencil icon** and set the custom attributes seatType, to the following values:

| **Group Name** | seatType |
| --- | --- |
| Figma | Full Seat | Full |
| Figma | Dev Seat | Dev |
| Figma | Collab Seat | Collab |
| Figma | View Seat | View |

![](https://help.figma.com/hc/article_attachments/30567583076119)

- Click **Save** for each value.
- Within the **Assignments** view, set the **Priority** by dragging/dropping the Okta app assignment groups **into the same order as mentioned in the table above**. This will ensure in the edge case that a user is assigned to multiple groups, the top-most level group assigns the *most* permissive combination of licenses.
  - Note that the assignment group model used in this guide assumes an Okta user will be assigned to a single Okta Group that assigns a single seat value.

## **Re-enable your Okta provisioning service**

Under **Okta Admin > Applications > Applications > Figma > Provisioning,** click **Edit. Enable** the settings **Create User, Update User Attributes** and click **Save**.

**Note**: You will enable Okta Deprovisioning *after* performing a successful test provision.

![](https://help.figma.com/hc/article_attachments/30567583078167)

## **Test user provisioning**

Before testing your mapping, remember to assign a test user to your groups. We recommend you test provisioning a seat from each group with a single test user.

- Assign a **test user** to one of your Okta assignment groups.

![](https://help.figma.com/hc/article_attachments/30567573659927)

- Navigate to **Applications > Figma > Provisioning.**
  - Ensure **Provisioning to App: Create Users** and **Update Users** are **Enabled**, at minimum.
  - Under **Figma Attribute Mappings** click **Force Sync** – this will push any test SCIM users you have assigned to access groups to Figma.
  - You can validate a successful push SCIM event under **Applications > Figma > View Logs.**

**![](https://help.figma.com/hc/article_attachments/30567573662103)**

- Within Figma’s admin console, navigate to **Members.** You should see your test user reporting **“Pending SCIM”** with the appropriate license combination associated with that Okta App Assignment Group.

![](https://help.figma.com/hc/article_attachments/30567583087127)

- You may repeat the above test for the other following test cases:
  - Remove that test user from one Okta App Assignment Group and add to another: this should update the user’s licenses in Figma.

## **Re-enable your Okta deprovisioning service**

Under **Okta Admin > Applications > Applications > Figma > Provisioning,** click **Edit. Enable** the setting **Deactivate Users** and click **Save**.
