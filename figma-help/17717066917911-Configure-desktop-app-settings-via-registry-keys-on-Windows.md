---
기술지원명: Configure desktop app settings via registry keys on Windows
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Configure desktop app settings via registry keys on Windows
출처링크: https://help.figma.com/hc/en-us/articles/17717066917911-Configure-desktop-app-settings-via-registry-keys-on-Windows
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

This article is for IT administrators configuring Figma on employee machines

You can configure the following desktop app settings via registry keys on Windows:

|  |  |  |  |
| --- | --- | --- | --- |
| **Registry value** | **Description** | **Type** | **Value type** |
| DisableUpdater | If set to 1, the updater will be disabled | REG\_DWORD | Integer |
| AllowedOriginHosts | Domains that can be loaded within the Figma app, one per line | REG\_MULTI\_SZ | Multi-string value |
| ProxyUrl | If specified, all requests will be routed via this URL. http://, https://, ftp://, and socks:// schemes are accepted. For a direct connection, specify direct://. Advanced configuration options are available by using the proxyRules syntax documented [here](https://www.electronjs.org/docs/latest/api/structures/proxy-config). | REG\_SZ | String |

The AllowedOriginHosts setting is a list of non-Figma domains that can be loaded in the app. For example, if `https://*.example.com` is on the list, the app will allow redirects to URLs on any subdomain of example.com.

Figma’s keys are located in `HKEY_LOCAL_MACHINE\SOFTWARE\Figma`. Keys stored in the `HKEY_LOCAL_MACHINE` namespace apply to all users on a computer.
