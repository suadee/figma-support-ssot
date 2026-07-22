---
기술지원명: Publish apps to the Figma Community
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Publish apps to the Figma Community
출처링크: https://help.figma.com/hc/en-us/articles/35074258201495-Publish-apps-to-the-Figma-Community
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

**This article covers just the step of publishing an OAuth app to the Figma Community.** Find everything you'll need to create and configure OAuth apps on the [Figma Developers site](https://developers.figma.com/docs/rest-api/authentication/#oauth-apps).

If you have a public app, integration, or platform that uses a Figma OAuth app to authenticate users, you can publish the app in the Figma Community. Publishing helps users of Figma discover your app and learn more about it.

When you publish your app, Figma will review the listing and test the app's functionality. Read the [App review guidelines](https://help.figma.com/hc/en-us/articles/34963247780247) to understand qualifying and disqualifying criteria for your app.

### Publish an app to the community

When you publish an app to the Figma Community, you'll need to provide several things:

- For your app's community listing:
  - A logo
  - A tagline (100 characters or less)
  - A description of the app
  - A landing page URL
  - A support contact (email or URL)
  - A cover image (recommended size: 1920 x 1080px)
- Testing instructions for how Figma can test your app during the review process

Optionally, you may also want to include:

- A set of up to 9 images for the carousel that appears on your app's community listing
- Release notes that describe the functionality of your app

To configure and publish your OAuth app, you go to [figma.com/developers/apps](https://www.figma.com/developers/apps) and click an OAuth app to go through the configuration flow. During the flow, you'll set up your app's community listing. At the end of the flow, you'll submit your app and community listing for review by Figma. Once approved, your app will appear in the Figma Community.

**Note:** To publish your OAuth app to the Figma Community, it must be a public app. You can start with an existing public OAuth app or use a draft OAuth app. For a draft OAuth app, you'll need to make it public during the configuration flow.

You can close the configuration flow at any time and your OAuth app will remain in draft if it hasn’t been previously published.

To publish a OAuth app to the Figma Community:

1. In the list of your OAuth apps at [figma.com/developers/apps](https://www.figma.com/developers/apps), click the OAuth app that you want to publish to the Figma Community.
2. On the left side of the configuration modal, click **Publish**.
3. On the **Publish** page:
   1. If you're publishing a draft OAuth app, select **Public**.
   2. Select **List this app on community**.
   3. Click **Next**.
4. On the **Set up your listing** page:
   1. Select the author that will appear for your app. You can select either yourself, or the team or organization your OAuth app is assigned to.
   2. Enter a tagline.
   3. Enter a description of your app. You can use markdown in the description, and text formatting controls are provided.
   4. Enter a landing page URL for your app. The landing page should go to installation instructions, documentation, or your app's homepage.
   5. Enter a support contact. This can be an email address or a URL to a support page.
   6. Select relevant tags for your app. You can also pick from the list of tags recommended by Figma.
   7. Optionally, enable or disable commenting on your community listing.
   8. Optionally, add release notes that describe functionality and changes to your app.
   9. Click **Next**.
5. On the **Choose some images** page:
   1. Set a cover image for your app.
   2. Optionally, add up to nine images of your app to the carousel for your app's Community page.
   3. Click **Next**.
6. On the **Review scopes** page:
   1. Review the scopes that you selected for your OAuth app on the **OAuth scopes** page.
   2. For each scope, describe why your app needs access to that scope.
7. On the **Testing instructions** page:
   1. Enter all the steps that are required for in order for Figma's OAuth app reviewer to successfully test your application and understand its features.
   2. Optionally, add a link to a testing video.
   3. If necessary for working with your application, provide a free trial URL or login credentials that the OAuth app reviewer can use to access your application.
8. On the **Review and submit** page, read the summary of what to expect during the review process. You should also read the [Figma Community Apps Review Guidelines](https://help.figma.com/hc/en-us/articles/34963247780247) to ensure your application meets the requirements.

   When you’re ready, click the **I certify…** checkbox, and then **Submit for review**.

   You’re done! When your OAuth app and community listing have been reviewed and approved, your app will be added to the Figma Community.
