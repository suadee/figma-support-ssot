---
기술지원명: Create a widget for development
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Create a widget for development
출처링크: https://help.figma.com/hc/en-us/articles/4410676552727-Create-a-widget-for-development
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

You must use the Figma desktop app to create and publish widgets. The Figma desktop app is only available for Mac and Windows. [Download the Figma desktop app →](https://www.figma.com/downloads/)

This article covers one step in the widget development process. [Learn how to make widgets for Figma →](https://help.figma.com/hc/en-us/articles/4410596533143)

Find all the information you need to get started writing widgets on the [**Figma widget developers page**](https://developers.figma.com/docs/widgets)**.**

This article covers how to create a new widget in FigJam, and is only one step in the widget development process.

The widget development process:

1. [Setup your development environment →](https://developers.figma.com/docs/widgets/setup-guide/)
2. **Create a widget for development (current article)**
3. [Publish widgets to the Figma Community →](https://help.figma.com/hc/en-us/articles/4410337103639/)
4. [Manage widgets as a developer →](https://help.figma.com/hc/en-us/articles/4410592119703/)

Check out our [Widget Developer docs](https://developers.figma.com/docs/widgets/) for a complete guide on making widgets for the Figma Community.

## Create a widget

Create a widget to begin developing and testing it in FigJam. There are two methods for creating a widget:

- [Widget templates ↓](#h_01FJBE9QM4QC0PXVHMKPYZKX6Q)
- [Import a manifest ↓](#h_01FJBE9Z8SDP9HEYBWN1HXDP8N)

### Widget templates

If you use templates to register a widget, Figma will create a **manifest.json** file on your computer, along with other files and information you'll need to build the widget.

- **code.ts**: the code for the widget in TypeScript
- **code.js**: the compiled Java Script from code.ts
- **package.json**: which describes the widget and includes things like build scripts
- **tsconfig.json**: which configures the TypeScript development
- **README.md**

Warning

**Do not** delete your widget's manifest and other code files from your computer. Figma does not store the code in its database. Deleting the source code from your computer will result in a widget error and remove it from FigJam.

If you create a widget from a FigJam file, you can choose a widget template to create your widget for development.

1. Open a file on the Figma desktop app.
2. Open the **Create widget** modal.
   - Right-click the board or canvas> **Widgets** > **Development** > **New widget.**
   - Or open the file menu > **Widgets** > **Development** > **New widget**.![alt](https://help.figma.com/hc/article_attachments/4420579101719)
3. In the **Create widget**modal, give your widget a name and select a product to develop for:
   - **Figma Design + FigJam:** Create a universal widget that works for both products.
   - **Figma Design:** Select this to create a widget for Figma Design only.
   - **FigJam:** Select this to create a widget for FigJam only.
4. In the **Create widget** modal, give your widget a name and select a template:
   - **Empty**: A blank slate where you can build your widget from the ground up.
   - **Simple widget:** Use this template to build a widget that users can directly click on to perform actions. The simplest way to get started.
   - **With iFrame & browser APIs:** Use this template if you want users to interact with your widget in an iFrame window, which also provides access to browser and third-party APIs. ![Create widget modal in Figma showing options: Empty, Simple widget, and With iframe & browser APIs, with 'Simple Widget' selected.](https://help.figma.com/hc/article_attachments/4411033069463)
5. Click **Save as**.
6. Figma will prompt you to enter a name and select a location on your computer to store your widget's source code. Click **Save** to confirm the download.

You can now access your widget from **Widgets** > **Development** in your file. You'll see your widget's name appear in this menu.

### Import the widget from a manifest

If you're building the widget from scratch, you can import your manifest to create your widget.

1. Open a file on the Figma desktop app.
2. To import a manifest, do one of the following:
   - Right-click the board or canvas > **Widgets** > **Development** > **Import widget from manifest**
   - You can also open the file menu > **Widgets** > **Development** > **Import widget from manifest**
   - Or use [quick actions](https://help.figma.com/hc/en-us/articles/360040328653) > **Import widget from manifest**
3. Select a manifest file from your computer, then click **Open** to confirm the import.

You can now access your widget from **Widgets** > **Development** in your file. You'll see your widget's name appear in this menu.

## View the widget's code

To view where a widget's source code is located:

### Figma Design

1. Open a Figma file on the Figma desktop app.
2. Click  and select the **Widgets** tab. Once you have a widget in development, you’ll be able to see the **Development** section in the dropdown menu.
3. Click  next to the widget and select **Reveal in Finder.**

### FigJam

1. Open a FigJam file on the Figma desktop app.
2. Click  and select the **Widgets** tab. Once you have a widget in development, you'll be able to see the **Development** section.
3. Click  next to the widget and select **Reveal in Finder.**

![Development panel in FigJam showing widgets in progress with options to Reveal in Finder or publish.](https://help.figma.com/hc/article_attachments/4419772517271)

Figma will open the folder with the manifest file selected.

## Insert your development widget

You can insert your widget into a FigJam file while it's in development to test your widget.

1. ### Figma Design

   1. Click  and select the **Widgets** tab. Find your widget under the **Development** section.
   2. To insert your widget, do one of the following:
      - Click or drag the widget into the canvas
      - Use the right-click menu or file menu > **Widgets** > **Development** > Select the widget
      - Use quick actions and search for the widget by name.

   ### FigJam

   1. Click  and select the **Widgets** tab. Find your widget under the **Development** section.
   2. To insert your widget, do one of the following:
      - Click or drag the widget into the board
      - You can also use the right-click menu or file menu > **Widgets** > **Development** > Select the widget
      - Or use [quick actions](https://help.figma.com/hc/en-us/articles/360040328653) and search for the widget by name.

   Once you've finished building your widget, share it with the Figma Community so others can install and use it! [Learn how to publish your widget to the Figma Community →](https://help.figma.com/hc/en-us/articles/4410337103639-Publish-widgets-to-the-Figma-Community)

   [Back: Widgets developer guide](https://help.figma.com/hc/en-us/articles/4410596533143)[Next: Publish a widget](https://help.figma.com/hc/en-us/articles/4410337103639/)
