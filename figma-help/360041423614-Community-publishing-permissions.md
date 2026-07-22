---
기술지원명: Community publishing permissions
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Community publishing permissions
출처링크: https://help.figma.com/hc/en-us/articles/360041423614-Community-publishing-permissions
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

[Community profiles](https://help.figma.com/hc/en-us/articles/360038510833) showcase files, plugins, and widgets people have created for the Figma Community. You can have a profile as an individual creator, a team, or an organization.

A file’s location, its permissions, and your plan tier are all factors that can determine if you can [publish to a Community profile](https://help.figma.com/hc/en-us/articles/360040035974).

- [View required permissions by profile type ↓](#profiles)
- [View all permissions in a table ↓](#permission-tables)
- [View requirements for being listed as a creator ↓](#creators)

# Publish to profiles

**Note:** If you are a team or organization admin, you may be able to publish to more than one profile. You can select which profile to publish to during the publishing process.

## Personal profiles

Who can publish to a personal profile?

Anyone with a **Figma account** can create a personal profile. You can create one profile per Figma account (email address).

People with `can edit` access to the file can publish that file to their profile.

Starter, Education, or Professional  Organization or Enterprise

You can publish any file you have `can edit` access to. This includes files in your drafts, teams, and shared projects.

You can also publish updates to an existing Community file, as long as you have edit access to the file. This includes publishing changes to the resource's tags or description, and adding or removing creators.

If you have both personal and work accounts, you can [add connected profiles](https://help.figma.com/hc/en-us/articles/4404285788183). This allows you to publish resources from multiple accounts to a single Community profile.

If you're part of an organization, any files or plugins you create in the organization belong to that organization. This means there are limitations on who can publish organization resources.

- By default, it's not possible to publish organization resources to a personal profile. Switch to a non-organization team, or a personal Figma account, to publish resources to your personal profile. Organization admins can also enable publishing to personal profiles for other organization admins by navigating to **Admin** > **Settings** > **Other** and enabling the **Community file publishing** setting.
- Only organization admins can publish resources to an organization's profile. As part of this process, organization admins can [add organization members as creators](https://help.figma.com/hc/en-us/articles/360040035974). To be listed as a creator, you need a Community profile connected to your work account.
- Organization teams can also have their own team Community profiles.  If you're a team admin, you can publish files from that team to the team's profile. Team admins can't publish resources to the organization's main profile.

**Tip:** You can [connect a Community profile to multiple Figma accounts](https://help.figma.com/hc/en-us/articles/4404285788183). If you have both a work and personal account, you can connect them to the same profile.

This allows you to publish files and plugins from Starter and Professional teams outside the organization, and from your personal account. Organization admins can also list you as a creator on organization resources.

If you leave the company, or are removed from the organization, you can disconnect your work account from your profile.

## Team profiles

Who can publish to a team profile?

Only team owners and admins can publish resources to a team profile.

Teams can also have Community profiles. To publish to a team profile, the file must live inside that team. If it is in your drafts or another team, you will need to [move it to the correct team](https://help.figma.com/hc/en-us/articles/360038511573) before you publish it.

As part of the publishing process, team admins can add other contributors as creators. Creators need to have explicit `can view` or `can edit` permissions on the file. [**Learn more about being listed as a creator ↓**](#creator)

Note: Once the file is published to the Community, you won't be able to move it to another team. You can still move the file between projects on the same team.

## Organization profiles

Who can publish to an organization profile?

Only organization admins can publish resources to an organization profile.

If you're an **organization admin**, you can publish files and plugins to the organization's Community profile. To publish a file to the organization's profile, the file must:

- Be located in a team within the organization
- Not be in a member's drafts or a team outside the organization
- Not be in a hidden team
- Not be moved between teams once published

Organization admins can list other contributors as creators when they publish the file. Creators need to have explicit `can view` or `can edit` permissions on the file.

**Note:** Organization teams can also have their own team Community profiles. Only team admins can publish resources to those team profiles. Team admins can't publish resources to the organization's main profile.

# Permission tables

A **file's location** and**permissions** determine if you can [publish to a Community profile](https://help.figma.com/hc/en-us/articles/360040035974). Use the tables below to see which profiles you can publish to.

### Drafts

|  |  |
| --- | --- |
| **File permission** | **Personal profile** |
| Can edit | ✓ |
| Can view | ✕ |

### Professional, Education, or Starter teams

|  |  |  |
| --- | --- | --- |
| **Team permission** | **Team profile** | **Personal profile** |
| Admin | ✓ | ✓ |
| Can edit | ✕ | ✓ |
| Can view | ✕ | ✕ |

### Organization

#### Organization resources

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Account** | **Team permission** | **Organization profile** | **Team profile** | **Personal profile** |
| Admin | Admin | ✓ | ✓ | ✕ |
| Admin | Can edit | ✓ | ✕ | ✕ |
| Admin | Can view | ✕ | ✕ | ✕ |
| Member | Admin | ✕ | ✓ | ✕ |
| Member | Can edit | ✕ | ✕ | ✕ |
| Member | Can view | ✕ | ✕ | ✕ |

#### Teams outside the organization

|  |  |  |  |
| --- | --- | --- | --- |
| **Team permissions** | **Organization profile** | **Team profile** | **Personal profile** |
| Admin | ✕ | ✓ | ✓ |
| Can edit | ✕ | ✕ | ✓ |

# Creator contributions

If you've contributed to other files in the Community, and have ‌permissions on that file, you can also be added to the file as a creator.

Publishers can add any other contributors to the file as creators as part of the publishing process. Creators need to have explicit `can view` or `can edit` permissions on the file itself.

Every who is added as a creator will have the option to accept or decline the request. Figma will send you a notification in your account.

Figma displays accepted creators on the file's Community page, as well as include the file on each individual creator's profile.

If you have published to a team or organization profile, Figma will show the team or organization first, then any individual creators.

Note: If you only have access to the file based on your team permissions, you won't be included in the list of potential creators. If someone is missing from the list of creators, you may need to invite them to the file first.

|  |  |  |
| --- | --- | --- |
| **Team permissions** | **File permission** | **Creator supported** |
| Can edit | - | ✕ |
| Can edit | Can edit | ✓ |
| Can view | - | ✕ |
| Can view | Can view | ✓ |

# Multiple publishers

Once a plugin or widget is published, the owner can invite multiple users to publish the same resource. This is useful when you’re working with a team to build a plugin or widget. Publishers can:

- Invite or remove other publishers
- Publish updates to the resource
- See the resource in their list of development resources in the Figma desktop app,
- Remove themselves as a publisher

Note: Only resource owners can unpublish a resource or change where a resource is published to.

To invite other publishers:

1. Open a Figma Design or FigJam file on the Figma desktop app.
2. Open the permissions modal:
   1. Click  and select the **Plugins** or **Widgets** tab.
   2. Open the dropdown menu and select **Development.**
   3. Click  next to your plugin or widget and select **Manage permissions.**
3. Use the field to invite other publishers.
   - If publishing from an organization file, you’ll be suggested users in your organization.
   - If publishing from any other file, you’ll be suggested anyone involved in the file.
   - If the resource is private to an organization, you can only invite publishers who are members of that organization.
4. Click **Send invite.**

Invitations are sent via email and in-app notification from the bell icon.

Note: If a public Community resource is republished as private to an organization, any publishers who are not members of that organization will be removed.
