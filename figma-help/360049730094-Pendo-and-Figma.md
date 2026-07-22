---
기술지원명: Pendo and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Pendo and Figma
출처링크: https://help.figma.com/hc/en-us/articles/360049730094-Pendo-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

[Pendo Guidance in-app messaging](https://www.pendo.io/product/guidance/) campaigns allow you to tailor messaging to specific segments of users to ensure they’re using the features most beneficial to them.

They are also a great tool to capture user feedback on new features and proposed enhancements.

Embed a live view of a public Figma file in any Pendo Guide to:

- Get input early in the development process to ensure you're solving the right customer concern.
- Get feedback on prototypes from your power users, segmented by feature usage.
- Get higher response rates and more precise feedback when customers are active in your app.
- Reduce churn by keeping your customers in the loop on the latest feature enhancements being planned.

Note: The Figma integration is currently only available for use with [Pendo Guidance](https://www.pendo.io/product/guidance/).

# Embed a Figma file in a Pendo Guide

You can embed any file or prototype, regardless of the file's [link sharing settings](https://help.figma.com/hc/en-us/articles/360040531773). Your app visitors can [interact with Figma Live Embeds](https://help.figma.com/hc/en-us/articles/360051741274) based on:

- Their [Team](https://help.figma.com/hc/en-us/articles/360039970673) or [Organization permissions](https://help.figma.com/hc/en-us/articles/360039960434)
- The file's [link sharing permissions](https://help.figma.com/hc/en-us/articles/360040531773-Share-Files-with-anyone-using-Link-Sharing#Update_Link_Sharing)

When using embeds in Pendo Guides, Pendo recommends using public files so any visitor can interact with them.

## In Figma

1. Open the file you want to embed in a Pendo Guide.
2. To link to a specific frame in the Figma file, select the frame you'd like to embed.
3. Click the **Share** button in the toolbar.
4. Update your [Link Sharing permissions](https://help.figma.com/hc/en-us/articles/360040531773-Share-Files-with-anyone-using-Link-Sharing#Update_Link_Sharing) to determine who can interact with the embed (Optional).
5. Click **Get Embed Code**.
6. Click **Copy** to add the public embed code to your clipboard.  
   ![Share modal in the file Editor and Get Embed Code modal where code can be copied](https://help.figma.com/hc/article_attachments/360075783054)

## In Pendo

Add Figma to an existing Guide or [create a new Guide](https://support.pendo.io/hc/en-us/articles/360032204111-Create-a-Guide). You can only add one Figma embed to each Guide.

1. Go to the **Guides** section in Pendo.
2. Click the **+ Create Guide** button in the top-right corner.  
   ![Guides section of Pendo with Create Guide button in top-right corner](https://help.figma.com/hc/article_attachments/360075783594)
3. As an example, select the **How Can We Improve? Open Text Poll** template.
4. Pendo will ask you to give your Guide a name. Click the **Manage in my app** button.
5. Enter the URL for your app in the field provided and click **Launch Designer**.
6. Click the blue + **plus icon** above the text box to add [Building Blocks](https://support.pendo.io/hc/en-us/articles/360032204051-Building-Blocks) to the Guide.  
   ![Blue plus icon in gGuide template for adding Building Blocks](https://help.figma.com/hc/article_attachments/360076907393)
7. In the **Advanced** section, select **Code Block**.
8. Paste your Figma embed code in the **HTML** tab. You may need to adjust the **width** and **height** in the code to fit your Guide. Click **Done** to apply.
9. Add any other [Building Blocks](Building Blocks) to the Guide (optional). Use the [Activation functionality](https://support.pendo.io/hc/en-us/articles/360031864692-Guide-Activation-Options) to choose where your guide is displayed.
10. When you’re finished editing the Guide click **Save** in the menu bar. Click **Exit** to return to Pendo.

## Publish the Guide

Now you can publish the Guide to a segment of your users. You can choose an existing segment, or [create a new one](https://support.pendo.io/hc/en-us/articles/360031862532-Segments).

1. In the **Segment** section, click **Edit** to choose a Pendo segment.
2. Select an existing segment, or create a new one to view the Guide.
3. Update the status of the Guide from **Draft** to **Public**. This will publish the Guide.
4. Pendo will now present the Figma prototype to your target segment. Users can enter their message in the field provided and click **Submit Feedback** to send.

# Remove a Figma embed

To remove an embedded Figma file from your Pendo Guide:

- Edit the Guide and remove the code block for the Figma embed.
- [Delete the entire Guide](https://support.pendo.io/hc/en-us/articles/360038655211).
