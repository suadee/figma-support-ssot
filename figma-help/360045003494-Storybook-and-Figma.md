---
기술지원명: Storybook and Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Storybook and Figma
출처링크: https://help.figma.com/hc/en-us/articles/360045003494-Storybook-and-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

 

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with can edit permissions on a Figma file can use the Storybook plugin in Design Mode or Dev Mode

[Storybook](https://storybook.js.org/) is an open source tool for developing, testing, and documenting UI components across many. Use Storybook to:

- Create code-based components that can be used across different platforms and devices.
- Collaborate with designers, engineers, and product managers.
- Showcase components in an interactive development environment, without needing to spin up the full application.
- Show different use cases and examples for implementing components.
- Install [addons](https://storybook.js.org/addons/) for prototyping, testing, and documentation.

Connect Storybook to Figma to view your designs in Storybook and view your stories in Figma.

The [design addon](https://storybook.js.org/addons/storybook-addon-designs/) for Storybook allows you to embed Figma files alongside your code-based components in Storybook. Meanwhile, the [Storybook plugin](https://www.figma.com/community/plugin/1056265616080331589/Storybook-Connect) for Figma allows you to embed stories alongside your design components in Figma. Storybook for Figma can be used by designers in Design Mode or by developers in Dev Mode.

Learn more about Storybook in their [docs](https://storybook.js.org/docs/basics/introduction/) and [tutorials](https://www.learnstorybook.com/).

# About the Storybook plugin

Figma [Storybook plugin](https://www.figma.com/community/plugin/1056265616080331589/Storybook-Connect) lets you embed component stories in Figma. This lets you cross-reference the live implementation from Storybook in your Figma file. The Storybook plugin is powered by [Storybook embeds](https://storybook.js.org/docs/react/sharing/embed#embed-stories-on-other-platforms) and [Chromatic](https://chromatic.com/docs/figma), a publishing tool created by the Storybook team.

Before embedding Storybook in Figma you'll need:

- Your Storybook project is published on Chromatic
- `Can edit` permissions in Figma
- Be listed as a collaborator in Chromatic

To connect Storybook to Figma, you will need to install the Storybook plugin in Figma: Design or Dev Mode.

## Embed Storybook in Figma

### In Storybook

1. Sign in with Chromatic.
2. Go to a story in a Storybook that is published on Chromatic.
3. Copy the URL for the story from the address bar.

### In Figma

1. Open a Figma file in Design or Dev Mode.
2. Run the Storybook plugin in Figma.
3. Select the Figma component you want to link the story to. The Storybook plugin supports linking stories to Figma components, variants, and instances.
4. Paste the URL into the plugin modal.
5. Click **Link story**.![Storybook Connect modal in Figma for pasting a Chromatic story URL to link a design, with a prompt to "Link story".](https://help.figma.com/hc/article_attachments/5685890162327)
6. Figma will show links to the story in the right sidebar. If a component was linked, all instances of that component will have the link.

## Open a story in Figma

1. In Figma, select a component that you’ve previously linked to a story.
2. Click **view story** in the right sidebar.
3. or run the Storybook plugin.

![Figma panel showing Storybook plugin options to view and open stories directly in the browser.](https://help.figma.com/hc/article_attachments/5685878836759)

# **Embed Figma in Storybook**

Storybook [design addon](https://storybook.js.org/addons/storybook-addon-designs) allows you to embed Figma files and prototypes in Storybook. It’s powered by [Figma Live Embeds](https://help.figma.com/hc/en-us/articles/360039827134). You can embed Figma files in Storybook, regardless of the file's [sharing settings](https://help.figma.com/hc/en-us/articles/360040531773). Share private files within a team, or public files with the world.

Collaborators can interact with embeds based on their [team](https://help.figma.com/hc/en-us/articles/360039970673) or [Organization permissions](https://help.figma.com/hc/en-us/articles/360039960434).

1. Install the addon:

   ```
    npm install -D @storybook/addon-designs
    # yarn add -D @storybook/addon-designs
   ```
2. Register the addon in your **.storybook/main.js** file:

   ```
    // .storybook/main.js
    module.exports = { addons: ['@storybook/addon-designs']
    }
   ```

   If you're using Storybook@5.0.x, use this module instead.

   ```
    // .storybook/addons.js
    import 'storybook-addon-designs/register'
   ```

For detailed instructions, check out the [Figma addon readme](https://github.com/pocka/storybook-addon-designs/blob/master/README.md) on GitHub.

## Copy the Figma URL

Copy the URL for the file or frame you’d like to embed in your story.

1. Open the Figma file.
2. If you want to share a specific frame, select the frame on your canvas.
3. Click the **Share** button.
4. Click the **Copy link** button.

## Paste the Figma URL in Storybook

Use a [parameter](https://storybook.js.org/docs/basics/writing-stories/#parameters) to associate Figma files and frames to your story.

1. Open your stories file (in many cases, it’s named like \*.stories.js)
2. Add a story parameter named design:  

   ```
   export const myStory = () => <Button>Hello, World!</Button>myStory.story = {  
   parameters: {  
          design: {  
             type: 'figma',  
             url: ''  
          }  
       }  
    }   
   ```
3. Paste the copied URL to the **URL field**.

## Open a Figma file in Storybook

1. Open Storybook
2. Open the **Design** tab in the addon panel.
3. Click the embedded Figma file to open it.

![Storybook interface displaying green button components from Figma, showcasing design integration.](https://help.figma.com/hc/article_attachments/5685826347287)
