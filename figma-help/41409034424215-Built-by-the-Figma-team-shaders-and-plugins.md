---
기술지원명: Built by the Figma team: shaders and plugins
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Built by the Figma team: shaders and plugins
출처링크: https://help.figma.com/hc/en-us/articles/41409034424215-Built-by-the-Figma-team-shaders-and-plugins
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**Generated plugins and shaders are currently in open beta.** Features may change and you may experience performance issues as we continue to improve generated plugins and shaders. Learn more about [what's included in the beta](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta).

Before you Start

Who can use this feature

Available [all plans](https://figma.zendesk.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a Figma Design file can use plugins and shaders created by Figma

Plugins and shaders created by Figma are free to use

The Figma team has built dozens of plugins and shaders created for you to use for free in your design files.

In this article, you’ll find descriptions for some of the more technical settings and terminologies to help you understand how they work. This article is not comprehensive of the shaders and plugins available by Figma.

**New to generative plugins and shaders?** Check out our [quick start guide](https://help.figma.com/hc/articles/41147702210071/) to learn more.

## Find tools created by Figma

To find free shaders and plugins created by the Figma team:

1. Open a Figma design file, and click **Tools** from the navigation bar.
2. Open the **Source** dropdown and select **From Figma**.
3. (Optional) Click the  **Filter** icon and select **Shader fill**, **Shader effect**, or **Plugin**.

## Shader effects

Shader effects can be applied to any existing images and layers to create striking visuals—like distortions, blurs, and dithering.

### Bloom

Add cinematic bloom and glow to images, with on-canvas controls for region, intensity, softness, and color.

![Bloom effect preview.png](https://help.figma.com/hc/article_attachments/41435665299479)

### Bokeh blur

Create a soft bokeh blur with customizable highlight density and blur radius.

![Bokeh blur effect preview.png](https://help.figma.com/hc/article_attachments/41435665301527)

Bokeh is the soft, round glow that out-of-focus lights make in a photo. It shows up best on images with bright spots like lights, neon, or reflections. To create a blurry background look, put a sharp subject on top of the blurred layer.

### Channel mixer

Create custom color treatments for false-color imagery, duotones, and creative grading.

![Channel mixer effect preview.png](https://help.figma.com/hc/article_attachments/41435665302679)

Channel mixer takes the red, green, and blue colors in a image and recolors each channel with your own selected color.

The color space setting defines how colors blend in the areas where channels overlap. The sRGB setting looks vivid and familiar, and Linear is softer with more gradual blends.

For bold results, pick three colors that are spread across the color wheel. For a muted or monochromatic look, pick closers closer together.

### Chromatic metal

Give shapes a glossy, inflated metal finish with adjustable depth, roughness, and RGB separation.

![Chromatic metal effect preview.png](https://help.figma.com/hc/article_attachments/41435658382743)

Start by setting the metal's colors in the Gradient.

**Settings**

- **Rounding:** Smooths the edges of the reflection shapes
- **Depth:** How 3-dimensional the surface looks. A higher depth makes the bumps and dents stronger. A lower depth makes the surface look flat.
- **Roughness:** How shiny the metal is. At 0% the surface is mirror-smooth, and higher looks brushed or matte.
- **RGB split:** Adds a rainbow edge by nudging the colors apart, creating an oil-slick or holographic look
- **Scale:** The size of reflections
- **Stretch:** Compresses or elongates the reflections
- **Angle:** Rotates the reflective pattern
- **Gradient:** The colors of the metal surface
- **Repeats:** How many times the colors repeat across the surface. More adds extra bands of contrast.
- **Offset:** Shifts which part of the gradient sits on top
- **Phase:** Shifts where the colors lands without changing the pattern itself
- **Evolution:** Drag to try different versions of the pattern without changing anything else

### Color adjust

Adjust tone, color, and detail with photo correction tools like exposure, contrast, saturation, and more.

![Color adjust effect preview.png](https://help.figma.com/hc/article_attachments/41435665305495)

**How to use it**

1. Start with **Exposure** for overall lightness, then set **Black Point** and **White Point** to anchor your darkest and brightest values.
2. Shape contrast with **Contrast**, then refine **Highlights** and **Shadows** on their own. Use **Brilliance** to recover detail at both ends at once (it lifts darks and reins in bright areas without blowing out highlights), and **Gamma** to shift mid-tones.
3. Adjust color with **Temperature** (warm to cool), **Tint** (green to magenta), **Vibrance**, and **Saturation**. Add a **Color Filter** for an overall color wash.
4. Finish with **Definition** for crispness and perceived detail without the halos of traditional sharpening.

### Colored edges

Transform images into vibrant line art by adjusting gradient colors, edge detection, thickness, and opacity.

![Colored edges effect preview.png](https://help.figma.com/hc/article_attachments/41435665305751)

**Settings**

- **Threshold:** Edge sensitivity. A lower threshold catches softer edges, and higher threshold catches hard, dramatic edges
- **Thickness:** Width of the colored lines
- **Intensity:** How vivid and opaque the lines are
- **Gradient:** Colors of edge lines. Wraps radially around the center, so edges at different angles pick up different colors. Up to eight stops.
- **Opacity:** How much the photo fades in favor of the background color. At 0 the photo shows fully, and at 100 only the background and edges show
- **Background:** The solid color behind the edges. They become visible as you raise Opacity.

### Dither

Create stylized dithering using popular algorithms like Atkinson, Floyd–Steinberg, Bayer, and blue noise.

![Dither effect preview.png](https://help.figma.com/hc/article_attachments/41435658385303)

Dithering recreates shades and colors using patterns of small dots, like an old printed comic or a retro game. Start by choosing a Style, since it sets the look of the dots.

**Settings**

- **Style:** The pattern used to place the dots (see table below)
- **Size:** How big each dot is, from fine and photo-like to chunky and retro
- **Levels:** The number of shades the image reduced to. Higher levels retain more detail.
- **Brightness, Contrast:** Adjust these to give the dots cleaner light and dark areas to work with
- **Mono:** Turns the image monochromatic, based on the Mono Color selected. Off keeps the original colors.
- **Mono Color:** The color used when Mono is on

| Style | What it does | How it looks |
| --- | --- | --- |
| Bayer | Fixed mathematical grid | Regular, geometric halftone; no randomness |
| Blue Noise | Perceptually uniform random scatter | Organic but even; closest to film grain |
| Threshold | No dithering, a hard cut to the nearest tone | Stark, flat posterization, clean edges |

### Filter presets

Apply classic color filter presets to any layer, like grayscale, sepia, vintage, warm, cool, and noir.

![Filter presets effect preview.png](https://help.figma.com/hc/article_attachments/41435658386455)

Pick a preset, then use Intensity to blend it with the original image. The 40 to 80 percent range often reads best, as the filter is visible while allowing the image's original colors to still show through.

### Gooey merge

Create smooth, organic blobs that merge and separate dynamically. Fine-tune spread, edge softness, and blending.

![Gooey merge effect preview.png](https://help.figma.com/hc/article_attachments/41435665309591)

This effect makes nearby shapes melt together like drops of liquid. Start by choosing how shapes are detected with Input mode, then drag Threshold negative to merge them.

**Settings**

- **Input mode:** How the effect finds your shapes. Alpha follows the see-through areas (best for icons and cutouts), and Luminance follows brightness (best for photos).
- **Threshold:** Sets where the edge of each shape sits. Negative values grow the shapes so nearby ones touch and merge. This is the main control.
- **Spread:** How far apart shapes can be and still merge
- **Edge Softness:** How soft the blob edges are, from crisp to gooey
- **Foreground Color:** The color of the blobs
- **Background Color:** The color behind them
- **Invert:** Swaps the shapes and the background, so the shapes become see-through
- **Source Mix:** How much of the original layer shows through on top. At 0 you see only the blobs.

**Good for:** liquid blob illustrations, organic shape systems, smooth blob backgrounds, sticker-style outlines around icons, soft spotlight masks (with Invert on), and merging letters into a single flowing logo.

### Gradient map

Apply flexible color mapping with custom gradients, and control pattern repetition, offset, and color space.

![Gradient map effect preview.png](https://help.figma.com/hc/article_attachments/41435658389143)

**How to use it**

1. Design your **Gradient** first. The left stop colors the darkest pixels and the right stop the brightest. Two stops give a clean duotone, and more stops give richer results.
2. Pick a **Mix space** for how colors blend between stops. Use **sRGB** for a familiar look, or **OKLab**, **OKLCH**, or **Linear** if transitions look muddy.
3. Nudge **Offset** if the shadows or highlights map to the wrong colors.
4. Raise **Repeat frequency** above 1 to tile the gradient into vivid color bands, and set the **Repeat type** (Mirror gives smooth symmetrical bands, and Repeat gives hard-edged neon cycling).
5. Add **Scatter** to break up harsh banding with a film-grain or risograph texture.

**Good for:** duotone and brand coloring, false-color data visualization, consistent recoloring across mismatched assets, mood grading, risograph simulation, and psychedelic banding.

### Halftone

Simulate vintage print and comic-book halftones with controls for color separation, softness, scale, and placement.

![Halftone effect preview.png](https://help.figma.com/hc/article_attachments/41435658398359)

A halftone recreates an image using a grid of dots, like a printed newspaper or comic book. Start by choosing the Pattern and Color Mode, then set the dot size.

**Settings**

- **Pattern:** The dot style. Dot is crisp circles, and Blended is soft, fading dots.
- **Dot Size:** How big the dots are. Bigger means fewer, chunkier dots, and smaller means a fine grain.
- **Dot Scale:** How much each dot can grow to fill its space in the darkest areas
- **Color Mode:** How color is handled (see the table)
- **Rotation:** Tilts the whole dot grid. 45 degrees is the classic print angle.
- **Center:** The point the grid lines up from
- **Softness:** How soft the dot edges are
- **Clip to Alpha:** When on, keeps the dots inside the solid parts of your layer, leaving see-through areas clear

| Mode | What it does | How it looks |
| --- | --- | --- |
| CMYK | Splits into Cyan, Magenta, Yellow, and Black at print screen angles | Authentic offset-print rosette pattern |
| RGB | Splits into Red, Green, and Blue dot screens | Additive, digital screen feel |
| BW Light | Black dots on white, luminance-mapped | Classic newspaper halftone |
| BW Dark | White dots on black (inverted) | Dramatic, screen-printed dark look |

### Hatching

Create hatching effects for text, shapes, and images. Adjust directly on canvas for density, spacing, and shape.![Hatching effect preview.png](https://help.figma.com/hc/article_attachments/41435665313559)

Start by picking the line Pattern, then position it with the on-canvas Transform handle.

**Settings**

- **Pattern:** Waves, Zigzag, or Circles
- **Density:** The thickness of lines that fill the bright areas of the image. Low density means lines will be thin. A high number means lines will be thick, producing nearly solid fills.
- **Frequency:** Number of pattern cycles that fit across the layer
- **Amplitude:** How far the lines bend
- **Softness:** Feathers the edges of lines
- **Offset:** Shifts the position of the pattern without rotating it
- **Background:** Color behind the lines
- **Foreground:** Color of the lines
- **Transform:** An on-canvas handle that sets the origin (center), rotation (angle), and line spacing (radius).

### Lens distortion

Create a realistic lens distortion and chromatic aberration with an adjustable center point.

![Lens distortion effect preview.png](https://help.figma.com/hc/article_attachments/41435665314455)

This mimics a real camera lens: a fisheye bulge that rounds the image outward, plus chromatic aberration, the rainbow fringe where colors split at the edges. Start by placing the Center point, then build up Distortion and Aberration.

**Settings**

- **Center point:** The spot the bulge pushes out from. Starts in the middle.
- **Distortion:** How strong the fisheye bulge is. 0.3 to 0.5 looks natural, and toward 1 is extreme.
- **Aberration Strength:** How far the colors split apart, from a subtle fringe to a bold rainbow edge
- **Mode:** The style of color split (see the table)
- **Quality:** Trades speed for smoothness. Higher is smoother with less banding, and lower renders faster but rougher.

| Mode | What it does | How it looks |
| --- | --- | --- |
| Lateral | Colors pushed sideways from the center | Dark core, glowing edges |
| Longitudinal | Colors split by focus plane | Full rainbow across the shape |
| Anamorphic | Horizontal cinema-lens split | Horizontal gradient, dark crossband |

### Outlines

Create stacked outlines with adjustable spacing, thickness, and color gradients. Perfect for bold typography and graphic accents.

![Outlines effect preview.png](https://help.figma.com/hc/article_attachments/41435665315991)

This draws a series of evenly spaced outlines that echo your shape outward, like ripples. Use Input Mode to tell it how to find your shape's edges: Luma uses brightness, Inverse luma uses darkness (for dark art or text on white), and Alpha uses the see-through areas.

### Pattern refraction

Simulate refracting light to create distortions like waves, zigzags, and lenticular patterns.

![Pattern refraction effect preview.png](https://help.figma.com/hc/article_attachments/41435665316119)

This bends the image as if you were looking at it through textured or rippled glass. Start by picking a lens Pattern, then position the grid with the on-canvas Transform handle.

**Settings**

- **Pattern:** The shape of the glass lenses (see the table). This sets the overall look.
- **Strength:** How much the image bends (−100 to 100). Positive is a deep, glassy warp, and negative bends it the other way.
- **Smoothness:** Blends the lenses together so the surface looks like one smooth sheet instead of a grid
- **Frost:** Adds a grainy, frosted-glass haze
- **Dispersion:** Splits the colors into a rainbow fringe at the edges of each lens, like light through a prism
- **Edge wrap:** What fills in at the layer's edges where the bend pulls from outside. Zero is see-through, Clamp smears the edge, Repeat tiles the image, and Mirror reflects it.
- **Transform:** An on-canvas handle for the grid's position, rotation, and lens size

| Pattern | How it looks |
| --- | --- |
| Lenticular | Vertical stripes, like a 3D trading card |
| Zigzag | Angular, jagged ribbons |
| Waves | Soft, undulating ribbons |
| Circular | Grid of magnifying beads |
| Curved square | Soft, squarish bubbles |
| Flat square | Blocky grid with sharp seams |

### Pixel stretch

Create stretch and motion-inspired distortion effects. Edit the effect visually with on-canvas controls.

![Pixel stretch effect preview.png](https://help.figma.com/hc/article_attachments/41435665316503)

Place the on-canvas circle over the area you want to stretch, then drag Offset to set how far and which way the pixels pull. Negative and positive values go opposite directions.

### Pixelate

Pixelate and scatter an image into tiled shapes with adjustable size, color reduction, and dissolve.

![Pixelate effect preview.png](https://help.figma.com/hc/article_attachments/41435658404119)

Choose a tile Shape and Size, then use Color trim to cut down the number of colors.

For a scatter effect, raise Dissolve to make tiles drop away, and use Knockout to choose whether the gaps show transparency or the original image.

Use Falloff to feather the region's outer edge, so tiles near the edge dissolve more than those at the center.

### Slice shift

Slice an image into angled bands and shift them apart with adjustable angle, spread, and randomness.

![Slice shift effect preview.png](https://help.figma.com/hc/article_attachments/41435665321239)

Place the on-canvas circle and rotate it to set the push direction, then use Shift to set how far the bands slide. Add Random for an uneven, hand-made feel.

### Warp

Create organic distortions like ripples, swirls, twists, and bulges.

![Warp effect preview.png](https://help.figma.com/hc/article_attachments/41435658405655)

**How to use it**

1. Pick a distortion shape in **Type** first (see the table). It defines the whole character of the effect.
2. Set the **Center** handle, the point the distortion radiates from.
3. Dial **Frequency** (how many ripples or cycles fit across the layer) and **Amplitude** (how dramatic the displacement is, where too high tears the image).
4. Reset Frequency and Amplitude when you switch Type, since each formula responds differently.

| Type | How it looks |
| --- | --- |
| Sine wave | Undulating warp running both directions, like shaken cloth |
| Twist | Swirling spiral tightening toward the center |
| Bulge | Convex bubble popping toward you |
| Pinch | Concave sink pulling inward |
| Ripple | Concentric ripples, like a stone in water |
| Flag | Bands waving like cloth in wind |
| Squeeze | Accordion-like vertical squeeze and stretch |
| Swirl | Tighter, more dramatic pinwheel than Twist |

## Shader fills

Shader fills are great for standalone visuals such as realistic textures (like fire and water), patterns, and complex gradients.

### Clouds

Create procedural cloud textures with customizable colors, scale, and turbulence.

![cloud.png](https://help.figma.com/hc/article_attachments/41447138129687)

Start by framing the view with the on-canvas Transform handle, then set the sky and cloud colors.

**Settings**

- **Sky color:** The background sky, as a top-to-bottom gradient (top is the upper sky, bottom is the horizon)
- **Cloud color:** The color of the sunlit tops of the clouds
- **Shadow color:** The color of the shaded undersides. The bigger the difference from Cloud color, the more 3D the clouds look.
- **Coverage:** How much of the sky is filled with clouds
- **Density:** How thick and solid the clouds are
- **Brightness:** The overall lightness of the clouds
- **Detail:** How intricate the cloud edges are. High adds fine detail, and low keeps them soft.
- **Variation:** How lumpy and uneven each cloud looks
- **Warp amount:** How much the clouds are bent and distorted, from clean shapes at 0 to wild, swirly ones
- **Warp scale:** The size of that distortion, from fine crinkles to big rolling warps. Only matters when Warp amount is above 0.
- **Stretch:** Stretches the clouds sideways into long, wispy bands
- **Phase:** Drag to reshape every cloud into a new arrangement
- **Transform:** An on-canvas handle to pan, tilt, and zoom the view

### Concentric patterns

Generate bold concentric patterns with customizable shapes, spacing, scale, rotation, and falloff.

![concentric-pattern.png](https://help.figma.com/hc/article_attachments/41447144815639)

Falloff fades the rings darker toward the edges, and Inverse falloff flips that so the center darkens and the outer rings brighten instead.

### Fractal noise

Create organic procedural textures with Perlin, Value, and Voronoise noise patterns. Adjust scale, turbulence, and layering.

![Fractal noise fill preview.png](https://help.figma.com/hc/article_attachments/41435658408983)

This builds organic, textured patterns from procedural noise. Start by picking a Noise type, then position and scale it with the Transform handle.

**Settings**

- **Noise type:** The base texture. Value is blocky and smooth, Perlin is soft and cloud-like, and Voronoise looks like soft-edged cells.
- **Saturation:** How colorful the texture is. At 0 it is greyscale.
- **Sharpness:** How hard or soft the edges between areas are, from watercolor-soft to crisp
- **Turbulence:** How much the pattern twists and swirls instead of staying even
- **Layers:** How many layers of detail are stacked up. More layers add finer texture.
- **Layer blend:** How those layers combine (see the glossary). The mode decides whether layers add up, cut into each other, or form sharp ridges.
- **Layer gain:** How strong each finer layer is compared to the one before it
- **Layer scale:** How much smaller each layer is than the last, which sets how tightly packed the detail is
- **Layer flow:** Shifts each layer a little, adding a sense of motion or depth
- **Tile size X, Tile size Y:** Set these to make the pattern repeat seamlessly across a surface
- **Cycles:** How many times the colors repeat across the pattern
- **Phase:** Shifts which colors land where, without changing the pattern itself
- **Transform:** An on-canvas handle for the pattern's position, scale, and rotation

**Glossary**

- **Procedural noise:** Computer-generated randomness that looks natural. It is what gives these textures their organic, cloud-like or marbled feel.
- **Layer blend modes:** The options for Layer blend. Add, Min, Max, Add absolute, Subtract absolute, Add multiplied, Exclusion, Coarse knockout, and Fine knockout. They range from layers simply adding together to sharp ridges and cut-out effects.

### Glowing wave

Generate luminous wave graphics with on-canvas controls for color, glow, and motion.

![Glowing wave fill preview.png](https://help.figma.com/hc/article_attachments/41435665328663)

Set the Wave Color and position the wave with the on-canvas handle, then adjust Amplitude and Glow Intensity to taste.

**To animate a looping scroll:** in Motion mode, set Phase to 0 percent on the first frame and 100 percent on the last. The wave then scrolls smoothly with no visible jump.

**To animate a looping scroll:**

1. Enable Motion mode and select the layer with the glowing wave shader.
2. Open the shader fill settings, and click  **Add keyframe** next to the **Phase** control.
3. In the timeline, set Phase to 0 percent on the first frame and 100 percent on the last. The wave then scrolls smoothly with no visible jump.

[Learn more about using motion in Figma.](link)

### Mesh gradient

Create smooth mesh gradients with 16 editable color points, and edit directly on the canvas.

![Mesh gradient fill preview.png](https://help.figma.com/hc/article_attachments/41435658412055)

Change the corner and center colors first, then fine-tune the edge points (16 in a 4×4 grid). Use Tessellation to set how smooth the blend is, where higher is smoother and lower looks more faceted. You can stack other fills above or below this one.

### Moire

Create mesmerizing moiré patterns with customizable line distortion, RGB separation, and optical interference effects

![Moire-Hero.png](https://help.figma.com/hc/article_attachments/41435658416023)

A moiré is the rippling, shimmering pattern you get when two sets of lines overlap. Use Line count to set the density, Warp origin to move where the ripples spread from, and RGB split for a rainbow edge along the lines.

### Nebula

Create deep-space backgrounds with customizable colors, density, brightness, and other atmospheric details.

![Nebula fill preview.png](https://help.figma.com/hc/article_attachments/41435665330071)

Set the three colors, then roll a new scene with Seed, where each number gives a completely different sky. Use Travel to fly the view forward through the layers of stars. It loops, so 0 and 1 look the same.

### Pattern grid

Create custom geometric pattern fills with adjustable shapes, layouts, sizes, spacing, colors, and strokes.

![PatternGrid-Hero.png](https://help.figma.com/hc/article_attachments/41435658417431)

Start by choosing a Shape and Layout, then position the grid with the on-canvas Transform handle.

**Settings**

- **Shape:** The repeating shape: Diamond, Circle, Box, Triangle, Hexagon, Cross, or Ring
- **Layout:** How the shapes are arranged. Grid is straight rows and columns, Brick offsets every other row, and Hex packs them in a honeycomb.
- **Size:** How much of each cell the shape fills
- **Scale:** Zooms the whole pattern in or out
- **Shape color:** The color of the shapes
- **Background color:** The color behind the shapes
- **Stroke color:** The outline color (shows when Stroke width is above 0)
- **Stroke width:** How thick the outline around each shape is
- **Softness:** Blurs the shape edges into a soft glow
- **Clip to cell:** Keeps each shape inside its own cell, so pointed shapes like Diamonds and Triangles don't overlap their neighbors
- **Offset:** Slides the whole pattern across the frame. It wraps seamlessly, so you never see a seam.
- **Transform:** An on-canvas handle for the position, spacing between shapes, and rotation

### Water caustics

Generate shimmering water caustics with customizable colors, scale, and motion.

![Water caustic fill preview.png](https://help.figma.com/hc/article_attachments/41435658421783)

Set the Water and Highlight colors (keep them close for a natural look), then use Scale to zoom and Phase to shuffle the ripples into a different arrangement.

**To animate it:**

1. Enable Motion mode and select the layer with the water caustic shader.
2. Open the shader fill settings, and click  **Add keyframe** next to the **Phase** control.
3. In the timeline, set Phase to 0 percent on the first frame and 100 percent on the last. The wave then scrolls smoothly with no visible jump.

[Learn more about using motion in Figma.](link)

## Generated plugins

### Mock Data Lab

Mock Data Lab helps designers quickly create realistic mockups from a single design template, eliminating the need to manually edit each variation.

With Mock Data Lab, you can:

- Create a template from a selected design frame
- Map layers to mock data generators
- Save templates to the plugin library
- Generate multiple variations populated with realistic mock data

**Create a template**

1. Select a frame and run the plugin. Click **Create**.
2. To map a layer to mock data, select a layer on the canvas and click **Add layer** in the plugin.
3. Configure the layer by:
   - Giving it a descriptive name
   - Choosing a generator type. (Available generator types depend on the type of layer selected)
   - Selecting a mock data source
4. Repeat for any other layers, then click **Save template** to add it to the library. The template will be added to your Mock Data Lab library.

Example mappings:

| Layer | Generator type | Data source |
| --- | --- | --- |
| First Name | Text | First name |
| Title | Text | Job title |
| Thumbnail component | Variant | — |

**Generate mockups**

1. Open the Mock Data Lab library and choose a saved template.
2. Select a **Theme** that best matches the type of content you want to generate.
3. For each field, you can:
   - Use the **Target** icon to find its layer
   - Use the **Lock** icon to fix a value across all variations, or leave it unlocked to generate new values
4. Under **Layout**, set the number of variations and how they're arranged, then click **Generate**.
