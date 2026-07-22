---
기술지원명: Publish classic plugins to the Figma Community
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Publish classic plugins to the Figma Community
출처링크: https://help.figma.com/hc/en-us/articles/360042293394-Publish-classic-plugins-to-the-Figma-Community
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

You must be an approved creator to publish paid plugins to the Community. Learn more about [selling resources on Community](https://help.figma.com/hc/en-us/articles/12067637274519).

You must use the Figma desktop app on macOS or Windows to develop plugins. [Download the Figma Desktop app](https://www.figma.com/downloads/).

**This article covers just one step in the classic plugin development process**. Find everything you'll need to make plugins for Figma's products on the [Figma Developers site](https://www.figma.com/plugin-docs/intro/).

When you're ready to share your classic plugin you can submit your plugin to the Figma Community. This allows other users to install and run your plugins.

You'll need to do the following before you can publish or update a plugin:

- [Download the Figma Desktop app](https://www.figma.com/downloads/)
- [Create a plugin for development](https://help.figma.com/hc/en-us/articles/360042786733)
- [Enable two-factor authentication](https://help.figma.com/hc/en-us/articles/360039817634)

## Before you publish

### Plugin review process

Before Figma lists a plugin in the Figma Community, it needs to go through our review process. Figma doesn't review any plugins you choose to share privately within an organization. [Learn more about Figma's Plugin Review Guidelines](https://help.figma.com/hc/en-us/articles/360039958914).

When you first submit a plugin for review, Figma will move the plugin to the **Published** section with an **In review** badge.

Figma will contact you via your Figma account email to notify you of our decision. Our goal is to be thoughtful and reasonably prompt in our review. Approval times vary depending on current volume and the team’s availability.

Once approved, Figma will add a **Published** badge next to your plugin. If Figma rejects your plugin, you can address any feedback and submit again.

**Noticed a mistake?** You can still push updates to your plugin during the review process. [Learn how to manage plugins as a developer](https://help.figma.com/hc/en-us/articles/360042293714).

## About publishing paid plugins

Creators who meet our eligibility requirements can apply to sell plugins on Community. Learn more about [selling resources on Community](https://help.figma.com/hc/en-us/articles/12067637274519).

When publishing a paid plugin, keep in mind:

- The creator who first publishes the plugin will be the designated payee. Once the designated payee is set, it cannot be changed.
- You can choose to publish the plugin using one-time payments or a monthly subscription. This cannot be changed after publishing.
- You can choose to offer a yearly discount (between 1 and 95%) for plugins published using a subscription. Users who purchase a yearly subscription to the plugin are locked into the price set at time of purchase for one year. You can toggle this setting as often as needed. This allows you to offer discounts at different times throughout the year.
- Plugins published with a subscription come with a 7 day free trial by default. You can customize the free trial period for paid plugins so users can try your plugin before they purchase it. For more information see the [Payments API documentation](https://figma.com/plugin-docs/requiring-payment).
- After a plugin has been published as paid, it cannot be converted to free at a later date.
- Paid plugins cannot be unpublished but may be delisted. Learn more about [delisted paid resources](https://help.figma.com/hc/en-us/articles/12843697930519).

Note: After you are approved to sell on Community, you must activate your [Stripe account](https://help.figma.com/hc/en-us/articles/12730712101783) before you can publish paid resources.

## Publish your plugin

When you're ready to share your plugin with the Figma Community, you can submit it for review. You can only submit plugins from the [Figma desktop app](https://help.figma.com/hc/en-us/articles/360039823654).

Note: Licenses for published plugins vary depending on if the plugin is free or paid. Learn more about the [Figma Community copyright and licensing](https://help.figma.com/hc/en-us/articles/360042296374).

Warning! Any attempts to exploit the Figma Plugin API will result in immediate removal. This will also ban you from publishing plugins in the future.

This includes but is not limited to: Providing false information, plagiarism, deceitful manipulation of user files, and theft of data.

![Publishing modal in Figma showing steps to describe a plugin, including name, tagline, description, and category.](https://help.figma.com/hc/article_attachments/34104199344919)

To publish a plugin to the Figma Community:

1. Create or open a file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Plugins** > **Manage plugins**.
3. Click  next to the plugin and select **Publish.**
4. On the **Describe your resource**page of the **Publish plugin** modal:
   - Enter a name for your plugin
   - Add a short tagline that describes the plugin
   - Provide a description that describes what your plugin does and the features it provides
   - Select a category, such as **Design tools** or **Software development**.
5. On the **Choose some images** page of the **Publish plugin** modal:
   - Set an icon (recommended size 128 x 128px)
   - Set an image or video as the thumbnail (recommended size 1920 x 1080px)
   - (Optional) Include a playground file where people can try your plugin
   - (Optional) Add up to nine images and videos to the carousel for your plugin
6. (Optional) On the **Data security** page of the **Publish plugin** modal, complete the security disclosure form for your plugin. The [security disclosure](https://help.figma.com/hc/en-us/articles/16354660649495) is a set of questions to help identify the data security practices of your plugin. Your answers are reviewed by Figma.

   Note: Review and approval may take up to two weeks. When the disclosure form is approved by Figma, your answers are visible to logged-in users who view the plugin's listing in the Figma Community.
7. On the **Add the final details** page of the **Publish plugin** modal:
   - (Organization and Enterprise plans only) Choose where to publish the plugin using the **Publish to** setting:
     - Select **Organization** to share the plugin privately within your organization
     - Select **Community** to publish the plugin and share it with to the Figma Community
   - Choose whether to publish the plugin as yourself, one of your teams, or your organization
   - Add a support contact
   - Review your plugin's network access. Your plugin’s network access is indicated by one of the following labels:

     - **Unknown network access:** Network access isn’t defined in your plugin’s manifest.json.
     - **Unrestricted network access:** Your plugin can access any domain.
     - **Restricted network access:** Your plugin can access only a specific set of domains.
     - **No access to network:** Your plugin cannot access any domains.

     Click the label to get additional details. If your plugin is labeled **Unknown network access**, you can [specify network access](https://www.figma.com/plugin-docs/making-network-requests) in your [plugin manifest](https://www.figma.com/plugin-docs/manifest) to change the label.
   - (Optional) Add additional contributors
   - (Optional) Allow or disallow comments from Community members
   - (Optional) If you are approved to sell on the Community and have activated your Stripe account, click **Sell this resource on Community** to make it a paid plugin. Keep in mind:

     - You must provide a price
     - Plugins can be sold as one-time payments or subscription with a minimum price of $2.00.
     - Prices are in USD and must be whole numbers.
     - You can change the price for plugins using one-time payments at any time. When the price of a subscription is updated, it can take up to one hour for the new price to display on the Community.
     - The price for plugins using monthly subscriptions may only be increased once every 30 days and cannot be increased more than 50% at a time.
     - For plugins sold using a subscription, you can choose to offer a yearly subscription at a discount. To do this, enable the **Give yearly discount** toggle and enter a percentage between 1 and 95. You can toggle this setting as often as needed. Existing yearly subscriptions will continue even if the **Give yearly discount** toggle is disabled.

     Note: The Pricing settings are disabled if you attempt to publish a paid plugin that is in a team or organization. Move the plugin to your drafts to enable the Pricing settings.
8. Click **Publish** to submit your plugin for review.

## Publish an update

Publish updates to your plugin if you've made changes to the code or fixed a bug. You can also edit the details of your plugin page at any time, without publishing a new update. [Learn how to publish updates to your plugins](https://help.figma.com/hc/en-us/articles/360042293714).

## Share your plugin

Figma gives your published plugin its own listing in the [Figma Community](http://figma.com/community), this allows other Figma users to [find and install](https://help.figma.com/hc/en-us/articles/360040450413) your plugins.

Every plugin has a unique URL which you can copy and share with others. Find the plugin URL in the **Share** section of your plugin listing. It should look something like this: `https://www.figma.com/community/plugin/uniqueidentifier/name`

If you have more than one plugin, you may want to share your creator profile instead. [Learn more about Community profiles](https://help.figma.com/hc/en-us/articles/360038510833).
