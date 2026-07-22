---
기술지원명: Figma MCP collection: How to set up the Figma remote MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Figma MCP collection: How to set up the Figma remote MCP server
출처링크: https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma introduces new MCP tools that allow agentic tools to make
edits directly to Figma files. If you have already installed the
remote
Figma MCP server, you'll need to reinstall it with the updated installation
guide.

Figma’s remote MCP server allows you to connect directly to an MCP server hosted by Figma. Then, you can use the context of your Figma design files to improve your workflows in your favorite AI development tools and build faster.

In this lesson, we’ll walk you through how to set up the remote Figma MCP server in these development tools. Then, we’ll show you how to use the Figma MCP server to pass context from your Figma Design files. Let’s get started!

Figma recommends using the remote Figma MCP server, where you'll find the latest tools and skills. If you prefer to use the desktop Figma MCP server, view instructions to [set up the desktop Figma MCP server instead →](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)

## Set up the Figma MCP server

Setting up the Figma MCP server requires you to configure your preferred development tools.

We’ll provide the configurations to set up different development tools including [Claude Code,](https://www.anthropic.com/product/claude-code) [Codex](https://chatgpt.com/codex/?c_id=23655882150&c_agid=197861433244&c_crid=807850089496&c_kwid=kwd-21294781&c_ims=&c_pms=1014221&c_nw=g&c_dvc=c&gad_campaignid=23655882150&gbraid=0AAAAA-I0E5ef8EiE9dBi2Iyk60LaTYqyn), [Cursor](https://cursor.com/get-started?cc_platform=google&cc_campaignid=23656700841&cc_adgroupid=195242436238&cc_adid=798371314311&cc_keyword=cursor%20install&cc_matchtype=e&cc_device=c&cc_network=g&cc_placement=&cc_location=1014221&cc_adposition=&gad_campaignid=23656700841&gbraid=0AAAABAkdGgSc_XtBTItyHuaAAMAqoMTh1), [VS Code](https://code.visualstudio.com/download), and [Gemini CLI](https://geminicli.com/docs/get-started/installation/) in this lesson:

- [Claude Code and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server#h_01KPPEJMXTZGNJS32R62SCME0S)
- [Codex and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server#h_01KPPFC952S5ZRG6KQCTVRAKCG)
- [Cursor and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server#h_01KPPGE8VQMJAXZ6CSZ0M32VHY)
- [Gemini CLI and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39889246888855-Gemini-CLI-and-Figma-Set-up-the-MCP-server#h_01KPPGHCQTQAC1KQSB1YS03ETE)
- [VS Code and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39890361040535-VS-Code-and-Figma-Set-up-the-MCP-server#h_01KPPGM2WBVB21ZYNEXJYDH16P)
- [Xcode and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/41061095668759)

For a complete list of supported clients, check out our
[Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server#h_01K25F7RBRZKCATVJHNXCS6KXW)
article
to learn more.

## Using the Figma MCP server

To start using the Figma MCP server, you need:

- A full or dev [seat](https://help.figma.com/hc/en-us/articles/360040453433) (other seats may have usage limits with the MCP server)
- A [Figma Design](https://help.figma.com/hc/en-us/articles/15297425105303-Explore-design-files), [Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231), or [FigJam](https://help.figma.com/hc/en-us/articles/15300412458647) file
- Edit or view only [permissions](https://help.figma.com/hc/en-us/articles/35361119554711) to that file. If someone else owns the file your team wants to use, just ask them to [share it with you](https://help.figma.com/hc/en-us/articles/1500007609322) first.

The remote Figma MCP server is link-based. This means that you need to provide the context of the link or selection that you want the MCP server to use, by copying from a file, and pasting it into your tool of choice.

![](https://help.figma.com/hc/article_attachments/35819041902231)

To get the link to an object, select a layer or frame in any of your Figma Design files:

1. Right click on a layer.
2. Choose **copy link to selection**. You can also copy the URL to that layer from your browser’s address bar. This will include the node ID for the object in your file.
3. Then, paste the URL into your development tool to scope your prompt to that node.

You can also use the entire file URL if you have nothing selected on the canvas, and copy the URL from the address bar. Doing this allows you to extract context from the entire Design file If you’re using the MCP server with Figma Make, you will likely want to pass the entire file URL using this method.

## Wrap up

Now that you’ve got the remote Figma MCP set up in your code editor, you’re ready to start building and coding with extra context and information straight from your Figma Design files.

Trying to set up the Figma MCP server on other code editors? Check out our [developer docs](:) to learn more.

Figma’s MCP servers work best with Code Connect to keep your codebase consistent with your design system. Check out our [Code Connect documentation](https://help.figma.com/hc/en-us/articles/23920389749655) to learn more.
