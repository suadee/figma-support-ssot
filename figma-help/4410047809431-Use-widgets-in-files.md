---
기술지원명: Use widgets in files
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Use widgets in files
출처링크: https://help.figma.com/hc/en-us/articles/4410047809431-Use-widgets-in-files
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only people with `can edit` access to the file can interact with widgets, including visitors in [open sessions](https://help.figma.com/hc/en-us/articles/4410786053911). This is because it's possible for widgets to edit or interact with other layers and objects in the file.

If you are in an organization, you can run widgets [approved by your organization](https://help.figma.com/hc/en-us/articles/360039958894).

Widgets are custom objects that you can add to the Figma editor or FigJam board. They allow you to level up your sessions with different tools, data from external applications, or new ways to play.

Unlike plugins which are only visible to individuals, widgets are objects that everyone in the file can see. You'll need to have `can edit` access to a file to add or use a widget. You can add as many widgets as you want and reposition them like any other object.

Find widgets and other resources on the [Figma Community](https://help.figma.com/hc/en-us/articles/360038510693-Guide-to-the-Figma-Community).

Note: You can save frequently used widgets so that you can more easily access them when moving between files. Figma links any widgets you save to your Figma account. If you’ve added [profile connections](https://help.figma.com/hc/en-us/articles/4404285788183), saving a widget also saves the widget on your connected accounts. Learn more about [saving widgets →](https://help.figma.com/hc/en-us/articles/360052033434-Community-follows-and-likes)

## Add widgets

You can add a widget from the Community, the file browser, or directly from a file in Figma or FigJam. You need to have `can edit` access to the file where you want to add a widget.

Note: Licensing terms for Community files vary depending on if the widget is free or paid. Learn more about [Figma's copyright and licensing →](https://help.figma.com/hc/en-us/articles/360042296374)

### Add widgets from the Figma Community

1. From the widget's Community page, click **Open in** or **Buy** (paid widgets). Paid widgets badged with “in-app purchases” include a [time or usage-based free trial](https://help.figma.com/hc/en-us/articles/11786473291159#Preview_a_paid_resource).
2. Select a recent file to open the widget in or click **New file**. If the widget’s creator included a playground file in the widget's listing, the option to open a new file does not display.
3. If prompted, select where you’d like to open the widget.

You will be redirected to a file where you can try out the widget. To use the widget in a different file:

- **Figma Design:** Click  **Actions** in the toolbar, navigate to the **Plugins & Widgets** tab, and select the widget under **Recents**.
- **FigJam:** Click **More** in the pile of recently used icons in the toolbar, navigate to the **Widgets** tab, and select the widget under **Recents**.

### Add widgets from the file browser

1. From the file browser, click  **Templates and tools** in the left sidebar.
2. Select a widget from **Community** or your internal team’s tab.
3. Click **Open in** and select a recent file to open the widget in or click **New file.** If the widget’s creator included a playground file in the widget's listing, the option to open a new file does not display.
4. If prompted, select where you’d like to open the widget.

You will be redirected to a file where you can try out the widget.

### Add widgets from Figma Design

1. Click  **Actions** in the toolbar.
2. From the **Plugins & Widgets** tab, select from your recently used or saved widgets or search for a widget from the Community.
3. Click on a widget to view its details.
4. Click **Run** to add the widget to the current file.

![Widget selection panel in Figma, showing options like Photo Booth and Alignment Scale under Plugins & Widgets tab.](https://help.figma.com/hc/article_attachments/24294287297559)

### Add widgets from FigJam

1. Hover over the pile of recently used icons in the toolbar.
2. Click **More**.
3. From the **Widgets** tab, select from your recently used widgets or click **Browse more in Community** to be redirected to the Community.
4. Click on a widget's name to view its details.
5. Click **Add** to add the widget to the current board.

![Figma screen showing a Widgets panel with options like 'lil poll' and 'Giphy Stickers' under Recents and saved.](https://help.figma.com/hc/article_attachments/24294135572503)

## Remove widgets

To remove all widgets from a file:

1. Right-click the board or canvas, or open the file menu.
2. Hover over **Widgets**.
3. Click **Select all widgets**.
4. Press `Delete` (Mac) or `Backspace` (Windows).

## Update widgets

When a widget’s creator publishes a new version, the widget’s Community page is updated to that version. Widgets that have been added to files are not automatically updated to protect any information stored in the widgets.

To check and see if a widget has an available update:

1. Right-click on the widget.
2. Hover over **Widgets** at the bottom of the menu.
3. If there is an update available, select **Update to latest version**.

Figma will replace the widget with the latest version and copy over any information from the previous version.

If this breaks your widget or deletes any data, you can undo the update using the shortcut:

- **Mac:** `⌘ Command` `Z`
- **Windows:** `Ctrl` `Z`

### View the version history of a widget

Widget developers can add a description of their changes when they publish updates. You can use this information to decide if you want to update the widget.

To view any widget updates:

1. Right-click on the widget.
2. Select **Widgets > View widget details**.
3. Click **See more details in Community** to open the widget's Community page.
4. Scroll down to view any **Version history**.

If you have any questions for the developer, you can [leave a comment](https://help.figma.com/hc/en-us/articles/1500002628062#add-general) using the **Add a comment** field.

## Widget security and performance

Widgets run third-party code and can open iFrames—inline windows that allow widgets to run HTML and JS code, or access external APIs, websites, and resources.

Figma will let you know when you’re interacting with a widget:

- View a widget’s name when you select it on the board
- View a widget’s name and icon at the top of any iFrames

![Widget object and iFrame side by side, demonstrating visual interface components within Figma.](https://help.figma.com/hc/article_attachments/24294135611415)

Widgets can also access information about the file and any users in that file:

- All layers and objects that are in the file
- The username, ID, and avatar of any users in the file
- Current cursor position of file participants
- Current viewport—the area of the canvas or board that is visible on screen
- The ID of selected layers or objects

### Data security info

Widget developers can voluntarily complete a [security disclosure form](https://help.figma.com/hc/en-us/articles/16354660649495) for their widget. When the security disclosure is reviewed and accepted by Figma, the **Data security info available** label appears in the Community entry for the widget. Click the label to review the answers that the developer provided for the security disclosure. Only logged-in users can view the answers.

![Widget data security disclosure for Figma, including network request and authentication details.](https://help.figma.com/hc/article_attachments/17444591387287)

### Network access

Widget developers can voluntarily [specify the domains](https://www.figma.com/widget-docs/making-network-requests) that their widgets access. A widget’s Community page includes the scope of network access for that widget. By default, a widget can access any domain.

The network access scope is indicated by one of the following labels.

|  |  |
| --- | --- |
| Label | Description |
| Label indicating unknown network access for a widget with an expandable option to view details. | **Unknown network access:** Network access isn’t defined in the widget's manifest.json. The widget can access any domain. |
| Icon indicating unrestricted network access with a dropdown arrow for more details. | **Unrestricted network access:** The widget can access any domain. A reasoning is provided by the developer. |
| Text label showing "Restricted network access" with a globe icon indicating widget's limited domain permissions. | **Restricted network access:** The widget can access only a specific set of domains. |
| Widget label displaying "No network access" with dropdown, indicating restricted domain connectivity for security purposes. | **No access to network:** The widget cannot access any domains. Optionally, a developer may provide a reasoning. |

When network access is unrestricted, click **Unrestricted network access** to see the developer’s reasoning.

When network access is restricted, click **Restricted network access** to see a list of the domains that the widget is permitted to access. If the developer specified a reasoning, the reasoning is also included. This is useful for users who want to understand a widget’s access scope before [approving that widget for use](#h_01H00NBBV6489DBJY6M1SY4HWG).

The enforcement of network access is limited only to requests made by the widget, such as requests to a public API. In a situation such as a widget rendering a website in a frame, network access limits only apply to the website's domain. Network access limits don’t affect the website’s resources.

For example, suppose a widget is restricted to only `figma.com` and shows that page in Figma. The widget would be prevented from loading other sites, `figma.com` itself would still be able to load external resources needed to effectively run their website, such as scripts for Google Analytics.

## Approve organization widgets

If you are in an organization, you can restrict widget use to approved widgets only. When enabled, members can only install and run widgets that organization admins approve. [Approve organization widgets →](https://help.figma.com/hc/en-us/articles/4420945686807)

## Get help with widgets

Figma does not provide support for third-party applications, including widgets.

If you have questions about a widget or need help with an issue, we recommend reaching out to the developer. You can find the contact information on the widget’s Community page.

**Interested in making widgets?** Figma's [widget API](https://www.figma.com/plugin-docs/intro/) supports both read and write functions, allowing you to view and edit existing layers as well as create new ones. [Make widgets for the Figma Community](https://help.figma.com/hc/en-us/articles/4410596533143) →

## Use widgets in files shortcuts

Use the table below to see the keyboard shortcuts and quick actions available for using widgets in files.

|  |  |  |  |
| --- | --- | --- | --- |
| **Shortcut** | **Mac** | **Windows** | [**Quick action**](https://help.figma.com/hc/en-us/articles/360040328653-Use-shortcuts-and-quick-actions) |
| Find more widgets | x | x | ✓ |
| Select all widgets | x | x | ✓ |
