---
기술지원명: What are the system requirements for Figma?
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: What are the system requirements for Figma?
출처링크: https://help.figma.com/hc/en-us/articles/360039827194-What-are-the-system-requirements-for-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma is predominantly browser-based software, which means it can be run on all full desktop operating systems (such as macOS, Windows, or Linux), as well as ChromeOS .

Figma also has [desktop applications](https://www.figma.com/downloads/) available for both macOS and Windows. [Learn more about the requirements of using Figma's Desktop Apps](https://help.figma.com/hc/en-us/articles/5601429983767). The requirements for the desktop application are generally the same with regard to WebGL and graphics cards.

For live device previewing, you can also download the [Figma mobile app](https://help.figma.com/hc/en-us/articles/1500007537281), which is available on both iOS and Android devices.

**Having trouble?**Try updating to the latest version of your browser. We recommend enabling automatic updates to stay up-to-date.

## Browsers and operating systems

Figma uses [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) (Web Graphics Library) to handle rendering. This has very low graphical requirements which means it runs well on most browsers.

The WebGL browser support requirements are:

- Minimum version: WebGL 1.0
- Minimum version for [shaders](https://help.figma.com/hc/articles/41147702210071/) support: WebGPU (cannot be in compatibility mode)

The minimum browser requirements are:

- Chrome 99 or later (minimum 113 for shaders)
- Firefox 101 or later (minimum 141 for shaders)
- Safari 16 or later (minimum 26 for shaders)
- Microsoft Edge 121 or later

Note: To use Figma on Microsoft Edge, you'll need to make sure the **Strict mode** privacy setting is disabled for `Figma.com`. Visit [Microsoft's help center](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-security-browse-safer) for information.

The minimum operating system (OS) requirements are:

- Windows 8.1 or later
- macOS 11 or later
- Any Linux OS that supports the browsers mentioned above
- Any Chrome OS that supports the browsers mentioned above

**Tip:** You can find out what browser and operating system version you're using via [What's my Browser](https://www.whatsmybrowser.org/).

## Graphics cards

On Windows and Linux, OS and device driver updates are often required to keep performance optimal. On macOS, any OS releases will update Safari and provide any bug fixes related to WebGL.

While Figma doesn’t restrict the use of specific graphics cards, individual browser support may prevent you from using Figma on a specific browser. We recommend using the minimum operating system requirements as a guide instead.

## Integrated and dedicated graphics cards

Some newer laptops will have both a dedicated card (Nvidia or AMD) and an integrated graphical processor (Intel or AMD).

If you have a dual-GPU laptop, you can choose to use the dedicated GPU over the integrated GPU. This will result in improved performance in Figma, but will increase your battery consumption.

Figma is unable to provide support or troubleshooting around dedicated graphics cards. For help with using a dedicated GPU, we recommend the following resources:

- **macOS:** Apple provides the following information around using a dedicated GPU:
  - [Find out which graphics processor is in use on your MacBook Pro](https://support.apple.com/en-us/HT202053)
  - [Set graphics performance on MacBook Pro](https://support.apple.com/en-us/HT202043) (Disable Automatic switching)
  - Other Figma users have had success with [gfxcardstatus app](https://gfx.io/), which allows you to switch between dedicated and integrated GPU. gfxCardStatus card is not endorsed by Figma.
- **Windows** **(Nvidia):** In the Nvidia control panel set `chrome.exe` to use discrete graphics card.
- **Windows (AMD):** In the AMD control panel set `chrome.exe` to use discrete graphics card.

## Unsupported graphics cards

The following GPUs have known bugs and may cause rendering glitches when using Figma. Behavior with these GPUs may vary from browser to browser:

- Intel HD Graphics 3000

## Virtual desktops

As Figma relies on [graphics cards](#graphics) to keep performance optimal, using Figma with virtual desktop infrastructure (VDI) such as Citrix or VMware can result in sub-optimal performance. Generally, this is because VDI can be provisioned without additional graphics card support.

When possible, we recommend using Figma on devices that offer a full desktop operating system with a graphics card. This includes macOS, Windows, and ChromeOS, and applies to both the Figma web and desktop app. To enhance the virtualized performance of Figma, consider assigning a graphics card to the virtual machine where Figma is being used.

## Mobile requirements

When you’re using Figma on a mobile device, you can only access a **View Only** version of Figma files. Tablets that run a full desktop OS, like Microsoft Surface or an Apple iPad, support viewing Figma Design files and editing FigJam files.

For viewing Figma files or prototypes on a mobile phone, we recommend using the [Figma mobile app](https://help.figma.com/hc/en-us/articles/1500007537281).

You can also view prototypes on a mobile browser. To do so, open a prototyping link on your mobile device. Keep in mind that the browser address bar may obstruct or prevent some actions.

The minimum requirements to view Figma files on mobile browsers are:

- **iOS:** Safari on devices with iOS 11.4 or later
- **Android:** Chrome on devices with Android 7 or later

Note: The file browser is no longer supported on mobile phone web browsers (such as Chrome or Safari). You can still access the file browser using web browsers on a tablet.
