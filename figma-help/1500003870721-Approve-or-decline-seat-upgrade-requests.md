---
기술지원명: Approve or decline seat upgrade requests
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Approve or decline seat upgrade requests
출처링크: https://help.figma.com/hc/en-us/articles/1500003870721-Approve-or-decline-seat-upgrade-requests
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

In March 2025, Figma introduced updates to how seats and other billing features work. This article describes the updated billing model.

[Learn more about the transition to the updated billing model](https://help.figma.com/hc/en-us/articles/27468498501527).

Before you start

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

[Admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Admins use [seat approval settings](https://help.figma.com/hc/en-us/articles/4414038570007) to handle incoming seat requests.

If your seat approval settings require manual approval, then you’ll need to individually review each incoming seat request.

From the dashboard, admins can manually approve or decline seat requests. If a request is approved, the user is assigned to an available seat. If a seat isn't available, Figma adds a new paid seat to your account.

[Learn more about managing seats in Figma](https://help.figma.com/hc/en-us/articles/360039960434).

## Review pending upgrade requests

Admins can review, approve, or deny pending seat requests from their admin **Dashboard**.

- On the Professional plan, upgrade requests go to [team admins](https://help.figma.com/hc/en-us/articles/4420557724439).
- On the Organization or Enterprise plan without billing groups, upgrade requests go to [organization admins](https://help.figma.com/hc/en-us/articles/4420557724439).
- On Enterprise plans with [billing groups](https://help.figma.com/hc/en-us/articles/19100885191191):
  - Billing group admins receive requests from users in their billing group.
  - Organization admins receive requests from users who are not assigned to a billing group. They can also review all outstanding requests from the **Dashboard**.

To review seat requests:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/).
   - If you’re in a specific Figma file, you can access the file browser by clicking  the Figma menu > **Back to files** from the left sidebar toolbar.
2. Select **Admin** from the sidebar.

![The admin dashboard shows a list of pending requests](https://help.figma.com/hc/article_attachments/41066863800215)

From this page, you can:

- View the total number of pending seat requests.
- Select the **Reminders** tab to view requests from users who have sent a reminder.
- Click **Approve** to approve a seat request.
- Select an individual request to open a side panel with request details—including where the user sent the request from, request reason, current seat, time of request, and the cost to add the new seat.
- Click **View all** to open a seat request page, where you can filter and sort requests by user type, requested seat type, and billing group.
- View how many current assigned and available seats you have from the **Total seats** table.

Note: Upgrade requests from users whose [seats are managed via SCIM](https://help.figma.com/hc/en-us/articles/360048787534) won't appear in the dashboard. Admins still get notified of these requests, but can only manage them via the identity provider.

## Manage upgrade requests via notifications

Figma sends both an email and in-app notification to relevant admins when someone requests an upgrade. The person who made the request will get notified of your decision via an email and in-app notification.

**Notifications in Figma**

1. From the file browser, click the
   notification bell next to your user name to view your notifications.
2. You will see the name of the requester, requested seat type, and the
   cost of the seat change (if any).
   - Select **Approve** to grant them the requested
     seat type.
   - Select **Deny** to decline the request.
     Figma will let them know their request was declined and they
     will keep their current seat.

**Notifications via email**

1. Open the upgrade request email.
2. You will see the requester’s name, email address, and request details.
   Do one of the following:
   - Select **Approve** to grant them the requested
     seat.
   - Select **Review in Figma** to manage open up
     the file browser and manage the request from your
     **Dashboard**.
