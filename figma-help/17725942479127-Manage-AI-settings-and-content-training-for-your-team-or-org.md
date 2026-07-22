---
기술지원명: Manage AI settings and content training for your team or organization
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Manage AI settings and content training for your team or organization
출처링크: https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Team or organization admins can control AI content training settings.  
Figma’s AI features are available across plans and seats. A person’s feature access and [usage limits](https://help.figma.com/hc/en-us/articles/33459875669015) depends on their plan and seat.

To make improvements to Figma's AI features and products over time, we will be training models that better understand design concepts and patterns, and Figma’s internal formats and structure through Figma content. Admins can enable AI features on a team, workspace, or organization basis, and choose whether they participate in content training.

[Learn more about Figma's AI features and products](https://help.figma.com/hc/en-us/articles/24039793359767).

## Adjust AI content training settings

Content training settings help you manage how your team’s data contributes to improving AI. [Learn more about Figma’s approach to AI →](https://www.figma.com/ai/our-approach)

Note: If an admin turns off content training, new content and edits will not be used to train AI models. Content training does not affect access to AI capabilities. Enabling AI features for your account is a separate setting, [which can be enabled for a team or organization](#h_01J0SNQBZ9JXM4T45V5QWZ2QFZ).

Select your plan for detailed instructions:

Starter plansProfessional plansOrganization or Enterprise plans

By default, content training is turned **on** for Starter teams.

Admins of a Starter team can toggle off content training at any time in the team's settings.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), open your team and click **All Projects** in the left sidebar.
2. Select  next to your team name and choose **View settings**
3. Go to the **Settings** tab and scroll to **AI** section.
4. Select **Manage AI settings**.
5. Toggle **Content training** on or off.  
   ![AI settings panel showing content training toggle switched on, explaining Figma's privacy measures.](https://help.figma.com/hc/article_attachments/33686474776599)

By default, content training is turned **on** for Professional teams.

Admins of a Professional team can toggle off content training at any time in the team's settings.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), open your team and click  **Admin** in the left sidebar.
2. Open the **Settings** tab and scroll to **AI** section.
3. Toggle **Content training** on or off.

![Toggle switch for enabling Figma's AI content training with privacy protection information.](https://help.figma.com/hc/article_attachments/33686459159447)

By default, content training is turned **off** on Organization and Enterprise plans. Content training does not affect access to AI features.

Note: Content training is currently disabled for Organization and Enterprise plans and can't be toggled on right now. We'll let you know if this changes in the future.

## Adjust access to AI across Figma

Enabling AI features in your team, workspace, or organization allows users to leverage Figma’s AI capabilities, including [Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231) and other [Figma AI tools](https://help.figma.com/hc/en-us/articles/24039793359767).

Select your plan for detailed instructions:

Starter plansProfessional or Organization plansEnterprise plan

On Starter plans, admins can enable AI if previously disabled during beta. Once AI features are turned on, they're permanently enabled on your account.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), open your team and click **All Projects** in the left sidebar.
2. Select  next to your team name and choose **View settings**
3. Go to the **Settings** tab and scroll to **AI** section.
4. Select **Manage AI settings**.
5. Here you’ll see if AI features are currently disabled. If so, you can select **Enable AI** to grant access.  
   ![AI settings panel showing AI features disabled with option to enable for access to Figma Make and other AI features.](https://help.figma.com/hc/article_attachments/33686459162775)

On Professional or Organization plans, team or organization admins can enable AI features in admin settings if previously disabled during beta. Workspace admins and team admins do not have access to this setting. Once AI features are turned on, they're permanently enabled on your account.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), open your organization and click **Admin** in the left sidebar.
2. Open the **Settings** tab and scroll to **AI** section.
3. Here you’ll see if AI features are currently disabled. If so, you can select **Enable AI** to grant access.  
   ![AI features disabled notification in Figma settings with option to enable AI.](https://help.figma.com/hc/article_attachments/33686459163287)

If you already have AI features enabled, you will not see the **AI features** setting in your admin settings. Instead, you'll only see **Content training** settings. You can also check to see if you have AI features already enabled by [trying to use one within your team or organization](https://help.figma.com/hc/en-us/articles/24039793359767).

On Enterprise plans, organization admins can enable or disable AI features in the organization’s admin settings.

You can manage AI feature access at either the organization or workspace level:

- Organization-level AI settings define the default AI feature access for all workspaces in the organization, as well as for drafts. By default, AI features are turned **on**.
- Workspace-level AI settings determine whether a specific workspace has access to AI features.

If a file belongs to a workspace with its own AI setting, that workspace’s setting applies. If the workspace doesn’t have a specific AI setting, the file follows the organization-level setting.

Note: Workspace admins and team admins can’t change AI settings. Only organization admins can manage them.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), open your organization and click **Admin** in the left sidebar.
2. Open the **Settings** tab and scroll to **AI > AI features** section.
3. In the modal, choose to enable or disable AI features for your entire organization.
4. [Optional] Adjust AI settings for specific workspaces.

![Update workspace or organization AI access from settings.](https://help.figma.com/hc/article_attachments/35285429200663)

**When AI features are toggled on for an organization/workspace:** users can use any AI feature, [relevant to their seat](https://help.figma.com/hc/en-us/articles/24039793359767), from within files in that workspace, as long as they have access to the file.

**When AI features are toggled off for an organization/workspace:** members won’t be able to access AI features or products within the organization or workspace where AI is toggled off. This won’t prevent them from using AI features in spaces outside of the disabled organization or workspace. For example, if AI is enabled in an organization but disabled in a workspace, users can still use AI features in their drafts and other workspaces where AI is enabled.

## Data privacy and security

We know how important your data is to you, your company, and your clients. Our model development process is designed to protect your privacy and confidential information.

We take additional steps to train our models so that they learn general design patterns and Figma-specific concepts and tools—not your content, concepts, and ideas. For example, we de-identify content and redact sensitive information including from text and images.

You can learn more about how we protect your data [here.](https://www.figma.com/ai/our-approach/#data-privacy-and-security)

## Frequently asked questions

I'm a **Figma for Education** or **Figma for Government** account. What does this mean for me?

- [Figma for Education](https://help.figma.com/hc/en-us/articles/360041061214): AI feature availability depends on the type of Education account.
  - AI tools are available for higher education and bootcamp Education users. AI tools are not available for K-12 Education users.
  - Figma Make, our AI-driven prompt-to-app tool, is available for higher education and bootcamp Education users. Figma Make is not available for K-12 Education users.
- [Figma for Government](https://help.figma.com/hc/en-us/articles/22932461365015): Organizations using the Figma for Government solution have access to Figma Make, our AI-driven prompt-to-app tool. Other Figma AI features are not currently available on Figma for Government.

Figma does not use any data from Figma for Education or Figma for Government accounts to train AI models.

How does the content training setting work and what happens after I turn it off?

Content helps us build better, more useful experiences, but sharing it with Figma for AI training is optional. Admins can control whether or not content is used for AI model training with the content training setting. For Starter and Professional accounts, this is a team-level setting.

Content training went into effect on August 15, 2024. If an admin turns off content training after this date, new content and edits will not be used to train AI models.

What 3rd party models does Figma’s AI use?

We work with multiple vendors, such as OpenAI, to operationalize, build and fine-tune AI models, as well as process data to power Figma’s AI features. You can find the list of the sub-processors used to power AI features [here](https://figma.com/sub-processors/).

Do you use content from my drafts to train AI models?

Drafts organized into teams are treated the same as other files in that team and will only be used to train AI models if content training is set to ‘on’. Content training is an admin setting. If you prefer that Figma not use content in your drafts to train AI models, please:

- Turn off content training or ask your admin to do so
- Move your drafts into a Starter or paid team where content training is set to ‘off’

How does Figma protect my privacy and confidential information?

We know how important your data is to you, your company, and your clients. Our model development process is designed to protect your privacy and confidential information.

For all customer data, we:

- Encrypt all data at rest and in transit
- Use security measures designed to protect against unauthorized access to customer data
- Enforce tailored permissions and user access controls around who can view and access your data

When working with 3rd party companies to process data, we:

- Do not permit 3rd party model providers to use data that customers upload or create on the Figma platform for training their own models
- Limit how long vendors can store data. OpenAI and our other 3rd party model providers store data temporarily, or in some cases not at all, in order to process requests and enable AI features

We take additional steps to train our models so that they learn general design patterns and Figma-specific concepts and tools—not your content, concepts, and ideas. For example, we de-identify content and redact sensitive information including from text and images.

Read more about Figma’s security practices [here](https://www.figma.com/security/).

### Have another question?

- Learn more about [Figma’s approach to AI →](https://www.figma.com/ai/our-approach)
- Review our updated [AI Terms →](https://www.figma.com/legal/ai-terms/)
- Read about [Figma’s Security →](https://www.figma.com/security/)

If you have any other questions about AI settings, please [submit a request to our Support team](https://help.figma.com/hc/en-us/requests/new) using the below form fields so we can best support you:

- Under **Please choose your issue**, select **Data privacy and content training**
- Under **I need help with…**, select **Content training**
