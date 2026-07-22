---
기술지원명: Debug view in Figma
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Debug view in Figma
출처링크: https://help.figma.com/hc/en-us/articles/35340652461079-Debug-view-in-Figma
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

When [working with the Figma Support team](https://help.figma.com/hc/en-us/articles/360041057214) on a performance issue or troubleshooting a potential bug, we may request to enable Debug view on your behalf.

Debug view is an internal tool used by Figma Support and product engineers, and helps the teams collect technical information about how Figma is running in your browser or desktop app. With this additional information, our team can identify the cause of slowdowns, freezes, or unusual behavior to more quickly to find solutions.

Note: Debug view does not collect or change the content of your designs. It only gathers technical data about performance, environment, and system behavior.

## How Debug view works

- Collects extra diagnostic data about your Figma session while you use the product.
- Monitors performance at a deeper level, including the health of your network and the way your browser or desktop app runs Figma.
- Runs temporarily for a short period of time, usually a few business days, while we investigate your issue.

Figma Support will ask for your permission to enable Debug view. It is always temporary and will automatically expire after 7 days, if not turned off sooner by the Figma Support team member troubleshooting your issue.

There may be a small, marginal performance hit while Debug view is running. Most users will not notice a difference, but some actions may take slightly longer.

## Information collected

Debug view captures data about:

**Your Figma usage**

- Actions you take in files like selecting, editing, and scrolling
- Performance details of those actions (how long things take to load or respond)
- Pages you load outside of files, such as the Figma home screen, community, or settings
- Navigation patterns (which views or screens are opened and in what order)

**The files you interact with**

- File size, structure, and complexity
- How the file is performing (render times, memory use)

**Your environment**

- Browser or desktop app version
- Operating system details
- Device specs (CPU, memory, screen resolution)
- Network connection quality (latency, bandwidth, errors)
- Geographic region of your connection

**App performance**

- JavaScript performance profiles (timing information about how Figma code executes)
- Errors and stack traces from the app
- Resource usage data (CPU, memory, graphics)
- Network requests (e.g. API calls, assets like images or fonts being loaded)
- Slow operations (tasks blocking the app for long enough to cause visible lag)

## Data Retention

We only keep this data long enough to investigate your issue. After that, it’s automatically deleted.

## Privacy and Security

- Debug view does not collect your designs, text content, or personal files.
- The data is used only for troubleshooting and is not shared with third parties.
- Once Debug view is turned off, no further debug level data is collected.
