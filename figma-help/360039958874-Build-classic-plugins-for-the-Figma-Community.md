---
기술지원명: Build classic plugins for the Figma Community
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Build classic plugins for the Figma Community
출처링크: https://help.figma.com/hc/en-us/articles/360039958874-Build-classic-plugins-for-the-Figma-Community
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Users on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan) can develop plugins for the Figma Community.

You can only develop and publish plugins from the [Figma Desktop App](https://www.figma.com/downloads/). The Desktop App is only available for macOS and Windows.

Plugins are third-party scripts or applications that extend the functionality of Figma's products. You can use plugins to customize your experience and create more efficient workflows. Plugins interact with Figma using the **Plugin API**.

The Plugin API is built around a set of fixed controlled endpoints. This ensures your plugins won't break when Figma releases new features and updates.

- The Figma Plugins API gives both you **read** and **write** access to Files.
- Plugins can also use external **Web APIs** such as the Google Maps API. This allows you to create plugins that can view, modify and create objects or layers.
- Plugins are usually short-lived and are always manually invoked by the user. They can run immediately, or may require input from the user before applying any changes.

## Make classic plugins for Figma products

This article outlines the classic plugin development process in Figma. We designed this as a supplementary resource to our developer documentation. Classic plugins are created differently from generated plugins. Learn more about the [differences between classic and generated plugins](https://help.figma.com/hc/en-us/articles/41407987481879).

1. [Create a classic plugin for development](https://help.figma.com/hc/en-us/articles/360042786733)
2. [Build and test your classic Plugin](https://www.figma.com/plugin-docs/plugin-quickstart-guide)
3. [Publish a classic plugin to the Figma Community](https://help.figma.com/hc/en-us/articles/360042293394)
4. [Manage classic plugins as a developer](https://help.figma.com/hc/en-us/articles/360042293714)

**Check out our**[**Plugin API documentation**](https://developers.figma.com/docs/plugins/) **for a complete guide on making plugins for the Community.**

You must have the Figma Desktop app installed to make plugins.

## Figma Plugin Examples

Here's some examples of existing Figma plugins:

- [**Content Buddy**](https://www.figma.com/c/plugin/731260490045684148/Content-Buddy): Find text within your designs and replace it with the actual copy.
- [**Themer**](https://www.figma.com/c/plugin/731176732337510831/Themer): Swap between published styles from your libraries, in bulk.
- [**Content Reel**](https://www.figma.com/c/plugin/731627216655469013/Content-Reel): Bring data into your designs. Including text strings, avatars and icons.
- [**Map Maker**](https://www.figma.com/c/plugin/731312569747199418/Map-Maker): Insert customized maps into any shape layer.
- [**Figmotion**](https://www.figma.com/c/plugin/733025261168520714/Figmotion): Animate objects within a Frame, without having to leave Figma.
- [**Stark**](https://www.figma.com/c/plugin/732603254453395948/Stark): Checks the contrast of a selected layer against [WCAG 2.1 guidelines](https://www.w3.org/TR/WCAG21/).

![Interactive demonstration of a Figma plugin inserting images into a design project, showing layers panel and toolbar interactions.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d41f4b9042863478675b20a/file-zgl3xr072A.gif)

## Sell plugin source code

Note: Ownership of paid plugins cannot be transferred.

If you’re interested in selling the source code and ownership of plugins you’ve built, do the following:

1. The buyer and seller must [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new) to facilitate the sale. Select **Community plugins, widgets, and files** and **Using or buying a resource**from the dropdowns, then provide details of your request in the **Description**box.
2. The seller must confirm that they are authorizing the sale.
3. The buyer confirms they will abide by our [Terms of Service](https://www.figma.com/tos/) after the sale.

Once this process is complete, the Support team transfers ownership of the plugin between parties.

Keep in mind that once a plugin has been published, the publisher cannot materially change the purpose or nature of the plugin. In order to do so, a new plugin must be [published and reviewed](https://help.figma.com/hc/en-us/articles/4410337103639/) again.

Next: Create a plugin
