---
기술지원명: Save a local copy of files
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Save a local copy of files
출처링크: https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available on
[any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with at least `can view` access
to the file can save the file as a local copy as long as
the file’s owner has not [restricted copying and sharing](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files)

You can save a local copy of a file in the .fig
(Figma Design),
.jam
(FigJam), .deck (Figma Slides), .buzz (Figma Buzz), .site (Figma Sites), and
.make (Figma Make) formats. This is useful if you want to
duplicate files between Figma accounts or teams, or if you want to manually
back up your files.

Figma doesn't include any version history or comments when you save a local
copy of a file. When you reimport this file, Figma treats this like a new
file and it won't be connected to the original. Any components in the imported
file
will become
new main components. Instances in the imported file will connect to the new
main components and will not receive updates from components in the original
file.

Note: The .fig, .jam, .deck, .buzz, .site, and .make file
formats are proprietary
and may change in the future. We recommend against using any third-party
tools that ask for these file types because they may not be able
to properly read these files. If you're building a third-party tool,
we recommend accessing files and their contents through one of
[Figma’s officially supported APIs](https://www.figma.com/developers).

To save a local copy of a file:

1. Open the file you want to export.
2. Click  **Main menu**.
3. Go to **File** > **Save local copy** to
   download a copy of the file to [your downloads folder](https://help.figma.com/hc/en-us/articles/360040521373).

Note: If you don’t see the **Save local copy**
setting, the file owner may have restricted viewers from being able
to copy or export assets. Learn more about [restricting copying and sharing on files](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files).

To import a local copy of a file:

1. Open the Figma account you want to import the file to.
2. Drag the file into the file browser.
