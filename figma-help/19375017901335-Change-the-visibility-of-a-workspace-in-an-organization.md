---
기술지원명: Change the visibility of a workspace in an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Change the visibility of a workspace in an organization
출처링크: https://help.figma.com/hc/en-us/articles/19375017901335-Change-the-visibility-of-a-workspace-in-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

By default, workspaces are visible to every member of an organization. This means people can click **All workspaces** in the sidebar of the file browser and browse the contents of every workspace in the organization.

However, organization admins can limit the visibility of a workspace so it’s only visible to people assigned to the workspace and other organization admins.

Making a workspace hidden doesn’t affect access to teams, projects, or files within the workspace:

- If a hidden workspace contains teams that are open to anyone at the organization, people can still search for and browse the content of the teams.
- When a workspace becomes hidden, the default audience for any new [team](https://help.figma.com/hc/en-us/articles/360040450293-Create-a-team-in-an-organization) created in the workspace is **Only those invited,** with a **Visible** setting. However, team admins can [change the team’s access settings](https://help.figma.com/hc/en-us/articles/10551384098711)  if they choose.
- Individual teams, projects, and files can still be shared with people outside the hidden workspace. This includes sharing via [public links](https://help.figma.com/hc/en-us/articles/360040531773). If someone is invited to a resource in the hidden workspace, they won’t know which workspace the resource belongs to.

**Note:** If your organization [lets people assign themselves to workspaces](https://help.figma.com/hc/en-us/articles/7249713835799), people won't be able to add themselves to a hidden workspace. An organization or workspace admin will need to [manually assign them](https://help.figma.com/hc/en-us/articles/4419365500695).

### Change the visibility of a workspace

Organization admins can see a list of all workspaces, including those set to hidden. Workspaces set to hidden have a  lock icon in **Admin** and the **All workspaces** view.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Click **Content**, then select the **Workspaces** tab.
3. Search or navigate to a workspace.
4. Click  **More** at the end of the row and select **Edit details.**
5. Toggle the visibility of the workspace and click **Save changes**.
