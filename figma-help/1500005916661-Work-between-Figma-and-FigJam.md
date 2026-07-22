---
기술지원명: Work between Figma and FigJam
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Work between Figma and FigJam
출처링크: https://help.figma.com/hc/en-us/articles/1500005916661-Work-between-Figma-and-FigJam
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

- Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273)

Share designs, gather feedback, or incorporate research as references. There are a few ways to work between FigJam and design files.

Tip

We've focused on supporting copy and paste between file types, but we'd love to hear what other functionality you'd like to see here. [Share your thoughts and feedback on the Figma Support Forum →](https://forum.figma.com/)

# Copy and paste

You can copy and paste assets between files to progress your design process.

## Copy and paste across devices

Working between multiple devices? You can move Figma and FigJam content from your iPad to your computer, and vice versa, using copy and paste.

Note: You must have version 22.9 or newer of the [Figma mobile app](https://help.figma.com/hc/en-us/articles/1500007537281-Guide-to-the-Figma-mobile-app) installed in order to copy and paste across devices. You also must be logged in to the same account on both devices.

1. Select the objects you want to copy.
2. Copy the objects:
   - iPad: Tap  **Copy**.
   - Desktop: Press `⌘ Command` + `C` (Mac) or `Control` + `C` (Windows).
3. On your second device, a notification banner will pop up on your active Figma or FigJam file. On the notification banner, select **Paste**.

![Image of the pop-up notification on a FigJam canvas prompting to paste a selection copied from another device, with options to paste or dismiss.](https://help.figma.com/hc/article_attachments/12754884431383)

## FigJam to Figma

You can paste any objects from FigJam into a Figma Design file and they will keep their existing color, format, size, and layout.

- Stamps from FigJam boards are actually images! Figma treats them as images when you copy and paste them into a Figma file.
- Any stickers or components will paste as instances in Figma Design.
- Anything drawn with the marker will be treated as a path with stroke properties. You can edit these in edit object mode or adjust the stroke properties.
- Text and links are pasted as text and text with links.
- Even though GIFs do not play in FigJam boards or in the Figma Design canvas, you can copy them from FigJam and they will play in presentation view. Copying GIFs from the browser will paste as static images. **[Add animated GIFs →](https://help.figma.com/hc/en-us/articles/360041486873-Add-animated-GIFs-to-prototypes)**

Figma recognizes some objects from FigJam files as special objects. Special objects appear in the Layers panel in purple with a specific symbol for each object type:

- Sticky notes
- Shapes with text
- Lines and connectors
- Tables

### Edit special objects

|  |  |
| --- | --- |
| Move, flip, rotate, or rearrange special objects on the canvas | ✓ |
| Adjust style properties of a special object, like color and typography | ✓ |
| Select, view, or edit child layers of a special object | ✕ |
| Include special objects in components or instances | ✕ |

Caution

If you are working with special objects in Figma Design, you may run into issues or unexpected outcomes issues when using keyboard shortcuts.

Plugins can read special objects and should be able to change their position on the canvas. We haven't extensively tested interactions between plugins and special objects, so can't guarantee anything beyond this.

## Figma to FigJam

Copy layers from Figma and paste them in FigJam. This includes frames, images, components, text layers and links, and more.

As there is no layers panel in FigJam files, there will be limitations on what you can select within frames, components, or other layers pasted from Figma Design files.

You can still edit most of these layers in FigJam files, but you'll only have access to the curated tools and styling in FigJam. For example: you can only adjust layers to use the FigJam colors and text formatting options.

Figma won't convert objects from Figma Design into their FigJam counterparts. For example: arrows won't become connectors, and custom vector shapes won't become shapes with text.

### FigJam objects

If you've copied FigJam objects to Figma Design and made changes, Figma will keep these changes when you bring them back into FigJam files. For example: changing the color of a sticky note, or adjusting the stroke weight of a connector.

If you update the object to use a FigJam-specific style again, you won't be able to undo that action to access the custom styling you applied in Figma Design.

Note

If you copy an unpublished component from a Figma file and paste it into a FigJam file, the object will paste as a regular object. We recommend publishing the component to a library and accessing the component from your  libraries in FigJam.

# Share libraries

Create component libraries in Figma Design and access them from FigJam files.

- [Guide to libraries →](https://help.figma.com/hc/en-us/articles/360041051154-Guide-to-libraries-in-Figma)
- [Libraries in FigJam →](https://help.figma.com/hc/en-us/articles/1500004290841)
