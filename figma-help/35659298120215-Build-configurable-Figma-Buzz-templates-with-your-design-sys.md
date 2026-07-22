---
기술지원명: Build configurable Figma Buzz templates with your design system
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Build configurable Figma Buzz templates with your design system
출처링크: https://help.figma.com/hc/en-us/articles/35659298120215-Build-configurable-Figma-Buzz-templates-with-your-design-system
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Publishing templates is available on paid plans.

Professional plan teams can publish five templates. Organization and Enterprise plan teams can publish unlimited templates.

Create on-brand, flexible templates powered by your design system. Figma Buzz templates can use:

- Component properties (variants, booleans, instance swaps)
- Variable modes

When you build templates in Figma using component sets, component properties, and variable modes, Figma Buzz converts them into configurable templates—all connected to your design system.

To get started with component properties in templates:

1. Build your template using component properties or variable modes.
2. Publish the templates.
3. Template users configure template options in Figma Buzz. Users can select layout variations and toggle options, all configured based on the component properties or variable modes in the template.

![An assortment of configurable templates in Figma Buzz, with dropdown toggles to customize the template based on component properties.](https://help.figma.com/hc/article_attachments/35752900445847)

## Build your template with component properties

Component properties are the changeable aspects of a component. They let you define which parts of a design can be edited.

[Learn more about component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties).

Use the following component property types to define configuration options in Figma Buzz:

- Use variant properties for any variations you need in a template, such as size, layout, or color variations.
- Use boolean properties to toggle element visibility on or off (e.g., show/hide a logo or other element).
- Use instance swap properties for swapping between nested components, such as a logo or icon.
  - You can define [preferred instances](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties#preferred) when configuring your component properties so that template users only see preferred replacements in Figma Buzz

See below for examples of how each component property type is used in a Figma Buzz template.

Note: When you add a text property to a Figma Buzz template, it appears as an editable text field in the **Edit content** panel on the right sidebar.

**Variant properties**

Template users see each variant as layout options for their template.

1. Select the asset.
2. Click  **Change layout** from the toolbar.
3. In the **Change layout** modal, use the **Browse** tab to preview and select layout variations, or switch to the **Customize** tab to select a variant from a dropdown.

![An asset is selected, and the _Change layout_ button from the toolbar is also selected. There is a _Change layout_ modal with a _Browse_ tab with different template variations to select from.](https://help.figma.com/hc/article_attachments/35659839799831)

**Boolean properties**

Template users see boolean properties as toggle controls when customizing a layout.

For a template user to see boolean properties:

1. Select the asset.
2. Click  **Change layout** from the toolbar.
3. In the **Change layout** modal, select the **Customize** tab.
4. Use the toggle switches to turn boolean properties on or off.

![An asset is selected, and the _Change layout_ button from the toolbar is also selected. There is a _Change layout_ modal with a _Customize_ tab with different template configurations to set.](https://help.figma.com/hc/article_attachments/35659839802775)

**Instance swap properties**

Template users see instance swap properties as dropdowns when customizing a layout.

1. Select the asset.
2. Click  **Change layout** from the toolbar.
3. In the **Change layout** modal, select the **Customize** tab.
4. Select instance swaps from a dropdown menu.

### Build component sets in Figma Design

Create your templates in Figma Design using component sets and properties.

[Learn more about component properties in Figma Design](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties).

**Tip**: Use clear, readable names for the component properties you create in Figma Design. The names you use in Figma Design appear as dropdown labels for templates users in Figma Buzz.

Then, paste the component set from Figma Design into Figma Buzz. When you paste a component set:

- Figma Buzz automatically converts your component set into a template set, preserving its variants and properties.
- Each variant becomes it’s own template within the template set.
- Select  **Grid view** from Figma Buzz to see the full template set.
- Templates in a template set are organized in rows, and outlined in a pink bounding box. The name of the component set in Figma Design is the name of the template set in Figma Buzz.

### Configure template sets in Figma Buzz

Users with Full seats can also build and configure template sets directly in Figma Buzz.

To create a template set:

1. Switch to **Design mode** by selecting the  **Design** toggle from the bottom toolbar.
2. Select multiple assets.
3. From the right sidebar, click **Create template set**.

![Multiple assets are selected on the canvas. The mouse is hovering over a _Create template set_ icon in the right sidebar.](https://help.figma.com/hc/article_attachments/35659816299159)

Once you’ve created the template set:

- Use the right sidebar to create or edit properties and variants
- Define property names and default values for each property you add

Note: If you see an error message about conflicting values or invalid properties, it usually means there’s an issue with how your variants are set up. Try the following to fix the error:

- Make sure each variant includes all defined properties
- Update any variants that share identical property combinations so each variant is unique.

![A template set is selected. From the right sidebar in Design mode, you can add and configure variant properties.](https://help.figma.com/hc/article_attachments/35659816300311)

## Build your template with variable modes

Variable modes let you define design-system–level configurations such as color themes, localized content, or other variables, all within a single template.

[Learn more about variables in Figma](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma).

Variable modes must be created in Figma Design, then copied and published as a template to Figma Buzz.

Template users can switch between variable mode options using the  **Apply variable modes** option from the inline toolbar.

[Learn more about applying variable modes in Figma Buzz templates](https://help.figma.com/hc/en-us/articles/31271689852823-Find-and-use-Figma-Buzz-templates).

## Publish templates

When you publish, you can mix template sets and single templates in the same file.

To publish:

- Click **Share > Publish** template
- Review all templates in the **Review & select** step
- Figma Buzz highlights templates with property conflicts (such as missing or duplicate values) under **Review issues** so you can fix them before publishing

After resolving any issues, click **Next**, then fill in your **Set details** such as name, thumbnail, and description.

[Learn more about publishing templates](https://help.figma.com/hc/en-us/articles/31271693614487-Create-and-publish-Figma-Buzz-templates).

Note: Templates published in Figma Buzz are not synced with Figma Design, even if you copied them from Figma Design into Buzz.

Once you copy a design to or publish a template in Figma Buzz, it becomes a separate, independent file.

However, any nested components inside your Buzz templates remain connected to their original components in Figma Design and can still [receive updates from your libraries](https://help.figma.com/hc/en-us/articles/33799043961879).

### Update templates with nested instances

If your published templates include nested instances (any component embedded within your main component), you’ll need to follow this workflow to ensure changes propagate correctly.

1. [Publish updates from the source component](https://help.figma.com/hc/en-us/articles/360025508373-Publish-a-library#h_01J688PTA7V9DE1KSKQXAMNXRZ): Open the original component file for the nested instance, and publish your updates to the team library.
2. [Pull the updates in the Figma Buzz template file](https://help.figma.com/hc/en-us/articles/33799043961879-Use-libraries-in-Figma-Buzz#h_01K1BN0095E4RPV5VV842Z1BVV): Open the Figma Buzz template file that uses the nested instance, and pull the latest changes for that nested component.
3. Re-publish the Figma Buzz template.

Any existing assets made from that template can then pull the new updates.

## Related resources

- [Create and publish Figma Buzz templates](https://help.figma.com/hc/en-us/articles/31271693614487-Create-and-publish-Figma-Buzz-templates): Follow the full workflow for preparing and managing templates in Buzz.
- [Find and use Figma Buzz templates](https://help.figma.com/hc/en-us/articles/31271689852823-Find-and-use-Figma-Buzz-templates): Learn how users add, edit, and stay on brand using published templates.
- [Playground file](https://www.figma.com/community/file/1562846464052533915): Grab a copy of the playground file to get hands-on practice while you learn.
- **Video**: Watch the video below for more guidance on building templates with component properties.
