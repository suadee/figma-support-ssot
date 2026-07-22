---
기술지원명: BYFP: Plugin Environment Setup
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: BYFP: Plugin Environment Setup
출처링크: https://help.figma.com/hc/en-us/articles/4407531166743-BYFP-Plugin-Environment-Setup
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note**: This course covers the development process for **classic plugins** only, and will not cover generative plugins. Learn more about the [differences between classic plugins and generative plugins](https://help.figma.com/hc/en-us/articles/41407987481879).

We're exploring other ways of learning and exploring Figma. This article is a written version of our [**Build Your First Plugin: Plugin Environment Setup**](https://youtu.be/p-z566ILvxc) video tutorial!

Hi there! Welcome to part three of the **Build your first plugin** series. In this video, we are going to get our environment set up and ready for us to start building a Figma plugin. If you are entirely new to plugins and would like an overview of basic programming concepts, check out parts one and two before watching the rest of this video.

We'll be following [Figma's Plugin Quickstart Guide](https://www.figma.com/plugin-docs/plugin-quickstart-guide/), so it'll be helpful to have it open as we go through this tutorial. Up next, we're going to install:

- **Visual Studio Code** - the development environment we'll use to build our plugin
- **Node.js** - a way for us to run JavaScript outside of the browser and use tools like npm
- **Typescript** - a programming language built on top of Javascript
- **Figma's Typings file** - provides assistance while using Figma's Plugin API

By the end of the setup guide, we'll have a sample plugin that opens a modal, asks the user for a number, and creates that many rectangles on the canvas.

## Install Visual Studio Code

First, we need to install Visual Studio Code. If you already have it on your computer, you can skip to the next step. Otherwise, pause the video and go to [code.visualstudio.com](http://code.visualstudio.com) to download Visual Studio.

Once your download is complete, let's launch Visual Studio Code and take a look. VS Code may ask you for a few additional setup steps like choosing a theme and browsing language extensions. We don't need to worry about this for now, so you can click on **Get Started** in the top left corner to go to the welcome screen.

![](https://help.figma.com/hc/article_attachments/6443437544087)

On the welcome screen, you'll see a Start menu where we can create a new file, open an existing file or run a specific command. Let's create a new file to get a better look at our editor.

**![](https://help.figma.com/hc/article_attachments/6443466759319)**

VS Code will open a new tab. This is the text editor where we'll do a majority of our work when we start writing code.

To the left, you'll see a sidebar with a few different icons.

Let's click on the first icon - it looks like two pieces of paper on top of each other. This is our **Explorer**. From here we can open code folders and view the structure of those projects.

**![](https://help.figma.com/hc/article_attachments/6443426872727)**

Visual Studio is an **Integrated Development Environment**, meaning it combines several commonly used developer tools into one convenient interface.

Underneath the Explorer are icons for Search, Source Control, Run and Debug, and Extensions. We won't be using these IDE features, but feel free to explore if you want to continue familiarizing yourself with Visual Studio.

## Install Node.js and npm

We're going to download the dependencies needed to build our plugin. A dependency is a library or piece of code needed in order for a different part of the project to work. For example, a car needs four wheels in order to run. Without one of the wheels, our car wouldn't get us anywhere. Or a house of cards. If we take one of the cards away, the whole thing collapses.

![](https://help.figma.com/hc/article_attachments/6443663768983)

One way to manage these dependencies is through the use of a tool called 'npm' or **Node Package Manager.**

Originally, JavaScript was a language designed for web and could *not* run outside of a web browser. Node.js is an environment that allows us to do this.

Npm is the default package manager for Node.js. Npm is both a command-line tool and an online repository of open source Node.js projects. Instead of manually including dependencies into our project, npm makes it easy to install these dependencies using scripts.

![](https://help.figma.com/hc/article_attachments/6443663874327)

For example, a library like TypeScript has *hundreds* of files and dependencies. If we were to include these dependencies manually, it would take us forever and it's likely that we'll make a mistake along the way. Instead, we can use a single npm script to install the entirety of TypeScript which saves us time and leaves less room for error.

In order to use npm, we first need to download Node.js. Go to [nodejs.org](http://nodejs.org) and click on "Downloads."

Choose and download the installer for your operating system. Once the file is downloaded, open it to start the Node.js Setup Wizard.

### Additional step (for Windows)

If you're on Windows, when you get to the part of the Node setup that asks about tools for native modules, check the box to **Automatically install the necessary tools** then hit **Next**. In the following screen, click **Install**. Once the installation is complete, hit **Finish**.

### Verify npm installation

We can verify that node was properly installed by checking it in Visual Studio's built in terminal. A **terminal** is a text-based interface where we can do things like execute programs or type in commands to tell our computer to perform certain actions. Open up a new terminal window by clicking **Terminal** in the top menu and selecting **New Terminal**. Then, type `node` and hit enter. You'll see a line that will tell you which version of Node.js you've installed.

![](https://help.figma.com/hc/article_attachments/6443664047511)

If you are not seeing this message, try restarting Visual Studio and running this command again.

Hit **Ctrl-C** twice to exit Node.

## Install TypeScript

Now that you have Node installed, we have access to npm which allows us to install TypeScript. If you're a Windows user, make sure to start with the additional step below before continuing with the rest of your environment setup.

### Additional step (for Windows)

On Windows, we need this additional setup step:

While in Visual Studio, hit **Ctrl-Shift-P** and in the search bar that pops up, type in "terminal select default profile" then select the matching option.

A new menu pops up listing our options for a default terminal profile. Select **Command Prompt**.

### TypeScript install scripts

To use npm, we'll need to open up a new terminal window.

Find **Terminal** in the top level menu, then select **New Terminal**.

From here, we can install TypeScript using npm by typing this line of code in the command line and hitting **Enter**:

- **Windows**: `npm install -g typescript`
- **Mac**: `sudo npm install -g typescript`

You may be asked for a password once you run this script. Typically, this is the same password you use to log in to your computer. Keep in mind that once you start typing in your password, you may not see anything being typed out. Don't worry, the terminal is still reading your input.

If the installation is successful, you'll see something like this:

![](https://help.figma.com/hc/article_attachments/6443466863511)

### Verify TypeScript installation

To check that everything works, you can run this command to see the version of TypeScript you just installed:

```
tsc
```

![](https://help.figma.com/hc/article_attachments/6443467072919)

## Install the Figma desktop app

Awesome! You're almost ready to start building your first plugin. From here on out, Figma will need to read our code saved as a local file. To do this, we'll need the Figma desktop app which you can download from <https://www.figma.com/downloads/>

Once that's done, [log in to the desktop app](https://help.figma.com/hc/en-us/articles/360041064554-Log-in-or-add-accounts) and create a new design file.

Now, select **Plugins** from the menu, then under **Development** select **New plugin**.

This will bring up the **Create plugin** modal. Since we're building this plugin for Figma only, we'll select Figma Design. Let's name this "my-first-plugin", and hit **Next**.

![](https://help.figma.com/hc/article_attachments/6443467097495)

You'll see three options for creating a new plugin - 'Empty', 'Run once' and 'With UI & browser APIs.' The sample plugin we're using requires an interface, so we'll create it with a UI & browser APIs. Hit **Save as** to save it anywhere on your disk. Moving forward, it might be helpful to create a dedicated folder for your plugins to make them easy to find later.

### Open the code folder

Now that our sample plugin is saved, let's take a look at the underlying code. We can do this by opening up the folder in Visual Studio.

Go to **File** > **Open Folder**, then select the folder you saved when you created a new plugin.

A modal may pop up asking if you trust the authors of the files in this folder. Check the box and click "Yes, I trust the authors" to proceed.

Under Explorer, a new dropdown directory is available under the same name as the folder we opened. If you expand this, you'll notice that a few files already exist in our project.

![](https://help.figma.com/hc/article_attachments/6443467198103)

Take a look at the manifest.json file. A manifest is a JSON file that specifies metadata about our project, like its name and version. In this sample plugin, we have a field in the manifest called `editorType` that is currently set to `figma`. As we mentioned earlier, this plugin is designed for Figma only, and not FigJam.

In the manifest, you'll see a reference to the ui.html file. Let's open it up.

Remember that HTML is responsible for the structure of our interface. This is where we indicate labels, buttons and fields that will be in our UI. Notice that there are already a few things written out for the sample plugin.

Finally, let's open up the code.ts file. You guessed it! This is where our TypeScript will go. This file is going to be responsible for adding logic and functionality to our plugin. You should see some pre-written TypeScript in here for our plugin to create rectangles.

## Install dependencies

**What's changed?** Since we first created the Build Your First Plugin course, we’ve introduced some changes to Figma to make it easier to set up a new plugin. In the video, we previously described how to install the Figma typings file. Now, the Figma typings are automatically included as a dependency when you create a plugin. We’ve updated this section (previously “Install typings”) to reflect the changes.

You might notice that there are a few errors in our code highlighted by Visual Studio.  
To fix this, we need to install [Figma's typings file](https://www.figma.com/plugin-docs/api/typings/) and the [plugin linter](https://www.figma.com/plugin-docs/plugin-quickstart-guide/#plugin-linter) into our project.

Think of the typings file and plugin linter (software that automatically tests your code for issues) as assistants while you use the Figma API. While the API documentation is there for you to reference as you build your plugin, the typings file contains annotations that can assist you while writing code by providing API suggestions and letting you know when you've missed an edge case. The plugin linter uses ESLint with a set of rules for the Plugin API and lets you know if you try to do things like use deprecated API methods.

To install the dependencies, open up a new Terminal and run this script in new plugin directory:

```
npm install
```

When you run `npm install`, npm reads the `package.json` file in your plugin directory and installs the dependencies that are defined there, such as the typings and linter. `package.json` also includes the default configuration for the plugin linter.

If the installation was successful, you'll see something like this:

![](https://help.figma.com/hc/article_attachments/21870998063511)

That should've fixed the errors in our TypeScript file. If we take a look at our Explorer again, you'll see a new directory called 'node\_modules.' This is where the typings library is saved. In the index file are the annotations we mentioned earlier for the Figma Plugin API. Feel free to take a look if you're interested in how the types are defined, but make sure not to change anything here!

## Setup compilation

With our dependencies set up, all that's left for us to do is to make sure that our TypeScript compiles to JavaScript in order for our plugin to run.

You might have noticed in the manifest.json file that the `main` field references a JavaScript file instead of the TypeScript file we looked at earlier.

Since Figma plugins run in the browser, and browsers only support JavaScript, the `main` field in our manifest will *always* point to a JavaScript file. Compilation is the process responsible for making sure that our TypeScript gets turned into usable JavaScript that allows our plugin to run.

![](https://help.figma.com/hc/article_attachments/6443664090263)

Our plugin code will continuously change and evolve as we build it. Having to go through the compilation process every time that we save a new change to our file can become tedious. Instead, we should set up our project to watch for changes in code.ts then automatically compile into code.js by hitting `CtrlShiftB` in Windows, or `CommandShiftB` for Mac then selecting 'tsc:watch-tsconfig.json.'

![](https://help.figma.com/hc/article_attachments/6443693099287)

## Run the sample plugin

Now, we're ready to run the sample plugin! Go back to the design file we created in the Figma desktop app, navigate to **Plugins** and under **Development**, select the name of your sample plugin.

A modal will pop up with an input for the number of rectangles you want to create. For now, we can stick with the default of five rectangles and hit **Create** to run the plugin.

You should see that five orange rectangles have been created in the canvas.

![](https://help.figma.com/hc/article_attachments/6443686390039)

### Make some changes and run the new code

Great! Your environment is setup and ready for building plugins. Let's make a few test changes in code.ts and re-run our plugin.

In code.ts, on line 20 we'll find the code that creates a rectangle.

![](https://help.figma.com/hc/article_attachments/6443423906071)

Let's modify this by replacing `figma.createRectangle()` with `figma.createEllipse()`. Save your changes, then go back to Figma and re-run the plugin. What do you notice? Has anything changed?

Now, on line 22 in code.ts you'll see something that says `rect.fills` with type and color values passed in. Let's change the rgb values to 0, 0 and 0. Don't forget to save your work! How are our shapes different?

As you can see, changing the code in our TypeScript file also changes the way that our plugin behaves. Using the Plugin API, we are able to interact with objects that exist on the canvas, or create new ones entirely!

Congratulations on getting your development environment set up and ready to go!

In the next video, we'll start building our own plugin and learn more about how to use Figma's Plugin API. I can't wait for us to get started! See you there!

2: Introduction to plugins  4: Building your plugin
