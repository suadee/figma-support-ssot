---
기술지원명: BYFP: Publishing to the Community
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: BYFP: Publishing to the Community
출처링크: https://help.figma.com/hc/en-us/articles/4407531267607-BYFP-Publishing-to-the-Community
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note**: This course covers the development process for **classic plugins** only, and will not cover generative plugins. Learn more about the [differences between classic plugins and generative plugins](https://help.figma.com/hc/en-us/articles/41407987481879).

We're exploring other ways of learning and exploring Figma. This article is a written version of our [**Build Your First Plugin: Publishing to the Community**](https://youtu.be/ZpJ_z1WNRgA) video tutorial!

Welcome to part five of the Build Your First Plugin series! In this video, we’re going to show you how to publish your own plugins to the Figma Community. The Figma Community is home to thousands of templates, widgets, and plugins built by other Figma users. We’ll learn how to add our work to the Community so that others can find and install our plugin!

If you’ve been following along on our video series, you should already have a plugin ready to publish! If not, check out [videos one through four](https://www.youtube.com/playlist?list=PLXDU_eVOJTx5YBAszyuOTyxlgIxkQVyii) to learn how you can build your very first Figma plugin.

To publish a plugin to the Community, we’ll need to use the Figma desktop app. Let’s open up the desktop app, and navigate to the left sidebar. Click on **Explore community**. This will open up the Figma Community page in the desktop app.

In the top-right of the Community page, click on the blue **Publish** button and a modal will pop up displaying your Figma files. In the top-left of this modal, navigate to **Plugins** to view a list of plugin projects that are available for publishing.

![](https://help.figma.com/hc/article_attachments/6446266944023)

We’ll select the plugin we built in the previous video, hit **Next** and the **Publish plugin** modal will pop up.

Every plugin has its own page in the Figma Community. This allows other members of the Community to find and install a plugin, and learn more about what each plugin does. In the **Publish plugin** modal, we can provide the information we want to display on our plugin page. We recommend having this information ready before starting the publishing process.

Let’s add an icon to represent our plugin in the Community and in the Editor when a user runs our plugin. Although I already have an icon ready to use here, this is something you can create yourself! Just make sure to follow the recommended dimensions outlined in the **Publish plugin** modal. Luckily, Figma makes this easy by having frame presets available for plugin publishing. To use the plugin frame presets, open a design file, select the Frame tool, then click on the Prototype tab in the right sidebar. Under the Figma Community dropdown, you should see presets available for creating a plugin icon, a profile banner and a plugin cover. Nice!

![](https://help.figma.com/hc/article_attachments/6446285232407)

Next, we’ll give our plugin a name. This can be as descriptive or creative as you want! Users will be able to search for your plugin using this name.

Then, we’ll write a description of our plugin. This is where we can explain what our plugin does and how to use it.

We can also add some cover art to display at the top of our plugin page. Again, make sure to follow the recommended dimensions outlined in the modal so that your image looks its best!

**Let’s not forget to add relevant tags to the plugin.** We can have up to twelve keywords and these can be anything that would make it easier for other Community members to find our plugin.

![](https://help.figma.com/hc/article_attachments/6446273223959)

It’s important to note that as a plugin creator, it’s your responsibility to provide support for your plugins. Under **support contact**, we should provide an email address, website or help center link, just in case users have any questions about the plugin.

You’ll see that the **publish plugin** modal has automatically assigned you as the plugin Creator. If anyone else assisted in the building of this plugin, you can credit them here by entering their Figma Community handle.

Under **Plugin info**, you may get an error that says “Invalid ID in manifest.json.”

![](https://help.figma.com/hc/article_attachments/6446273235607)

To fix this issue, click on the “Generate ID” button to the right. You should now see a message that says “Please add this to your manifest.json file” with an id property and value underneath it.

![](https://help.figma.com/hc/article_attachments/6446428512407)

First, we’ll copy this newly generated id, then open up the plugin project in Visual Studio Code. In the manifest.json file, replace the current id property and value with the new id you generated in the modal.

![](https://help.figma.com/hc/article_attachments/6446444132631)

Save this change, then hit Command Shift B to watch for changes. If we made the change correctly, our project should compile successfully with no errors. Great!

Let’s head back to the **publish plugin** modal in our desktop app. By default, comments are allowed on the plugin page since they are a way for other Community members to provide feedback and make feature requests. However, if you’d like to turn this off, you can uncheck the box in the **Comments** section here.

Finally, let’s scroll back up to the top of this modal to see a preview of our plugin. This is a great time to check for typos and verify the information we filled in.

![](https://help.figma.com/hc/article_attachments/6446455885335)

If you like what you see, go ahead and hit **Publish** at the bottom of the modal.

Congratulations! You’ve submitted your first Figma plugin for review! Figma will contact you through your Figma account email to let you know if your plugin has been approved.

![](https://help.figma.com/hc/article_attachments/6446429166999)

Learn more about [publishing plugins and the review process](https://help.figma.com/hc/en-us/articles/360039958914-Plugin-and-widget-review-guidelines).

Thank you so much for following along in the Build Your First Plugin series. We hope that you had fun learning with us and we can’t wait to see your plugins in the Figma Community. Have an idea for another video series you’d like to see? Let us know in the comments below! See you next time!

[4: Building your plugin](https://help.figma.com/hc/en-us/articles/4407531247639)
