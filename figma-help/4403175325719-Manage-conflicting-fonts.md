---
기술지원명: Manage conflicting fonts
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage conflicting fonts
출처링크: https://help.figma.com/hc/en-us/articles/4403175325719-Manage-conflicting-fonts
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma uses fonts from three different sources. If the same font is available from more than one source, Figma will serve fonts in this order:

1. [Shared font uploaded to the organization](https://help.figma.com/hc/en-us/articles/360039956774)
2. [Fonts installed on your device](https://help.figma.com/hc/en-us/articles/360039956894)
3. [Default web fonts provided by Figma](https://help.figma.com/hc/en-us/articles/360039956634)

Note: Inter, the default font in Figma Design, is served in a different order. If you have Inter installed on your device, Figma will ignore this version and use the one provided by Figma. If your organization uploads Inter as a shared font, Figma will use the shared font in files.

Inter is Figma's interface font and is one of the default fonts we provide in Figma. If you also have Inter installed on your device, Figma will use this version over the one provided by Figma. If your organization uploads Inter as a shared font, Figma will use this version in files.

If editors use different versions of the same font, you may see conflicting fonts. This can appear in any of these ways:

- [Missing font warning in some files ↓](#missing-font-some)
- [Text shifts or changes format ↓](#text-reformatting)
- [Icon fonts turn into text ↓](#broken-icon-font)
- [Ligatures not working ↓](#ligatures)

[**Jump to fix conflicting font issues ↓**](#resolve-conflicts)

- A 

  ### Missing font warning in some files

  The font is an available choice in your Figma file, but some files have missing font weights or are showing the missing font warning modal. This happens when other editors of the file using a different version of the same font.

  ![Missing font warning in Figma with options to select replacement fonts for Misto and Ribes fonts.](https://help.figma.com/hc/article_attachments/27454892078743)
- B 

  ### Text shifts or changes format

  The text layer moves or reformats when you edit it. For example, the layer baseline shifts, changes weight, or changes alignment.

  This happens when other editors of the file are using a different version of the same font.

  > Crystal has Inter v3.0 installed on her computer and uses it in a Figma file. A few days later, Joey installs Inter v3.18 and opens the same file. He edits an existing text layer using Inter, and the layer shifts two pixels up. While Crystal and Joey have the same font installed, they were different versions.
- C 

  ### Icon fonts turns into text

  An icon font turns into a text description of the icon font when you edit or activate the text layer.
- D 

  ### Ligatures aren't working

  If ligatures aren't working, make sure you've toggled them on in the **[Type Details panel](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties#h_593601e4-3239-4664-8939-96712e1d881d)**. If ligatures are on and you're still experiencing the issue, make sure all editors are using the same version of the font.

## Fix conflicting font issues

If editors use different versions of the same font, you may have **[conflicting font issues ↑](#conflicting-fonts).** To resolve conflicting font issues, all editors in the file need to:

### Update the font

1. Uninstall and remove the font from their computer.
2. Download and install the font from one common source.
3. Restart the desktop or browser app.

### Update affected layers

1. Select a layer using that font.
2. Open the  menu or open the quick actions menu.
3. Use **Select all with same font** to select all text layers with that font.
4. Use **Recompute Text Layout in Selection** to reset text to the correct formatting.

[Troubleshoot font issues](https://help.figma.com/hc/en-us/articles/4403018301079) [Manage missing fonts](https://help.figma.com/hc/en-us/articles/360039956994)

Tip: If you're still experiencing problems, please submit a bug report! To speed up the process, please let us know which steps you've tried and any results. [**Learn how to submit a bug report →**](https://help.figma.com/hc/en-us/articles/360041468234)
