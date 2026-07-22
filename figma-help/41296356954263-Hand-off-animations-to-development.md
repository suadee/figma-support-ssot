---
기술지원명: Hand off animations to development
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Hand off animations to development
출처링크: https://help.figma.com/hc/en-us/articles/41296356954263-Hand-off-animations-to-development
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Figma Motion is currently in open beta.** Features may change and you may experience performance issues as we continue to improve Figma Motion. Learn more about [what's included in the beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

Before you Start

Who can use this feature

Available on all paid plans

Requires a [Full](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor) or a [Dev seat](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-GA-for-admins#h_01HKN19J4JJTKGMATHW6BP331A)

After building animations in Figma Motion, developers can use Dev Mode and the Figma MCP server to inspect animation details and implement them accurately.

## Dev Mode

To inspect an animation in Dev Mode:

1. Select the animated frame.
2. Open the **Motion** tab in the Inspect panel.
3. Click **Show in timeline view**.

![rectangle_animate.gif](https://help.figma.com/hc/article_attachments/41434755851671)

Timeline view provides a read-only view of the animation alongside the code used to recreate it.

To copy the animation code:

1. Select **Code** under the **Motion** tab in the Inspect panel.
2. By default, code is displayed as **CSS**. Use the format selector to switch between **CSS**, **React**, and **JSON** outputs.
3. Click **Copy** to copy the generated code.

## MCP integration

Figma Motion is compatible with the MCP server.

In Dev Mode, **MCP** details appear in the Inspect panel. Copy the frame link and provide it to your coding agent. The MCP server supplies the full animation context, including:

- Keyframes
- Motion type
- Timing values
- Easing curves

This allows coding agents to generate implementations that closely match the original animation.
