---
기술지원명: Identify matching objects
카테고리: 디자인
작성자: Figma
승인자: (승인 대기)
출처: Identify matching objects
출처링크: https://help.figma.com/hc/en-us/articles/21523793229463-Identify-matching-objects
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Matching objects are identical objects that exist across more than one frame. For example, many app designs use an identical header across the top of each frame.

Use matching objects to save time when selecting, editing, and prototyping.

![Three different frames, depicting checkout cart designs. Across the top of each frame is the same header with a navigation menu and a checkout cart icon.](https://help.figma.com/hc/article_attachments/21551618063767)

Matching objects are used with:

- [Smart animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames): Create advanced animations between matching objects when prototyping
- [Multi-edit](https://help.figma.com/hc/en-us/articles/21635177948567/): Edit objects in bulk
- [State management](https://help.figma.com/hc/en-us/articles/14397859494295-State-management-for-prototypes): When prototyping, share the state of interactive components, frames with scroll, and videos when navigating between frames with matching objects
- [Matching interactions](https://help.figma.com/hc/en-us/articles/360040315773-Create-interactions#01H8ET45XC4RZ8ZTJAQSCQM39E): Select and edit prototyping interactions on matching objects in bulk

In order for two objects to be considered matching, they must:

- [Match layer names](https://help.figma.com/hc/en-us/articles/21523793229463-Identify-matching-objects#h_01HQ9AJBJPP79AP6V2ATX46YX8)
- [Match parent frames](https://help.figma.com/hc/en-us/articles/21523793229463-Identify-matching-objects#h_01HQ9EWGM67H5SVJ9615K2777X)
- [Match layer hierarchy](https://help.figma.com/hc/en-us/articles/21523793229463-Identify-matching-objects#h_01HQ9F7DQK9B1W0MAV024T89EZ)

## Matching object requirements

Figma uses the following terms to help define matching object requirements:

- **Parent objects**: Objects such as frames, components, and groups, that contain other objects.
  - **Grandparent objects** are objects that contain the parent object. **Ancestors** are any other objects in the hierarchy that contain child, parent, or grandparent objects.
- **Children**, or **child objects**: Objects that are contained within a parent.
- **Top-level frames**: Frames placed directly on the canvas. They do not have any parent objects.

[Learn more about parent, child and sibling relationships.](https://help.figma.com/hc/en-us/articles/360039959014-Parent-child-and-sibling-relationships)

Note: Top-level frames can be matching objects, but only for [smart animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames) or [state management](https://help.figma.com/hc/en-us/articles/14397859494295-State-management-for-prototypes). You cannot use [multi-edit](https://help.figma.com/hc/en-us/articles/21635177948567/) or [select matching interactions](https://help.figma.com/hc/en-us/articles/360040315773-Create-interactions#01H8ET45XC4RZ8ZTJAQSCQM39E) on top-level frames.

Objects in [sections](https://help.figma.com/hc/en-us/articles/9771500257687-Organize-your-canvas-with-sections) can only match with other objects within that section.

### Layer names

Objects must have the same layer name.

There is one exception to this rule:

Text layers

Text layers don’t always require identical layer names. When you create a text layer, the name of the layer will reflect the content of the text itself. You have the option to rename the text layer.

- If the text layers were explicitly [named or renamed from the Layers panel](https://help.figma.com/hc/en-us/articles/360039958934-Rename-Layers), the names must match.
- If the text layers were implicitly named based on the text content, their [text styles](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties) must match. If there are multiple matching text objects, the best match will be selected based on the x and y coordinates of the text layer in the frame.

![In the first example, there is a frame with a rectangle object named 'rectangle'. A second frame has a rectangle object also named 'rectangle', so the two rectangle objects match. In the second example, there is a frame with a rectangle object name 'rectangle'. A second frame has a rectangle object named 'shape'. The two rectangle objects do not match.](https://help.figma.com/hc/article_attachments/21553062244503)

### Parent frames

All parent and ancestor frames of the objects must have matching names. The names of top-level frames do not need to match.

![In the first example, there is an object that sits in a parent frame named 'parent'. A second object also has an object that sits in a parent frame named 'parent'. The objects match. In the second example, there is an object that sits in a parent frame named 'parent'. A second object also sits in a parent frame that is named 'mother'. The objects do not match.](https://help.figma.com/hc/article_attachments/21556646112023)

Note: Top-level frames and variant names in a component set do not need to match.

### Layer hierarchy

In order to be considered matching, objects must have the same position in layer hierarchy across top-level frames. For example, an object that has a parent and grandparent layer in one frame must also have a parent and grandparent layer in the second frame.

![In the first example, there is a top-level frame that contains a parent frame and a child object. A second frame also has a top-level frame that contains a parent frame and a child object. The objects match. In the second example, there is a top-level frame that contains a parent frame and a child object. A second frame has a top-level frame, a grandparent frame, a parent frame, and a child object. The objects do not match.](https://help.figma.com/hc/article_attachments/21554441367959)

**Tip**: When all requirements match, and there are two or more objects with the same name in a frame, the index of the object within the parent frame is used to determine which one matches.

![Two identical frames, each with two objects. Object A matches with Object B in the second frame. Even though Object A visually appears above Object B, they have the same index from the left Layer panel.](https://help.figma.com/hc/article_attachments/21556673438231)

## Identify matching objects

To highlight matching objects on the same page:

1. Click to select an object.
2. Hold `Shift` to highlight all matching objects in light blue.

Alternatively, you can identify matching objects from the **Prototype** tab.

1. Open the **Prototype** tab in the right sidebar.
2. Hover over an object or layer in the canvas.

Figma will highlight the matching object in any other frames it exists in.
