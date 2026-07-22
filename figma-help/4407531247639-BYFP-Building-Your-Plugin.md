---
기술지원명: BYFP: Building Your Plugin
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: BYFP: Building Your Plugin
출처링크: https://help.figma.com/hc/en-us/articles/4407531247639-BYFP-Building-Your-Plugin
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note**: This course covers the development process for **classic plugins** only, and will not cover generative plugins. Learn more about the [differences between classic plugins and generative plugins](https://help.figma.com/hc/en-us/articles/41407987481879).

We're exploring other ways of learning and exploring Figma. This article is a written version of our [**Build Your First Plugin: Building Your Plugin**](https://youtu.be/ExwP3Kmh-vI) video tutorial!

Hi again! Sophie here from Figma's Product Education team and in the previous video, we set up our environment and installed the dependencies needed so we can start building our plugin.

By the end of this video we'll have a UI with some input elements and a button for our plugin. Before we do that, we should gather the requirements for our plugin in order to figure out what we need to create.

## Copy the design file

You can get a copy of the design file with pre-made components by searching [**Figma for Beginners**](https://www.figma.com/community/file/915647337333327091) in the Community from the desktop app.

With the Community page open, create your own copy of the file.

![](https://help.figma.com/hc/article_attachments/6444009881623)

If you do this from the web app, be sure to switch back to the desktop app since this is where we'll be doing our plugin development.

## About the plugin

So, what are we building?

We're building a plugin with a user interface that contains a form that a user can fill out.

The plugin will take the user input, create a component instance for a post in our social media app, and populate the component with the information the user entered.

![](https://help.figma.com/hc/article_attachments/6443993549847)

You might be wondering, why are we building *this* plugin? This example will teach us fundamental concepts like how to:

- [Build a UI](https://www.figma.com/plugin-docs/creating-ui/) with the Figma Plugin API
- [Create an instance](https://www.figma.com/plugin-docs/api/ComponentNode/#createinstance) of a variant from a component set
- Take user input to create new components in a Figma file

This beginner series focuses on these important skills. You'll need a good foundation in order to build more complex plugins in the future! Once you have a solid grasp of some basic programming concepts and how the Figma Plugin API works, we'll be able to explore more advanced ways of using the API. This means we can eventually create features that will save us time during the design process!

The assets in the Figma for Beginners design file are similar to what you might find on other social media platforms like Twitter or Instagram. One thing these apps have in common are card components that serve different purposes. You could use the same skills learned in this video to build a plugin that creates cards like:

- Travel website cards with an image, destination name, price and description
- E-commerce shop items with an item name, price, and description
- Or Podcast listings in a music app with a name and number of episodes

![](https://help.figma.com/hc/article_attachments/6443969191831)

These are just a few examples of how you can apply what we're learning in this series. Once you build your first plugin, you might start to think about creating more complex plugins that use third-party APIs.

Third-party APIs are APIs outside of Figma that provide tons of information. There are APIs for almost anything you can think of. When we implement other APIs, we can build plugins that automatically pull data, instead of manually filling in this information. Think of something like a weather app plugin that generates cards with weather information. To do this we'd need to pull data from an external weather API. Weather data is constantly changing and varies day to day, so this saves us the trouble of manually entering all this information.

![](https://help.figma.com/hc/article_attachments/6443993694487)

## Plugin requirements

### UI requirements

Now that you have a better idea of how we can apply the skills from this series, let's get back to building our plugin.

Let’s gather the project requirements before we set out to write any code. This gives us an overall idea of where the project is headed and a way to track our progress as we build each piece.

With the **Figma for Beginners** file open in the desktop app, go to the **Components** page and take a look at the **Cards**.

![](https://help.figma.com/hc/article_attachments/6443993857559)

Here, you'll see a few variants of a Petma post component. Our plugin will be responsible for creating an instance of one of these post components. To do this, we'll need:

- A window with a form for the user to fill out
- A plugin name. We can do this by adding a heading to the form.
- Input fields and labels for Username and Name
- A text area and label for the Description of the post

Remember that an input field is generally a one-line field, so for multiple line entries we want to use text area. We could limit our Petma posts to a specific character count, or have no limit at all. Either way, we want to make sure we use an input type like text area that can handle large text entries.

You'll notice that there are several variants of the post component. We also want to provide our user with ways to:

- Choose between light mode and dark mode
- Specify whether they want no image, a single image or multiple images on their post

These features could be implemented a number of ways - with components like dropdowns, radio buttons or input fields.

![](https://help.figma.com/hc/article_attachments/6444019642391)

[Tom Lowry's lightweight UI library](https://bit.ly/3PkLbWT) provides useful pre-built components we can add to our plugin. For example, the Switch component can be used to toggle between light mode and dark mode, and the Radio buttons would allow a user to select an option for the number of images in a post.

To save us time with creating these components, we are going to include Tom’s UI library in our project later.

Finally, we'll add a button to submit all of the information from the form.

### Functional requirements

Now that we know the requirements for our user interface, let's think about some of the functional requirements of our plugin.

Using the Figma API, we’ll learn how to:

- Open a modal in order to display our user interface.
- Send form information to our plugin logic once the user clicks Submit.
- Find the appropriate component set and its variants from our **Figma for Beginners** file.
- Check which variant of the card component the user has selected based on the form.
- Load the same fonts used in the existing card components.
- Use a method from the Figma API to create a new Post component.
- Overwrite text and use other tools like the `Math.random` function to change the content in a Post component.
- Add the new Post component to the Figma file.
- Tell Figma to zoom in to the newly created Post.

Now that we’ve gathered our requirements... we are *finally* ready to write some code!

## Building the UI

Let's open up the project that we started in the [last video](https://www.youtube.com/watch?v=c6OEXx_cLvM&feature=emb_imp_woyt). The first thing we need to do is delete all code from code.ts and ui.html. We won't be using the sample plugin code since we're building ours from scratch.

Make sure that you add `editorType:figma` to the manifest.json file in order for the plugin to work in the Figma desktop app.

Taking a look at our checklist, we want a modal to pop up when we run our plugin.

![](https://help.figma.com/hc/article_attachments/6443998842903)

In ui.html, let's give our plugin a title. We can use an `<h1>` heading tag for this. This is the message that will display in the modal once it pops up.

The Figma API has a `showUI` function that displays a plugin’s interface. This function creates a modal that contains the html markup we pass into it. For example, `figma.showUI(”<h1>Hello, world!</h1>”)` would result in something like this:

![](https://help.figma.com/hc/article_attachments/6443998907287)

Now, replace that line of code with `figma.showUI(__html__)`. By passing in `__html__` , the modal is able to display the contents of your HTML file.

In your manifest.json file, you’ll see that the 'ui' property is set to 'ui.html.' This is how we specify which file the `__html__` variable is referring to.

### First run of the plugin

So far, we’ve added a heading to our html file, added the showUI function to code.ts and confirmed that our manifest is pointing to the right file. This gives us enough code to run our plugin for the first time.

Remember, we can use the command `Command``Shift``B` then select the ‘watch’ script.

Since the file is now watching for changes, we don’t need to worry about updating the build manually while the project is open in Visual Studio.

Going back to the Figma for Beginners file in the desktop app, we can select our plugin to run it. If the build was successful, you should see a modal pop up with the message we wrote in our html file.

![](https://help.figma.com/hc/article_attachments/6444010523543)

Awesome! Now that you see how changes in our code affect the plugin in the Desktop app, we can continue constructing our UI.

### Create a form

Right now, all our plugin does is display a heading inside of a modal, which isn’t very useful.

We need to add a form that will allow the user to interact with our plugin.

We want the input fields on this form to match the fields on the component we’re making. This includes inputs for Username, Name and the Description of the Post. Finally, we’ll provide a way for them to choose between light mode or dark mode, and to select the number of images in a Post.

Back in ui.html, let’s add a `<div>` tag to create a section for our text inputs.

`<div>` tags are a great way to divide up content in a page. We can use it to group other HTML tags in a way that is easier to visualize. In this div section, we’re going to use the `<input>` tag to create inputs for the username, name and description. Don’t forget to add a corresponding label to each input!

![](https://help.figma.com/hc/article_attachments/6443999063959)

While the input types for username and name are “text”, remember that description will be a “textarea”, because it needs to hold a larger amount of characters. Since we’re still in watch mode in Visual Studio, we should be able to save our file and view the form when we run the plugin again!

We can add some basic styling to make sure that our inputs are being displayed as block elements and not wrapping. To do this, add this block of code to the top of your html file:

```
<style>
    input {
        display: block;
    }
</style>
```

So far, we’ve got our form with a heading, as well as input fields for username and name, and a textarea for description.

![](https://help.figma.com/hc/article_attachments/6444010616599)

Next, we need to decide how we’re going to represent the choice between dark mode and the default styling, which we’ll refer to as light mode. While there are several ways for us to approach this, something that immediately comes to mind is a switch that toggles between the two options.

Creating a custom element like this would require more CSS on our part and additional programming logic that we don’t want to worry about at this point. To make things easier, we are going to use [Thomas Lowry’s Figma Plugin UI Library](https://github.com/thomas-lowry/figma-plugin-ds). By including this in our project, we can access ready to use elements without having to build them from scratch.

To include the UI Library in our plugin project, add the following line of code to the top of ui.html:

```
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/thomas-lowry/figma-plugin-ds/dist/figma-plugin-ds.css">
```

Taking a look at the UI library’s [ReadMe](https://github.com/thomas-lowry/figma-plugin-ds/blob/master/README.md) on GitHub, you’ll see that we need to include specific classes to style our elements.

Let’s add some classes to our inputs and see what happens.

Great! Our input fields should look a bit different than they did before. This is thanks to the CSS already included in the UI Library. With these built-in styles, we can even do things like specify the number of rows that a text area takes up.

Now, we can add the switch that allows our user to turn Dark mode on and off. We can find the code for a [Switch in the README](https://github.com/thomas-lowry/figma-plugin-ds/blob/master/README.md#switch) (feel free to copy the block of code below).

```
<div class="switch">
  <input id="dark-mode-on" class="switch__toggle" type="checkbox">
  <label class="switch__label" for="dark-mode-on">Dark mode</label>
</div>
```

We highly recommend typing out this code yourself while learning how to build plugins, but if you need to reference this code in the future, check out this [link to the GitHub repository](https://github.com/thomas-lowry/figma-plugin-ds/blob/master/README.md).

With the Dark mode switch added, we need to give the user an option between no image, a single image, or a carousel in their post.

Since they will only have to choose one of these options for every post created, radio buttons are a great way to represent this.

![](https://help.figma.com/hc/article_attachments/6444010703127)

We’ll create a div with a class of “radio” to make sure the radio buttons are part of the same group, then we’ll add inputs and labels for each option.

Note that while each radio button has a different id, they all have the class "radio\_\_button" and the name "variantGroup". Make sure that the labels correspond to the correct input by using the input id.

Before running the plugin again, let’s add a Submit button at the end of the form and give it the id attribute ‘submit post’.

```
<div>
    <button class="button button--primary" id="submit-post">Submit</button>
</div>
```

We’ve just completed our last two UI requirements!

Let’s run the plugin!

### Default text values

Awesome! Our form is built out and ready to start taking user input.

Before moving on to the next section, we can add some default values for our text inputs using the value attribute. Now is also a great time for us to make sure that all of our inputs have an id attribute.

Next, we can resize the plugin modal by going to code.ts and adding the Figma resize method. This method takes in numbers to represent the width and height of the modal - let’s try 500 by 500:

`figma.ui.resize(500,500)`

Finally, let’s give our form a bit more style.

```
<style>
    body {
        padding: 2em;
    }
    div {
        margin: 1em;
    }
    input {
        display: block;
    }
</style>
```

[Learn more about styling elements with CSS ->](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmtlUVJnb1V0VXVKS1pZOWpkaHhkMnFOQ2JpUXxBQ3Jtc0tuX3M1VFNIWUdSR0VxWkdleDNiLVBfcXFZSE9VRDNLQTFWQW5LZXlhTjF0V3dfdVZLcTJXMko2cEl2aWNiVmdhOVVtYjhaWGJpSEp5d044RFU2WWNDNFpoSFR3RVVqN0RNM0N5X1UwVzAxbl9QMjFaZw&q=https%3A%2F%2Fbit.ly%2F3N2c8MR&v=K8pRan78B9Q)

## Program Logic

One of our functional requirements is to take form input and send that information to our plugin when the user clicks Submit. How exactly do we do this?

### Event listeners

In JavaScript, there is something called an [event listener](https://www.w3schools.com/js/js_htmldom_eventlistener.asp) that waits for a specific event like a mouse click or key press. The event listener then handles what happens once the event occurs. You’ve likely encountered event listeners on the web. For example, when you press the up or down keys, you can scroll through a web page. Or when you click a button to play a video or sound file - these actions are handled by event listeners.

First, we’ll need to write some code that makes something happen when the user clicks the Submit button. We need to indicate that this event is happening in the **document** where our button exists. Then, we need to select the correct element by targeting its id. This is the element that we’re attaching the event listener to. In this case, that’s our Submit button with the id ‘submit-post.’ Finally, we’ll use the ‘onlick’ method to specify that something should happen once a user clicks on the Submit button. To finish writing this method, we need to add a parentheses and some curly brackets. The curly brackets will contain the logic that runs once the click event happens.

```
document.getElementById('submit-post').onclick = () => {}
```

Let’s go ahead and add this code to our plugin. We can do this by using `<script>` tags at the bottom of ui.html and putting our Javascript code in between them. `<script>` tags allow us to embed JavaScript directly into our HTML file and are typically used to work with dynamic content on a page.

We still haven’t decided what happens when someone clicks the Submit button. For now, let’s add the line:

```
console.log("Building my first plugin!")
```

Save your file and make sure that Visual Studio is watching for changes. If you’re no longer in ‘watch’ mode, just hit `COMMAND``Shift``B` again. Run the plugin, then open the console by hovering over **Development** in the **Plugin** menu, and selecting **Open console**. In the plugin form, click Submit. If we take a look at our console, we should see the message “Building my first plugin!”

Great job!  Our event listener noticed the click on the submit button, then handled it by printing out a message to the console.

Now, how do we send the form information to the rest of the plugin code that will live in our Typescript file? First, we need to pull the values from each form input when the click event happens.

Let’s start by creating a constant called name within our event listener. A constant in JavaScript is a type of variable with a value that can’t be changed once it is assigned. In this constant, we’ll store the current value of the name input by assigning `document.getElementById('name').value`

Why don’t you try doing the same thing with the username and description?

We can check these values by logging each variable to the console. Save your changes and run the plugin. Remember to open your console! Type in some random text for name, username and description then click Submit. Are you able to see the logs for the values you entered?

If not, try double-checking that your syntax is correct by comparing it to what we have below:

![](https://help.figma.com/hc/article_attachments/6444020229655)

For the dark mode switch, since it is a checkbox input type, we need to determine whether or not it is in a checked state. Similar to our text inputs, we’re going to create a constant to store this information. Rather than storing the value of the dark mode element, we’ll use the ‘checked’ method that returns either ‘true’ or ‘false’ depending on whether or not the switch is toggled.

```
const darkModeState = document.getElementById('dark-mode-on').checked;
```

If the variable stores ‘true’ then we know that dark mode is selected and vice versa.

Now, let’s add some value attributes to each one of our radio inputs. We’ll use string values 1, 2, and 3. For radio buttons, we need to use a querySelector to target the group of buttons by their shared name, rather than selecting a single element by its id. Then, we’ll find the checked radio button and grab its value. This will either be 1, 2, or 3 depending on the option that the user submits.

```
const imageVariant = document.querySelector('input[name="variantGroup"]:checked').value;
```

We won’t be diving into query selectors in this series, so if you’d like to learn more, check out [this additional resource](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1Nic3EyU1V4ak9jdzJuRERxLWQzc0JLMGVOZ3xBQ3Jtc0tsQmJDWUtqYXNzeGlrUnB0SWhWTFJObE5mNXF6dk1lbUI1OFlUajk0YjY0QmdBODdXLWw1SERtRkE4RDVzRG00aGpzTlRDLVJNTXZYV0djOFpIODhrdkVUc09kS3l5eFk1WUlPSDA2c25kWEhjcnRkbw&q=https%3A%2F%2Fbit.ly%2F3yjBx0u&v=K8pRan78B9Q).

Write a couple of console logs for the two new variables you’ve created, then run the plugin.

Like our last test, type in some text for name, username and description. Toggle the switch to turn Dark mode on, and select Carousel from the list of options. Submit the form and check the console. After the text inputs for name, username and description, you should see a log that prints ‘true’ and another that prints out ‘3’.

![](https://help.figma.com/hc/article_attachments/6444020291991)

Awesome! We are successfully pulling all the values from our form inputs.

### Post message method

We’ve captured the values from our form fields and logged them in the console. How do we put these values to use in the rest of our plugin? We are going to use the [parent post message method](https://htmldom.dev/communication-between-an-iframe-and-its-parent-window/). This will send over data from the form to our Typescript file. Go ahead and add this line of code to your Javascript in ui.html within the event listener you created.

```
parent.postMessage(message,'*')
```

This will go at the very end of the code in our event listener, right before the closing curly brace.

We’ll replace the message parameter with an object that contains our form variables. Remember that a function parameter acts as a placeholder with a default value of *undefined* until we pass in an argument. In this case, that is the 'pluginMessage' object with the values - name, username, description, darkModeState and imageVariant - which are pulled from the form once it’s submitted.

```
parent.postMessage({ pluginMessage: {name, username, description, darkModeState, imageVariant}}, '*');
```

In code.ts, we can use the Figma API’s on message method:

```
figma.ui.onmessage = pluginMessage => {}
```

This receives the same object that we send over from the postMessage in our event listener. Since pluginMessage is an object, we need to use dot notation to access its different properties. For example, to access the name property, we would write `pluginMessage.name` or to check for the dark mode state we would write `pluginMessage.darkModeState`.

Let’s validate that the pluginMessage from ui.html is successfully received by our Typescript file.

In our on message method, console log all of the variables from the pluginMessage object. Once you’ve done this, go ahead and delete the console logs from your event listener.

![](https://help.figma.com/hc/article_attachments/6444011115031)

Save your changes and re-run the plugin. When you check your console, you should see logs for all of your form variables. These console logs are now coming from your Typescript file! You’ve successfully sent information from the plugin form back into your program logic. Amazing job!

An important thing to keep in mind as you build plugins: we should always close our plugin once it’s done running. To do this, we’ll add the line `figma.closePlugin()` at the end of our on message method.

This method ensures that the plugin UI is closed once we are done using it and that access to the currentPage is disabled. This way, we can avoid getting any unexpected behavior from our plugin.

### Conditional logic

Now that we are returning information from the form, we can use these variables in our plugin logic. For example, if the user selects Dark mode, let’s print out a message that says “Welcome to the dark side.” Otherwise, we’ll print out a message saying “I’m Mr.LightSide”

```
if(pluginMessage.darkModeState === true) {
	console.log("Welcome to the dark side.");
} else {
	console.log("I'm Mr.LightSide");
}
```

This block of code is called a **conditional.** A conditional is a statement that tells our program what action to take depending on whether a condition is true or false. In this case, we are telling our program that IF the darkModeState from the form is set to ‘true’, print out “Welcome to the dark side.” Otherwise, print out the other message.

The else statement in a conditional acts as a default path in case the ‘if’ condition isn’t met. This concept is something that we’ll return to as we develop our plugin.

### Loading all pages

**What’s changed?** In 2024, Figma introduced dynamic page loading for plugins. When this tutorial was created, when a Figma Design was opened, all pages in the file were immediately loaded. This could lead to long load times for very large or complex files. Now, pages in Figma files are loaded only as a user needs them, such as when the user navigates to the page or runs a plugin. Because of that change, plugins now need to take a new step to ensure that the pages they want to work with are loaded.

To get ready for working with components in our file, we need to make sure that our plugin has access to all the pages in the document. This is because we can’t guarantee that the user of our plugin has navigated to every page in the document, and we want to make sure we can get the components we want from anywhere in our file.

To make sure we can find all the components in our document, we first need to load all the pages in the file:

```
await figma.loadAllPagesAsync()
```

When we run this method, all of the pages in the file are loaded and we’re ready to find nodes across the whole document.

**Note:** Normally, plugins should avoid using `figma.loadAllPagesAsync()`. It may take very large or complex files as long as 20 to 30 seconds to load all the data. Instead, plugins should try to focus on the user’s current page, or load individual pages as needed. In the case of this example, because our plugin is designed to search across the entire document, it’s appropriate to load all pages.

If you’re interested in learning more about the changes related to dynamic page loading, we provide an advanced guide for [Migrating Plugins to Dynamically Load Pages →](https://www.figma.com/plugin-docs/migrating-to-dynamic-loading/)

### Working with components

Now that we are successfully using form information in our plugin logic, how do we use information from components that already exist on the canvas?

Once again, we’ll need to reference the Figma Plugin API documentation. In the Figma API, there are different [node types](https://www.figma.com/plugin-docs/api/nodes/) that represent layers on the canvas. Each of these nodes correspond to different Figma objects and layers, and have their own set of properties. For example, we have the **RectangleNode** which is a basic shape node that represents a Rectangle on the canvas. Some of its properties include width, height, and corner radius.

There’s also a TextNode that allows us to reference text components in Figma. In this node we’ll find properties like .**characters** that allow us to read or write the characters within a text component. There are also methods for finding text properties like fontSize, fontName, letterSpacing and more.

Let’s continue exploring nodes. Go back to the Figma for Beginners file and open up the Components page. This group of Post components can be referred to as a **component set**.

![](https://help.figma.com/hc/article_attachments/6444020451479)

You guessed it, there is a matching `COMPONENT_SET` node type that we can use to reference component sets on the canvas.

To get information from this particular component set, there is a **findOne** method that will return a **single** matching node from the canvas. For example, we can write:

```
figma.root.findOne(node => node.type == "COMPONENT_SET" && [node.name](<http://node.name/>) == "post")
```

`figma.root` tells the method *where* to look for the node. Root here refers to the entire Figma document. We want to use this method as opposed to `figma.currentPage` because we want to be able to find this node no matter what page we’re currently on in the document.

Here we are telling the findOne method to locate a node whose **node type** is **component set** and has the **name** “post”. Let’s take this line of code and test it out in the console to see what it returns.

![](https://help.figma.com/hc/article_attachments/6444020637975)

You should see a similar ComponentSetNode returned with an id. Click on the arrow to the left to expand the object. What do you notice? These are all the properties of our selected ComponentSet. Let’s take a look at the name property to make sure that we have the right node.

There it is! This component set is named “post” so we know that our findOne method found the correct node successfully.

Go ahead and explore some of the other properties. What do you see when you expand the **children** property? It looks like this component set has six child components. Where do you think those are coming from? Exactly! Those six components are the six *variants* of our Post component.

![](https://help.figma.com/hc/article_attachments/6444020699543)

Let’s move this line of code over to our Typescript file and store the component set in a variable named ‘postComponentSet’.

![](https://help.figma.com/hc/article_attachments/6444028450711)

We’ll add ‘**as ComponentSetNode’** to the end of this line to make sure that when our TypeScript is compiled, the variable will still be seen as a Component Set, just in case JavaScript interprets it as a different node type.

Test the new variable by logging ‘postComponentSet’. While we’re here, we may as well log some of the component set’s properties like ‘postComponentSet.children’ and ‘[postComponentSet.name](http://postComponentSet.name)’. We’ll re-run the plugin and open up the console. You should see that we’re getting the same object as we were earlier! We can verify this with the type Component Set and the object name, which is “post.”

![](https://help.figma.com/hc/article_attachments/6444020846103)

### Find the default variant

Now, to take this one step further. According to the plugin docs, the [default variant in a component set is the top-left most variant](https://www.figma.com/plugin-docs/api/ComponentSetNode/#defaultvariant). That’s this component here:

![](https://help.figma.com/hc/article_attachments/6443999954327)

Luckily, there’s already a nifty component set property that will return the default variant.

```
figma.root.findOne(node => node.type == "COMPONENT_SET" && node.name == "post").defaultVariant
```

When we test this in our console, we get a Component node. Take a look at the defaultVariant’s name property. What do you notice? This name exactly matches the name of the component on the canvas.

Let’s find this component, and you’ll see that this is in fact the default variant in the top-left position of the component set.

Before we go back to the rest of our code, let’s run one more test in the developer console. Let’s try creating an instance of the default variant. The Component node type has a createInstance method that does exactly this. Add `.createInstance()` to your previous line of code.

```
figma.root.findOne(node => node.type == "COMPONENT_SET" && node.name == "post").defaultVariant.createInstance()
```

We get an InstanceNode object. What just happened? If you don’t see anything, try zooming out. Notice anything different? You should see the default variant that we just created an instance of! Nice!

Now, we can work on moving this into our Typescript file. First, we’ll store the default variant as a separate variable from our component set. Since we’ve already got our component set in a variable, we can simplify this by saying `postComponentSet.defaultVariant`

Don’t forget to add “as ComponentNode” at the end of this line to remind our compiler to read this as a component node.

Finally, create an instance of this default variable using the `createInstance()` method and run the plugin again.

Now, when we submit the form, no matter what the input is, the plugin creates an instance of the defaultVariant.

```
const postComponentSet = figma.root.findOne(node => node.type == "COMPONENT_SET" && node.name == "post")  as ComponentSetNode;
const defaultVariant = postComponentSet.defaultVariant as ComponentNode;
defaultVariant.createInstance();
```

### Using the findOne method

Although we are successfully able to find and create an instance of the defaultVariant, we can’t forget about the others! The great news is we can use the same **findOne** method to select the other variants from the component set!

Create a new variable called ‘defaultDark’ and using findOne, we’ll store the variant with the name “Image none, Dark mode true”, which should be this component here.

![](https://help.figma.com/hc/article_attachments/6444000142615)

Note that the name we put in our findOne method needs to **exactly** match the name of the component on the canvas.

```
const defaultDark = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=none, Dark mode=true") as ComponentNode;
```

Remember the conditional we wrote earlier that checks whether or not the user selected dark mode? Let’s put it to use! Delete the console logs within the if-else blocks and instead, if dark mode is selected, create an instance of the dark mode component by writing `defaultDark.createInstance()`. Otherwise, if dark mode isn’t selected, write `defaultVariant.createInstance()`.

```
const defaultDark = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=none, Dark mode=true") as ComponentNode;

    if (pluginMessage.imageVariant === true) {
      defaultDark.createInstance()
    } else {
      defaultVariant.createInstance()
    }
```

We’ll run the plugin a couple of times to see if our conditional logic is working. Let’s add some text to our inputs, and for this round we won’t select Dark mode. Right now, we can choose any of the image options since we haven’t written code to handle that yet. Once you submit the form, it should still create the defaultVariant from earlier. Then, we’ll fill out the form again, this time **with** Dark mode selected and hit submit. If we wrote our conditional correctly, the plugin should have created a dark mode variant with no image. Awesome job!

### Switch case

Using conditional logic, we told our plugin to create a different component based on user input. How do we implement this same concept to create the rest of the variants in our component set?

In our html, we can see that the way we specify which variant the plugin creates is with the imageVariant variable. This variable checks the value of the radio button that is selected. A returned value of 1 means no image, 2 means a single image, and 3 means the carousel variant. We can check these values in our typescript by logging pluginMessage.imageVariant. Let’s run our plugin a few times and test these different values. You’ll see that the value we get back directly corresponds with the radio button we selected when we submitted our form.

Back to our implementation. We have an additional layer of decision making to consider.

First, we ask the question do we want dark mode? Yes or no? If yes, then which dark mode variant do we want - 1, 2 or 3? If no, then which light mode variant do we want - 1, 2, or 3?

![](https://help.figma.com/hc/article_attachments/6444028750359)

There are a couple of ways we can represent this in our plugin logic. One way is by creating nested if-else statements. For example, if dark mode is true, we can nest if else statements that will then check for the imageVariant.

```
  if(pluginMessage.darkModeState === true) {
	  if(pluginMessage.imageVariant === 1) {
      postTemplate = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=none, Dark mode=true");
    } else if(pluginMessage.imageVariant === 2) {
      postTemplate = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=single, Dark mode=true")
      console.log(postTemplate);
    } else if(pluginMessage.imageVariant === 3) {
      postTemplate = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=carousel, Dark mode=true");
    }
  } else {
   if(pluginMessage.imageVariant === 1) {
      postTemplate = postComponentSet.defaultVariant;
    } else if(pluginMessage.imageVariant === 2) {
      postTemplate = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=single, Dark mode=false");
    } else if(pluginMessage.imageVariant === 3) {
      postTemplate = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=carousel, Dark mode=false");
    }
  }
```

However, as you can see this looks a bit cluttered and we want to make sure our code is as concise and easy to read as possible. A better option would be to use a different conditional logic structure called a **switch** **case.**

A switch case evaluates one expression and decides which case to execute depending on the resulting value. For example, pluginMessage.imageVariant will either evaluate to a value of 1, 2 or 3, so we can write our switch case like this:

```
if(pluginMessage.darkModeState === true){
    switch (pluginMessage.imageVariant) {
      case "2":
        // create instance of dark mode, single image 
        break;
      case "3":
        // create instance of dark mode, carousel 
        break;
      default:
        // create instance of dark mode, no image 
        break;
    }
  }
```

You’ll notice that instead of creating a case “1” for the dark mode variant with no image, we’ve gone ahead and added this variant to the default case. The default case in a switch statement will run if none of the other cases match the evaluated expression. So if the value of imageVariant is not 2 or 3, then run the default case. This is useful in case our plugin somehow receives a value that we aren’t expecting.

It’s also important to note that each case ends with the ‘break’ keyword and a semicolon. When a switch statement finds a matching case, all of the code inside the case will execute up until the break. The break statement is what tells our program to stop.

This is a great time to pause the video and try writing a switch statement on your own! Finish out the conditional logic by creating a switch statement within the else code block to find the light mode variants. For now, don’t worry about creating instances of the variants. You can use comments as placeholders just like we’ve done here. Hit play once you’re ready to continue!

Welcome back! Hopefully you had a chance to write your own switch statement. At this point, you should have some code that looks like this:

```
if(pluginMessage.darkModeState === true){
    switch (pluginMessage.imageVariant) {
      case 2:
        // create instance of dark mode, single image 
        break;
      case 3:
        // create instance of dark mode, carousel 
        break;
      default:
        // create instance of dark mode, no image 
        break;
    }
 } else {
		switch (pluginMessage.imageVariant) {
      case 2:
        // create instance of light mode, single image 
        break;
      case 3:
        // create instance of light mode, carousel 
        break;
      default:
        // create instance of light mode, no image 
        break;
    }
}
```

### Creating variant instances

We’re getting there! Our plugin is really starting to take shape. Our next task is figuring out how to create instances of all these different variants. As of now we are only able to create instances of the default variant and one of the dark mode variants.

One way we can approach this is by creating different variables for all the other variants, like what we’ve done with defaultVariant and defaultDark. Instead, what if we could just have one variable that gets assigned a component depending on which case is met in our switch statement?

To do this, we’ll create a variable outside of our conditional logic called ‘selectedVariant.’

![](https://help.figma.com/hc/article_attachments/6444028937495)

Notice that instead of a constant variable, we are creating a let variable here. Unlike a constant that can’t be changed, a let variable allows us to reassign the value depending on which variant we create an instance of. For example, if the user doesn’t select dark mode and selects the no image option, we would want to create an instance of the default variant. In the case, we’ll assign ‘selectedVariant’ the defaultVariant from the postComponentSet.

```
else...
switch(pluginMessage.imageVariant)
...
default:
  selectedVariant = postComponentSet.defaultVariant;
	break;
```

We can apply the same concept to assign the rest of the variants within our switch statements. Since the other variants are not the default, we can utilize the findOne method similar to the way we used it to find the first dark mode variant. To demonstrate, under the default case for the dark mode path of the conditional, your code might look like this:

```
default:
  selectedVariant = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=none, Dark mode=true");
	break;
```

Again, it’s important to note that the node name matches the name of the component on the canvas exactly.

This is the property that will allow us to differentiate between the variants. You can pause here and complete the rest of the switch case statements. Replace your comments by assigning the correct findOne method to the selectedVariant variable. Press play once you’re ready for the next part.

Once you’re done updating the switch cases, your conditional logic should look like this:

```
if(pluginMessage.darkModeState === true){
        switch (pluginMessage.imageVariant) {
          case "2":
            selectedVariant = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=single, Dark mode=true");
            break;
          case "3":
            selectedVariant = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=carousel, Dark mode=true");
            break;
          default:
            selectedVariant = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=none, Dark mode=true");
            break;
        }
     } else {
        switch (pluginMessage.imageVariant) {
          case "2":
            selectedVariant = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=single, Dark mode=false");
            break;
          case "3":
            selectedVariant = postComponentSet.findOne(node => node.type == "COMPONENT" && node.name == "Image=carousel, Dark mode=false");
            break;
          default:
            selectedVariant = postComponentSet.defaultVariant;
            break;
        }
    }
```

We can go ahead and delete our defaultVariant and defaultDark variables since we don’t need them anymore. Remember to save your work!

Before we run our plugin to test this, we can’t forget to create an instance of the selectedVariant!

```
selectedVariant.createInstance();
```

We’ll do this right after the conditional and before the closePlugin method. Great! Let’s open up our file and test out our changes. Run the plugin a few times and try different combinations of dark mode with the number of images to see if you can get all the Post component variants.

![](https://help.figma.com/hc/article_attachments/6444000813079)

If you’re not able to create the six variants, make sure to check your syntax. Are the names of the nodes matching? Are your switch statements checking for string values rather than numbers? Attention to detail is really important here!

### Update the default text

Spectacular job! If your plugin is working properly, you should be able to create all six Post component variants. However, with the way our plugin is at the moment, no matter what we type in for username, name and description, we are still creating new instances with the component’s original text. We can change this by selecting the TextNodes from the newly created component and overwriting them with the information submitted in the form.

Remember that when we create an instance using the createInstance method, what we are actually doing is creating a **copy** of the selected object.

First, we need a way to reference the new Post component. We can do this by storing the new instance in a variable like this:

`const newPost = postTemplate.createInstance();`

Then, we’ll create variables for name, username and description to store the corresponding TextNodes.

```
const templateName = newPost.findOne(node => node.type == "TEXT" && node.name == "displayName") as TextNode;
const templateUsername = newPost.findOne(node => node.type == "TEXT" && node.name == "@username") as TextNode;
const templateDescription = newPost.findOne(node => node.type == "TEXT" && node.name == "description") as TextNode;
```

Notice that we are looking for these nodes from within the newPost, which stores the new instance that we are going to create. We can find each node by name and by checking that they are of the TextNode type. Before we overwrite the current TextNodes, let’s check that we are in fact returning the right text nodes. We can use the TextNode **characters** property to see the text being stored in each node.

Write a few logs to view the characters in the text variables we just created.

```
console.log(templateName.characters);
console.log(templateUsername.characters);
console.log(templateDescription.characters);
```

Once you’ve written out these logs, run the plugin and take a look at the console.

![](https://help.figma.com/hc/article_attachments/6444000445591)

If you are seeing the default text printed out, it means you were able to find the correct TextNodes. Great job!

Now comes the fun part! We can also use the **characters** property to replace the characters in our text nodes with the values submitted from the form.

```
templateName.characters = pluginMessage.name;
templateUsername.characters = pluginMessage.username;
templateDescription.characters = pluginMessage.description;
```

Remember that those values are sent to our Typescript file from the pluginMessage object and we can access them using dot notation.

### Loading fonts

With the characters reassigned, ideally we should be overwriting the text nodes. However, when we run the plugin, you’ll likely encounter a Plugin Error that looks like this:

![](https://help.figma.com/hc/article_attachments/6444045692567)

This is telling us that we can’t overwrite the TextNode due to an unloaded font. Don’t worry! We can fix it. It’s important to know that anytime we are changing the contents of a TextNode, we first need to load the font that the text node is using.

It looks like the font used in our Post component is Rubik, Regular. We’ll load this font in at the top of our onMessage method by using the Figma loadFontAsync function.

```
await figma.loadFontAsync({ family: "Rubik", style: "Regular" });
```

Notice the ‘await’ keyword at the beginning of this line. That’s because this function is asynchronous and returns something called a ‘Promise’. Since the loadFont function only works to load fonts *already accessible in the Figma editor,* the ‘Promise’ will either resolve, meaning the font was found and loaded successfully, or reject and give us an error.

We won’t be diving into asynchronous methods or Promises in this course, so check out the link in the description below if you want to learn more!

Once we’ve done that, we’ll have to do a small refactor of our code and test it again.

```
figma.ui.onmessage = async(pluginMessage) => {
```

All we’ve done is add the **async** keyword and put the pluginMessage parameter in parentheses.

Once you’re done adding these changes, run the plugin again. If it’s successful, you should see the text in the new component being overwritten with your form inputs. Wonderful! Take a moment to give yourself a huuuuuge pat on the back because you’ve just built your **very first** Figma plugin!

### Next steps

You can continue working on this plugin and even implement additional features! For example, we can add some random number generators to randomize the number of likes and comments when we generate a new Post. We can overwrite these text nodes by first locating the node with the **findOne** method, then assigning the random number function to change the TextNode’s characters.

```
const numLikes = newPost.findOne(node => node.name === "likesLabel" && node.type === "TEXT") as TextNode;
const numComments = newPost.findOne(node => node.name === "commentsLabel" && node.type === "TEXT") as TextNode;
...
numLikes.characters = (Math.floor(Math.random() * 1000) + 1).toString();
numComments.characters = (Math.floor(Math.random() * 1000) + 1).toString();
```

In this example, every time we run the plugin, our code will generate a random number from 1 - 1000 and assign it to the number of likes and comments in a Post component.

We could also make it easier to view our new Post by writing in some code that tells the editor to focus on the new component once it’s created. There’s a **scrollAndZoomIntoView** method which automatically adjusts the viewport to focus on the selected nodes.

```
figma.viewport.scrollAndZoomIntoView();
```

To have this method focus on our new Post component node, we need to add this line right after we load our font:

```
const nodes: SceneNode[] = [];
```

We just created a variable called ‘nodes’ that is currently an empty array. An **array** is typically used to store multiple elements. However, in this case we are just adding the new Post to the array since the scroll and zoom into view method is expecting an array to be passed in.

Although we won’t be diving into Arrays in this course, remember to check out the description below to learn more!

Animation here would be really helpful to explain the concept of an array and that we need to add our Post to it since the method is expecting an array type passed in.

We can add our new Post to the list of nodes using the **push** method:

```
nodes.push(newPost)
```

This line should be added at the bottom of our code, right before the close plugin method. Remember that newPost is the name we’ve given the variable that stores the new instance of our selectedVariant.

```
let newPost = selectedVariant.createInstance();
```

After the newPost is added into the nodes variable, we can tell the scrollAndZoom method to focus on that component by passing in ‘nodes’.

```
figma.viewport.scrollAndZoomIntoView(nodes);
```

Run the plugin again, and you’ll notice that it’s so much easier to find our new Post component now!

These are just a few ideas you can implement, so have fun and get creative!

Once again, congratulations on building your very first Figma plugin!

I hope that learning these fundamentals helped you on your journey to becoming a plugin developer! Keep on learning and we can’t wait to see all of the cool things you come up with. In the next video, we’ll show you how to publish your plugins to the community so you can share what you’ve created. See you there!

[3: Environment setup](https://help.figma.com/hc/en-us/articles/4407531166743) [5: Publish to the Community](https://help.figma.com/hc/en-us/articles/4407531267607)
