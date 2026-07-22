---
기술지원명: Plugin and widget review guidelines
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Plugin and widget review guidelines
출처링크: https://help.figma.com/hc/en-us/articles/360039958914-Plugin-and-widget-review-guidelines
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Caution:** This is an evolving document, so its contents may change over time. If you have any questions or concerns around our review guidelines, please [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new).

Figma is committed to supporting plugins and widgets within the Figma Community. Developers like you help our community discover new ways to design and explore Figma's products. We can't wait to see what you've created.

Before a plugin or widget can be listed in the [Figma Community directory](https://www.figma.com/community), it needs to go through our review process.

To make the submission process as seamless as possible, we have created a set of guidelines that we use to evaluate plugins and widgets. These guidelines are meant to give you an idea of the criteria we review, but are not exhaustive.

## Before you submit

When you are ready to submit, please make sure you have done the following:

- Tested your plugin or widget thoroughly with a variety of scenarios and confirmed it’s free of bugs and crashes.
- Reviewed this process and Figma’s plugin and widget review guidelines below.
- Established a way for users to contact you for support. It's your responsibility to provide support for your plugin and widget users. For example, you can provide them with an email address or a link to a website or help center.
- Reviewed and understand your obligations under our [Developer Terms](https://www.figma.com/legal/developer-terms/), [Creator Agreement](https://www.figma.com/legal/creator-agreement/), [Licensing Terms](https://help.figma.com/hc/en-us/articles/360042296374-Figma-Community-copyright-and-licensing), and [Figma Community Terms](https://www.figma.com/legal/community-terms/).
- Consulted legal counsel to understand your legal obligations, and prepare necessary documents (like a privacy policy).

## What to expect

Our goal is to be thoughtful and reasonably prompt in our review. Approval times vary depending on current volume and the team’s availability. We will contact you via your Figma account email to notify you of our decision. If your plugin or widget has been rejected, we'll send you an email with our determination. You may submit your plugin or widget again for review after addressing any feedback.

## Updates

Any material updates to your plugin or widget are subject to re-review in accordance with this process. If the core functionality of your plugin or widget substantially changes, you should create a new, separate plugin and submit it for review. Figma may also require periodic reviews to ensure compliance with relevant standards as they evolve.

## Review guidelines

1. [Quality and Usability](#quality-and-usability)
2. [Trust and Safety](#trust-and-safety)
3. [Business](#business)
4. [Legal](#legal)

### 1. Quality and Usability

We want the plugins and widgets available in the Figma Community to be high quality. In connection with this, we review for:

- Completeness
  - Please make sure your plugin or widget is completed, functions as intended, and does not include temporary content. We will reject plugins and widgets that crash or have obvious bugs.
  - Please do not use developer error messages to communicate with end-users.
- Accurate Descriptions
  - Your plugin or widget should operate as described. Please include an accurate description, screenshot, or previews so that the users will not be surprised by any hidden functionality.
  - Your listing should reference documentation that describes how to set up and use your plugin or widget.
- Design
  - We highly recommend matching your plugin or widget to Figma's UI so we can create a seamless experience for our users.
  - If there are any concerns with usability, or any other negative externalities, we may reject the plugin or widget.
- Performance
  - If your plugin or widget negatively impacts the overall performance or experience within Figma, we may reject it. An example of this would be a long-running background process.
  - Your plugin or widget should deliver the appropriate notifications if the user is offline and your plugin or widget cannot work while the user is offline.
  - Plugins and widgets that stop working or offer a low quality experience may be removed at any time.

### **2. Trust and Safety**

We want our users to feel confident that installing Figma plugins and widgets is safe, secure, and unoffensive. In connection with this, we review for:

- Objectionable Content
  - Content that is fraudulent, false, misleading, deceptive, defamatory, obscene, pornographic, vulgar, offensive, relates to gambling or sweepstakes, or otherwise violates [Figma's Community Terms](https://www.figma.com/legal/community-terms/) is not permitted.
- Security
  - The security of our platform is critical for maintaining our customers' trust, and we expect our plugin and widget developers to maintain similar standards. In connection with this, we may reject plugins or widgets that read or modify a Figma file without a user's explicit awareness and consent, or that don't adequately protect the privacy and security of customer data (including how data is retained and served).
  - We encourage creators to fill out the [security disclosure form](https://help.figma.com/hc/en-us/articles/16354660649495-Security-disclosure-principles) when publishing their plugin or widget, to inform users about how the plugin secures their data.
- API Usage
  - Plugins and widgets can only leverage official plugin APIs or widget APIs provided by Figma and cannot require users to install separate packages that manipulate Figma on the Web or the Desktop App.
  - Any attempts to exploit the plugin or widget API (provide false information, plagiarism, deceitful manipulation of user files, or theft of data) will result in immediate removal. You will also be banned from publishing future plugins or widgets to the community.
  - Developers may not sub-license or otherwise distribute Figma APIs to other third parties
- Account Requirements
  - If you are publishing a plugin/widget on behalf of an organization, you are responsible for ensuring you have the appropriate authority to do so.
  - Please ensure that your contact information is accurate for users in the event they have any questions, support issues, or feedback.
  - Authors may not share their Figma account or password information with other users or otherwise sell, transfer, or assign ownership or control over plugins or widgets without Figma's approval.
- External Connections are Clear
  - If your plugin or widget requires a separate third-party account or requires additional payments or licensing this must be clear in the description.
  - Developers are encouraged to specify the network access of their plugins and widgets, learn more [here](https://www.figma.com/plugin-docs/making-network-requests/#specify-network-access).
  - If your plugin or widget shares data with a third party, you must obtain all necessary permissions and meet all legal requirements to do so.

### **3. Business**

Figma Community is designed to enable plugins and widgets that add value to the Figma community and help our customers leverage the power of Figma more effectively. The Figma plugin and widget review team will use its best judgment to evaluate whether plugins and widgets are the right fit for our platform and business goals. In connection with this, we review for:

- Community availability
  - The purpose of Figma Community is to enable sharing of plugins and widgets with all Figma Community users – not for publishing plugins/widget that are meant to be used only by an internal team.
  - If you want to publish a plugin or widget that is meant to be used privately within a team or small group of users, then you should publish a plugin or widget privately to your organization. Learn more [here](https://help.figma.com/hc/en-us/articles/4404228629655-Create-private-organization-plugins).
- Business sense
  - If a plugin or widget has the same essential functionality as an existing plugin or widget you've published previously, it should share the same listing.
  - We allow plugins and widgets to direct users to a third party to allow for monetization, but we reserve the right to reject plugins and widgets that attempt to monetize in poor taste.
  - We may not approve plugins and widgets that harm Figma's business or reputation, recreate Figma functionality, or allow users to access or use Figma functionality in a manner intended to avoid fees.
- Advertisements
  - Plugins and widgets may not display ads to Figma users. Please do not insert advertisements into design files or present ads in the plugin UI or widget UI.

### **4. Legal**

Please review our [Developer Terms](https://www.figma.com/legal/developer-terms/), [Creator Agreement](https://www.figma.com/legal/creator-agreement/), [Licensing Terms](https://help.figma.com/hc/en-us/articles/360042296374-Figma-Community-copyright-and-licensing), and [Figma Community Terms](https://www.figma.com/legal/community-terms/), and consult with a lawyer to ensure you understand your legal obligations when posting plugins and widgets on Community. Do not rely on these guidelines or Figma's review process to make sure you are in compliance with the law. We reserve the right to reject or remove any plugins or widgets if we learn they are violating our terms or the law.

If you are using Figma's brand, you are required to review and comply with the [Figma trademark guidelines](https://www.figma.com/using-the-figma-brand/).

Also, please remember, if your plugin or widget processes user data, you must provide and maintain a privacy policy that satisfies applicable legal standards.

**Note:** If you have any questions or concerns around our review guidelines, please [submit a request through our contact form](https://help.figma.com/hc/en-us/requests/new).
