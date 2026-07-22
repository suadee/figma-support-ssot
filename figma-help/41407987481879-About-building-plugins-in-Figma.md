---
기술지원명: About building plugins in Figma
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: About building plugins in Figma
출처링크: https://help.figma.com/hc/en-us/articles/41407987481879-About-building-plugins-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## What are plugins?

Plugins are third-party scripts or applications that extend the functionality of Figma's products. You can use plugins to customize your experience and create more efficient workflows. Plugins interact with Figma using the [Plugin API](https://developers.figma.com/docs/plugins/).

The Plugin API is built around a set of fixed controlled endpoints. This ensures your plugins won't break when Figma releases new features and updates.

- The Figma Plugins API gives both you **read** and **write** access to Files.
- Plugins can also use external **Web APIs** such as the Google Maps API. This allows you to create plugins that can view, modify and create objects or layers.
- Plugins are usually short-lived and are always manually invoked by the user. They can run immediately, or may require input from the user before applying any changes.

## Types of plugins

In Figma, there are two types of plugins that are categorized by the method in which they’re built:

- **Classic plugins**, where your development environment is hosted locally on your computer
- **Generative plugins**, where you build via prompting the [Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799-Work-with-the-Figma-agent-in-design-files) in design files

If you are interested in building a plugin, there are some key distinctions between classic and generative plugins that may influence which method you wish to take. These differences are laid out in the comparison table below:

|  | **Classic plugins** | **Generative plugins** |
| --- | --- | --- |
| **Backed by** | Figma Plugin API | Figma Plugin API |
| **Environment** | Local; Built in your own development environment and hosted in your local database. | Figma Design; Built via prompting Figma’s agent in Figma Design, and hosted on Figma’s database. |
| **Third-party API Calls** | Supported | Not supported |
| **UI customization** | Full customization of look and feel | Uses assets from [Figma’s PropsKit components](https://help.figma.com/hc/en-us/articles/41306719221143-PropsKit-component-playground) and therefore looks native to Figma files |
| **Cost** | Free to build and publish | Costs AI credits to build; Free to run the tool |
| **Monetization** | Supported, optional | Coming soon |
| **Shareability** | Private plugins for Org; Publishable to Community | Coming soon |

Overall, classic plugins are suitable for developers who are familiar with how to code and the development lifecycle, or who need full control over the style and feel of a plugin.

On the other hand, generative plugins are best for those are not familiar with code, or want their plugins to look native to Figma.

## Get started

To get started on building a classic plugin, check out Figma's article series on [making classic plugins for the Figma Community](https://help.figma.com/hc/en-us/articles/360039958874) and the [Build Your First Plugin](https://help.figma.com/hc/en-us/sections/6448765398551-Build-your-first-plugin) course.

If you're looking to work with the Figma agent to generate a plugin, check out the [quick start guide to generative plugins and shaders](https://help.figma.com/hc/en-us/articles/41147702210071).
