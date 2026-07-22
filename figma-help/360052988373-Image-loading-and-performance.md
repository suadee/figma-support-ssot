---
기술지원명: Image loading and performance
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Image loading and performance
출처링크: https://help.figma.com/hc/en-us/articles/360052988373-Image-loading-and-performance
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

This article covers common image-related issues in Figma and how to fix them.

## Image resolution

Figma stores both high-resolution and low-resolution versions of your images. High-resolution images are images larger than 512 by 512 pixels.

Figma only downloads high quality versions of images in your current viewport. For images outside your current view, Figma loads a lower quality version. This improves performance when you first load a file.

If you have a lot of high-resolution images in a file, your images may look blurry at first. Figma will load high-resolution images as you explore the file.

Note: Because Figma only loads high quality versions of images in your current viewport, exporting content that includes images outside your current view may take longer than expected. This is due to Figma loading high-resolution versions of all images before exporting.

If you’re still seeing low-resolution images, you can try the following:

- Close and reopen the affected file
- Close any other Figma files
- Check your internet speed and connection to make sure your device is online
- **Using Figma in the browser:** quit your internet browser application, then relaunch it.
- **Using the desktop app:** right-click on the file’s tab and select **Reload Tab**.

## Incorrect image rotation

EXIF data (Exchangeable Image File Format) provides information on an image's characteristics such as orientation, size, device used to create the image, date, and more.

Before mid-2020, internet browsers didn't always check the orientation value in an image's EXIF data, including those taken on a mobile device. When this happened, Figma would automatically rotate images according to the EXIF data.

Now that most internet browsers check an image's EXIF data, images that were previously manually rotated in Figma may need to be corrected once more to account for this change in your browser's behavior.

![EXIF orientation examples showing 0-degree rotation on a vertical phone and 90-degree rotation on a horizontal phone.](https://help.figma.com/hc/article_attachments/360087072673)

### Example

1. You imported an image to a file in Figma. Your internet browser ignored the image's EXIF data, so Figma corrected the image's orientation for you.
2. In mid-2020, you updated your browser to a version with new EXIF data handling. Your images have now been rotated twice—once by the browser, then again by Figma—resulting in the wrong orientation.
3. Before October 2020, you manually rotated the image to the correct orientation.
4. In October 2020, Figma released an update to account for the new behavior by newer versions of internet browsers. Your image appears incorrectly rotated again.

Note: You only need to correct image rotation once if you encounter this issue. Going forward, your browser will set image orientation correctly using an image's EXIF data.

You may also need to [manually rotate an image](https://help.figma.com/hc/en-us/articles/360041098433-Adjust-the-properties-of-an-image#h_0845a776-edab-4717-af55-d7a7ce15bc27) if the thumbnail image appears incorrectly rotated while zooming, loading, or panning around a file.

## Images in prototypes not loading

There are two possible causes for images in prototypes not loading:

- Limited internet connection
- Blocked by a browser extension

![Flight booking prototype in Figma showing an error message at the bottom of the page about images failing to load.](https://help.figma.com/hc/article_attachments/360084246414)

### Limited internet connection

Images may fail to load if your device is experiencing a limited internet connection, or is offline. Confirm your device has a [reliable internet connection](https://help.figma.com/hc/en-us/articles/360040523973-Technical-Troubleshooting-Tips#%E2%9C%85_You_have_a_reliable_and_stable_internet_connection).

### Browser extensions

Browser extensions, such as ad blockers, can prevent images from loading in presentation view.

You can disable the browser extension, or add `figma.com` to the extension’s allow list. The process for this varies by extension, so make sure to reference the documentation for the relevant extension.

As of August 2020, the following extensions are known to block images in Presentation view:

- [Ghostery](https://www.ghostery.com/)
- [Video Downloader PLUS](https://paper.dropbox.com/ep/redirect/external-link?url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fvideo-downloader-plus%2Ffhplmmllnpjjlncfjpbbpjadoeijkogc%3Fhl%3Den&hmac=jCvPgSy6r1K39k6%2BgQx7TqhxNeI%2FgcnVmOa9%2Fy9qNkA%3D)
- [iDM Integration Extension](https://chromewebstore.google.com/detail/idm-integration-module/ngpampappnmepgilojfohadhhmbhlaek)
- [Honey](https://www.joinhoney.com/)
