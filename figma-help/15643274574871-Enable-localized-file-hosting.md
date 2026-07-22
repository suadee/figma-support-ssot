---
기술지원명: Enable localized file hosting
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Enable localized file hosting
출처링크: https://help.figma.com/hc/en-us/articles/15643274574871-Enable-localized-file-hosting
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

Organization admins only

To enable international customers to have greater control over where their Figma data is stored, organizations on Figma’s Enterprise plan can host key parts of their Figma content in a local data center, as described below (the “**Figma Data Residency Solution**”).

## Who can use this plan?

The Figma Data Residency Solution is only available to customers on the Figma Enterprise plan.

## Where can you host your Figma data?

You can host your relevant Figma data locally in the following regions: EU, Australia (from Q1 2026) and India (from Q1 2026).

## Which Data Center provider does Figma use?

Figma’s Data Residency Solution is hosted on AWS Data Centers, no matter which region is chosen.

|  |  |  |
| --- | --- | --- |
| **Region** | **Primary** | **Data Recovery** |
| US | us-west-2 | us-east-1 |
| EU | eu-central-1 | eu-west-1 |
| Australia | ap-southeast-2 | ap-southeast-4 |
| India | ap-south-1 | ap-south-2 |

## What types of Figma data can be hosted locally?

Figma can localize the following parts of your Figma Design, FigJam, Figma Slides, Figma Draw, Figma Buzz and Figma Make files:

| File data type | Localized |
| --- | --- |
| Shapes | Yes |
| Text boxes | Yes, except @mentions which are not localized |
| Sticky notes | Yes, except @mentions which are not localized |
| Stamps | Yes |
| Frames | Yes |
| Components | Yes |
| Images | Yes |
| Videos | Yes |
| Comments | No |
| Plugins | No |
| File names | No |
| Fonts | No |
| File preview thumbnails | No |
| Dev Mode / Code Connect code - inspect panel | No |
| AI chats | No |

## What about non-file data?

- Data that lives outside of Figma files, such as billing information, metadata, activity & security logs, indexed data for file search, Figma Community assets, user profile data, and any other data types not listed in the table above are not included in Figma’s Data Residency Solution.
- Figma’s Data Residency Solution only applies to data at-rest, not data in-transit.

## What about AI-generated file data?

The method of generating file content does not impact its storage location. AI Output will also be stored in accordance with the organization's data storage localization configuration and, if localized, in accordance with the table above. Note that any part of a Figma file that is published (see "Published data") will not be localized and is hosted in the US.

**Published data** (websites, apps, blogs etc.): Any file data that is published or generally made available via the internet is currently outside the scope of Figma’s Data Residency Solution.

## How can I see my data storage localization location?

You can check where your data is localized from the Admin dashboard in Figma:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click  **Admin**
2. Click the **Settings** tab
3. In the **Data** section, navigate to **Data storage localization**.

To change the storage location for your organization, reach out to our [support team](https://help.figma.com/hc/en-us/requests/new?ticket_form_id=360001731233).
