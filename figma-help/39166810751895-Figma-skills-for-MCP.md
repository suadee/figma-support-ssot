---
기술지원명: Figma skills for MCP
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Figma skills for MCP
출처링크: https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Skills are pre-built instructions that teach your AI agent how to handle common Figma tasks reliably, such as creating a new file, building a screen from your design system, or generating code from a design. Without skills, you'd need to describe each step yourself every time. With them, you can ask your agent to do something like "create a new Figma file" or "implement this design" and it already knows what to do.

**Note:** This article describes the skills that Figma provides for the Figma MCP server. To learn about MCP skills and how to use them, check out [Use skills with the Figma MCP server](https://help.figma.com/hc/en-us/articles/39287396773399).

Figma provides a number of skills for use with the [Figma MCP server](https://help.figma.com/hc/en-us/articles/39216419318551):

- [figma-use](#h_01KMFHKFDR8Q78CR8CC9W8J18E)
- [figma-use-figjam](#h_01KPXSNCM35QC8ZJFJVASXJG50)
- [figma-use-slides](#h_01KS0S2X0EDWC8MRRS1BE16QP9)
- [figma-swiftui](#h_01KTM69WDPTM2RTB3JKJ3HYNYN)
- [figma-code-connect](#h_01KMFHKFDRME0YHTRCJ6J4Q2J4)
- [figma-create-new-file](#h_01KMFHKFDR3V4PCCPPH4NHG1PP)
- [figma-generate-diagram](#h_01KS0S2X0EJ0XBCAHPRTKYTXD1)

As well as two example skills that demonstrate how to write to the canvas in Figma:

- [figma-generate-library](#h_01KMFHKFDRH9CCNEFBDKEJ3MQS)
- [figma-generate-design](#h_01KMFHKFDRN7C0PSVAB88Z8087)

Additionally, you can browse a collection of [curated skills in the Figma Community](#h_01KMFHKFDRW2KF5EH5YV05R5S4).

## Get the Figma skills

### Figma plugin

The easiest way to get the Figma skills is through an agentic tool that supports the Figma plugin, such as Claude Code or Cursor. When you install the Figma plugin in one of these tools, the skills are included automatically.

The instructions for [setting up the remote Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) describe how to get the Figma plugin for several common clients.

### Download the skills

If your AI tool doesn't have a Figma MCP plugin, you can download and manually install the skills.

[Click here to download the skills.](https://github.com/figma/mcp-server-guide/archive/refs/heads/main.zip)

You can also view the skills in our [mcp-server-guide repository](https://github.com/figma/mcp-server-guide) on GitHub.

Once you've downloaded the skills, the easiest way to install them is to ask your AI agent to unzip the file and place the contents in the right folder for your tool. Your agent will know where skills are expected to live.

### Troubleshooting

If you run into issues downloading or installing skills, see our [Figma MCP server FAQs](https://help.figma.com/hc/en-us/articles/39252411778583).

## Use skills

You use the Figma skills for the MCP server the same way skills are generally used with Claude Code, Codex, and others. The exact way you invoke a skill depends on the client.

To learn more, see [Use skills with the Figma MCP server.](https://help.figma.com/hc/en-us/articles/39287396773399)

## Figma skills

This article dives into the skills that Figma provides and some example use cases, but don't think of the examples as the limits of a skill; they're just a way to get started!

The skills you'll use depend on the task you're doing.

`figma-use`, for example, is the foundational skill for anyone who wants to write content to a Figma canvas. The skill is used for creating frames, components, variables, and layouts directly in a file. Other skills build on top of it for more specific workflows.

Some skills, like `figma-create-new-file` and `figma-generate-design`, are useful for designers working directly with Figma files.

Others, like `figma-code-connect`, are more relevant if you write code or are working closely with developers.

### figma-use

**Note:** We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.  
  
This tool is currently available to Full and Dev seats on paid plans. Dev seats only have read-only access outside drafts.

`figma-use` is the skill that powers write-to-canvas. When you want your agent to create or modify content directly in a Figma file, such as building frames, placing components from your design system, setting up variables, arranging auto layout, this is the skill that makes it possible.

Instead of generating a static image or a rough approximation, your agent uses `figma-use` to write real, editable Figma content: the same components, variables, and layout rules your team already relies on. The result lands directly on the canvas and is ready to inspect, refine, and extend.

You can write to any Figma Design file you have edit access to. To get started, share a Figma file URL or a link to a specific selection in your prompt, then describe what you want to create or change. For example:

- "Using this Figma file: <URL>, create a new page and build a settings screen using our existing components."
- "Using this selection: <URL>, add an empty state that matches the existing design system."
- "Using this Figma file: <URL>, convert the raw color values in this frame to variables."

**When to use it:** Use this skill any time you want your agent to create or modify content on the Figma canvas, whether you're building a new screen, updating components, or working with variables and tokens.

**Requirements:**

- A Figma Design file URL or a link to a specific selection
- Edit access to the file

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use/SKILL.md>

### figma-use-figjam

**Note:** We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.  
  
This tool is currently available to Full and Dev seats on paid plans. Dev seats only have read-only access outside drafts.

`figma-use-figjam` is the foundational skill for working with FigJam boards. When you want your agent to create or modify content directly in a FigJam file, such as adding stickies, sections, connectors, shapes, tables, or code blocks, this is the skill that makes it possible.

Instead of treating FigJam like a generic whiteboard, your agent uses `figma-use-figjam` to work with real, editable FigJam content and structure. The result lands directly on the board and is ready to review, reorganize, and build on with your team.

You can use it with FigJam boards you have access to through a supported MCP client. To get started, share a FigJam file URL or a link to a specific board in your prompt, then describe what you want to create or change. For example:

- "Using this FigJam file: <URL>, organize this brainstorm into sections and add stickies for the main themes."
- "Using this FigJam board: <URL>, create a planning board with sections, stickies, and connectors for this project brief."
- "Using this FigJam file: <URL>, update this architecture diagram with a new service and reconnect the related systems."

**When to use it:** Use this skill any time you want your agent to create or modify content on a FigJam board, whether you're organizing information, building a planning board, or refining a diagram.

**Requirements:**

- A FigJam file URL or a link to a specific selection
- Edit access to the file

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-figjam/SKILL.md>

### figma-use-slides

**Note:** We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.  
  
This tool is currently available to Full and Dev seats on paid plans. Dev seats only have read-only access outside drafts.

`figma-use-slides` is the foundational skill for working with Figma Slides decks. When you want your agent to create or modify content directly in a Slides file, such as adding slides, organizing them into sections, updating text and shapes on a slide, applying a theme, or writing speaker notes, this is the skill that makes it possible.

Instead of producing a static export or a one-off mockup, your agent uses `figma-use-slides` to write real, editable Slides content: actual slides in the slide grid, theme variables and text styles your team can keep building on, and speaker notes that show up in Presenter View. The result lands directly in the deck and is ready to present, refine, and extend.

You can use it with Slides files you have edit access to. To get started, share a Slides file URL or a link to a specific slide in your prompt, then describe what you want to create or change. For example:

- "Using this Slides file: <URL>, build a five-slide kickoff deck for this project brief."
- "Using this slide: <URL>, rework the layout to match the rest of the deck."
- "Using this Slides file: <URL>, add speaker notes for every slide that has substantive content."
- "Using this Slides file: <URL>, organize the deck into sections and name them."

**When to use it:** Use this skill any time you want your agent to create or modify content in a Slides deck, whether you're building a new presentation, reworking individual slides, or adding speaker notes.

**Requirements:**

- A Slides file URL or a link to a specific slide
- Edit access to the file

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-slides/SKILL.md>

### figma-swiftui

`figma-swiftui` translates between Figma designs and SwiftUI code in both directions. Use it to implement a Figma design as SwiftUI in your iOS project, or to push SwiftUI views and screens back into a Figma file.

The skill recognizes iOS patterns rather than rebuilding them from primitives. A Figma frame with a large title and back chevron becomes a `NavigationStack`, and a row of icon-and-label pairs becomes a `TabView`. SF Symbols round-trip by name in both directions, and semantic colors map to the iOS HIG tokens your team already uses (`Color(.systemBackground)`, `Color.secondary`) rather than being inlined as hex values.

To get started, share a Figma file URL alongside your SwiftUI project, then describe which direction you want. For example:

- "Implement this Figma screen in SwiftUI: <URL>"
- "Build this in SwiftUI for iPad: <URL>"
- "Push the SwiftUI views in `Sources/Screens/Settings/` into this Figma file: <URL>"
- "Mirror this SwiftUI design system in Figma: <URL>"

If the request is ambiguous, such as a Figma URL appearing alongside `.swift` files with no clear verb, your agent will ask which direction you want before continuing.

**When to use it:** Use this skill any time you want to translate between a Figma design and SwiftUI code, whether you're implementing a screen for iOS or pushing existing SwiftUI views back into Figma.

**Requirements:**

- A Figma Design file URL
- For pushing SwiftUI into Figma, edit access to the file

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-swiftui/SKILL.md>

### figma-code-connect

`figma-code-connect` connects your published Figma components to their matching code implementations using Figma's Code Connect feature. Once connected, developers can open a component in Figma's Dev Mode and navigate directly to the corresponding code without having to hunt for it.

To use it, point your agent at a Figma selection or share a Figma URL containing the components you want to connect. The agent will scan your codebase for matching components, show you the proposed connections for review, and then create them in bulk once you confirm.

**When to use it:** Use this skill when you want developers in Dev Mode to be able to see code references linked from the design component to its implementation in the codebase.

**Requirements:**

- A Figma URL for the components you want to connect, or the components selected in the Figma desktop app
- Components must be published to a team library
- Organization or Enterprise plan

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-code-connect/SKILL.md>

### figma-create-new-file

`figma-create-new-file` creates a new blank Figma file in your drafts. It works for both design files and FigJam boards.

**Usage:** `/figma-create-new-file [editorType] [fileName]`

Examples:

- `/figma-create-new-file` creates a design file named "Untitled"
- `/figma-create-new-file figjam My Whiteboard` creates a FigJam file named "My Whiteboard"
- `/figma-create-new-file design My New Design` creates a design file named "My New Design"

When the file is created, your agent returns a link you can open directly in Figma.

If your account belongs to multiple Figma organizations, your agent will ask which one to create the file under before proceeding.

**When to use it:** Use this skill whenever you need a fresh Figma file, typically as the first step before asking your agent to build something on the canvas with `figma-use`.

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-create-new-file/SKILL.md>

### figma-generate-diagram

`figma-generate-diagram` turns a description of a system, process, or flow into an editable FigJam diagram. Describe what you want to diagram and your agent will produce a flowchart, sequence diagram, ER diagram, state diagram, or Gantt chart, and place it in a FigJam file you can keep editing.

Instead of generating a static image you have to redraw to change, your agent uses `figma-generate-diagram` to write a real FigJam diagram: actual nodes and connectors you can move, rename, restyle, and build on with your team. For diagrams that need annotations or color-coded sections beyond what the base diagram supports, the agent can extend it with stickies, shapes, and other FigJam content after the diagram is created.

To get started, describe the diagram you want, or point your agent at the source material it should diagram, such as code, a spec, or an existing file. For example:

- "Diagram the auth handshake between our web client, API gateway, and identity service as a sequence diagram."
- "Using the schema in this repo, generate an ER diagram of our core tables."
- "Create a flowchart of the onboarding steps in this PRD, and add stickies next to each step with the owning team."

**When to use it:** Use this skill when you want a diagram you can keep editing in FigJam, whether you're documenting a system, walking a team through a process, or sketching a data model.

**Requirements:**

- A description of what to diagram, or a link to the source material the diagram should be based on

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-diagram/SKILL.md>

## Example skills: Write to canvas

`figma-generate-library` and `figma-generate-design` are examples of what's possible when you build on top of `figma-use`. Each one shows how write-to-canvas can be combined with design system awareness and multi-step orchestration to tackle a larger workflow.

Both skills are fully functional and ready to use. They're also provided as references: if you want to build your own skill for a workflow specific to your team, these are good starting points to learn from and adapt.

### figma-generate-library

`figma-generate-library` builds or updates a Figma design system library from your codebase. It works in phases: first understanding what you have (in both code and Figma), then creating token collections, building out component pages, and running a final quality check. It pauses for your review between phases before continuing.

The phases are:

- **Discovery**: Reviews your codebase and existing Figma file to understand what tokens and components are already there, then confirms scope with you before creating anything
- **Foundations**: Creates variable collections for colors, spacing, and other tokens; sets up text and effect styles
- **File structure**: Sets up standard pages (Cover, Getting Started, Foundations, Components, Utilities) with documentation for color swatches, type specimens, and spacing
- **Components**: Builds each component with variants, auto-layout, and variable bindings; validates with screenshots before moving on
- **Integration and QA**: Finalizes Code Connect mappings, checks naming and accessibility, and takes final screenshots

**When to use it:** Use this skill when you want to generate or sync a Figma design system library from your codebase, including themes like light and dark mode, token collections, and component libraries.

**Requirements:**

- Access to the project codebase
- An existing Figma file to build into (create one first with `figma-create-new-file` if needed)

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-library/SKILL.md>

### figma-generate-design

`figma-generate-design` builds full-page screens in Figma using real components, variables, and styles from your design system. Point it at a page or view in your codebase and it will find the matching design system assets, import them, and assemble the screen section by section.

For web apps, it can also take a live screenshot of the running application to use as a layout reference, helping it match the real proportions and spacing.

**When to use it:** Use this skill when you want to push a page, screen, or multi-section layout from your application into Figma.

**Requirements:**

- Access to the project codebase
- A Figma file with a connected design system, or a linked library

See the whole skill on GitHub: <https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-design/SKILL.md>

## Community skills

The Figma Community features a growing library of skills that can enhance how you’re using the Figma MCP server. Take a look at the available skills to find good fits for your use cases: [Skills in the Figma Community](https://www.figma.com/community/skills)
