---
기술지원명: Get Figma notifications in Slack
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Get Figma notifications in Slack
출처링크: https://help.figma.com/hc/en-us/articles/360039829154-Get-Figma-notifications-in-Slack
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

 

Supported on [all team and organization plans](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with **can edit** access to a file, project, or team can subscribe a channel to a resource that is accessible to everyone on a team.

Anyone with **can edit** access to a file can see previews of the file in Slack.

Stay on top of updates to Figma files, projects, and teams by installing the [Figma integration for Slack](http://slack.com/apps/A01N2QYSA81-figma). With the Figma integration in Slack, you can:

- View a single feed of Figma comments you’ve been mentioned in
- Get timely feedback from teammates and stakeholders
- Customize Slack channels with updates on specific projects and teams, or conversations happening in relevant files.

Figma for Slack brings your Figma notifications to Slack so you can easily and quickly respond. The [Figma Privacy Policy](https://www.figma.com/legal/privacy/) applies to Figma for Slack.

Figma notifications in Slack come in two types: **default notifications** and **channel subscriptions**.

[**Default notifications ↓**](#h_01FXKNJCFTKQ9BAGNCKPZNY1KJ) appear on your **Figma** app channel and include comments you've been mentioned in and invitations to files, projects, and teams.

With [**channel notifications ↓**](#h_01FXKNJK0DF0DCSGM0V73V9EM0), you can customize your Slack channels to receive notifications on specific files, projects, and teams. Notifications can include comments, mentions, branching updates, new files, and new projects. [**Learn more ↓**](#h_01FXKNJK0DF0DCSGM0V73V9EM0)

![figma and slack icons with bidirectional arrow](https://help.figma.com/hc/article_attachments/4622255502103)

# Set up

To set up your Figma app integration in Slack:

1. [**Add the Figma app to your Slack workspace ↓**](#h_01FXKNK75VWPSHPHB3G4HJW300).
2. Once added, **[connect your Figma account to Slack ↓](#h_01FXKNM6CMMFMZKM1Z095XTJ5X)**to receive notifications and create channel subscriptions.

If you want to use the Figma integration in multiple Slack workspaces, you'll need to repeat the set up process in each workspace.

## Add Figma app to Slack

Any Slack workspace member can install apps to the Slack workspace. However, Slack owners and admins can [restrict this ability](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#manage-app-approval).

Add the Figma app to your Slack workspace from the Slack App Directory.

1. Navigate to the **Apps** section of your Slack workspace. ![add Figma app in Slack](https://help.figma.com/hc/article_attachments/4621850054039)
2. Click  or **Add apps**.
3. Search **Figma** in the directory.
4. Install the **Figma** app and authorize access to your Figma files. ![Figma authorization screen for Slack app](https://help.figma.com/hc/article_attachments/360104339153)

**[Learn more about adding apps to your Slack workspace →](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace)**

Once you’ve successfully added the Figma app to your Slack workspace, any member of the Slack workspace can connect their Figma account and subscribe channels to notifications.

Tip! In the **Figma** app channel, type `help` and hit send to see tips on using the Figma integration in Slack.

## Connect your Figma account to Slack

If the Figma app has been added to your Slack workspace, be sure to connect your Figma account to Slack.

1. Open the Figma app in Slack workspace.
2. Click **Connect your account.** A tab will appear prompting you give Figma access to Slack. ![connect your account button in Figma app channel](https://help.figma.com/hc/article_attachments/4621869081239)
3. Click **Allow**.

# Get default notifications

After [set up](#h_01FXN7XDRTN8D5HVGXSEX7P7V0) is complete, you’ll start receiving these notifications by default:

- Comments you’ve been mentioned in
- Files, projects, and teams you've been invited to

Default notifications show up in your **Figma** app channel.

You can turn these notifications on and off at any time.

**Note:** Developers are auto-subscribed to [status notifications](https://help.figma.com/hc/en-us/articles/26781702258583-Dev-Mode-statuses-and-notifications#h_01J96T2MJRH0Y3ZAKB13FKS9W1) once they’ve viewed a file in Dev Mode. They will receive an email notification when a design’s status is changed to “Ready for dev.”

## Manage default notifications

To turn your default notifications from Figma on or off in Slack:

1. Navigate to the **Figma** app channel.
2. Type:
   - `off` or `stop` in the text field to turn notifications off
   - `on` or `start` in the text field to turn notifications on
3. Press `return` or `enter` to send the message.

## Manage notification settings

To change your notification settings:

1. Navigate to the **Figma** app channel.
2. Type `/figma settings`
3. Update your preferences in the notification center, then click **Close.**

### Seat request upgrade notifications

Figma admins who use the integration will receive seat request notifications in Slack.

![Figma Slack notification for seat request showing options to approve or review in Figma.](https://help.figma.com/hc/article_attachments/30255018687383)

Admins can choose to approve requests directly from Slack, or review the requests in Figma.

To stop receiving Slack notifications for seat upgrade requests:

1. Navigate to the **Figma** app channel.
2. Type `/figma settings`
3. Under **Seat requests,** select **None.**
4. Click **Close.**

**[Manage email notifications for comments in Figma →](https://help.figma.com/hc/en-us/articles/360041547813)**

# Get channel notifications

Receive updates on specific Figma files, projects, and teams in your Slack channels. You can subscribe channels to updates on any resource where you have **can edit** access, and customize the frequency of notifications for each subscription. You'll need to make sure that the resource is [accessible to everyone on the team](https://help.figma.com/hc/en-us/articles/360052679454-Access-shared-resources-in-an-organization#h_01HFW5QSM25B6DEDF9JMGDQWKF) to create a channel subscription for it.

The types of notifications a channel receives depend on the resource type:

| Notification | File | Project | Team |
| --- | --- | --- | --- |
| [Comments, replies, @mentions](https://help.figma.com/hc/en-us/articles/360039825314) | ✓ |  |  |
| [Branching: merge requests, approvals, and changes suggested](https://help.figma.com/hc/en-us/articles/360063144053) | ✓ | ✓ | ✓ |
| New files added to project |  | ✓ | ✓ |
| New projects added to team |  |  | ✓ |

Here are some ways to make the most out of channel notifications:

- **Create new channels** dedicated to receiving notifications on project-specific files. This allows main channels to be used for conversation, minimizing channel noise.
- **Notify your team channel** of newly added files to a Figma project or team. This avoids needing to send file links over Slack or email every week for weekly meetings or retros.
- **Customize a Slack channel** with updates on conversations happening in relevant files.

## Add Figma app to a channel

If the Figma app hasn’t been added to a channel, you’ll need to add it first before you can create subscriptions.

1. Open the Slack channel you want to receive Figma notifications.
2. Type `/invite @figma` and press `enter` or `return`.

Once Figma has been added, you can create subscriptions for that channel.

## Create a channel subscription

Before you create a subscription in a Slack channel, make sure you’ve [**added the Figma app to the channel**](#h_01FXKRCJRKB389HV7CSQSW5J56).

To create a subscription for a Slack channel to receive updates on a Figma resource:

1. Open the Slack channel.
2. Type `/figma subscribe` and press `enter` or `return`. A modal appears for you to configure your subscription. ![Configure subscription to Figma notifications in Slack channel](https://help.figma.com/hc/article_attachments/4621850045847)
3. From the modal:
   1. Choose the type of source you want updates for: **file**, **project**, or **team**.
   2. Find your resource using the search bar.
   3. Choose how often updates on this resource will be delivered: **real time**, **hourly**, or **daily**.
      - For daily notifications, choose a specific time for them to be delivered to the channel.

Subscriptions are created one at a time. Repeat the process above to create more subscriptions. Each channel can have unlimited subscriptions, and multiple channels can be subscribed to the same resource.

Comments made within 10 minutes of each other will be batched in a single Slack message instead of individual messages.

## Remove a channel subscription

To stop receiving notifications about updates on a file, project, or team in a channel, you can remove the subscription:

1. Open the Slack channel you wish to remove a subscription from.
2. Type `/figma list` and press `return` or `enter`. A list of the channel’s subscriptions will appear.
3. Click **delete subscription** next to the subscription you wish to no longer receive notifications.

[**You can subscribe again at any time ↑**](#h_01FXKP86P8BZTM60XX56JQRKNZ)

# Remove Figma from Slack

To completely remove the Figma integration, you will need to disconnect the app from your Slack workspace.

**[Learn how to remove apps from your Slack workspace →](https://slack.com/help/articles/360003125231-Remove-apps-and-custom-integrations-from-your-workspace)**
