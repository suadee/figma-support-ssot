---
기술지원명: AI workflows collection: Create skills for repeatable processes
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Create skills for repeatable processes
출처링크: https://help.figma.com/hc/en-us/articles/41159668700311-AI-workflows-collection-Create-skills-for-repeatable-processes
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

Rachel is wrapping up Cheddar's new savings dashboard before a brand review. The flow is in good shape, but she wants to catch the details people always comment on later, especially copy that sounds too formal or might rub users the wrong way.

She could ask the agent to "update the copy to follow UX writing best practices," but that usually leads to more generic updates that don't really sound like Cheddar.

What she really needs is the same review pattern her team uses every time: check copy against Cheddar's style guide, and leave specific notes on the frames for what to rewrite or adjust.

Skills let you package a workflow into a reusable set of instructions for an AI agent. Instead of rewriting long prompts and re-explaining conventions, a skill gives an agent a stable process to follow.

Any repeated pattern can be a good candidate for a skill, whether it's a process you regularly follow, the standards you apply in every review, or the details that are easy to forget when you're moving quickly.

Skills are most useful when the work is repetitive—you keep writing the same prompt, checklist, or explanation—or feels like busywork.

**Tip**: Learn more about [creating and managing your own custom skills](https://help.figma.com/hc/en-us/articles/40283639496599) in the agent.

In this article, we'll explore four example areas where skills can help smoothen design workflows in Figma:

- [Encode style and aesthetics](#h_01KVPRJYS60ZZ992A310GA94JA)
- [Transform layouts](#h_01KVPRJYS6GDRE4RC36XPTGF52)
- [Get feedback and critique](#h_01KVPRJYS6A9Y8WJR9VG1QZ0RG)
- [Apply standards and QA](#h_01KVPRJYS6HJRSBYRD7N3C3D4T)

## Encode style and aesthetics

A style skill can capture repeatable style intent when a library isn't available. You can use it to describe practical details about what a visual aesthetic actually means in your work.

If you already have a published library with components, variables, examples, and documentation, use that as the source of truth. A style skill is most useful before a full system exists, or when you're exploring brand expression that isn't captured in components yet.

| Example | What to encode |
| --- | --- |
| Brand guidelines | The specific applications of your brand guidelines: which typeface for which context, how color is used, what spacing to apply. You can point the agent at a reference design to start extracting some of the details. |
| Dashboard style | Your chart preferences, color sequence for data series, and your rules about when to use which chart type. |

**A grab-and-go skill**

![](https://help.figma.com/hc/article_attachments/41391023143319)

An example of a skill that wraps a selected Figma object in a polished 16:9 presentation frame with an AI-generated background. The skill includes six style presets to choose from.

Try the hifi-mockup-presenter skill

```
      ---
name: hifi-mockup-presenter
description: Creates a polished presentation frame around a selected Figma design frame, using AI-generated backgrounds. Choose from different vibes!
---

---
name: hifi-mockup-presenter
description: Creates a polished presentation frame around a selected Figma design frame, using AI-generated backgrounds. Use whenever someone asks to "present a frame", "wrap a design in a background", "make a mockup", "add a background to my frame", or "create a presentation frame". Trigger when words like "hi-fi", "mockup presenter", "presentation frame", or "background aesthetic" appear. Always use this skill when the user wants to showcase a design frame with a generated backdrop.
---

# Hi-Fi Mockup Presenter

Wraps a selected Figma frame in a polished 16:9 presentation frame with an AI-generated background. The source frame is never moved — only cloned and composited on top.

---

## Step 1 — Show the Aesthetic Picker UI

Before doing anything in Figma, present the user with a choice of five background aesthetics. Use the `show_widget` visualizer tool to render a picker with five cards. Wait for the user's selection (they'll reply with their choice) before proceeding.

### The five aesthetics

| ID | Name | Vibe |
|----|------|------|
| `fluid-glass` | **Fluid Glass** | macOS Sequoia, iridescent liquid swoops, film grain |
| `gradient-fog` | **Gradient Fog** | Pure chromatic mist, color bleeding into color, maximally blurred |
| `concentric-bands` | **Concentric Bands** | Layered arc stripes radiating from offscreen, topographic, editorial |
| `clay-forms` | **Clay Forms** | Soft matte 3D blobs, putty-like, SaaS brand art energy |
| `noise-gradient` | **Noise Gradient** | Soft gradient base with heavy uniform grain overlay, Unsplash-textured |

Render this picker as an interactive widget — five cards in a grid, each with a color swatch preview, label, short descriptor, and a "Select" button. On click, call `sendPrompt("Use [aesthetic name] aesthetic")` so the user's reply triggers the next step.

Use the CSS variables and design system from `read_me` for consistent styling. Each swatch should visually hint at the aesthetic:
- Fluid Glass → iridescent smear
- Gradient Fog → soft blur of two colors
- Concentric Bands → concentric arc lines
- Clay Forms → soft rounded blob dissolving into neutral ground
- Noise Gradient → noisy gradient patch

Do not proceed until the user has selected an aesthetic.

---

## Step 2 — Read the Selected Frame

Use the Figma MCP to:

1. Confirm the selected node is a **frame** (not a group, component, etc.). If not, notify the user and stop.
2. Read the frame's **width**, **height**, and **dominant colors** (sample from fills, children, or screenshot analysis).
3. Detect **mode** — dark if the background luminance is below ~30%, light otherwise.

---

## Step 3 — Create the Presentation Frame

Calculate dimensions:
- Padding: 18% of the longer frame dimension
- Presentation frame: 16:9, large enough to contain the source frame + padding on all sides
- Place the new frame **80px to the right** of the source on the canvas

Steps:
1. Create a new frame at 16:9 dimensions
2. Clone the source frame
3. Center the clone within the new presentation frame
4. Apply a **soft drop shadow** to the clone: `y: 8, blur: 24, spread: 0, opacity: 0.25, color: #000`

---

## Step 4 — Generate the Background Image

Use Figma's AI image creation tool with the prompt for the selected aesthetic (see below). Apply the generated image as the background fill of the presentation frame.

### Aesthetic Prompts

#### Fluid Glass (`fluid-glass`)
```
Abstract fluid glass background in the style of macOS Sequoia. Smooth liquid swoops all flowing in the same diagonal direction. Heavily blurred, soft focus throughout — no sharp edges anywhere. Iridescent edges with subtle chromatic aberration. Soft gradient fills in [DOMINANT_COLORS] — deep, saturated, slightly translucent. Subtle film grain and noise texture overlaid across the entire image. No text, no UI, no bokeh. Photorealistic. Widescreen 16:9.
```
- Dark → append: `"Deep rich shadows, midnight tones, jewel-like saturation."`
- Light → append: `"Airy, bright, pearl-white base, soft pastel iridescence."`

---

#### Gradient Fog (`gradient-fog`)
```
Pure abstract chromatic fog background. Absolutely no edges, no shapes, no texture — only soft color dissolving into color. [DOMINANT_COLORS] bleeding into each other across the entire frame with long, imperceptible gradients. Maximum gaussian blur applied to everything. Feels like looking at color through frosted glass from 10 meters away. No grain, no bokeh, no objects. Just atmosphere. Widescreen 16:9.
```
- Dark → append: `"Colors are deep and muted — navy, plum, ash. Very low brightness overall."`
- Light → append: `"Colors are pale and washed — blush, sky, cream. High key, almost white in the center."`

---

#### Noise Gradient (`noise-gradient`)
```
Abstract background with a smooth, wide chromatic gradient as the base — [DOMINANT_COLORS] blending softly from one corner to another. Over the entire surface, a heavy uniform film grain is applied — dense, even, photographic noise that covers every pixel without clumping. The grain and the gradient are equally visible and inseparable. Feels like a high-ISO photo of a colored surface, or a grainy Unsplash texture. No shapes, no bokeh, no blur — only gradient and grain. Widescreen 16:9.
```
- Dark → append: `"Gradient is dark and saturated — deep navy to violet to near-black. Grain reads as bright speckle against dark."`
- Light → append: `"Gradient is bright and open — soft coral to lavender to sky. Grain is subtle and fine, like linen."`

---

## Step 5 — Finalize

- Confirm the presentation frame is placed 80px to the right of the source
- Notify the user with the name of the new frame and which aesthetic was applied
- Do **not** move, modify, or delete the original source frame

---

## Notes

- Frame nodes only — if the selected node is not a frame, notify and stop
- Source frame is never moved, only cloned
- Substitute `[DOMINANT_COLORS]` with a comma-separated list of descriptive color names or hex values (e.g. "deep teal, warm coral, off-white")
- If color detection is unavailable, infer a reasonable palette from the mode (dark/light) and the mode adjustment copy
```

## Transform layouts

A layout transformation skill captures a structural pattern so you can apply it to any content without re-explaining the rules each time.

| Example | What to encode |
| --- | --- |
| Mobile reflow | Your breakpoints, what stacks vs. scrolls vs. hides at each size, and any mobile-specific component swaps your system requires. |
| Pattern application | The exact rules of the pattern: gap size, label placement, cell proportions, how the pattern breaks at different content lengths. |

## Get feedback and critique

A feedback skill encodes your criteria so you get consistent, targeted critique each time. It captures what you and your team care about based on product context, standards, and past design reviews.

| Example | What to encode |
| --- | --- |
| Copy tone | Specific word choices, constructions your product uses or avoids, and examples of good copy. |
| Assess cognitive load | User context, moments where people may feel confused, and lessons from previous experiments or reviews. |
| Research to action | What counts as a blocker vs. a nice-to-have, how findings map to design principles, and what "actionable" means for your product. |

**A grab-and-go skill**

![](https://help.figma.com/hc/article_attachments/41391007138583)

An example of a skill that critiques a design, flow, or product concept in the voice of Yuhki, a product leader at Cheddar with high craft standards and a storytelling-first lens.

Try the critique-like-yuhki skill

```
---
name: critique-like-yuhki
description: Critiques a design, flow, or product concept in the voice of Yuhki (a product leader with high craft standards and a storytelling-first lens). Pushes on the underlying insight, the user problem, simplicity, and whether the value is immediately legible. Use when someone asks to "critique this like Yuhki," "review in Yuhki's voice," "what would Yuhki say," or wants a sharp product-leadership critique before a review.
---

# Critique Like Yuhki

You are reviewing the current design (or the user's selection) in the voice of **Yuhki** — a product leader known for a storytelling-first, craft-obsessed, customer-grounded critique style. Your job is to give the kind of feedback that makes the work meaningfully better, not 10% better.

Be warm and encouraging in tone, but hold a very high bar. Lead with genuine curiosity ("why this?"), get to first principles fast, and never let vagueness slide. You're generous with the *why* behind every note so the designer learns the lens, not just the fix.

## The lens — what Yuhki always pushes on

Work through these, in roughly this order:

1. **What's the insight?**
   - What's the non-obvious idea this design is built on? If you can't name it in one sentence, that's the first problem.
   - Is this solving a *real* user problem, or a self-imposed one? Start from the user, not the UI.

2. **Show, don't tell.**
   - Does the design *demonstrate* its value, or does it rely on labels, copy, and explanation to make its case? The best work is legible at a glance.
   - If someone saw this for three seconds with no context, would they get it?

3. **What's the story?**
   - Can you articulate the narrative this flow tells the user — beginning, middle, end? Where does it lose the thread?
   - Is there a clear emotional arc, or just a sequence of screens?

4. **Simplicity — what can you cut?**
   - What's doing the most work here, and what's just noise? Push to remove, not add.
   - Is this the *simplest* version of the idea, or the first version? Almost always there's a simpler one hiding underneath.

5. **Craft & taste.**
   - Do the details feel considered — spacing, hierarchy, type, motion, copy? Craft is the signal that the team cared.
   - Where does it feel "fine" instead of "great"? Name those spots specifically.

6. **The 10x question.**
   - If we weren't constrained, what would make this *dramatically* better — not incrementally? Push past the obvious.
   - What's the version of this we'd be proud to show on stage?

## How to respond

Don't just list problems. Critique like a thoughtful leader in a review:

**Critique — [what you're reviewing]**

**The big question** — Open with the single most important thing: usually "what's the insight / problem here?" Stated as a real question, warmly.

**What's working** — 1–3 specific things that are genuinely good (be concrete, not flattering).

**Where I'd push** — The substantive notes, each as:
- *[The note]* — and the *why* behind it, tied to one of the lenses above. Be specific about *where* in the design.

**The 10x move** — One bold suggestion for how this could be dramatically better, not just cleaner.

**If I had to pick one thing** — Close by naming the single highest-leverage change to make next.

## Guardrails

- Be direct but never dismissive — the goal is to raise the work *and* the designer.
- Always ground notes in the user and the insight, not personal preference. If something is taste, say so.
- This is an articulated *lens*, not the real person — frame it as "a Yuhki-style critique," and flag when a question genuinely needs the real stakeholder's input rather than guessing their intent.
```

## Apply standards and QA

A standards and QA skill encodes pre-handoff checks, compliance requirements, and team quality criteria so you can catch issues before they create rework.

Use these skills as a first pass. The agent can surface likely issues and suggest fixes, but you still review the output and decide what to change.

| Example | What to encode |
| --- | --- |
| Accessibility pass | Standards that go beyond WCAG, known exceptions, target sizes, contrast expectations, and accepted tradeoffs. |
| Handoff readiness | Naming conventions, annotation standards, developer questions, and what a ‘clean file’ means on your team. |
| Localize | Languages to test, string expansion expectations, language-specific guidance, and acceptable layout adjustments. |

### Before you go: What makes a useful skill?

Creating a skill is deceptively easy: you can just ask an agent to make one for you and hey presto; it’s written and ready to go.

The problem: people often ask AI to write a skill for them, but they don't provide enough detail to make it genuinely useful, or aren't prepared to iterate on it to make it better.

For example, Jenny, a UX writer at Cheddar, could ask the agent to “write a UX writing skill.” It might produce something that sounds solid at first glance: use a friendly tone, keep copy concise, make actions clear, and avoid jargon. Because Jenny’s prompt is generic, the skill is generic too.

In practice, there’s probably much more specific criteria that matters to Jenny and her team. Maybe Cheddar needs extra care around money stress, teen users, privacy, and notification previews. Maybe the team has specific rules for spending alerts, empty states, or savings goals. That’s the kind of context Jenny can add to make the skill genuinely useful.

One giveaway of a skill that's not quite right is when you find yourself editing the output more than if you'd done the work yourself, or just ignoring the output entirely.

That's a sign to take a step back and refine the skill—either by prompting or by hand—to get the result you want.

Take a skim through the skills below. At a high level, can you spot details that might make one skill more useful than the other?

Highly-customized skill based on Cheddar best practices

```
---
name: cheddar-ux-writing-guide
description: UX writing guide for Cheddar, a budgeting app for teenagers learning saving habits, setting goals, and managing money. Use when drafting, reviewing, or answering questions about Cheddar product copy, including onboarding, empty states, spending alerts, weekly insights, savings goals, transaction history, notifications, errors, accessibility notes, and brand/community event copy. Apply Cheddar's supportive, direct, teen-respectful voice and finance-sensitive content patterns.
---

# Cheddar UX writing guide

Use this skill to draft, review, or explain product copy for Cheddar.

Cheddar is a budgeting app that helps teenagers learn saving habits, set goals, understand spending, and manage money. The core product moments include account connection, first budgets, savings goals, weekly insights, spending alerts, transaction history, category breakdowns, savings dashboards, and occasional brand/community experiences such as Cheddar Unlocked.

## How to respond

- **Drafting:** Provide polished copy options that follow this guide. Include brief rationale only when a choice is not obvious.
- **Reviewing:** List only the issues that need attention. For each issue, include the rule name, what is wrong, and a concrete fix.
- **Answering:** Point to the relevant rule names and explain the guidance directly.

Keep the response practical. UX writers do not need throat-clearing.

If the user asks about terminology, component behavior, legal requirements, or product policy that is not covered here, say what is missing and ask for the relevant source of truth instead of inventing rules.

## Brand voice

### Supportive, not parental

Cheddar talks to teens as capable people learning a new life skill. Sound like a clear coach or older peer, not a parent, banker, teacher, or scold.

**Do**
- You are $12 under your food budget this week
- Start with 1 small goal
- Your spending changed this week

**Do not**
- Good job being responsible
- You need to make better choices
- Teens like you should start with a budget

### Calm around money stress

Money can feel personal and stressful. Use neutral language for overspending, missed goals, declined actions, security issues, and account connection problems.

**Do**
- You are $8 over your food budget
- Your account needs attention
- We could not refresh your transactions

**Do not**
- You failed your budget
- You blew past your limit
- Oops, your bank is having a moment

### Progress over perfection

Frame budgeting as practice. Emphasize patterns, next steps, and progress instead of flawless behavior.

**Do**
- You spent less on rides this week
- Try moving $5 to your concert goal
- Set a budget you can adjust later

**Do not**
- Perfect week
- Never go over budget again
- Fix your spending

### Useful before clever

Cheddar can be warm and expressive, especially in brand moments, milestones, and community experiences. Product copy still needs to make the user's money situation clear first.

- Use playful language only when the stakes are low.
- Avoid cheese, cash, or hustle puns in core product flows.
- Do not use jokes in alerts, errors, security, fees, account connection, or overspending moments.

**Do**
- You hit your savings goal
- Cheddar Unlocked is live

**Do not**
- That budget is looking grate
- Time to make cheddar
- Your spending is nacho average problem

## Core writing rules

### Lead with the user outcome

Say what changed, why it matters, and what the user can do next. Do not lead with system mechanics.

**Do**
- You spent $14 less on snacks this week
- Connect your account to see your latest transactions

**Do not**
- Weekly insight generated
- Bank connection required

### Make numbers meaningful

Money copy should help users understand the number, not just see it.

- Pair totals with context: category, timeframe, goal, or budget.
- Use exact amounts when precision helps decision-making.
- Use rounded amounts for summaries if exact cents add noise.
- Show whether a number is good, neutral, or needs attention through text, not color alone.

**Do**
- $32 left for food this week
- You are $8 over your rides budget
- Food made up 42% of your spending

**Do not**
- $32 remaining
- 42%
- Red means over budget

### Give one next step

When a surface asks the user to act, make the next step obvious. Avoid stacking competing CTAs.

**Do**
- Set a food budget
- Move $5 to savings
- Review transactions

**Do not**
- Set a budget, review spending, and create a goal
- Learn more
- Continue

### Respect privacy

Treat financial data as sensitive. Do not reveal more than necessary in notifications, previews, lock-screen surfaces, or shared contexts.

- Use generic previews when the surface may be public.
- Avoid exposing merchant names, exact balances, or sensitive categories outside the app unless the user opted in.
- Avoid copy that assumes the user is alone or safe to discuss money.

**Do**
- New spending insight is ready
- Cheddar needs your attention

**Do not**
- You spent $47 at Burger Palace
- Your balance dropped to $12

### Be specific without overexplaining

Use plain terms teens can understand without talking down to them.

**Do**
- Spending
- Savings goal
- Food budget
- Recurring subscription
- Connected account

**Do not**
- Financial wellness behavior
- Expenditure category
- Monetary allocation
- Fiscal discipline

## Mechanics

### Capitalization

Use sentence case for product copy.

- Capitalize Cheddar and proper nouns.
- Capitalize the first word of every UI string.
- Lowercase feature names unless they are branded event names.
- Use title case only for proper names such as Cheddar Unlocked.

**Do**
- Weekly insights
- Set a savings goal
- Cheddar Unlocked

**Do not**
- Weekly Insights
- Set a Savings Goal
- cheddar unlocked

### Numbers and money

- Use numerals, including 1 through 9.
- Use dollar signs for amounts: $5, $12.50, $1,200.
- Use commas for 1,000 and above.
- Use percentages with the percent sign: 42%.
- Use "under budget" and "over budget" as neutral status language.
- Avoid ordinal suffixes: use Jan 4, not Jan 4th.

**Do**
- Save $10 by Friday
- You are $6 under budget
- Food was 42% of your spending

**Do not**
- Save ten dollars
- You failed by $6
- Food was forty-two percent

### Dates and time

- Use relative time for recent activity: Today, Yesterday, 2 days ago.
- Use concise absolute dates when needed: Jan 4, Feb 12, 2026.
- Do not include weekdays unless scheduling requires it.
- Use AM and PM without periods.

**Do**
- Today
- 2 days ago
- Jan 4
- 9:30 AM

**Do not**
- January 4th
- Monday, Jan 4
- 9:30 a.m.

### Punctuation

- Use the Oxford comma.
- Avoid exclamation points in product UI.
- Use periods in body copy and alerts.
- Omit periods in buttons, tabs, labels, chips, and short headings.
- Use contractions for a natural tone.
- Avoid semicolons.

**Do**
- You are $8 over budget. Try adjusting next week's food budget.
- Couldn't refresh transactions

**Do not**
- You are $8 over budget!
- We were unable to refresh transactions; please try again.

### Pronouns

- Use "you" for the Cheddar user.
- Use singular "they" for unknown or general people.
- Do not call users "kids" in product copy.
- Use "teens" only in external or internal explanatory copy, not as a label inside the app.

**Do**
- Your goal is on track
- Ask them to review the shared goal

**Do not**
- Kids should start here
- He or she can connect their account

### Accessibility

Cheddar's baseline product standards include AA contrast, 44 px touch targets, and no color-only indicators.

For copy:

- Do not rely on color alone to communicate status.
- Pair icons with labels when the meaning is not obvious.
- Keep links and buttons distinct by text, not just position.
- Keep alerts scannable for screen reader users: status first, context second, action third.
- Avoid directional copy such as "tap the green button" unless color is not the only cue.

**Do**
- Over budget
- On track
- Needs review

**Do not**
- Green means good
- Tap the red icon

## Content patterns

### Onboarding

Onboarding should help users get to their first useful money moment quickly.

- Explain why an action matters.
- Ask for 1 action at a time.
- Avoid teaching everything upfront.
- Reassure users when they can change something later.

**Do**
- Connect your account to see where your money goes
- Start with 1 budget. You can adjust it anytime.

**Do not**
- Complete your full financial profile
- Before you begin, learn how budgets, goals, categories, insights, and alerts work

### Empty states

Use empty states to orient the user and point to the first action.

For the post-account-connection, pre-budget state, focus on what to do first and why it matters.

**Do**
- Set your first budget
- Pick 1 category to track this week
- Once you set a budget, Cheddar can show what is left to spend

**Do not**
- Nothing here yet
- Your dashboard is empty
- Add data to continue

### Budget setup

Budget copy should make the commitment feel adjustable and realistic.

- Use concrete category names.
- Clarify timeframe.
- Avoid moral language about spending.
- Do not imply Cheddar can guarantee outcomes.

**Do**
- Set a weekly food budget
- Choose an amount that feels realistic for this week
- You can change this later

**Do not**
- Commit to smarter spending
- Stop overspending on food
- Cheddar will keep you on track

### Savings goals

Savings goals should feel motivating and practical.

- Name the goal when available.
- Show progress toward the goal.
- Suggest small actions.
- Avoid pressure, guilt, or fake urgency.

**Do**
- $15 saved for Concert tickets
- Add $5 to stay on pace
- You reached your goal

**Do not**
- Do not miss your chance
- You are behind again
- Be disciplined and save more

### Weekly insights

Weekly insights should make spending patterns understandable and actionable.

- Lead with the most meaningful change.
- Include timeframe and category.
- Explain what the user can do next.
- Avoid insight copy that sounds like surveillance or judgment.

**Do**
- Food took up more of your budget this week
- You spent $18 less on rides than last week
- Review your top categories

**Do not**
- We noticed everything you bought this week
- Your spending behavior changed significantly
- You are bad at sticking to budgets

### Spending alerts

Spending alerts should be calm, timely, and useful.

- State the status first.
- Include the relevant budget, category, or transaction if the surface is private.
- Offer a next step.
- Avoid panic, shame, jokes, or urgency that is not real.

**Do**
- Food budget is almost used
- You have $6 left for food this week
- Review food transactions

**Do not**
- Warning: You're almost out of money
- Uh oh, food budget busted
- Act now before it's too late

### Transaction history

Transaction copy should be scannable and trustworthy.

- Use recognizable merchant names when available.
- Use category labels users understand.
- Distinguish pending, recurring, and reviewed states.
- Do not over-interpret a transaction without context.

**Do**
- Pending
- Recurring subscription
- Review category
- Food and dining

**Do not**
- Suspicious spending
- Bad purchase
- Lifestyle expense anomaly

### Errors

Errors should say what happened, what it affects, and what to do next.

- Use "couldn't" when the user can retry or fix permissions.
- Use "can't" when the action is not possible.
- Apologize only for significant Cheddar-caused problems.
- Never joke in errors about money, accounts, identity, privacy, or security.

**Do**
- Couldn't refresh transactions. Try again in a few minutes.
- Can't connect this account. Cheddar does not support this bank yet.
- We showed the wrong budget total. We're sorry for the confusion.

**Do not**
- Something went sideways
- Bank drama
- Your payment failed

### Loading states

Loading copy should name the task in progress.

- Use present tense.
- Omit punctuation.
- Avoid jokes and ellipses.

**Do**
- Refreshing transactions
- Loading weekly insights
- Connecting account

**Do not**
- Loading...
- Crunching your cash
- Hang tight while we do money magic

### Buttons and actions

Buttons should be short, specific, and action-led.

- Use 1 to 4 words where possible.
- Prefer the action over a vague destination.
- Use "Back" and "Next" in multistep setup.
- End setup flows with the action taken, such as "Set budget" or "Create goal."
- Avoid "Continue" unless the product pattern requires it.

**Do**
- Set budget
- Create goal
- Review spending
- Connect account

**Do not**
- Continue
- Proceed
- Learn more
- Click here

### Notifications

Notifications should be useful, private, and non-alarming.

- Make the notification worth the interruption.
- Avoid exposing sensitive financial details on lock screens.
- Do not use notifications to shame users into engagement.
- Use exact money details only when the user has opted into detailed previews.

**Do**
- Your weekly insight is ready
- Cheddar needs your attention
- Food budget update

**Do not**
- You overspent again
- $7.42 left until you're broke
- Open Cheddar before you mess up your budget

### Marketing and brand moments

Marketing, event, and community copy can be more expressive than core product UI.

- Keep the brand energetic, modern, and teen-aware.
- Make the offer or event clear before adding personality.
- Use Cheddar Unlocked as a proper noun.
- Avoid slang that tries too hard or will age quickly.
- Keep financial claims and product promises precise.

**Do**
- Cheddar Unlocked is live
- See what is new for your goals, insights, and weekly habits
- Sign up for Cheddar Unlocked

**Do not**
- The ultimate money glow-up
- Get rich with Cheddar
- Welcome to the most epic budgetverse

## Sensitive content

Loop in product, legal, or compliance reviewers for copy involving:

- Bank account connection
- Fees, payments, subscriptions, or money movement
- Security, privacy, visibility, and data retention
- Minors, guardians, consent, or account ownership
- Claims about saving money, financial outcomes, credit, taxes, or investments
- Crisis language, debt, fraud, or account compromise

When in doubt, keep copy factual and avoid promises.

**Do**
- Cheddar uses your connected account to show recent transactions
- This may affect which insights you see

**Do not**
- Cheddar will save you money
- Your data is always completely private
- This guarantees better spending habits

## Review checklist

Before shipping Cheddar copy, check:

- Does it respect teen users as capable people?
- Does it avoid shame, panic, and moral judgment?
- Does it make the money number meaningful?
- Does it provide one clear next step?
- Does it protect privacy on public surfaces?
- Does it avoid jokes in sensitive moments?
- Does it use sentence case, concise punctuation, and plain language?
- Does it communicate status with text, not color alone?
- Does it flag legal or compliance-sensitive claims for review?
```

Generic skill that needs refining to be more useful

```
---
name: cheddar-ux-writing-style
description: UX writing guidance for Cheddar, a fictional budgeting app for teens. Use when drafting or reviewing Cheddar product copy for onboarding, budgets, goals, insights, alerts, errors, notifications, and marketing moments.
---

# Cheddar UX writing style guide

Use this skill to write or review product copy for Cheddar.

Cheddar is a budgeting app for teenagers. It helps people understand their money, create budgets, set goals, and build better financial habits. Cheddar should feel approachable, useful, trustworthy, and modern.

## How to use this skill

When drafting copy:

- Write in Cheddar's voice
- Keep copy short and easy to understand
- Make the next step clear
- Use plain language
- Avoid sounding too formal or too childish

When reviewing copy:

- Look for places where the copy could be clearer
- Make sure the tone feels friendly and supportive
- Check that the user knows what to do next
- Suggest improvements where needed
- Keep feedback practical and concise

## Voice and tone

Cheddar's voice should be:

- Friendly
- Encouraging
- Clear
- Confident
- Helpful
- Youthful but not immature
- Trustworthy

Cheddar should avoid sounding:

- Judgmental
- Scary
- Too serious
- Too silly
- Corporate
- Technical
- Like a parent or teacher

Use a tone that feels calm and helpful. Money can be stressful, so the product should not make users feel bad about their choices. At the same time, Cheddar should help users understand what is happening and take action.

## General writing principles

### Keep it clear

Use simple words and short sentences. Avoid jargon and explain concepts when needed.

### Be supportive

Write in a way that helps users feel capable. Focus on progress, learning, and next steps.

### Stay concise

Most UI copy should be brief. Avoid unnecessary explanations unless the user needs more context.

### Be useful

Copy should help the user understand what happened, what it means, and what to do next.

### Match the moment

Use a lighter tone for positive moments and a calmer tone for serious moments. Do not joke about problems with money, accounts, or security.

## Style rules

### Capitalization

Use sentence case for most product copy. Capitalize Cheddar and proper names.

### Punctuation

Use punctuation sparingly. Avoid too many exclamation points. Buttons and short labels usually do not need periods.

### Numbers

Use numerals for amounts, percentages, and counts. Keep money values easy to scan.

### Dates and times

Use simple date and time formats. Keep them consistent across the product.

### Pronouns

Use "you" and "your" to speak directly to the user. Use inclusive language.

## Product areas

### Onboarding

Onboarding should explain the value of Cheddar and help users get started quickly. Focus on one step at a time and avoid overwhelming people with too much information.

### Account connection

Account connection copy should feel trustworthy. Explain why Cheddar needs access and what the user gets from connecting their account.

### Budgets

Budget copy should help users understand where their money is going and how much they have left. Keep the tone neutral and supportive.

### Savings goals

Savings goal copy should feel motivating. Show progress and encourage users to keep going.

### Weekly insights

Weekly insights should summarize useful patterns in spending. Make the insight easy to understand and help the user decide what to do next.

### Spending alerts

Spending alerts should be clear and calm. Let users know when something needs attention without making it feel like a crisis.

### Transaction history

Transaction copy should be simple and scannable. Make categories, amounts, and statuses easy to understand.

### Errors

Errors should explain the problem and help the user recover. Avoid blame. Keep the message brief and useful.

### Loading states

Loading states should describe what Cheddar is doing. Keep them short.

### Notifications

Notifications should be timely and useful. Avoid sending messages that feel nagging or overly personal.

### Marketing and events

Marketing copy can be more energetic than product copy, but it should still be clear. Make the main message easy to understand.

## Accessibility

Write copy that is easy to scan and understand. Avoid relying only on color or visuals to communicate important information. Make sure actions and status messages are clear.

## Sensitive content

Be careful with copy about money, privacy, security, fees, and account access. Keep claims factual and avoid promising outcomes that Cheddar cannot guarantee.

## Review checklist

Before shipping Cheddar copy, check whether it:

- Sounds like Cheddar
- Is clear and concise
- Feels supportive
- Avoids blame or shame
- Explains the next step
- Uses simple language
- Fits the moment
- Handles money topics carefully
```
