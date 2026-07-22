---
기술지원명: Manage a library for a workspace or organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage a library for a workspace or organization
출처링크: https://help.figma.com/hc/en-us/articles/21310245473815-Manage-a-library-for-a-workspace-or-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

[Organization admins](https://help.figma.com/hc/en-us/articles/4420557724439) and [workspace admins](https://help.figma.com/hc/en-us/articles/4420557724439)

![The Manage Library modal, accessed from the Resources tab of Figma admin.](https://help.figma.com/hc/article_attachments/28287123757719)

As an organization scales, it can have tens, hundreds, or even thousands of published libraries available. Figma has three different ways organization and workspace admins can help people surface and use the best libraries for their work:

1. [Approve a library (Enterprise plan only)](#h_01HPJ9MNC4J7XP0DKGF72E8KXH)
2. [Enable a library by default for a workspace or organization](#h_01HPJ91TKHB3BNJNT0HJS5XC87)
3. [Set a default variable mode for a library (Enterprise plan only)](#h_01HPJA6RTTT98AAYR5EAAXE1CX)

**What’s the difference between approving a library and enabling a library by default?**

- Approving a library adds a check mark next to the library name so people can use its components, styles, and variables with confidence.
- Enabling a library by default for an organization or workspace adds the library to files by default, making it easier to access.

You might choose to combine these features, or just use one. For example:

- The marketing team has a library of client logos that have been officially approved for company use, so they mark the library as approved. Since most teams don’t need to use it in their day-to-day work, they don't enable it by default.
- The company is doing a brand overhaul and plans to launch a new design system. Many teams have already started designing with the new system, but it changes frequently. The library is enabled by default so designers can start exploring it in their designs, but with the understanding that it is not yet approved for production use.

## Approve a library

Enterprise

![Screenshot of a Figma file focusing on the 'Assets' panel. A tooltip reading 'Approved by Twigma admin' appears above a checkmark next to the 'Twigma Core' library, indicating it has been approved. ](https://help.figma.com/hc/article_attachments/21360047655191)

Approving a library for a workspace or organization lets everyone know that the library has been recommended by an admin. This helps people feel more comfortable choosing which components, styles, and variables to use in their designs.

When a library is approved, everyone sees a  check mark next to the library name wherever it appears in design files—like the assets panel or [quick inserts](https://help.figma.com/hc/en-us/articles/360039150173-Create-and-insert-component-instances#quick-insert)—or in **Admin**. Approved libraries are also pinned to the top of the list of available libraries in files.

**Note**: When a library gets approved for a workspace, everyone can see an approved check mark next to the library's name in all the workspace's files, even if they're not assigned to that workspace. In draft files, the approved libraries will only show as approved for the workspace someone is assigned to, since drafts don't belong to any workspaces.

### Approve or unapprove a library

Workspace admin Organization admin

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Select the relevant workspace in the sidebar.
3. Select the **Libraries** tab.
4. Search for—or navigate to—the library you’d like to approve or unapprove and click it.
5. In the **Manage this library** modal, click the toggle next to **Set as approved library**.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin** in the left sidebar.
2. Select the **Resources** tab.
3. Search for—or navigate to—the library you’d like to approve or unapprove and click it.
4. In the **Manage this library** modal, click the toggle next to **Set as approved library**.

**Note**: A workspace admin won’t be able to unapprove a library that’s been approved at the organization level.

## Enable a library by default for a workspace or organization

- On the Organization and Enterprise plans, organization admins can enable any [published library](https://help.figma.com/hc/en-us/articles/360040529593) by default for all files in the organization. Team admins can also [enable libraries they have access to for teams they manage](https://help.figma.com/hc/en-us/articles/360039234953).
- On the Enterprise plan, organization and workspace admins can enable libraries by default for all files in a workspace.

Enabling a library by default helps people access a library’s components and styles in their Figma Design and FigJam files, without having to manually search for and add the library.

Organization and workspace admins can enable a library by default for an organization or specific workspaces by selecting one of the following:

- **Design files:** Enables the library by default only for Figma Design files in the organization or workspace.
- **FigJam boards:** Enables the library by default only for FigJam files in the organization or workspace.
- **Slide decks:** Enables the library by default only for Figma Slides files in the organization or workspace.
- **Figma Buzz files**: Enables the library by default only for Figma Slides files in the organization or workspace.

**Note**: Other admins can override the default libraries and [default variable modes](#h_01HPJA6RTTT98AAYR5EAAXE1CX) for any workspaces or teams they manage. For example, if an organization admin enables a library by default for all files in an organization, a team admin can [modify this setting for teams they manage](https://help.figma.com/hc/en-us/articles/360039234953-Manage-libraries-in-teams). Whenever a lower-level admin overrides these settings for an [approved library](#h_01HPJ9MNC4J7XP0DKGF72E8KXH), higher-level admins get an in-app notification notifying them of the change.

### Enable or disable a default library

Workspace admins Organization admins

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Libraries** tab.
3. Navigate to, or search for, the library you want to manage and click it.
4. Select the workspace you want to enable the library for.
5. Select the Figma file types where you want to enable the library.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**.
2. Select the **Resources** page and then the **Libraries** tab.
3. Navigate to, or search for, the library you want to manage and click it.
4. Select the workspace you want to enable the library for.
5. Select the Figma file types where you want to enable the library.

**Caution**: The **Libraries** tab contains a list of all the libraries you have access to in the organization.

You can enable any library in the list as a default for the organization. This includes libraries where access may be restricted, such as those in closed or secret teams.

If the library file isn’t shared with everyone in the organization, you’ll see the following warning:

![Manage Library modal displaying library permission change warning and toggle to set as approved library.](https://help.figma.com/hc/article_attachments/21359625613207)

If you enable the library by default, Figma will publish the library to the organization and modify the permissions on the file for you.

**Note**: You can update this setting at any time. Changing the setting does not affect anyone’s ability to manually access the library. If you want to remove access to a library, you can [unpublish](https://help.figma.com/hc/en-us/articles/360039236853-Unpublish-a-library) it.

## Set a default variable mode for a library

Enterprise

If a library contains a [variable collection](https://help.figma.com/hc/en-us/articles/14506821864087.html#h_01H9V3QSVH2T1EYNXP7RNXZ8MV) with at least two [modes](https://help.figma.com/hc/en-us/articles/15343816063383), you can also set a [default mode](https://help.figma.com/hc/en-us/articles/15343816063383.html#Default_mode) for the library.

If you're on the Enterprise plan, you can override the library's default mode by selecting a default mode at the team-level or at the workspace-level.

For example, you might have a variable collection that contains spacing values for different screen sizes. The variable collection might have three modes: Desktop, Tablet, and Mobile. If your workspace is dedicated to mobile apps, you could set the default mode to Mobile. When someone creates a new file in the workspace, the page-level default mode is set to Mobile and applies to all variables used on the page. People can always switch to another mode if they need to.

Team level Workspace level

Before you start, make sure the library is published with at least two modes.

To set a default mode on a library in a team:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), open the team for which you wish to set a default mode.
2. Click the  next to the team name and select **View settings**.
3. From the **Shared** section, click **View team's libraries**.
4. Find the library you want to use and select it.
5. Make sure the **Enabled by default** dropdown is set to **All files** or **Design files**.
6. From the **Default mode** column, choose a mode.

Before you start, make sure the library is published with at least two modes.

To set a default mode on a library for a workspace:

1. From the file browser:
   - Organization admin: Go to  **Admin** >  **Resources** > **Libraries**.
   - Workspace admin: Go to  **Admin** > [Your workspace] > **Libraries**.
2. Find the library you want to use and select it. If the library has not been enabled on any workspaces by default, be sure to remove any **Added by default** search filters.
3. From the **Manage this library** modal, find and select the workspace for which you wish to set a default mode.
4. In the **Enable this library by default** section, make sure the library is turned on for **Design files**.
5. From the **Manage default modes** section, choose a mode.
