---
기술지원명: Set up SAML SSO for AD FS
카테고리: 보안
작성자: Figma
승인자: (승인 대기)
출처: Set up SAML SSO for AD FS
출처링크: https://help.figma.com/hc/en-us/articles/360048269533-Set-up-SAML-SSO-for-AD-FS
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only Organization Admins can set up SAML SSO.

Organizations that have stricter security requirements can configure SAML SSO. [**Learn more about SAML SSO in Figma →**](https://help.figma.com/hc/en-us/articles/360040532333)

If you use Microsoft's [Active Directory Federation Service](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) (AD FS), you can set up SAML SSO for your Figma Organization.

To use this integration you will need to:

- Have an AD FS instance of 3.0 or later
- Expose the SAML endpoint for AD FS

You can use Micro as your identity provider to authenticate and provision users. Figma supports SAML SSO initiated from both Microsoft AD FS (identity provider) and Figma (service provider).

## Add Figma to AD FS

### Required information

There are a few pieces of information that you'll need from Figma during the set up process. We recommend having this open in another tab or window, so you can quickly copy it across.

1. Open Figma in the file browser.
2. Click **Admin**.
3. Select **Settings** at the top of the screen.
4. In the **Login and provisioning** section, click **SAML SSO**.
5. Find the **SP Entity ID** and the **SP ACS URL**. You'll need both to set up the connection in AD FS.

**Tip!** These URLs will look very similar as they both include your **Tenant ID**. The only difference is that your *SP ACS URL* will have `/consume` added to the end of it.

You need to decide if logging in via SAML SSO is mandatory, or if users can still login via email address and password. **[Learn more about authentication options →](https://help.figma.com/hc/en-us/articles/360046005913)**

### Add Figma to your AD FS instance

Now you need to add Figma as a "Relying Party Trust" to your AD FS instance.

1. Open your AD FS instance.
2. In the **Actions** column, click **Add Relying Party Trust**. This will open a wizard that will guide you through the set up process. ![AD FS instance with panels showing an overview of the instanc and a list of actions, including the add relying party trust option](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588197332390_Screenshot+2020-04-29+14.45.49.png)
3. On the Welcome screen, click “**Start**” to start the set up process.
4. On the **Select Data Source** step, select **Enter data about the relying party manually** and click **Next**.
5. Add a **Display name**, like Figma or similar, then click **Next** to proceed.
6. On the **Configure Certificate** step, click the **Browse** button. Select **AD FS profile** from the options and click **Next**.
7. On the **Configure URL** step, select **Enable support for the SAML 2.0 WebSSO protoco**l
8. On the same page, paste the **Figma SP ACS URL** in the field provided. The link should look something like this: `https://www.figma.com/saml/123456789123456789/consume`. Click **Next** to proceed. ![The Configure URL step of the process with the Enable support for the SAML 2.0 option checked and the URL pasted in the field provided](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209465768_Screenshot+2020-04-29+14.48.40.png)
9. On the **Configure Identifiers** step, paste in your **SP Entity ID** in the **Relying party trust identifier** field. The link should look something like this: `https://www.figma.com/saml/123456789123456789`. Click **Next** to proceed. ![Configure identifiers page with the SP Entity ID url listed in the Relying party trust identifier section](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209490383_Screenshot+2020-04-29+14.49.23.png)
10. On the **Choose Access Control Policy** step, choose an access control policy. This determines who can authenticate their Figma account via SSO. Click **Next** to proceed. ![The Choose Access Control Policy with Permit Everyone selected](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209510113_Screenshot+2020-04-29+14.49.29.png)
11. On the **Ready to Add Trust** step, click the **Next** button to complete the process.
12. Click **Close** to finish the Wizard.

### Add attributes to AD FS

Next, you need to add a rule to AD FS. This will ensure the integration sends LDAP attributes as claims.

1. On the **Edit Claim Issuance Policy** page, click the **Add rule** button. ![](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209572512_Screenshot+2020-04-29+14.51.13.png)
2. Under **Claim rule template**, select **Send LDAP Attributes as Claims**. Click **Next** to proceed. ![](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209587464_Screenshot+2020-04-29+14.51.24.png)
3. On the **Configure Claim Rule** step:
   1. Enter a **Claim rule name**.
   2. For your **Attribute store**, select **Active Director**.
   3. In the **LDAP Attribute...** column, select **E-Mail Address**.
   4. In the **Outgoing Claim Type...** column, select **E-Mail Address**.
   5. Click **Finish** to complete the process and return to the **Edit Claim Issuance Policy** screen.![](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209621441_Screenshot+2020-04-29+14.52.17.png)
4. Click **Apply** to apply the rule and return to the *Issue Transform rules* page.
5. Click **Add Rule** to add a second Transform rule.
6. Under **Claim rule template**, select **Transform an Incoming Claim**. Click **Next** to proceed.
7. On the **Configure Claim Rule** step:
   1. For **Claim rule name**, enter **Transform email address as NameID**
   2. In the **Incoming claim type**, select **E-Mail Address**.
   3. In the **Outgoing Claim Type** column, select **NameID**
   4. In the **Outgoing name ID format** column, select **Email**
   5. Toggle **Pass through all claim values**.
   6. Click **OK** to complete the process and return to the **Edit Claim Issuance Policy** screen.![](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1590524934156_Screenshot+2020-05-26+13.10.22.png)
8. Click **Apply** to apply the rules to your instance.

### Export signing certificate

Now you'll need to export your **Signing Certificate**, usually called the X509 certificate. We use this to verify your Organization via your Identity Provider.

1. In your AD FS instance, go to **Service > Certifications**
2. Click on the certificate under **Token-signing** and select **View Certificate**. certificate ![](https://paper-attachments.dropbox.com/s_5A407347E66203089B4D4D0A79E33FE8E66A6080021E945AF8DD08F107AACD3D_1588209659955_Screenshot+2020-04-29+14.53.27.png)
3. Click **Copy to File >** **Ok**.
4. Click **Next** on Certificate Export Wizard.
5. Select **Base-64 encoded...** from the options and click **Next**.
6. Name your certificate file `figma.cer` and click **Next**.
7. Click **Finish** to export the certificate. AD FS will export the certificate to your configured downloads folder.

## Complete the set up process in Figma

Now that you have everything set up in AD FS, you'll need to add your AD FS details to Figma. Our [Set up a custom SAML configuration](https://help.figma.com/hc/en-us/articles/360040047774) article takes you through that process.

You'll need the following information from AD FS:

- **IdP Entity Id:** This lets Figma know which Identity Provider you are using.
- **IdP SSO Target URL:** Figma will use this link to connect to the Identity Provider when someone from your Organization attempts to login via SAML SSO. For AD FS, it should look something like this: `https://sso.yourdomain.tld/adfs/ls/`
- **Signing Certificate:** This is the certificate that you have just downloaded.

### Let your users know about the change

The first time a user logs into Figma using SSO, or after they are provisioned via SCIM, they'll receive a verification email from SendGrid. This email contains a unique 6-digit pin, which they'll use just once as an additional security measure during their initial login.

To make sure users don't mistake the email for spam or a phishing attempt, you may wish to let them know about this extra step in advance.
