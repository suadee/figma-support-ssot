---
기술지원명: Set up Figma with Chrome App licensing
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Set up Figma with Chrome App licensing
출처링크: https://help.figma.com/hc/en-us/articles/17866896241687-Set-up-Figma-with-Chrome-App-licensing
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

This article describes Step 2 when [setting up Figma for your school →](https://help.figma.com/hc/en-us/articles/17866533974295)

Set up Figma with Chrome App licensing via your Google administrator account. This makes sure that every time a student or educator logs in to Figma with their school email, a license is redeemed in your Google workspace.

Note: The steps in this article need to be performed in your Google administrator account, not Figma. For help with this process, visit the [Chrome Enterprise and Education Help Center →](https://support.google.com/chrome/a/answer/9681911?hl=en)

## Step 1: Provision Figma app

1. Login to [admin.google.com](https://admin.google.com) with your Super administrator account.
2. From the admin **Home** page, go to **Devices** > **Chrome**.
3. Click **Apps & extension**s > **Users & browsers**.
4. In the lower-right corner, click the yellow **Add** button.
5. Four circles will pop up, select the top one with a globe icon to **Add by URL**.
6. Add `https://www.figma.com` (please use this exact URL).
7. You can choose to have the website open in browser tab or a separate window.
8. Select the **Organizational Unit** (OU) you want to provision the app to.
9. To apply the setting to everyone, leave the top organizational unit selected. Otherwise, select a child organizational unit.
10. Under Installation policy for the Figma app, select **Force Install + pin to Chrome OS taskbar**.
11. Click **Save** in the top-right corner.

## Step 2: Redeem Figma Licenses

1. Click on the redemption URL provided to you for your district. This is provided by Figma Education team once approved after verifying your education status. For questions, [submit a request](https://help.figma.com/hc/en-us/requests/new).
2. Confirm that the app listed and the license quantity match your order > click **Redeem**.
3. Follow the onscreen redemption instructions.
4. Click **Save** in the top-right corner.

## Step 3: Deploy Figma Licenses

Note: When a user first signs in to Figma with their Google Account, Figma claims a license. Once claimed, the license remains with the user until they move organizational units or groups, the license is turned off for their organizational unit or group, or the license expires.

1. Select the Figma app on the App Licensing page.
2. Change the app license to **ON** for the domain or each of the child organizational units that should have access.
3. Click **Save** in the top-right corner.

## Step 4: Install the FigJam add-on for Google Classroom

If your school or district has **Google Workspace Education Plus or the Teaching & Learning Upgrade**, please install the FigJam add-on for Google Classroom for better tool integration and simplified workflow. Skip if you don’t have these versions of Workspace.

1. Visit the [FigJam add-on Google Workspace Marketplace listing](https://workspace.google.com/marketplace/app/figjam/185512328996) and click **Admin Install**.
2. Review the terms of installation and click **Continue**.
3. Choose to install the app automatically for **Everyone at your organization** or for **Certain groups or OUs** > click **Finish**.

## Step 5: Install the FigJam app for the Jamboard Importer

In order for teachers to utilize the Jamboard importer, you will need to grant FigJam access to your Drive. This can be done by approving the APIs of the FigJam App in your Google Workspace.

1. Log in to the Google Admin console and visit Security > API controls
2. Select **Manage third-party app access**.
3. Click **Configure new app** and search for the following App ID: `438425412978-45umild77kjr12jigqg31ojvlno436ev.apps.googleusercontent.com`
4. Select the application and follow the on-screen prompts. You can configure access for your entire domain, group, or individual OUs.
5. In order to work correctly, it is recommended that you configure FigJam as a “trusted” app.
6. Click **Finish** to complete the configuration.

[For help with this process, visit this Chrome help center article →]((If%20you%20have%20additional%20questions,%20visit%20this%20Chrome%20help%20center%20article))

## Step 5: Provide admin contacts

After granting API access, provide the name and email address of the admin and others in your organization that are responsible for the apps. This information will be shared with the app developer so they can contact the admin with any additional resources and requirements.

## Step 6: Confirm and test access

Once you have completed the license redemption and API steps, please confirm your completion with the Figma team. You will be notified once your organization's account has been created and your account, or another designated account, has been upgraded to serve as the administrator.

At this time, you should [test to confirm access to your Figma account](https://help.figma.com/hc/en-us/articles/17867675040663) matches your expectations.

[Learn more in the Chrome Enterprise & Education FAQ →](https://support.google.com/chrome/a/answer/188447?hl=en&ref_topic=4386908&sjid=16721839668462426833-NA)

[Next step: Test Figma organization access →](https://help.figma.com/hc/en-us/articles/17867675040663)
