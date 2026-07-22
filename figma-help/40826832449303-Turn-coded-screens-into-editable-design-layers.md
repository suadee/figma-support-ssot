---
기술지원명: Turn coded screens into editable design layers
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Turn coded screens into editable design layers
출처링크: https://help.figma.com/hc/en-us/articles/40826832449303-Turn-coded-screens-into-editable-design-layers
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on all plans

Capture code-backed screens and bring them into Figma Design and FigJam as design layers. Use the editable layers on the canvas in Figma Design to riff on your production websites, pull real-world inspiration into your FigJam files, jump-start a Figma Make prototype, or revive legacy designs on the canvas.

## Methods

There are few methods for capturing coded screens and bringing them into Figma as editable design layers:

- Use the [Figma Chrome extension](https://help.figma.com/hc/articles/9067379354135) in your browser
- [Copy design layers](https://help.figma.com/hc/en-us/articles/35060759685015-Copy-a-Figma-Make-preview-as-design-layers) from a Figma Make preview
- Use the [Code to canvas tool](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/) `generate_figma_design` via the Figma MCP server

Click the links above to view step-by-step instructions on how to use each method. Below, we’ll cover common workflows, how to incorporate existing variable libraries into the designs, and troubleshooting tips.

## Common workflows

### Start designing from your production websites

Capture your own product's current state and use those frames as the foundation of a redesign exploration on the canvas.

### Revive legacy designs on the canvas

For when you’re working with old legacy designs but the original Figma file no longer exists or is difficult to track down.

### Bring inspirational content onto the canvas

When you're researching patterns or building a moodboard, the extension lets you grab specific UI from real sites and assemble them in a Figma Design file or FigJam board. Because each capture lands as layers, you can isolate the parts you want to study, recolor them, or annotate them directly.

### Kickstart a Figma Make prototype

Capture a page or section from your production website, paste it into Figma Design, then send it to Figma Make as the starting point for a prototype. To send the layers, right-click the frame that contains the layers and select **Send to Figma Make**.

## Connect variables to pasted designs

Figma will try to connect existing variables (color, number, and string) to the pasted designs. Existing variables include variables that were created in the file and variables inside libraries that have been added to the file.

Before you paste your designs, be sure to [add the library](https://help.figma.com/hc/en-us/articles/1500008731201-Add-or-remove-a-library-from-a-design-file) containing the variables. If the variables you want to use already live inside the file, you can skip this step.

[Adding published libraries](https://help.figma.com/hc/en-us/articles/1500008731201-Add-or-remove-a-library-from-a-design-file) to a file is available on paid plans. Those on organization and enterprise plans can use [check designs](https://help.figma.com/hc/en-us/articles/39592284074263-Check-designs-in-Figma) to find layers and properties that didn’t get bound to a variable.

### Supported properties

The following properties are supported on frames:

- Fills and stroke colors
- Stroke weights
- Corner radius
- Padding
- Gap-between
- Layer opacity

The following properties are supported on text layers:

- Text color fills
- Font family
- Font size
- Font weight
- Line height
- Letter spacing

The following properties are supported on other vector layers:

- Fills and strokes

### **How does Figma match variables to the pasted design?**

Figma prioritizes connecting variables based on matching the variable name from the webpage’s extracted CSS to the [code syntax](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections#code_syntax) of the variable in Figma.

If there are no matches, the extracted CSS variable name is matched to the variable name in Figma. If there are still no matches, Figma will look for the variable with the best matching and most limited [variable scope](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections#h_01H32HZB74TE7MJXYBWEBBQWJV).

If you have a complex design system, it’s good practice to review the variables that have been bound. If you are on an Organization or Enterprise plan, you can use [check designs](https://help.figma.com/hc/en-us/articles/39592284074263-Check-designs-in-Figma) to catch anything that may need attention, like missing matches or suggestions we may want to swap for a more intentional variable.

**Note**: Color variables with opacity will not be bound. You can use [selection colors](https://help.figma.com/hc/en-us/articles/360042553434-View-and-adjust-colors-in-a-mixed-selection) to identify color fills that do not have a variable mapped to them and manually bind them.

## Tips for better captures

- **Scroll first on animated pages.** For pages with dynamic scrolling effects (like marketing sites with reveal animations), scroll all the way to the bottom of the page *before* triggering a page capture. This activates the page's interactions so they're included in the capture.
- **The most recent capture is on your clipboard.** You don't need to click anything in the tray, just go to the canvas in Figma Design or FigJam and paste.
- **Define the variable code syntax for exact mapping**. Figma prioritizes connecting variables based on matching the variable name from the webpage’s extracted CSS to the code syntax of the variable in Figma. Learn how to [define the code syntax](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections#code_syntax).
- **Use readable CSS variable names.** Some site's build process shortens or scrambles variable names (for example, `-font-size` becomes `var(--Mhs7de)`), Figma won't be able to match them to your variable code syntax and names in Figma.
- **Capture from your dev server URL if variable names don't match.** Dev servers typically preserve readable variable names, which allows Figma to match them to your Figma variables.

## What's not currently supported

This is a beta release. In particular:

- **No component and styles mapping yet.** Captures come in as plain Figma layers with variables bound if any are available. They are not automatically mapped to your library components or styles. Further design system support is on the roadmap.
- **Complex scroll-driven or canvas-rendered sites may capture imperfectly.** Pages that use heavy JavaScript animation, `<canvas>` rendering, or virtualized lists may not translate cleanly. If a capture looks off, try element capture on the specific section instead of the whole page.
- `chrome://` **and other privileged pages can't be captured.** The extension button has no effect on internal Chrome pages.

## Troubleshooting

**Nothing happens when I click the Figma icon.** The extension can't run on `chrome://` URLs, the Chrome Web Store, or other privileged pages. Open a regular webpage and try again.

**I just updated the extension and the toolbar isn't showing up.** Refresh the tab, and ensure you have a paid plan. Extension updates don't take effect on tabs that were already open.

**Pasting into Figma doesn't add anything to the canvas.** Make sure the Figma tab is focused (click into the canvas first), then paste. If it still doesn't work, try recapturing. The most recent capture is what gets pasted.

**I'm on a Starter plan and capture doesn't work.** Code to canvas is currently limited to paid plans during the beta. Other extension features remain available on all plans.

**A variable didn’t bind to the layer.** Make sure that the library with variables you want to use is added to the file *before* you paste the designs.

## Share feedback

This feature is in active development. If you encounter a bug, capture something that comes out wrong, or have an idea for how it should work, please share it.

- [Contact Figma Support](https://help.figma.com/hc/en-us/requests/new)

## Keep learning

- [Workflow lab: Code to canvas](https://help.figma.com/hc/en-us/articles/40219873508247-Workflow-lab-Code-to-canvas)
- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559)
- [Get started with Figma Make](https://help.figma.com/hc/en-us/categories/31304285531543)
