---
기술지원명: Zeroheight and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Zeroheight and Figma
출처링크: https://help.figma.com/hc/en-us/articles/360039829314-Zeroheight-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

[zeroheight](https://www.zeroheight.com/) allows you to keep your design system resources in one place. Use zeroheight to:

- Establish and outline the principles of your design system.
- Craft and maintain living style guides.
- Document your Styles and Components and educate Team Members on how to use them.
- Collate related resources in one place.

Connect zeroheight to Figma, to share your Styles and Components. This allows you to view your Figma Styles and Components alongside your other design system resources.

You will need to create an account with zeroheight first: [Sign up for a zeroheight account](https://zeroheight.com/create/account). Learn more about zeroheight on their website: <https://zeroheight.com/>

# Allow zeroheight to access your Figma account

You will need to give zeroheight **read-only** access to your Figma account. This allows zeroheight to access the Figma API on your behalf.

Once you've signed up for a zeroheight account:

1. Login to your zeroheight account.
2. Head to the **Uploads Dashboard**: ![zeroheight interface showing the selected "Uploads" tab for managing Figma file uploads.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458a80428631d263c1fb3/file-ygnE4ucDnj.png)
3. Click the **Add New Upload** button: ![Uploads dashboard in zeroheight with an "Add new upload" button highlighted, prompting integration of design files.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458c80428631d263c1fb5/file-37fMEv9HsO.png)
4. Click the **Upload** button next to the Figma icon:![Add new upload dialog in zeroheight showing options to upload from Sketch or Figma, with Figma selected.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458cd2c7d3a0e059ccd4c/file-whOgwJKt0G.png)
5. You'll need to allow zeroheight to access your Figma account. This will prompt you to login to your Figma account and grant access. Click **Authorize** to proceed: ![Prompt in zeroheight asking for read-only access to Figma files with an "Authorize" button.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458d72c7d3a0e059ccd4d/file-EK5caCUmXh.png)
6. Sign in to your Figma account and click **Allow access**:![zeroheight integration requesting read-only access to a Figma account, with an "Allow Access" button.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458dd0428631d263c1fb7/file-SOPha6qtws.png)

# Share Figma Files with zeroheight

To open a Figma File in zeroheight, you will need to share the File's URL. This allows zeroheight to access any Styles or Components within that specific File.

It doesn't matter if the File has *View* or *Edit* access. zeroheight will only need to *view* the File to access any Styles or Components.

Note: Due to the Figma API, zeroheight can only import Styles that you have applied to Layers in that File. If you're missing any Styles, you can apply these to a Layer in the original File.

## Copy the Figma File link

You will need to copy the File URL from Figma. There are a couple of places you can find the File URL.

- From the URL in the browser: Copy the File's URL in the browser window: ![Figma interface showing a design system file URL highlighted in the browser address bar for sharing with zeroheight.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb45a960428631d263c1fe6/file-4bp0S7EUaa.png)
- From the File's **Share** modal:
  - Click **Share** on the File
  - Use the **Copy link** button to copy the URL to your clipboard: ![Figma share modal with user access settings, copy link option highlighted; facilitates sharing Figma file URL.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d4ab8a30428635a6ec8a11d/file-eYBNkvBdbj.png)

## Share the link with zeroheight

When you first connect to zeroheight, you can add a Figma File link: ![Input field in zeroheight for pasting a Figma file share link with an "Add file" button.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458f10428631d263c1fba/file-otoGrtIeYV.png)

Access this screen again by clicking the **Add new upload** link in the **Uploads** tab:

1. Go to the **Upoads** tab:![zeroheight dashboard with "Uploads" tab active, ready to manage Figma file uploads.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458a80428631d263c1fb3/file-ygnE4ucDnj.png)
2. Click the **Add new upload** link: ![Uploads dashboard in zeroheight with an "Add new upload" button highlighted for integrating design files.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb458c80428631d263c1fb5/file-37fMEv9HsO.png)
3. Paste the Figma link in the field provided: Click **Add file** to add the File to zeroheight: ![Add Figma file dialog in zeroheight, with a file share link input and "Add file" button highlighted.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb4592a2c7d3a0e059ccd4e/file-hHPDrBtJkW.png)
4. zeroheight will download the Figma File to your account: ![Uploading dialog showing progress of fetching a file from Figma in zeroheight's Uploads interface.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb4593a0428631d263c1fbe/file-ZT1b8kHkPX.png)
5. The File will now show up in the **Uploads** dashboard:![Uploads dashboard showing Figma file "Design System Styles" added with components, text styles, frames, and colors.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb4593f0428631d263c1fbf/file-BhBV7iZPdd.png)

# Add Styles and Components to your Style Guides

Insert any Figma Styles and Components into your Styleguides in zeroheight.

1. Go to the **styleguides** tab in zeroheight: ![zeroheight interface showing the "Styleguides" tab selected, highlighting the section for managing design style guides.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459440428631d263c1fc3/file-yWDgcNXzsn.png)
2. Select the Styleguide from the list:![Styleguides tab in zeroheight displaying a "Figma Help Center" style guide, ready for managing design system resources.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459532c7d3a0e059ccd50/file-koRUsHfYDk.png)  

   Note: If you haven't created a Styleguide yet, click the **Create styleguide** button to add a new one:![Welcome screen for creating a style guide in Zeroheight, featuring a "Create styleguide" button.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459490428631d263c1fc5/file-5IsVKykZLj.png)
3. Select the page you'd like to add your Figma content to.
4. Click on the design block to add content to your page: ![UI showing where to add design components and styles for primary and secondary colors in zeroheight.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb4595e0428631d263c1fc7/file-vCORLvgOvZ.png)
5. If you're adding this to an existing list of Styles or Components, click the **Add** block:![Neutral color palette with hex and RGB values, option to add additional color swatches.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459940428631d263c1fcd/file-ZR7tNeMVCW.png)
6. You'll see the Figma file in the browser on the left: ![Adding design uploads panel showing color styles list with options to select and apply in zeroheight.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459682c7d3a0e059ccd51/file-UDrCpN46Up.png)
7. Click the checkbox next to an individual Style or Component to select it:![Selecting color styles for upload in zeroheight, showing a checklist of color hex codes with an 'Add' button.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459740428631d263c1fc8/file-9nkwD4W0Ut.png)
8. Or use the checkbox at the top of the select all Styles or Components in the list:![Adding design uploads panel in zeroheight showing color styles from Figma with selection checkboxes.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb4597a0428631d263c1fc9/file-70G8rjI003.png)
9. Click the **Add** button to add them to the page: ![Design uploads window showing Figma color styles being added to zeroheight, with the "Add" button highlighted.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459a20428631d263c1fcf/file-0htuigNcl2.png)
10. You can then click-and-drag to rearrange:![Primary color swatches with HEX and RGB values, featuring green, blue, purple, red, orange, and yellow.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459a60428631d263c1fd0/file-c91Vnrjl9D.png)

### Made Changes to your Figma Files?

If you have made a change to any Styles or Components in Figma, you will need to update the File in zeroheight.

1. In zeroheight, open the **Uploads** Dashboard.
2. Click the *Update File* icon: ![Uploads dashboard in zeroheight showing "Design System Styles" file with options to update or delete.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb459ac2c7d3a0e059ccd55/file-wD4fcpqhdf.png)
3. Updates are then applied to any Styles and Components in zeroheight.

# Disconnect zeroheight from Figma

If you want to remove the zeroheight integration, or remove access, you can remove it from your **Connected Apps** section:

1. Open Figma and go to your **Account Settings**: ![Dropdown highlighting "Account Settings" under user profile in Figma.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb465eb0428631d263c20dd/file-3ZrbkKrIEL.png)
2. Find the **Connected Apps** section.
3. Click the **Revoke access** link next to the zeroheight application:![Connected Apps section in Figma settings showing zeroheight app with option to revoke access.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5cb465f00428631d263c20de/file-mOVu8CnC5k.png)

If you have any questions or issues with using Figma and zeroheight, [please reach out to the Zeroheight Team!](mailto:support@zeroheight.com)
