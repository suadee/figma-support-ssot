---
기술지원명: Push from Figma Make to GitHub
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Push from Figma Make to GitHub
출처링크: https://help.figma.com/hc/en-us/articles/35463818346647-Push-from-Figma-Make-to-GitHub
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Figma Make is available for [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on paid plans.

You can try Figma Make on other seats and plans.

Push to GitHub is available on all plans.

To let you back up your code, track changes, and continue working in your preferred development tools, you can push your Make projects directly to GitHub.

Using Figma Make you can:

- Connect your GitHub account to Make
- Push updates from Make to your linked repository when your file changes

To push from Figma Make to GitHub, you first need to [connect your GitHub account or organization](#h_01K7GNYV5TQTNP05MXS13QD924). Then, you can use Figma Make to create new GitHub repositories and [push your code to GitHub](#h_01K7GPNZVXPBPV03VQS24JQGHD).

## Connect to GitHub

When you set up the GitHub integration for the first time, you'll need to connect Figma Make to GitHub. This step only needs to be performed once for your team or organization.

**Important:** When you connect to GitHub, the connection is for your whole team or organization. For example, when you connect a GitHub account or organization to your Figma organization, all teammates with access to Figma Make will be able to create and push to repositories. You can't connect multiple GitHub accounts or organizations to a single Figma team or organization.

To connect Figma Make to GitHub:

1. Open an existing Figma Make file or create a new one.
2. In the upper-right corner of Figma Make, click  **Make settings**, and then click **GitHub**.
3. In the **Connect to GitHub** modal, click **Connect GitHub**.
4. In GitHub, you're prompted to select which account or organization you want to connect to Figma Make. Select the account or organization you want to connect.
5. When prompted, select whether you want to authorize the Figma GitHub app for all repositories or just for selected repositories. This step doesn't have any functional effect, but is required by GitHub. Figma Make never accesses repositories other than the ones it creates via the integration.
6. Click **Install & Authorize**. If prompted, re-authenticate with GitHub.

When you complete the last step, you're sent back to your Figma Make file and you're ready to start pushing code to GitHub.

## Push to GitHub

To push code to GitHub:

1. Go to the Figma Make file that has code you want to push to GitHub.
2. In the upper-right corner of Figma Make, click  **Make settings**, then select **GitHub**.
3. If it's the first time you're pushing from the Figma Make file to GitHub, select **Create Repository**, enter a name for your repository, and click **Create**.
4. Each subsequent time you want to push to GitHub, in the  **Make settings** menu, select **GitHub** **>** **Push to...**. Figma Make pushes to the same repository it created for your file.

## View a GitHub repository

To view the GitHub repository connected to a Figma Make file:

1. Go to the Figma Make file that's connected to the repository you want to view.
2. In the upper-right corner of Figma Make, click  **Make settings**, then select **GitHub** **>** **View...**.

## FAQs

### Can I push changes to an existing repo?

You can't push to GitHub repos you've created yourself. Figma Make only pushes to repositories it creates. When you push from a Figma Make file for the first time, a corresponding repository is created in GitHub. Any subsequent push will update that same repository.

Each Figma Make file you push from gets its own repo. You can't push from one Figma Make file to a repo created by another Figma Make file.

### Does the Push to GitHub feature include two-way sync?

No. It’s a one-way push from Figma Make → GitHub. If you edit your code in GitHub, those changes won’t appear in Figma Make and will be overwritten next time you push from Figma Make to GitHub.

### Which branch does Make push to?

When you push, the changes always go to the repository's default branch. This is usually `main`, unless the repository's default branch has been changed. Branch management isn’t supported at this time.

### Is GitHub Enterprise Server (GHES) supported?

Currently, GitHub Enterprise Server isn't supported. You can't connect Figma Make to a GHES instance.

### Why can’t I connect the app when using GitHub IP allow lists?

The Figma GitHub App doesn’t support GitHub IP allow lists.
