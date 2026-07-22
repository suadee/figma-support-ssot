---
기술지원명: Lesson 3: Build your design system
카테고리: 디자인
작성자: Figma
승인자: suadee
출처: Lesson 3: Build your design system
출처링크: https://help.figma.com/hc/en-us/articles/14548865734679-Lesson-3-Build-your-design-system
게시일: 2026-07-22
검토일: 2026-07-22
---

## 내용

This is a written version of our [**Introduction to design systems: Lesson 3**](https://www.youtube.com/watch?v=0XSLMGh8yhM) video tutorial. Watch the video and follow along with the written course below.

Welcome back! In this lesson, we’ll join Kai and the Habitz team as they build their design system.

We’ll focus on some core design system features in Figma: [styles](https://help.figma.com/hc/en-us/articles/360039238753) and [components](https://help.figma.com/hc/en-us/articles/360038662654). As well as some tips for defining and organizing your system.

- Explore the different types of styles you can create
- Create components, variants, and other component properties
- Establish consistent naming conventions

# Chapter 1: Set up your library

## Back to basics

Before we get too far ahead, let’s define what Figma means by styles, components, and libraries.

### Styles

Styles allow us to define a collection of properties or settings we want to reuse. We can use styles to:

- Capture specific color values for fills and strokes![](https://help.figma.com/hc/article_attachments/14798259090327)
- Define text properties like font, line height and letter spacing![](https://help.figma.com/hc/article_attachments/14798317611671)
- Make presets for shadow and blur effects![](https://help.figma.com/hc/article_attachments/14798291149207)
- Create reusable scaffolding in the form of rows, columns, and uniform grids![](https://help.figma.com/hc/article_attachments/14798333022871)

#### Note

You may have heard about tokens, or seen them in another design system. At the time this course was written, Figma was still working on features to support tokens.

In June 2023, Figma launched support for variables. You can follow Kai as they explore bringing tokens to the Habitz design system in [Update 1: Tokens, variables, and styles](https://help.figma.com/hc/en-us/articles/18490793776023).

### Components

Components are the building blocks of our designs. In a design system, they’re the elements, structures, and patterns we want to reuse in our designs.

They can be individual elements, like icons or buttons; or a collection of elements, like menus and layouts.

There are two aspects to a component:

1. A **main component** that defines the properties of the component.
2. An **instance**, or copy of the component, you can reuse in your designs which receive any updates made to the component.

![](https://help.figma.com/hc/article_attachments/14798279719831)

### Libraries

Libraries are collections of styles and components shared within a team or organization. They establish consistency, streamline workflows, and keep elements up to date across designs.

1. Select the styles and components you want to share
2. Publish them as a library to your team or organization
3. Access libraries to use styles and components in your files
4. Review updates and apply them across the file

## Structure your library

There are lots of different ways to set up a library. In Figma, each published library is linked to a file. But a library could use styles and components from another library.

You could keep everything in one file as a single source of truth. Or break it into individual files to better suit your team or organization’s needs.

#### Considerations

- Does your product design team share colors and assets with your brand team?
- Does your company have multiple themes, separate products, or a collection of brands?
- Are there resources that you want to share—or don’t want to share between brands or products?
- Do you have separate design and engineering teams for desktop and mobile development?
- Do your design system users need access to every style and component?

#### Habitz

The Habitz team are a small company with a single product. They’re still exploring the value a design system could bring to their product design team. It may take some time for the rest of the company to get on board. For now, Kai and the team will create a single file for their style and component library. ![](https://help.figma.com/hc/article_attachments/14798380498839)

As their design system matures, they may need to consider breaking up their components between files. For example:

- A separate file for their foundational styles
- A dedicated icon library
- Separate component libraries for web and mobile
- And perhaps some functional components, like a wireframe library or sticker set![](https://help.figma.com/hc/article_attachments/14798411070999)

Kai sets up a `Design systems` project within their design team and creates a new design file. They want to use [pages](https://help.figma.com/hc/en-us/articles/360038511293) to organize the different aspects of the system.

They set up a `Welcome` pages to introduce the system, as well as pages for `Foundations`, `Components`, and `Patterns`.

#### Your design system might be different

The approach that works for you may be different to what works for Kai and the Habitz team. Check out our best practices guide for more information and guidance.

- [Best practices: component, styles, and shared libraries](https://www.figma.com/best-practices/components-styles-and-shared-libraries/)
- [Twitter thread: Figma component library structure](https://twitter.com/disco_lu/status/1630217466088497153)

## Component architecture

Back in the audit file the team made earlier, the Habitz team have organized their design elements into groups. They identified a variety of elements that exist across their designs: a range of colors, a number of fonts and text sizes, and a bunch of icons.

Beyond those foundational elements, there are some other consistent patterns across designs, as well as some obvious discrepancies.

When it comes to turning these into components, the team are a little overwhelmed and don’t know where to start. Kai suggests they use the principles of atomic design to rebuild their components from scratch.

### Atomic design

Atomic design, [popularized by Brad Frost](https://atomicdesign.bradfrost.com/chapter-2/), takes cues from the structure of chemical compounds: atoms, molecules, and organisms. And uses this analogy to describe a modular approach to building components.

- **Atoms** are the basic building blocks of matter. In a design system, they represent elements that can’t be broken down any further without losing its function. Like an icon, input field, or button.
- **Molecules** are groups of two or more atoms that are bonded together. In a design system, they’re a collection of individual elements that together form a single unit. Like a search bar made up of an icon, input field, and button.
- **Organisms** are complex structures made up of molecules and atoms. Like a navigation menu that includes a search bar, along with a logo and other menu items.

![](https://help.figma.com/hc/article_attachments/14798360117783)

### Habitz atomic design

The Habitz team take a look at some of their more complex elements (`organisms`), check to see if there are parts of that element that are reused elsewhere (`molecules`), and identify the basic building blocks of each (`atoms`).

There are some components in the Habitz app that have stricter applications. The team have decided to capture these as patterns, separate from their more atomic and molecular components.

This makes it clear to people using the system that these components should be implemented in the specific way they’ve been created.

In this header element, we have an avatar, the brand word mark, and a notifications icon. Each of these elements are atomic components, they can function alone or be combined with other atoms and molecules to create new designs. But the header must always consists of these three elements in this specific order, so we treat this component as a pattern.

![](https://help.figma.com/hc/article_attachments/14798430983831)

#### Think modular

Even if you don’t call them atomic components, a modular approach that has that flexibility is worth considering. To learn more about atomic design, check out the resources we’ve linked.

- [Atomic design](https://bradfrost.com/blog/post/atomic-web-design/)
- [Best practices: Component architecture in Figma](https://www.figma.com/best-practices/component-architecture/)
- [Best practices: Creating and organizing variants](https://www.figma.com/best-practices/creating-and-organizing-variants/)

## Naming conventions

The team have identified universal attributes of their designs, like color and typography. They’ve also grouped elements from their audit into components and patterns.

Before they start building out these components, they need to align on an approach for naming them.

Kai reached out to the engineering team to align on a common naming convention to make moving from design to code easier for everyone. The engineering team already uses camelCase for their elements in code. So Kai decides to also use this approach for layer names, components, and component props.

With a clear path forward, the Habitz team divides the work between them and gets started building out the system.

#### Be consistent with naming

You might prefer another approach for your design system. Like SnakeCase, Title Case, or ALLCAPS. Or maybe you’ll separate words with dashes or dots. Whatever you choose, having the same name for an element in design and code is more important than the way you write it.

# Chapter 2: Build your foundations

## Spacing

[In the previous lesson](https://help.figma.com/hc/en-us/articles/14552740206743/#Spatial_systems), we talked about spacing and how it contributes to the architecture of our designs. The Habitz team uses a modified version of an 8-point grid system, which allows for some limited flexibility around 4 and 6 points as they work on mobile experiences.

There are a few Figma features they can use to keep things in line. But for the most part, spacing will be communicated to design system users through their documentation. We’ll follow Kai as they [document these decisions in the next lesson](https://help.figma.com/hc/en-us/articles/14552804059927/).

![](https://help.figma.com/hc/article_attachments/14798548218903)

### Layout guides

**Note**: The Figma feature "layout grid" has been renamed to "layout guide" and may not match what you see in the video course.

To help enforce the grid system, Kai can define layout guide styles. Layout guides can be made up of rows, columns, or a uniform grid like the 8-point grid.

![](https://help.figma.com/hc/article_attachments/14798595376023)

1. Create a frame and name it default grid.
2. In the **Layout guide** section of the right sidebar, click .
3. Click  to adjust the properties.
4. Update the **Size** to `8` and leave the default color.
5. Click in the Layout guide section, then  to create a new style.
6. Name the new style `8 point grid` and add a description.
7. Click **Create style**.

Another inconsistency in their existing designs were icon designs and sizes. A modular layout guide—a combination of two or more guides—would help designers create standard dimensions and padding for icons.

![](https://help.figma.com/hc/article_attachments/14798628806295)

In Figma, you can apply multiple layout guides to a frame and define them as a single style. Kai wants all of their icons to live in a 24 by 24 frame, with consistent padding between the icon and its parent frame.

1. Create a frame with the 24 by 24 dimensions.
2. Add a layout guide and change the Type to column.
3. Set the **Count** to `1`, **Gutter** to `0`, and the **Margin** to `3`.
4. Hover over the guide in the right sidebar and press `⌘Command` / `Ctrl` `D` to duplicate it.
5. Click  and update the **Type** to **row**.
6. Finally, click  and
7. Name the new layout guide style `Icon grid` and click **Create style**.

### Auto layout

They also want to make use of [auto layout](https://help.figma.com/hc/en-us/sections/13165750874519-Auto-layout), a property you can add to frames. With auto layout you can define the [space between layers](https://help.figma.com/hc/en-us/articles/360040451373#spacing-between) in a frame, as well as any [vertical and horizontal padding](https://help.figma.com/hc/en-us/articles/360040451373#padding). This allows you to maintain consistent spacing and layout as the frame’s content changes.

The Habitz team can keep elements aligned to the 8-point grid, by making sure each auto layout property is a multiple of 8.

![](https://help.figma.com/hc/article_attachments/14798594335127)

### Nudge settings

To make it easier to quickly update the distance between layers, Kai updates their [big nudge settings](https://help.figma.com/hc/en-us/articles/4404575206295-Set-small-and-big-nudge-values) to **8** point. Nudge values are set per person, so Kai makes a note to add this as a suggestion for other designers.

![](https://help.figma.com/hc/article_attachments/14798653847575)

## Color

You can see color in every aspect of the Habitz designs. There are different hues, tints, and tones that represent the brand’s primary colors. Without a limited palette of colors, it would be easy for the team to end up with an infinite number of colors or inconsistent values between designs.

![](https://help.figma.com/hc/article_attachments/14798657793687)

The Habitz team can use [styles](https://help.figma.com/hc/en-us/articles/360038746534) to not only define their colors, but to make it easier to apply and update colors across the design system.

They’ve already collected the different colors used in their designs. The next step is to create color styles for all of the colors they’ve collected. Before they do that, they need to define a system for naming and organizing the color styles.

### Name your color styles

There are a few different approaches you could take to naming:

- If you had multiple brands or themes, you could organize your colors that way.
- You could organize colors by type. Like by primary and secondary functions, or by application, like text, buttons, and alerts.
- Or you could arrange colors by hue.
- If your engineering team already has an established color palette, you can align with that to avoid duplicating your efforts.

![](https://help.figma.com/hc/article_attachments/14798659753879)

Kai wants to make it easy for designers to find the right styles. So they’ll start with some basic functional groups With the goal of partnering with the engineering team and moving towards a semantic token system in the future.

With a functional approach in mind, four distinct groups emerge:

- The primary brand colors, with a variety of tints and tones.
- A range of neutral colors for less important elements and actions.
- A selection of colors for defining user habits.
- And some colors for specific functions in the app, like destructive actions and alerts.

![](https://help.figma.com/hc/article_attachments/14798825261719)

### Create color styles

The Habitz team can use the slash naming convention in Figma to organize the styles into groups. For every slash they add to the style’s name, Figma creates another folder or level of organization.

Kai creates styles for the two functional colors. To name the styles, they add its function, followed by a slash, then a value.

They use the description to guide designers towards any specific use cases. But they’ll also need to build out some documentation that explains this approach to naming.

![](https://help.figma.com/hc/article_attachments/14798832110487)

## Typography

Typography is an important aspect of the Habitz app. You can see typography in core elements and experiences, like habits, app cards, and even the calendar.

Kai can use [text styles in Figma](https://help.figma.com/hc/en-us/articles/360039957034-Create-and-apply-text-styles) to define properties like font family, weight, and size, as well as line-height and letter spacing.

### Define the type system

They need to define a semantic type system, that captures how text is used in the app and is easy to understand and apply.

During the audit, Kai identified two typefaces—or font families:

- **Space grotesk**: A futuristic monospaced font which they use for larger text sizes, like headings and titles. ![](https://help.figma.com/hc/article_attachments/14798852368023)
- and **DM Sans:** a lighter sans-serif typeface, which they use for smaller text sizes, like descriptions and the calendar layout.![](https://help.figma.com/hc/article_attachments/14798888804631)

Between these two typefaces, they identified 12 unique combinations of color, size, weight, line height, and letter spacing.

![](https://help.figma.com/hc/article_attachments/14798885124887)

In Figma, a text layer’s color is defined by a color style, not a text style. So Kai consolidates any text differentiated by color alone.

![](https://help.figma.com/hc/article_attachments/14798909933975)

There’s also typography for specific applications, which they can document as exceptions instead of including them as distinct styles. Like this third typeface, Smooch Sans, which is used more like a visual element than a text style during the *add habit* flow. Or these text layers in different weights.

![](https://help.figma.com/hc/article_attachments/14798915318807)

### Apply semantics

They now have seven distinct combinations of text properties, with font sizes that loosely follow the major second scale and fit within an 8pt grid. From these styles they identify two main use cases:

- Four **title** styles for core elements and wayfinding, like page headings and card titles.
- And three **body** styles for page content or long-form text, like descriptions, calendar days and dates.![](https://help.figma.com/hc/article_attachments/14798990374807)

They could categorize them further by use case, but they’d end up with multiple styles that share the same properties. Instead, they decide to organize them further by size.

- Both title and body styles have a base size of 16 points,
- as well as medium and large styles,
- with an extra large title style

They update the text samples to better reflect their size, then create a text style for each one. They use the slash naming convention to create separate groups by use case—title and body—and size.

![](https://help.figma.com/hc/article_attachments/14799015921303)

## Elevation

In our previous lesson, we spoke about how elevation can establish hierarchy, create separation, and communicate interaction.

The Habitz team has embraced a flat minimalist approach across most of their designs. But there are a few elements that stand out from the rest: buttons, cards, and the main navigation menu.

They all share a bold neo-brutalist style, with a thick black border and a solid offset shadow. While you can interact with other elements in the app, this styling draws attention to the core focus of the app: creating and managing habits.

![](https://help.figma.com/hc/article_attachments/14799019050263)

### Additional styles

At the moment, the elements all have the same properties, so technically Kai only needs one entry for elevation in the design system.

But Kai and the team have been considering other ways to use elevation. Like changing an element’s elevation when you interact with it. Kai thinks extra chunky shadow for focused elements would help low-vision habit trackers.

They decide to define three levels of elevation: `4` to match the value of the current shadow and two extra values consistent with their spacing system: `6`, and `8`.

By aligning on these values and defining these styles now, the team has approved resources whenever they’re ready to explore those ideas.

![](https://help.figma.com/hc/article_attachments/14799054904983)

### Define shadow effect

They create a square frame, round the corners, and add a fill. They add a text layer to label the shadows. They create two more frames and update the labels accordingly. Then select all the frames, apply auto layout, and adjust the padding and space between them.

In the right sidebar, Kai adds an **Effect** and edits the settings of the default drop shadow. To get that neo-brutalist style, they set the **blur** to zero and the shadow **opacity** to 100%. They repeat the process for the remaining two levels.

### Create effect styles

Now Kai can [create styles](https://help.figma.com/hc/en-us/articles/360038746534-Create-color-text-effect-and-layout-grid-styles) for these properties. They select the first frame and click the  in the **Effects** section, then the  to create a new style.![](https://help.figma.com/hc/article_attachments/14799072610327)

They name it `elevation/4`and add a description. Then repeat the process for the `6` and `8` level shadows. If we view the file’s local styles, all three shadows are grouped in an elevation folder.![](https://help.figma.com/hc/article_attachments/14799142048023)

## Icons and illustrations

The Habitz team uses icons and illustrations to support the personality of their brand: a bold neobrutalist style with some whimsical elements.

![](https://help.figma.com/hc/article_attachments/14799121209495)

### Create icon components

They aligned on supporting three different icon sizes: 16, 24, and 32. They start by building the middle icon size.

They place each icon in a `24` by `24` frame, aligned to the icon grid they created earlier. This makes sure icons are centered, aligned, and consistent in size when [swapping between icons](https://help.figma.com/hc/en-us/articles/360039150413). They did the same thing for icons with dimensions of `16` and `32`.

![](https://help.figma.com/hc/article_attachments/14799163284631)

With every icon in their collection selected, they select **create multiple components** from the toolbar, and turn each icon into a component.

Kai checked with the Habitz engineering team to make sure icon names are consistent with code, as well as searchable by anyone using the design system.

They aligned on a naming structure of *icon / size / name* and applied that to all icons. This makes sure icons are grouped in the assets panel, first by icon, *then* size.

![](https://help.figma.com/hc/article_attachments/14799187613591)

Because the icons are now components, they can [add descriptions](https://help.figma.com/hc/en-us/articles/7938814091287) to communicate their intended use. They can also include extra search terms to make the icons easier to find.

### Illustrations

Habitz uses illustrations to reinforce their brand and add that touch of whimsy to the product. Like icons, illustrations benefit from consistent frame sizes, and thoughtful naming and descriptions.

The Habitz team uses illustrations in two ways: as large hero images during onboarding screens, and as smaller illustrations on app cards. These smaller illustrations also have an optional accent color.

### Create component sets

Kai wants to create two separate component sets, one for each use case. This will make it easier for designers to find the right illustration for their context. They start by giving each illustration a name that captures both its use case and type.

With the hero illustrations selected, they choose **Create component set** from the toolbar. In the right sidebar, they update the default property in the **Properties** section (Property 1) to rename it `type`.

For the smaller illustrations, Kai wants to add another attribute to each name, to account for the accent color.

Kai selects the card illustrations with the accent color and uses [bulk rename](https://help.figma.com/hc/en-us/articles/360039958934) to add `/true` to the end of the current name. Then uses `/false` for the illustrations without the accent color.

With all the card illustrations selected, they click **Create component set.** Because of the extra attribute, the component set has two properties with correct values for each variant. They update the property names to `type` and `hasColor` respectively.

To make the illustrations easy to find, they decide to add `illustration/` to the beginning of each component set’s name.

# Chapter 3: Build components

Now that Kai has the foundations of the design system captured, it’s time to put these concepts together.

## dayToggle component

One core flow of the Habitz app is creating a new habit. As part of this process, users select which days they want to include in their habit schedule.

Kai wants to create a pattern for this schedule, but to make a pattern, they need a component that is the toggle for an individual day.

![](https://help.figma.com/hc/article_attachments/14799255069335)

### Create variants

The component needs two different states: a deselected state, and a selected state. Kai uses this existing element of the selected state and:

1. Presses  to turns it into a component
2. Rename the component to `dayToggle`
3. Use **Create variant** in the right sidebar to create a new variant and variant property
4. Set this to `false` for the new variant and rename the property to `isSelected`
5. Style the false variant: remove the stroke property of the new component and change the fill color to *primary/1*.
6. Set the component property to `true` for the original *Selected* variant

#### Question

Habitz also allows people to track a habit multiple times a day. How would you make a variant that shows the habit frequency? Check out the file to see what the Habitz team made.![](https://help.figma.com/hc/article_attachments/14799257596183)

### Add a text component property

The Habitz team will need to use this component for every day of the week. Kai could create a variant for each day, but to better support multiple languages, they create a text component property instead. That allows designers to update the text to match the day.

1. They select the text layer
2. In the **Content** section, create a text component property.
3. Name it `dayCharacter`.

### Set default variant

Lastly, Kai wants the deselected variant to be the default component of this set. In Figma, the default variant is the component in the top-left corner. They swap the variants to suit. Then, name the component set `dayToggle`.

## actionPresentationCard component

In addition to call-to-action buttons, Habitz has interactive cards made up of three elements:

- an editable text layer,
- an illustration
- and an icon

![](https://help.figma.com/hc/article_attachments/14799308853271)

### Build default component

Because the cards are interactive, they need four states: *default*, *hover*, *focused*, and *pressed*. Kai starts by building the default state, with the three elements we mentioned earlier.

They set the frame fill to **primary/1** and the effects are set to **elevation/100.**Then they set up component properties for the aspects of the component that designers will be able to adjust.

#### Instance swap property: illustration

First, Kai needs to define how the card illustration can be swapped for another illustration.

1. With the illustration selected, they create an [instance swap property](https://help.figma.com/hc/en-us/articles/5579474826519#h_01G2Q5FYN2ADEDQ3ZSB1KKY8Z0).
2. They name it *illustration* and click  **Create property**.

#### Text property:

Next, Kai wants to make it so people can update the contents of the text layer.

1. They select the text layer and in the **Content** section, click the  **Create property** button.
2. They name it `text` and make sure the default value is `add`.

#### Instance swap property: icon

Finally, Kai wants designers to be able to change the component’s default icon to another icon. They can do this using an instance swap property.

1. They select the icon and click **create component property** in the right sidebar
2. They select  **Create property**... and name the property `icon`.

### Create variants

Now that Kai has component properties for the default state, they can set up variants for the remaining states.

![](https://help.figma.com/hc/article_attachments/14799313424023)

#### Hover

1. Kai selects the default component and  [adds a new variant](https://help.figma.com/hc/en-us/articles/360056440594#create-new-variants).
2. From the right sidebar, they rename the variant `hover` and the property to `state`.
3. The only difference between the **hover** and **default** states is the color, so all Kai needs to do is click *primary/1* in the right sidebar and change the color to *primary/5*. All done!

#### Focused

The focused state has a more prominent stroke compared to the default. To create the focused state, they:

1. Select the component set
2. Add a new variant
3. Rename it `focused`
4. Increase the stroke weight to `4`

#### Pressed

1. Finally, Kai creates a new variant for the pressed state.
2. Name it `pressed`
3. Update the **fill** color to *primary/20*
4. Remove the elevation effect style

### Build other components

Kai and the team continue to build out more components for their system. To see all the component they’ve created, check out the **Components** page in the Habitz file.

# Chapter 4: Patterns

With their flexible components created, Kai is now ready to build out some of the fixed patterns in the design system.

## daySelector

A core part of the Habitz app is letting people set a schedule every time they create or edit a habit. Given its importance in the app, Kai wants to create a fixed pattern so it’s always created in the same way.![](https://help.figma.com/hc/article_attachments/14799345317911)

### Build weekly schedule

Kai decides to build the weekly schedule using the existing dayToggle component.

1. From the **Assets** panel, Kai finds the dayToggle component and drags it onto the canvas to create an instance.
2. To make it easier to add new toggles, [add an auto layout frame](https://help.figma.com/hc/en-us/articles/5731482952599#add) around the toggle.
3. Press `Enter` to select the child layer.
4. Use the `⌘Command` or `Ctrl` `D` shortcut to create seven toggles in total.
5. Update the **direction** to  **horizontal**
6. Update the **padding** on all sides to `0`
7. Update the  **space between** to `10`

### Configure component properties

In the component section of the right sidebar, Kai can see the component properties they set up earlier.

1. They update the *dayCharacter* property to the correct day
2. Then change the name of each toggle to match
3. Click  **Create component**in the toolbar
4. Name the new component `daySelector`

### Add component description

The order of days should always be chronological, but they can be rearranged to accommodate regional differences for the first day of the week. Like Saturday, Sunday, or Monday.

Kai wants to communicate this to anyone who uses the component. In the right sidebar, they click the edit icon and add this information to the description.

## navigation

Kai continues by defining another pattern. This one is a core navigational element in Habitz: a floating menu bar where users can create new habits and move between different pages of the app.

![](https://help.figma.com/hc/article_attachments/14799368558743)

This navigation element has a **fixed** layout with no customizable properties. It changes state depending on which page the user is on in the app.

Kai uses variants to represent each state. An alternative approach might be to create boolean properties for the pattern, however this could allow for a state where both indicators are active. Variants are a way to ensure that only one state is selected at a time.

If you want to see exactly how this component set was built, grab a copy of the Habitz design systems file and check it out!

#### Summary

Together, the Habitz team has created order out of chaos.

- They turned a jumble of different elements and designs into a comprehensive library of components.
- They created patterns for the system’s more structured components.
- They defined styles for color, typography, elevation, and layout guides.
- They curated a collection of brand-friendly icons and illustrations.
- They were intentional about what designs to include in the design system and what to leave out.

### Next steps

Before the Habitz team makes the design system available to the whole company, they want to set everyone up for success.

The team wants to make sure everything is documented so that other people know how to use the system. They also want to create a process for updating and maintaining the system over time.

Lastly, Kai wants to get feedback from key stakeholders across the company—like the brand and engineering teams—to make sure the system fits in with other teams’ practices and resources.

In the next video, we’ll check back in with Kai and the Habitz team as they document their design system, support people who want to use it, and decide how to maintain it over time.

[2: Define your system](https://help.figma.com/hc/en-us/articles/14552740206743) [4: Document, update, maintain](https://help.figma.com/hc/en-us/articles/14552804059927)
