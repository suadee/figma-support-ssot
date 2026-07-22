---
기술지원명: Manage classic plugins as a developer
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Manage classic plugins as a developer
출처링크: https://help.figma.com/hc/en-us/articles/360042293714-Manage-classic-plugins-as-a-developer
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

You must use Figma's desktop app to develop plugins. [Download the Figma Desktop app for Mac or Windows →](https://www.figma.com/downloads/)

Classic plugins are plugins that you code in your own development environment and are different from generative plugins. This article covers managing classic plugins. [Learn more about other plugins](https://help.figma.com/hc/en-us/articles/41407987481879).

Figma built the [Plugin API](https://www.figma.com/plugin-docs/intro/) around a set of fixed, controlled endpoints. This ensures your plugins won't break as Figma releases updates and new features.

If there is something wrong with the Plugin API itself, or you have questions about the development process or a specific endpoint, please [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new).

To ask questions about how to use the API, and get resources and help from fellow plugin developers, join our [community-driven Discord server](https://discord.gg/xzQhe2Vcvx).

## Update a plugin

### Publish a new release

Once Figma approves your plugin, you don't need to submit your plugin for further review. This means you can publish any updates immediately.

If you've updated your plugin's code and are ready to release the new version, you can publish an update. Doing this will update the plugin for every user. Users who have already installed your plugin will only have access to the latest version of your plugin.

It's not possible for users to revert to a previous version of the plugin. If you need to roll back any changes, you can republish an earlier version of the plugin.

The process for submitting an update is the same as the publishing process. You can update any information about your plugin, including the name, description, tags, and any artwork.

1. Open a file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Plugins** > **Manage plugins**.
3. Click  next to the plugin you'd like to update and select **Publish new version**.

   **Note:** If you don't see **Publish new version** in the list of options, select **Locate local version**. In the file selector, go to the directory that contains the version of your plugin that you want to publish. Then, select the manifest.json file for your plugin and click **Okay**. You should now see **Publish new version** in the list of options.
4. Use the **Publish plugin** modal to update plugin information as needed.
   - (Optional) Update the security self-assessment form on the **Data security** page. If you've previously submitted the self-assessment and the form has not yet been approved, a banner appears in the form to identify that the plugin is still under review.
   - (Optional) On the **Add final details** page, enter details about the changes to your plugin in the **Release notes** box.
   - Update any other fields as needed.
5. Click **Publish** to complete the process. Figma will update the plugin for everyone that has it installed.

### Edit a Community page

Your plugin's Community page helps users understand what your plugin does and allows them to install it for use. Creators, contributors, and publishers of a plugin can edit the details of the plugin's page at any time, without having to publish an update.

1. Open the plugin's Community page.
2. In the upper-right corner of the page, click **Manage resource** > **Edit this page**.
3. In the **Publish plugin** modal, update the desired fields, then click **Publish** when you're finished.

## Manage permissions

### Invite additional publishers

Once your plugin is published to the Figma Community, you can invite others to help publish updates to your plugin. [Learn how to invite additional publishers →](https://help.figma.com/hc/en-us/articles/360041423614#multiple-publishers)

### Transfer ownership or private organization plugins

Owners of private organization plugins can transfer ownership to any one who has permission to publish a resource. Organization admins can also transfer ownership of private plugins to another organization member.

Note: You cannot transfer ownership of plugins published outside of an organization.

1. Open a file on the Figma desktop app.
2. Open the permissions modal:
   1. Click  and select the **Plugins** tab.
   2. Open the

       dropdown menu and select **Development.**
   3. Click  next to your plugin and select **Manage permissions.**
3. Click the dropdown next to a publisher’s name.
4. Select **Owner.** The former owner will have their permissions changed to **Can update.**

## Remove a plugin

If you're a developer of a Figma plugin, you can remove a plugin at any stage of the development process.

### Published

If your plugin is published to the Figma Community, unpublishing your plugin will remove it for anyone who has installed it. Users who've installed your plugin won't receive a notification if it's been unpublished.

Note: Paid plugins cannot be unpublished but can be delisted. Learn more about [delisted paid resources →](https://help.figma.com/hc/en-us/articles/12843697930519)

We recommend warning your users of your plans to unpublish the plugin. For example, you can add a note to the plugin description or your personal website with the date you will unpublish the plugin.

**Unpublish from a Community page**

1. Open the plugin's Community page.
2. In the upper-right corner of the page, click **Manage resource** > **Unpublish**.
3. In the **Unpublish plugin** modal, click **Unpublish**.

**Unpublish while in a file**

1. Open a file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Plugins** > **Manage plugins**.
3. Click  next to the plugin you want to unpublish and select **Unpublish** from the options.

The plugin will be removed from the Figma Community and users will no longer be able to use the plugin or view the listing. The plugin will remain in development on your account.

Caution

When removing a plugin from the Community, likes and installs will be retained, but any details—such as title, tagline, description, and so on—will be lost.

### In development

If you decide to cease development of a plugin, or want to start from scratch, you can remove the plugin. This will delete the plugin from Figma, but you can still access the manifest from your computer.

1. Open a file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Plugins** > **Manage plugins**.
3. Open the

    dropdown menu and select **Development.**
4. Click  next to the plugin you want to remove and select **Remove** from the options.

Caution

It's not possible to restore a deleted plugin. Deleting a plugin will also remove any likes and installs you have acquired, even if you publish the same plugin in the future.

## Provide support

Figma does not provide support for third-party applications. As the plugin's developer, it's your responsibility to assist your plugin's users with technical issues.

You need to add a Support contact when you submit your plugin for approval. This can be an email address users can contact, or a link to a website or help center.
