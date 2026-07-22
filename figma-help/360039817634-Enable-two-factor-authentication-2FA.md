---
기술지원명: Enable two-factor authentication (2FA)
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Enable two-factor authentication (2FA)
출처링크: https://help.figma.com/hc/en-us/articles/360039817634-Enable-two-factor-authentication-2FA
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Use two-factor authentication on any [Figma team or plan](https://help.figma.com/hc/en-us/articles/360040328273)

You can't configure two-factor authentication in Figma if you login via Google SSO or SAML SSO

Enable two-factor authentication (2FA) to add an extra layer of security to your Figma account. When 2FA is enabled, you need to confirm your identity each time you log in to your Figma account.

You can authenticate your Figma account using any of the following methods:

- SMS
- Google Authenticator
- Duo Mobile
- Authy
- 2FA (Windows phone)

You need to choose your authentication method as part of the setup process. We recommend installing any authentication apps before you start.

Two-factor authentication must be set up on each Figma account individually. If you have Governance+ for Figma Enterprise, [you can also set up two-factor authentication for an entire team or organization](https://help.figma.com/hc/en-us/articles/31825370509591-Governance-for-Figma-Enterprise#h_01JT8V7QE37XJMKJ7YQ05Z1SSF).

Note: If you login to Figma via [Google SSO](https://help.figma.com/hc/en-us/articles/360040047614) or [SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333), you won't be able to enable two-factor in Figma. You will need to enable two-factor or multi-factor authentication with your identity provider instead.

# Set up two-factor

Enable two-factor authentication in your Figma account settings. To view and update your account settings:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click your name in the top-left corner.
2. Select **Settings** from the account menu.
3. From the **Security** tab, click **Enable two-factor authentication**.

- A 

  ## SMS

  1. Click **Enable two-factor authentication**.
  2. Enter your password to confirm your identity and click **Continue**.
  3. Select **Send me an SMS instead** option.
  4. Enter your phone number and click **Verify**. Figma will send you an SMS with a seven-digit code.
  5. Enter the code you received in Figma and click **Verify**.
  6. Click **Continue to recovery codes** to receive your recovery code(s).
  7. Figma will display a list of recovery codes on screen. We recommend saving a copy of these somewhere safe. For example: in a password manager or encrypted file storage.

  **Note:** When you set up two-factor with SMS, you can also add an authenticator app. When both are enabled, Figma will prompt you to authenticate via the app first. Click **Send me an SMS** to authenticate via SMS instead.
- B 

  ## Authenticator app

  You need to choose your authentication method at the beginning of the set up process. We recommend setting your authenticator up on your device(s) before you enable two-factor in Figma:

  - [Get verification codes with **Google Authenticator**](https://support.google.com/accounts/answer/1066447) (external link)
  - [Authenticating with the **Duo Prompt**](https://guide.duo.com/prompt) (external link)
  - [Downloading and Installing **Authy** Apps](https://support.authy.com/hc/en-us/articles/115001945848-Installing-Authy-apps)
  - [Get **Microsoft Authenticator**](https://www.microsoft.com/en-us/p/microsoft-authenticator/9nblgggzmcj6) (external link)
  1. Click the **Enable two-factor authentication** setting.
  2. Enter your password to confirm your identity and click **Continue**.
  3. Figma will display some links to download and install your desired authenticator. Once you have your authenticator installed or set up, click **Continue**.
  4. Figma will display a unique barcode on screen. Use your authenticator app to scan the barcode.
  5. Your authenticator app will generate a six digit code. Enter the code in the field provided and click **Verify**.
  6. Click **Continue to recovery codes** to receive your recovery code(s).
  7. Figma will display a list of recovery codes on screen. We recommend saving a copy of these somewhere safe. For example: in a password manager or in encrypted file storage.

  Note: Disable two-factor authentication by visiting this page and clicking the **Disable** link. You will need to confirm your password before you can disable two-factor authentication.

# Remove two-factor authentication

Remove or reconfigure your two-factor authentication settings at any time. Manage two-factor authentication in your Figma account settings:

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click your name in the top-left corner.
2. Select **Settings** from the account menu.
3. From the **Account** tab, scroll to the **Password** section.

- A 

  ## SMS

  1. Next to the **Configured cell phone number** click **Configure**.
  2. Click **Unregister SMS number.**
  3. Click **Turn off 2FA**.
- B 

  ## Authenticator app

  1. Next to **Authenticator apps are enabled** click **Disable**.
  2. Enter your password to confirm your identity and click **Continue**.
  3. Click **Ok** to confirm and remove two-factor authentication.
  4. Click **Use an authenticator app instead**.
