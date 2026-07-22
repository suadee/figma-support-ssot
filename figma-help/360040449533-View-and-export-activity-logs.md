---
기술지원명: View and export activity logs
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: View and export activity logs
출처링크: https://help.figma.com/hc/en-us/articles/360040449533-View-and-export-activity-logs
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Only organization admins can view activity logs

Activity logs provide a record of how members and guests interact with organization files and resources.

- See when people access, copy, and share files.
- Track any changes made to team administration and settings.
- Track any changes made to team, project and file permissions.
- View actions taken by specific members.
- Track changes made by organization admin to organization-level settings.
- Identify and prevent misuse of any organization resources.

**Monitor security at scale with the Activity Logs API.** On the Enterprise plan, organization admins can use the [Activity Logs API](https://figma.com/developers/api#activity_logs) to protect their organization’s creative work. Use this API to identify anomalous events faster, build an internal application, and create security rules.

## View activity logs

Access activity logs in the **Activity** tab of the organization's **Admin**.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Click **Activity** in the left sidebar.
3. Use the fields to filter results by your desired criteria. Choose from:
   - **Member**: Enter an email address to view any events related to that person. These can be actions they have taken, or actions taken by someone else that apply to them.
   - **Date**: Enter a start and end date to see results for a specific date range.
   - **Events**: Select a specific type of event. [**Explore tracked events ↓**](#events)
   - **Team:** Select a team to view activity within that specific team.

![The Activity tab of Figma admin, showing user activity such as when files were viewed.](https://help.figma.com/hc/article_attachments/28287152772503)

**Note**: Admins can also view recent activity for a specific member or guest in the  **People** tab. If they click to see more activity, Figma will open the **Activity** tab with that person's email address already populated.

## Activity log events

The activity log begins tracking events as soon as you've upgraded to the Organization or Enterprise plans.

**Note**: Activity logs don't track events on Starter or Professional teams and cannot be retroactively applied after upgrading to an Organization or Enterprise plan.

For every event in the activity log, you'll see:

- The type of **event** that took place.
- The **team member**'s name and email address. This could be the person that took the action, or the person the event applies to.
- **Date** and **time** the event occurred. All times are shown in Coordinated Universal Time (UTC).
- **Product** the event relates to, if applicable.
- The **Team** the event relates to, if applicable.
- **IP address** of the related team member.

![Activity log header with member, date, product, team, and IP details](https://help.figma.com/hc/article_attachments/6132624715159)

**Note**: It's not possible to review activity logs for individual members after they have been removed from an organization.

### Members

- Members signed in or signed out

Note: Figma doesn't record login events for guests of the organization. Figma also doesn't track when a member closes a browser window or exits Figma without logging out.

### Files

- Created a file
- Duplicated a file
- Exported a file
- Downloaded an image
- File link access changed
- File link expiration changed
- Viewer permissions changed
- File membership changed
- Moved a file
- Permanently deleted a file
- Restored a file
- File password set
- File password unset
- Renamed a file
- Saved a file
- Trashed a file
- Viewed a file
- Viewed a prototype
- Open session started
- Open session ended

### Branches

- Created a branch
- Merged a branch
- Updated a branch
- Archived a branch
- Unarchived a branch
- Deleted a branch
- Branch membership changed

### Sites and web apps

- Custom domain connected
- Custom domain removed

### Projects

- Created a project
- Deleted a project
- Project membership changed
- Moved a project
- Renamed a project
- Change the team access of a project
- Outgoing transfers
- Incoming transfers

### Teams

- Created a team
- Deleted a team
- Outgoing transfers
- Incoming transfers
- Restored a team
- Team membership changed
- Renamed a team
- Changed the org access of a team
- Changed the workspace of a team
- Changed team creation setting

### Organizations

- Org merged
- Org membership changed
- Exported the members list
- Exported the organization team list
- Exported the workspace team list
- Requested to join the org
- Org join request approved
- Org invite created
- Auto-approval settings updated
- Cursor chat enabled/disabled
- Idle session timeout changed
- SCIM token generated/revoked
- AI features enabled/disabled
- Web search enabled/disabled
- AI content training enabled/disabled
- File attachments enabled/disabled in Figma Make
- Seat renewals
- 2FA for guests enabled/disabled

### Seat changes

- Changed default seat type
- Upgrade requests and activity
- Org seat type changed

### External access

- Changed guest invite setting
- Changed open sessions setting
- Changed public link setting
- Changed network access setting
- External org membership changed
- External team membership changed
- Password protection setting changed
- Viewed an external file
- Viewed an external prototype
- Web publishing enabled/disabled
- Workspace web publishing setting changed
- Changed workspace public link setting
- External collaboration controls changed

### Workspaces

- Added workspace admins
- Removed workspace admins
- Created a workspace
- Deleted a workspace
- Renamed a workspace
- Changed a user’s workspace
- User selected their own workspace
- Workspace visibility setting changed

### Billing groups

- Added billing group admins
- Removed billing group admins
- Created a billing group
- Deleted a billing group
- Renamed a billing group
- Changed a user's billing group
- User selected their own billing group

### SCIM groups

- SCIM group created
- SCIM group deleted
- SCIM group renamed
- SCIM group connection added
- SCIM group connection removed

### Libraries

- Org library setting changed
- Workspace library setting changed
- Workspace library approval changed
- Org library approval changed

### Users

- Idle session timeouts
- User signed in/signed out

### Community

- File published, updated, or deleted
- Plugin published, updated, or deleted
- Widget published, updated, or deleted

### Private plugins

- Plugin published
- Plugin updated
- Plugin deleted

### Plugin management

- Plugin approval settings changed
- Plugins requested
- Plugins reviewed
- Install plugins org-wide

### Plugin publishers

- Plugin publisher accept/remove invite
- Plugin publisher invite
- Plugin publisher remove
- Plugin ownership transfer

### Private widgets

- Widget published
- Widget updated
- Widget deleted

### Widget management

- Widget approval settings changed
- Widget requested
- Widget reviewed
- Install widgets org-wide

### Widget publishers

- Widget publisher accept/remove invite
- Widget publisher invite
- Widget publisher remove
- Widget ownership transfer

### SSO Authentications

- Google SSO authentication changed
- SAML SSO authentication changed

### Audio

- User joined audio call

### Integrations

- Personal access token created/deleted
- App connected/disconnected
- Supabase integration enabled/disabled
- Supabase project connected
- Supabase project disconnected

### Custom MCP connectors

- Custom connector created
- Custom connector updated
- Custom connector deleted
- Custom connector published
- Custom connector unpublished

### Webhooks

- Webhook created
- Webhook updated
- Webhook deleted

### Domain management

- Domain capture updated
- Domain added
- Domain removed
- Domain verified

### GitHub

- GitHub app changes
- GitHub repository changes

### SCIM provisioning

- User is provisioned to the organization
- User is deprovisioned from the organization
- User’s profile is updated, including name, email address, or title
- User’s [seat type is changed](https://help.figma.com/hc/en-us/articles/360048787534) (Enterprise plan only)

**Note**: SCIM events are recorded with the label ‘Identity provider’ in the **Team Member** column of the **Activity** table. To view all recent SCIM events, click **Get CSV** and manually filter the exported data by ‘Identity provider’.

## Export the activity log to CSV

You can export a copy of your activity log to CSV. This is a great option if you want to explore the data in a spreadsheet or other tool.

The export will include all events within the date range you select, and will ignore other filters you may have applied on the Activity page. To request an export:

1. If required, click the **Last 30 days** filter and select a different time period, or select **Custom** to enter your own start and end dates.
2. Click  **Get CSV** in the top-right corner of the screen.
3. Figma will email you the activity log in CSV format.

## **Activity Logs API**

The Activity Logs API provides programmatic access to your organization's activity logs. Activity logs allow you to see how people are accessing and using your organization. You can use the Activity Logs API to build your own custom applications.

To learn more about using the Activity Logs API, check out the [Figma REST API documentation](https://www.figma.com/developers/api#activity-logs-intro).
