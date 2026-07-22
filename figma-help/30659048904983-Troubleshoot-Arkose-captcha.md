---
기술지원명: Troubleshoot Arkose captcha
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Troubleshoot Arkose captcha
출처링크: https://help.figma.com/hc/en-us/articles/30659048904983-Troubleshoot-Arkose-captcha
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

In order to [create a Figma account](https://help.figma.com/hc/en-us/articles/360039811114), you will need to pass a captcha verification with Arkose. If your captcha verification fails to load, it's usually due to an issue with your browser or network settings.

## Common causes and solutions

### Unresponsive browser

- [Confirm you're using a supported browser](https://help.figma.com/hc/en-us/articles/360039827194-What-are-the-system-requirements-for-Figma)
- [Confirm your browser is up to date](https://help.figma.com/hc/en-us/articles/360040523973-Troubleshooting-checklist#h_01HHQKQKD0FE2ZHPH2SK1BP520)
- Quit and restart your browser
- Close any other Figma tabs you may have open
- Reload the page
- Clear your browser cache
- Try a different browser
- Turn off any ad blockers or browser extensions

### Weak or slow network connection

Your internet network may be weak or too slow to load Arkose captcha puzzles.

- Restart your internet network
- Try a different network
- [Adjust your network settings](https://help.figma.com/hc/en-us/articles/19424714305943)

### Necessary domains are being blocked

It's possible your access to necessary domains is being blocked by your organization or network admins.

- Talk to your organization's network admin to confirm Figma and Arkose domains are allowed
- Make sure `*.arkoselabs.com` and `verify.figma.com` domains are accessible in your network
- Confirm you can complete a demo verification puzzle on the [Arkose website](https://www.arkoselabs.com/arkose-matchkey/)

You can also visit the [Arkose status page](http://status.arkoselabs.com/) to confirm their service is active.
