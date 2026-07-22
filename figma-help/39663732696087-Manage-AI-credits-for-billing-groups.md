---
기술지원명: Manage AI credits for billing groups
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage AI credits for billing groups
출처링크: https://help.figma.com/hc/en-us/articles/39663732696087-Manage-AI-credits-for-billing-groups
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on the Enterprise plan

On Enterprise plans, organization admins can manage AI credits at the billing group level. This allows you to allocate credits across teams, departments, or cost centers, and better control how AI usage maps to your organization’s budget.

[Learn more about managing and purchasing additional AI credits for your organization](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits).

## Overview

Billing group controls apply to AI credits available at the plan level, including:

- Credits from an AI credits subscription (if purchased)
- Credits available through pay-as-you-go (if enabled)

[Learn more about AI credit purchasing options](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits).

Billing group controls do not apply to individual seat credits. Seat credits:

- Are assigned per user based on seat type
- Can’t be reallocated between users

[Learn more about how AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work).

## Manage billing group credits

You can divide your plan’s total shared AI credits into:

- **Billing group credits:** Credits set aside for specific billing groups
- **Remaining credits:** Credits that haven’t been set aside for a group

You must purchase an AI credits subscription or enable pay-as-you-go billing before you can set aside credits per billing group.

To set aside credits for a billing group:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/). If you’re in a file, click  the Figma menu > **Back to files.**
2. Click  **Admin**.
3. In the **AI credits** section, click **Manage**.
4. Select the **Billing groups** tab.
5. Hover over a billing group row and select  **More > Manage credits**.
6. In the modal, use the slider to to set a number of credits aside for the billing group.
7. Click **Assign credits** to confirm.

![Set aside AI credits for each billing group from the Billing groups tab of the AI credits admin page.](https://help.figma.com/hc/article_attachments/39797190898711)

After confirming, the updated credit amount will appear in the **Billing group credits** column of your AI credits dashboard.

To change the amount of credits for a billing group, repeat the steps above and enter a new value. To remove credits for a billing group, set the value to 0.

Organization admins can also view and manage billing group AI credits from **Admin > Billing > Billing groups**. From this page, you can bulk assign AI credits by selecting multiple billing groups and choosing **Manage AI credits** from the bulk actions toolbar.

![Manage billing group AI credits in bulk from the billing groups tab of the billing page](https://help.figma.com/hc/article_attachments/39797190901911)

## Understand the AI credit dashboard

To track how each billing group is using AI credits:

1. Open the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183-Guide-to-the-file-browser) by logging in to your account at [figma.com](https://figma.com/). If you’re in a file, click  the Figma menu > **Back to files.**
2. Click  **Admin**.
3. In the **AI credits** section, click **Manage**.
4. Select the **Billing groups** tab.

Each row represents a billing group, with a summary of its usage and available credits.

If you have set aside any billing group credits, the top of the **Billing groups** tab shows:

- **Billing group credit usage**: The total number of billing group AI credits used and set aside across all billing groups.
- **Remaining credits**: Credits that haven’t been set aside for a billing group. Billing groups without credits set aside will use these.
- **Days until credit reset**: The number of days until credits reset for the next billing cycle.

## How billing group credits work

### Remaining credits

All paid AI credits start as remaining credits.

- Remaining credits are available to any billing group without credits set aside
- When you set aside credits for a group, that amount is deducted from remaining credits
- Billing groups without billing group credits set aside will share the remaining credits

**Example**

Your organization has 5,000 AI credits purchased through an AI credits subscription.

- You set aside 2,000 credits for the Design team billing group
- You set aside 1,000 credits for the Marketing team billing group
- The remaining 2,000 credits are available for any other billing groups

Billing groups without billing group credits set aside will draw from the remaining credits as they use AI features.

### Maximum credits per billing group

The maximum number of billing group credits you can set aside for a group is the total number of paid credits available on your plan, including subscription credits and any pay-as-you-go budget.

**Example**

Your organization has 5,000 AI credits purchased through an AI credits subscription, and a 3,000 pay-as-you-go spending limit.

You can set aside up to 8,000 credits for each billing group in your organization.

### Setting aside more credits than your total

You can set aside more credits across billing groups than your plan total.

This doesn’t increase your total credits. Instead:

- Not all groups will be able to use their full amount
- Your total credits are more likely to be fully used each cycle

**Example**

Your organization has 5,000 AI credits purchased through an AI credits subscription.

- You set aside 3,000 credits for the Design team billing group
- You set aside 3,000 credits for the Marketing team billing group

If the Design team uses all 3,000 credits first, only 2,000 credits remain for the rest of the organization. This means the Marketing team can only use up to 2,000 credits, even though 3,000 were set aside.

### Using all credits across billing groups

If you set aside all available credits across billing groups:

- Each group has a fixed amount of credits
- Groups won’t use each other’s unused credits
- Any unused credits expire at the end of the billing cycle

**Example**

Your organization has 5,000 AI credits purchased through an AI credits subscription.

- You set aside 2,500 credits for the Design team billing group
- You set aside 2,500 credits for the Marketing team billing group

If Design only uses 1,500 credits, the remaining 1,000 won’t be available to Marketing.

### Usage near billing group limits

When a group is close to its billing group credits:

- Usage may slightly exceed the amount set aside due to:
  - Variability in AI request cost
  - Multiple users using AI at the same time
- Any overage is deducted from your total plan credits

This may reduce credits available to other groups.

**Example**

The Design team billing group has 2,000 billing group credits and is close to its limit.

Several team members use AI at the same time, and total usage reaches 2,050 credits. The extra 50 credits are deducted from your remaining credits. If there are no credits available, further usage is blocked.

## Related resources

- [Manage AI credits](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits): Learn how to track usage, and purchase and manage AI credits across your plan.
- [How AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work): Understand what AI credits are and how they are consumed by AI features.
- [Manage billing groups in an organization](https://help.figma.com/hc/en-us/articles/19100486415255-Manage-billing-groups-in-an-organization#h_01HGKWWWE2SAAY6FWP2GYGC6B0): Learn how to manage billing groups as a organization or billing group admin.
- [AI Usage API](https://developers.figma.com/docs/rest-api/ai-usage/): Use the Figma REST API to get AI usage data. Enterprise plan only.
