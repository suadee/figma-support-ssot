---
기술지원명: AWS Amplify Studio and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: AWS Amplify Studio and Figma
출처링크: https://help.figma.com/hc/en-us/articles/6376798776343-AWS-Amplify-Studio-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

 

Supported on [Education, Professional, Organization, and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with **can edit** access to a file, project, or team can subscribe a channel to that resource.

Anyone with **can edit** access to a file can see previews of the file in Slack.

[AWS Amplify Studio](https://aws.amazon.com/amplify/studio/) lets you go from Figma Design to feature-rich, full-stack web apps in hours, on AWS.

Designers and developers use Amplify Studio to work collaboratively on development tasks and ensure pixel-perfect implementation of your Figma designs.

Typically, front-end developers spend a lot of time incrementally making minor UI code tweaks to match provided designs. Designers need to verify that new implementations match the designs. This can lead to inefficiencies and suboptimal end user experiences due to compromises made to ship on time.

With AWS Amplify Studio, developers can automatically import UI component designs from Figma as code. The generated components are familiar to any React developer and offer the same flexibility as hand-authored components, with mechanisms to modify component properties.

Amplify Studio’s Figma Integration:

- Automatically converts your UI component designs into clean React code.
- Lets your developers select from a library of prebuilt UI components, such as news feeds, contact forms, and e-commerce cards, and primitives such as buttons, text ares, and alerts, which can be fully customized within Figma.
- Generates UI components that follow accessibility best practices and are themeable using a Figma plugin to match your brand’s look-and-feel.
- Lets your developers easily connect the generated UI components to existing backend data.

# **Import a Figma UI design to AWS Amplify Studio**

## **Step 1: Set up Figma file**

To get started, simply link your Amplify Studio project to a Figma file. While you can link any Figma file to Amplify Studio, for the best end-to-end experience, we recommend starting with our template Figma file. To start from scratch, simply **[duplicate our Figma UI file](https://www.figma.com/community/file/1047600760128127424)**.

## **Step 2: Link Figma file in Amplify Studio**

In Amplify Studio, enter the URL for the Figma file you created or duplicated. You will be asked to authenticate with Figma.

![Figma and AWS Amplify Studio interface showing the process to sync designs by pasting a Figma file link for integration. Copy the link from the sharing modal in Figma and paste it into the AWS sync modal.](https://lh6.googleusercontent.com/aMkIvDxiPTJFczbxv3GBk1q3ct5U246QdltasLbkE1_pJ6wQKUZ94r6YtzZaosQR2v1Jn984Lt4n7yVCpGK3Gx-2Nk1hGFi1atU3MIBd4mmgpgxKKqpTlGDb9hgxY2iEY1zwxcHH_Ohyl9txOg)

After authenticating with Figma, you will see a list of components that you can sync with Amplify Studio.

Select **Accept all** to import all components, or walk through them individually to ensure they are visually acceptable.

Once you complete the sync, you will see a list of components that have been imported.

All previews of the components are live renders of the coded UI components. You can open your developer tools inspector to confirm.

![Figma sync interface showing comparison of current and updated hero layouts, with options to reject or accept changes.](https://lh6.googleusercontent.com/gbazkrTzRFOoIfsLzkJFFLJrPnP-7996TXkIeB7X5lpyBH_6-TDuYHutidsxv5iJvogEDmR55kdJUqtSHlfukjvJCUeU8LlAd07E_t-3_AT-Pk6o1OiblDRpevNeq3ZHrvaPxHwbfM-LEjAATw)

## **Step 3: Pull UI components code into your project**

In Amplify Studio, choose a component and select **Configure** to get to the component editor screen. Select **Get component code** at the bottom of the page.

Go to the **Initial project setup** tab and follow the setup instructions.

![Instructions for setting up the initial project in Amplify Studio, including npm install, configuring index.js, and using AmplifyProvider.](https://lh5.googleusercontent.com/rjw5V5BvOFaA73BBe4Z9iqX8FYCb8MSbTv_1abQXWpoI2M4iPteUHO5p8aD9C5ed213bblX7UyycIdqoiTVEPIA9Eq9GgCVkXAQYWsOIlRb8DR9g_Uet9zDrF55-TZVZu7PyvoQtOc2329o9eQ)

Amplify Studio generates all UI component code into src/ui-components, as JSX and TS files. All generated code is built with primitives from the [Amplify UI library](https://ui.docs.amplify.aws/).

Although you have access to inspect the component code, you cannot modify it directly as Amplify Studio will override any changes on the next amplify pull.

Once the amplify pull command downloaded all UI components to your src/ui-components folder, you can use the components anywhere in your app. Learn how to **[customize these UI components in code](https://docs.amplify.aws/console/uibuilder/override/)**.

```
  import { ComponentA, ComponentB }  from './ui-components';
```

**Need help using AWS Amplify Studio?** Check out the [AWS Amplify Studio docs](https://docs.amplify.aws/console/) or join the Discord community at [discord.gg/amplify](http://discord.gg/amplify).
