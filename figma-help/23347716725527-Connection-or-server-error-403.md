---
기술지원명: Connection or server error 403
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Connection or server error 403
출처링크: https://help.figma.com/hc/en-us/articles/23347716725527-Connection-or-server-error-403
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Error 403 is a web server error that’s generally related to permissions. In Figma, this more commonly happens in the desktop app, and can have a few root causes:

## Common causes and solutions

### You have been signed out of Figma

The most common cause of a 403 error is that you have been signed out of your Figma account.

How do I check if this is my issue?

Visit [figma.com/login](https://figma.com/login) and make sure you're signed in to your account.

How do I fix it?

Visit [figma.com/login](https://figma.com/login) and [log in to your Figma account](https://help.figma.com/hc/en-us/articles/360041064554). If you’re already logged in, try the next steps.

### You’re accessing Figma using a VPN, firewall, or proxy

If you're using the desktop app behind a firewall, proxy, or Virtual Private Network (VPN), you will see the error message: Connection Error (407).

How do I check if this is my issue?

Contact your IT department or systems administrator to see if this applies to you, or try using a different network.

How do I fix it?

You have two options:

- Use Figma in the browser. You can access the Figma web app from any of our supported browsers. [What browsers does Figma support?](https://help.figma.com/hc/en-us/articles/360039827194)
- Ask your IT department or systems administrator to **unblock Port 443**. This is the standard port for websites that are run over SSL (Secure Sockets Layer).

### Network settings may be blocking the connection

If you're using the desktop app behind a firewall, proxy, or Virtual Private Network (VPN), you will see the error message: **Connection Error (407)**.

How do I check if this is my issue?

Try a different network, like another wifi connection or mobile hotspot. If you’re trying to use the Figma desktop app on a work-managed computer, ask your IT department if any network settings are blocking Port 443.

How do I fix it?

You have two options:

- Use Figma in the browser. You can access the Figma web app from any of our supported browsers. [What browsers does Figma support?](https://help.figma.com/hc/en-us/articles/360039827194)
- Ask your IT department or systems administrator to **unblock Port 443**. This is the standard port for websites that are run over SSL (Secure Sockets Layer).

### There’s an issue with cached permissions

Cached permissions on your device can sometimes prevent you from accessing files you previously did not have access to, but have since been given permission to edit.

How do I check if this is my issue?

Does the issue occur across all browsers, as well as the desktop app? If this only occurs in one place, there is an issue with the cached permissions.

How do I fix it?

[Clear the cache for the Figma desktop app](https://help.figma.com/hc/en-us/articles/22380853110551) or browser. Once cleared, log out and back in to Figma.

### Your access to the file has been removed

You may encounter an error if your access to a file has been removed.

How do I check if this is my issue?

If you do not own the file, reach out to the file owner to confirm or request access.

How do I fix it?

Reach out to the file owner to request access.

### The file may have been deleted

How do I check if this is my issue?

Check deleted files and [restore deleted files](https://help.figma.com/hc/en-us/articles/360047512294) if needed. If you do not own the file, ask the owner to check if the file has been deleted or if your access has been removed.

How do I fix it?

If a file's original project still exists, anyone with `can edit` access can restore a file. This will also restore the file for anyone who had access to it at the time of deletion.

Restoring a file retains the [permissions](https://help.figma.com/hc/en-us/articles/360039970673), [comments](https://help.figma.com/hc/en-us/articles/360041068574), [version history](https://help.figma.com/hc/en-us/articles/360038006754), and [library connections](https://help.figma.com/hc/en-us/articles/360041051154-Guide-to-libraries-in-Figma) of the original file.

To restore a file:

1. Locate the file you want to restore on the **Deleted**tab.
2. Right-click on the file and select **Restore**.

**Note:** The restore option does not display if you had `can view` access to a file. If its parent project gets deleted, then you won't be able to restore the file to its original location. Instead, you can duplicate the file your **Drafts**.
