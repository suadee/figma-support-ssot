---
기술지원명: Troubleshooting checklist
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Troubleshooting checklist
출처링크: https://help.figma.com/hc/en-us/articles/360040523973-Troubleshooting-checklist
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

As part of the troubleshooting process, Figma will need to confirm a few things about your setup. We've put together a list of common troubleshooting tasks you can try before reaching out to support.

## Try these quick fixes

Here are some actions you can take to improve performance and the resolve most issues:

- Close any Figma tabs you’re not using
- **Browser**: Force-quit and open Figma in a new browser window.
- **Desktop App:** Force-quit the Figma Desktop app and restart it.
- [Toggle off multiplayer cursors, layout guides, and effects](https://help.figma.com/hc/en-us/articles/360041065034#tt)
- Split up files to [reduce memory usage](https://help.figma.com/hc/en-us/articles/360040528173)
- [Clear desktop app cache →](https://help.figma.com/hc/en-us/articles/22380853110551)

## Confirm requirements to use Figma

The first step is to make sure your current setup meets Figma’s minimum requirements.

### Check your internet connection

Figma requires access to a reliable and stable internet connection. While there are [some activities you can do offline](https://help.figma.com/hc/en-us/articles/360040328553), Figma doesn't have a dedicated offline version or mode.

If your connection is unreliable, or you experience periods of limited bandwidth, your performance in Figma will be impacted. Some things you will experience are:

- Files loading slowly
- Low-resolution versions of images
- Lagging when panning and zooming in the Canvas

We're actively working on improving the Figma experience for low-bandwidth connections. Let us know by reaching out to the support team or [Submit a bug report](https://help.figma.com/hc/en-us/articles/360041468234).

### Check you're running the latest version of a supported browser and operating system

Figma only supports stable release versions of browsers, including Chrome, Firefox, and Safari. Figma doesn't support any developer, early-access, or beta versions of browsers.

If you’re running into issues, check that you are running the latest version of browser. Find out what browser and operating system version you're using via [What's my browser](https://www.whatsmybrowser.org/).

[What browsers does Figma support →](https://help.figma.com/hc/en-us/articles/360039827194-What-browsers-does-Figma-support-)

### Check Web GL is enabled and your graphics card is up to date

Figma is built using [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API). You will need to have this enabled to use Figma. You can check if your browser has this installed and enabled, by visiting this website: <https://webglreport.com/>

[Configure your browser for Figma →](https://help.figma.com/hc/en-us/articles/360039828614)

Note: If you have confirmed WebGL is enabled, there may be a Chrome extension blocking WebGL.

### Check you are running a 64-bit version of Windows

You must be running the Figma Desktop app in a **64-bit** environment. Figma isn't supported on machines running a 32-bit environment.

[What browsers does Figma support →](https://help.figma.com/hc/en-us/articles/360039827194-What-browsers-does-Figma-support-)

### Check you have enough available memory

Every browser has its own active memory limit. This can differ across devices, but the general understanding is there's an **active memory limit of 2GB** for each tab in a browser.

Figma measures your memory usage as a percentage of your available memory. To keep you informed of your memory usage, Figma displays banners and alerts at certain thresholds: 60%, 75%, and 100%.

If your file reaches `100%` of your memory limit, Figma will lock the file and inform you that there's no available memory. To access affected files, you will need to [reduce your memory usage →](https://help.figma.com/hc/en-us/articles/360040528173)

### Check your network settings

It’s not possible to access Figma through a VPN (Virtual Private Network) or proxy service. There are also some browser extensions that can cause issues when accessing Figma.

If you want to use Figma with a VPN or proxy, you can add Figma to your safe list.

There are a few error messages you may encounter with a VPN, proxy, or browser extension:

- [Server Connection 403 error →](https://help.figma.com/hc/en-us/articles/23347716725527)
- [Error 404 has occurred →](https://help.figma.com/hc/en-us/articles/23431834395671)
- [Zscaler has blocked your connection →](https://help.figma.com/hc/en-us/articles/23432055153175)

## Review common issues

Are you experiencing any of these common issues? Select an issue to view detailed troubleshooting steps.

[Memory →](https://help.figma.com/hc/en-us/articles/360040528173)

[Typography and fonts →](https://help.figma.com/hc/en-us/sections/19818416478487-Fonts)

[Low resolution or blurry images →](https://help.figma.com/hc/en-us/articles/360052988373)

## Contact our support team

If you're still encountering problems, Figma support will ask you to perform some diagnostic tests. We've put together step-by-step instructions for each of these tests:

- [Export console logs](https://help.figma.com/hc/en-us/articles/360041949073)
- [Export network logs](https://help.figma.com/hc/en-us/articles/360041949073)
- [Record a Chrome performance profile](https://help.figma.com/hc/en-us/articles/360041468414)
- [View your graphics card specifications](https://help.figma.com/hc/en-us/articles/360041948573)
- [Download Figma desktop app debug logs](https://help.figma.com/hc/en-us/articles/19589001018903-Download-Figma-desktop-app-debug-logs)

## Submit a bug report

If you're still experiencing problems, let us know! Check out the [Submit a bug report](https://help.figma.com/hc/en-us/articles/360041468234) article for more information on getting help.
