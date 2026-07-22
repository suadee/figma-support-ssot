---
기술지원명: Deploy Figma on macOS
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Deploy Figma on macOS
출처링크: https://help.figma.com/hc/en-us/articles/1500012289622-Deploy-Figma-on-macOS
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

This article is for IT administrators installing Figma on employee machines.

To install Figma on your own device, please visit [Figma's downloads page](https://www.figma.com/downloads/). [Learn more about the Figma desktop app](https://help.figma.com/hc/en-us/articles/360039823654) [→](https://help.figma.com/hc/en-us/articles/360039823654)

Organization admins on the Enterprise plan can use the macOS Enterprise installer to deploy the Figma Desktop package to multipe macOS computers simultaneously. Learn more about the [macOS Enterprise installer →](https://help.figma.com/hc/en-us/articles/17686512113175)

## Install directory

- `/Applications` for system wide installation. All users will have access to Figma.
- `~/Applications` for a single user installation.

### Auto-update policy

If you install to `~/Applications`, users should be able to auto-update to the Figma app without needing special permissions. If you install to `/Applications`, users need to have write access to the Figma.app bundle directory for auto-updates.

We recommend creating a permission group containing all relevant users and then making app directory writable by that group.

For example: if you were to have a group called `figma_group`, you could use:

```
chown -R :figma_group /Applications/Figma.app && chmod -R 755 /Applications/Figma.app
```

## Choose a deploy method

You have two options for deployment:

- If you allow write access to the Figma.app bundle, you can use the **universal stub installer**
- If you don't allow write access, you can download **architecture specific builds**

### Universal stub installer

The universal stub installer supports both Intel and Apple Silicon machines. Place the stub installer Figma.app in the Applications directory and it will automatically download and install the latest version of Figma on first launch.

Download here: <https://desktop.figma.com/mac-installer/Figma.zip>

### Architecture specific builds

If you don't allow write access to the Figma.app bundle, or can't use the stub installer for any reason, you can fetch architecture-specific builds instead.

Here is the shell script to obtain the URLs:

```
latest_version=$(curl -fsSL "https://desktop.figma.com/mac/version.txt")  
intel_url="https://desktop.figma.com/mac/Figma-${latest_version}.zip"  
apple_silicon_url="https://desktop.figma.com/mac-arm/Figma-${latest_version}.zip"
```

The Figma app will not try to auto-update if the app directory is unwritable by the user. In this case, please note that we support desktop app versions only for up to two months. You must make sure to manually deploy updates to users in a timely manner. You can check the latest available version of the desktop app from [version.txt](https://desktop.figma.com/mac/version.txt).
