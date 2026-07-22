---
기술지원명: Rename layers with AI
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Rename layers with AI
출처링크: https://help.figma.com/hc/en-us/articles/24004711129879-Rename-layers-with-AI
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available in Figma Design

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires can edit file access

[Learn more about who can access AI features in Figma](https://help.figma.com/hc/en-us/articles/24039793359767).

With Figma AI, you can give your layers contextual names in a few clicks. This helps you organize your files and simplifies the process of [naming layers in bulk](https://help.figma.com/hc/en-us/articles/360039958934-Rename-Layers).

## How it works

Figma AI will use a layer's contents, location, and relationship to other selected layers to choose a name.

If you have the same unnamed layer across multiple top-level frames on the page, Figma will also rename any matching layers. This makes sure any prototyping settings, like [Smart animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames) and [scroll position](https://help.figma.com/hc/en-us/articles/360051747774), continue to work as expected.

Figma AI will only rename layers that use Figma's default naming convention. If you've already renamed layers and include them in your selection, Figma AI will keep those layer names.

**Figma AI will only rename certain types of layers:**

- Frames
- Groups
- Rectangles and rounded rectangles that contain an image fill
- Text layers
- Instances that still use the same default name as their main component. This will only apply to the container name, Figma AI will ignore any instance sublayers.

**Figma AI will not rename these types of layers:**

- Layers you've already renamed. Figma will keep the existing layer name, even if you include them in your selection.
- Hidden or locked layers. You can lock or hide any layers you don't want Figma AI to rename.
- Any layers nested within an instance. If you want to rename instance sublayers, you can update the layer names manually, or at the component level.
- Individual vector shapes, such as ellipses, stars, polygons, and vector networks. This also include rectangles and rounded rectangles that don't contain an image fill.

## Rename layers with Figma AI

There are a few ways to rename layers. Once you've made your selection, you can:

- Right-click the selection and select **Rename layers**
- Click  **Actions** in the toolbar and select **Rename layers**
- Open the quick actions menu and type **Rename layers**

If the layers in your selection have already been renamed, you'll see a **No layers need renaming** message above the toolbar. Select **Rename anyway** to perform the action again.

**Tip:** You can further [customize your layer names with regular expressions and bulk renaming](https://help.figma.com/hc/en-us/articles/360039958934-Rename-Layers). This is helpful if you want to use specific layer naming conventions, like a prefix or suffix.
