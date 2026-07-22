---
기술지원명: Manage color profiles in design files
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage color profiles in design files
출처링크: https://help.figma.com/hc/en-us/articles/360039825114-Manage-color-profiles-in-design-files
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Available in Figma Design in the browser and on the desktop app

Requires can edit permission to the file

Different displays use different technologies to render color, which can lead to visual inconsistencies between the different devices, monitors, browsers, and applications. As a team grows, inconsistencies can also grow. 

With color management in Figma, you can:

- Maintain color consistency even if teammates have different displays
- Choose your preferred color profile for all newly created design files
- Change colors in a file from one color profile to another
- Export assets to a specific color profile

## Supported color profiles

In Figma Design, you can choose between two color profiles: sRGB and Display P3.

**sRGB** is the most widely used color profile. It has been the standard for web for a long time, and is supported by almost all web browsers and displays.

**Display P3**—also called **P3**—has more vibrant colors and represents 49% more visually distinct colors than sRGB. While not yet the standard for web and displays, it is growing in popularity. If you're building for iOS devices or retina screens, Display P3 is suited for those experiences.

![a graph showing the color gamuts of sRGB and Display P3, inner circle labelled sRGB, outer circle labeled Display P3 ](https://help.figma.com/hc/article_attachments/16433812072343)

Note: The image above represents the range of colors of sRGB and Display P3 in the Hue, Saturation, Brightness (HSB) space. [Learn more about color models →](https://help.figma.com/hc/en-us/articles/360043042113)

Saturation is represented on the radius, with less saturation toward the center and more saturation toward the outer edge. The area outside the sRGB circle means P3 can represent even more saturation than sRGB.

Brightness is pictured only at 100%, but both color profiles have full range of brightness.

For best results, make sure your display supports and is set to the selected color profile. For example, Display P3 colors won’t display properly on monitors that don’t support that profile.

FigJam boards are rendered in sRGB.

## Choose your preferred color profile

New design files are set to sRGB by default. To choose a different color profile for design files that you create:

1. Open any file you have access to.
2. Open the  Figma menu.
3. Go to **Preferences** > **Color profile**.
4. From the **Color profile settings** modal, choose **sRGB** or **Display p3**.
5. Click  to close the modal and save your settings.

## Change the color profile of a file

Color profiles can be changed at the file-level. When you change a file’s color profile, you have two choices:

- [Keep color values (Assign)](#h_01H6PW1X566917FS9HEBXRRQAZ) to change the appearance of colors, but not their values
- [Keep appearance (Convert)](#h_01H6PW23Z5NZV2XSSEJM4659R8) to change the values of colors, but not their appearance

Note: It’s not possible to change a color profile through [branching and merging](https://help.figma.com/hc/en-us/articles/360063144053). For example, if you convert a file from Display P3 to sRGB from a branch, merging the changes will change the color values, but not the color profile.

### Keep color values (Assign)

When you assign a color profile to a file, the colors visually change, but their underlying data—like hex codes or HSB values—stay the same.

You may choose to preserve color values when working with specific colors, like your brand colors. In this case, it’s more important that brand hex codes stay consistent across devices and files, even if the color appears slightly different.

![On the left is a title that says Keep color values (Assign). On the right are two circles with slightly different green colors, one labelled Display P3, one labelled sRGB. Both circles labelled with the same hex code #00A010](https://help.figma.com/hc/article_attachments/16435210472343)

To assign a color profile to a file:

1. With the file open, click  next to the file name.
2. Go to **File color profile** > **Change to Display P3** or **Change to sRGB**.
3. From the modal, choose **Keep color values (Assign)**.
4. To save your changes, click **Assign Display P3** or **Assign sRGB**.

### Keep appearance (Convert)

When you convert a file to a different color profile, the colors' underlying data changes, but will look the same or as similar as possible.

You may choose to preserve the appearance of colors if you’re focused on brainstorming, wireframing, or testing how colors appear on different devices. In these cases, a consistent appearance is more important than maintaining a system. ![On the left is a title that says Keep appearance (Convert). On the right are two pink circles with the same color, one labelled Display P3 with hex code #FF0B71, one labelled sRGB with hex code #FF0070.](https://help.figma.com/hc/article_attachments/16435210474263)

Before you convert, keep in mind:

- Converting a file to a previously used color profile might not revert colors back to their original before values
- Because sRGB has a smaller range of colors, converting a file from Display P3 to sRGB may "clip" some colors by finding the closest approximate color

To convert a file to a different color profile:

1. With the file open, click  next to the file name.
2. Go to **File color profile** > **Change to Display P3** or **Change to sRGB**.
3. From the modal, choose **Keep appearance (Convert)**.
4. To save your changes, click **Convert to Display P3** or **Convert to sRGB**.

Color styles and color variables are unaffected by converting, so their color values won't change.

### Undo a color profile change

To undo a color profile change to a file, choose one of the following:

- Use keyboard shortcuts `⌘ Command` / `Control` `Z`
- Select an earlier version in [version history](https://help.figma.com/hc/en-us/articles/360038006754)

Note: Version history logs activity for color profile changes and the profile it was changed to, but it doesn't log whether it was assigned or converted. You can edit the version info to add this detail.

## Assign a color profile to a legacy file

The **Unmanaged** setting is no longer available starting August 2023. Previous design files set to unmanaged won’t have a specified color profile and will be set to be **Same as preferred profile (preferred color profile)**. If you don't have a preferred color profile set, then this legacy file will render in sRGB.

To assign a color profile to a legacy file:

1. With the file open, click  next to the file name.
2. Go to **File color profile** > **Assign to sRGB** or **Assign to Display P3**.

Once you assign a color profile, you’ll gain access to convert the file to a different color profile, but you won’t be able to revert to the **Same as preferred profile** setting.

## Export assets

By default, Figma exports assets using the color profile of the file. However, you can choose a different color profile when exporting. [Learn how to export assets in a color profile →](https://help.figma.com/hc/en-us/articles/13402894554519#Color_profile)
