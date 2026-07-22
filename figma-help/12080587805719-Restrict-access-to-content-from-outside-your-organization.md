---
기술지원명: Restrict access to content from outside your organization
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Restrict access to content from outside your organization
출처링크: https://help.figma.com/hc/en-us/articles/12080587805719-Restrict-access-to-content-from-outside-your-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

This feature requires [domain capture](https://help.figma.com/hc/en-us/articles/360045953273).

By default, members of a Figma organization can create and edit files outside the organization. For example, they can join files shared with them from people at other companies, or create new files in Starter and Professional teams outside the organization.

By restricting access to external content, organization admins can keep everyone’s work inside the company Figma organization. When access to external content is disabled, members can’t:

- Create new files or projects outside your organization.
- Edit files they’ve created outside your organization.
- Edit or comment on files shared with them from people outside your company.
- Accept **new invites** to join files, projects, or teams from outside your company. The exceptions are **open sessions in FigJam**, **public files**, and **password protected files**. In these cases, people can join the files with **view-only** permissions.

**Note**: When this setting is enabled, everyone's permissions will change to **view-only** in files they have access to outside of your Figma organization. This includes drafts they’ve made in other organizations or in Starter and Professional teams outside your organization.

![A screenshot showing the banner that appears in the External Teams space telling users that external content has been restricted](https://help.figma.com/hc/article_attachments/15105275079447)

### Let people know about the change in advance

Before limiting access to content outside your organization, we recommend telling people in advance what they can expect. Here’s a customizable message template you can use to prepare everyone for the change.

Hi team,

On [date], we're going to change an important setting in our Figma organization. In an effort to keep [company name]’s creative work inside our organization, we're going limit editing access to content from outside our company.

Here's what you can expect on [date]:

- Any existing files, projects, and teams shared from outside our company will switch to **view-only**.
- You won't be able to accept new invites to join files, projects, or teams shared outside our company.
- You won't be able to create drafts, files, or projects outside of the [company] organization.
- Any drafts you've made outside of the organization will become view-only.
- You can still create and edit drafts within the [company] organization.
- You can still join open sessions in FigJam, public files, and password protected files from outside our organization with view-only permissions.

Before [date], please review any content you have access to outside our organization. You can click on the name of our Figma organization at the top left of the file browser to view other organizations or teams you have access to.

If you have content you need to move into our Figma organization, export or [save a copy of each file to your computer](https://help.figma.com/hc/en-us/articles/8403626871063.html), then [import the files](https://help.figma.com/hc/en-us/articles/360041003114.html) by dragging and dropping them in Figma’s file browser.

If you have questions about this change, please reach out to [person or process].

## Enable or disable access to external content

Access to external content is enabled by default. You can disable or re-enable access at any time by following the instructions below.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Admin.**
2. Select the **Settings** tab.
3. Under **External access**, click **Access to external content**.
4. Change the setting and press **Save**.

**Note**: For added security, we recommend using this feature with [single-sign on authentication](https://help.figma.com/hc/en-us/articles/360040532333).
