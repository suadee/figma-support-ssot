---
기술지원명: FD4B: Set page scrolling behavior and customize animations
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: FD4B: Set page scrolling behavior and customize animations
출처링크: https://help.figma.com/hc/en-us/articles/31012379669783-FD4B-Set-page-scrolling-behavior-and-customize-animations
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

## Scrolling and position behavior

The pages we designed are pretty long—a lot longer than your average device screen is tall. Figma Design assumes that we want to scroll the page vertically. But when we scroll, all content on the page scrolls together. Figma takes the entire frame and treats it as one big chunk of content.

We want the nav bar to be visible at all times, even when scrolled all the way to the bottom of the page. We can use the sticky scroll position to do this.

### Change the navigation bar's scroll position

1. Select the navigation bar instance in the **Home** frame.
2. In the **Prototype** tab, select **Sticky** from the **Position** menu.

Objects with their position set to **Sticky** will "stick" themselves to the top edge of their scrolling container. In this case, the scrolling container is our whole page. Be sure to also select the navigation bar in the **Case study** frame and change its position to **Sticky** as well.

![](https://help.figma.com/hc/article_attachments/31742507947287)

### Adjust the canvas stacking order

If your page content is scrolling *over* the navigation bar, you may need to adjust the **Canvas stacking** property. Canvas stacking determines whether the top-most or bottom-most layer in the auto layout frame appears visually on top.

This is particularly handy is when using negative gaps between items. You may see this in components like a face pile, with overlapping photos—and you may prefer one stacking order to another.

By default, layers in an auto layout frame are ordered Last on top. Open the **Auto layout settings**, and make sure Canvas stacking is set to First on top. This makes it so the **Navigation** frame, which is the top-most layer in the Layers section, now appears above all other layers.

![](https://help.figma.com/hc/article_attachments/31742570707863)

### Preview the change

Changing the scroll behavior was a quick change, so we can preview it right away and see if it's the behavior we were looking for. Now, when we scroll, the nav stays stuck at the top. Great!

![](https://help.figma.com/hc/article_attachments/31742507948567)

Tip: It's often a good idea to frequently check your prototype as you go. When you make changes to the prototype's behavior, you can check to see if you got the desired result so you can continue to fine tune it. If you move on to something else and wait to long, you may forget to go back.

## Create a secondary button

Our case study page is quite long. Wouldn’t it be a nice experience if a reader could jump back to the top of the page after they reach the bottom? Let's design a floating button for this.

We could create an instance of the button component we made in an earlier lesson, but then our new button will have the same visual weight as the other buttons on this page. Let's make some minor adjustments to the button's design so it feels more like a secondary button.

We'll use our button main component as a starting point, so we don’t need to start from scratch.

1. Locate the **Button** main component on the **Components** page.
2. Duplicate the Button component to create an instance.
3. Right-click on the instance and select **Detatch instance**. This will permanently break the connection to the main component.
4. Press `Shift` `X` to swap the button's fill and stroke so that it has a lighter visual weight.
5. Change the text's fill color to black so it matches the outline.
6. Select the new button's frame and give it a new fill color so that it matches the page's background color: `#FFFDF8`.
7. Give the button a short and descriptive label like “Back to top”. For a more minimal approach, type two carets `^``^` and a space `⎵` which Figma will convert to an up arrow symbol ↑.
8. Turn the new button into component and rename it to `Button/secondary` to distinguish it from our other, primary button.
9. While we’re here, let’s rename the original button to `Button/primary`.

![](https://help.figma.com/hc/article_attachments/31742507950359)

### Add an instance of the secondary button

Let’s go back to our portfolio design and add an instance of this new button to the **Case study** page. Figma will automatically add the button to the auto layout flow.

![](https://help.figma.com/hc/article_attachments/31742570711959)

By default, objects in an auto layout frame can’t be positioned freely, but we can use  **Ignore auto layout** exclude our button from the auto layout flow. This allows us to ignore the rules set by auto layout, so we can position the object precisely within the frame without taking it out of the frame. Learn more about [ignore auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties#h_01G2RPRBBKVKXK0JV59NCSKEE0).

1. Select the secondary button instance you just added.
2. Click **Ignore auto layout** in the **Position** section of the right sidebar.
3. Drag the button to a location that you like. We'll place ours in an empty space in the footer.

![](https://help.figma.com/hc/article_attachments/31673914460439)

In the **Prototype** tab, change the button's position to **Fixed**. When a layer’s position is set to **Fixed**, Figma Design will move it to a new section of the layers panel, above other layers that scroll.

![](https://help.figma.com/hc/article_attachments/31742507952663)

Our new button looks great on the canvas but if you preview the page, you’ll notice that the button isn’t there. Not even when we scroll all the way to the bottom. This is due to the layer’s constraints.

### Constraints for fixed layers

Earlier, we explained that the default scrolling behavior takes the entire frame—or page—and treats it as one large piece of content.

Our button is positioned far away from the top of the frame and doesn’t scroll with the screen, since it’s **Fixed** in place. So, it’s in your prototype, but it’s just really, really far down. We can’t see it there!

We could move the button higher in the frame, so it’s within the device display. But that doesn’t work well with screen sizes that have different heights.

Instead, we can fix this with [constraints](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize). When you use constraints on objects with **Fixed** positions, you are telling Figma Design how you want to position the object relative to the sides of the viewer window.

We’ve positioned our button near the bottom and right edges of our frame, so let’s change the button’s constraints to **Bottom** and **Right**. Figma Design will display the button in a fixed position with offsets relative to those edges.

![](https://help.figma.com/hc/article_attachments/31673914466455)

Back in the inline viewer, we can see the button appears in the bottom right corner, and stays fixed as we scroll the page, or if we resize the window.

Now it’s time to add the functionality for this button to scroll to the top of the page.

## Add scroll to behavior

**Scroll to** is an action that tells Figma Design to move the user to an object within the same frame. We'll use this action to make it so that clicking on the button scrolls the user back to the top of the page. There are a couple of different ways to add this interaction, so we'll walk through two different methods together:

### Method 1

1. Select the button you just added.
2. From the **Prototype** tab, add a new interaction.
3. Change the **Action** to **Scroll to**, and keep the **Trigger** as **On click**.
4. Choose **Navigation** from the **Destination** menu, since we want this button to take a user all the way to the top and the Navigation component is at the top of the page

By default, the **Animation** is set to **Instant**. If you preview this in the inline view, you'll notice that this doesn't feel like a scrolling experience. If you blink, you'd miss it.

We can improve this experience by changing the animation:

1. Select **Animate** from the **Animation**menu.
2. Set the **Curve** to **Ease out**.
3. Set the **Duration** to `400` milliseconds. This is how long the animation takes to complete. If you hover your cursor over the preview, you'll see an example of what the animation will look like.

![](https://help.figma.com/hc/article_attachments/31744407691031)

### Method 2: Select matching layers on the canvas

We can also create **Scroll to** actions directly on the canvas. Let’s do that with the “Case studies” text link in our page navigation. When a user clicks this link from the home page, we want for them to scroll down to the list of case study cards.

This link also exists on the case study page, and if a user clicks the link from that page, we want them to be sent to the same place.

We can create both of these connections at once:

1. Switch to the **Design** tab in the right sidebar.
2. Select the "Case studies" text layer in one of the nav bars, and then choose **Select matching layers** in the sidebar, or use the keyboard shortcut:  
   - **Mac**: `Command` `Option` `A`
   - **Windows**: `Ctrl` `Alt` `A`
3. Figma Design will recognize that these are the same layers but on different frames, and add the other one to the current selection.
4. Open the **Prototype** tab and click the plus symbol on the canvas.
5. Click and drag a connection from one of the links to the section title frame on the home page. Figma Design will create both connections at once.

![](https://help.figma.com/hc/article_attachments/31753662740631)

#### **Mixed states**

Since we still have both of the connections selected, some of the values will show a **mixed** state. You can deselect the connections, and click on each, one at a time, to see their properties. We can see that the home page was set to **Scroll to** and copied the same animation properties we just set on our last scroll to interaction. While the other connection was set to **Instant**, like our other **Navigate to** connections.

## Consider adding additional interactions

Here are a few additional interactions you may want to add to your prototype to help it feel like a real website:

- Turn the wordmark in the nav bar into a quick way to return to the home page
- Give readers an additional way to reach your case studies, such as clicking on a card's image. You'll commonly see interactions like this on e-commerce websites where clicking the product image will take you to the product's details page.
- Add interactions to the email address and wordmark in the footer
- Try creating an additional case study page from scratch and hook them up to the prototype using what we learned

## Lesson wrap up

Congrats on making your very first prototype! We covered a lot in this lesson, including:

- Key prototyping terms
- How to add connections that navigate between frames
- How to preview our prototype using the inline viewer
- and how scrolling, fixed position, and constraints work

We also discovered a need for a secondary button, thus improving our portfolio's user experience. As you continue to explore different interaction types, you'll discover more techniques for customizing and improving your portfolio.
