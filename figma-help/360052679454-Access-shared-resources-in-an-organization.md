---
기술지원명: Access shared resources in an organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Access shared resources in an organization
출처링크: https://help.figma.com/hc/en-us/articles/360052679454-Access-shared-resources-in-an-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273).

Any organization member  can access resources shared across the entire organization. Guests of the organization can only access resources you invite them to.

Organizations go beyond the team setup you may be used to in a Professional or Starter team. Create unlimited teams in an organization and access them all from the organization in the file browser. Any team you create will have access to all the features of a Professional team, plus some extras.

In addition to that space, members have a personal space for any teams outside the organization. Everything in the organization space is owned by the organization. This includes files from every team in the organization, as well as files in individual's drafts.

In this article, we'll cover accessing shared resources including files, libraries, fonts, and plugins.

**Note:** Everyone in an organization has both an **account type** and a [seat type](https://help.figma.com/hc/en-us/articles/360039960434). These control what resources a person can access in the organization and how they can interact with them.

## Share files

Sharing files in an organization is different than sharing files from a Starter, Education or Professional team. Organizations support seamless collaboration between members, so there are a few ways members can get access to files:

- A member invites them to the file
- They are a member of the team or project
- They open a link to an organization file (link sharing)

**Note:** If you invite someone who's email address doesn't match any of the organization's domains, they will be a [guest](https://help.figma.com/hc/en-us/articles/360039960434#h_5983390f-530a-4286-b0b4-f9ebc6b5b44c) of the organization. Guests can only access the files, projects, and teams to which you invite them. Learn about [inviting guests to organization resources](https://help.figma.com/hc/en-us/articles/4410795216791).

### Invite collaborators to teams

When you are a member of a team, you can access any files and projects within the team. Learn how to [invite members to teams](https://help.figma.com/hc/en-us/articles/360039481034).

### Invite collaborators to files

Invite a collaborator to a file in your organization to give them explicit access to the file. You can view everyone invited to the file in the share modal.

1. Click **Share** in the right sidebar in the file.
2. Enter the member's email in the invitation field
3. Choose whether to give them `can edit` or `can view` permission.
4. Click **Invite** to confirm. They will need to accept the invite to edit the file.

### Share links to files

Every file and prototype in Figma has a unique URL. For example: `http://www.figma.com/file/ABCDEFGHIJKL/file-name`

You can use this link to share designs and prototypes with members of your organization. This includes organization members who aren't invited to that specific file or team

Use the audience settings to define who can open the file, and whether they have view or edit access. Learn more about [sharing links in an organization](https://help.figma.com/hc/en-us/articles/360040044834).

Note: Organization admins can [disable public link sharing for the organization](https://help.figma.com/hc/en-us/articles/360039829474#Other). This removes the **Anyone** option from the audience settings and prevents anyone outside the organization accessing files via link sharing.

## Libraries

Styles and components live in the files you created them in. To access and reuse these in other files, you can publish them to a library. This allows you to maintain a consistent brand and style, at scale.

Members of an organization can choose to publish files to a specific team or share it across the entire organization. Learn how to [share libraries in an organization](https://help.figma.com/hc/en-us/articles/360040529593).

- Choose which libraries you want to make available to the organization.
- Organization admins can choose which libraries are available to members in organization files.
- Guests can only access libraries you invite them to.
- Admins can also remove libraries to hide or remove them for organization members.

**Tip:** See how members of your organization are using published libraries, components, styles, and variables with library analytics. Learn how to [explore and understand library analytics](https://help.figma.com/hc/en-us/articles/360039238353).

## Fonts

Figma gives you access to an extensive catalog of [Google Web Fonts](https://fonts.google.com/). If you would like to use extra fonts in your Figma designs, you can use fonts installed on your computer.

- If you're using the [Figma Desktop app](https://help.figma.com/hc/en-us/articles/360039823654), any fonts installed on your computer will already be available to you. You can find these alongside the Google Web Fonts in the [font picker](https://help.figma.com/hc/en-us/articles/360041308034).
- If you're using Figma in the browser, you will need to [install the Figma Font Helper application](https://help.figma.com/hc/en-us/articles/360039956894). This allows you to access any fonts you have installed on your computer when using Figma in the browser.

Organizations can also upload and share custom fonts. This allows members to share fonts in a specific team, or across the entire organization.

- Only organization admins can upload fonts to the entire organization.
- Only team admins can upload fonts to a specific team.

[Learn more about uploading fonts to an organization.](https://help.figma.com/hc/en-us/articles/360039956774)

## Plugins

In an organization, you have both an [Organization and Personal space](https://help.figma.com/hc/en-us/articles/360039819074). Figma links any plugins you install to your entire account.

Organization members can access both public and private plugins in an Organization. This allows other members of the Organization to use internal plugins, as well as access plugins from the Figma Community.

- [Browse and install plugins in the Figma Community](https://help.figma.com/hc/en-us/articles/360040450413). Figma will add any plugins you install to your account so can access them within both the organization and any Starter or Professional teams outside of it.
- If the [Approved plugin list is enabled](https://help.figma.com/hc/en-us/articles/360039958894#Approve_plugins), you can only use public plugins on this list within the organization space. You can use plugins outside of that list in teams outside the organization.
- View and install private organization [plugins that are private to your organization](#h_01EWKBJM81QDMRX6A8F8X6TS6H).
- View and [manage your installed plugins](https://help.figma.com/hc/en-us/articles/360043031473) under your **Account** > **Plugins**.

View private organization plugins

To find and install plugins that are private to your organization:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **All teams** or **All workspaces**.
2. Select the **Plugins** header at the top of the page to view any plugins that are private to your organization.
3. Click the **↓ Install** button to add the plugin to your account.

Looking to develop and publish plugins? Members of an organization can create and publish **private** plugins, making them available only to other organization members. Learn how to [create private plugins for your organization.](https://help.figma.com/hc/en-us/articles/4404228629655)

## Make kits

[Make kits](https://help.figma.com/hc/en-us/articles/39241689698839) are customizable bundles containing npm packages, Figma Design library styles, and guidelines. Make kits can be published to your organization so your team can use them in their Figma Make projects to generate designs and prototypes that stay truer to how your product looks and functions.

Admins of an organization can surface Make kits to the entire organization so teams know which kit are the best ones to work with. Admins can:

- **Approve a Make kit**: The kit gets pinned to the top of the list when teammates are choosing from a list of kits to Make kits to use. Approved Make kits lets everyone in the organization know that the kit has been recommended by an admin and helps them feel more comfortable choosing which kit to use in their Make projects.
- **Add a Make kit by default**: Enabling a Make kit by default adds the kit to any new Make files automatically without having to manually search for and add the kit.

[Learn more about managing Make kits for your organization.](https://help.figma.com/hc/en-us/articles/39313426360087)
