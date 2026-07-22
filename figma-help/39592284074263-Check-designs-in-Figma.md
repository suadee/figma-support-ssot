---
기술지원명: Check designs in Figma
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Check designs in Figma
출처링크: https://help.figma.com/hc/en-us/articles/39592284074263-Check-designs-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to the file can use Check designs

Check designs helps you quickly find and fix inconsistencies with your design system, including:

- Hard-coded values that can be replaced with variables or styles, such as:
  - Colors
  - Text styles
  - Corner radius
  - Spacing and padding
- Components, variables, and styles from incorrect libraries, based on your current library selection. This also includes libraries not added to your file, which can happen when designs are copied across files, teams, or projects.
  - For variables and styles, Check designs suggests replacements from your connected libraries. You can accept a suggestion or choose another value from the dropdown.
  - For components, Check designs only flags issues. You’ll need to manually replace them with components from the correct library.

Check designs does not use LLMs or generative AI. Suggestions are ranked based on factors like:

- Similarity to the current value
- Variable naming and hierarchy
- Usage frequency across your team or organization

As your team uses Check designs, suggestions may become more relevant over time.

## Prepare your file

Before you start, keep the following in mind:

- Check designs works best with a published, variables-based design system. By default, Check designs pulls suggestions from all libraries added to this file. However, we recommend [marking a specific selection of libraries](#h_01KNNM8ZYAXX0JE6E8VGJRNEG1) to pull from in Check designs’ settings menu to improve suggestion quality.
- Use precise variable scoping in your design system to improve suggestion quality. For example, you can hide primitives to prevent them from appearing in your design check, or scope variables to specific asset types (like text colors) for more relevant results. [Learn more about scoping variables](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections).

## Run Check designs

Note: There are a few current limitations of Check designs:

- Check designs only runs on one page at a time. It can’t check multiple pages simultaneously in a file.
- Selections are limited to 25K layers. If you exceed this, you’ll be prompted to reduce your selection.
- Swapping color styles isn’t currently supported. You can only bind a hard-coded color to a variable.

Once your design is ready, you can run **Check designs** to review and resolve suggestions.

To get started:

1. Select the layers you’d like to check.
2. Access **Check designs** from:
   - Right-click menu from a selection or frame
   - Click the **Ready for Dev** dropdown of a section on the canvas
   - Open the **Actions** menu in the bottom toolbar and search for **Check designs**
3. Run **Check designs**.

If the check results in suggestions that need to be reviewed, they will appear organized into four tabs:

- **Colors**: Hard-coded color values, contrast suggestions, and colors from libraries missing from the file or deselected in  Settings
- **Dimensions**: Hard-coded values like spacing, padding, and corner radius, as well as values from libraries missing from the file or deselected in  Settings
- **Typography**: Hard-coded font styles and sizes that can be replaced with text styles, along with values from libraries missing from the file or deselected in  Settings
- **Components**: Components detached from their source library, and those from libraries missing from the file or deselected in  Settings

![Check designs modal showing suggestions in the Colors tab](https://help.figma.com/hc/article_attachments/40896949842583)

## Review suggestions

Check designs opens to the first tab with violations and issues. At the top, you’ll see the total number of suggestions across all categories. Suggestions are based on values similar to a variable in your design system, or labeled as a **Match** when the value exactly matches an existing variable.

Click  **Check color contrast** to see if your design meets your accessibility standards. You can pick between AA and AAA contrast levels in the  Settings menu. 

## Preview changes

Click a row to recenter the canvas on the affected area. To preview changes on the canvas:

- Hover over a suggestion row to highlight affected layers in both the canvas and the **Layers** panel
- Hover over a suggested value in the right column to preview the change to the affected layer on the canvas
- Use the dropdown to select a different value

## Apply changes

You can apply suggestions in a few ways:

- **Apply all**: Apply all suggestions in the current view by clicking **Apply**
- **Apply a single change**: Select a row and click **Apply**
- **Apply multiple changes**:
  - `⌘Command` / `Control` + click to select multiple rows
  - `⇧Shift` + click to select a range
  - Group selections by clicking the section heading.

Click **Apply** once you’re ready.

## Undo changes

Press `⌘Command` / `Control` `Z` to undo changes.

Undo behaves like any on-canvas edit. Refresh the Check designs modal to ensure results are up to date.

## Adjust settings

Open the  **Settings** menu to:

- Show or hide row counts
- Choose which libraries to check against
- Select a **Contrast level** to use when contrast checks are enabled

## Adjust libraries

To update the libraries used for Check designs:

1. Open the  **Libraries** selector.
2. Select or unselect libraries for Check designs

Check designs will refresh to reflect your updated library selection.

[Learn how to add and remove libraries in a file](https://help.figma.com/hc/en-us/articles/1500008731201).

## Re-run Check designs

Use the  **Reload** button to re-run Check designs on a new selection. Once you’ve resolved all suggestions, each tab will show a completion state.
