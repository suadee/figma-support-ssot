---
기술지원명: AI workflows collection: Bring imagery into your designs
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Bring imagery into your designs
출처링크: https://help.figma.com/hc/en-us/articles/41159711083543-AI-workflows-collection-Bring-imagery-into-your-designs
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

![](https://help.figma.com/hc/article_attachments/41442804467351)

Rachel is designing a new landing page for Cheddar, a budgeting app with a playful, trend-forward aesthetic.

She's got the layout figured out, but now she needs the visual assets: a hero image that feels culturally current, a dark mode version for night owl users, and supporting visuals throughout the page. Some of those assets don't exist yet. Others need to be adapted to fit the design.

She'll need to generate imagery, make edits, and refine everything until it feels like a cohesive brand.

Imagery is as fundamental to a design as typography or layout. It shapes first impressions and communicates brand personality, often before someone reads a single word.

So, what makes an image right for a design? It needs to feel on-brand, consistent with the other imagery in the design, and composed to fit the layout it's living in.

This all comes down to your creative vision. Figma’s AI image tools handle the execution of creating, editing, and refining imagery, but the creative decisions are yours.

In this article, you'll learn how to use Figma's image tools to execute on a creative direction in three steps:

- **Generating imagery from scratch** using text prompts, reference images, and the right model for the job
- **Editing and adapting images** to fit your layout
- **Creating consistent creative treatments** across your designs with Weave tools

You’ll practice with some hands on exercises to build out a landing page design along the way.

## Generate imagery from scratch in Figma

When you’re working on a design that needs images that don’t yet exist, Figma’s generate image tool can create them right in your design file.

### Tips for writing image generation prompts

When getting started with image generation, it's natural to lead with the subject: “generate an image of a coffee cup” or “generate an image of a woman skating”. But two prompts with the same subject can produce completely different images depending on how you describe everything else around it.

When prompting images, think of yourself as a creative director and go beyond specifying the subject. Here are some helpful things to include in your image generation prompt:

|  | **What to include** | **Examples** |
| --- | --- | --- |
| **Subject** | What’s in the photo? | The New York City skyline, a plain white t-shirt mockup |
| **Shot type** | What is the angle of the photography? | Close-up, wide shot, overhead flat lay, bird's eye view |
| **Composition** | How are elements arranged? | Negative space on the left, subject at the edge of the frame |
| **Lighting** | How does the light hit the subject? | Soft window light, golden hour backlight, overcast diffused |
| **Photography style** | What is the genre and aesthetic context of the image? | Street photography, editorial fashion, still life |
| **Mood and color** | How does the image feel? | Warm and minimal, high contrast, muted pastels, blue and orange hues |

### Using reference imagery

In addition to a detailed prompt, including reference imagery in image generations can help guide your outputs in ways that words cannot. There are several different ways you might use reference imagery in your image generation prompts. Consider the following:

- A mood board or photo for overall style and color direction
- An existing image from the design to match lighting or tone
- A sketch or wireframe to guide composition and layout
- A product or object you want included in the scene

## Now you try!

Experiment with Figma’s image generation tools to create a trendy and on-brand hero image for the Cheddar landing page.

### 1. Copy the reference images into a file

First, click **Copy design layers** on the image below and paste the **reference images** from your clipboard into a [new Figma Design file](https://figma.new). The images may take a few moments to load in your file.

![](https://help.figma.com/hc/article_attachments/41442804469143)

### 2. Generate an image with a prompt and reference imagery

[](https://help.figma.com/hc/article_attachments/41432102594071)

Select **Make an image** in the toolbar and paste in the prompt:

```
Street photography of a woman doing a jump trick at a skate park, midair with open sky all around, vibrant saturated pastel colors, bright natural daylight, slightly grainy, shot on 35mm.
```

Then, attach one or more reference images by selecting the  plus button in the bottom right of one or more images.

Try swapping different reference images or making small prompt edits and compare the results. Notice how these changes affect the style, mood, composition, and overall direction of the image.

## Edit and adapt images to fit your designs in Figma

Whether you’ve generated images for your design, sourced stock photography, or taken your own, you’ll usually need to make some modifications to fit your layout and design style. You might need to make larger changes, like editing the style and colors of an image, or targeted edits, like removing a pesky background element.

You can achieve many of these adjustments with Figma’s [AI-powered image editing tools](https://help.figma.com/hc/en-us/articles/24004542669463): Isolate, Expand, Erase, Boost resolution, Remove background, and Edit with prompt.

These tools work best when you combine them. You’ll find that sequencing several of these tools can turn Figma into a powerful image editor.

A useful approach is to work from broad to specific. Get the overall composition right first: Does the image fit the frame? Does the subject read clearly in the layout? Then focus in on the details.

As a general rule: reach for edit with prompt for broad changes like style, color, and mood. Then use targeted tools for precise structural edits once the overall image is where you want.

## Now you try!

We’ll build on the previous exercise by using the generated images in some website section layouts.

Your challenge is to recreate the sample website sections by combining and layering Figma's image editing tools. Feel free to follow the examples closely or put your own spin on them.

### 1. Copy the reference imagery and starter designs into a file

First, click **Copy design layers** on the image below and paste the **image and website section designs** from your clipboard into your file.

![](https://help.figma.com/hc/article_attachments/41442804470167)

### 2. Recreate these layouts, or imagine your own

Use the starting assets provided, or the images you created in the previous step, recreate one or both of the example layouts using Figma's image editing tools. Or, skip the examples and create your own layouts from scratch!

You’ll need to layer multiple image editing tools, like [**Expand**](https://help.figma.com/hc/en-us/articles/24004542669463-Make-or-edit-an-image-with-AI#h_01KBJQAF0GHQH58JT9VKQETNPY) and [**Isolate**](https://help.figma.com/hc/en-us/articles/24004542669463-Make-or-edit-an-image-with-AI#h_01KBJQAF0G6X98H5JJ8GBAPTGP), together to achieve these layouts.

**Not sure where to start?** Follow along in the videos below, or copy the finished layouts into your file to inspect the designs:

[](https://help.figma.com/hc/article_attachments/41432962126231)

[](https://help.figma.com/hc/article_attachments/41433012141847)

![](https://help.figma.com/hc/article_attachments/41442776560407)

## Creating consistent creative treatments with Weave tools

As you work with Figma’s image tools, you might find yourself re-using parts of the process to create similar results: for example, the same reference imagery or the same language in each prompt.

Figma Weave allows you to systemize these workflows, packaging detailed prompts and reference imagery into node-based workflows that excel in consistent, high quality results. With Weave tools, you can access these workflows right from the Figma canvas.

Figma currently offers a set of pre-built Weave tools built for common creative tasks. They're particularly useful for:

- **Applying a visual style** to an image: Bauhaus, marker art, pixel art, crayon
- **Generating product imagery:** e-commerce shoots, multi-view product sheet

Coming soon, you'll be able to build your own Weave tools to define your own visual systems.

Think of building your own Weave workflow as setting up a creative system upfront. You define the style, the references, the prompts once. From there, anyone on the team can apply that treatment to any image, consistently, without having to recreate the thinking each time.

## Now you try!

We'll build on the previous exercises by adapting an existing image for a new design direction.

Cheddar's landing page now needs a dark mode, and the current imagery no longer fits the theme. Instead of generating a new image and trying to recreate the original composition, you'll use Figma's **Change Lighting Weave tool** to transform the existing image into a neon-lit version. Same shot, completely different energy.

### 1. Copy the reference imagery and starter designs into a file

First, click **Copy design layers** on the image below and paste the **image and website section designs** from your clipboard into your file.

![](https://help.figma.com/hc/article_attachments/41442776561687)

### 2. Transform the images for dark mode

1. Head over to **Tools** in the navigation bar on the left and search for **Change lighting.**
2. Select one of the starting assets, or any image you’ve created, and choose the **Neon colored light** style.
3. Then, follow the same steps as the previous exercise to adapt the new dark mode imagery into the website layouts, or create your own.

**Not sure where to start?** Follow along in the video below or copy the finished layouts into your file to inspect the designs.

[](https://help.figma.com/hc/article_attachments/41434318678679)

![](https://help.figma.com/hc/article_attachments/41442776563607)

Figma's AI image tools cover the full arc of working with imagery in a design. You can use them to handle the execution of your ideas, and speed up the amount of time it takes to create and refine images for your designs.

The best results come from bringing creative direction to the tools. Things like a specific prompt, a well-chosen reference, a clear sense of what the image needs to do in the design go a long way.
