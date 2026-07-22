---
기술지원명: Attach files to a prompt in the Figma agent and Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Attach files to a prompt in the Figma agent and Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/31304529835671-Attach-files-to-a-prompt-in-the-Figma-agent-and-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

The Figma agent is currently available to try for free in open beta. [Learn more.](https://help.figma.com/hc/en-us/articles/34932042346775)

Who can use this feature

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Users with Full seats can chat with the agent in Figma Design and Figma Make files

Users with View, Dev, or Collab seats can try the agent in Figma Design and Figma Make files in Drafts

Requires edit access to the file

When you're creating designs, prototypes, web apps, and interactive UI using the Figma agent or Figma Make, you can attach files to your prompts to guide the agent toward better results.

You can attach:

- [Figma files](#h_01JTF3AP5ZBBN1T78R93VG269D)
- [Images](#h_01JTF3AP5ZTEXT0FILES00001)
- [Text files](#h_01JTF3AP5ZTEXT0FILES00002)
- [PDFs](#h_01JTF3AP5ZTV18VCWW048EJKG3)
- [Video (Make only)](#h_01KN5GXMM2RBR412TPF7K09CJV)
- [Audio (Make only)](#h_01KN5GXMM2RBR412TPF7K09CJV)
- [Presentations (Figma agent only)](#h_01KVGS7C2ZDEAT9499YD74FK8K)
- [Spreadsheets (Figma agent only)](#h_01KVGS7C2ZDEAT9499YD74FK8K)

**Note**: In Figma Make, you can attach up to **10 files per prompt**. The total number of attachments you can have in your file depends on your plan:

- Starter plan: 30 attachments
- Professional, Organization, and Enterprise plans: 500 attachments

Text and code attachments don't count toward the per-file limit in your Figma Make files.

There is no limit to the number of attachments in a chat with the Figma agent.

## Attach a Figma file

You can attach three types of Figma files to a prompt: Design files, FigJam boards (agent only), and Slide decks (agent only).

To attach Figma files in the agent chat:

1. In the prompt box, click  **Add context**, then  **Attach Figma file**.
2. Paste the link to the Figma Design, Figma Slides, or FigJam file you want to attach.

To attach the Figma designs in Figma Make:

1. In the prompt box, click  **Add context**, then  **Attach a design**.
2. Paste the link of the design you want to attach.

**Note:** When you use a [Community design](https://help.figma.com/hc/en-us/articles/31304526749207) for prompts in Figma Make, a reminder appears above the prompt box that lists the designs. Additionally, Figma Make creates an `Attributions.md` file that includes a list of all assets that require attribution. The file is packaged with your functional prototype or web app to ensure proper attribution to original creators.

## Attach your own files

You can attach different file types to provide additional context, data, or reference material to a conversation with the agent.

To attach a file:

1. In the prompt box, click  **Add context**, then **Add images and files**.
2. Select the file from your system's file browser.

**Tip**: You can also drag and drop files directly into the prompt box.

**Caution**: Attaching a file can increase the number of AI credits used in a prompt.

### Image files

You can attach images to provide visual reference or to embed directly in your output.

**Supported formats:**

- JPEG
- PNG
- GIF
- SVG (1MB limit)

Images work in two ways:

- **As reference:** The model reads the image and uses it to guide the layout, colors, and positioning of the generated output. The model does its best to replicate text, colors, and the position of elements, but the result may still differ from the original image.
- **As embedded assets:** You can instruct the agent to embed the image file directly in the generated output. For example, you can upload an image and say "use this as the background image."

In Figma Make, image file size limits depend on your plan:

- **Starter plan:** 25MB maximum
- **Professional, Organization, and Enterprise plans:** 50MB maximum

In the Figma agent, image file size is limited to 50MB.

### Text files

**Tip:** Currently, text files are the best way to use attachments with the Figma agent.

You can attach text files to provide context, data, or code in the agent chat. The AI can reference these files to better understand your requirements and generate more accurate results. Code files like .tsx and .js can be embedded directly in your project.

**Supported formats:**

- **Markup:** .html, .htm, .handlebars, .hbs, .svg, .xml
- **Markdown/text:** .md, .mdx, .txt, .docx (agent only)
- **TypeScript:** .ts, .mts, .cts
- **JavaScript:** .js, .mjs, .cjs
- **Components:** .tsx, .jsx
- **Styles:** .css, .scss, .sass
- **Data files:** .json, .map, .csv

**Note**: Text files have a maximum size limit of 1MB.

**Common use cases**

| Use case | Description |
| --- | --- |
| Import real data into a design or prototype | Upload a `.csv` or `.json` file to generate dashboards, tables, or data-driven UI with realistic content. |
| Reuse existing components | Attach a `.tsx` or `.jsx` file and ask the agent to extend, refactor, or adapt it for a new screen. |
| Design and prototype with real content | Add product copy, FAQs, or marketing messaging in a `.txt` or `.md` file so layouts reflect real-world constraints. |
| Generate UI from API responses | Paste a sample API response in a `.json` file and prompt the Figma agent or Figma Make to design or build the interface around it. |
| Migrate static HTML into interactive UI | Upload an `.html` and `.css` file and ask the model to convert it into a more modular, interactive experience. |

### PDFs

You can attach PDF files to provide additional context to the agent. For example, you might attach brand guidelines, product requirement documents (PRDs), or design specifications to help guide the agent's output.

PDFs are used as reference material. The agent can read and reference the content in your PDF but won't embed the PDF itself in the output.

**Note**: PDFs have a maximum file size limit of 5MB.

### Video and audio files (Make only)

You can attach video and audio files and instruct Figma Make to embed them directly in your output. Tell Figma Make explicitly what to do with the file—for example, "embed this video as a hero background" or "add this audio as background music"—to get the best results.

**Note:** Unlike images, the agent can't analyze video or audio content—it can't watch a video to use it as a style reference.

**Supported formats:**

- **Video:** .mp4, .webm
- **Audio:** .mp3, .m4a

Video and audio file size limits depend on your plan:

- **Starter plan:** 50MB maximum
- **Professional, Organization, and Enterprise plans:** 50MB maximum

### Spreadsheets and presentations (agent only)

You can attach presentations and spreadsheets to your prompts to enhance your output. For example, you might attach a presentation that walks through an upcoming event or product feature, or a spreadsheet that contains data you want to pull into an app.

**Supported formats:**

- **Presentation files:** .pptx
- **Spreadsheet files:** .xlsx

**Note**: Spreadsheets and presentations have a maximum file size limit of 20MB.

## Best practices for working with attachments

When you're working with attachments, here are some best practices to follow.

### Working with large files in Figma Make

Keep attachments as lightweight as possible, especially when you want Figma Make to embed them in the site or prototype it generates. Large images, videos, and other media can slow down the generated site and can also affect the Make editor while you work. Even if a file is under the upload limit, one or more large attachments can cause prompts to load slowly, freeze, crash the browser tab, or run out of memory.

Before uploading assets, resize or compress them to the smallest practical size for the experience you're building. Use web-friendly formats, avoid full-resolution source files when a smaller export will work, and remove unused or duplicate large files from the project. If Make becomes slow or unstable, try deleting large attachments first, especially files over 10MB or projects with multiple large assets.

### Working with the Figma agent

We're continually improving the agent experience. Currently, text files and data-heavy files like spreadsheets (files that don't rely heavily on visuals) are the best types of attachments for working with the Figma agent.

Currently, if you submit a prompt with images in Figma Design and ask the agent to create a design with them, the agent will place the images on the canvas as its working, and then use them to create the designs.

### General best practices

- **In designs, use auto layout where possible.** When you attach a design or component, the agent is good at understanding the flow of content using auto layout.
- **Focus on layout first and functionality after.** Prompt for the layout you want first, then use subsequent prompts to add functionality.
- **Work in steps.** Rather than giving a full, end-to-end description of the result you want, start with a high-level description. Then, as you work, continue to add more granular detail and functionality. When you're attaching components and images of more complex designs, attach frame by frame rather than all at once.
- **Iterate on the result.** For complex functional prototypes or web apps, it will likely take a few steps in the conversation to get a result that satisfies all of your requirements. Don't hesitate to tell the agent where it's gotten functionality wrong. When you do, give examples of what the preferred outcomes are.
- **Common design elements and layouts yield the best one-shot results.** For example, simple galleries and web apps that use a single primary frame work well, among similar design approaches. More complex or novel layouts may require additional prompting.
- **Focus on desktop and full-screen friendly outcomes.** We're working to improve mobile output, but right now content that fits full-screen displays works best.

### Single attachments

When you're working with individual attachments, here are some best practices to follow:

- **Specify exact 1:1 build or reference as style.** In your prompt, tell the agent if you want an exact 1:1 build of the attachment, or to use it as style inspiration or reference.
- **Add details for each section of the build.** For the closest 1:1 build, you can specify with more exactness what you want. Try doing this section by section in your design. You can also ask the agent to help write a more detailed prompt.

### Multiple attachments

When you're working with multiple attachments, here are some best practices to follow:

- **Build screen by screen.** You can attach multiple designs or images, but for best 1:1 results, try building by attaching only one or two at a time. Remember: the agent will remember what you attached in the context of the conversation, so if it didn't get it right the first time, remind it of what you attached and try again.
- **Style references in multiple screens.** You can attach multiple designs or images to help build in the style you'd like. Just remember to specify that you want the images used as inspiration, not rebuilt 1:1.

### Resolving issues

When you're trying to fix or work around issues you encounter, here are some best practices to follow:

- **Try smaller designs.** If your design isn't being faithfully re-created, try a smaller attachment for a more accurate build.
- **Try fewer images and less content-rich designs.** If you're attaching designs with many images, SVGs, or vector illustrations, the agent can sometimes struggle. Try scaling back the fidelity or size of images, or use a less content-rich attachment.
