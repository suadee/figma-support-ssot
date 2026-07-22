---
기술지원명: FD4B: Add prototype connections
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Add prototype connections
출처링크: https://help.figma.com/hc/en-us/articles/31011968186007-FD4B-Add-prototype-connections
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Connect the project card button to the case study page

Before we add a connection, let’s take a peek at our portfolio design to plan out what we want each interaction to feel like. Which elements would we expect to be able to interact with, and what would it do? If a user clicks the button in a project card, we want them to go to the case study page. Let's add that connection first.

Switch to the **Prototype** tab in the right sidebar. From here, we can access the prototyping features and properties. Now when we select the button, a new option appears on the canvas—a blue circle on its edge. If we hover over it, it changes to a  blue plus that we can use to add a new connection.

![](https://help.figma.com/hc/article_attachments/31726534483607)

To add a connection to the button:

1. Select the button.
2. Hover over the blue circle on the button layer's edge until a  blue plus icon appears.
3. Click and drag from the blue circle towards the **Case study** frame.
4. Figma will snap the connection noodle to the **Case study** frame when you get close enough.
5. Release your cursor to complete the connection.

![An animation demonstrating how to add a prototype connection.](https://help.figma.com/hc/article_attachments/31726507894551)

### Flows and interaction menu

Figma also added a small blue label to our home page frame and named it `Flow 1`. The label is attached to the top-level frame where our prototype flow starts.

![](https://help.figma.com/hc/article_attachments/31726534488727)

An **Interaction** menu also appeared. This is where we can make adjustments to the connection’s properties, like its trigger or animation.

![](https://help.figma.com/hc/article_attachments/31726534490007)

Figma already set some of these properties. The **Trigger** is set to **On click**, the **Action** to **Navigate to**, and the destination to the **Case study** frame. This means that when a user clicks on the project card’s button, they’ll be taken to the case study page.

If you created a connection you no longer need, you can select it and press **Delete** to remove it. Or, click and drag the connection to an empty space on the canvas, and release it.

## Connect the button in the navigation bar

You can also add interactions from the right sidebar. Let’s use that to connect the contact button in the navigation bar.

1. Select the button in the navigation bar.
2. Click the plus  in the **Interactions** section
3. Leave the trigger set to **On click**.
4. Set the action to **Open link**. This will open a web browser to a URL.
5. Enter any url—like `help.figma.com` which links to Figma’s Help Center or use the prefix `mailto:` followed by an email address with no spaces, like `mailto:name@test.com`—this will open the user’s mail app with that address already added to the **To** field.

![](https://help.figma.com/hc/article_attachments/31726534492183)

### Copy and paste prototype connections

This contact button actually exists on both of our pages, and we want both instances of the button to have the same behavior.

To save time, copy the connection to the main component.

1. Select and copy the connection you just created using the shortcut:
   - **Mac:** `Command` `C`
   - **Windows:** `Control` `C`
2. Go to the **Components** page and locate the **Navigation** component.
3. Select the button inside the navigation bar and paste the connection:  
   - **Mac**: `Command` `V`
   - **Windows**: `Control` `V`

With the interaction added to the main component, we won’t need to remember to add it again even if new pages are added to our portfolio.

## About playing prototypes

Now that we've added a few connections, we can test them by previewing our prototype in the prototype viewer.

To play, or present, a flow, open the **Prototype** tab, and click the  **Preview** icon next to the flow’s starting point. You can also find all flows on the page in the right sidebar when you have nothing selected.

![](https://help.figma.com/hc/article_attachments/31726507904023)

For each flow, you can do a few different actions:

- Select  **Select frame** to select the starting frame in the canvas. This will also allow you to view details in **Interaction** section of the sidebar
- Select  **Copy link** to copy link to clipboard
- Select  **Preview** to open the flow in [inline preview](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes)—we'll select this option.

### The inline viewer

When you select  **Preview**, Figma will open the prototype in a floating window, called the **inline preview**. This window view is useful to check your prototype as you work. If you make a change to your design on the canvas, Figma will update the preview automatically.

At the top of the window, you can:

- Use the left and right arrows to navigate back or forward through the prototype.
- Restart the prototype from the last selected frame on the canvas. You can also press `R` to restart.
- Open the [overflow menu](#h_01J0YFD4CF9M4129CEE585BFEW) to choose from different scaling options for your prototype.
- Open the prototype in presentation view in a new tab.
- Click the X to close the inline preview.
- Resize the preview by clicking and dragging the edge of the preview window. Hold `⇧ Shift` to scale it proportionally.

![](https://help.figma.com/hc/article_attachments/31726534494103)

Learn more about [playing prototypes](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes).

### Presentation view

Presentation view is a more immersive experience as it uses your own device screen or monitor to display the prototype, just like a real site. You can also access presentation view by clicking **Present** in the right sidebar.

![](https://help.figma.com/hc/article_attachments/31726507906711)

If you want to view it on a device frame like a phone or tablet instead, choose a device frame from the right sidebar while you have nothing selected. Learn more about [prototype devices](https://help.figma.com/hc/en-us/articles/21158597546391-Set-prototype-device-and-background-settings) or how to [preview a prototype on your own device](https://help.figma.com/hc/en-us/articles/360040321093-View-prototypes-on-a-mobile-device).

And if you ever want to change how your prototype fills the screen, you can press `Z` to cycle through different viewing options. **Fill screen** is handy when you’re designing for a resolution that isn’t the same as the device you’re using. Learn more about [scaling options](https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes#h_01J0YFW3ASF4FVTZ124FH6N2RF).

![](https://help.figma.com/hc/article_attachments/31726507910295)

## Preview your prototype to test the interactions

Now that we've learned about previewing our prototypes in the Figma's prototype viewers, let's test our connections we made earlier:

1. Click  **Preview** to view to open the prototype in the inline viewer.
2. Scroll using the trackpad or mouse wheel to scroll to the project card.
3. Click the button you added the interaction to. The prototype will navigate to the **Case study** page, just like we configured it to.
4. Click the contact button in the header to open the `mailto:` link.
5. Check the box if you see a warning page. The first time you open an external link, Figma will alert you that you’re about to navigate to another website. You can disable future notices to make the experience more immersive.

Our prototype connections are working just like we set them up. Perfect! In the next lesson, we'll learn how to change various scrolling behaviors, like setting layers to stay in a fixed position as we scroll down the page.

## Check your knowledge
