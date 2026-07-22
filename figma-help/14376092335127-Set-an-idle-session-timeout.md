---
기술지원명: Set an idle session timeout
카테고리: 보안
작성자: Figma
승인자: suadee
출처: Set an idle session timeout
출처링크: https://help.figma.com/hc/en-us/articles/14376092335127-Set-an-idle-session-timeout
게시일: 2026-07-22
검토일: 2026-07-22
---

## 내용

Who can use this feature

Available on the
[Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273).

Organization admins only.

By default, Figma automatically logs users out when they are inactive for 21
days. For added security, organization admins can set an idle session timeout
to log inactive users out earlier.

**More details**

- You can log out users as soon as 12 hours, or as long as 14 days, after they
  become inactive.
- Idle session timeouts only affect **members** of an organization
  and not **guests**.
- When a session times out, users are logged out on every platform they are inactive in, including
  web browsers, desktop apps, mobile apps, embeds, and integrations like
  [Microsoft Teams](https://help.figma.com/hc/en-us/articles/7405452518423).
- Users get a prompt to stay logged in when they are less than one minute away
  from their session timing out. If the session times out, users will need
  to log back in to access their files.
- If a user is part of multiple organizations that have session timeouts enabled,
  the shortest session timeout will apply.

**Note:** Figma's
[activity log](https://help.figma.com/hc/en-us/articles/360040449533)
captures changes to the session timeout policy, as well as each time
a member is logged out due to a timeout.

Timeouts from an open web browser or the desktop app are logged immediately,
while timeouts that happen in the background are logged the next time
the user accesses Figma.

### Set an idle session timeout

1. From the
   [file browser](https://help.figma.com/hc/en-us/articles/14381406380183),
   click 
   **Admin**.
2. Select the **Settings** tab.
3. Under **Login and provisioning**, click
   **Session timeout**.
4. Click **Custom timeout**.
5. Choose a timeout length and click **Save**.

**Note:** When you set a new idle session timeout, Figma
resets inactivity for everyone in your organization and will only log
users out when they have been inactive for longer than the new timeout
period.

If anyone in your organization can't log back in to Figma after their
session times out, please ask them to
[contact support](https://help.figma.com/hc/en-us/requests/new?ticket_form_id=360001731233).
