---
기술지원명: Publish widgets to the Figma Community
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Publish widgets to the Figma Community
출처링크: https://help.figma.com/hc/en-us/articles/4410337103639-Publish-widgets-to-the-Figma-Community
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

You must use the [Figma desktop app](https://www.figma.com/downloads/) to create and publish widgets

You must be an [approved creator](https://help.figma.com/hc/en-us/articles/12067637274519) to publish paid widgets to the Community

When you’re ready to share your widget with others, you can publish it to the Figma Community. This allows others to insert your widget into their Figma Design and FigJam files.

Note: You must have [two-factor authentication](https://help.figma.com/hc/en-us/articles/360039817634-Enable-two-factor-authentication-2FA-) enabled to publish widgets. You won't need to use two-factor authentication if you sign in to Figma via SAML SSO or Google SSO.

## Before you publish

### Widget review process

Every widget must go through a review process the first time it gets published to the Figma Community. Once the widget is approved, you won’t need to go through the process again for future updates. Learn more about Figma's [plugin and widget review guidelines](https://help.figma.com/hc/en-us/articles/360039958914).

We will contact you via your Figma account email to notify you of our decision.
The review process typically takes between 5-10 business days. If we reject
your widget, you can address any feedback and submit again. You can still
publish updates to your widget during the review process.

### About publishing paid widgets

If you’re an approved creator, you can publish your widgets as paid and sell them directly from the Community. Learn more about [selling resources on the Community](https://help.figma.com/hc/en-us/articles/12067637274519).

When publishing a paid widget, keep in mind:

- The creator who first publishes the widget will be the designated payee. Once the designated payee is set, it cannot be changed.
- You can customize a free trial period for paid widgets so users can try your widget before they purchase it. For more information see the [Payments API documentation](https://figma.com/plugin-docs/requiring-payment).
- After a widget has been published as paid, it cannot be converted to free at a later date.
- Paid widgets cannot be unpublished but may be delisted. Learn more about [delisted widgets](https://help.figma.com/hc/en-us/articles/12843697930519).

Important: After you are approved to sell on Community, you must activate your [Stripe account](https://help.figma.com/hc/en-us/articles/12730712101783) before you can publish paid resources.

## Publish your widget

Each widget goes through the same publishing flow the first time it is published
and every time it gets updated. You can only publish widgets from the Figma
desktop app.

You can only publish widgets from the Figma desktop app.

Warning: Any attempts to exploit the Figma Widget API will result in immediate removal. This will also ban you from publishing widgets in the future.

This includes but is not limited to: Providing false information, plagiarism, deceitful manipulation of user files, and theft of data.

![Publish widget modal in Figma showing fields for name, tagline, description, and category selection during the resource setup process.](https://help.figma.com/hc/article_attachments/34104134650519)

To publish a widget to the Figma Community:

1. Create or open a file on the Figma desktop app.
2. Click the Figma logo in the upper-left corner, then go to **Widgets** > **Manage widgets**.
3. Click  next to the widget and select **Publish.**
4. On the **Describe your resource**page of the **Publish widget** modal:
   - Enter a name for your widget
   - Add a short tagline that describes the widget
   - Provide a description that describes what your widget does and the features it provides
   - Select a category, such as **Design tools** or **Software development**.
5. On the **Choose some images** page of the **Publish widget** modal:
   - Set an icon (recommended size 128 x 128px)
   - Set an image or video as the thumbnail (recommended size 1920 x 1080px)
   - (Optional) Include a playground file where people can try your widget
   - (Optional) Add up to nine images and videos to the carousel for your widget
6. (Optional) On the **Data security** page of the **Publish widget** modal, complete the security disclosure form for your widget. The [security disclosure](https://help.figma.com/hc/en-us/articles/16354660649495) is a set of questions to help identify the data security practices of your widget. Your answers are reviewed by Figma.

   Note: Review and approval may take up to two weeks. When the disclosure form is approved by Figma, your answers are visible to logged-in users who view the widget's listing in the Figma Community.
7. On the **Add the final details** page of the **Publish widget** modal:
   - (Organization and Enterprise plans only) Choose where to publish the widget using the **Publish to** setting:
     - Select **Organization** to share the widget privately within your organization
     - Select **Community** to publish the widget and share it with to the Figma Community
   - Choose whether to publish the widget as yourself, one of your teams, or your organization
   - Add a support contact
   - Review your widget's network access. Your widget’s network access is indicated by one of the following labels:

     - **Unknown network access:** Network access isn’t defined in your widget’s manifest.json.
     - **Unrestricted network access:** Your widget can access any domain.
     - **Restricted network access:** Your widget can access only a specific set of domains.
     - **No access to network:** Your widget cannot access any domains.

     Click the label to get additional details. If your widget is labeled **Unknown network access**, you can [specify network access](https://developers.figma.com/docs/widgets/making-network-requests/) in your [widget manifest](https://developers.figma.com/docs/widgets/widget-manifest/) to change the label.
   - (Optional) Add additional contributors
   - (Optional) Allow or disallow comments from Community members
   - (Optional) If you are approved to sell on the Community and have activated your Stripe account, click **Sell this resource on Community** to make it a paid widget. Keep in mind:

     - You must provide a price
     - Widgets can be sold as one-time payments or subscription with a minimum price of $2.00.
     - Prices are in USD and must be whole numbers.
     - You can change the price for widgets using one-time payments at any time. When the price of a subscription is updated, it can take up to one hour for the new price to display on the Community.
     - The price for widgets using monthly subscriptions may only be increased once every 30 days and cannot be increased more than 50% at a time.
     - For widgets sold using a subscription, you can choose to offer a yearly subscription at a discount. To do this, enable the **Give yearly discount** toggle and enter a percentage between 1 and 95. You can toggle this setting as often as needed. Existing yearly subscriptions will continue even if the **Give yearly discount** toggle is disabled.

     Note: The Pricing settings are disabled if you attempt to publish a paid widget that is in a team or organization. Move the widget to your drafts to enable the Pricing settings.
8. Click **Publish** to submit your widget for review.

## Publish an update

Publish updates to your widget if you've made changes to the code or fixed a bug. You can also edit the details of your widget page at any time without publishing a new update. [Learn how publish updates to your widget](https://help.figma.com/hc/en-us/articles/4410592119703).

## Share your widget

Published widgets have their own listing in the [Figma Community](http://figma.com/community), which allows other Figma users to find and install them.

Every widget has a unique URL that you can copy and share with others. Find the widget URL in the **Share** section of a widget listing. It will look something like this: `https://www.figma.com/community/widget/uniqueidentifier`

If you have more than one widget, you may want to share your creator profile instead. [Learn more about Community profiles](https://help.figma.com/hc/en-us/articles/360038510833).

Congratulations, you've published a widget! Next, learn how to manage widgets as a developer.

[Back: Create a widget](https://help.figma.com/hc/en-us/articles/4410676552727)[Next: Manage widgets](https://help.figma.com/hc/en-us/articles/4410592119703/)
