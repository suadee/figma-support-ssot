---
기술지원명: Add a backend to a functional prototype or web app
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Add a backend to a functional prototype or web app
출처링크: https://help.figma.com/hc/en-us/articles/32640822050199-Add-a-backend-to-a-functional-prototype-or-web-app
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Figma Make is available for [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on paid plans.

You can try Figma Make on [other seats and plans](https://help.figma.com/hc/en-us/articles/31722591905559-Figma-Make-FAQs#h_01JZQX7SQ7RX4SJ65DHDTYS2EK).

When creating a prototype or web app using Figma Make, there are times you'll need to securely store and manage data by [adding a backend](#h_01JZV9T8CDD78K561XPWRHBJ42). For example, you’ll need a backend when you want to:

- Maintain the state of an app across different browsers
- Provide working authentication flows, such as a login screen for your app
- Collect user input and responses to forms
- Save and load content, like text and images
- Store secrets, API keys, and tokens for making requests to servers

Figma Make integrates with Supabase to provide a backend environment that offers secret storage, compute, and a Postgres database. Figma Make will set up basic key-value stores inside this Postgres database; at the moment, Figma Make will not set up a full SQL database in the Postgres provided by Supabase.

You can bring your own existing Supabase account to Figma Make. If you don’t have an account, Figma Make will walk you through how to get started.

Once your account is ready, Figma Make will guide you through the steps to connect a Supabase project to your app.

Figma Make remembers Supabase projects that you’ve previously connected to, so you can more easily reuse Supabase projects throughout your Figma Make files.

Once you have a backend, you can also [add secrets and API keys](#h_01JZV9T8CNYZH9K10N8P8R6Q44) that can be used to query external servers.

For more information, check out our [best practices](#h_01JZV9T8CSSMPRREZ2H39NQ5C6) and [example prompts](#h_01JZV9T8CS9VA8B6HD0QDYW6SW). Additionally, organization admins are able to [manage backend integration](https://help.figma.com/hc/en-us/articles/34162517434007) for Figma Make.

## Backends

When working with backends in your Figma Make files, you can:

- [Add a backend](#h_01JZV9T8CDD78K561XPWRHBJ42)
- [Add a secret or API key](#h_01JZV9T8CNYZH9K10N8P8R6Q44)
- [Manage Supabase secrets, projects, and organizations](#h_01JZV9T8CRNHQHMREZP2BTME7C)

## Add a backend

There are two ways to enable the Supabase integration that adds a backend to your functional prototype or web app:

- Figma Make will automatically recommend adding a backend based on the intent of your prompts in the AI chat. You can also explicitly prompt to add a backend, using a prompt like "Add authentication to my app."
- In the settings of your Figma Make file, connect Supabase.

You can use either method in your Figma Make files. You won’t use both methods in the same file, as you only need to set up a backend once per file.

### Prompt to add a backend

To add a backend using the AI chat:

1. In the AI chat, tell the model to add a backend to your functional prototype or web app. This can be as simple as "Add a backend", "Add user sign-in", or "Call [a secure API, like OpenAI]".
2. When Figma Make asks you to set up your Supabase account, click **Connect**. This step only occurs the first time you’re setting up the Supabase integration.

   In a new browser tab, you’re directed to the Supabase website.

   When you’re prompted to log in to Supabase, use your existing account or create a free account.

   If your Supabase account isn’t already associated with an organization, Supabase also prompts you to create an organization.
3. On the **Authorize API access for Figma** page, select an organization and click **Authorize Figma**.

   **Note:** This is a one-time step for each Figma organization or Pro team you're in. In future files, when Figma Make wants to connect to Supabase, the Supabase account and organization you specified will be used. You can't provide different Supabase organizations for different Figma Make files.

   In your browser, the Supabase tab closes and you’re directed back to Figma Make.
4. If you already have an existing Supabase project, click **Choose a project,** then click **Connect** next to the project you want to use for the Figma Make file.

   If you don’t have any Supabase projects, click **Create project**. Then, in the **New Supabase project** modal, enter a project name, select the region where you want the Supabase project hosted, and create a password for your database.

   **Note:** The database password is not the same as your Supabase account password. The database password is used for accessing the Postgres database in your Supabase project. You likely won't need to use this password while working in your Figma Make file, but Supabase requires that your database have a password.
5. Click **Create project**.

Once your Supabase project is connected to the Figma Make file, you’re all set! In the AI chat, you can tell the model the functionality you want to build, such as a form to collect user input, and the model will handle implementing the functionality for you.

### Add a backend in the file settings

To add a backend in the settings of your Figma Make file:

1. In the upper-right corner of your Figma Make file, click  **Make settings**.
2. In the left sidebar, under **Integrations**, click **Supabase**.
3. Click **Connect Supabase**. This step is only required the first time you’re setting up the Supabase integration.

   In a new browser tab, you’re directed to the Supabase website.

   When you’re prompted to log in to Supabase, use your existing account or create a free account.

   If your Supabase account isn’t already associated with an organization, Supabase also prompts you to create an organization.
4. On the **Authorize API access for Figma** page, select an organization and click **Authorize Figma**.

   **Note:** This is a one-time step for each Figma organization or Pro team you're in. In future files, when Figma Make wants to connect to Supabase, the Supabase account and organization you specified will be used. You can't provide different Supabase organizations for different Figma Make files.

   In your browser, the Supabase tab closes and you’re directed back to Figma Make.
5. If you already have an existing Supabase project, click **Connect** next to the project you want to use for the Figma Make file.

   If you don’t have any Supabase projects, click **Create new project**. Then, in the **New Supabase project** modal, enter a project name, select the region where you want the Supabase project hosted, and create a password for your database.

   **Note:** The database password is not the same as your Supabase account password. The database password is used for accessing the Postgres database in your Supabase project. You likely won't need to use this password while working in your Figma Make file, but Supabase requires that your database have a password.

   Click **Create project**.

Once your Supabase project is connected to the Figma Make file, you’re ready to go back to the AI chat and start working with the model to take advantage of your backend.

## Add a secret or API key

When you’re creating a functional prototype or web app, you may want to be able to get data from external servers. For example, if you have an app that displays weather information to your users, you may use a weather API that requires an API key or access token.

When you’re prompting in the AI chat to create your functional prototype or web app, Figma Make will ask you to set up a backend (if you haven’t done so already), and then provide an interface for you to enter your secret or API key.

![The Create a secret box that contains an input field labeled Add secret details.](https://help.figma.com/hc/article_attachments/33466562810391)

**Caution:** You should only enter your secret or API key into the **Create a secret** box that Figma Make provides while you’re prompting. Do not provide your secret or API key in the actual text of your prompts.

To add a secret or API key:

1. In the AI chat, tell the model that you want to add a secret for your functional prototype or web app. For example: "I want an app that lets me view stock prices. Create a secret to store my API key."
2. In the **Create a secret** box, under **Add secret details**, enter your secret or API key.
3. Click **Create secret**.

When you click **Create secret**, Figma Make will use Supabase to securely store the secret or API key. Then, you can continue to prompt Figma Make to add more features to your functional prototype or web app that take advantage of added secret or API key.

## Manage Supabase secrets, projects, and organizations

Secrets in your backend, as well as your Supabase projects and organizations, are all managed via the Supabase website. Figma Make provides some quick links to get you to the correct pages on the Supabase website.

![](https://help.figma.com/hc/article_attachments/33466301966871)

To manage secrets, projects, and organizations in Supabase:

1. In the upper-right corner of your Figma Make file, click  **Make settings**.
2. In the left sidebar, under **Integrations**, click **Supabase**.
3. In the row for the project connected to your Figma Make file, click the ellipsis icon. Then:
   - Click **Manage project** to go to that project’s Supabase dashboard.
   - Click **Manage organization** to go to your Supabase organization’s settings page.
   - Click **Manage secrets** to go to the Edge Functions database for your Supabase project.

## Best practices for working with backends

Here are some best practices to keep in mind while you’re working with backends in Figma Make:

- Make sure you’re using the Supabase interfaces that Figma Make provides. Don’t include sensitive data, such as secrets or API keys, in the actual, plain text of your prompts.
- Generally, to make most efficient use of your Supabase projects, we recommend that you try to reuse Supabase projects across your Figma Make files.

## Example prompts

Here are some example prompts that you can use to try working with a backend in Figma Make.

### Examples of storing data and state

- "Make a task-tracking app where I can save my tasks. It should include time-tracking functionality so I can enter how long I spent on each task."
- "Create a photo gallery where I can upload images."
- "I'm a product manager at a marketing platform. Create a proof of concept for the campaign comparison tool we're adding. Show how historical campaign data will be stored and how users can select date ranges for comparison."
- "I'm a product manager at an e-learning platform. Make a prototype of the quiz creation tool for our course authoring system. Show how instructors can create a wide range of questions, from free text to multiple choice to sliders. make the quizzes shareable so people playing with the prototype can create their own quiz and share it for feedback."

### Examples of using secrets and API keys

- "Make a music playlist creator that pulls in my listening history from the Spotify API."
- "I need a reading list app that connects to the Goodreads API to pull book information and lets users track their progress."
- "Build a job application tracker that uses the LinkedIn API to import job listings and lets users track application status."

### Examples of adding authentication

- "Create a habit tracker that requires user sign-in and stores streak information in a key-value store."
- "I'm a developer building a SaaS product. Create a user login system. It should support email/password authentication as well as social logins through Google and GitHub, and include password reset functionality."
- "Build a code snippet manager that requires GitHub sign-in and stores snippets in a database."
