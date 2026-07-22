---
기술지원명: Config 2026: a guide for admins
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Config 2026: a guide for admins
출처링크: https://help.figma.com/hc/en-us/articles/41301052048791-Config-2026-a-guide-for-admins
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

At Config 2026, we expanded what's possible on the Figma canvas: new materials like motion and shaders, tools you can build yourself, and a more powerful agent to support your work.

This article walks through each feature we announced, including availability status and what to know as an admin. Some features are in beta or coming soon. We'll note availability for each below and keep this article updated as things change.

Here's what's new:

- [Figma Motion](#h_01KTN7QBXW6KS1ACWCXEQT506N)
- [Custom shader effects and fills](#h_01KTN83YAEP8XT0X6EMAVY9HYJ)
- [Weave tools in Figma Design](#h_01KTN7Y1CTH37GZJD245X1QH1J)
- [Updates to the Figma agent in design files](#h_01KTN7TC1KKXP7DS4SR06TFHEQ)
- [Generative plugins](#h_01KTN83F3RX24C86S3PTK4V3TC)
- [Code layers (closed beta)](#h_01KVG8HJ70PKQ2SCTN1T1YSYJV)

## Figma MotionOpen beta

Before you start

Who can use this feature

Available for Full seats on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Creating and editing motion requires **can edit** access to the file.

Create production-ready animations directly in your design files with Figma Motion.

- **Animate your designs:** Quickly add motion with preset animations, or build your motion from the ground up with keyframes.
- **Fine-tune your motion:** Use easing curves and spring animations to shape how your motion feels.
- **Generate a first pass with the Figma agent:** Describe the motion you want and let Figma agent add keyframes to the timeline. Then refine the details manually or keep prompting until the motion is just right.
- **Build your motion system:** Maintain consistency across your motion system with timing and easing variables and animated components.
- **Ship your animations:** Use the read-only timeline in Dev Mode to inspect animations at full fidelity, then copy code into CSS, JSON, or React. Or send animation context to your coding tools via the Figma MCP server.

[Learn more about Figma Motion](https://help.figma.com/hc/en-us/articles/41274629073303-Explore-Figma-Motion).

### Frequently asked questions

**Who can access Figma Motion?**

Figma Motion is available on all plans in open beta. You can access Figma Motion in any design file you have can edit access to by switching the toolbar toggle to Motion.

Publishing animated components, generating animations with the Figma agent, and high-resolution video exports require a Full seat on a paid plan.

**Is Figma Motion available on Figma for Government plans?**

Figma Motion is not available on [Figma for Government](https://help.figma.com/hc/en-us/articles/22932461365015) plans.

**Does Figma Motion consume AI credits?**

Figma Motion doesn't use AI credits directly, but using the [Figma agent](#h_01KTN7TC1KKXP7DS4SR06TFHEQ) to create motion will use AI credits in the future. Currently, while the Figma agent is in beta, it does not use AI credits. Once the agent is generally available, [standard AI credit usage](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work#seatcredits) will apply. Manually editing agent-created motion never consumes credits.

## Custom shader effects and fillsOpen beta

Before you start

Who can use this feature

Custom shaders are available in Figma Design, Figma Draw, and Figma Motion on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Using a custom shader requires **can edit** access to the file

Figma-created shader effects and fills are available on all plans

Prompt to build custom shader effects and fills you can save and reuse to create striking visuals, add personality to your designs, and help your brand stand out.

- **Native creation tools**: Create shader effects directly in Figma Design with prompts
- **On canvas controls**: Shaders use Figma’s UI so they feel like native properties
- **Natively rendered**: WebGPU shaders as custom effects, making it possible to build new fills
- **Use across Figma**: Export effects to Figma Make and other platforms via MCP

[Learn how to build custom effects and fills](https://help.figma.com/hc/en-us/articles/41159710233623).

### Frequently asked questions

**Which plans and seat types have access to custom shaders?**

- Creating shaders via the Figma agent are rolling out to users with a Full seat on all [paid plans](https://help.figma.com/hc/en-us/articles/360040328273) in open beta.
- Users with a View, Collab, or Dev seat can try it in **Draft** files.
- Using Figma’s first party agent-built shaders are rolling out to users with a Full seat on all plans in open beta.
- Creating shaders via the Figma agent is not available on Figma for Education, Figma for Government, or Starter plans.

**Why can't my team or organization see the Figma agent?**

If an admin has deactivated AI features for your Figma team or organization, the agent won't appear in your account during or after the beta. [Learn more about managing AI features](https://help.figma.com/hc/en-us/articles/17725942479127).

If you’re not sure whether AI features are enabled, [try using another AI feature in Figma Design.](https://help.figma.com/hc/en-us/articles/23870272542231)

**Can I turn off custom shaders for my team or organization?**

Yes, Admins can [disable Figma AI features](https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization#h_01J0SNQBZ9JXM4T45V5QWZ2QFZ) at any time.

**Do shaders consume AI credits?**

As of now, shaders do not consume AI credits. Once the Figma agent becomes generally available, [standard AI credit usage will apply](https://help.figma.com/hc/en-us/articles/33459875669015) to build shaders with the agent. It does not consume AI credits to apply shaders.

## Figma Weave

You can now use Weave tools in Figma Design to generate visuals in a design file and use pre-built workflows for Weave from the Figma Community.

### Weave tools in Figma Design Open beta

Before you start

Who can use this feature

Available on [Professional, Organization, and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Using a Weave tool requires **can edit** access to a file

Learn more about [Figma Weave](https://help.figma.com/hc/en-us/articles/35965787376919)

Plug inputs into the straightforward UI of Weave tools in Figma Design and generate quality assets on repeat – without the need for robust prompting. Weave tools make it easy to quickly execute on common AI image tasks, like replacing a background, adding a logo to a product, and changing the aspect ratio of an image.

- Choose from a curated list of Weave tools in Figma Design to accomplish simple AI image generation task
- Weave tools are backed by powerful AI workflows, saving you from having to write new prompts yourself
- Swap out inputs and receive consistent results every time you run a Weave tool

[Learn more about using Weave tools in Figma Design](https://help.figma.com/hc/en-us/articles/40779260614935-Use-Weave-tools-in-Figma).

### Weave workflows on Community Generally available

Before you start

Who can use this feature

Available for Full seats [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Requires **can edit** access to a file

Learn more about [Figma Weave](https://help.figma.com/hc/en-us/articles/35965787376919)

Find and create Weave workflows—either as a tool or a template file—for others to use on the Figma Community.

These files let you:

- Duplicate proven Weave workflows into your workspace
- Learn how workflows are structured
- Have a starting workflow to change or add to based on your own creative needs
- Create and share your own workflows with your team or others

[Learn more about Figma Weave workflows in the Figma Community](https://help.figma.com/hc/en-us/articles/360038510693).

### Frequently asked questions

**What is the difference between Weave tools in Figma and Weave as a standalone product?**

Weave is Figma's platform for generative AI and professional editing tools on the open canvas, spanning image, video, animation, motion design, and VFX.

Weave tools in Figma bring that power directly into your design workflow, with a simple UI for common AI image tasks so you can generate consistent results without leaving Figma.

[Learn more about Figma Weave](https://help.figma.com/hc/en-us/articles/35965787376919).

**Which plans have access to Figma Weave tools in Figma Design?**

Available to Professional plans and above with Full seats. Weave workflow templates on Community are available to all plans with Full seats.

**Why can't my team or organization see Weave tools in Figma Design?**

Weave tools in Figma Design are not available for K-12 Education, Figma for Government, or Starter plans.

**Do Weave tools in Figma Design consume AI credits?**

As of now, Weave tools in Figma Design will not consume AI credits.

**Can I turn off Weave tools in Figma Design?**

Yes. Admins can [toggle AI features in Figma](https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization#h_01J0SNQBZ9JXM4T45V5QWZ2QFZ) off at any time.

## Updates to the Figma agent in design filesOpen beta

Who can use this feature

Available on [Professional, Organization, and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Users with Full seats can chat with the agent in Figma Design files

Using the Figma agent requires **can edit** access to the file

Now in open beta, [collaborate with the Figma agent in design files](https://help.figma.com/hc/en-us/articles/37998629035799) to generate and remix designs, automate busywork, and get design feedback.

What's new with the Figma agent:

- [**Create and manage custom skills**](https://help.figma.com/hc/en-us/articles/40283639496599)**:** Turn your team's workflows, conventions, and preferences into shareable skills that can be run on demand
- [**Search the web:**](https://help.figma.com/hc/en-us/articles/39715554287255) The agent can search the web and fetch content from URLs, so you can ground your designs in real-world, up-to-date information
- [**Connect to external tools using MCP connectors**](https://help.figma.com/hc/en-us/articles/35440096186007)**:** The agent can connect to external tools via the Model Context Protocol (MCP), allowing you to pull context into your designs and write back to external sources
- [**Attach files**](https://help.figma.com/hc/en-us/articles/31304529835671)**:** Attach Figma files, images, text and code files, and PDF and spreadsheet files to your prompts so the agent has specific references it can use to produce better results

Starting June 23, new conversation threads with the agent in Figma Design are visible by default to people within their organization or team with a Full seat and edit access to the file. Threads created before June 23, 2026 remain private unless you make them public. [Learn more.](https://help.figma.com/hc/en-us/articles/41272399602583)

**New to using AI in your design workflow?** Check out our "Using AI in your design workflow" collection for ideas, hands-on examples, and best practices for using AI across a broad design workflow.

[Learn more about using the Figma agent.](https://help.figma.com/hc/en-us/articles/37998629035799)

### Frequently asked questions

**Do I have access to the Figma Design agent?**

The agent is available to the following Figma Design users:

- Full seats can use the agent in all Figma Design files
- View, Dev, or Collab seats can try the agent in **Draft** files
- The agent is included on the Professional, Organization, or Enterprise plans with [AI features enabled](https://help.figma.com/hc/en-us/articles/17725942479127)
- The agent is not available on Education, Government, or Starter plans

**Does the Figma Design agent consume AI credits?**

The agent is free during the beta period. AI credits won't be consumed for any prompts or actions. When the agent is generally available, [Figma’s AI credit system](https://help.figma.com/hc/en-us/articles/33459875669015) will apply.

**Are there admin controls to manage how my team or organization uses the Figma agent?**

Yes, Figma admins can disable AI tools for everyone in their team or organization. [Learn more about managing AI feature access and settings as an admin](https://help.figma.com/hc/en-us/articles/17725942479127).

## Generative pluginsOpen beta

Before you start

Who can use this feature

Generative plugins are available in Figma Design, Figma Draw, and Figma Motion on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Generative plugins are not available on Education, Government, or Starter plans

Using generative plugins requires **can edit** access to the file

Figma-created plugins are available on all plans

Prompt the Figma agent to build reusable plugins right in your file that feel native to Figma. Create custom tools that support your unique workflow, like reordering or sorting layers by criteria, applying consistent spacing or padding across selections, or finding and replacing text or colors across a file.

- **Prompt-to-create**: Build custom plugins by chatting with the Figma agent
- **On canvas controls**: Plugins use Figma’s UI so they feel like native tools

[Learn more about generative plugins](https://help.figma.com/hc/en-us/articles/41159704839831).

### Frequently asked questions

**Which plans and seats have access to generative plugins?**

The ability to create generative plugins is available to the following Figma Design users:

- Full seats can create generative plugins in all Figma Design files
- The agent is included on the Professional, Organization, or Enterprise plans with [AI features enabled](https://help.figma.com/hc/en-us/articles/17725942479127)
- The agent is not available on Education, Government, or Starter plans

**Can I turn off the ability to create generative plugins for my organization?**

Yes, Figma admins can disable AI tools for everyone in their team or organization. [Learn more about managing AI feature access and settings as an admin](https://help.figma.com/hc/en-us/articles/17725942479127).

**Where do generative plugins run? Who hosts them?**

Generative plugins are hosted by Figma. They are written and run right inside your Figma file. Classic plugins are built on your local machine using the Figma desktop app and a development environment like Visual Studio Code or Cursor, and then published to the Figma Community where other Figma users can discover and run them.

**Do generative consume AI credits?**

As of now, generative do not consume AI credits. Once the Figma agent becomes generally available, [standard AI credit usage will apply](https://help.figma.com/hc/en-us/articles/33459875669015) to build plugins with the agent. It does not consume AI credits to run an generative plugin.

## Code layers Closed beta

Note: This feature is currently in closed beta, but will be available more broadly soon. Stay tuned!

Bring working code into the Figma canvas as a new kind of layer: code layers.

- **All the features of Figma, now with code:** Design, explore, and work with code layers just like any other layer. Riff off of each other, make collaborative changes to it.
- **Import from GitHub:** Teams can import a frontend repo and start working directly on the Figma Design canvas.
- **Design system fidelity:** Your real design system backs each prototype.

[Sign up to join the waitlist for early access to code layers](https://www.figma.com/config-betas/).

## Sign up to get early access to our other announcementsEarly access sign-up

We showcased some exciting tools coming to Figma soon. You can apply for early access to these tools with one request using [this fohttps://www.figma.com/config-betas/rm](https://www.figma.com/config-betas/).

- **Code layers**: Design with code on the Figma canvas
- **3D transforms in Figma Design:** We are bringing native 3D transforms to Figma, from editable spatial design to dev-ready export.
- **Figma agent across the Figma platform:** Use the Figma agent across FigJam and Figma Slides.

### Waitlist frequently asked questions

**How do I join the waitlist?**

You can join the waitlist using [this form](https://www.figma.com/config-betas/).

After submitting the form, you’ll receive an automated confirmation email letting you know that your request was received. While joining the waitlist doesn’t guarantee immediate or early access, it helps our team understand your interest in the feature(s).

**How can I tell if I’m on the waitlist?**

Once you’ve added your name to the waitlist, you’ll receive an email confirmation that verifies you are on the waitlist. If you aren’t sure whether you have signed up yet, check your email for the confirmation.  
This doesn’t guarantee early access but will let our team know that you’re interested.

**Can I request my whole team or organization get access?**

Access is evaluated on a feature-by-feature basis. Depending on the feature and its rollout plan, access may be granted to an individual, a team, or an entire organization. If you're selected for a beta, we'll communicate the scope of access as part of the onboarding process.

## Watch all of Config 2026

If you weren't able to make it live, check out the keynote from Config 2026 and catch up on the recordings on our [YouTube channel](https://www.youtube.com/figmadesign). We’ll be posting more videos in the coming week, so be sure to subscribe to stay up to date!
