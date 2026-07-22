---
기술지원명: Adjust your network settings
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Adjust your network settings
출처링크: https://help.figma.com/hc/en-us/articles/19424714305943-Adjust-your-network-settings
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

When configuring Figma for your company, we recommend adding the following domains to your network's allowlist for GET requests, POST requests, and the remote Figma MCP server:

- `*.figma.com`
- `*.figma.site`
- `*.makeproxy-c.figma.site`
- `*.makeproxy-m.figma.site`
- `*awswaf.com`
- `esm.sh`
- `jsdelivr.net`
- `figma.app`

For those on the Figma for Government solution, we recommend adding the following domains:

- `*.figma-gov.com`
- `*.figma-gov.site`
- `*.makeproxy-c.figma-gov.site`
- `*awswaf.com`
- `esm.sh`
- `jsdelivr.net`

In addition to these domains, there may be other domains that must be added to the allowlist to perform certain actions in Figma. If a required domain is not on the allowlist, users may receive an error when attempting to perform the following actions:

- [Publishing a library](https://help.figma.com/hc/en-us/articles/360025508373-Publish-a-library)
- [Adding media to comments](https://help.figma.com/hc/en-us/articles/360041068574#h_01HEBETCZN3S7DRZNVESSABAG9)
- [Importing content](https://help.figma.com/hc/en-us/articles/360040027794-Imports-in-Figma-design)

## Recognize when network traffic is blocked

In addition to error messages, network issues typically show up in two ways:

- **Entire** `figma.com` **domain blocked:** The homepage is blank or never finishes loading (including sign-in).
- **WebSocket connections blocked:** The homepage loads, but **Recent**, **Drafts**, team and file lists stay empty; thumbnails and other data don’t appear.

While these symptoms can look like a service outage, they usually point to a local proxy, firewall, or VPN rule.

## Check your network settings

You can open the **Network settings** modal in two ways to check your settings and see any blocked actions or issues:

### From an error message

If you see an error while performing an action in Figma, select **View settings** in the message to open the **Network settings** modal and see which actions are blocked.

![Publishing error message (1) (1).png](https://help.figma.com/hc/article_attachments/20991069393815)

### From within a file

The **Check network settings** [quick action](https://help.figma.com/hc/en-us/articles/360040328653-Use-shortcuts-and-quick-actions#Quick_actions) is only available from within a file canvas, not the homepage. If your homepage looks blank or doesn’t show files, use one of these entry paths to open a file first:

- Open a file directly from a shared link
- Create a new Design or FigJam file
- Try the desktop app if your browser homepage is blocked

Once you’re in a Design or FigJam file:

1. Use the keyboard shortcut to access the quick action bar:
   - **Mac:** `⌘ Command` or `⌘ Command` `P`
   - **Windows:** `Control` `/` or `Control` `P`
2. Type "Check network settings" in the quick action bar.
3. Press `Return` or `Enter` to perform the quick action.

If network issues are found, the **Network settings** modal will display them.

![Image of the network settings modal showing domain access for publishing allowed, and media/comment actions blocked.](https://help.figma.com/hc/article_attachments/20991072260247)

## Configure a proxy bypass on macOS

If you’re on a Mac behind a proxy, try adding a bypass for Figma domains:

1. Open **System Settings** → **Network** → select your active network → **Details** → **Proxies**.
2. Add `.figma.com` under **Bypass proxy settings**.
3. Apply changes, then restart your browser or the Figma desktop app.

[Learn more about changing proxy settings on Mac →](https://support.apple.com/guide/mac-help/change-proxy-settings-on-mac-mchlp2591/mac)

**Note:** If your Mac is managed with MDM, some network settings may be locked and you may need your IT admin to add this bypass.
