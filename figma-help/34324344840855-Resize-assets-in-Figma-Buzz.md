---
기술지원명: Resize assets in Figma Buzz
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Resize assets in Figma Buzz
출처링크: https://help.figma.com/hc/en-us/articles/34324344840855-Resize-assets-in-Figma-Buzz
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

While in beta, Figma Buzz is available on all seats and plans.

Anyone with `can edit` permissions in a file can resize assets

Both brand designers and marketers can use Figma Buzz to create high-quality, on-brand assets quickly and confidently. Brand designers build and share templates for their teams, while marketers customize those templates to suit specific needs.

Often, assets need to be adapted for different formats and sizes—like vertical social media stories, banner images, and other platform-specific dimensions.

In this article, you’ll review best practices for preparing assets for resizing, and learn how to resize assets directly in Figma Buzz.

## Resize assets

To resize an asset in Figma Buzz:

1. Select the asset on your canvas.
2. In the toolbar, open the **Size** dropdown menu.
3. Choose a preset size (like "Instagram Post" or "YouTube thumbnail") or enter your own custom dimensions.

![An asset is selected in Figma Buzz. Choose a new asset size from the dropdown in the inline toolbar.](https://help.figma.com/hc/article_attachments/34325068560023)

Note: If you’re using a branded template, you won’t be able to resize it unless you [remove editing restrictions](https://help.figma.com/hc/articles/31271689852823).

To resize multiple assets quickly:

1. Click  **Bulk create** from the left navigation bar.
2. In **Asset size** column, select the size dropdown for each asset to resize.

![Resize assets quickly from the Bulk create tab.](https://help.figma.com/hc/article_attachments/40665352558743)

## Resizing best practices

When you're designing assets for Figma Buzz, it's important to consider how they will behave when resized. Following a few best practices can help ensure that the asset is flexible and responsive.

These techniques are intended for designers creating and publishing templates. You can apply them while building the original design in Figma Design (before pasting it into Figma Buzz), or in [design mode in Figma Buzz](https://help.figma.com/hc/en-us/articles/31271851622807-Use-Figma-Design-tools-in-Figma-Buzz).

### Use auto layout

Auto layout is an essential tool for creating responsive, adaptable designs in Figma.

![Autolayout is applied in Figma Design. Then, in Figma Buzz, the asset is resized, with the text on the asset adapting to the new size.](https://help.figma.com/hc/article_attachments/34326312486679)

Elements in an auto layout frame are automatically arranged based on direction, spacing, padding, alignment, and other auto layout properties. When the content changes or the frame is resized, the layout adjusts without manual repositioning.

You can apply auto layout to parent frames and child objects within a frame.

To apply auto layout in Figma Design:

1. Select one or more layers.
2. Press `Shift` `A`, or click  **Use auto layout** from the **Layers** section of the right sidebar.

Then, adjust the auto layout properties from the **Auto layout** section of the right sidebar.

How you use auto layout will depend on the specifics of your design, but here are a few key concepts to help you get started:

- Use **padding** and **gap** values to maintain spacing between and around objects.
- If you want a child object to stretch to fill all available space in their parent frame while still respecting any spacing values, apply **Fill container** resizing to the child objects.
- If you want to ensure that objects don’t collapse too small or expand too large when resized, set **minimum and maximum width and height values** for those objects. You can use minimum and maximum values in combination with **Fill container**.

**Tip:** If you’re new to auto layout, check out these resources:

- Watch and read: [the auto layout module in the Figma Design for Beginners course](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners)
- Read: [Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout).

### Apply constraints

Constraints define how layers behave when their parent frame is resized. This allows you to build assets that adapt to different sizes without misaligning or overlapping content.

Note:  It's not possible to apply constraints to layers in an [auto layout frame](https://help.figma.com/hc/en-us/articles/360040451373). Play around with auto layout and constraints separately, to see which strategy works best for your design.

![Constraints are applied to image and logo in Figma Design. Then the design in pasted into Figma Buzz. When the user resizes the asset, the image and logo adapts to new size.](https://help.figma.com/hc/article_attachments/34326309405079)

You can apply constraints in Figma Design, or in [design mode in Figma Buzz](https://help.figma.com/hc/en-us/articles/31271851622807-Use-Figma-Design-tools-in-Figma-Buzz).

1. Select a layer.
2. Click  **Constraints** from the **Position** section of the right sidebar.

How you use constraints will depend on the specifics of your design, but here are a few key concepts to help you get started.

You can apply constraints in both the **horizontal (x)** and **vertical (y)** directions:

- **Left** or **Top**: Keeps the layer pinned to the top or left side of the frame.
- **Right** or **Bottom**: Pins the layer to the opposite edge.
- **Left and Right** (or Top and Bottom): Stretches the layer between both sides, so it expands/contracts when resized.
- **Center**: Keeps the layer centered as the frame resizes.
- **Scale**: Maintains the layer’s position and size as a percentage of the frame dimensions.

**Tip:** If you’re new to constraints, check out these resources:

- Watch: [the constraints fundamentals lesson in the Figma Design for Beginners course](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners)
- Read: [Apply constraints to define how layers resize](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize).

### Lock aspect ratio

Locking a layer’s aspect ratio ensures it retains the same width-to-height proportions when resized. This is especially helpful for logos, product images, vector objects, or illustrations that must maintain visual consistency at any size.

![An asset is resized, and the image in the asset does not maintain proportions when resized. Then, aspect ratio is locked on the image. When the asset is resized, the image retains proper proportions.](https://help.figma.com/hc/article_attachments/34326312489367)

You can apply lock aspect ratio in Figma Design, or in [design mode in Figma Buzz](https://help.figma.com/hc/en-us/articles/31271851622807-Use-Figma-Design-tools-in-Figma-Buzz).

1. Select the layer.
2. In the right sidebar under the **Layout** or **Auto layout** section, click  **Lock aspect ratio.**

**Tip:** If you’re new to lock aspect ratio, check out these resources:

- Watch and read: [Aspect ratio lock on Figma's YouTube channel](https://youtube.com/shorts/SITklmLqXo4?si=sM6XLkF-Q_RYYwlo)
- Read: [Lock aspect ratio](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-position-and-dimensions#aspect-ratio).

### Test your design

Even with auto layout, constraints, and aspect ratio locks in place, your design may still require manual adjustments—especially when resizing across drastically different sizes and ratios.

To test your design, try resizing it either in Figma Design and Figma Buzz. Then, check for common issues, such as:

- Overlapping content
- Misaligned content or padding
- Unexpected shifts in layout
- Image distortion

Test with long and short text strings to validate text behavior. Adjust as needed using the techniques above—each design is different, so take time to QA your asset thoroughly before publishing.

### Publish assets as a template set

As the template designer, you can include multiple assets in a single Figma Buzz file when publishing.

Each asset will be published as part of a template set. Template sets are helpful when assets need to exist in different dimensions for different platforms—so your team doesn’t need to search or resize manually.

**Tip:** Learn more about templates in Figma Buzz:

- [Create and publish Figma Buzz templates](https://help.figma.com/hc/en-us/articles/31271693614487-Create-and-publish-Figma-Buzz-templates)
- [Find and use Figma Buzz templates](https://help.figma.com/hc/en-us/articles/31271689852823-Find-and-use-Figma-Buzz-templates)
