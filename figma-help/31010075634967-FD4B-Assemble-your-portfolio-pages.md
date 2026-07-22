---
기술지원명: FD4B: Assemble your portfolio pages
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Assemble your portfolio pages
출처링크: https://help.figma.com/hc/en-us/articles/31010075634967-FD4B-Assemble-your-portfolio-pages
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Lesson overview

In this lesson, we’ll organize our main components using sections. Then, we’ll use instances to build the page layouts of our portfolio website.

## Organize the components page using sections

We’ll start on the **Components** page of our file. We’ve been moving our main components to this page throughout the course, but we haven’t organized them beyond that. Let’s organize our main components using [sections](https://help.figma.com/hc/en-us/articles/9771500257687-Organize-your-canvas-with-sections).

We learned a little bit about sections from our friends Kaitie and Lauren. Like frames, sections are a type of container layer that we can use to organize other layers. They are a great way to group related design elements, making it easier for collaborators to find what they need.

To create a section:

1. Select the  **Section**tool from the toolbar or press `Shift` `S`.
2. Click and drag your cursor to add a section to the canvas.

Sections have a title field that you can use to give the section a label. Double-click on the field to rename it. We’ll call this first section `Button`. Bet you can guess which element we’re going to add here. Select the **Button** main component and drag it into the section.

![An animation demonstrating how to add a section to the canvas. ](https://help.figma.com/hc/article_attachments/31617504445975)

**Tip:** You can also click and drag to create sections over objects to place them inside.

We can also add multiple layers to a section at the same time. The two hero elements—the **Personal bio** and the **Impactful text block**—serve a similar purpose so let’s add them to the same section.

1. Select the **Personal bio** and the **Impactful text block** main components.
2. Right-click on the selection and choose **Wrap in new section**. Rename this section to **Hero**.

**Tip:** Placing components in sections also organizes them in the **Assets** tab.

We're going to add individual sections for the navigation bar, footer, and the custom shapes, and a larger section for the remaining components. Feel free to use a different organization structure. Just make sure that all of your components are inside a section before moving on.

![](https://help.figma.com/hc/article_attachments/31617504447511)

You might also want to change the background color of your sections, which also updates the thumbnail background behind components in the **Assets** tab. Use this to improve color contrast and make components easier to scan and find.

### Remove the background fill from components

When making some of our components, we added a white background for a similar reason—to make them easier to read and see while we built them. Let's remove the white background fills from every component except the **Navigation** component.

### Change the navigation bar component's background fill

When we get to prototyping, we'll want our content to scroll behind the nav bar and keeping the background fill will prevent the content from showing through. We'll change the **Navigation**component's fill to a warm, neutral color like `FFFDF8`. This will also make it easier to apply a single background color to our whole design later on.

![](https://help.figma.com/hc/article_attachments/31617504448791)

## Assemble your portfolio pages

Now that our main components are organized, we’re ready to assemble our portfolio’s home page and case study page designs.

We’ll build our designs on the **Designs** page. The canvas on this page should be completely blank but it won’t be for long!

We’re planning to create two pages for our portfolio site, and they each have three parts in common. The **Navigation bar**, the **Skill list**, and the **Footer**.

Let’s drag out instances of each of these components from the **Assets**tab and arrange them on the canvas. Then, select them and press `Shift` `A` to add them to an auto layout frame. Give the frame the same background color as the navigation bar: `FFFDF8`.

![](https://help.figma.com/hc/article_attachments/31729607056535)

Set the new frame's **Width resizing**to a **Fixed width** of `1440`. Make sure the **Height resizing**is set to **Hug contents**so it will grow as we add more stuff to our page. The **Gap** and **Padding** values should both be `0` (zero).

![](https://help.figma.com/hc/article_attachments/31617504451351)

Since out portfolio will have two pages, let's duplicate this frame. Name one frame `Home` and the other `Case study`.

Don’t worry if your components don’t stretch the full width of the frame yet. We’ll update that later. But, feel free to update them now so now if you remember how!

### Build the home page

Now comes the fun part—building our page layouts! Starting with the home page.

Drag an instance of the **Personal bio** main component into the **Home page** frame, and position it between the navigation bar and the skills list, and watch as they automatically adjust to accommodate the new content.

![](https://help.figma.com/hc/article_attachments/31617529474071)

All of the work we did earlier to make these building blocks are making this a seamless drag-and-drop experience. Imagine how easy this would be if you were collaborating with a team, since they’d be able to leverage the work that went into these components and move much more quickly when building out their own pages.

Let’s add the rest of the content to our home page, including a section heading and a few project cards. You can add additional cards either by dragging in new instances from the **Assets** tab, searching for them in the actions menu, or by duplicating an existing instance. No matter which method you use, the frame will grow to accommodate the new content because its **Height resizing** is set to **Hug contents**.

If you want to experiment with a different flow on your page, you can also reorder elements by clicking and dragging them inside the frame or by selecting one and using your arrow keys.

![An animation demonstrating how to drag an instance from the Assets tab onto the canvas. ](https://help.figma.com/hc/article_attachments/31617529475863)

Our home page is taking shape, but there’s one more step we need to take before moving on.

Select the Home page frame, and press `Enter` on your keyboard to select all child layers. Then, change the **Width resizing** to **Fill container**.

This ensures every element will always span the full width of the parent frame, even on different screen sizes.

If you’re wondering why we didn’t do this in earlier videos, it’s because the **Fill container** option is only available when nested inside another frame. Like the name implies—**Fill container** allows the layer’s width or height to fill all available space in its parent.

Once you’re happy with the layout of your home page, we can move on to the case study page.

### Build the case study page

The process of building out the case study page is very similar to the home page, but the exact layout you use depends on the story you want to tell.

We’ll start by adding an instance of the **Impactful text** component to the top of the page below the nav bar.

Then, follow it up with a mix of paragraph text blocks, section headings, images, and a quote block. Choose the components that work best for you and your story. If you’re not sure what story you’d like to tell, feel free to pause and think about it! You can also check out some [case studies](https://www.figma.com/blog/case-study/) published on Figma’s blog, *Shortcut,* for inspiration.

**Tip:** If you're new to product design, check out the Shortcut blog post [Breaking in: A guide to landing your first product design role](https://www.figma.com/blog/breaking-in-a-guide-to-landing-your-first-product-design-role/).

Remember that the page layout isn’t set in stone and you can easily remove elements or add new ones, if needed.

![](https://help.figma.com/hc/article_attachments/31617504454167)

Once you’re feeling good about how your page is shaping up, select the **Case study** frame, press `Enter` to select all the child layers, and change their **Width resizing** to **Fill container**.

Oh wait, it looks like our image block component is still left aligned instead of center. Let's see what's going on here.

![](https://help.figma.com/hc/article_attachments/31617504455959)

Right-click on the instance and select **Go** **to main component**. It looks like the alignment is set to **Align top-left**. Let’s update that to **Align center**. Then click **Return to instance** to quickly jump back to the **Designs** page.

![](https://help.figma.com/hc/article_attachments/31617504459159)

Now the image block instance’s alignment should also set to **Align Center**. If you’re not seeing the instance update, go to the Instance menu and select  **Reset all changes**.

![](https://help.figma.com/hc/article_attachments/31617529481111)

That looks much better! This workflow is really helpful as you’re bound to encounter small tweaks that you want to make, or tiny things that aren’t working quite like you expected. No one is perfect on their first try, and it’s all part of the process.

## Customize the instances

All of our portfolio pieces are in place and our page layouts look great! Now we can start replacing the placeholder text and images with our own content. Constructing an engaging portfolio takes time, so it’s ok to pause here and think about the story you want to tell.

To edit a text string inside an instance, double-click on it and start typing. Feel free to make the content as long or short as you want. Auto layout will take care of the rest.

Want to add images? Double-click into the image placeholders and replace them with real content. If you used Figma Design, or any of Figma’s other products like FigJam or Figma Slides for a project, you can add snapshots of your work by copying as PNGs and pasting them in the image placeholders. Learn more about [copying as PNG](https://help.figma.com/hc/en-us/articles/4409078832791-Copy-and-paste-objects#h_01HR635DDBT06JQT8S82EH00BZ).

![An animation demonstrating how to copy content from other Figma products as PNGs.](https://help.figma.com/hc/article_attachments/31729634393879)

Remember, a portfolio is never finished—it’s a living project that you can revisit whenever inspiration strikes. As you work on more projects, personal or professional, consider writing more case studies so your site has even more pages. Or maybe you’re feeling bold and want to make an entirely new page for something else instead. Keep iterating, updating, and fine-tuning, because as your portfolio grows, so will your design skills.
