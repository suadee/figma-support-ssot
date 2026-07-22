---
기술지원명: Set AI credit limits
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Set AI credit limits
출처링크: https://help.figma.com/hc/en-us/articles/41944442159767-Set-AI-credit-limits
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on paid plans

On the Professional plan, team admins can set user limits. On the Organization plan, organization admins can. On the Enterprise plan, organization admins can manage limits for anyone on the plan, and billing group admins can manage limits for members of their own group.

Note: This feature is slowly rolling out to paid plans over July and August 2026. If you don’t see the feature in your account yet, you should have it within a few weeks.

As an admin, you can control how many of your plan's paid AI credits each person can use. This gives you a way to manage costs and choose who gets to be the AI power users in your organization.

**Note**: This article covers limits for individual people. See [Manage AI credits for billing groups](https://help.figma.com/hc/en-us/articles/39663732696087) for billing group level controls.

## Overview

Each person on your plan has one of three levels of paid credit access:

- **Full access:** no limit, the person can use paid credits up to what's available on your plan.
- **Custom credit limit:** the person can use up to a specific number of paid credits you set for them each month.
- **No access:** the person can't use paid credits at all. Once they use up their included seat credits, they're blocked until the next reset.

Every user starts will **Full access**, and admins can change their access level at any time.

### How this works with other credit limits

A person's limit, their [billing group limit](https://help.figma.com/hc/en-us/articles/39663732696087-Manage-AI-credits-for-billing-groups) (if applicable), and your plan's overall credits all apply independently. Whichever one runs out first blocks that person from using paid credits.

Example

Jesse has a custom limit of 300 credits a month, and he's in a billing group with a shared limit of 1,000 credits a month. If his billing group runs out of credits before he reaches his own 300 credit limit, he's blocked from further AI use—even though he hasn't hit his personal limit yet.

If his billing group still has plenty left but he reaches his 300 credit limit first, his own limit is what blocks him instead. He can request more credits from his admin.

The same logic applies to your plan's overall credits: if the plan runs out, everyone is blocked, no matter what their individual or billing group limits allow.

## Set access for one person

To manage paid AI credit access or limits for an individual:

1. Open the file browser by logging in to your account at [figma.com](http://figma.com). If you're in a file, click the  Figma menu > **Back to files**.
2. Click  **Admin**.
3. Select the  **People** tab.
4. Select a user’s name to open their user management side panel.
5. In the **AI credits** section, click **Set limit**.
6. In the modal, set their access. If you select **Custom credit limit**, use the slider to enter a monthly credit amount.
7. Click **Save**.

![Manage paid AI credit access from the People page..png](https://help.figma.com/hc/article_attachments/41945568940439)

**Note**: You can also set access by clicking directly on a user’s access level from the **Paid AI credit access** column, or from the AI credits dashboard.

## Set access for multiple people at once

You can set AI credit access for users in bulk:

1. Open the file browser by logging in to your account at [figma.com](http://figma.com). If you're in a file, click  the Figma menu > **Back to files**.
2. Click  **Admin**.
3. Select the  **People** tab.
4. Select multiple people using the checkboxes.
5. From the bulk actions menu, choose **Change paid AI credit access.**
6. In the modal, set their access. If you select **Custom credit limit**, use the slider to enter a monthly credit amount.
7. Click **Save**.

## What happens when someone reaches their limit

When someone reaches their limit, they see an "Out of AI credits" message on the AI surface they're using. If they’ve hit their individual user limit, but more plan or billing group credits are still available, they can click the **Request more** button to request more credits from their admin.

Admins will receive a notification of the request via email and in app, and can choose whether to increase the individual’s AI credit limit.

[Learn more about AI credit requests](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work#h_01KHS83VXRE7WFXHW3P6GEATFR).

## Related resources

- [How AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work) — What AI credits are, how they're included with each seat, and what drives consumption up or down.
- [Manage AI credits](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits) — Purchasing additional paid credits and managing overall credit usage at the plan level.
- [Manage AI credits for billing groups](https://help.figma.com/hc/en-us/articles/39663732696087-Manage-AI-credits-for-billing-groups) — Setting a shared credit limit for a whole billing group instead of one person.
