---
기술지원명: Make in your local codebase: Setup, gotchas, and troubleshooting
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Make in your local codebase: Setup, gotchas, and troubleshooting
출처링크: https://help.figma.com/hc/en-us/articles/40789739982871-Make-in-your-local-codebase-Setup-gotchas-and-troubleshooting
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

This feature is currently available to try for free in closed beta for a limited number of users. [Learn more.](https://help.figma.com/hc/en-us/articles/40775535020695#h_01KSPN2MGSG5Q5J870HK6ECEZ0)

Get answers to common questions about using Figma Make with your codebase.

For setup instructions, see [Make in your local codebase](https://help.figma.com/hc/en-us/articles/40775535020695).

## Using Make in your local codebase

### You need access to a repository

When you're working with a codebase, you need access to the repository that contains the code. If it's a public repository or you've created the repository yourself, you're all set. If you're using Make to [clone a private repository](https://help.figma.com/hc/en-us/articles/40775535020695-Make-in-your-local-codebase#h_01KSPVV8KYS9HD8NRJ1T26SA8E) in your GitHub organization, ensure you have access to the repository.

For example, if someone gives you a URL for a private repository to use in Make, you must also have access to the repository in the GitHub organization. Otherwise, Make will be unable to clone the repository for you.

**What to do:** Try to go to the repository URL in your browser. If you encounter a `404` error, you should ask the owner of the repository or an admin in your GitHub organization to give you access.

### Your repository needs `.figma/make` config files

Make creates config files at `.figma/make` in order to set up and run your project. Generally, Make will set up these files automatically. If these don't exist yet, Make will show a **"Couldn't load preview"** state.

**What to do:**

- Try prompting Make to create the `.figma` config files for you.
- If setup fails, try clicking the **Fix for me** button that appears above the prompt box.
- If you're an engineer setting up a repository for others: commit the `.figma/make` config to `main` so that everyone inherits it automatically on every branch. See the configuration instructions in [Make in your local codebase](https://help.figma.com/hc/en-us/articles/40775535020695).

### Wait a moment after setup completes before making changes

For some repos, Make responds that setup is complete as soon as your dev server responds. However, background build tasks (like generating registry files in shadcn-based repos) may still be running. If you start making changes immediately, Make may auto-commit a large number of temporary or unwanted files.

**What to do:** Wait 30 to 60 seconds after setup is completed and the preview appears before sending your first prompt, especially on a slower machine.

### Config files are branch-specific, not global

When Make first sets up the config files for a repository, those files live in a branch, not globally.

**What to do:** Make sure `.figma/make` config files are committed to `main`. In the future, any branch created from `main` will automatically have them.

### You'll need SSH authentication for GitLab or Bitbucket set up

Make provides some support for SSH for GitLab and Bitbucket. If you haven't configured  
 SSH before, this is a required one-time setup step. You only need to do this if you're using a provider other than GitHub.

**What to do:** Follow the provider’s SSH setup guide to generate and add an SSH key. If you're not sure where to start, ask an engineer to pair with you — this is the most common first-time blocker for designers.

---

## Preview and localhost

### The preview might show the wrong project

If you have another dev server already running on port 3000 (e.g., from a different project open in VS Code), Make may load that project's preview instead of yours. This can look alarming, like Make is reaching across your computer.

**What to do:** Before starting a session, close any other dev servers running on the same port. You can check which port your project uses in your `.figma/make` config or `package.json`.

### The preview doesn't always load automatically after setup

After Make finishes the setup for your local repository, Make may not automatically navigate to your dev server in the preview panel, leaving a blank or stuck preview.

**What to do:** If the preview doesn't load on its own, manually type your dev server URL (e.g., `http://localhost:3000`) into the preview bar. You can ask Make what the URL should be.

### Preview is blank or infinitely loading

Possible causes:

- Setup scripts didn't finish successfully (errors may have run silently)
- Your dev server is waiting for an interactive prompt (e.g., Payload CMS asking to confirm a schema migration) that Make has no way to surface
- A race condition on first load (usually fixed by reloading)

**What to do:**

1. Try starting a new session:
   1. In the upper-right corner, click  next to the name of your Make file.
   2. Select **Switch session**, then **New session**.
2. If it persists, open a separate terminal and run your dev server manually to see if it prompts for input.
3. If your dev server requires interactive confirmation on startup, modify your setup script to handle those prompts non-interactively (e.g., pass `--yes` flags or pre-seed environment variables).

### The preview shows something other than the dev server

Make in the Figma Beta app lets you browse to sites other than your dev server. To return to your dev server in Make, use the back button in the address bar of the preview or close and re-open the Make file.

---

## Common errors

### "Failed to start session"

One of the most common errors. It usually means something went wrong during setup.

**What to do:**

1. Ask Make to identify the errors.
2. [Submit a bug report.](#h_01KSPPBQXHAJV6BX28Q9H6VS04)

### "Something went wrong" and "Try again" does nothing

This tends to be repository-specific. To narrow it down, try opening a different repository to see if the issue follows the repository or the app.

**What to do:** Submit a bug report with debug logs so the team can investigate. [Submit a bug report.](#h_01KSPPBQXHAJV6BX28Q9H6VS04)

---

## Submit a bug report

### Use the built-in bug report feature

You can submit a bug report directly from Make. At the top of Make in the Figma Beta desktop app, click **Feedback** and select **Bug report**.

The bug report collects everything Figma needs:

- Session logs and conversation transcript
- Bootstrap scripts and current git state
- Environment variables and runtime versions
- System info (OS, CPU, GPU, memory)

Submitting a report automatically creates a support ticket with all logs attached, which dramatically speeds up resolution.

---

## FAQs

### Access

#### How do I get access?

Join the waitlist at [figma.com/join-waitlist-make](https://www.figma.com/join-waitlist-make/). Access rolls out in waves by organization. When your access is ready, you'll receive an email at the address on your Figma account.

#### How do I know if I'm on the waitlist?

If you signed up at [figma.com/join-waitlist-make](https://www.figma.com/join-waitlist-make/), you should have received a confirmation email at the address tied to your Figma account. If you didn't get one, submit the form again. The original submission may not have gone through.

#### My teammate has access. Why don't I?

Access rolls out by organization, in batches. When your organization is admitted, you'll receive an email. There's no way to skip the waitlist for individual accounts. You can [download the Figma Beta desktop app](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app#Download_the_beta_version) ahead of time so you're ready when your access is ready.

#### Can I move my access to a different account?

No. Access is tied to the Figma account that was admitted from the waitlist. To use a different account, join the waitlist again with that account at [figma.com/join-waitlist-make](https://www.figma.com/join-waitlist-make/).

#### When will it be generally available?

Plans for broader access will be shared when they're finalized. When the open beta begins, the waitlist no longer applies.

### About the feature

#### How does Make work in your codebase?

Figma Make can now connect to a Git repository and edit the running app directly. Your app opens inside Make with real data, and you can change the UI by adjusting properties in a panel, annotating elements, or describing changes in chat. The agent updates the code, and when you're ready, you can create a branch and open a pull request without leaving Figma.

Make also supports prototyping for exploring new UI ideas without a codebase. See [Explore Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make) for more on that workflow.

#### What's the difference between working with my codebase and prototyping in Make?

Prototyping in Make is for exploring new UI in a sandbox. No codebase is required, and nothing you make is committed anywhere.

Working with your codebase means your changes become real commits and pull requests in your project. Your live app renders in Make with real data, and the agent updates your code in place.

Most teams use both. Prototype when you're exploring an idea, and work with your codebase when you're shipping changes.

#### Do I need to know how to code?

No. After an engineer on your team completes the one-time setup for your repository, you can open Make, see your live app, and make changes three ways: adjust layouts, colors, fonts, and spacing in the editing panel, drop annotations on specific elements, or describe what you need in chat.

### Requirements and limitations

#### What frameworks and languages does Make support?

Make works with any web framework and language. React, Vue, and Svelte are verified, and other web frameworks also work.

Make is not intended for backend work, infrastructure changes, native mobile, or non-web codebases during the closed beta.

#### What version control providers are supported?

GitHub is natively supported in the Figma Beta desktop app, including cloning, pushing branches, and creating pull requests. GitHub Enterprise Cloud is supported. GitHub Enterprise Server is not.

GitLab and Bitbucket are partially supported through SSH. You can clone via SSH (not HTTPS) and push branches, but pull request creation is not supported. GitLab and Bitbucket users must open pull requests in their provider's interface.

#### What can I build with Make in my codebase?

Make is designed for UI changes to existing screens. Examples include layout adjustments, component swaps, spacing and color fixes, implementing a new design from a Figma frame, and iterating on a feature without handing it off to engineering for every small change.

Make is not intended for major architectural changes, building a new application from scratch, backend or API work, or infrastructure changes.

#### Is it safe to use Make on production repositories?

Yes. Make doesn't merge code on its own. Changes stay on your local machine until you push a branch, and pull requests follow your team's normal code review and deployment process.

#### What are the known limitations during the closed beta?

- Mac only. Windows support is planned.
- GitHub is natively supported in the UI. GitLab and Bitbucket connect through SSH.
- Access is by waitlist. Not everyone on the waitlist will get access during the closed beta.
- While most repositories can be automatically configured, some may require a one-time engineering setup.
- Large refactors that span many files work better with explicit chat prompts than with the editing panel alone.
- Performance on very large repositories can vary. Pointing Make at a single package, such as a design system or component repository, gives better results.
- Organizations that require authentication through a corporate-approved browser, hardware key, or other restricted auth flow may not be able to complete the GitHub login flow inside Make.

### Plans and pricing

#### Is Make free during the closed beta?

Yes. The codebase capabilities are free during the closed beta.

#### What seat do I need?

Seat requirements for these capabilities are still being finalized. During the closed beta, access is granted by waitlist and is not tied to a specific seat tier.

#### Will this become a paid feature?

Pricing for the open beta and general availability has not been announced.
