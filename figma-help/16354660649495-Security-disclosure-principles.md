---
기술지원명: Security disclosure principles
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Security disclosure principles
출처링크: https://help.figma.com/hc/en-us/articles/16354660649495-Security-disclosure-principles
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

🚧  **The security disclosure program is currently in open beta**

Beta features can change during the beta period. You may experience bugs or performance issues during this time.

As a part of Figma’s security disclosure program, developers of plugins and widgets can voluntarily fill out a security disclosure form for their plugins and widgets. The form is intended to give users of plugins and widgets a better view into the data security practices of a given plugin or widget. After the disclosure form has been approved by Figma, logged-in users can view the disclosure in the Community listing of the plugin or widget.

When you submit your security disclosure form, it may take up to two weeks for the form to be reviewed and approved. While you're waiting for approval, you can continue to update your plugin or widget.

This page includes:

- [General security recommendations for plugins and widgets](#01H84R4NVTB5NVQ96CCMG5R2KP)
- The [questions and passing criteria](#01H7ZKD2G0D37XS23AYJBD51W7) for the voluntary security disclosure form

## Data security recommendations

Data security is a complex and expansive topic. These best practices are general, high-level principles that plugins and widgets are asked to follow.

### Protect users

Protecting users and user data is critical. Plugins and widgets must protect user data in the following ways:

- If a plugin or widget requires a user to authenticate, it should use a trusted security provider or method such as Auth0 or OAuth 2.0.
- If Personal identifiable information (PII) and user data derived from the Figma APIs must be sent outside Figma, you need to be transparent with your users and comply with all disclosure requirements under applicable law.
- If a plugin or widget must store data, where possible, the storage features provided by Figma should be used.

### Use HTTPS

All network requests made from a plugin or widget to an external server should use HTTPS. Plugins and widgets should never use HTTP for network requests from Figma.

### Restrict network access

Plugins and widgets should restrict ‌network access to only the domains that are required for the plugin or widget to run.

## Questions and disclosure principles

This section contains the questions that appear on the security disclosure form for plugins and widgets, and the principles that Figma considers for the security disclosure program.

| Question | Applied principle |
| --- | --- |
| **1. Do you host a backend service for your plugin or widget?** | Ideally, the plugin or widget doesn't use an external backend. |
| **1b. Do you have a publicly documented process for managing security vulnerabilities in the service(s) you host? For example, see [Figma’s security vulnerability process](https://hackerone.com/figma?type=team&view_policy=true).** | If the plugin or widget sends data derived from Figma's APIs to an external backend, the developer must provide documentation of a vulnerability management process. |
| **1c. Are you accredited to any relevant security standards (for example, SOC 2, PCI DSS, HITRUST, ISO27001, and SSAE 18)?** | If the plugin or widget sends data derived from Figma's APIs to an external backend, the developer must identify and provide documentation of the security standards that are met. |
| **2. Does your plugin or widget make network requests with services you don’t host?** | Ideally, the plugin or widget does not make any network requests. If network requests are made, no data derived from Figma's APIs is sent in the requests.  If the plugin or widget makes network requests that send data derived from the Figma APIs, the developer must describe why the data is required. |
| **3. Does your plugin or widget have user authentication?** | Ideally, if the plugin requires the user to authenticate, it does so through a security service such as Auth0 or Google. |
| **3b. Describe how you keep user credentials secure (for example, credential storage, password constraints, verification systems, etc.)** | If the plugin or widget hosts its own authentication service, the developer must describe how user credentials are secured. |
| **4. Do you store any data read or derived from Figma’s plugin or widget API?** | Ideally, the plugin or widget doesn't store any data derived from the Figma APIs, or uses the storage options provided by Figma. |
| **4b. Please describe how and where this data is stored** | If the plugin or widget stores data derived from the Figma APIs in a location outside Figma, the developer must:   - Describe how and where the data is stored - Disclose the same information in the privacy policy that the developer makes available as a part of their authentication process |
| **4c. Describe who can access this data and any relevant data handling policies** | If the plugin or widget stores data derived from the Figma APIs in a location outside Figma, the developer must describe who has access to the data and how the data is handled. |
| **5. How do you manage updates to your plugin?** | Describe how updates to the plugin or widget are handled. |
