---
기술지원명: Widget Code Generator by Figma
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Widget Code Generator by Figma
출처링크: https://help.figma.com/hc/en-us/articles/5601345554967-Widget-Code-Generator-by-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

🚧  Widget Code Generator is currently in open beta

Beta features can change during the beta period. You may experience bugs or performance issues during this time. **[Learn more about beta features →](https://help.figma.com/hc/en-us/articles/4406787442711)**

Before you start

Who can use this feature

 

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

This plugin is for Figma Design only. You must use the Figma Desktop app to develop widgets.

[**Download the Figma Desktop app ->**](https://help.figma.com/hc/en-us/articles/360039827194)

The Widget Code Generator plugin for Figma Design allows you to design FigJam widgets and easily translate your designs into code. This Figma plugin generates code that you can copy and use to create a widget interface. In order to add functionality to your widget, you’ll need to edit the generated code. [Learn how to build widgets →](https://www.figma.com/widget-docs/setup-guide/)

In order to use generated code from the plugin, you need to:

- Setup your widget development environment. [Check out the setup guide here →](https://www.figma.com/widget-docs/setup-guide/)
- Install the [Widget Code Generator](https://www.figma.com/community/plugin/1096460041736534298/Beta-2) from the Figma Community. [Learn how to find and install plugins →](https://help.figma.com/hc/en-us/articles/360040450413-Find-and-install-plugins)

## Run the plugin

Once you have Widget Code Generator installed, you can run it a few different ways:

- Right-click on the canvas > **Plugins** > Select **Widget Code Generator**
- From the desktop app, open the **Plugins** menu at the top then select **Widget Code Generator**

After selecting the plugin, the **Widget Code Generator** modal will pop up.

![Widget Code Generator modal displaying JSX code for a Figma widget design with AutoLayout and Frame elements.](https://help.figma.com/hc/article_attachments/5976447430679)

### Generate code

The Widget Code Generator can only generate code one layer at a time, including all of the children in the layer tree. Select an individual layer while the plugin is running to see the generated code in the modal.

![Widget Code Generator in Figma transforming a star shape design into JSX code within a modal window.](https://help.figma.com/hc/article_attachments/5979643892375)

If changes are being made to a layer, the generated code won’t automatically update. After making changes to a layer, hit the ‘Refresh’ button to get the most updated code for your component.

![Widget Code Generator displaying SVG code for a star shape; refresh and copy buttons visible in the modal.](https://help.figma.com/hc/article_attachments/5979654564375)

Note

When preparing to generate code for your design, make sure that you are only using characters A-Z and 0-9 in your layer names and that none of your components have [reserved names](https://github.com/figma/widget-typings/blob/1d9390f5b43e1ea3abcaabd4e7f2e4aa96ba62b5/index.d.ts#L53) that are used for Figma component types(ie. frame, rectangle).

### Instance nodes

When you generate code for a design containing an Instance node, the code for all layers of that instance will not be included. Instead, a tag representing the instance will be shown. This reduces duplication when you use several instances of the same component, and makes your generated code more readable. If your design includes several instances of a component named `MyComponent`, the generated code will look like this:

```
export function MyDesign() {
  return <Frame>
  	<MyComponent/>
	<MyComponent/>
	<MyComponent/>
 </Frame>
}
```

If you copy-paste this into your editor and try to run it, it will not compile because `MyComponent` will be undefined.

To fix this, select `MyComponent` in Figma and generate code for that instance. To go to the main component, right-click on the individual layer then select **Go to main** **component**. You can also click on the **Go to main component** link that appears in the warning message at the top of the modal.

![Widget Code Generator modal displaying JSX code with an instance warning for a Figma component, suggesting a need to access the main component.](https://help.figma.com/hc/article_attachments/5977759245335)

### Create inputs

Since there’s no way to mark a component as an Input in Figma, the Design→Code plugin can’t generate `<Input/>` tags.

If your widget design contains an input:

1. Design the input field using the Text layer type.
2. Generate code for the text layer using the plugin.
3. Locate the opening and closing `Text` tags for that node and replace them with `Input`.
4. Add props for `onTextEditEnd`, `placeholder` and `value` to [make your input functional.](https://www.figma.com/widget-docs/text-editing/)

### Render images

To render an image in a widget, the image must be externally hosted or passed in as a data URI. Since we don’t know where your image will come from, we can’t generate complete code for an `Image` tag. Instead, you will receive something like:

```
<Image src="<Add image URL here>"/>
```

Complete the code with the correct image source and it will be visible in your widget!

### What’s not supported

The following features are supported in Figma Design, but aren’t supported in Widgets yet and therefore cannot be generated:

- Masks
- [Fonts from your computer](https://help.figma.com/hc/en-us/articles/360039956894-Access-local-fonts-on-your-computer) you’ve uploaded to Figma (not Google fonts)
- Multiple text styles in one node (plugin will generate the first style)
- Layer names with characters outside of A-Z and 0-9
- Nodes with a width or height of less than 1px will be rounded up to 1px
- Gradient strokes (supported in widgets but the plugin currently doesn’t generate code for it)
