---
기술지원명: Update 1: Tokens, variables, and styles
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Update 1: Tokens, variables, and styles
출처링크: https://help.figma.com/hc/en-us/articles/18490793776023-Update-1-Tokens-variables-and-styles
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

This is a written version of our [Introduction to design systems: Update 1](https://www.youtube.com/watch?v=JyCmacSyDY4) video tutorial. We’ve edited some of the language for brevity. Watch the video and follow along with the written course below.

Previously in our Intro to Design Systems course, we followed Kai—a product designer at a habit-forming app called Habitz—on their journey to building their first design system in Figma.

Since implementing their design system, the Habitz team has seen more consistency in designs and no longer debates endlessly over which standards to use.

The Habitz app is evolving and growing, and they have some new challenges to address:

- **Theming**: After discovering that users track their habits before bed, the team wants to add a dark theme to ease tired eyes.
- **Spacing inconsistencies**: While the spatial system has sped up the design process and solved alignment issues, the team struggles to keep track of which border radius and spacing values to use. This has led to an unpredictable and inconsistent user experience.
- **Team growth**: They're adding new teammates and features, and want a more efficient way to manage changes and improve accuracy during the handoff process.

Kai has been learning about design tokens and believes this could be the next step in supporting scalability of the Habitz design system.

# Chapter 1: Design tokens

The benefits of design tokens are very similar to that of design systems.

- Provides a single source of truth to maintain consistency between design and code
- Improves management of a scaling design system
- Removes the guesswork when building products
- Help you build more efficiently

## What are tokens?

But what exactly are design tokens? How might they help the Habitz team? Design tokens are a method for managing design properties and values across a design system.

Each token stores a piece of information—such as color, sizing, spacing, font, animations, and so on. To make them easier to refer to, each token also gets a name.

![](https://help.figma.com/hc/article_attachments/18492500044055)

### A source of truth

The tokens can be reused across your designs, and become a source of truth and a shared language between design and code.

![](https://help.figma.com/hc/article_attachments/18492515990807)

#### **Habitz**

Here's an example where *not* using tokens lead to confusion within the Habitz team.  
  
 Kai recently handed a design file to a developer that contained spacing values of 25pt. However, the Habitz codebase uses an 8pt spatial system. The developer assumed this was intentional and updated the codebase with the new designs.

![](https://help.figma.com/hc/article_attachments/18492609675287)

Oops! Kai meant to have spacing values of 24pt, but their file was set up incorrectly. If the team used tokens, the design file would have included information on which *spacing token* to use. The spacing token would point to a correct value, preventing errors and ambiguity.

![](https://help.figma.com/hc/article_attachments/18492609681175)

### Increased efficiency

In addition to being a reliable source of truth, tokens make updating our designs and design systems more efficient.

#### **Spotlight on Habitz**

Imagine the Habitz team has a color token being used in different areas of the product. If they change the value of this color token, then every asset using the token will change too.

![](https://help.figma.com/hc/article_attachments/18492679980439)

This can be useful, like when changing a color system for a product rebrand. But what if they only wanted the values of *some* assets to change? Currently, they’d have to remap these values one-by-one to a different token.

![](https://help.figma.com/hc/article_attachments/18492691564311)

This isn’t a problem if ‌only a few assets need updating. But if assets had to be updated, the Habitz team would need a lot more time and resources! This is where aliasing can help.

## Aliasing

Aliasing allows any token to reference—or take on—the value of another token. If a token changes, then any token referencing it will update as well.

![](https://help.figma.com/hc/article_attachments/18492125409431)

But how does this solve the Habitz team’s problem? Aliasing lets you organize tokens into categories and sub-categories. These categories communicate how a token is used.

![](https://help.figma.com/hc/article_attachments/18492080430231)

If Habitz had their tokens set up correctly, they’d be able to update any category, and all associated tokens downstream would get updated, without unintentionally affecting others.

![](https://help.figma.com/hc/article_attachments/18492080434327)

There is no limit to how far a series of token references can go. And no limit to how many times a single token can be referenced. This allows us to create complex design token structures.

![](https://help.figma.com/hc/article_attachments/18492691567383)

Keep in mind, aliasing isn’t always necessary, especially for assets like fonts and animations.

## Organizing tokens

After realizing the benefits, the Habitz team decided to implement design tokens into their system. Before they jump in, they want to understand how tokens can be organized.

Here's a common way to structure design tokens:

- [Primitive tokens](#token-organization)
- [Semantic tokens](#semantic-tokens)
- [Component-specific tokens](#semantic-tokens)

Each type communicates the **what** (primitive), **how** (semantic), and **where** (component-specific) of a token. Let’s take a closer look at each one!

![](https://help.figma.com/hc/article_attachments/18492822651031)

### Primitive tokens

Primitive tokens tell us **what** properties and values exist within our designs. Sometimes known as **global tokens**, they ‌define the values in a system.

For example, primitive color tokens would include every color used in the app and its brand. While primitive spacing tokens would include all padding, margin, and spacing between values.

In this kind of token structure, primitive tokens are for **reference only.** They provide the foundation for other tokens, so you wouldn’t apply them directly to elements in your designs.

![](https://help.figma.com/hc/article_attachments/18492786782871)

### Semantic tokens

Semantic tokens give us context on how the token should be used. Assets with [semantic names](https://help.figma.com/hc/en-us/articles/14552740206743-Lesson-2-Define-your-design-system#name) convey **meaning**, **purpose**, and **how** and **where** the asset should be used. You can apply semantic tokens to your designs.

For example, the token `surface/brand-contrast` references a primitive token `pink/400`. It takes on whatever value is set to.

![](https://help.figma.com/hc/article_attachments/18492855282327)

`Surface` tells us that it should be used for an object’s background color. `Brand` indicates the color is central to the app’s identity. And `contrast` indicates the color is saturated and should be used to draw a user’s attention or focus.

### Component tokens

Component-specific tokens tell us **where** a token can be used. And yep, these are used directly in designs, too.

![](https://help.figma.com/hc/article_attachments/18492905817239)

Say we have a set of buttons (`primary` and `secondary`) each with a state (`default`, `hover`, and `inactive`).

![](https://help.figma.com/hc/article_attachments/18492881850007)

We could create a token for each one and reference a semantic token. For example, button primary could reference ‌surface/brand-contrast since primary buttons should grab a user’s attention.

The token for this could look something like `button-primary-background-default`.

![](https://help.figma.com/hc/article_attachments/18492949986071)

The rest of the buttons’ tokens would follow this same format: `asset`-`typepropertystate`.

![](https://help.figma.com/hc/article_attachments/18492927937303)

This level of tokens is detailed and more commonly used by larger, enterprise-level systems. Component-specific tokens might not be necessary for everyone. [**Components, styles, and library best practices →**](https://www.figma.com/best-practices/components-styles-and-shared-libraries/)

### Order your tokens

Design token structures should always begin with a foundation of primitive tokens. Beyond that is entirely up to the unique needs of your system and organization.

You might only need semantic tokens *or* component-specific tokens. You might need both, in that order, or the other way around. Your semantic and component tokens could be on the same level. Or you might even want to have multiple levels of each type.

![](https://help.figma.com/hc/article_attachments/18492965506455)

Whatever the format, make sure to plan what your token structure will look like. This will save you hassle in the long run, as any future restructures could require significant time and effort.

# Chapter 2: Implement tokens in Figma

Now that we’ve got a better grasp on design tokens, let’s check back in with the Habitz team. They’ve decided to set up both **semantic** and **component-specific** tokens, on the same level.

Since their design system already lives in Figma, they can use two key Figma features to implement their tokens: [styles](https://help.figma.com/hc/en-us/articles/360039238753) and [variables](https://help.figma.com/hc/en-us/articles/15339657135383).

## Styles and variables

You might be wondering, why should the Habitz team use both styles *and* variables?

Variables can support complex token structures, because they can be used to define other variables and styles. They also support multiple modes for theming, scoping for specifying where a variable can be used, and code syntax for a better handoff experience.

Meanwhile, styles can support color gradients and composite values, like multiple fills or multiple shadow effects.

|  |  |  |
| --- | --- | --- |
| **Functionality** | **Variables** | **Styles** |
| Define other variables and styles | ✓ | ✕ |
| Supports multiple modes or themes | ✓ | ✕ |
| Supports scoping to specify usage | ✓ | ✕ |
| Supports code syntax | ✓ | ✕ |
| Supports color gradients | ✓ | ✓ |
| Supports composite values (like a solid color and a gradient) | ✕ | ✓ |

For many, implementing design tokens means using a combination of styles and variables. Check out our guide on the [differences between styles and variables](https://help.figma.com/hc/en-us/articles/15871097384471%0A%20%20%20%20%20%20%20%20%20%20%20).

## Migrate colors

Kai is interested in diving into migrating colors first. If you followed along with [Lesson 3](https://help.figma.com/hc/en-us/articles/14548865734679), you’ll know that the [Habitz app’s color system](https://help.figma.com/hc/en-us/articles/14548865734679-Lesson-3-Build-your-design-system#color) is connected to color styles, organized by purpose or usage.

![](https://help.figma.com/hc/article_attachments/18493170139799)

The Habitz team decided to migrate all of their color styles to variables except for one gradient, which they’ll keep as a style since variables can’t capture gradients.

They [create a new variables collection](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables#01H8044A3JH5079S16V2YHA1RV) called **Primitives** for their primitive tokens and copy each color value over.

![](https://help.figma.com/hc/article_attachments/18493208936983)

**Tip**: You can use the eyedropper in the color picker to select a value.

Each color variable is organized by their base color — pink, neutral, green, blue, red, purple, orange, and yellow. Within each base color, a ramp is created based on their tint and shade using a numbering system. The more white a base color contains, the lower its number. The more black it contains, the higher the number.

![](https://help.figma.com/hc/article_attachments/18493208939799)

**Tip:** To prevent primitive tokens from being used directly in designs, you can hide them from getting published to team libraries. From the **Primitives** variable collection:

1. Select all the variables
2. Right-click and choose **Edit variables**.
3. From the edit modal, uncheck **Show in all supported properties**.
4. Check **hide from publishing**.

![](https://help.figma.com/hc/article_attachments/18493170159127)

## Create semantic tokens

Next, they want to direct ***how*** and ***where*** the colors can be used. So, they create a second variables collection called **Tokens** for their semantic and component-specific tokens.

![](https://help.figma.com/hc/article_attachments/18493208949143)

The team conducted an audit to document every color used in the product, and identified a few areas that use color: surface, button, text, border, and icon. Within each area, they further identified color categories—like brand, toasts, user colors, and more.

![](https://help.figma.com/hc/article_attachments/18493170185239)

From there, they established tokens within each category and gave them names that communicate “how” or “where” the color can be used.

For example, a semantic token might include the word `primary` to communicate its use on the most common elements or actions on a page.With `secondary` for less common elements.

![](https://help.figma.com/hc/article_attachments/18493208956311)

After creating these tokens, they organize them into variable groups based on their categories, and apply them to their designs.

![](https://help.figma.com/hc/article_attachments/18493208961943)

## Dark mode

Now that their color primitives and semantic tokens are set up, how might the Habitz team tackle dark mode?

![](https://help.figma.com/hc/article_attachments/18493170191639)

Remember that every semantic and component-specific token is assigned a job and communicates a function.

To add a dark mode or any other theme, you need to create a *separate set of tokens* that mirrors your existing tokens.

![](https://help.figma.com/hc/article_attachments/18493208972695)

In Figma Design, we can account for light and dark themes using variable [modes](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables).

Variable [modes](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables) represent the different contexts of our designs. A mode contains a list of values for a variable within a collection, storing one value per variable.

If a variable collection has multiple modes, then we can switch modes on layers and elements to quickly change designs for different contexts. Like a light and dark theme.

Kai [creates a new mode](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables#Create_a_mode) in the `Tokens` collection and updates references to variables in the `Primitives` collection.

And that’s it! There’s no need to change the names of tokens, since they already communicate information on *how* and *where* they’re used.

They can then change from light to dark mode by changing the mode in the right sidebar.

![](https://help.figma.com/hc/article_attachments/18492177824919)

## Define spacing tokens

The Habitz team is all done setting up their color tokens, so they tackle their spatial system using number variables next.

We cover creating number variables for spatial systems more in our [Intro to Variables tutorial](https://www.youtube.com/watch?v=1ONxxlJnvdM&t=617s), so be sure to check that out!

# Chapter 3: Name your tokens

If you’re ready to set up tokens for your design system, here are a few tips to help you with naming:

- Make sure tokens are easy to understand. Creating language-neutral names makes them approachable across different teams. You may want to factor in people from different countries as well.

  ![](https://help.figma.com/hc/article_attachments/18493300215447)
- Use full words instead of abbreviations. Abbreviations can be unclear and open to interpretation.

  ![](https://help.figma.com/hc/article_attachments/18493317042071)
- Be consistent with prefixes. For example, token names for background colors should start with “background” instead of it appearing in a different part of the name.

  ![](https://help.figma.com/hc/article_attachments/18493300235671)
- Use singular or plural names based on the context for which they're being used.

  ![](https://help.figma.com/hc/article_attachments/18493317059991)
- If you have multiple products or brands, avoid using the brand’s name in a token. Instead, choose a more generic name so the token can be used in broader contexts.

  ![](https://help.figma.com/hc/article_attachments/18493300259863)
- Future-proof tokens by anticipating potential growth of your design system. Token names should be able to accommodate new additions and modifications without causing confusion.

Now that their tokens are set up to go, Kai and the Habitz team are looking forward to building dark mode for their users, and experiencing the efficiency that this shared language provides! We’ll see you in the next one 👋🏻
