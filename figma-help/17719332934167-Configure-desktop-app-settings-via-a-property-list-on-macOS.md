---
기술지원명: Configure desktop app settings via a property list on macOS
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Configure desktop app settings via a property list on macOS
출처링크: https://help.figma.com/hc/en-us/articles/17719332934167-Configure-desktop-app-settings-via-a-property-list-on-macOS
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

This article is for IT administrators configuring Figma on employee machines

You can configure some desktop app settings via a property list. If you are an administrator on the computer, you can use this method to prevent non-admin users from modifying these settings. The following settings can be configured via a property list:

|  |  |  |
| --- | --- | --- |
| **Key** | **Description** | **Value Type** |
| DisableUpdater | If true, automatic updates will be disabled | Boolean |
| AllowedOriginHosts | Domains that can be loaded within the Figma app | Array |
| ProxyUrl | If specified, all requests will be routed via this URL. http://, https://, ftp://, and socks:// schemes are accepted. For a direct connection, specify direct://. Advanced configuration options are available by using the `proxyRules` syntax documented [here](https://www.electronjs.org/docs/latest/api/structures/proxy-config). | String |

The **AllowedOriginHosts** setting is a list of non-Figma domains that can be loaded in the app. For example, if `https://*.example.com` is on the list, the app will allow redirects to URLs on any subdomain of example.com.

Configure these settings with a property list file during the `defaults` command. The app identifier for the Figma Desktop app is `com.figma.Desktop`. For more information on how to edit property lists, see [Edit property list in Terminal on Mac](https://support.apple.com/zh-sg/guide/terminal/apda49a1bb2-577e-4721-8f25-ffc0836f6997/mac) from Apple’s help documentation.

For example, use the command `defaults write com.figma.Desktop ProxyUrl "https://myproxy.com"`. This creates or updates a property list file at `~/Library/Preferences/com.figma.Desktop.plist`. Move this file to `/Library/Preferences/com.figma.Desktop.plist` to apply it to all users on a computer.
