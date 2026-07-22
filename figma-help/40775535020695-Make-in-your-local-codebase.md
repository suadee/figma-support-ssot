---
기술지원명: Make in your local codebase
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Make in your local codebase
출처링크: https://help.figma.com/hc/en-us/articles/40775535020695-Make-in-your-local-codebase
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

This feature is currently available to try for free in closed beta for a limited number of users. [Learn more.](#h_01KSPSHEJG5G8DDRBVQN0NXP0Z)

You can use Figma Make to ship the UI changes you want directly into your team's real codebase. Connect a GitHub repository to Figma Make and edit the running app directly. Your app opens inside Make with real data, and you can change the UI by adjusting properties in a panel, annotating elements, or describing changes in chat. The agent updates the code, and when you're ready, you can create a branch and open a pull request without leaving Figma.

**Tip:** For a great rundown of all the new functionality available in the closed beta, see [Figma Make, now on your local code](https://www.figma.com/blog/figma-make-now-on-your-local-code/) in the Figma blog.

## Work with Make in your local codebase

Here's a quick overview of how to use the Figma Beta desktop app version of Make in your local codebase:

### **Work directly with real code**

[](https://help.figma.com/hc/article_attachments/40790434027927)

Connect a local repository or clone one from GitHub. Your app opens inside Make with real data, exactly as your users see it.

### **Manage branches right in Figma Make**

[](https://help.figma.com/hc/article_attachments/40790418758679)

Create, switch, and work on branches directly from Make. Your changes stay on your local machine until you push.

### **Commit to your codebase**

[](https://help.figma.com/hc/article_attachments/40790434027799)

Each prompt that changes code is saved as a local commit, so you can step back through your work. When you're ready, open a pull request for your engineering team to review.

### **Annotate your UI to prompt**

[](https://help.figma.com/hc/article_attachments/40790434024471)

Drop annotations directly on the rendered UI to describe what you want changed. Stack several annotations across the screen and submit them together as a single prompt.

### **Point to edit your interface**

[](https://help.figma.com/hc/article_attachments/40790418755095)

Select any element in your live app and adjust its properties in the editing panel. Change layouts, colors, fonts, and spacing without writing a prompt.

## Get access

To apply for access, join the waitlist at [figma.com/join-waitlist-make](https://www.figma.com/join-waitlist-make/). Joining the waitlist doesn’t guarantee you’ll get access to the closed beta.

After you sign up at [figma.com/join-waitlist-make](https://www.figma.com/join-waitlist-make/), you’ll receive a confirmation email at the address tied to your Figma account. If you didn't get one, submit the form again. The original submission may not have gone through.

When your access is ready, you'll receive an email at the address on your Figma account.

The closed beta for using Make in your local codebase is **Mac-only**. You’ll need to use the Figma Beta desktop app for Mac.

For more information, see our [FAQs](https://help.figma.com/hc/en-us/articles/40789739982871#h_01KSPPBQXHZ0RP7DPXBQHXMDA9).

## Setup, gotchas, and troubleshooting

When you’re setting up Make for your codebase, because this feature is in closed beta, you may have questions or encounter unexpected issues. We provide a comprehensive set of guidance and answers in [Make in your codebase: Setup, gotchas, and troubleshooting](https://help.figma.com/hc/en-us/articles/40789739982871).

## Set up Make for your codebase

This article covers setup for designers and PMs, and a separate section for the engineer who configures the repository.

### Before you start

You need the following to use Make with your codebase during the closed beta:

- The [Figma Beta desktop app](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app#Download_the_beta_version) for Mac
- A Figma account that has been admitted to the closed beta
- Your organization has [AI features enabled](https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization#h_01J0SNQBZ9JXM4T45V5QWZ2QFZ)
- A codebase hosted in a Git repository
- Access to the repository through your version control provider

GitHub is natively supported in the Figma Beta desktop app. GitLab and Bitbucket are partially supported through SSH.

**Note:** Each repository needs a one-time setup by an engineer on your team before designers and PMs can use it in Make. See [Configure a repository for Make](#h_01KSPN2MGT210RJHZJEG0RHCJG) below.

Once your account has been admitted to the closed beta, you’re ready to get started. Choose one of the following methods:

- [Start from a local repository](#h_01KSPVV8KSB7132SPB8GTZ19HR): If you’re already working with code locally, such as with an app you’re building or one of your organization’s repositories, you can start using Make with that repository.
- [Start by cloning a repository](#h_01KSPVV8KYS9HD8NRJ1T26SA8E): You can use Make to clone a repository from GitHub. When you clone a repository, Make pulls down the remote code so you can start working with it locally. This is a good way to get started if your organization has a repository you want to work with.

### Start from a local repository

Here’s how to set up Make with one of your local repositories for the first time. After following these steps, you start new sessions for the repository without needing to set it up again.

1. Open the Figma Beta desktop app.
2. Create a Figma Make file. In the file browser, navigate to your drafts. Then, in the upper-right corner, click **Make**.
3. Under the prompt box, click **Open a folder**.
4. Click **New session**.
5. Make will add required configuration files to your repository. When you’re prompted in Make, click **Run** to add the files. You may be prompted to click **Run** more than once.
6. If your local repository isn’t using git yet, you can add git-based version control. Above the prompt box, next to **Initialize git for version control**, click **Run**.

   **Note:** If the repository already has the `.figma/make` configuration files, Make installs dependencies, starts the dev server, and loads the preview automatically. If it does not, the chat will guide you through the next steps.

After completing these steps, the preview of your app loads, displaying the live, local version of the interface. You’re ready to start making changes to your app in Make.

### Start by cloning a repository

Here’s how to set up Make with a remote repository. As a part of this setup, Make will clone the remote repository, enabling you to work with it locally.

1. Open the Figma Beta desktop app.
2. Create a Figma Make file. In the file browser, navigate to your drafts. Then, in the upper-right corner, click **Make**.
3. Under the prompt box, click **Clone a repository**.
4. In the **Repository URL** box, enter or paste the URL for the remote repository.

   **Note:** The URL must be for a public repository or a private repository you have access to within the connected GitHub organization or account.
5. For **Local folder destination**, select a folder for the repository. Make pulls the files from the remote repository into the local folder you select.
6. Click **Clone**.
7. Make will add required configuration files to your repository. When you’re prompted in Make, click **Run** to add the files. You may be prompted to click **Run** more than once.

   **Note:** If the repository already has the `.figma/make` configuration files, Make installs dependencies, starts the dev server, and loads the preview automatically. If it does not, the chat will guide you through the next steps.

After completing these steps, the preview of your app loads, displaying the live, local version of the interface. You’re ready to start making changes to your app in Make.

To find your repository URL in GitHub, go to the web version of the repository on GitHub. Then, at the top of the repository page on GitHub, click **Code** and copy the repository URL under **HTTPS**.

**Troubleshooting: Make can't clone the repository.**

This usually means authentication failed. Confirm that you have access to the repository through your version control provider, and that your SSH key or GitHub credentials are set up on your machine. See [Install the Figma GitHub app](#h_01KSPN2MGTQN9XMZ7ARXHJ8FWS) and [Authenticate with GitHub](#h_01KSPN2MGT4AQSF08BA5NGPVW8).

### Install the Figma GitHub app

To use GitHub with Make, a GitHub org admin installs the Figma GitHub app for your organization. This is a one-time setup per organization. Once it's installed, every person on your team can authenticate with GitHub on their own, without admin involvement, terminal access, or SSH keys.

To install the app, your GitHub org admin visits <https://github.com/apps/figma/installations/new>.

**Version control provider support during the closed beta:**

- **GitHub:** Fully supported, including cloning, pushing branches, and creating pull requests.
- **GitHub Enterprise Cloud:** Supported.
- **GitHub Enterprise Server:** Not supported.
- **GitLab and Bitbucket:** Partially supported through SSH. Cloning works via SSH (not HTTPS), and pushing branches works, but pull request creation does not. Users on GitLab or Bitbucket set up their own authentication, such as a local SSH key.

For information about uninstalling the Figma GitHub app, see [Manage the Figma Github app for a team or organization](https://help.figma.com/hc/en-us/articles/37516294384919).

**Note:** Organizations that require authentication through a corporate-approved browser, hardware key, or other restricted auth flow may not be able to complete the GitHub login flow inside Make. This limitation applies to other agentic coding tools as well.

### Authenticate with GitHub

The first time you push a branch or create a pull request, Make prompts you to authenticate with GitHub. Sign in through the prompt to give Make permission to push branches and open pull requests on your behalf.

**Note:** Pull request creation in Make is only supported for GitHub during the closed beta. GitLab and Bitbucket users can push branches and open pull requests in their provider's interface.

## Configure a repository for Make

Each repository needs a one-time setup before it can be used in Make. This step is typically done by an engineer on your team and only needs to happen once per repository.

To ease using the repository, the configuration files should be committed and pushed to the main branch of the repository. This ensures that Make doesn’t need to reapply the configuration files when a branch is switched or the repository is pulled elsewhere. Once the folder is committed to your main branch, every designer and PM on the team can open the repository in Make without further setup.

### Automatic setup

The first time a repository is used in Make, the required configuration files will usually be automatically added to the local repository as part of the setup.

Simply commit and push the configuration files to the main branch of the repository.

### Manual setup

If preferred, an engineer on your team can manually add the configuration files.

The configuration must be created in a `.figma/make` folder at the root of the repository.

The folder contains five files:

| File | Purpose | Runs |
| --- | --- | --- |
| `setup` | Installs system dependencies, such as databases and language toolchains | The first time Make sees the repository |
| `install` | Installs project dependencies, such as packages and libraries | At the start of every Make session |
| `dev` | Starts the development server | After `install`, at the start of every Make session |
| `verify` | Checks whether the development server is ready to serve requests | After `dev` |
| `env` | Defines environment variables and tells Make which port and URL the dev server uses | Read by Make when the session starts |

The `setup`, `install`, `dev`, and `verify` files are shell scripts. They must return exit code `0` on success and any other value on error. Scripts should be idempotent. For example, the `setup` script should check whether a dependency is already installed before installing it.

#### .figma/make/setup

Use this script to install system dependencies such as databases and language toolchains.

```
#!/bin/bash
set -e

echo "Checking system dependencies..."

NODE_VERSION="$(node --version 2>/dev/null || echo "none")"
if [[ "$NODE_VERSION" == "none" ]]; then
  echo "Installing node"
  brew install node
fi
echo "Node $NODE_VERSION OK"

echo "System dependencies verified."
```

#### .figma/make/install

Use this script to install project dependencies.

```
#!/bin/bash
set -e

echo "Running npm install"
npm install
echo "Dependencies installed"
```

#### .figma/make/dev

Use this script to start the development server. Make runs this process in the background and terminates it when the session ends.

```
#!/bin/bash
set -e

echo "Starting development server"
npm run dev
```

#### .figma/make/verify

Use this script to check that the development server is ready to serve requests. The script should wait for the server to come up, then return exit code `0`. It should return a non-zero exit code if the server fails to start within a reasonable time.

```
#!/bin/bash
set -e

HEALTHCHECK_ENDPOINT='http://localhost:3000/health'
MAX_WAIT=120
INTERVAL=2
ELAPSED=0

echo "Waiting for development server to be ready"

while [ $ELAPSED -lt $MAX_WAIT ]; do
  if curl -sf $HEALTHCHECK_ENDPOINT >/dev/null 2>&1; then
    echo "Dev server is up"
    exit 0
  fi
  sleep $INTERVAL
  ELAPSED=$((ELAPSED + INTERVAL))
done

echo "Error: Dev server did not start within ${MAX_WAIT}s"
exit 1
```

#### .figma/make/env

This file follows the envfile format and serves the following purposes:

- Define any environment variables that should be passed to your development server when running .figma/make/dev.
- Telling Make the port and url your development server uses to fulfill requests
  - `PORT` and `FIGMA_MAKE_URL` are mandatory.
- `BOOTSTRAP_TIMEOUT` is an optional param to decrease the timeout

```
PORT=3000
FIGMA_MAKE_URL=http://localhost:3000
BOOTSTRAP_TIMEOUT=60000
```

#### Commit the configuration

Once the five files are in place, commit the `.figma/make` folder to your main branch. Every branch created from main will inherit the configuration, and designers and PMs on the team can start sessions without further setup.

## Troubleshoot setup

If you run into issues while trying to set up Make with one of your local repositories, see [Make in your local codebase: Setup, gotchas, and troubleshooting](https://help.figma.com/hc/en-us/articles/40789739982871).
