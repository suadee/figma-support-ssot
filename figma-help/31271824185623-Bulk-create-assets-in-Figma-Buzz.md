---
기술지원명: Bulk create assets in Figma Buzz
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Bulk create assets in Figma Buzz
출처링크: https://help.figma.com/hc/en-us/articles/31271824185623-Bulk-create-assets-in-Figma-Buzz
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

While in beta, Figma Buzz is available on all seats and plans

Anyone with `can edit` permissions in a file can bulk create assets

Use  **Bulk create** to create multiple assets at once. You can import content from a CSV or XLSX file to populate individual fields within each asset.

Use bulk create to help you:

- Batch asset creation for events, products, or campaigns
- Create personalized assets, such as greeting cards or invitations
- Localize or translate content in bulk

To use bulk create, start with a single asset as your starting point. You can then import content from a CSV or XLSX file to update text and image fields within each asset in bulk.

## Prepare your data file

Before you upload, format your spreadsheet so Figma Buzz can read it correctly.

Bulk create supports comma separated value (CSV) and Microsoft Excel Spreadsheet (XLSX) file formats. Structure your file like this:

- The first row is the header row. Each column header should describe the content (for example: "Headline", "Date", "Image").
- Each subsequent row represents one asset that will be created.

You have a few options for adding images to your bulk-created assets:

- **Embed images directly in cells:** Only supported in XLSX files. Place the image inside the cell in your spreadsheet before uploading.
- **Use an image URL:** Paste a direct link to any publicly accessible image into the cell. Works in both CSV and XLSX.
- **Use a Google Drive URL:** Paste a shareable Google Drive link to an image file into the cell. Works in both CSV and XLSX.

Tip: Most common spreadsheet programs, such as Google Sheets or Numbers, allow you to download spreadsheets in CSV or XLSX format.

Use the table below as an example of how to format your file. In this example, there are two text fields (”Name” and “Job title”) and one image (”Headshot”) that will be mapped to the Figma Buzz asset. Since there are four rows of items beneath the labels, four assets will be created.

| Name | Job title | Headshot |
| --- | --- | --- |
| Jules | Entrepreneur | https://example.com/headshot1.jpg |
| Jesse | Dancer | https://example.com/headshot2.jpg |
| John | Analyst | https://example.com/headshot3.jpg |
| Billie Jean | CEO | https://example.com/headshot4.jpg |

**Note**: You can only connect only one data field per object, so format your data to align with the individual objects in the asset. For example, if the asset has a single text object that includes both a first and last name, you don’t need two separate columns for “First Name” and “Last Name”—your spreadsheet should only have one column for “Name”.

## Upload your data

Once you’ve formatted your data for importing, you can upload it to your Buzz file to bulk create assets.

Note: If you want to bulk resize an asset, without changing any of the content itself, check out [Resize assets in Figma Buzz](https://help.figma.com/hc/en-us/articles/34324344840855).

1. [Create or select a single asset](https://help.figma.com/hc/articles/31271664997911) in your Figma Buzz file.
2. Click  **Bulk create** from the left navigation bar.
3. Click **Upload spreadsheet**.
4. Select a CSV or XLSX file from your device.
5. Select piece of text or image on your asset, then select the corresponding data field from the left sidebar. You can only link text fields with text, and image fields with images. Once an object is linked to a data field, the data field will be marked with a  check and highlighted pink. You can also click  from the selected object’s toolbar and **Select matching objects** to connect multiple of the same object type across multiple asset sizes.
6. Repeat step 5 for each object you’d like to update.
7. Click **Create assets**.

![Click Bulk edit from left navigation bar, then Upload spreadsheet.](https://help.figma.com/hc/article_attachments/40665397834903)

Note: If you’re working from a template, you won’t be able to select any locked objects. To use locked objects in bulk create, first [remove editing restrictions](https://help.figma.com/hc/articles/31271689852823) from the template.

New assets will be created after the selected asset. To view all new assets, navigate to  **Grid view**.

##
