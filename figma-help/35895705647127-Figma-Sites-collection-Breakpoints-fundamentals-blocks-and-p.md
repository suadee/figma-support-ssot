---
기술지원명: Figma Sites collection: Breakpoints fundamentals, blocks, and preview your site
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Figma Sites collection: Breakpoints fundamentals, blocks, and preview your site
출처링크: https://help.figma.com/hc/en-us/articles/35895705647127-Figma-Sites-collection-Breakpoints-fundamentals-blocks-and-preview-your-site
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

## Breakpoints in Figma Sites

![](https://help.figma.com/hc/article_attachments/35895683228311)

In web design, breakpoints refer to specific screen widths where your webpage layout changes to meet the needs of different screen sizes. You can add as many breakpoints as you like, but most sites won’t need more than a desktop, tablet, and mobile breakpoint.

In Figma Sites, there are two types of breakpoints: Primary and secondary.

- **Primary breakpoint:** Any changes you make to objects in the primary breakpoint cascade to the other breakpoints. The Desktop breakpoint is the primary breakpoint by default.
- **Secondary breakpoints:** Changes made in a secondary breakpoint affect only that specific breakpoint.

Because changes from the primary breakpoint affect all of the others, you don’t have to design every breakpoint from scratch, but you also get the ability to customize each screen’s experience by editing the secondary breakpoints.

### Set as primary breakpoint

![](https://help.figma.com/hc/article_attachments/36082442071319)

You can change any breakpoint to the primary breakpoint by right-clicking on the breakpoint and choosing **Set as primary breakpoint**.

### **Add a new breakpoint**

When you start building a website, it’s best to create all your breakpoints first before adding your designs. As you start adding content, you’ll get immediate feedback on how the layout looks on different devices.

To add a new breakpoint to a webpage:

1. Click the  **plus** button in the webpage header on the canvas.
2. Choose a desktop, tablet, or mobile breakpoint with predefined widths, or enter a custom breakpoint width.
3. Let's add a tablet breakpoint.

![](https://help.figma.com/hc/article_attachments/35895705645975)

## Build with blocks

Now, let's use Figma Sites’ prebuilt blocks to quickly lay out a website. Blocks are ready-made design components that you can easily drag and drop into to your website to quickly assemble a layout. This also includes embeds—components that let you interact with external content, such as videos or maps.

### Insert blocks from the Insert menu

In the navigation bar, select  **Inserts**. You’ll see the option to choose either blocks or libraries. We’ll start with blocks. Figma Sites has different types of blocks that give you access to design elements found in most webpages, like:

- **Page blocks** are complete web pages with everything you need already set up, ready to go.
- **Navigation blocks** include navigation bars and footers. These help people move around your website with links.
- **Hero blocks** feature important information and are often large and visually rich to grab user attention.
- **Embed blocks** let you bring new functionality like forms, and assets like video from external websites.

Blocks in Figma Sites are built to automatically reflow across screen sizes, and they’re stackable, making them a great way to get started quickly.

### Try it out!

![](https://help.figma.com/hc/article_attachments/36083172871703)

Take a minute and go and try adding blocks to a new site for yourself. Don’t worry about having an amazing idea for a site right now, we just want to practice adding the blocks in—the content can come later.

1. Open the  **Inserts** menu from the left navigation bar.
2. From the Navigation section, select a **header** block.
3. Drag it into the primary breakpoint (the Desktop breakpoint is the primary by default).
4. The header block will align to the top and fills the width of the breakpoint. You may notice that auto layout is set to vertical in the left sidebar. Breakpoints automatically apply vertical auto layout when blocks are dragged into them. This helps you snap a page together by adding one block after another.
5. Find a **footer** block in the Navigation section and drag one below the header.
6. Then, add a **hero** and drag it between the header and footer. You should see a blue line as a visual indicator on where the block will be placed. Release your click when the blue line is between the header and footer blocks.
7. Finally, grab a **feature** block and place it under the hero.

You just set the foundation for a complete webpage! Because you added the blocks to the primary breakpoint, Figma Sites has automatically adjusted the design of our Mobile and Tablet breakpoints using the same blocks.

Now that we have our different breakpoints set up, we can customize the experience for each screen. As mentioned, any changes made in the secondary breakpoints will only affect the designs in that breakpoint.

## Preview designs and breakpoints

![](https://help.figma.com/hc/article_attachments/36131025499159)

Let’s see what our site looks like at different screen sizes by previewing it. To preview a site, click the  Preview icon in the top left corner of the website page on the canvas to preview just that page. Or, click the Preview icon at the top of the right sidebar.

![_MConverter.eu_IntroToSites_HC.webp](https://help.figma.com/hc/article_attachments/36126687860119)

In the preview, you can toggle between different breakpoints by clicking the device screens at the top.

You can also see how it adjusts by dragging the handles on either side to see the site adjust. This is a great way to check that your breakpoints are working how you want them. When the preview crosses the width for a new breakpoint, you can see how Figma switches over to the layout of the next breakpoint.

### Check minimum and maximum widths for breakpoints

You can view the minimum and maximum widths for any breakpoint for your page inside of the Figma Sites editor by looking at the name on the canvas.

To change them, select a breakpoint and change its width in the right sidebar. Figma Sites will adjust all other breakpoints accordingly, so that none of the values overlap with each other.

## Check your knowledge

## Up next: Move from Figma Design to Figma Sites

If you've been using Figma Design for a while, you might already have some website designs across your Design Files. In the next lesson we'll teach you how to bring those designs into Figma Sites so you can publish them, fast.

## Additional resources

- [Figma Sites playground file](https://www.figma.com/community/file/1543020893913814047/figma-sites-playground) — Practice what you just learned directly inside of Figma Sites! We recommend following the Figma Sites playground file to learn more about breakpoints in Figma Sites through hands-on learning.
- [Breakpoints on the Figma help center](https://help.figma.com/hc/en-us/articles/31242797809815-Add-or-delete-breakpoints-in-a-webpage) — This comprehensive help center article will give you more in-depth knowledge about using breakpoints in Figma Sites.
