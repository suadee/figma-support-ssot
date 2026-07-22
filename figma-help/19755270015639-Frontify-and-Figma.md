---
기술지원명: Frontify and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Frontify and Figma
출처링크: https://help.figma.com/hc/en-us/articles/19755270015639-Frontify-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

[Frontify](https://www.frontify.com/en/) is a brand management platform that helps teams centralize brand guidelines, templates, and assets, and foster creative collaboration.

Frontify has two integrations to connect your Figma Design files and Frontify brand systems:

- [Frontify plugin](https://www.figma.com/community/plugin/893898815372491269/frontify): Access and add brand elements stored in Frontify—such as media, colors, or fonts—directly in Figma Design files
- [The Figma Content Block](https://help.frontify.com/en/articles/6588621-figma-content-block): Add Figma assets to Guideline pages in Frontify

Before you start, you will need a paid Frontify plan that includes the projects feature, and have editor rights in at least one Frontify project.

## Add Frontify assets to Figma

The Frontify plugin allows you to access and use brand colors, typography, local styles, media library, and icon and logo libraries directly in Figma Design files.

1. Save the [Frontify plugin](https://www.figma.com/community/plugin/893898815372491269/frontify) and run it from any Figma Design file.
2. From the plugin, type your Frontify domain and click **Get Started**.
3. Log in to Frontify if needed, then click **Allow access** from the authorization window.

Once you’ve authorized the plugin, you can start using assets from the Frontify plugin in your Figma Design files.

[Learn more about the Frontify plugin →](https://help.frontify.com/en/articles/4485473-get-started-with-your-frontify-plugin-for-figma)

[Learn how to save and manage plugins in Figma →](https://help.figma.com/hc/en-us/articles/360052033434-Community-follows-and-likes#like)

## Add Figma assets to Frontify

Add Figma layers, components, pages, and prototypes to your Guideline pages in Frontify. To do this, you'll need to import Figma assets to Frontify and make sure you've installed the Figma Content Block.

### Import Figma assets

1. In Frontify, select the **Projects** tab from one of your brands.
2. Open a project, then click **New** in the top-right corner and select **Figma** from the dropdown.
3. If your Figma account is not connected, you will be directed to log in to Figma and authorize access.
   - If you’re logged into multiple Figma accounts, you can click **Switch account** toward the bottom of the authorization window to choose a different Figma account to use.
4. Paste the URL of the Figma Design file or layer. Your connected Figma account must have at least `can view` access to the file or `can edit` access to the prototype.
5. Choose the Figma asset(s) you’d like to import. You can hold `⌘ Command` / `⇧ Control` to select multiple assets.
6. Click **Create Asset**.

### Install the Figma Content Block

You must [install the Figma Content Block](https://help.frontify.com/en/articles/6579314-installation-guide-for-figma-block-sync) before you can add Figma assets to Guideline pages.

The Figma Block only needs to be installed once per [Figma team](https://help.figma.com/hc/en-us/articles/360039484194). For example, if the Figma assets you’ll be importing to Frontify belong to two teams, you’ll need to install the Figma Content Block for each team.

### Add imported assets to Guideline pages

1. Open one of your brand’s guidelines and toggle Edit Mode.
2. Click the + **Add Content Block** icon on the guideline page to open the block selector.
3. Choose **Figma** from the **UI & Code** section, or type `Figma` in the search bar.
4. Click **Choose Figma asset**.
5. Select the project containing Figma assets and click on the asset to upload it.
6. Click the block's setting icon to choose a preview option: **Live mode** (embed) or **Image mode**(SVG). Keep in mind:
   - In order for a viewer of a Guideline page to see an embed of a Figma asset, they must have at least `can view` access to the design file, or the file must have `Anyone with the link can view` enabled. [Learn more about Figma’s file permissions →](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes)
   - If a block’s preview is set to Image, then anyone with access to the Guideline page will be able to see the image capture. [Learn more about additional customizations to Figma Blocks →](https://help.frontify.com/en/articles/6588621-figma-content-block)

## Questions

For questions and issues, please [contact Frontify’s support team](mailto:support@frontify.com).
