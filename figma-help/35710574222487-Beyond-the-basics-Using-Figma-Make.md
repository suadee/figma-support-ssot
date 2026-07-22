---
기술지원명: Beyond the basics: Using Figma Make
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Beyond the basics: Using Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/35710574222487-Beyond-the-basics-Using-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

You've made your first prompt and now you're ready for what's next. Here are some common use cases and needs that follow the initial generation of your app or functional prototype.

- [Support multiple users](#h_01K7SJRJ311QYGV021ZMHADCAN)
- [Move to Figma Design](#h_01K7SKTZNV55CE6ETAD6NK6GPT)
- [Share your work](#h_01K7SM9G7ET7Q2YTKDZ94CHXRW)
- [Get your code](#h_01K7SN0F7PDQ1B124HA08ZDQYQ)
- [Explain the code](#h_01K7T12Z46DZK1Y5951667PQAW)
- [Plan before changes](#h_01K7T0EFMGM3B4F0ER5STNXW0Q)

## Support multiple users

Many apps will need to support multiple users. For example:

- An app that lets users fill out and share tournament brackets
- A social media app where users log in, have profiles, and post
- A game that has a global leaderboard or some multiplayer functionality

In all these cases, you'll use Supabase to provide a backend for your app that lets users log in and stores data such as accounts, posts, scores, or other content.

### Example prompt

```
I want my app to support multiple users. Use Supabase to provide a way for users to create and log in to accounts. Implement the appropriate backend per-user functionality.
```

### Try it out in this Community file

To try the example prompt, [remix this community file](https://www.figma.com/community/file/1565044743188735435/example-app-markdown-notes) and paste the prompt into the AI chat. You can modify the prompt to experiment with additional functionality.

**Example app: Markdown Notes**

[Community file](https://www.figma.com/community/file/1565044743188735435/example-app-markdown-notes)

### Why this works

The example prompt explains clearly to Figma Make that you want to add a backend to support multiple users. The prompt triggers the Supabase backend flow. Because of the wording, Figma Make considers the context of your existing conversation and builds appropriate backend support for the app you're working on.

---

## Move to Figma Design

Your app is in a state you want to bring to Figma Design. In this case, you'll use the **Copy design** feature. In the preview of your app, get to the view you want to copy, then follow the instructions in [Copy a Figma Make preview as design layers](https://help.figma.com/hc/en-us/articles/35060759685015-Copy-a-Figma-Make-preview-as-design-layers#h_01K5W3WKETKGKPA18EZ8CAWFHR).

Currently, you can't get a functional version of your Figma Make file in Figma Design, and changes you make to layers in Figma Design aren't applied back to your Figma Make file.

### Try it out in this Community file

To test out the **Copy design** feature, [remix this community file](https://www.figma.com/community/file/1565046759883561444). You can add elements to the canvas, move layers, and expand the canvas to fill the view. Try the **Copy design** feature with different canvas states and paste the layers into Figma Design to see the result.

**Example app: Canvas Editor**

[Community file](https://www.figma.com/community/file/1565046759883561444)

### Why this works

When you use the **Copy design** feature, it copies the current state of the preview in your Figma Make file. That means you go to different parts of your app, such as expanding a menu or opening an overlay, and then copy that state of the preview to Figma Design as layers you can edit.

---

## Share your work

You're ready to share the work you've done in Figma Make. There are several different approaches to sharing based on your need:

- **Share the entire Figma Make file:** If you want to invite your teammates to see your chat history and collaborate with you, you can [share the Figma Make file itself](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes).
- **Let others iterate using your work:** If you want to enable your teammates to iterate in a way that doesn't impact your original file, you can [publish the Figma Make file as a template](https://help.figma.com/hc/en-us/articles/34716344138519-Create-and-update-a-template-in-Figma-Make).
- **Show a working version internally:** If you want to hide the chat history and provide the functional experience of your app or functional prototype to a limited number of people, you can [publish a password-protected version of your app](https://help.figma.com/hc/en-us/articles/31304586129559-Publish-update-or-unpublish-a-functional-prototype-or-web-app#h_01K34TMRX527Z7YXY0D7ZKHWT8), or [publish it only to your organization](https://help.figma.com/hc/en-us/articles/31304586129559-Publish-update-or-unpublish-a-functional-prototype-or-web-app#h_01K57T19EN44C2DAFKJ4M658PX).
- **Share your work on the internet:** If you're ready to share the outcome of your work with everyone, you can [publish your app to the live web](https://help.figma.com/hc/en-us/articles/31304586129559-Publish-update-or-unpublish-a-functional-prototype-or-web-app#h_01JTEZTMFFJC4AKM0AKS59T4BF).

---

## Get your code

In some cases, you may want to get your code into editors or systems outside of Figma, such as moving the code into a GitHub repository, or modifying the code in VS Code or another IDE.

There are two approaches to obtaining your code:

- **In the code editor for your Figma Make file, download the code:** When you [download code from Figma Make](https://help.figma.com/hc/en-us/articles/33649966245783-Edit-the-code-of-a-functional-prototype-or-web-app#h_01K0T5XKHB9QW7Z185TPZ1VT9V), the product creates a .zip file that contains the code for your app. You can download the .zip file and pull the contents into the IDE you prefer. Changes you make to the code can't automatically be pushed back to Figma Make, though you can manually copy and paste your changes into the interface, or share the changes in the AI chat.
- **Push the code to GitHub:** All users of Figma Make can [push code to GitHub](https://help.figma.com/hc/en-us/articles/35463818346647-Push-from-Figma-Make-to-GitHub). When you use this feature, Figma Make creates a GitHub repository in your GitHub account or organization that corresponds to the Figma Make file you're in. Then you can push the changes from Figma Make to that repository as you continue to work.

---

## Explain the code

Sometimes you want to better understand what the code of your app is doing. You can prompt Figma Make to explain the code without making any actual changes to your app.

### Example prompt

```
Explain the code of this app to me. Start at a high level.
```

### Try it out in this Community file

[Remix this community file](https://www.figma.com/community/file/1565047453992750572) and try the example prompt to get an explanation of the code in the Figma Make file.

**Example app: Tetromino Game**

[Community file](https://www.figma.com/community/file/1565047453992750572)

### Example result

```
Tetromino Game - Code Explanation

High-Level Architecture

This is a classic Tetris-style game built with React and TypeScript. The app follows a component-based architecture with three main parts:

1. Component Structure
`App.tsx` - The main game controller containing all game logic and state
`GameBoard.tsx` - Visual component that renders the 10x20 playing field
`NextPiece.tsx` - Preview component showing the upcoming tetromino
`types.ts` - TypeScript interfaces for type safety

2. Core Game Concepts

The game manages several key pieces of state:
Board State: A 20x10 grid of cells, each either empty or filled with a colored block
Current Piece: The active falling tetromino with its shape, color, and position
Next Piece: Preview of what's coming next
Game Stats: Score, level, lines cleared
Game Status: Playing, paused, or game over

3. Game Loop Flow

```
Start Game
    ↓
Spawn New Piece
    ↓
Move Down (every X ms based on level)
    ↓
Check Collision
    ↓
If collision → Merge piece to board → Clear completed lines → Spawn new piece
If no collision → Continue moving
    ↓
Repeat
```

---

Detailed Breakdown

App.tsx - The Game Engine

Constants & Data
TETROMINOES array: Defines all 7 classic shapes (I, O, T, S, Z, J, L) with their rotation matrices and colors
BOARD_WIDTH/HEIGHT: 10 columns × 20 rows

Key State Variables
```typescript
board              // 2D array of cells
currentPiece       // Active tetromino shape
currentPosition    // {x, y} coordinates
nextPiece          // Preview piece
score, level, linesCleared
isPlaying, isGameOver
```

Core Functions

1. Collision Detection (`checkCollision`)
Tests if a piece at a given position would overlap with:
Board boundaries (left, right, bottom)
Already-placed blocks

2. Piece Movement (`moveLeft`, `moveRight`, `moveDown`)
Attempts to move piece in direction
Only updates position if no collision detected

3. Rotation (`rotate`)
Transposes the shape matrix and reverses rows (90° clockwise)
Only rotates if the new orientation doesn't collide

4. Merge & Clear (`mergePieceToBoard`, `clearLines`)
When piece lands, it's permanently added to the board
`clearLines` checks for complete rows (all 10 cells filled)
Removes completed lines and adds empty rows at top
Scoring: 1 line = 100pts, 2 = 300pts, 3 = 500pts, 4 = 800pts (multiplied by level)

5. Hard Drop (`hardDrop`)
Instantly drops piece to lowest valid position
Useful for fast gameplay

Game Loop (useEffect)
```typescript
setInterval(() => moveDown(), speed)
// Speed decreases as level increases
// Clears interval when paused/game over
```

Keyboard Controls (useEffect)
Arrow keys for movement
Space/Up arrow for rotation
Enter for hard drop

---

GameBoard.tsx - The Display

This component is purely visual:

Takes props: Current board state + active piece
Combines them: Creates a temporary display board by overlaying the active piece onto the static board
Renders grid: Uses CSS Grid with 30px cells
Styling: Each cell shows its color if filled, dark gray if empty

```typescript
// Pseudo-code
displayBoard = [...board]
Overlay currentPiece onto displayBoard at its position
Render 200 cells (10×20) with appropriate colors
```

---

NextPiece.tsx - The Preview

Simple 4×4 grid showing the next tetromino:
Smaller cells (20px vs 30px)
Centers the piece shape within the grid
Same color-coding as the main board

---

types.ts - Type Definitions

```typescript
Block: { filled: boolean, color: string }  // Single cell
Tetromino: { shape: number[][], color: string }  // Piece definition
Position: { x: number, y: number }  // Coordinates
```

---

Key Design Decisions

Immutable State Updates: Always creates new arrays/objects rather than mutating
Callback Hooks: Uses `useCallback` to prevent unnecessary re-renders
Separation of Concerns: Display components don't contain logic
Game Loop via setInterval: Simple time-based piece dropping
Level Progression: Every 10 lines increases level and speeds up the game

The architecture is clean and maintainable - game logic lives in App.tsx while rendering is delegated to specialized components!
```

### Why this works

Figma Make is able to read the code files it creates or edits. When prompted to explain the code of an app, Figma Make is able to summarize the contents of the code files, as well as give detailed explanations of how the code works.

---

## Plan before changes

When you're dealing with issues in your app, such as Figma Make adding debug functionality into the code or trying to execute large, complex changes, you may want to instruct Figma Make to plan the changes first.

### Example prompt

First prompt:

```
Don't make any changes to the code of the app. Create a file called plan.md. In plan.md, write down a plan to implement the changes I want to make.
```

Second prompt:

```
Use the latest version of the plan in plan.md to make changes to the app.
```

### Try it out in this Community file

[Remix this community file](https://www.figma.com/community/file/1565048634745156091) and send the first prompt in the AI chat with some specific changes for Figma Make to implement. For example, tell Figma Make that you want to add the ability to save and import tournament brackets.

Then, in the code editor, experiment by making changes to the `plan.md` file that Figma Make creates.

Finally, send the second prompt in the AI chat to have Figma Make implement the changes detailed in the `plan.md` file.

**Example app: Tournament Brackets**

[Community file](https://www.figma.com/community/file/1565048634745156091)

### Why this works

Figma Make is able to make specific files when you instruct it to do so. The `plan.md` file will contain a plan that Figma Make can execute in order to make complex changes to your app. The advantage of creating the `plan.md` file before Figma Make executes the changes is that you can validate the plan in the code editor, and make your own changes or additions to the plan.

The subsequent prompt then instructs Figma Make to use the plan, including any changes you've made.
