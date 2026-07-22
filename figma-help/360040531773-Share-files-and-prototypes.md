---
기술지원명: Share files and prototypes
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Share files and prototypes
출처링크: https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273)

Prototypes are only available in Figma Design files.

You can share Figma files and prototypes to collaborate with teammates, clients, or stakeholders. In this article, you’ll learn how to share a file or a prototype andadjust share settings and permissions.

## Share a file

You can share any Figma file via link or direct invitation.

### Share via link

1. Open the file and click **Share** in the top-right corner.
2. In the share modal, adjust the [share settings and permissions](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions).
3. Click **Copy link** and send the link to collaborators.

**Note**: If you have a frame or node selected in a file, the copied link will open to that frame. If the frame is nested inside other frames, Figma links to the parent frame.

### Share via invitation

You can send direct invitation to individuals. On the Organization or Enterprise plan, you can also send invitations directly to [user groups](https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups).

1. Open the file and click **Share**.
2. Enter email addresses or user group names in the invite field (separate multiple entries with commas).
3. Adjust each person’s [permissions](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions).
4. Click **Send invite**.

Invitees get both an email and a notification in the file browser.

## Share a prototype only

Use a prototype-only link when you want to present designs for clients, stakeholders, or usability testing without giving access to the full design file.

Note: Prototypes are only available in Figma Design files.

Additionally, sharing a prototype-only link is available on paid plans. On the Starter plan, if you share a file from presentation view, viewers can still open the source file by selecting the dropdown next to the file name and choosing **Open in editor** from the prototype view.

1. Open the design file and click  **Present** in the right sidebar.
2. In presentation view, click **Share prototype**.
3. Adjust the prototype’s [settings and permissions](https://help.figma.com/hc/en-us/articles/1500007609322-Guide-to-sharing-and-permissions).
4. Share the prototype.
   1. Enter email addresses or user group names in the invite field to send invitations.
   2. Click **Copy link** to send the link to collaborators.

## Share settings and permissions

From the **Share** modal, you can access the following settings:

![An annotated image of the share settings of a file, where you can invite people and set their file permissions.](https://help.figma.com/hc/article_attachments/35463302707223)

1. **Invite field**: Enter email addresses or [user group](https://help.figma.com/hc/en-us/articles/38020006913943-Create-and-manage-user-groups) names you want to invite to the file.
2. **File sharing permissions**. Click to see additional settings. Set file sharing permissions to:
   - **Anyone**: Anyone, even those outside your organization, will be able to access this file
   - **[Organization name]**: Anyone at your organization can access the file (Organization/Enterprise plan only).
   - **[Workspace name]**: Anyone in the selected workspace can access the file (Enterprise plan only).
   - **Only invited people:** Only those directly invited to the file can access it
3. If the file is part of a project, see what access project members have on the file. Learn more about [project permissions](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions).
4. **List of existing permissions:** See a list of people who have explicitly been invited to the file and their permissions. This will not include everyone who has access to the file via the organization, team, or project.
5. **Additional sharing options:** Use the sharing options to:
   - Copy a link to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode)
   - Copy a link to the prototype (Figma Design only)
   - [Publish the file to the Community](https://help.figma.com/hc/en-us/articles/360040035974-Publish-files-to-the-Community)
   - Get the [embed code](https://help.figma.com/hc/en-us/articles/360039827134-Embed-files-and-prototypes) (Figma Design only)
   - [Publish the file as a template](https://help.figma.com/hc/en-us/articles/13590681087127-Create-custom-templates-in-FigJam) (FigJam only)
   - Start an [open session](https://help.figma.com/hc/en-us/articles/4410786053911-Invite-visitors-to-an-open-session) (FigJam only)
6. **Copy link:** Click to copy a direct link to the file or prototype. If you have a frame selected, the copied URL will link directly to that frame.

### Share settings

When you click into file sharing permissions, you’ll see additional share settings.

![An annotated image of the share settings, where you can set organization access to a file and additional security settings.](https://help.figma.com/hc/article_attachments/35463302710551)

1. **Who has access**: Choose who can access the file: anyone, only people invited to the file, or people within your organization or workspace (if applicable).
2. **What they can do**: Set the level of access for your chosen audience: view or edit.
3. **Additional security:** If you are on a paid plan, you'll have access to additional sharing features:
   - [Password protect files](https://help.figma.com/hc/en-us/articles/5726720100247-Add-password-protection-to-files)
   - Control whether the file appears in organization search results.
     - **On**: Organization members can find the file in the file browser.
     - **Off**: Organization members can only find the file if they’re directly invited to the file or its parent project.

       You can’t turn this off if the file is shared with **Anyone in [Workspace Name]**. In that case, workspace members can find the file in search, and organization members outside the workspace can only access it if they’re directly invited or have previously opened the file via a link.
   - [Set an expiration on file links](https://help.figma.com/hc/en-us/articles/16142157359255-Set-an-expiration-on-public-links-in-design-files) (Enterprise plan only)
4. **Advanced**: If you are on a paid plan, you'll have access to advanced sharing features:
   - [Allow viewers to copy, share, and export](https://help.figma.com/hc/en-us/articles/360040045574)

**Note**: If a file is stored in a **Drafts** folder on a Starter team, and the file's **Who has access** setting is set to **Anyone**, then those with the file link will only be to view the file. To grant edit access, move the file into a project.

## Troubleshooting

**The person I invited didn’t receive an email.**

If an invitee doesn’t see the email, you can resend access by copying the file or prototype link and sharing it directly with them. They will still be able to open the file if they have permission.

**The “Anyone” option doesn’t appear in my share settings.**

This usually happens if your organization admin has [disabled public links](https://help.figma.com/hc/en-us/articles/5726756336791-Manage-public-link-sharing-and-open-sessions). Reach out to your admin for confirmation.
