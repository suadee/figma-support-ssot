---
기술지원명: Figma and Microsoft Teams
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Figma and Microsoft Teams
출처링크: https://help.figma.com/hc/en-us/articles/7405452518423-Figma-and-Microsoft-Teams
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Supported on [all team and organization plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with **can edit** access to a FigJam file can edit the file via Microsoft Teams

Anyone with **can view** or **can edit** access to a Figma Design file can view and comment via Teams

Anyone with **can edit** access to a file can see link previews of the file in Teams

Microsoft Teams is a communication app for teams and organizations to connect, collaborate, and stay informed in one place. Use Teams to send messages, hold video conferences, and share important files and information. [Learn more about Microsoft Teams →](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)

With the [Figma app for Microsoft Teams](https://appsource.microsoft.com/en-us/product/office/wa200004521?tab=overview), you can:

- Present and collaborate in Figma Design files, prototypes, and FigJam files with meeting attendees
- Add Figma files as tabs to any Teams channel and interact with them
- View a single feed of file comments, updates, and invites
- Share file links in chat that unfurl the file name and file preview

# Permissions

To integrate with Teams, the Figma app requests certain permissions:

- **Basic capabilities (required):** All Microsoft Teams apps require basic capabilities, a set of permissions determined by Microsoft's development framework. These permission aren't explicitly set by Figma, but rather are implicitly defined by Microsoft. As a part of these basic capabilities, the following permissions are included:

  - Receive messages and data that I provide to it.
  - Send me messages and notifications.
  - Access my profile information such as my name, email address, company name, and preferred language.
  - Receive messages and data that team or chat members provide to it in a channel or chat.
  - Send messages and notifications in a channel or chat.
  - Access information from this team or chat such as team or chat name, channel list and roster (including team or chat member's names and email addresses) - and use this to contact them.
  - Maintain access to the team's data.

  The Figma app needs these permissions to use tabs to embed files, share links to chats and channels, and get notifications. To learn more about basic capabilities, see [Microsoft's app permissions documentation →](https://learn.microsoft.com/en-us/microsoftteams/app-permissions#:~:text=Basic%20capabilities%3A%20When,any%20app%20functionality)
- **MeetingStage.Write.Chat (required):** One of the RSC delegated permissions for chats or meetings, [MeetingStage.Write.Chat →](https://learn.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema#:~:text=MeetingStage.Write.Chat) lets the app show content on the meeting stage in meetings associated with the chat, on behalf of the signed-in user. Figma uses this permission to let users present Figma files in meetings.

# Use tabs to embed files

Tabs in Microsoft Teams allow you to embed important files, apps, or services in Teams meetings or channels. [Learn more about tabs →](https://support.microsoft.com/en-gb/office/first-things-to-know-about-apps-in-microsoft-teams-747492ee-7cdd-4115-a993-8c7e7f98a3d0)

You can use tabs to embed Figma Design files, prototypes, and FigJam files, and interact with them, without leaving Microsoft Teams.

- From Microsoft Teams, you can access all the functionality of **FigJam** files. For those with edit access, you can explore, add to, and edit FigJam files as you normally would.
- **Figma Design** files and prototypes are view and comment-only, even for people who have edit access to the file. You can click **Open in Figma** to open the file and edit from the web or desktop app.
- To allow others to see or interact with the file, you may need to adjust the [file's sharing and permissions](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes). FigJam files also have the option to start an [open session](https://help.figma.com/hc/en-us/articles/4410786053911-Invite-visitors-to-an-open-session) to temporarily invite anyone to edit the FigJam file, including those without Figma accounts.

## Add a tab

1. Start from one of the following places:
   - **From a meeting**: Click **+ Add app** from the meeting controls ![image showing add app modal in Microsoft Teams meeting](https://help.figma.com/hc/article_attachments/7735408078999)
   - **From a channel**: Click **+** next to the tabs at the top of the channel ![image of Microsoft Teams channel with cursor over plus button to add app to channel](https://help.figma.com/hc/article_attachments/7735391613847)
2. Find and select the Figma app.
3. From the modal, select  [Create FigJam file ↓](#h_01G8XWX7PB139ZZBYSBC7ZDDYD)  or  [Share existing file ↓](#h_01G8XWXT0SG3G3YNVPYEX3GZAJ) .

Note: The **+ Add App** option is available only in meetings that are scheduled. Unscheduled meetings created from a chat or channel will not have this capability.

### Create a FigJam file

Select this option to create a new FigJam file so teammates can brainstorm and collaborate together, even if you don't have a Figma account.

From the pop-up modal, give the FigJam file a name and click **Save**. A dedicated tab for the file is added to the channel or meeting.

- If your Figma account is already connected to tabs in Microsoft Teams, this new file can be found in your personal [drafts folder](https://help.figma.com/hc/en-us/articles/360041543473-Explore-your-Figma-account#draft-sidebar) in Figma.
- If a Figma account is not connected, you have 24 hours for someone to claim the file by clicking **Save board** in the FigJam file. If no one saves the board within 24 hours, the file is be permanently deleted.

### Share an existing file

Select this option to share an existing Figma Design file, FigJam file, or prototype.

If you haven’t yet connected your Figma account for app tabs in Teams, you will be prompted to log in to your Figma account.

From the pop-up modal, paste the link to the desired Figma Design or FigJam file into the text box. If you’re creating a channel tab, use the checkbox to choose whether to post to the channel about the new tab.

Click **Save**and a dedicated tab for the file is added to the channel or meeting.

![side-by-side image, showing where tabs are added in channels and in meetings](https://help.figma.com/hc/article_attachments/7735391560727)

Note: Connecting your Figma account for tabs does not connect your account to receive Figma notifications. You will need to link your Figma account separately if you wish to [receive Figma notifications ↓](#h_01G8XW0717MTGEQ8NDRGBPQ13Z).

## Present file in meetings

On Microsoft Team's desktop app, share your Figma file from the tab when you're ready to present it to meeting attendees:

1. Select the tab for the file you want to share.
2. Click **Share to stage** when you’re ready to present.

![image of side panel that appears when you click on a Figma tab during a Meeting, with cursor over Share to Stage button](https://help.figma.com/hc/article_attachments/7735407932695)

# Share links to chats and channels

Drop links to Figma Design and FigJam files in Teams chats and channels to reference designs, research, and other resources.

The link will expand to show a preview, with the file name and thumbnail displayed below your message.

1. Copy link to Figma Design or FigJam file. [Learn how to copy links to a file →](https://help.figma.com/hc/en-us/articles/360040531773#copy-link)
2. Paste link into a meeting or channel chat and send the message.

Link previews will be seen by anyone whose Figma account has access to the file and is [connected to receiving Figma notifications ↓.](#h_01G8XW0717MTGEQ8NDRGBPQ13Z)

![image of an expanded link to a Figma file shared to a Teams channel](https://help.figma.com/hc/article_attachments/7735391410967)

# Get notifications

Get notifications for updates to your Figma Design and FigJam files in a single feed from the Figma app’s chat.

- Get notified when someone comments and mentions you in files you follow
- Get notified when someone invites you to a file
- Reply to comments
- Accept or decline invites to files, projects, and teams
- Get notified when [Dev Mode statuses change](https://help.figma.com/hc/en-us/articles/26781702258583)
- (Organizations only) Get [updates on branches and merges](https://help.figma.com/hc/en-us/articles/360039813234-Stay-in-the-loop-with-notifications#Branching_Organization_plans_only)

## Enable notifications

To receive Figma notifications in Microsoft Teams:

1. Click  in the left sidebar.
2. Find and select the Figma app.
3. From the app’s chat box, type `Connect` and send the message. Follow the prompts to connect your Figma account.
4. Once connected, type `On` into the chat box and send the message to enable notifications.

You’ll begin receiving any new comments, mentions, and invitations in this chat.

## Manage notifications

To manage Figma notifications in Microsoft Teams, type and send the following `commands` into the app’s chat:

- `On` to start receiving notifications on updates from your Figma account
- `Off` to stop receiving further Figma notifications
- `Connect` to connect your Figma account to the Figma notifications feature
- `Disconnect` to disconnect your Figma account from the Figma notifications feature. This only prevents you from receiving further notifications via the chat. This won’t affect any files you’ve added to tabs.

Note: Using [@mentions](https://help.figma.com/hc/en-us/articles/360041068574-Add-comments-to-files#mention) when replying to a comment from Microsoft Teams is currently not supported.
