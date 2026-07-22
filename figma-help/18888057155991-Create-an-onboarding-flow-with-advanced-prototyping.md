---
기술지원명: Create an onboarding flow with advanced prototyping
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Create an onboarding flow with advanced prototyping
출처링크: https://help.figma.com/hc/en-us/articles/18888057155991-Create-an-onboarding-flow-with-advanced-prototyping
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Project overview**

- **Product**: Figma Design
- **Topics**: [Variables](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma), [interactive components](https://help.figma.com/hc/en-us/articles/360061175334-Create-interactive-components-with-variants), [prototypes](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma), [conditional logic](https://help.figma.com/hc/en-us/articles/15253220891799-Multiple-actions-and-conditionals), [expressions](https://help.figma.com/hc/en-us/articles/15253194385943-Use-expressions-in-prototypes), [inline preview](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes#Preview_your_prototype)
- **Difficulty**: Advanced
- **Length**: 30 minutes

In this project, we’re going to build a prototype for a podcast app. In the onboarding flow, users select one or more topics of interest. The app then offers a collection of recommended podcasts that align with the user’s selected preferences.

Before continuing, you’ll need to duplicate the [Figma Community file](https://www.figma.com/community/file/1301324459782928636/prototype-with-variables) that contains the pre-built assets needed to complete this tutorial. By the end of the project, your final prototype will look similar to the following:

![An animation demonstrating the final onboarding flow prototype. ](https://help.figma.com/hc/article_attachments/25203831160599)

You can also watch our [video tutorial](https://youtu.be/vGIrfVrw_Ss) to follow along.

We’re using variables, interactive components, and conditional logic to build our prototype.

These advanced features allow us to prototype with less time, reduce memory usage, and minimize maintenance time.

To build this prototype, we’ll do the following:

1. [Create boolean variables for topic buttons](#h_01HEN9J7DEHN26CC3Z4NDQEFRS)
2. [Track the number of topics selected](#h_01HENAPXCY1QS3VMZQBAMBQ1HQ)
3. [Create enable conditions for the continue button](#h_01HENCEBN6S6PSF48YCCW1RXHP)
4. [Create disable conditions for the continue button](#h_01HENFV6MMGBG55GXTSKXKDDV4)
5. [Add a skip button](#h_01HENG8ZW70H6S99H9DGDV22NE)

Let's begin!

## Create boolean variables for topic buttons

[The Community file](https://www.figma.com/community/file/1301324459782928636/prototype-with-variables) contains a few of the key elements needed for our app, including:

- **Get started page**: where users can select one or more topics that interest them
- **Homepage**: which displays related podcast cards based on the users’ selections
- **Loading page**: which displays a loading animation

We also set up some initial prototyping connections. Users can select and unselect the topics on the get started page, and navigate across the pages.

![](https://help.figma.com/hc/article_attachments/25174307468951)

The file also includes a component set named **topic** that represents the topic buttons. The component set includes a **isSelected** variant property, with a false value that represents the unselected state, and a true value that represents the selected state.

![](https://help.figma.com/hc/article_attachments/25174510523415)

The Get started page includes four instances of the false variant that each represent a different topic: Music, Food & drink, Product design, and News.

Our goal is to remember which podcast topics were selected on the Get started page and display relevant podcast recommendations on the Homepage after the user taps Continue. To do this, we’ll use boolean variables.

### Create the boolean variables

Let’s start by creating four boolean variables:

1. With nothing selected, click  **Open variables** in the **Local variables** section of the right sidebar.
2. Click the **+ Create variable** button and select **Boolean**.
3. Rename the variable to “hasMusic”, and set the default value to “False”.
4. Select the “hasMusic” variable and press  `Shift`   `Enter`  to duplicate it.
5. Rename the new variable to “hasFood” and set its value to “False”.
6. Duplicate the variable again until you have four boolean variables named “hasMusic”, “hasFood”, “hasDesign”, and “hasNews”. All of them should have a default value of “False”.

![](https://help.figma.com/hc/article_attachments/25175677186327)

### Assign the boolean variables

Now, let’s close the panel and assign the variables to the topic instances on the get started page.

1. Select the **Music** instance on the Get started page.
2. Click  **Assign variable** and assign the **hasMusic** variable.
3. Repeat the steps and assign the **hasFood** variable to the **Food & drinks** instance, the **hasDesign** variable to the **Product design** instance, and the **hasNews** variable to the **News** instance.

![](https://help.figma.com/hc/article_attachments/25194896002455)

Now that we have assign variables to all the instances, we also need to assign the variables to the podcast cards on the Homepage. This determines which podcast cards will be visible on the Homepage after the user selects their topic.

Think of it like a chain. The instance is linked to the boolean variable. We can then link the boolean variable to other elements in our design.

To apply the boolean variables to the podcast cards:

1. Hold `Shift` and select all the music-related podcast cards on the homepage.
2. From the right sidebar, right-click the  eye in the **Layer** section to open the **Assign variable** panel.
3. Select **hasMusic** variable.
4. Repeat the steps to assign the **hasFood** variable to all the **Food & drinks** podcast cards, the **hasDesign** variable to all the **Product design** podcast cards, and the **hasNews** variable to all the **News** podcast cards.

![](https://help.figma.com/hc/article_attachments/25198892094871)

### Check your work

You’ll notice all the podcast cards are hidden on the homepage. This is because the default value of the variables are set to “False”, which turns the layer visibility of the cards to hidden. Before moving on, let’s check to make sure everything is behaving correctly.

1. Press  `Shift`  `Space`  to open inline preview.
2. Select **Music** and **Product design** on the Get started page.
3. Click **Continue**.

As you can see, only music and product design related cards are populated on the homepage. You should only see music and product design-related cards on the Homepage. If that isn’t the case, go back and make sure your variables are assigned correctly.

![](https://help.figma.com/hc/article_attachments/25198892097687)

## Track the number of topics selected

To prevent users from accessing the Homepage without choosing any topics, we’ll need to make sure that the **Continue** button is only enabled if at least one topic is selected.

We can do that using conditional logic and expressions. Let’s break it down:

- Every time we click on a topic, the number of selected topics will increase by 1
- If the number of selected topics is greater than 0, we will set the button from “disabled” to “enabled”

To achieve this, we will need two variables:

- A number variable, that will represent the number of selected topics
- And a string variable, that will represent the “disabled” or “enabled” state of the **Continue** button

### Create the number variable

Let’s start by creating the number variable. We can do this directly in the **Interaction details** panel.

1. Switch to the **Prototype** tab, and select the false variant in the topic component set.
2. Click the current interaction from the right sidebar to open the interaction details panel.
3. From the **Add Actions** dropdown menu, select **Set variable**.
4. Click the  plus in the pick target variable dropdown menu to open the variables panel.
5. Select **Number** to create a number variable in the same variable collection.
6. Name it `topicsSelected` and set its default value to `0`.
7. Click **Create variable**.

### Assign the number variable to the topic button

Let’s add the newly created variable to our interaction:

1. Select the `topicsSelected` variable from the dropdown menu.
2. Enter `topicsSelected + 1` in the **Value** field.
3. Press `Enter`.

![](https://help.figma.com/hc/article_attachments/25198879042967)

## Create enable conditions for the continue button

The **Set variable** action has been added. Now, we need to think about our conditional. If the `topicsSelected` amount is greater than 0, the **Continue** button’s state should change from “disabled” to “enabled”.

Let’s take a quick look at how our button component is set up. It has a variant property called “state”, with values for a “disabled” and “enabled” state.

We can use a string variable in our conditional statement with the same values.

![](https://help.figma.com/hc/article_attachments/25200717585303)

### Create the string variable

1. With nothing selected on the canvas, click  **Open variables** in the **Local variables** section of the right sidebar.
2. Click **+ Create variable** and select **String**.
3. Rename the new variable to `buttonState`, and set its default value to `disabled`.

### Assign the string variable to the continue button

1. Select the button instance on the get started page.
2. Click  **Assign variable** next to the state variant property in the right sidebar.
3. Select `buttonState` variable.

![](https://help.figma.com/hc/article_attachments/25200747405463)

Notice the button instance has changed from its enabled state to disabled state. That is because we have set the default value of the `buttonState` variable to “disabled”. When we assigned the variable to the button instance, the variant property is linked to the variable’s default value and updated its state to match.

**Note**: Your string variable value needs to match the variant property value for the prototype interactions to work. For example, if your string variable value is set to “clickable” and the button state variant property is set to “enabled”, the variable value will not map to the variant property and an error message will display.

![](https://help.figma.com/hc/article_attachments/25201312991383)

### Add a conditional action to the topic button

Then, let’s add a conditional action to our topic component in order for our prototype to work.

1. Navigate to the **Prototype** tab.
2. Select the “False” variant in the topic component set.
3. Click the prototype connection to open the **Interaction details** panel.
4. From the **Add action** dropdown menu, select **Check if/else**.
5. In the **Condition** field, enter `topicsSelected >  0`.
6. In the **Add action** field, select **Set variable**.
7. Select `buttonState` from the dropdown menu.
8. Type `"enabled"` in the **Value** field.
9. Press `Enter`.

![](https://help.figma.com/hc/article_attachments/25201869253783)

### Check your work

Now that we have everything set up, let’s open inline preview and test it out.

By default, the **Continue** button is disabled until at least one topic is selected.

![](https://help.figma.com/hc/article_attachments/25202271034903)

## Create disable conditions for the continue button

We need to make sure that the **Continue** button reverts back to its disabled state if all topics are deselected. We can do that by adding additional actions to the topic component set.

Just like before, we can do that by adding actions to the topic component set. But this time, we’ll add the actions to the reversed direction.

Let’s break down the interactions we need to add:

- Every time we deselect a topic, the number of selected topics will decrease by 1
- If the number of selected topics is less than 1, we will set the button back to “disabled”

To add the new **Set variable** action to the True variant:

1. Switch to **Prototype** tab.
2. Select the “True” variant in the topic component set.
3. Click the prototype connection to open the interaction details panel.
4. From the **Add actions** dropdown menu, select **Set variable**.
5. Select `topicsSelected` from the pick target variable dropdown menu.
6. Enter `topicsSelected - 1` in the **Value** field.
7. Press `Enter`.

Then, we’ll add a new conditional action to the variant:

1. From the **Add Actions**dropdown menu, select **Check if/else**.
2. Enter `topicsSelected < 1` in the **Value** field.
3. Click to open the **Add action** field and select **Set** **variable**.
4. Select `buttonState` from the dropdown menu.
5. Type `"disabled"` in the **Value** field.
6. Press `Enter` to confirm.

### Check your work

Open the inline preview and test the interaction. When we select a topic, the **Continue** button becomes enabled. When we deselect the topic, the **Continue** button reverts to its disabled state.

![](https://help.figma.com/hc/article_attachments/25202271037335)

## Add a skip button

We can add a **Skip** button to the Get started page so users can opt out of the onboarding process. [The Community file](https://www.figma.com/community/file/1301324459782928636/prototype-with-variables) already includes a **Skip** button design in the **Button** component set, so let’s add the enabled variant to our design.

1. While holding `⌥ Option` (Mac) or `Alt` (Windows), click and drag the “secondary, enabled” button variant to create an instance.
2. Place the instance below the **Continue** button inside the get started page.
3. Hold `Shift` to select both buttons, and press `Shift` `A` to add auto layout.
4. Set vertical gap between items to `16`.
5. Align the new auto layout frame to the center of the Get started page.

![](https://help.figma.com/hc/article_attachments/25202378556567)

### Add a prototype connection

We need to add a prototype connection so that when a user clicks the **Skip** button, they are brought to the Loading page. The Loading page has its own interaction to automatically navigate to the homepage after a delay.

1. Switch to **Prototype** tab.
2. Select the **Skip** button on the get started page.
3. Click the  blue plus sign on the edge of the button, and drag the connection to the loading page. This opens up the **Interaction details** modal.

Because the user is skipping the onboarding step, we’ll need to add an action to the **Skip** button to set the **hasMusic**, **hasFood**, **hasDesign**, and **hasNews** variables to true. This will cause all podcast cards to display on the Homepage if the **Skip** button is tapped.

1. From the **Add Actions** dropdown menu, select **Set variable**.
2. Select **hasMusic** from the **Pick target variable** dropdown menu.
3. Select **True** from the **Write expression** dropdown menu.
4. Repeat the steps to add new set variable actions until you have set **hasFood**, **hasDesign**, and **hasNews** to `true`.

![](https://help.figma.com/hc/article_attachments/25203081403927)

### Check your work

Let’s test it out again in inline preview.

When we select the skip button, all the cards show up on the home screen.

![](https://help.figma.com/hc/article_attachments/25203035629591)

## What's next?

Congratulations! You’ve created a prototype with advanced prototyping features. If you want to challenge yourself a bit more, try creating a prototype where users are only allowed to select two or less options with conditional logic.

![](https://help.figma.com/hc/article_attachments/25203952326423)

If you’re interested to learn how to create the podcast card design or the loading animation, check out the following mini projects:

- [Create a responsive card with auto layout and constraints](https://help.figma.com/hc/en-us/articles/18894664907287)
- [Create a loading animation](https://help.figma.com/hc/en-us/articles/18892560291351)
