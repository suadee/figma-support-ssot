---
기술지원명: AI workflows collection: Build your own shaders and effects
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: AI workflows collection: Build your own shaders and effects
출처링크: https://help.figma.com/hc/en-us/articles/41159710233623-AI-workflows-collection-Build-your-own-shaders-and-effects
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Story time!**

Rachel is working on the hero for the landing page of Cheddar’s special event of the year. The hero is looking a bit bland, so the Cheddar team wants to bring it to life to make a memorable impression and get people excited about the event!

Rachel has been hearing a lot about the amazing world of shaders to create visual effects, and wants to try a few iterations of the hero using shaders. But they sound like something only developers know how to do. Luckily, the Figma agent can handle the coding, so all Rachel has to do is describe what she wants to see.

## What are shaders?

If you've ever added a blur, blend mode, gradient overlay, or glassy distortion effect in Figma, shaders are what make those effects possible.

**Shaders** are tiny programs that give you precise control over the visual appearance of everything rendered on a screen. Think of them as the logic behind how light, color, and texture are applied to every pixel. They run directly on the GPU, which means they’re incredibly fast at producing complex visual effects in real time—like realistic fire, soft shadows, and distortions. This makes shaders widely used across industries and disciplines, from web design and augmented reality to game development and architectural design.

## Build shaders via the Figma agent

You don't need to be a shaders expert to create stunning visual effects in your designs. You can work with the Figma agent to build custom shader fills and effects without touching a line of code! All you have to do is describe the visual result that you want and the agent does the coding for you.

Here are a few prompting tips on describing the shader you want to the agent:

|  |  |
| --- | --- |
| **Prompting tip** | **Description** |
| **Reference real-world analogies** | Real-life references and analogies are more specific than a long abstract description. For example, you could say "like a CRT monitor from the 80s" or "the look of an oil slick on wet pavement." |
| **Use positive descriptions** | Tell the agent what you want to see, rather than leaning only on what you don’t want to see. |
| **Try this formula** | “Build me a shader that” + [describe what you want to see or a real-world analogy] + [where it appears on the layer] + [controls you want]"    For example: *"Build me a shader effect that looks like a 90's movie dream sequence where the image looks soft and glowy and there's a fog-like vignette on the edges. Let me control the vignette placement and how 'glowy' the image looks."* |
| **If you can picture it, but can't describe it** | Drop a reference image into the agent chat and ask, *"Can you describe the visual effect in this image so I can use it as a shader prompt?"* The agent will translate what it sees into language you can refine and use. |

[Get more tips on prompting the agent for shaders.](https://help.figma.com/hc/articles/41408020198935/)

## Try it out

Here are two shaders—[holographic glitch effect](#h_01KVV3KYRN4643T0VDK2X6E8JE) and [blob fill](#h_01KVV3KYRZJ4AM86ZPZGWJNAT9)—with prompts you can copy into your chat with the agent for it to build. For each shader, you'll see the same prompt but in different versions:

- **Simple prompt**: A plain-language prompt that is short, without much detail. Great for when you want to get started quickly, are comfortable with multiple follow-ups and iterations, and want to lean on the agent more.
- **Human language prompt**: A more detailed explanation for when you can explain exactly what you want, but without any of the technical jargon.
- **Technical prompt**: It’s the human language prompt but with all the technical jargon!

### Holographic glitch effect

Rachel has been seeing holographic finishes everywhere lately. They’re iridescent and unexpected, which feels right for the attendees who expect something more inspired. Let’s try this out.

![glitch-cheddar-hero.png](https://help.figma.com/hc/article_attachments/41444169904151)

Copy one of the following prompts into your chat with the Figma agent and watch the agent build the shader.

Simple prompt

```
Build me a shader that looks like a scratched holographic sticker—rainbow colors, cracked, and frozen mid-glitch.
```

Human language prompt

```
Build me a shader that looks like a holographic sticker that's been slightly damaged — like the surface is cracked and shifted, with rainbow colors peeking through the breaks. Think of a CD that's been scratched, or a piece of iridescent foil that's been torn. It should feel frozen mid-glitch, not moving.

I'd like to be able to adjust:

- How damaged or glitchy it looks
- How much the colors bleed and separate at the edges
- How rainbow and color-shifty the surface feels overall
- How many stripes or bands are visible
- The main color of the fragments
- The background color underneath
```

Technical prompt

```
Build me a holographic glitch custom effect with iridescent fragments — designed as a frozen glitch frame, not animated. Fragments are statically displaced and sliced as if caught mid-glitch. The surface has iridescent color variation across shards, with chromatic color splitting and visible banding.

UI Controls:
- Glitch Intensity (slider:continuous range, 0 = clean, 1 = heavy displacement)
- Color Split (slider)
- Iridescence (slider)
- Band Frequency (slider)
- Fragment Color (color)
- Background Color (color)
```

Once the agent has finished building the shader, test the shader out on an image layer and configure it to your liking.

**Controls explained**

- **Glitch Intensity**: Controls how much the image looks broken
- **Color Split**: Amount of chromatic offset between color channels
- **Iridescence**: Range of hue shift across fragments
- **Band Frequency**: Density of horizontal/diagonal bands
- **Fragment Color**: Base tint applied across shards
- **Background Color**: Underlying fill behind the fragments

### Blob fill

Rachel also wants to try something warmer as a second direction—something that feels more approachable in case the holographic effect is too edgy for the whole team.

![blob-cheddar-hero.png](https://help.figma.com/hc/article_attachments/41444169906711)

Copy one of the following prompts into your chat with the Figma agent and watch the agent build the shader.

Simple prompt

```
      Build me a shader that looks like blobs of colored ink floating in water, layered on top of each other like real objects. Slight paper grain over the whole thing.
```

Human language prompt

```
      Build me a shader that feels like you’re looking down into a lava lamp, or blobs of colored ink floating in water — soft round shapes that sit on top of each other like real objects, not like glowing lights. Each blob should have its own color that fades from the inside out in three steps, like a fried egg has a yolk, a white, and a clear edge. The whole thing should have a slight paper or film grain over it, like an old photograph.

I'd like to be able to adjust:
- The color at the very center of each blob
- The color in the middle ring of each blob
- The color at the outer edge of each blob
- The background color behind all the blobs
- How much grain or texture is over the whole thing
- How big or small the blobs are overall
- How sharp or soft the edge of each blob is
- How spread out or clustered together the blobs are
```

Technical prompt

```
Create a custom fill with 6 blobs in fixed positions — some circular, some oval-shaped, arranged in an organic overlapping composition. Each blob glows with 3 colors from center outward (a center color, a mid-ring color, and an edge color). Blobs have clear, visible edges rather than a soft infinite fade. They layer on top of each other like physical objects (not like glowing lights that add together). A light grain texture overlays the whole fill.

UI Controls:
- Color 1 (Center) — Color
- Color 2 (Mid-ring) — Color
- Color 3 (Edge) — Color
- Background Color — Color
- Grain Intensity — Slider (0 = no grain, 1 = heavy texture)
- Scale — Slider (controls overall blob size relative to the fill area)
- Edge Sharpness — Slider (0 = slightly soft edge, 1 = hard cut-off)
- Blob Overlap — Slider (how tightly the 6 blobs cluster together)
```

Once the agent has finished building the shader, run the shader and configure it to your liking.

## Iterating from here

The path to building something is iterative and almost always requires refinement. You don’t have to get it right in one prompt. As shown in the examples above, a brief, high-level prompt that explains the general effect that you want is an effective way to begin. After that, you can move into refining the details and controls.

For example you could ask the agent:

- “What controls would you suggest adding to give me more flexibility with this effect?”
- “Add an on/off toggle for the grain.”

More iterating tips:

- If you already know there are multiple changes you want to make, consider bundling them in one message to save time.
- Make sure to test as you go. Test the tool on a variety of inputs early and often. Make sure to use a duplicate of the design to test your shaders on.
- When to start fresh: If after a few prompts you’re not getting closer to what you envisioned, you can take your learnings and start fresh with more specificity.

## More effects you can try

Want to continue exploring shaders? Here are a few more shader types worth trying on the Cheddar hero design.

**Plasma:** Psychedelic, layered color blends. Good for backgrounds that need energy without communicating anything specific.

> Create a shader with a background of swirling, electric color blends in deep violet, magenta, and teal — like a still frame from a lava lamp.

**Heat haze displacement:** Makes your layer look subtly warped and shimmering, like hot air rising off pavement.

> Create a shader with a surface that looks warped and slightly wavy, like heat rising off hot pavement on a summer day. Controls for warp intensity and scale.

**Paper texture:** A math-generated texture that sits on top of your layer like physical grain or paper.

> Create a shader with a fine grain texture, like high-quality uncoated print paper. Should sit on top of my existing layer colors, not replace them. Controls for grain density and intensity.
