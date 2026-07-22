---
기술지원명: Manage backend integration for an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage backend integration for an organization
출처링크: https://help.figma.com/hc/en-us/articles/34162517434007-Manage-backend-integration-for-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) only

Figma provides backend integration with Supabase for [Figma Make](http://figma.com/make). Figma Make is a prompt-to-app tool that lets you bring ideas and existing Figma designs to life as functional, interactive web apps and UI.

Figma Make integrates with Supabase to provide a backend environment that offers secret storage, compute, and a Postgres database. Figma Make will set up basic key-value stores inside this Postgres database; at the moment, Figma Make will not set up a full SQL database in the Postgres provided by Supabase.

By default, anyone with a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434) can add a backend integration to a Figma Make file. The user is the one who determines what Supabase project they're connecting to. The Supabase account they use doesn't need to be the same email address or method of login they use for Figma, which means the backend can be tied to individual, free Supabase plans, as well as Pro, Team, or Enterprise plans that may be managed by your organization.

When backend integration is disabled, users won't be able to connect new Figma Make files to Supabase.

![](https://help.figma.com/hc/article_attachments/34162936647447)

Additionally, if the model is prompted to use Supabase, it will provide mock code rather than functionally connecting to Supabase.

![](https://help.figma.com/hc/article_attachments/34162936652311)

## Restrict or enable backend integration for your organization

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Click the  **Settings** tab.
3. In the **External access** section, click **Backend integration** and enable or disable the feature.

**Caution:** Existing Figma Make files that are already connected are *not* disconnected from Supabase when you disable backend integration. If your users have already created files with backend integration, you'll need to instruct your users to manually disconnect those files from Supabase.
