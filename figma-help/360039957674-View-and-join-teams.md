---
기술지원명: View and join teams
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: View and join teams
출처링크: https://help.figma.com/hc/en-us/articles/360039957674-View-and-join-teams
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on all plans

Teams are shared spaces for organizing and collaborating on projects and files. You can use teams to work with others or simply manage your own content.

You can create or join multiple teams from a single Figma account. The way you create and join teams depends on your plan type:

- Starter and Professional: The Starter and Professional plans each include a single team. Each team is managed separately.
- Organization and Enterprise: The Organization and Enterprise plans each include unlimited teams. You can create or join multiple teams within an organization, making it easier to collaborate cross-functionally and share resources.

## Join a Starter or Professional team

To join a Starter or Professional team, you must be [directly invited](https://help.figma.com/hc/en-us/articles/360039481034).

You’ll need a Figma account to accept an invitation. You can accept in two ways:

- **From the invitation email:** Click the **Accept** button to open Figma and accept the invitation.
- **From the file browser:** Click  your notifications the to view invitations. Click **Accept** to join the team.

## Join a team in an organization

On the Organization and Enterprise plans, you can join a team either by:

- Being [directly invited](https://help.figma.com/hc/en-us/articles/360039481034) via invitation
- Browsing or searching for available teams in the file browser

### Find teams in the file browser

You can search for teams by name using the  search bar.

To browse all available teams:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a file, click the  Figma menu > **Back to files.**
2. Navigate to a list of all teams:
   1. On the Organization plan or Enterprise plan without workspaces enabled, select  **All teams** from the left sidebar.
   2. On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Select a workspace to view its teams.

You'll only see teams that are available to you based on the team’s access settings.

### How team visibility works

When teams are created, the team owner sets the [organization access to teams](https://help.figma.com/hc/en-us/articles/360039970673).

![When you create a team, you can set the organization access level to the team.](https://help.figma.com/hc/article_attachments/35463257768087)

- If a team is open to the organization (the **Who can access** setting is set to the organization name), you don’t need to explicitly join the team. You’ll be able to view and access the team based on the [permissions](https://help.figma.com/hc/en-us/articles/360039970673) set by the team owner.
- If the team is open to anyone in a selected workspace (the **Who can access** setting is set to a workspace name), members of that workspace don’t need to explicitly join the team. They’ll be able to view and access the team based on the [permissions](https://help.figma.com/hc/en-us/articles/360039970673) set by the team owner. [Enterprise only]
- Teams that are set to **Only those invited** (from the **Who can access** setting) are either **Visible** or **Hidden**
  - **Hidden** teams cannot be found in the file browser.
  - **Visible** teams can be found by organization members in the file browser.

**Note**: Organization admins can see a list of all teams, including hidden teams, in **Admin**. They can also view activity related to hidden teams, including members and file names, in the [organization's activity logs](https://help.figma.com/hc/en-us/articles/360040449533).

Admins can join, request to join, or leave teams from the **Teams** tab, depending on team access settings.

Guests can only view teams to which they are invited.

### Join a visible team

Visible teams are teams that are set to **Only those invited**, but have a **Visible** setting.

Any member of the organization can find the team by browsing or searching, but cannot access its content unless invited.

- These teams display a  **lock icon** in the file browser.
- Members of the team can invite others, but only at or below their own access level.
  - For example, someone with `can view` can only invite another user with `can view`.
  - Someone with `can edit` can invite users with either `can view` or `can edit`.

Members can ask to join visible teams with `can view` or `can edit` access. A team admin needs to approve any requests before they can join the team.

To request to join a visible team:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a file, click the  Figma menu > **Back to files.**
2. Search for a team from the search bar, or navigate to a list of all teams:
   1. On the Organization plan or Enterprise plan without workspaces enabled, select  **All teams** from the left sidebar.
   2. On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Select a workspace to view teams in that workspace.
3. Click **Ask to join** on the team card.
4. Use the dropdown menu to choose `can view` or `can edit` access.
5. (Optional) Add any notes or information to give the team admin some context.
6. Click **Request access**.

Figma will notify all admins of the team. You’ll be granted access only after an admin approves your request.

![Click Ask to join to request to join a visible invite-only team.](https://help.figma.com/hc/article_attachments/35463257769239)

To cancel a request or change your access level, click **Cancel request** on the team card.

### Join a hidden team

Hidden teams are set to **Only those invited**, but have a **Hidden** visibility setting. They do not appear in the file browser or search results.

- A current team member must [invite you](https://help.figma.com/hc/en-us/articles/360039481034).
- Only admins and users with `can edit` team access can invite others (members or guests).
