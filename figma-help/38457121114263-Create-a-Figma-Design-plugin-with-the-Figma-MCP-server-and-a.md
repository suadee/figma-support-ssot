---
기술지원명: Create a Figma Design plugin with the Figma MCP server and agentic tools
카테고리: API
작성자: Figma
승인자: (승인 대기)
출처: Create a Figma Design plugin with the Figma MCP server and agentic tools
출처링크: https://help.figma.com/hc/en-us/articles/38457121114263-Create-a-Figma-Design-plugin-with-the-Figma-MCP-server-and-agentic-tools
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Project requirements

- The
  [Figma desktop app](https://www.figma.com/downloads/)
  installed on your computer.
- The remote Figma MCP server or the desktop Figma MCP server
  enabled.
- A copy of one of the following Community resources, depending
  on the approach you want to take: The
  [Figma Design file](https://www.figma.com/community/file/1608335923077674144)
  or the
  [FigJam file](https://www.figma.com/community/file/1608337496516251835)
- An agentic tool that is connected to the Figma MCP server.
  For a list of supported clients, see the
  [Figma MCP catalog](https://www.figma.com/mcp-catalog/).

In this lesson, we'll learn how to turn diagrams and designs into functional Figma plugins using the Figma MCP server and your favorite agentic tool. Together, we'll walk through how to create a Text splitter plugin that allows users to break up a single text layer into multiple layers by sentence, word, or letter.

We'll demonstrate how to build this plugin using two different approaches:

- **Using a FigJam diagram:** This approach is good for communicating precise logic and avoiding guesswork from the agentic tool. Recommended for users who are comfortable with creating diagrams.
- **Using a Figma Design file:** This approach is good for capturing important visual requirements, like color palette or design style. Recommended for users who are familiar with creating designs and using design systems.

![](https://help.figma.com/hc/article_attachments/38592871122711)

**Note:**
The agentic tool you use, and the model that powers it, is what
determines the final code output, not the Figma MCP server. We
recommend trying multiple MCP client tools to compare results. Because
AI tools are non-deterministic, your final outcome may not look identical
to what we create in this lesson.

## Create a Figma plugin using a FigJam diagram

### Create a folder for your plugin

First, let’s make sure we have a folder on our computer to store our plugin. Create a new folder on your computer and give it a descriptive name, like `text-splitter-plugin-1` since this is the first plugin that we’ll be creating. This is where you'll store your plugin.

Then, open the folder we just created in your agentic tool.

**Note:** You might receive a prompt asking if you trust
the authors of the files.
Select “Yes, I trust the authors”.

### **Share the FigJam diagram with the agentic tool**

Now that we’re done with setting up, let’s open our FigJam file. If you don't have a copy of the file, you can visit the [Community resource page](https://www.figma.com/community/file/1608337496516251835) to duplicate the file.

Let’s take a look at our diagram, which is wrapped inside a FigJam section.

![](https://help.figma.com/hc/article_attachments/38482934763031)

The diagram shows how the text splitter plugin works from start to finish. It explains how the plugin checks for a selected text layer, handles errors, and creates new text layers by splitting text into sentences, words, or letters. If there isn’t a text layer selected when the user clicks the **Run** button, it will display an error. If the plugin runs successfully, it will display a success message that includes the number of layers created.

**Tip:** Want to create your own diagrams? Consider
using
[AI in FigJam](https://help.figma.com/hc/en-us/articles/18706554628119-Make-boards-and-diagrams-with-FigJam-AI),
[Chat GPT](https://help.figma.com/hc/en-us/articles/35326636109975-Use-ChatGPT-with-Figma),
or
[Claude](https://help.figma.com/hc/en-us/articles/37883260397975-Create-FigJam-diagrams-with-Claude)
to help you get started.

We need to send this diagram to our agentic tool. To do this:

1. Select the section that contains the diagram. If your diagram isn’t inside a section already, select the whole diagram and click **Wrap in new section** from the inline menu.
2. Right-click and select **Copy link to selection**, or use the shortcut:
   - **Mac:**  `Cmd` `L`
   - **Windows:**  `Ctrl` `L`
3. Switch to your agentic tool and enter the following prompt:

   ```
   Create a Figma plugin for text splitter based on the logic in this file [Insert link]. Users can take a single text layer and break it down into multiple layers based on their choice. Keep a simple and minimalistic design for now.
   ```
4. Submit the prompt.

As the agentic tool runs, we can watch it access the FigJam file and plan out its actions based on the prompt we submitted and the logic provided in the diagram. We can see new files and codes are being added inside the folder.

### Import and test the plugin

Once the agentic tool is done with its first iteration, we can test the plugin in Figma Design.

Before we do that, let’s take a look at our new files. The `manifest.json` is the file we’ll need for plugin configuration in Figma. Here, the `editorType` specifies the Figma editors that your plugin can run in. Currently, this plugin can only run in Figma Design, but you can modify this line to include additional Figma products, like Dev Mode or FigJam. [Learn more about editor types.](https://developers.figma.com/docs/plugins/manifest/#editortype)

![](https://help.figma.com/hc/article_attachments/38592648917911)

Now we're ready to test the plugin:

1. Open the Figma desktop app and create a new Figma Design file.
2. Add a text layer to the canvas and enter a few lines of text.
3. Right-click on the canvas and navigate to **Select plugins** > **Development** > **Import plugin from manifest**.
4. Locate the folder you created and select the `manifest.json` file to import your plugin.
5. Select the **Actions** menu in the toolbar, locate your plugin, and click on it to run it.
6. Select the text layer on the canvas, then use the plugin to split the layer by sentence.

The paragraph is now broken down into multiple text layers, just as we expected!

![](https://help.figma.com/hc/article_attachments/38592648924439)

**Note:** If your plugin isn't working as expected,
visit
the
[Troubleshooting section](#h_01KHS5288YBDS83665BG5XJMWV) 
for tips on refining your plugin.

## Create a Figma plugin using Figma Design

Now let’s try creating another one using Figma Design.

### Create a folder for your plugin

First, let’s make sure we have a folder on our computer to store our plugin. Create a new folder on your computer and give it a descriptive name, like `text-splitter-plugin-2` since this is the first plugin that we’ll be creating. This is where you'll store your plugin.

Then, open the folder we just created in your agentic tool.

**Note:** You might receive a prompt asking if you trust
the authors of the files.
Select “Yes, I trust the authors”.

### Share the Figma Design file with the agentic tool

Open the Figma Design file. If you don't have a copy of the file, you can visit the [Community resource page](https://www.figma.com/community/file/1608335923077674144) to duplicate the file.

Let’s take a look at the design.

![](https://help.figma.com/hc/article_attachments/38483470374039)

The design has a simple user interface with the options for users to choose how to split a text later by sentence, word, or letter, and use the **Run** button to trigger the action. There is also a success or error message to give quick user feedback.

We need to send this design to our agentic tool. To do this:

1. Select the design frame.
2. Right-click and select **Copy/Paste as** -> **Copy link to selection**, or use the shortcut:
   - **Mac:**  `Cmd` `L`
   - **Windows:**  `Ctrl` `L`
3. Switch to your agentic tool and enter the following prompt:

   ```
   Create a Figma plugin for text splitter using this design: [Insert link]. Users can take a single text layer and break it down into multiple layers based on their choice. If the user didn't select a single text layer before clicking on the Run button, it returns an error message. Otherwise, it will show a success message telling the user how many text layers it has splitted into.
   ```
4. Submit the prompt.

As the agentic tool runs, we can watch it access the Figma Design file and plan out its actions based on the prompt we submitted and the visual requirements provided in the design. We can see new files and codes are being added inside the folder.

### Import and test the plugin

Once the agent is done with the iteration, we can test the plugin in Figma Design.

Now we're ready to test the plugin:

1. Switch to the Figma desktop app and create a new Figma Design file.
2. Add a text layer to the canvas and enter a few lines of text.
3. Right-click on the canvas and navigate to **Select plugins** > **Development** > **Import plugin from manifest**.
4. Locate the folder you created and select the `manifest.json` file to import your plugin.
5. Select the **Actions** menu in the toolbar, locate your plugin, and click on it to run it.
6. Select the text layer on the canvas, then use the plugin to split the layer by sentence.

The paragraph is now broken down into multiple text layers just as we expected, and we can see a message at the bottom of the plugin telling us how many layers the paragraph is splitted into.

![import and test the FD plugin.gif](https://help.figma.com/hc/article_attachments/38592622991511)

## Troubleshoot and refine your plugin

Even if everything works as expected, it's still a good idea to test the plugin multiple times to refine the experience and check for edge cases.

Remember, AI tools are non-deterministic and your results may look different from ours. We'll walk through some troubleshooting tips to help you refine your plugin experience using additional prompts.

For example, the plugin we created using the FigJam diagram didn't display an error message when we clicked the **Run** button without selecting a text layer. It also failed to display a success message when it ran successfully.

![](https://help.figma.com/hc/article_attachments/38592622992151)

Taking a look at the agent's thinking process, we can see that it defined the logic to include these messages, but there may have been an error during the implementation process. We can submit an additional prompt to ask the agent to fix this.

![](https://help.figma.com/hc/article_attachments/38592622994711)

When refining your plugin using additional prompts, try to be as descriptive and specific about the change you want it to make.

In our case, we can add the following prompt:

```
Looks like there is no error message displayed when the user didn’t select a text layer before running the plugin, and no success message displayed when the plugin runs successfully. Can you fix that?
```

When we submit a new prompt, the agent will begin evaluating the current implementation and fix any issues it finds. Once it's done iterating, you can re-open the plugin in Figma Design and test it again.

Now when we click the **Run** button in the plugin without selecting a text layer, we’ll see an error message at the bottom of the plugin. And when we split a sentence into words, we’ll know how many text layers were generated.

![](https://help.figma.com/hc/article_attachments/38592622995607)

It may take several rounds of iterating to achieve your expected results. Prompting is a skill, and like all skills, proficiency takes time and practice. Try entering a few more prompts to customize your plugin experience!

## What’s Next?

Once you’re happy with your plugin, you can [publish it to the Figma Community](https://help.figma.com/hc/en-us/articles/360042293394-Publish-plugins-to-the-Figma-Community) or use what you've learned to bring your own ideas to life. If you're new to building plugins, check out our [Build your first plugin course](https://help.figma.com/hc/en-us/sections/6448765398551-Build-your-first-plugin) for a deeper dive into Figma plugins.

## Check your knowledge
