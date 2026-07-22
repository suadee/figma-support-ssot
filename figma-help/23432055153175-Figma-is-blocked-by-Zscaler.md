---
기술지원명: Figma is blocked by Zscaler
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Figma is blocked by Zscaler
출처링크: https://help.figma.com/hc/en-us/articles/23432055153175-Figma-is-blocked-by-Zscaler
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

When accessing the [Figma desktop app](https://help.figma.com/hc/en-us/articles/5601429983767) using a proxy like Zscaler, you may encounter the error **Blocked navigation to gateway.zscloud.net** (or some other Zscaler-specific domain).

The Figma desktop app allows you to safe-list non-Figma origins used by the Zscaler ZIA proxy service to get everything to load within the desktop app. We recommend reaching out to your IT admin to confirm and safe-list the Zscaler ZIA domains in Figma.

You will need to configure the **AllowedOriginHosts** setting to reflect the domain(s) appropriate for your Zscaler ZIA configuration. Commonly the two values will be `https://*.zscloud.net` and `https://gateway.zscaler.net`. See the linked articles below for more information on how to set those values.

For more information, see the following articles:

- **Mac:**[Configure desktop app settings via a property list on macOS](https://help.figma.com/hc/en-us/articles/17719332934167-Configure-desktop-app-settings-via-a-property-list-on-macOS)
- **Windows:**[Configure desktop app settings via registry keys on Windows](https://help.figma.com/hc/en-us/articles/17717066917911)
