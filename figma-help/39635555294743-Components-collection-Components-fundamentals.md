---
기술지원명: Components collection: Components fundamentals
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Components collection: Components fundamentals
출처링크: https://help.figma.com/hc/en-us/articles/39635555294743-Components-collection-Components-fundamentals
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Note:** This video is part of our [Figma Design for beginners](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners) course, which includes an in-depth look at features like components, auto layout, prototyping, and more.

[Components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma) are reusable design elements. They save you from having to recreate the same element multiple times, and make it easy to manage changes across your designs.

There are two aspects to a component:

- The **main component** that defines the properties of the design element
- and an **instance** that’s a copy of the component, which you can add to your designs.

## About creating components

You can create main components from any collection of layers. This could be a simple element, like an icon or button; or an entire layout, like a card or menu.

![](https://help.figma.com/hc/article_attachments/39635597998871)

To create a main component, select the layers you want to use and click **Create component** in the right sidebar. You can identify main components by their purple bounding box on the canvas and  four diamonds icon in the layers section in the left sidebar.

## About adding instances

Once you’ve created a main component, you can add [instances](https://help.figma.com/hc/en-us/articles/360039150173-Create-and-insert-component-instances) of it to your designs. To add an instance, duplicate the main component on the canvas or select the main component from the Assets tab in the left sidebar and drag it onto the canvas. You can identify instances by their purple bounding box and their  outlined diamond icon.

Instances are connected to their main components. This means that changes made to the main component are automatically applied to every instance of that component in the same file, saving you time and making sure your designs stays consistent.

There may be times where you don’t want the instance to look identical to the main component. Buttons, for example, will need different labels for different actions. If you change the label in the main component, every instance would take on that new label.

You can make changes to some properties of an instance—including text, fill, stroke, and size—without breaking its connection to the main component. This allows you to customize instances to fit their new context, or test out different design variations.

You can always reset changes if you decide you’d rather use the default properties on an instance. You can also push changes to the main component, and any other instances in the file, if you find something you like more than your original design.

**Note:** Keep in mind, there are certain things you can’t change on an instance because they’re tied to the structure of the main component. For example, you can’t add or remove layers, or reorder layers within an instance. You also won’t be able to modify any constraints applied to the layers.

## About detaching instances

If you need to make more extensive changes, you can detach an instance, breaking its connection to the main component. This means that it won’t receive any updates from the main component. Detaching an instance can be useful, but keep in mind, once an instance is detached, it can’t be reconnected to the main component in the future. If you accidentally detach an instance, you can undo it right away using the keyboard shortcut:

- Mac: `⌘ Command` `Z`
- Windows: `⌃ Control` `Z`

## Check your knowledge

## Additional resources

For more information about components, check out these additional resources:

- Community playground file: [Collection companion: Components](https://www.figma.com/community/file/1627053215388532830)
- Help Center article: [Guide to components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma)
- Help Center article: [Create components to reuse in designs](https://help.figma.com/hc/en-us/articles/360038663154-Create-components-to-reuse-in-designs)
