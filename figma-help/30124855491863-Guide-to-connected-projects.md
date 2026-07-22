---
기술지원명: Guide to connected projects
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Guide to connected projects
출처링크: https://help.figma.com/hc/en-us/articles/30124855491863-Guide-to-connected-projects
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Requires both parties to have [a paid plan](https://help.figma.com/hc/en-us/articles/360040328273)

Connected projects aren't available on the Education plan

Only [admins](https://help.figma.com/hc/en-us/articles/4420557724439) can set up a connected project

Admins from both parties need to approve the connection

Connected projects let two separate teams or organizations—like an agency and a client—work together in a shared project using [billable seats](https://help.figma.com/hc/en-us/articles/360039960434-Manage-seats-in-Figma) from their own plans.

This makes it easy to design together, share resources, and hand off files smoothly—without paying for extra seats.

## How connected projects work

![File browser shows "Noodle Co Rebrand" project linked between Noodle Co. and KPMD, indicating a connected project.](https://help.figma.com/hc/article_attachments/31288466401431)

A connected project gets created in one team or organization and then shared with another.

- The party which creates the project and sends a request to connect is the **host**.
- The party which receives the request to join the connected project is the **external team**.

**Note:** There can only be one host and one external team per project.

### Who manages the connected project

![Admin panel showing connected projects with host and external team details, featuring a button to create a new connected project.](https://help.figma.com/hc/article_attachments/31288466405655)

Admins from both parties can view the connected project in their own **Admin** settings. Since the project originates in the host’s team or organization, the host has more control over the settings and permissions of the project.

|  | Host admins | External admins |
| --- | --- | --- |
| View the connected project in **Admin** | ✓ | ✓ |
| View members of the connected project | Can view all members of the project | Can only view people from their own team |
| Manage security and privacy features for the project | ✓ | X |
| [Allow people from the external team to use the host’s libraries](#h_01JMJDKJFE31AZHCQ2J0P3F15G) | ✓ | X |
| Manage [AI feature availability](https://help.figma.com/hc/en-us/articles/24039793359767-About-Figma-AI) | ✓ | X |
| [Disconnect a project](#h_01JMJDKJFERAFFPGVYFFDFM5B0) | ✓ | ✓ |
| Manage the project after it is disconnected, including [sharing a copy or transferring it](#h_01JMJDKJFERAFFPGVYFFDFM5B0) | ✓ | X |

**Note:** The host’s plan determines which features are available in the connected project.

If the host is on the Enterprise plan, and the external team is on the Professional plan, all features of the Enterprise plan are available to everyone in the project. This includes features like the number of [variable modes](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables), approved libraries, and security settings like [requiring password protection on publicly shared files](https://help.figma.com/hc/en-us/articles/5726756336791-Manage-public-link-sharing-and-open-sessions).

The reverse is also true. If the host is on the Professional plan and the external team is on the Enterprise plan, the connected project is limited to the functionality of the Professional plan for both parties.

**Note**: Both parties can create, move, or import files into a connected project. However, only people from the host team or organization can remove files from it.

### How seats work in connected projects

In Figma, a person's [seat](https://help.figma.com/hc/en-us/articles/360039960434) determines which Figma products they have access to. For example, a user with a Collab seat has access to FigJam and Figma Slides.

Seats are separate from permissions—to determine which individual files a user can edit, you can give them **can edit** or **can view** permission on each file. To edit a file in a connected project, a user needs both the relevant seat and **can edit** file permissions. [Learn more about sharing and permissions](https://help.figma.com/hc/en-us/articles/1500007609322).

People can work in a connected project based on the seat they have in their own team or organization. The host won’t be billed for users in the external team, and vice versa. Any seat upgrade requests continue to be routed to the user’s own admins.

If a user from the external team is invited to edit files outside of the connected project in the host team or organization, they will need a seat on the host’s plan.

**Note**: If a user is invited to the project and doesn’t currently have an account with either the host or the external team, they are added to the host’s plan with a [View seat](https://help.figma.com/hc/en-us/articles/360039960434). If they require a paid seat, their upgrade request is routed to a host admin.

### How many connected projects can you have?

Your plan determines the number of connected projects you can have in your team or organization at one time.

| Plan | Number of connected projects |
| --- | --- |
| Professional | 3 |
| Organization | 6 |
| Enterprise | 15 |

The number of connected projects is inclusive of:

- All connected projects in your team or organization, whether you are the **host** or the **external team**.
- Any pending invites to connect where you are the **host**.

When you disconnect a project, it no longer counts towards your connected project count.

### How libraries are managed in connected projects

![Connected projects panel showing collaboration between KPMD and Noodle Co, with project details and library options.](https://help.figma.com/hc/article_attachments/30125142327191)

Host admins can curate which of the host’s [libraries](https://help.figma.com/hc/en-us/articles/360041051154) are available to use in the connected project. Allowing access to a library grants members of the connected project view-only access to the library’s source file.

### Guests and external users in connected projects

Connected projects also support additional external collaborators, or guests. Both the host team and the external team can invite guests into a connected project. How those users join, and which seat they use, depends on a few factors.

- If the invited user belongs to the connected organization:
  - They join the connected project using the seat type they already have in their own organization.
- If the invited user is from another external organization:
  - They join the host organization as a guest.
  - By default, they are given a View seat in the host organization.
  - If they need a paid seat, any upgrade request is sent to the host organization admin.

On the Enterprise plan, [guest approval settings](https://help.figma.com/hc/en-us/articles/4410793238167-Restrict-or-prevent-guest-access) still apply to connected projects.

- If the **External users can join the organization without restrictions** setting is enabled:
  - External users invited to the connected project are automatically added as guests.
  - When a guest joins your organization, they join with a free View seat. You can change a guests [seat type](https://help.figma.com/hc/en-us/articles/360039960434) at any time, and a guest can [make a seat request](https://help.figma.com/hc/en-us/articles/360040453433) to change their seat type.
- If the **External users can only join the organization with admin approval** setting is enabled:
  - Workspace or organization admins must approve the guest access request before the external user can join the host organization as a guest.
  - The user will only be added to the connected project after approval is granted.

Note: If the connected project lives inside a workspace, then workspace admins—not just organization admins—may be responsible for approving or managing guest access requests.

## Connect a project to an external team

A project is connected when the external team accepts an invite from the host. Here’s how the process works:

### 1. The external team shares their team or organization URL

For a host to create a request to connect, they need the Figma URL of the external team and a contact person’s email address.

**Note:** To connect a project, the host and external team must use different business domains—for example, @agency.com and @client.com.

For Professional teams, the domain check applies to all admins on the team, not just the team owner. If any admin's business email domain matches a domain claimed by the other organization, the connection will be blocked. Personal email domains (e.g., gmail.com, yahoo.com) are not considered.

The external team can get their Figma URL by following these steps:

1. Log into Figma in a web browser.
2. If you're logged into more than one team or organization, make sure the correct one is showing in the left sidebar of the [file browser.](https://help.figma.com/hc/en-us/articles/14381406380183)
3. Copy the entire URL in your browser address bar.
4. Share this URL with the host admin.

### 2. A host admin creates the request

A host admin creates a project, or chooses an existing project to connect. This can be any project in their team or organization. They create a request to connect from the project page in the file browser, or from Admin. To send the request, they’ll need the URL of the external team and a contact person’s email address.

**Project page**

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), navigate to the project you'd like to connect.
2. Click  **Settings** in the top right of the screen.
3. Click **Connect an external team**.

**Admin**

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select  **Content**.
3. Click the **Connected projects** tab.
4. Click **Create a connected project** and search for the project.

### 3. An external team admin approves the request

Admins of the external team get notified about the request to connect, and can approve or decline the connection.

Once accepted, the contact person on the external team is added to the project. This person can invite more people from the external team to the project.

People on the external team can start working in the connected project by switching to the host’s team or organization in the file browser sidebar.

![Dropdown menu for switching teams in Figma with "Noodle Co." selected and "KPMD" as another option.](https://help.figma.com/hc/article_attachments/30125142331927)

## Disconnect a connected project

When a project comes to an end, an admin from either party can disconnect the project. When a project is disconnected, it remains in the ownership of the host. The external team will lose access to all the files in the project.

Host admins will be asked if they would like to share the project with the external team. They can:

1. Do nothing. The external team will lose access to the project once it is disconnected.
2. Share a copy of the project. The host keeps the original project and sends a copy to the external team.

**Tip**: You can always [share a copy of the project](https://help.figma.com/hc/en-us/articles/10250387712407-Transfer-a-project-or-team-to-a-different-account#h_01J5BDVCA0YGB4N1KMS59QJQ93)—or [transfer it completely](https://help.figma.com/hc/en-us/articles/10250387712407-Transfer-a-project-or-team-to-a-different-account#h_01J5BDVCA03KDMPYKR88NK94ZY)—at a later date.
