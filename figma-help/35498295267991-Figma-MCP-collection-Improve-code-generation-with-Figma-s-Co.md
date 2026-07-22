---
기술지원명: Figma MCP collection: Improve code generation with Figma’s Code Connect UI
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Figma MCP collection: Improve code generation with Figma’s Code Connect UI
출처링크: https://help.figma.com/hc/en-us/articles/35498295267991-Figma-MCP-collection-Improve-code-generation-with-Figma-s-Code-Connect-UI
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

If you wish to get higher quality code generation and improve the precision of the agentic tools, you can use Code Connect to link your design system file in Figma with your codebase.

In this lesson, we’ll explain what Code Connect is, compare the differences between Code Connect CLI and Code Connect UI, walk through the steps to setup Code Connect UI, and how to use it with the Figma MCP server.

**Note:** Code Connect is available on a [Dev or Full seat](https://help.figma.com/hc/en-us/articles/360040328273-Seats-in-Figma#seat-types) on the [Organization, and Enterprise plans](https://www.figma.com/pricing/).

## Code Connect fundamentals

![code connect.png](https://help.figma.com/hc/article_attachments/36500814755863)

Code Connect is a bridge between your codebase and Figma's Dev Mode, connecting components in your repositories directly to components in your design files. When implemented, these connections enhance the [Figma MCP server](https://developers.figma.com/docs/figma-mcp-server)'s ability to guide AI agents with more precise implementation details by giving them direct references to your actual code.

When you inspect an element in Dev Mode, Figma will display some generalized code in the right sidebar. You can choose different languages from the menu, like CSS, or iOS Swift code.

![inspect in dev mode.png](https://help.figma.com/hc/article_attachments/36501147563031)

This code could be helpful for developers when they first started building a design system library in the codebase. However, if you already have one, the code snippet here doesn’t reflect how your code looks like in your codebase.

That’s where Code Connect comes in. If your developers maintain a source of truth for your components in a codebase—with your own naming conventions and syntax—you can use Code Connect to link components in your codebase directly to components in your design files.

And if you’re using the Figma MCP server to build apps using agentic tools like Claude code, Cursor, and VS code, Code Connect can enhance the server’s ability by giving the AI agents direct references to your code for improved results.

## Code Connect CLI and Code Connect UI

There are two ways to use Code Connect to link design components in Figma with a codebase: **Code Connect CLI and the Code Connect UI**.

### Code Connect CLI

[Code Connect CLI](https://developers.figma.com/docs/code-connect/quickstart-guide/), short for “Command Line Interface”, runs locally in your repository and requires API token and npm package installation. It supports property mappings and dynamic code examples, allowing for deeper integration and accuracy. When you connect your Figma component library with your codebase using Code Connect CLI, you can inspect code snippet from the right sidebar which is constructed using the Code Connect template published from the Code Connect CLI setup. This ensures accuracy and consistency during developer handoff.

![code connect cli.png](https://help.figma.com/hc/article_attachments/36502153191447)

### Code Connect UI

[Code Connect UI](https://developers.figma.com/docs/code-connect/code-connect-ui-setup/) is a new way to connect your components using Code Connect. It runs entirely inside Figma and connects directly to GitHub for repository access and mapping context. This makes it easier to scale across both design and engineering teams, and you send design and code context to the agentic tools via the Figma MCP server.

![code connect UI-2.png](https://help.figma.com/hc/article_attachments/36503962018583)

In this lesson, we’ll walk you through all of the necessary steps to connect a codebase in Github to your Figma Design components using **Code Connect UI**. To learn more about the differences between Code Connect CLI and Code Connect UI, or link your codebase using Code Connect CLI, check out our [developer documentation](https://developers.figma.com/docs/code-connect/) for more information.

## Setting up Code Connect UI

### Prepare for the setup

Before we can setup Code Connect, you’ll need a few things to get started.

- First, you’ll need a Figma Design file that contains your design system. In this lesson, we’ll be using the [Figma Simple Design System](https://www.figma.com/community/file/1380235722331273046/simple-design-system). Feel free to make a copy of the file if you want to follow along, or use your own design system file. You must be the file owner of the design system file you're connecting.
- Second, you’ll need a seat that has access to Dev Mode, on either the Organization or Enterprise plan. To learn more about Figma’s seat types and plans, check out our [pricing page](https://www.figma.com/pricing/) or the [Figma help center](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features).
- Lastly, you’ll need a repository for your code components. In this lesson, we’ll use the [Figma Simple design system repository](https://github.com/figma/sds/tree/main) that is available on Github. You can fork the repository to your own GitHub account to follow along, or use your own codebase that matches your design system file in Figma.

If any of these topics sound unfamiliar, we’ve got some resources to help you out:

- To create your own components, check out our [Figma Design for beginners course](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners) to learn the basics.
- And if you’re curious to learn more about design systems in general, we’ve got an [Introduction to Design Systems course](https://help.figma.com/hc/en-us/sections/14548397990423-Introduction-to-design-systems) you can check out while you’re there.

Now that we know all the pieces to get started, let’s connect some code!

### Publish component library

In order to link your components in Figma Design with your codebase, you’ll need to publish them as a library first. Make sure to move the file to a team project if you haven’t already.

To publish a library:

1. In a file with components, styles, or variables you’d like to share, select the **Assets** tab in the left sidebar.
2. Click the **Libraries** icon. The tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. From the **This file** section, find your current file and click **Publish**.
4. Add a description of the library's purpose, or a summary of any decisions or changes.
5. From the list of styles, components, or variables that have been added, modified, or removed, uncheck any assets you don't want to publish. You can also uncheck **Changes** to deselect everything.
6. *Organization and Enterprise plans only:* Use the dropdown menu to choose [where to publish the library](https://help.figma.com/hc/en-us/articles/360025508373#h_01J688PTA7N7AHMGZMA6QA1F1V).
7. Click **Publish**. A notification will appear confirming your library has been successfully published.

[Learn more about publish a library in Figma →](https://help.figma.com/hc/en-us/articles/360025508373-Publish-a-library#h_01J688PTA7SPRDKBNDJ5RYVSP4)

Once the library is published, we can open Code Connect UI.

1. From the toolbar, switch to **Dev Mode**.
2. From the dropdown menu next to the file name, choose **Library → Connect components to code**.

![connect components to code.png](https://help.figma.com/hc/article_attachments/36505740633751)

Here, Figma will display all of the components in the file. If you have many components in your library, you can search for specific components using the search bar, or filter or sort them using the dropdown menus on the right.

You can also go into each individual page and select “Connect components” from the right sidebar to view the components available in that specific page.

![Code connect UI menu.gif](https://help.figma.com/hc/article_attachments/36506783821463)

### Connect to Github repository

Connecting to GitHub is optional. You can [map your design system components to code paths manually](https://developers.figma.com/docs/code-connect/code-connect-ui-setup/#manually-connecting-your-components) without a GitHub connection.

Now we’re ready to connect to our Github repository.

To connect:

1. Select the **Settings** icon in the Code Connect UI menu.
2. Click **Connect to Github**. Since this is the first time we connect the GitHub account, you’ll need to go through the authentication process in Github.
3. Log into the GitHub account that has access to the repository you want to connect.
4. When prompted, grant access to either:
   - **All repositories** in your account.
   - **Specific repositories** that contain the components for your design system.
5. Click **Install & Authorize.** You’ll be directed back to Figma once the installation process is completed.
6. Select **Continue** button in the successfully connected page.
7. Then, search and add any directories that contain your UI components for use with Code Connect. You can always add more directories later if needed.
8. Click **Connect** when done.

![connect to github.gif](https://help.figma.com/hc/article_attachments/36509316322839)

### Connect component

With the Github repository connected, you can now map your design component with your code component directly inside the Code Connect UI menu. Let’s try to connect this button component in the Simple Design System file to our codebase using Code Connect UI.

![button component.png](https://help.figma.com/hc/article_attachments/36552603322775)

1. In the Code Connect UI menu, search for “Button” in the search field.
2. Select the **Search repository for files** input field of the Button component.
3. From the dropdown menu, scroll through the list to select the correct code component path for the button component, or search for the keyword.
4. Click **Connect**.

   ![Connect button component.gif](https://help.figma.com/hc/article_attachments/36552603327767)

## MCP Preview

Now that we have connected our button component, click  to view the component and connection details. Here, you can see a side-by-side view of the design component and the code component, and the preview code of the button component, which will be sent to the agentic tools via the Figma MCP server.

Use **Change properties** to update the button’s component properties, and see the MCP Preview code reflects the change accordingly.

![mcp preview.gif](https://help.figma.com/hc/article_attachments/36552665216791)

### Add instructions for MCP

You can also add specific instructions for MCP to give extra design context for more accurate code generation.

1. Click **Add instructions for MCP.**
2. Add additional instruction in the textbox.
3. Click the **Save** button.

A new MCP code preview will be generated based on the new instructions.

![add instruction for mcp.png](https://help.figma.com/hc/article_attachments/36552665219479)

This is where the power of Code Connect comes in. Since now your design system file and your codebase is connected, it helps your agentic development tools build products even faster by giving direct references to your design and your codebase. This allows higher-quality code generation that’s aligned with your specifications.

And remember, this isn’t just for the current file you’re working in. You’ll see this connected code in other files once you added the published Figma Design libraries to them.

**Tip:** When organizing your variables in Figma, be sure to provide the code syntax to the corresponding variables.

If you use a particular syntax for naming variables in your design system, you can use the same syntax when naming variables in your Figma Design files.

That way, Figma will display the correct code syntax when Developers are inspecting the code snippet, and provide the metadata to the agentic tools via the MCP server.

## Wrap up

That’s it for this overview for how Code Connect can bring your design components and code base closer together by:

- Connecting your design components with your codebase to make a unified source of truth,
- And improving the results you get from your agentic tools when using the Figma MCP server with connected components.
