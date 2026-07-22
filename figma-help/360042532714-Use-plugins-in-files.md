---
기술지원명: Use plugins in files
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Use plugins in files
출처링크: https://help.figma.com/hc/en-us/articles/360042532714-Use-plugins-in-files
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Any user on a Starter plan or with a paid seat
[in an organization or enterprise](https://help.figma.com/hc/en-us/articles/360040328273)
can access the plugins feature

Organization admins can limit usage to only classic plugins that
have been
[approved by the organization](https://help.figma.com/hc/en-us/articles/360039958894)

Plugins are third-party scripts or applications that extend the functionality of Figma's products. Use plugins to customize your experience or create more efficient workflows in Figma Design, Dev Mode, FigJam, Figma Slides, and Figma Buzz.

The types of files you can run plugins in depends on your plan and seat.

|  | **Starter** | **Full** | **Dev** | **Collab** | **View** |
| --- | --- | --- | --- | --- | --- |
| **Figma Design** | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Dev Mode** | ❌ | ✅ | ✅ | ❌ | ❌ |
| **FigJam** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Figma Slides** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Figma Buzz** | ✅ | ✅ | ✅ | ❌ | ❌ |

Find plugins and other resources on the [Figma Community](https://help.figma.com/hc/en-us/articles/360038510693).

Note: You can save frequently used plugins so that you can more easily access them when moving between files. Figma links any plugins you save to your Figma account. If you’ve added [profile connections](https://help.figma.com/hc/en-us/articles/1500005162381), saving a plugin also saves the plugin on your connected accounts. Learn more about [saving plugins →](https://help.figma.com/hc/en-us/articles/360052033434-Community-follows-and-likes)

## Run plugins

You can run a plugin from the Community, the file browser, or directly from a file in Figma Design, Dev Mode, FigJam, Figma Slides, or Figma Buzz.

Instructions for use vary between plugins. Some plugins perform an action on the canvas or board immediately. Others require you to adjust inputs or settings before performing an action. You may need to select frames, objects, or layers before running the plugin. Test run the plugin or check the plugin listing to know what selections they support.

You should also keep in mind:

- You have to manually run plugins
- You can only run one plugin at a time
- Plugins can’t perform actions in the background
- You can't see what plugins another user has run in a file
- Paid plugins badged with “In-app purchases” include a [time or usage-based free trial](https://help.figma.com/hc/en-us/articles/11786473291159#Preview_a_paid_resource)

**Note:** Licensing terms for plugins vary depending on if the plugin is free or paid. Learn more about [Figma's copyright and licensing](https://help.figma.com/hc/en-us/articles/360042296374).

### Run plugins from the Figma Community

1. From the plugin’s Community page, click **Open in** or **Buy** (paid plugins). Paid plugins labeled with “in-app purchases” include a [time or usage-based free trial](https://help.figma.com/hc/en-us/articles/11786473291159#Preview_a_paid_resource).
2. Select a recent file to open the plugin in or click **New file**. If the plugin's creator included a playground file in the plugin's listing, the option to open a new file does not display.
3. If prompted, select where you’d like to open the plugin.

You will be redirected to a file where you can try out the plugin.

### Run plugins from Figma Design

1. From a design file, click the **Tools** tab in the navigation bar on the left.
2. Click the **Filter by price and type** icon and filter by **Plugin**.
3. Select from your recents, suggested, or use the search bar at the top to browse more plugins from the Community. You can also use the **Source** and **Category** dropdowns to narrow your search.
4. Click on a plugin open the details modal.
5. Click **Run** to run the plugin.

### Run plugins while in Dev Mode

1. Click **Plugins** in the right sidebar.
2. Select from your recently used or saved plugins, or search for a plugin from the Community.
3. Click on a plugin to run it.

![Plugins panel in Figma with sections for recent, saved, and community plugins, highlighting plugin selection and management options.](https://help.figma.com/hc/article_attachments/24146048593431)

### Pin plugins while in Dev Mode

You can pin frequently used plugins to the top of the right sidebar for easy access.

1. From the **Plugins** tab, find the plugin you want to pin.
2. Click the  **More** menu and select **Pin to top**.
3. To unpin a plugin, click the  **More** menu and select **Unpin from top**.

Note: If you are in an organization, plugins in Dev Mode that are pinned for your organization also appear with your pinned plugins. You can unpin plugins from your organization as normal.

![Plugin panel within Dev Mode right sidebar showing "Typer - Codes" with options to view details, pin to top, or run automatically, highlighting "Pin to top."](https://help.figma.com/hc/article_attachments/24146457839895)

### Run plugins from FigJam

1. Hover over the pile of recently used icons in the toolbar.
2. Click **More**.
3. From the **Plugins** tab, select from your recently used plugins or click **Browse more in Community** to be redirected to the Community.
4. Click on a plugin to view its details.
5. Click **Run** to run the plugin in the current board.

![Plugins panel in FigJam with a search bar, showcasing recent plugins like html.to.design, FlyOver, and Stark with "Run" buttons.](https://help.figma.com/hc/article_attachments/14314492135959)

### Run plugins from Figma Slides

1. Click / **Actions** in the toolbar.
2. From the **Plugins** tab, select from your recently used or saved plugins or search for a plugin from the Community.
3. Click on a plugin to run it.

![Plugins panel selected from the actions menu in Figma Buzz showing search results for integrating and enhancing Figma workflows with plugin options and usage stats.](https://help.figma.com/hc/article_attachments/30241069264535)

### Run plugins from Figma Buzz

1. Open a file in Figma Buzz.
2. In the left panel, click the  **Plugins** tab.
3. Browse, search, or select from your recently used or saved plugins.
4. Click on a plugin to run it. The plugin will open directly in the left panel, or you can select to **Open in a modal**.

Tip: You can also run a plugin by right-clicking an asset and selecting **Plugins** from the context menu.

![The plugins icon from the left sidebar is selected within Figma Buzz. A sidebar is open where the user can browse and search through available plugins.](https://help.figma.com/hc/article_attachments/35833777887767)

## Plugin security

Plugins run third-party code and can access user and file information for their plugin actions.

Information that plugins can access includes:

- Usernames
- User IDs
- User avatars
- Cursor position in a file
- The bounds of the editor that is visible on-screen
- The ID of a selected object
- All layers that exist in a file

When you're interacting with a plugin, Figma displays a toast notification at the bottom of the file while the plugin is running. If the plugin uses an iFrame, Figma will display the plugin's name and icon ‌at the top of the iFrame.

Figma is not responsible for performance-related issues of any plugin. If you experience performance issues or spot a bug in a specific plugin, [reach out to the plugin's support contact](https://help.figma.com/hc/en-us/articles/360043031473).

### Data security info

Plugin developers can voluntarily complete a [security disclosure form](https://help.figma.com/hc/en-us/articles/16354660649495) for their plugin. When the security disclosure is reviewed and accepted by Figma, the **Data security info available** label appears in the Community entry for the plugin. Click the label to review the answers that the developer provided for the security disclosure. Only logged-in users can view the answers.

![Data security self-assessment form showing plugin compliance with Figma's data security practices, including network requests.](https://help.figma.com/hc/article_attachments/17444559876759)

### Network access

Plugin developers can voluntarily [specify the domains](https://www.figma.com/plugin-docs/making-network-requests) that their plugins will access. A plugin’s Community page includes the scope of network access for that plugin. By default, a plugin can access any domain.

The network access scope is indicated by one of the following labels.

|  |  |
| --- | --- |
| Label | Description |
| Label indicating unknown network access for a Figma plugin, expandable for more details. | **Unknown network access:** Network access isn’t defined in the plugin’s manifest.json. The plugin can access any domain. |
| Icon indicating a plugin with unrestricted network access, allowing it to reach any domain, with an option to view developer rationale. | **Unrestricted network access:** The plugin can access any domain. A reasoning is provided by the developer. |
| Label indicating a Figma plugin with restricted network access, expandable for more details on the allowed domains. | **Restricted network access:** The plugin can access only a specific set of domains. |
| "No network access" label indicating a plugin cannot access any domains, with a dropdown option for details. | **No access to network:** The plugin cannot access any domains. Optionally, a developer may provide a reasoning. |

When network access is unrestricted, click **Unrestricted network access** to see the developer’s reasoning.

When network access is restricted, click **Restricted network access** to see a list of the domains that the plugin is permitted to access. If the developer specified a reasoning, the reasoning is also included. This is useful for users who want to understand a plugin’s access scope before [approving that plugin for use](https://help.figma.com/hc/en-us/articles/4404228724759-Approve-plugins-in-an-organization).

The enforcement of network access is limited only to requests made by the plugin, such as requests to a public API. In a situation such as a plugin rendering a website in a frame, network access limits only apply to the website's domain. Network access limits don’t affect the website’s resources.

For example, suppose a plugin is restricted to only `figma.com` and shows that page in Figma. The plugin would be prevented from loading other sites, `figma.com` itself would still be able to load external resources needed to effectively run their website, such as scripts for Google Analytics.

## Contact plugin developers

Figma does not provide support for third-party plugins. If you have issues with a plugin, we recommend reaching out to the developer.

Every plugin developer must provide a support contact. This can be an email address, a website, or a link to a help center. You can find this information on the plugin’s Community resource page.

## Report a plugin

Report plugins that are inappropriate, or look suspicious, to the Figma team.

1. Open the plugin’s Community page. Click the **Report resource** link on the right-hand side.
2. Fill out the form that displays.
3. Click **Send**.

## Use plugins in files shortcuts

Use the table below to see the keyboard shortcuts and quick actions available for using plugins in files.

Note: Individual plugins may support quick actions specific to using that plugin. Review the plugin’s documentation to see which quick actions are supported.

|  |  |  |  |
| --- | --- | --- | --- |
| **Shortcut** | **Mac** | **Windows** | [**Quick action**](https://help.figma.com/hc/en-us/articles/360040328653-Use-shortcuts-and-quick-actions) |
| Find more plugins | x | x | ✓ |
| Run last plugin | `Command` `Option` `P` | `Alt` `Control` `P` | ✓ |
