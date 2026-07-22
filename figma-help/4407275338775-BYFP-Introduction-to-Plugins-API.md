---
기술지원명: BYFP: Introduction to Plugins & API
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: BYFP: Introduction to Plugins & API
출처링크: https://help.figma.com/hc/en-us/articles/4407275338775-BYFP-Introduction-to-Plugins-API
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note**: This course covers the development process for **classic plugins** only, and will not cover generative plugins. Learn more about the [differences between classic plugins and generative plugins](https://help.figma.com/hc/en-us/articles/41407987481879).

We're exploring other ways of learning and exploring Figma. This article is a written version of our [**Build Your First Plugin: Introduction to Plugins & API**](https://youtu.be/wMpa8GoM0lk) video tutorial!

Hi again! Sophie here from Figma's Product Education team. Welcome back to the **Build your first plugin** course.

In the [previous video](https://help.figma.com/hc/en-us/articles/4407260620823), we saw a range of plugins that you can install from the Figma Community to customize and enhance your Figma experience.

Maybe you already have an idea for a plugin, and you're wondering "how exactly do we build a plugin?" In this series, we are going to take you through the process of building a plugin that creates components for social media posts in a Figma file.

## Using APIs

To begin, we'll use Figma's plugin API to make sure our plugin can communicate with Figma. An API or **Application Programming Interface** allows two applications to talk to each other. Our plugin creates a **request** to Figma, and Figma's API delivers a **response**.

![](https://help.figma.com/hc/article_attachments/6372251636887)

You can think of an API as a waiter at a restaurant. First, it takes an order from the customer, which in this case is our plugin. Then, the "waiter" takes that order to the kitchen and makes sure that the specifications have been met before serving the order to the table.

![](https://help.figma.com/hc/article_attachments/6372251804567)

In order to use Figma's API, we first need to learn how to talk to it. This is done by referencing the [Plugin API documentation](https://www.figma.com/plugin-docs/intro/) on [Figma's developer platform](https://www.figma.com/developers). Here, you'll find tons of information about how plugins work, as well as a reference to all the different components you can interact with using the API. If you're ever wondering, "can I do this with the API?" The docs are a great place to start!

Since the P in API stands for **Programming**, we need to use a programming language to use it. Well, actually a few different languages. But, don't worry! While it's handy to have some basic knowledge of writing code, it's not a requirement. We'll teach you everything you need to know, starting with a mini crash-course on some programming terminology. If you have previous experience writing code, you might want to skip ahead to the [next video](https://help.figma.com/hc/en-us/articles/4407531166743) where we'll talk about environment setup.

## Programming languages

Think of our plugin structure like a house. The programming languages we'll use all work together to specify the way our house looks and how it works.

![](https://help.figma.com/hc/article_attachments/6372282984215)

### TypeScript

First, we'll need to write some [TypeScript](https://www.typescriptlang.org/), a programming language that is built on top of JavaScript. While you can also use JavaScript, Figma recommends writing your plugins with TypeScript. TypeScript helps us write code with fewer bugs, along with the added benefit of inline autocomplete with our preferred editor, Visual Studio Code. Our TypeScript code will make the plugin interactive and contain all of the logic of the plugin.

If TypeScript was an element of a house, it would be the ways in which you interact with the home. These are things like turning on a light, or opening a door.

![](https://help.figma.com/hc/article_attachments/6372246331543)

### HTML

Then we'll use HTML, which stands for HyperText Markup Language. You don't need to know what "hypertext" or "markup" means. Just know that it will define the structure of the plugins interface if you choose to create one. These are the **labels**, **fields**, and **buttons** that the user will see and interact with.

Typing this creates a text input field for our plugin UI that a user can type into:

```
<input type="text">
```

And adding this code above it gives that field a label, so our user knows that this field is for their name:

```
<label type="text">Name</label>
```

Each of these lines between the angled brackets are called tags. Here, we have a label tag, and an input tag.

Back to our house. Here, HTML would be the objects and surfaces that you can interact with. You can think of HTML as the structure of the house. For example, when you turn a light on, HTML is the light switch itself.

![](https://help.figma.com/hc/article_attachments/6372261847447)

Or when you open a door? You guessed it. HTML is what gives us a door to open.

### CSS

Finally, we'll give the plugin some style using CSS. CSS is how we define the look of the interface. We can style anything from the color or size of our label or text input, or the font we want the interface to use. We can even use CSS to change the position of those same elements in the UI.

CSS is usually the final touch to a project. Wouldn't a house be boring without some color? Maybe our door could be cornflower blue, or the roof could be firebrick red.

![](https://help.figma.com/hc/article_attachments/6442738820887)

CSS allows us to customize the way that we present our UI to users.

## The Figma global object

Technically, we could stop after writing only the TypeScript code and not use HTML and CSS to build an interface—not all plugins *need* a user interface. Let's jump into a quick example to show you what we mean.

Almost everything in JavaScript is an object. Much like objects that exist in the real world, JavaScript objects have their own functions and properties. What about something like a car? Can you think of functions and properties associated with this object?

A car could have the properties **make**, **model** and **year**, as well as the function **drive**.

```
let myCar = {
	make,
	model,
	year,
	drive(),
};

myCar.drive();
```

Figma has its own global object. Conveniently enough, this object is also named `figma` and has its own functions and properties that let us interact with the canvas.

Using the Plugin API, we can tell the `figma` object to do many different things.

For example, we can create a rectangle on the canvas by writing this statement:

```
figma.createRectangle();
```

Take a closer look at this line of code from our car example, and compare it to the one for creating a rectangle. What do you notice?

```
myCar.drive();
```

This is called dot notation. The '**dot**' is how we call a **function** that belongs to an **object**.

You may also have noticed the parentheses after the function name. This is where we pass arguments into the function. Whether we pass arguments or not, depends on how the function was defined. We don't need to worry about that right now, so we'll leave them empty.

The semi-colon is how we end a statement in JavaScript. This is one way we can separate the different parts our code.

Most of the time, a basic program runs one statement at a time, in the order that they were written. Think of them as steps in a recipe. A plugin can have any number of statements, so it's a good idea to separate them.

### Write your first statement

If you want to try writing your first statement and running it, you can open Figma's Developer Tools in the desktop app by going to the **Plugins** menu and hovering over **Development**. Click on **Open console,** and in the Console tab type in `figma.createRectangle();` then hit Enter. You'll see that Figma has created a rectangle, just like if we had used the **R** shortcut and clicked on the canvas.

![](https://help.figma.com/hc/article_attachments/6372283196311)

You can also make plugins for FigJam, and can use FigJam only API functions like this to create sticky notes:

```
figma.createSticky();
```

## Preparing for environment setup

Nice! We could wrap this up, call it a day and publish this one-line plugin to the Community. We didn't even need to build a UI! However, we're going to build something a bit more complex than this and see some of the cool things we can do if our plugin did have an interface.

While we were able to test this one line of code in our developer tools, we'll actually need to set up a proper environment to build a plugin that uses all the tools we've just introduced.

There are a few ways to get our environment organized and ready for developing plugins. In this beginner series, we'll keep it simple by following [Figma's Plugin Quickstart Guide](https://www.figma.com/plugin-docs/plugin-quickstart-guide/) and use the structure already built into the sample project.

I'm sure you're excited to start building your very first plugin. Now that we've gone through a brief overview of the process and tools we'll need, head over to the next video and get your environment set up! If you want to get a head start, make sure to [download Visual Studio Code](https://code.visualstudio.com/download), since this is the development environment we'll be working in. See you in the next video!

## Next steps

- Check out [Figma's Plugin Quickstart Guide](https://www.figma.com/plugin-docs/plugin-quickstart-guide/)
- Download [Visual Studio Code](https://code.visualstudio.com/download)

1: Overview  3: Environment setup
