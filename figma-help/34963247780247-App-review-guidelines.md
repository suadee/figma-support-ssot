---
기술지원명: App review guidelines
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: App review guidelines
출처링크: https://help.figma.com/hc/en-us/articles/34963247780247-App-review-guidelines
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Caution:** This is an evolving document, so its contents may change over time. If you have any questions or concerns around our review guidelines, please [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new).

Figma is committed to offering developer resources to allow developers to build and publish amazing apps that extend the value of Figma, also known as "**Figma Community Apps**." Before a Figma Community App may be used outside of the team or org where it was registered, it needs to go through our review process. (For clarity, these guidelines do not apply to private apps authored and used by a single Figma customer.)

To make the review process as seamless as possible, we have created a set of guidelines to give you an idea of the criteria we review when assessing Figma Community Apps, outlined below. Please note, these guidelines are not exhaustive.

## Before you submit

When you are ready to submit, please make sure you have done the following:

- Tested your Figma Community App thoroughly with a variety of scenarios and confirmed it’s free of bugs.
- Reviewed the guidelines outlined below.
- Established a way for users to contact you for support. It's your responsibility to provide support for your Figma Community App users. For example, you can provide them with an email address or a link to a website or help center.
- Reviewed and understand your obligations under our [Developer Terms](https://www.figma.com/legal/developer-terms/).
- Consulted legal counsel to understand your legal obligations, and prepared necessary documents (like a privacy policy).

## What to expect

Our goal is to be thoughtful and reasonably prompt in our review. Approval times vary depending on current volume and the team’s availability. We will contact you via your Figma account email to notify you of our decision. If your Figma Community App has been rejected, we'll send you an email with our determination.

### Scope & Updates

You’ll need to register a separate Figma Community App for each application that’s calling Figma’s APIs. For example, if you offer a design system documentation app called "DS Docs" and a design system management app called "DS Manager," and both apps call Figma’s APIs, you would register two Figma Community Apps.

If the core functionality of your Figma Community App substantially changes, you should submit details of what changed in the developer portal for review. Figma may also periodically review your Figma Community App to ensure compliance with relevant standards as they evolve.

## Review guidelines

1. [Quality & Usability](#h_01K5FCVBPBBXYE9AW0QAJ9HHJG)
2. [Trust & Safety](#h_01K5FCVBPBK1K16PHAZWHVF3W1)
3. [Figma & Community](#h_01K5FCVBPBTQGHZ2WWHCA42X7F)
4. [Legal](#h_01K5FCVBPBDE8JN528XZKN9ZRB)

### 1. Quality & Usability

We want users to have a great experience using Figma Community Apps. In connection with this, we review for:

- Completeness
  - Please make sure the features in your application that use Figma’s APIs are complete and function as intended. We won't be able to approve Figma Community Apps that do not work or don't use Figma's APIs correctly.
- Accurate Descriptions
  - Your Figma Community App must include an accurate name and description, and an icon that matches your application’s brand. We will use this information to review your app, and Figma customers will use this information to decide whether or not to install your app.
- Performance
  - Figma Community Apps that stop working or offer a low quality experience may be removed at any time.

### 2. Trust & Safety

We want our users to feel confident that the Figma Community Apps they allow to access their Figma data are safe, secure, and unoffensive. In connection with this, we review for:

- Objectionable Content
  - Content that is fraudulent, false, misleading, deceptive, defamatory, obscene, pornographic, vulgar, offensive, relates to gambling or sweepstakes, or otherwise violates Figma’s [Developer Terms](https://www.figma.com/legal/developer-terms/) is not permitted.
- Security 
  - The security of our platform is critical for maintaining our customers’ trust, and we expect our Figma Community App developers to maintain similar standards. In connection with this, we may reject Figma Community Apps that read or modify a Figma file without a user’s explicit awareness and consent, or that don't adequately protect the privacy and security of customer data (including how data is retained and served).
- API Usage
  - Figma Community Apps can only leverage official APIs provided by Figma and cannot require users to install separate packages that manipulate Figma on the Web or the Desktop App.
  - Any attempts to exploit the API (deceitful manipulation of user files, theft of data) will result in immediate denial of API access.
  - Developers may not sub-license or otherwise distribute Figma APIs to other third parties.
- Account Requirements
  - If you are publishing or otherwise sharing a Figma Community App on behalf of an organization, you are responsible for ensuring you have the appropriate authority to do so.
  - Please ensure that your contact information is accurate and complete for users in the event they have any questions, support issues, or feedback.
  - Authors may not share their Figma account or password information.

### 3. Figma & Community

Figma’s developer platform is provided and maintained by Figma in order to enable Figma Community Apps that add value to the Figma community and help our customers leverage the power of Figma more effectively and securely. The Figma Community App review team will use its best judgment to evaluate whether Figma Community Apps are the right fit to have access to our platform. In connection with this, we review for:

- Value to Figma and the community
  - We may not approve, or we may revoke approval of, Figma Community Apps that harm Figma’s business or reputation, do not offer value to the Figma community but rather merely duplicate Figma functionality, or allow users to access or use Figma functionality in a manner intended to avoid fees.
  - To provide the most value to Figma and the Community, Figma Community Apps that utilize the Figma MCP Server are intended to allow data to flow both ways.  Figma reserves the right to disable any apps from using the Figma MCP Server in the event they block write back tool calls.
- Data protection – file search & indexing
  - Figma does not currently permit Figma Community Apps to index file content available in a Figma customer's account. Specifically, Figma Community Apps may not use [the projects endpoints](https://www.figma.com/developers/api#projects) to enumerate the files in an organization/team.
  - Figma does not currently permit bulk export of Figma file content by Figma Community Apps. Unpermitted use cases include but are not limited to: enterprise search / unified search and AI/LLM training. Specifically, Figma Community Apps may not use the [Figma files endpoints](https://www.figma.com/developers/api#files-endpoints) to ingest large/bulk quantities of Figma file content.

Figma does permit Figma Community Apps to request and store the metadata of individual Figma files that a joint customer uploads into the developer's system. Permitted use cases include: unfurling or embedding a Figma link pasted into a developer’s application by a customer.  Specifically, Figma Community Apps can use the [GET file metadata](https://www.figma.com/developers/api#get-file-metadata-endpoint) API for this purpose.

### 4. Legal

Please review our [Developer Terms](https://www.figma.com/legal/developer-terms/), and consult with a lawyer to ensure you understand your legal obligations when creating and sharing Figma Community Apps. Do not rely on these guidelines or Figma’s review process to make sure you are in compliance with the law. We reserve the right to reject any Figma Community Apps (and deny API access) if we learn they are violating our terms or the law.  

If you are using Figma’s brand, you are required to review and comply with [Figma Brand Usage Guidelines](https://www.figma.com/using-the-figma-brand/).

**Note:** If you have any questions or concerns around our review guidelines, please [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new).
