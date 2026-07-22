---
기술지원명: Get started with Make kits
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Get started with Make kits
출처링크: https://help.figma.com/hc/en-us/articles/39241689698839-Get-started-with-Make-kits
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

Available to [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on [paid plans](https://figma.zendesk.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan).

Admins of an organization can approve published Make kits and enable them by default. Learn how to [manage Make kits for an organization](https://help.figma.com/hc/en-us/articles/39313426360087).

## What are Make kits?

Make kits allow your team to jump straight into building designs and prototypes in Make that are realistic to how your product looks and functions without having to add code and style context from scratch.

Make kits can include:

- npm packages for code context
- Variables and styles from published Figma Design libraries
- Guidelines to help Figma Make understand how to use your system's assets

Once you've assembled a Make kit, you can publish it to your team or organization so that teammates can use the kit in their Figma Make projects to start building faster.

## Create and publish a Make kit

In a Make kit, you can add [npm packages](https://help.figma.com/hc/en-us/articles/35946832653975) to provide context on which assets—like components, styles, and tokens—to use, import variables and styles from [published design libraries](https://help.figma.com/hc/en-us/articles/360025508373), and write guidelines to provide context on how the assets should use style context and behave.

### Step 1: Start a new kit

Open a new Make file. Click  **Settings** in the top-right corner of the window and select **Create a kit**. From the pop-up modal, choose a starting point:

- **Assemble your kit:** Use existing npm packages and style context from your design libraries.
- **Start from scratch**: Build components and assets from scratch with Make.

### Step 2: Add npm packages and/or library styles

If you chose **Assemble your kit** as your starting point, then a modal will appear for you to import npm packages, public packages, and library styles to the kit.

![assemble-your-make-kit-modal.png](https://help.figma.com/hc/article_attachments/39315655618071)

If you choose **Start from scratch** as your starting point, you can prompt Make to build components for the kit. You can also click **Add items to your kit** to find packages and library styles to add.

**Note**: npm packages or libraries that contain a high volume of assets may take a few minutes to import to your kit.

### Step 3: Add custom configurations (optional)

If your npm package needs any custom configuration, such as requirements needed for Make to use your code packages, you can prompt Make to add those for you.

### Step 4: Add guidelines

Guidelines are essential for getting accurate, on-brand results from your Make kit. They teach Make how to properly use your components, when to apply specific variants, or how to follow your design system's rules.

When you start a Make kit, a **guidelines** folder is created in the file explorer with at least one markdown file (`.md`) for you to add information on how Figma Make should consume the kit. This helps Make create an app that better meets your needs and expectations. This includes instructions for how you want Figma Make to behave in terms of coding and personality, and how to use things like style context.

![add-guidelines-to-make.png](https://help.figma.com/hc/article_attachments/39315664803607)

The methods for adding guidelines to a Make kit is the same as adding guidelines to a Figma Make. Learn how to [add guidelines](https://help.figma.com/hc/en-us/articles/33665861260823).

When you're ready to start writing guidelines for your Make kit:

- Check out the section below to learn best practices for [guidelines for library styles](#h_01KMNQRFPC8J0SHQPKE9YXM0KJ)
- Check out our developer documentation for tips on [guidelines for design system packages](https://developers.figma.com/docs/code/write-design-system-guidelines/)

### Step 5: Test your kit

Testing your kit is a good way to see that the kit is working as intended and see if any adjustments are needed to npm configurations, assets, or guidelines. To test the kit, prompt Make to build something and look for anything that appear to deviate from your design system.

**Tip**: If you spot any issues, you can ask Make for feedback on what changes can be made to configurations and guidelines to alleviate them, and have Make implement them

### Step 6: Publish your Make kit

Once you’re done assembling your Make kit, you can publish it to your organization so your teammates can use it in their Make projects.

1. Click **Publish kit** in the top right corner.
2. A Make kit cannot be published if it lives in your drafts folder. If this the kit is in your drafts, you’ll be prompted to move it to a project in the organization.
3. Give your Make kit a name and thumbnail so that it’s easily identifiable.
4. Configure your package.
   - Choose whether to use default or custom package.json and vite.config.ts settings.
   - Update any advanced settings: npm package name or library, scope, version number. If you’d like to use the Make kit in a production setting as well as in Figma Make and your team has formal standards around how npm packages are named and organized, you can customize the scope in the package name to (@scope/package-name) to match your team’s requirements.
5. Click **Publish**.

![publish-make-kit-button.png](https://help.figma.com/hc/article_attachments/39315664804119)

## Guidelines for library styles

When your library styles are added to a Make kit, an empty `Guidelines.md` file is also added. Guidelines are critically important for ensuring Figma Make uses your library styles in a way that creates high quality, reliable results.

### Best practices

We recommend the following best practices when you’re writing the guidelines for your library styles.

#### Explain the quirks of your tokens before anything else

Some use unitless numbers that need `px` appended. Some have special characters in variable names that require careful escaping. Some mix shorthand and longhand properties in unexpected ways.

These format-level details are the first thing Figma Make needs to understand, because getting them wrong means every subsequent line of code could be subtly broken. If your spacing token `--spacer-3` equals `16` and not `16px`, that distinction matters enormously and it's easy to overlook. Put this kind of information right at the top of your guidelines, before you get into any specifics about which tokens to use for what.

#### Organize tokens around decisions, not around the CSS file structure

When someone is building a UI, they're thinking "I need a background color for this card" or "what's the right text color for a secondary label." They are not thinking "let me scan through all 200 variables in alphabetical order." This applies similarly to Figma Make.

Structure your guidelines around those decisions. Group tokens by what they help you do: picking backgrounds, choosing text colors, setting spacing, applying borders. Your guidelines don’t need to mirror the order of your CSS file.

#### Give typography its own dedicated section

Typography is where inconsistency creeps in fastest. There are so many properties involved (font family, size, weight, line height, letter spacing) that if there isn’t a complete picture of what's available, it’s easy to start improvising.

The most effective approach is a table that lists every typography class alongside its key properties and a short note about when to use it. This lets the Figma Make scan the full landscape of options in one place.

#### Create a clear priority between semantic tokens and raw color values

Make sure your guidelines describe a clear hierarchy for color tokens. Your design system may have semantic tokens with names like `bg-default` or `text-danger` that encode meaning and intent. It may also have raw palette tokens with names like `blue/300` or `grey/500` that are just colors without context.

Your guidelines should make it obvious how you want your color tokens used. For example, you’d likely want your guidelines to instruct that semantic tokens are the first choice, and raw palette values are a fallback for situations where no semantic token fits.

#### Tell Figma Make what not to do

Listing available tokens is necessary, but you also need to call out potential mistakes that could occur when working with your styles. For example, things like:

- Don't use the brand color as a page background.
- Don't hardcode pixel values when a spacing token exists.
- Don't pair dark text with dark backgrounds.

These constraints are just as important as the tokens themselves. Without them, it’s like technically having all the right building blocks but no guidance about how not to combine them.

#### Include code snippets for tokens that require composition

Some design tokens are split across multiple variables that need to be combined to produce a single CSS property. Shadows are the classic example, where you might have separate tokens for offset-x, offset-y, blur, spread, and color that all need to be stitched together into one `box-shadow` declaration.

For these cases, include a complete code snippet in your guidelines. The snippet removes all ambiguity about ordering, units, and syntax.

```
# Patternz Design System Guidelines

## Setup

Import the styles CSS in your application:

```tsx
import "../Patternz/styles.css";
```

## Token format quirks you need to know first

Before you use any token, understand these three things about how this stylesheet works. Getting any of them wrong will silently break your styles.

**1. Most numeric values are unitless.** Spacing, border-radius, font-size, shadow offsets — they're all raw numbers. You must multiply by `1px` when using them in CSS. If you write `padding: var(--spacer-3)` you'll get `padding: 16` which is invalid CSS. Always use the `calc()` pattern:

```css
padding: calc(var(--spacer-3) * 1px);   /* becomes 16px */
gap: calc(var(--spacer-2) * 1px);       /* becomes 8px */
border-radius: calc(var(--radius-medium) * 1px); /* becomes 5px */
```

**2. Many variable names contain special characters.** Tokens use `✦`, `/`, and `🎨` in their names. In CSS you reference them with `var()` using the exact escaped names from the stylesheet (backslash before each `/`). In inline JSX styles, the escaping looks like this:

```tsx <div style={{ color: "var(--✦/_text/text-default)" }} /> ```

**3. Color tokens are already complete CSS values.** Unlike spacing, colors do not need any transformation. Use them directly:

```css
background: var(--✦/_bg/bg-default);
color: var(--✦/_text/text-secondary);
```

## Choosing backgrounds

When you need a background color, start here. These are the semantic tokens, organized by the decision you're making.

**Page and card surfaces:**

| Token | Value | When to reach for it |
|---|---|---|
| `--✦/_bg/bg-default` | `#FFF` | The default background for pages and cards |
| `--✦/_bg/bg-secondary` | `#F5F5F5` | Subtle alternate sections, sidebars, secondary containers |

**Interactive states:**

| Token | Value | When to reach for it |
|---|---|---|
| `--✦/_bg/bg-hover` | `#F5F5F5` | Hover state on clickable elements |
| `--✦/_bg/bg-selected` | `#E5F4FF` | Active or selected item highlight |
| `--✦/bg/disabled/default` | `#D9D9D9` | Disabled element fill |

**Dark surfaces (menus and toolbars):**

| Token | Value | When to reach for it |
|---|---|---|
| `--✦/_bg/bg-menu` | `#1E1E1E` | Dropdown menus, dark popover backgrounds |
| `--✦/_bg/bg-toolbar` | `#2C2C2C` | Toolbar backgrounds |

When using these dark surfaces, pair them with `--✦/_text/text-onbrand` and `--✦/_icon/icon-onbrand` for legible text and icons.

**Semantic status backgrounds:**

| Token | Value | When to reach for it |
|---|---|---|
| `--✦/_bg/bg-brand` | `#0D99FF` | Brand-colored fills for buttons and small accents |
| `--✦/_bg/bg-danger` | `#F24822` | Destructive or error backgrounds |
| `--✦/_bg/bg-warning` | `#FFCD29` | Warning banners |

**Tertiary (tinted) backgrounds** for lighter variations:

| Token | When to reach for it |
|---|---|
| `--✦/bg/brand/tertiary` | Light blue tinted background (`#E5F4FF`) |
| `--✦/bg/brand/tertiary-hover` | Hover state for the above |
| `--✦/bg/brand/tertiary-pressed` | Pressed state for the above |
| `--✦/bg/danger/tertiary` | Light red background for error regions |
| `--✦/bg/warning/tertiary` | Light yellow background for warning regions |
| `--✦/bg/default/tertiary` | Neutral grey tertiary (`#E6E6E6`) |

## Choosing text colors

| Token | Value | When to reach for it |
|---|---|---|
| `--✦/_text/text-default` | `#000000E5` | Primary text: titles, body copy, tab labels |
| `--✦/_text/text-secondary` | `#00000080` | Secondary labels, timestamps, inactive tabs |
| `--✦/_text/text-tertiary` | `#0000004D` | Placeholder text — very low contrast, use sparingly |
| `--✦/_text/text-onbrand` | `#FFF` | Text placed on brand-colored or dark backgrounds |
| `--✦/_text/text-brand` | `#007BE5` | Links and brand-tinted inline text |
| `--✦/_text/text-danger` | `#DC3412` | Error messages |
| `--✦/_text/text-warning` | `#B86200` | Warning messages |
| `--✦/_text/text-success` | `#009951` | Success messages |
| `--✦/text/disabled/default` | — | Disabled text |

## Choosing icon colors

Icons follow the same semantic pattern as text. The tokens are:

`--✦/_icon/icon-default`, `icon-secondary`, `icon-tertiary`, `icon-onbrand`, `icon-brand`, `icon-danger`, `icon-warning`, `icon-success`.

Match your icon color to the equivalent text color in most cases.

## Choosing border colors

| Token | Value | When to reach for it |
|---|---|---|
| `--✦/_border/border-default` | `#E6E6E6` | Dividers, input borders, card outlines |
| `--✦/_border/border-strong` | `#2C2C2C` | High-emphasis borders when you need more contrast |
| `--✦/_border/border-selected` | `#0D99FF` | Focused or selected input borders |
| `--✦/_border/border-onbrand-strong` | `#FFF` | Borders on top of brand-colored backgrounds |

## Palette colors (fallback only)

Raw palette colors exist for situations where no semantic token fits. Always prefer the semantic tokens above. If you find yourself reaching for a palette color, pause and check whether a semantic token already covers your use case.

- **Blue:** `--🎨/blue/100` through `--🎨/blue/600`
- **Purple:** `--🎨/purple/100` through `--🎨/purple/900`
- **Violet:** `--🎨/violet/100` through `--🎨/violet/500`
- **Grey:** `--🎨/grey/100` through `--🎨/grey/500`
- **Red:** `--🎨/red/200` through `--🎨/red/400`
- **Persimmon:** `--🎨/persimmon/100` through `--🎨/persimmon/500`
- **Orange:** `--🎨/orange/100`, `--🎨/orange/400`
- **Green:** `--🎨/green/100`, `--🎨/green/500`
- **Pink:** `--🎨/pink/500`

Also available: `--color-1` through `--color-7`, `--white`, `--black`, `--warm-red` (#F24E1E).

## Spacing

All spacing uses `--spacer-*` tokens. Remember: values are unitless, so always multiply by `1px`.

| Token | Effective value |
|---|---|
| `--spacer-0` | 0 |
| `--spacer-1` | 4px |
| `--spacer-2` | 8px |
| `--spacer-2-5` | 12px |
| `--spacer-3` | 16px |
| `--spacer-4` | 24px |
| `--spacer-5` | 32px |
| `--spacer-6` | 40px |

For pixel-precise sizing, `--base/size/*` tokens are available from 2 to 128.

```tsx <div style={{ padding: "calc(var(--spacer-3) * 1px)", gap: "calc(var(--spacer-2) * 1px)" }}>
      ``` ## Border radius | Token | Effective value | When to reach for it
      | |---|---|---| | `--radius-none` | 0 | Sharp corners | | `--radius-small`
      | 2px | Subtle rounding on small elements | | `--radius-medium` | 5px
      | Default for inputs, cards, containers | | `--radius-large` | 13px |
      Prominent rounding for featured elements | | `--radius-full` | 9999px
      | Pill shapes, circular avatars | Legacy tokens (`--borderradius/small`
      = 3, `--borderradius/medium` = 6, `--borderradius/large` = 12, `--borderradius/full`
      = 9999, `--borderradius/default` = 6) are also available but prefer the
      `--radius-*` set. ## Typography Typography classes are the preferred
      way to style text. Each class sets font-family, font-size, font-weight,
      and line-height together, so you get consistent type with a single class
      name. Do not manually set individual font properties when a class exists
      for what you need. ### All typography classes at a glance #### Headings
      and display | Class | Font | Size | Weight | When to use it | |---|---|---|---|---|
      | `.display-display-large` | Whyte | 64px | 700 | Hero headlines, the
      biggest text on the page | | `.display-display-medium` | Whyte | 36px
      | 700 | Major section headlines | | `.display-display-small` | Whyte
      | 22px | 700 | Sub-headlines within sections | | `.heading-display` |
      Whyte | 48px | 500 | Product display text, lighter weight than display
      classes | | `.heading-heading-large` | Inter | 24px | 550 | Page-level
      titles | | `.heading-heading-medium` | Inter | 15px | 550 | Section titles
      within a page | | `.heading-heading-small` | Inter | 13px | 550 | Subsection
      titles, sidebar headings | | `.h1` | Whyte | 32px | 700 | Semantic H1
      elements | | `.h2` | Whyte | 24px | 700 | Semantic H2 elements | | `.h3`
      | Whyte | 20px | 700 | Semantic H3 elements | #### Body text | Class
      | Font | Size | Weight | When to use it | |---|---|---|---|---| | `.body-body-hero`
      | Whyte | 22px | 400 | Hero body text, large introductory paragraphs
      | | `.body-body-large-2` | Whyte | 22px | 400 | Large body text in marketing
      contexts | | `.body-body-medium-2` | Whyte | 18px | 400 | Medium body
      text in marketing contexts | | `.body-body-medium-bold` | Whyte | 18px
      | 700 | Bold callouts in marketing body | | `.body-body-regular` | Whyte
      | 16px | 400 | Standard body text (Whyte) | | `.body-body-regular-bold`
      | Whyte | 16px | 700 | Bold body text (Whyte) | | `.body-body-eyebrow`
      | Whyte | 14px | 500 | Eyebrow/overline text above headings | | `.paragraph`
      | Whyte | 16px | 400 | General paragraph text | | `.body-body-large`
      | Inter | 13px | 450 | UI body text (large) | | `.body-body-large-strong`
      | Inter | 13px | 550 | UI body text (large, bold) | | `.body-body-medium`
      | Inter | 11px | 450 | UI body text (medium) | | `.body-body-medium-strong`
      | Inter | 11px | 550 | UI body text (medium, bold) | | `.body-body-small`
      | Inter | 9px | 450 | Small labels, fine print | | `.body-body-small-strong`
      | Inter | 9px | 550 | Small labels (bold) | | `.title-small` | SF Pro
      Text | 16px | 600 | Small titles in UI contexts | #### Code and monospace
      | Class | Font | Size | When to use it | |---|---|---|---| | `.codeblock`
      | SF Mono | 13px | Multi-line code blocks | | `.mono-mono-large` | Roboto
      Mono | 13px | Inline code in UI (large) | | `.mono-mono-medium` | Roboto
      Mono | 11px | Inline code in UI (medium) | | `.mono-mono-small` | Roboto
      Mono | 9px | Inline code in UI (small) | | `.codeinline-body-large` |
      SF Mono | ~15px | Inline code within large body text | | `.codeinline-body-medium`
      | SF Mono | ~13px | Inline code within medium body text | | `.codeinline-body-small`
      | SF Mono | ~11px | Inline code within small body text | | `.codeinline-caption`
      | SF Mono | ~11px | Code in captions or footnotes | ### Font families
      - **Whyte** is for display and marketing: headings, hero text, paragraphs
      on landing pages - **Inter** is for UI: app headings, body text in product
      interfaces, labels - **SF Mono / Roboto Mono** are for code: blocks,
      inline snippets, technical values ### Font weight tokens If you need
      to override weight independently (rare — prefer the typography classes):
      | Token | Value | |---|---| | `--font/weight/default` | 450 | | `--font/weight/medium`
      | 450 | | `--font/weight/strong` | 550 | | `--base/text/weight/light`
      | 300 | | `--base/text/weight/normal` | 400 | | `--base/text/weight/medium`
      | 500 | | `--base/text/weight/semibold` | 600 | ## Shadows Shadows are
      composed from multiple tokens. Here are the assembled snippets so you
      don't have to figure out the composition yourself. ### Resting shadow
      (small) For cards, inputs, and static elevated elements: ```css box-shadow:
      calc(var(--shadow\/resting\/small\/1\/offsetx) * 1px) calc(var(--shadow\/resting\/small\/1\/offsety)
      * 1px) calc(var(--shadow\/resting\/small\/1\/blur) * 1px) calc(var(--shadow\/resting\/small\/1\/spread)
      * 1px) var(--shadow\/resting\/small\/1\/color), calc(var(--shadow\/resting\/small\/2\/offsetx)
      * 1px) calc(var(--shadow\/resting\/small\/2\/offsety) * 1px) calc(var(--shadow\/resting\/small\/2\/blur)
      * 1px) calc(var(--shadow\/resting\/small\/2\/spread) * 1px) var(--shadow\/resting\/small\/2\/color);
      ``` ### Floating shadows For overlays, dropdowns, and modals. Available
      in sizes: `small`, `medium`, `large`, `xlarge`. Each size has multiple
      layers. Follow the same composition pattern as the resting shadow, substituting
      `floating` for `resting` and the desired size. ## Breakpoints | Token
      | Value | When to reach for it | |---|---|---| | `--breakpoint/xsmall`
      | 320px | Small phones | | `--breakpoint/small` | 544px | Large phones
      | | `--breakpoint/medium` | 768px | Tablets | | `--breakpoint/large`
      | 1012px | Small desktops | | `--breakpoint/xlarge` | 1280px | Standard
      desktops | | `--breakpoint/xxlarge` | 1400px | Large screens | ## What
      not to do These constraints matter as much as the tokens themselves.
      Violating them is a common source of visual bugs. 1. **Do not use brand
      color as a page background.** `--✦/_bg/bg-brand` and `--✦/_text/text-brand`
      are for buttons, links, and small accents. Large brand-colored areas
      overwhelm the interface. 2. **Do not hardcode pixel values when a spacing
      token exists.** Write `calc(var(--spacer-3) * 1px)`, not `16px`. The
      tokens ensure consistency if the scale ever changes. 3. **Do not manually
      set font properties when a typography class covers your need.** If you
      want 13px Inter at weight 550, use `.body-body-large-strong`. Don't write
      `font-size: 13px; font-weight: 550; font-family: Inter`. 4. **Do not
      repurpose status colors.** Danger, warning, and success tokens are reserved
      for their semantic meanings. Don't use `bg-danger` as a decorative red.
      5. **Do not pair dark text with dark backgrounds.** When using `bg-menu`
      or `bg-toolbar`, switch to `text-onbrand` and `icon-onbrand`. 6. **Do
      not use raw palette colors when a semantic token exists.** Semantic tokens
      update correctly across themes. Palette colors don't. 7. **Do not forget
      the `* 1px` multiplication.** This is the single most common mistake
      with this token system. Spacing, radius, shadow offsets, and font sizes
      are all unitless numbers. 8. **Do not skip `border-selected` for focus
      states.** Use `--✦/_border/border-default` for resting borders, and `--✦/_border/border-selected`
      when an input or element receives focus. 9. **Disabled states** have
      their own tokens: `--✦/bg/disabled/default` for backgrounds and `--✦/text/disabled/default`
      for text. Don't approximate disabled styling with opacity hacks.
```

## Update a Make kit

### Edit items in kit

With the Make kit file open, you can click **Edit items in kit** from the file explorer to:

- Update the npm package to a different version
- Configure the kit to use different npm packages or style libraries

![edit-items-in-kit-button.png](https://help.figma.com/hc/article_attachments/39315841951895)

### Publish an update

When changes to a Make kit are republished, files using the Make kit will receive those updates and your teammates receive a notification next time they open the file. This is helpful when, for example, the version of an npm package is updated.

To publish updates to a Make kit:

1. Open the Make kit file and make any edits and changes as needed.
2. Click **Update kit** in the top-right corner.
3. From the modal click **Update kit** and review the kit’s details.
4. Click **Publish**.

![update-make-kit-modal.png](https://help.figma.com/hc/article_attachments/39315655620119)

### Unpublish a Make kit

To unpublish a Make kit:

1. Open the Make kit file and click **Update kit** in the top-right corner.
2. From the modal, click **Unpublish** and follow the prompt.

## Use a Make kit

1. Open a new or existing Make file.
2. From the prompter, and click **Select a Make kit**.
3. Choose from a list of Make kits in the list. You can add more than one kit if desired.

Now, when you prompt Make, it will build out your designs and prototypes using the Make kits you added.

![use-make-kit.png](https://help.figma.com/hc/article_attachments/39315655621911)

## Frequently asked questions

**FAQ: What is the difference between Make kits and Make templates?**

Make kits and Make templates are similar in that they both contain predefined elements that are published and shared with teammates, so they can begin building in Make without having to start from scratch. So, what makes them different?

Make kits are a collection of tools and building blocks that are often used in an earlier phase of the design process. For example, let’s say you are using Make to explore a new doodling experience for an arts and crafts app for kids. Having a ready-to-use Make kit means you already have style context, code context, and guidelines to use without having to add them manually. The kit has already been assembled with the proper context, tested, and vetted so you can focus on building and exploring your idea.

[Make templates](https://help.figma.com/hc/en-us/articles/34716178062871) work great if you want to build off of a specific design, idea, or problem. This could be a user dashboard refresh, a checkout screen that you’re stuck on, or rebranded homepage idea for a website.  Building a template often includes using an existing Make kit. Continuing on the previous example of the new doodling experience, you already started out your explorations using a Make kit, and now you're ready to gather feedback and ideas. You publish what you built so far as a Make template—which will contain the Make kit you used as well as designs and interactions you’ve added—and publish it for your team to use as a jumping off point to begin iterating.

**FAQ: Prior to Make kits, I previously extracted style context from my libraries. Do I need to use Make kits?**

Yes. It's important to know:

- Figma Make files that used extracted style context prior to the release of Make kits will continue to work as expected.
- If you want to use a library in Figma Make that you'd previously extracted, you'll need to add the library to a new Make kit. After you publish the Make kit, Figma Make files will be able to get the library styles from the Make kit.

**FAQ: How do I know what the Make kit is using from my library?**

After you add your library to a Make kit, head to the code view. In the editor, you'll see a folder that corresponds to the name of your library. The folder contains:

- A guidelines folder. You can edit the `guidelines.md` file in this folder and add additional guidelines files.
- A `styles.css` file.

The Make kit also contains a `setup.md` file that instructs Figma Make to use your library styles.

The guidelines folder at the root of your Make kit will also have several files in it. Overall, your Make kit will look something like this:

```
├── guidelines/
│   ├── components/
│   ├── Guidelines.md
│   ├── setup.md
│   ├── styles.md
│   └── tokens.md
│
├── src/
│   ├── app/
│      └── [your application code here]
│   └── [your library folder]
│      ├── guidelines/
│         └── Guidelines.md
│      └── styles.css (your library styles)
│ 
├── package.json
├── ATTRIBUTIONS.md
├── postcss.config.mjs
└── vite.config.ts
```

Keep in mind, the extracted CSS is a simplified version of your full library. It won’t capture every design detail. To ensure consistency and clarity, it's important that you add more context and rules in the `guidelines.md` file.

**FAQ: Will variable syntax from my library be preserved in a Make kit?**

Make kits currently don't support full extraction of design tokens. Instead, it pulls a subset of your variables and uses them to generate a global CSS file with raw values. This means variable syntax won’t be preserved exactly as defined. Rather than a 1:1 mapping, you’ll get a simplified view of your variables reflected in a single `.css` file. This helps ensure that generated code aligns with your foundational styles.

If you have additional rules or parameters for variables—especially those related to states—we recommend documenting them in your `guidelines.md` file to maintain consistency across your system.

**FAQ:** **I updated the design library since I first added it to a Make kit. How do I update my kit?**

1. In the code editor for your Make kit, find the folder for your library.
2. If you’ve previously modified the `guidelines.md` file, copy your changes out of the file.
3. After refreshing, click **Edit items in your kit** at the bottom of the file explorer in the code editor.
4. Find your library and re-add it to the Make kit.
5. Add your guidelines back to the `guidelines.md` file.
6. In the upper-right corner of your Make kit, click **Update kit**.

**FAQ: Do any CSS updates or guidelines within Figma Make affect the Figma Design library?**

No. Any updates to the CSS styles or guidelines only affect the Make kit.

## Additional resources

Ready to continue your Make kit journey? Check out the following resources:

- [Use your design system package in Make kits](https://help.figma.com/hc/en-us/articles/35946832653975)
- [Bring your design system package to a Make kit](https://developers.figma.com/docs/code/bring-your-design-system-package/) (developer documentation)
- [Write design system guidelines for Make kits](https://developers.figma.com/docs/code/write-design-system-guidelines/) (developer documentation)
