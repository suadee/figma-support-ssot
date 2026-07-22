---
기술지원명: Uninstall the Figma font helper
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Uninstall the Figma font helper
출처링크: https://help.figma.com/hc/en-us/articles/19764441960599-Uninstall-the-Figma-font-helper
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

To remove the [font helper](https://help.figma.com/hc/en-us/articles/360039956894) from your computer, you need to run the uninstaller.

### Windows

Depending on when you installed Figma, your font helper may be called one of the following:

- Figma Service
- Figma Font Helper
- Figma Agent

Uninstall any of the above programs from the programs section of the Windows Control Panel:

1. Open the Windows Control Panel
2. Select **Programs > Programs and Features**.
3. Right-click the program and select **Uninstall**. Follow the directions on the screen.

### Mac

1. Open **Terminal.app**
2. Paste in the following command:

   ```
   /bin/bash -c "$(curl -fsSL https://desktop.figma.com/agent/mac/uninstall.sh)"
   ```

**Font missing or running into other font issues?** [Troubleshoot common font issues →](https://help.figma.com/hc/en-us/articles/4403018301079)
