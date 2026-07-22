---
기술지원명: Local network access in Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Local network access in Figma
출처링크: https://help.figma.com/hc/en-us/articles/34458998159511-Local-network-access-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Starting in Chrome 145, this permission name changed from **Local network access** to **Apps on device**. The feature works the same way in Figma, but if you previously allowed **Local network access**, you’ll need to allow **Apps on device** again.

New versions of some internet browsers implement **Local Network Access**, a security feature designed to protect you from attacks that target devices or services on your home or work network, like printers, routers, or apps running on your computer.

When it comes to Figma, the Local Network Access permission is required for a browser to work with certain Figma features, including [local fonts](https://help.figma.com/hc/en-us/articles/360039956894), some languages for [spell check](https://help.figma.com/hc/en-us/articles/27323589692055), and the ability to [open file links in the Figma Desktop app](https://help.figma.com/hc/en-us/articles/360039824334).

Many platforms including iOS, macOS, and Android already have a similar permission for local network access.

![An example of the Local Network Access prompt in Chrome, options to Block or Allow site to connect with devices on local network.](https://help.figma.com/hc/article_attachments/35286037521047)

If you choose to **Block** this permission, you can still use Figma on a web browser, but:

- Local fonts installed on your computer will not appear in your font picker
- Spell check may not work for some languages
- Clicking **Open in Desktop** will not work

Granting this permission only allows [figma.com](http://figma.com) to talk to Figma apps on your own computer. If you rely on local fonts, spell check, or quick file opening in Desktop, choose **Allow** when prompted for **Local Network Access** for `figma.com`. This is an expected and safe part of Chrome’s new security model.

As more browsers add support, Figma may prompt you to connect to the font installer on your computer. At this point, your browser will ask you to allow local network access.

Note: If you prefer not to grant this permission in Chrome, you can still use local fonts and spell check by using the [Figma Desktop app](https://www.figma.com/downloads/).

## Why Figma needs this permission

If you’ve installed the [Figma font installer](https://www.figma.com/downloads/) on your computer, `figma.com` uses it to provide extra features:

- **Local fonts**: use the fonts installed on your computer
- **Spell check:** supports more languages and uses your computer’s spell check
- **Open in Desktop:** open files directly in the Figma Desktop app

The Figma font installer, FigmaAgent, runs locally on your computer and communicates with `figma.com` over your local network. With Chrome’s new security model, this kind of public-to-local request is now allowed with a user permission prompt.

## Allow Local network access in Chrome

Chrome changed the name of this permission in version 145. Depending on your Chrome version, you may see a different label in the browser, but the effect in Figma is the same.

**In Chrome 142-144**

1. Open `figma.com` in Chrome.
2. Click the settings icon in the address bar.
3. Select **Site settings**.
4. Find **Local network access**.
5. Set it to **Allow**.
6. Refresh the page.

**Chrome 145 and later**

1. Open `figma.com` in Chrome.
2. Click the site settings icon in the address bar.
3. Select **Site settings**.
4. Find **Apps on device**.
5. Set it to **Allow**.
6. Refresh the page.
