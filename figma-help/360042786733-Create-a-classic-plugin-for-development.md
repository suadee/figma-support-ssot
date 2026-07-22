---
기술지원명: Create a classic plugin for development
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Create a classic plugin for development
출처링크: https://help.figma.com/hc/en-us/articles/360042786733-Create-a-classic-plugin-for-development
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

You must use the Figma desktop app to create and publish plugins. The Figma desktop app is only available for Mac and Windows. [Download the Figma desktop app](https://www.figma.com/downloads/).

This article covers one step in the classic plugin development process. Learn how to [make classic plugins for Figma](https://help.figma.com/hc/en-us/articles/360039958874).

Find all the information you need to get started writing plugins in the [**Plugin API documentation**](https://developers.figma.com/docs/plugins)**.**

## Create a plugin

When you create a plugin, Figma generates a directory that includes the folders and critical files that you'll need to build your plugin.

1. Open the [Figma desktop app](https://www.figma.com/downloads/).
2. Create or open a file.
3. In the upper-left corner, open the Figma menu and select **Plugins**.
4. Under **Development**:
   - Select **New Plugin...** to create a plugin using a [plugin template](#h_01FJCABQ2ADBJZCY7MJZ7PVQ47). The set of templates that are available to you depend on the product you're using.
   - Select **Import new plugin from manifest...** if you already have your source code on your computer.
5. Follow the prompts provided to create your plugin.
6. After you create your plugin, you can find it listed under **Development**.
   - You can also find your plugin under the **Development** section of the [Plugins tab in Figma Design, Dev Mode, FigJam, Figma Slides, and Figma Buzz.](https://help.figma.com/hc/en-us/articles/360042532714-Run-plugins-in-files#Bottom_toolbar_FigJam_only)

Now that you have your plugin files, to learn more about developing plugins for Figma, check out the [Build your first plugin](https://help.figma.com/hc/en-us/articles/4407260620823) course.

![New plugin creation confirmation with options to open folder or connect with developers on Discord; setup guide link provided.](https://help.figma.com/hc/article_attachments/15460113314199)

When your plugin is ready to share with others, you can publish it! Read more about how to [publish plugins to the Figma Community](https://help.figma.com/hc/en-us/articles/360042293394).

## Plugin templates

Figma provides templates that you can use to get started with your plugin. You select a template when you [create a plugin.](#h_01H3DQNKYVJ2WXSY5820V6SKWJ)

When you create a plugin in Figma Design, FigJam, Figma Slides, or Figma Buzz, you're asked if you want your plugin to be **Multi-product** or specific to the product you're using at the time. Your selection determines the [editor type](https://www.figma.com/plugin-docs/setting-editor-type/) of your plugin.

After you make a choice, you're prompted to select one of the available templates:

- **Default**: A blank slate where you can build your plugin from the ground up.
- **Run once**: This is a template for a plugin that runs once with no further interaction from the user. Use this template if your plugin doesn't need a UI.
- **Custom UI**: Use this template if you want to create a plugin with an interactive UI or that uses browser APIs.

When you create a plugin in Dev Mode, the following templates are available:

- **Inspect**: Build a plugin that inspects a design. Implement UI elements that are rendered in the Plugins tab of the inspect panel in Dev Mode.
- **Code Generator**: Create a plugin that generates code snippets in the inspect panel in Dev Mode.
