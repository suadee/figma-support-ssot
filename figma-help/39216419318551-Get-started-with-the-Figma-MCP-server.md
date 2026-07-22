---
기술지원명: Get started with the Figma MCP server
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Get started with the Figma MCP server
출처링크: https://help.figma.com/hc/en-us/articles/39216419318551-Get-started-with-the-Figma-MCP-server
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma MCP server brings Figma directly into your development workflow, giving AI agents access to the structured design context needed to generate accurate, design-informed code.

Agents can read from Figma files to extract components, variables, layout data, and other design details, enabling code generation that reflects how your UI is actually built and not just how it looks.

With new write capabilities, agents can now also create and update Figma designs directly. Generate components, variables, and full screens using your existing design system. Instead of producing flat visual outputs, agents build with real Figma primitives and reuse what already exists in your libraries.

**Note:** The new write to canvas feature is currently available to Full and Dev seats on paid plans. Dev seats only have read-only access outside drafts.  
  
We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.

Together, this enables a continuous workflow between code and canvas, where agents can move in both directions while keeping your design system as the source of truth.

To get started:

1. [Set up the Figma MCP server](#h_01KMFFQ749HM9B5R4HAQFSFDGK)
2. [Start using the Figma MCP server](#h_01KMFFQ74B3W3GP2CTZ1X616G6)
3. [Check out the Figma Community](#h_01KMFFQ74EKBYHWHB7SFX9QYQ5)
4. [Create your own skills](#h_01KMFFQ74FEHQNMWKG0NDXD951)
5. [What’s next?](#h_01KMFFQ74FJQ1TBFJZ9PY8TSQE)

## **Set up the Figma MCP server**

To set up the remote Figma MCP server, follow the steps for your client. Figma provides instructions for several common clients:

- [Claude Code](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server#h_01KPPEJMXTZGNJS32R62SCME0S)
- [Codex](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server#h_01KPPFC952S5ZRG6KQCTVRAKCG)
- [Cursor](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server#h_01KPPGE8VQMJAXZ6CSZ0M32VHY)
- [Gemini CLI](https://help.figma.com/hc/en-us/articles/39889246888855-Gemini-CLI-and-Figma-Set-up-the-MCP-server#h_01KPPGHCQTQAC1KQSB1YS03ETE)
- [VS Code](https://help.figma.com/hc/en-us/articles/39890361040535-VS-Code-and-Figma-Set-up-the-MCP-server#h_01KPPGM2WBVB21ZYNEXJYDH16P)

The instructions vary depending on the client. For instructions about installing skills for other clients, ask your client how to add a server or check your client’s documentation: [Supported MCP clients](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server#h_01K25F7RBRZKCATVJHNXCS6KXW)

## **Start using the Figma MCP server**

Dive in! Here are some example prompts to get you started:

- "/figma-use can you help me create a new Figma design using my design system components? Place it in a new Figma file."
- "Capture the UI of my app homepage as frames in <Figma file URL>."
- "Create a flowchart for the user authentication flow using the Figma MCP generate\_diagram tool."

When you’re working with the remote Figma MCP server, a couple things are important to understand: tools and skills.

- **Tools** are what enable your MCP client to take actions with Figma files. You can see the tools available and example prompts [here](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/).
- **Skills** tell your MCP client how to effectively use tools. Using a skill will get you higher quality, more reliable results from the Figma MCP server.

Once you’ve set up the remote Figma MCP server, skills are the best way to get started prompting: [Use skills with the Figma MCP server](https://help.figma.com/hc/en-us/articles/39287396773399).

You can also learn more about the skills that Figma provides: [Figma skills for MCP](https://help.figma.com/hc/en-us/articles/39166810751895)

## **Check out the Figma Community**

The Figma Community features a growing library of skills that can enhance how you’re using the Figma MCP server. Take a look at the available skills to find good fits for your use cases: [Skills in the Figma Community](https://www.figma.com/community/skills)

## **Create your own skills**

You can also create your own skills to teach your agent how your team works in Figma. Custom skills help you package repeatable workflows and get more consistent results from the Figma MCP server: [Create skills for the Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/create-skills/)

## **What’s next?**

- Check out the [Figma MCP collection](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection) for a deep dive into using the Figma MCP server
- See the Shortcuts blog for some great info about the MCP server’s latest features:
  - [Agents, meet the Figma canvas](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/)
  - [The future of design is code and canvas](https://www.figma.com/blog/the-future-of-design-is-code-and-canvas/)
- Visit the [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559) for a table of supported clients and an overview of the functionality we provide
- Explore our [developer documentation](https://developers.figma.com/docs/figma-mcp-server/) for the most granular details about working with the Figma MCP server and all its capabilities
