---
기술지원명: Manage widgets as a developer
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Manage widgets as a developer
출처링크: https://help.figma.com/hc/en-us/articles/4410592119703-Manage-widgets-as-a-developer
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

You must use the Figma desktop app to create and publish widgets. The Figma desktop app is only available for Mac and Windows. [Download the Figma desktop app →](https://www.figma.com/downloads/)

This article covers how to create a new widget in FigJam, and is only one step in the widget development process.

The widget development process:

1. [Setup your development environment →](https://www.figma.com/widget-docs/setup-guide/)
2. [Create a widget for development →](https://help.figma.com/hc/en-us/articles/4410676552727)
3. [Publish widgets to the Figma Community →](https://help.figma.com/hc/en-us/articles/4410337103639/)
4. **Manage widgets as a developer (Current article)**

Check out our [Widget Developer docs](https://www.figma.com/widget-docs/intro/) for a complete guide on making widgets for FigJam.

## Update a widget

### Publish a new release

Note

Only the original widget publisher can publish updates to a widget. You can still list other contributors to the widget as creators, but they won't be able to publish any changes.

Once Figma approves your widget, you no longer need to submit your widget for further review. This means you can publish any updates immediately.

When you publish an update, Figma will update the widget for every user. Users who have already installed your widget will only have access to the latest version of your widget.

It's not possible for users to revert to a previous version of the widget. If you need to roll back any changes, you can republish an earlier version of the widget.

The process for submitting an update is the same as the original publishing process. You can update any information about your widget, including the **name**, **description**, **tags**, **creators**, and any **artwork**.

1. Open a file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Widgets** > **Manage widgets**.
3. Click  next to the widget you'd like to update and select **Publish new version**.

   **Note:** If you don't see **Publish new version** in the list of options, select **Locate local version**. In the file selector, go to the directory that contains the version of your widget that you want to publish. Then, select the manifest.json file for your widget and click **Okay**. You should now see **Publish new version** in the list of options.
4. Use the **Publish widget** modal to update widget information as needed.
   - (Optional) Update the security self-assessment form on the **Data security** page. If you've previously submitted the self-assessment and the form has not yet been approved, a banner appears in the form to identify that the widget is still under review.
   - (Optional) On the **Add final details** page, enter details about the changes to your widget in the **Release notes** box.
   - Update any other fields as needed.
5. Click **Publish** to complete the process. Figma will update the widget for everyone that has it installed.

### Edit a Community page

Your widget's Community page helps users understand what your widget does and allows them to install it for use. Creators, contributors, and publishers of a widget can edit the details of the widget's page at any time without having to publish an update.

1. Open the widget's Community page.
2. In the upper-right corner of the page, click **Manage resource** > **Edit this page**.
3. In the **Publish widget** modal, update the desired fields, then click **Publish** when you're finished.

## Manage permissions

### Invite additional publishers

Once your widget is published to the Figma Community, you can invite others to help publish updates to your widget. [Learn how to invite additional publishers →](https://help.figma.com/hc/en-us/articles/360041423614#multiple-publishers)

### Transfer ownership of private organization widgets

Owners of private organization widgets transfer ownership to any one who has permission to publish a resource. Organization admins can also transfer ownership of private widgets to another organization member.

Note: You cannot transfer ownership of widgets published outside of an organization.

1. Open a Figma Design or FigJam file on the Figma desktop app.
2. Open the permissions modal:
   1. Click  and select the **Widgets** tab.
   2. Open the dropdown menu and select **Development.**
   3. Click  next to your widget and select **Manage permissions.**
3. Click the dropdown next to a publisher’s name.
4. Select **Owner.** The former owner will have their permissions changed to **Can update.**

## Remove a widget

If you're a developer of a widget, you can remove a widget at any stage of the development process.

### Published

If your widget is published to the Figma Community, unpublishing your widget will remove it for anyone who has installed it. Users who've installed your widget won't receive a notification if it's been unpublished.

Note: Paid widgets cannot be unpublished but can be delisted. Learn more about [delisted paid resources →](https://help.figma.com/hc/en-us/articles/12843697930519)

We recommend warning your users of your plans to unpublish the widget. For example, you can add a note to the widget description or your personal website with the date you will unpublish the widget.

**Unpublish from a Community page**

1. Open the widget's Community page.
2. In the upper-right corner of the page, click **Manage resource** > **Unpublish**.
3. In the **Unpublish widget** modal, click **Unpublish**.

**Unpublish while in a file**

1. Open a Figma Design or FigJam file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Widgets** > **Manage widgets**.
3. Click  next to the widget you want to unpublish and select **Unpublish** from the options.

The widget will be removed from the Figma Community and users will no longer be able to use the widget or view the listing. The widget will remain in development on your account.

Caution

When removing a widget from the Community, likes and installs will be retained, but any details—such as title, tagline, description, and so on—will be lost.

### In development

If you decide to cease development of a widget, or want to start from scratch, you can remove the widget. This will delete the widget from Figma, but you can still access the manifest from your computer.

1. Open a Figma Design or FigJam file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Widgets** > **Manage widgets**.
3. Click  next to the widget you want to remove and select **Remove** from the options.

Caution

It's not possible to restore a deleted widget. Deleting a widget will also remove any likes and installs you have acquired, even if you publish the same widget in the future.

## Provide support

Figma does not provide support for third-party applications. As the widget's developer, it's your responsibility to assist your widget users with technical issues.

You need to add a **Support** contact when you submit your widget for approval. This can be an email address users can contact or a link to a website or help center.

[Back: Publish widgets](https://help.figma.com/hc/en-us/articles/4410337103639)
