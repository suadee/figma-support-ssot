---
기술지원명: Transfer a project or team to a different account
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Transfer a project or team to a different account
출처링크: https://help.figma.com/hc/en-us/articles/10250387712407-Transfer-a-project-or-team-to-a-different-account
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

**Project transfers**: Any plan can send a project. Only Professional, Organization, or Enterprise plans can receive a project.

**Team transfers**: Any plan can send a team. Only Organization or Enterprise plans can receive a team.

Only [admins](https://help.figma.com/hc/en-us/articles/4420557724439) can transfer a project or team to another account

You can transfer a project or an entire team to another account.

You can choose one of the following options:

- **Transfer a project**: Move the project and all its files to another team or organization
- **Send a copy of a project**: Duplicate a project to the destination while keeping your originals
- **Transfer a team**: Moves all projects and files to the destination organization

**Note**: The easiest way to move files between different accounts is to move them into a project and then transfer the project by following the instructions below.

If the recipient is on the free Starter plan—or you just have one or two files to move—you can also transfer files between accounts by [saving a copy of the file to your computer](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-a-file) and then [importing it](https://help.figma.com/hc/en-us/articles/360041003114) in another account.

## What's included in a transfer

Project or team transfers include the following resources:

| Resource | Included |
| --- | --- |
| Files | ✓ |
| Prototypes | ✓ |
| Comments | Yes, except when sending a copy |
| File version history | Yes, except when sending a copy |
| Branches | Yes, except when sending a copy. When sending a project from an organization to a Professional team, all branches show the last known state before the transfer. Creating new branches isn’t available on the Professional plan. |
| Components in files where the library is included in the transfer | ✓ |
| Components in files where the library is not included in the transfer | Components will show the last known state before the transfer and will not receive updates afterwards |
| Shared fonts | X |
| Private plugins | X |
| Published Community resources | X |

**Note**: You can keep accessing files and prototypes at their original links after the transfer.  Projects and teams will get new links in the destination organization. Any published sites or Make files will be unpublished when transferred.

## Transfer a project

When you transfer a project, all its files move to the recipient’s team or organization. The recipient decides whether to keep or remove collaborators from the sending team.

**Before you start:**

- Transfers typically take around 5 minutes to complete. During this time, project members may experience limited access.
- If a transferred file includes a published library, files in the sender’s team or organization will no longer receive library updates after the transfer. We recommend keeping libraries and their files together.

There are three steps to transfer a project:

1. [Recipient: Get the destination team URL](#h_01J5BDVCA09JQTGQQCDYDN9Q11)
2. [Sender: Make the transfer request](#h_01J5BDVCA0PJ290B0EWF27SJXW)
3. [Recipient: Accept the transfer](#h_01J5BDVCA0BKBEHYD75A418FMB)

### 1. Recipient: Get the destination team URL

Before you can move a project, the recipient needs to choose a destination.

An admin in the receiving team or organization must provide a destination URL. This tells Figma where project should go.

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. Navigate to the destination team page:
   - Professional plan: Select  **All projects** from the left sidebar.
   - Organization or Enterprise plan without workspaces enabled: Select  **All teams** from the left sidebar, then choose a team.
   - Enterprise plan with workspaces enabled: Select  **All workspaces** from the left sidebar, then choose a team from the **Your teams** tab.
3. Copy the entire URL in your browser’s address bar.
4. Share this URL with the admin transferring the project.

Tip: You can always [move a project](https://help.figma.com/hc/en-us/articles/12729516837271-Move-a-project) to a different team later on.

### 2. Sender: Make a transfer request

Next, the project sender needs to make the transfer request.

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. View a list of projects within a team.
   - On the Starter or Professional plan, select  **All projects** from the left sidebar.
   - On the Organization or Enterprise plan, select  **All teams** from the left sidebar. Then, select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, select a team from the **Your teams** tab.
3. Select the project you’d like to transfer.
4. Click the down arrow next to the project name and select **Settings**.
5. Click **Transfer**.
6. Review the information in the modal and press **Next.**
7. Enter the destination URL and email address of your contact at the other company and press **Request transfer.**

### 3. Recipient: Accept the transfer

When a transfer request is sent, Figma emails all admins in the destination plan to review and accept it.

- On the Professional plan, these are [team admins](https://help.figma.com/hc/en-us/articles/4420557724439).
- On the Organization or Enterprise plans, these are [organization admins](https://help.figma.com/hc/en-us/articles/4420557724439).

You can choose to either **Remove collaborators**, or **Keep all existing collaborators**.

- Remove collaborators: Everyone will lose access to the project except the admin who accepts the transfer and the designated contact person.
- Keep all existing collaborators: Members from the sending party with a role on the project will get a View seat in your team or organization.

Enterprise admins:

- If your organization has [restricted guest access](https://help.figma.com/hc/articles/4410793238167), guests won’t transfer—even if you choose to **Keep all existing collaborators**.
- The project’s [organization-level access](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions) generally stays the same when it’s transferred.
  - If access is set to **Anyone at the workspace** and the receiving organization doesn’t use workspaces, access is set to either **Anyone at the organization** (Organization or Enterprise plans) or**Only invited users** (Professional plan).

![Options to manage collaborators during a Figma project transfer: remove collaborators or keep all.](https://help.figma.com/hc/article_attachments/28223509760919)

## Send a copy of a project

When you send a copy, Figma duplicates the project and all its files to the recipient’s team or organization. Only members of the destination have access to the copy. Branches, comments, and version history remain with the originals.

There are three steps to transfer a project:

1. [Recipient: Get the destination team URL](#h_01J5BDVCA080KV3CQ9VVFAYDMN)
2. [Sender: Send the copy](#h_01J5BDVCA0B2CM6Q532EGQ9AVD)
3. [Recipient: Accept the copy](#h_01J5BDVCA0XMQKX3H9HNSF3E03)

### 1. Recipient: Get the destination team URL

Before you can send a copy of a project, the recipient needs to choose a location for it.

An admin at the receiving team or organization will need to provide the sender with a destination URL. This tells Figma where project should go. To get this URL:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. Navigate to the destination team page:
   - Professional plan: Select  **All projects** from the left sidebar.
   - Organization or Enterprise plan without workspaces enabled: Select  **All teams** from the left sidebar, then choose a team.
   - Enterprise plan with workspaces enabled: Select  **All workspaces** from the left sidebar, then choose a team from the **Your teams** tab.
3. Copy the entire URL in your browser’s address bar.
4. Share this URL with the admin transferring the project.

Tip: You can always [move a project](https://help.figma.com/hc/en-us/articles/12729516837271-Move-a-project) to a different team later on.

### 2. Sender: Send the copy

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. View a list of projects within a team:
   - On the Starter or Professional plan, select  **All projects** from the left sidebar.
   - On the Organization or Enterprise plan, select  **All teams** from the left sidebar. Then, select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, choose a team from the **Your teams** tab.
3. Select a project.
4. Click the down arrow next to the project name and select **Settings**.
5. Click **Send a copy**.
6. Review the information in the modal and press **Next.**
7. Enter the destination URL and email address of your contact at the other organization and press **Send.**

Note: If you’re sending a project to an Organization or Enterprise, the recipient must be an [organization admin](https://help.figma.com/hc/en-us/articles/4420557724439).

### 3. Recipient: Accept the copy

When someone sends you a transfer request, Figma will send you an email asking you to review and accept the transfer.

It takes around 5 minutes to copy the project between companies. Once the transfer is complete, you can find the project by navigating to it in the file browser.

## Transfer a team

When you transfer a team, all its projects and files move to the recipient organization.

**Before you start:**

- The transfer typically completes in about 5 minutes. Team members may have limited access during this time.
- Transferred teams retain their [team access settings](https://help.figma.com/hc/en-us/articles/360039970673-Team-permissions#h_01K6NBT5RPHEE8JD14YY8JD0YS), whether that's open to anyone in the organization, or **Only those invited.**
- If a transferred file includes a published library, files in the sender’s organization will no longer receive updates after the transfer.

**Billing and seat implications:**

**Transfer a Starter team**

When transferring a Starter team, all users join the receiving organization
with a View seat.

**Transfer a Professional team**

When transferring a Professional team, all users join the receiving organization
with a View seat, unless they already have a paid seat in the destination
organization, in which case they retain that seat. Any assigned paid seats
on the original team also transfer to the destination organization as available,
prorated seats—but if the destination organization already has unassigned
paid seats, those count toward the total first, and only the remaining seats
needed are added.

**Example**: If your Professional team has 5 users with Full seats
and the destination organization already has 2 unassigned Full seats, all 5 users
join as View seats—and the destination organization receives 3 additional
unassigned Full seats, bringing its total available Full seats to 5.

Tip: Want to avoid transferring paid seats? Downgrade
users from paid seats to View seats before initiating the transfer.
If no paid seats are assigned at the time of transfer, none will
carry over.

These implications apply when you transfer a team yourself. If you need seat
assignments preserved during the transfer, contact Figma Support instead.

The receiving organization also gets a prorated credit for any remaining
time on your plan, applied at their next invoice.

**Example**: If you transfer your team halfway through a monthly
billing
period, the receiving organization receives a credit covering the second
half of that month.

**Transfer an Organization or Enterprise team**

When transferring an Organization or Enterprise team: All users with any
role on any of the team files or projects join the receiving organization
with a View seat, unless they already have a paid seat in the destination
organization, in which case they retain that seat.

There are three steps to transfer a team:

1. [Recipient: Provide the destination URL](#h_01J5BDVCA0WKJV21TRWXPE7VMC)
2. [Sender: Make the transfer request](#h_01J5BDVCA0Y8Y6Z5X82TFPGD0A)
3. [Recipient: Accept the transfer](#h_01J5BDVCA07EAHF7F1ZWED8V17)

### 1. Recipient: Provide the destination URL

An admin in the receiving organization must share a destination URL that tells Figma where to place the team.

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. Click **All teams** or **All workspaces**.
3. Copy the entire URL in your browser address bar.
4. Send this URL to the admin sending the team.

### 2. Sender: Make a transfer request

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a Figma file, click the  Figma menu > **Back to files.**
2. Open a team page:
   - On the Starter or Professional plan, select  **All projects** from the left sidebar.
   - On the Organization or Enterprise plan without workspaces enabled, select  **All teams** from the left sidebar. Then, select a team.
   - On the Enterprise plan with workspaces enabled, select  **All workspaces** from the left sidebar. Then, choose a team from the **Your teams** tab.
3. Click the down arrow next to the team name and select **View settings**.
4. In the **Transfer** section, click **Transfer team to an external organization.**
5. Review the information in the modal and press **Next.**
6. Enter the destination URL and email address of your contact at the other organization and press **Request transfer.**

Figma will email the contact and admins in the destination organization.
You’ll receive an email when the transfer is complete.

### 3. Recipient: Accept the transfer

Figma emails the designated contact and all organization admins to review and approve the team transfer.

After you accept, you can find the team by navigating to it in the file browser.

Enterprise admins:

- If there are guests in the team being transferred and you have [restricted guest access](https://help.figma.com/hc/articles/4410793238167), these guests won’t transfer with the team.
- If you have workspaces enabled, you will need to manually [assign the team to a workspace](https://help.figma.com/hc/articles/4419471354007) after the transfer is complete.
- The team’s [organization-level access](https://help.figma.com/hc/en-us/articles/35361119554711-File-and-project-permissions) generally stays the same when it’s transferred.
  - If access is set to **Anyone at the workspace** and the receiving organization doesn’t use workspaces, access is set to **Anyone at the organization**.
