---
기술지원명: View and explore library analytics
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: View and explore library analytics
출처링크: https://help.figma.com/hc/en-us/articles/360039238353-View-and-explore-library-analytics
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan).

Any member of an organization can view library analytics as long as they have `can view` or `can edit` access to the library file.

Guests don’t have access to library analytics.

With library analytics, you can get a holistic view of how your design systems are being adopted in your organization and teams. Use library analytics to track and compare usage of your [published libraries](https://help.figma.com/hc/en-us/articles/360041051154), [components](https://help.figma.com/hc/en-us/articles/360038662654), [styles](https://help.figma.com/hc/en-us/articles/360039238753), and [variables](https://help.figma.com/hc/en-us/articles/15339657135383). Leverage the findings to guide decisions about design system improvements and what components, styles, and variables may be ready for deprecation.

**Note**: Library analytics update daily, and Figma tracks up to one year of library analytics data prior to the current day. Styles and variables tracking started on October 10, 2024.

## View library analytics

### For all libraries within the organization

View a summary of the total number of teams, libraries, components, styles, and variables in your organization in one place. This analytics modal for your organization can be accessed from the file browser:

Organization and Enterprise plan Enterprise plan with workspaces

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **All teams**.
2. Click **Libraries** to open the analytics modal.

![Library analytics modal showing team and library statistics, search field, total counts, and insertion data for design assets.](https://help.figma.com/hc/article_attachments/29908838670231)

From the library modal you can:

- A  Use the **Search** field to find a specific library.
- B  View a summary of analytics across all libraries:

  - **Total teams:** The total number of teams in the organization. This includes [open, closed, and secret teams](https://help.figma.com/hc/en-us/articles/360040452973).
  - **Teams with libraries:** The number of teams in the organization using libraries.
  - **Total libraries:** The total number of libraries in your organization. This includes libraries shared across the entire organization, or within a specific team.
  - **Total components:** The total number of main components across libraries.
  - **Total styles:** The total number of styles across libraries.
- C  View a list of all libraries shared within teams or across the organization. For each library you can view:

  - **# of components:** The total number of main components in that library.
  - **# of styles:** The total number of styles in that library.
  - **Inserts last week:** The number of times a component from the library was inserted into a file.
- D  Select a library to view its analytics.

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **All workspaces**.
2. Click **Libraries** to open the analytics modal.

![Library analytics panel showing total teams, libraries, components, styles, and variables with specific library details.](https://help.figma.com/hc/article_attachments/29908838673943)

From the library modal you can:

- A  Use the **S****earch** field to find a specific library.
- B  View a summary of analytics across all libraries:

  - **Total teams:** The total number of teams in the organization. This includes [open, closed, and secret teams](https://help.figma.com/hc/en-us/articles/360040452973).
  - **Teams with libraries:** The number of teams in the organization using libraries.
  - **Total libraries:** The total number of libraries in your organization. This includes libraries shared across the entire organization, or within a specific team.
  - **Total components:** The total number of main components across libraries.
  - **Total styles:** The total number of styles across libraries.
- C  Select a workspace to view analytics for the libraries within it.

### For a specific library

View component, style, and variable metrics and usage analytics for a specific library. You can access this from the library's file:

1. Open a library file and click anywhere on the canvas to deselect all layers.
2. Click the  **down arrow** next to the file name and select **Library analytics.**

**Tip**: You can also right click on a library file in the file browser and select **Library analytics** from the menu that appears.

The library analytics modal will appear, which contains two tabs:

The Overview tab The Analytics tab

The **Overview** tab includes a summary of information relating to the library.

![Library overview showing team component, style, and variable usage.](https://help.figma.com/hc/article_attachments/29908838676119)

- A High-level analytics for the library:

  - **Teams using the library:** Number of teams using components from the library.
  - **Total components:** Total number of main components in the library.
  - **Total styles:** Total number of styles in the library.
  - **Total variables:** Total number of variables in the library.
  - **Activity this week:** The total number of times people have inserted components from the library into their files. ”This week” refers to the last seven days.
- B Every style in the library.
- C Every variable collection in the library.
- D Every component in the library.

The **Analytics** tab includes detailed metrics about how people are using each asset within the library, such as which teams are using the asset the most, and number of inserts of a specific asset.

![Analytics tab displaying component insertions graph, top teams by insertions, and component statistics with filters and CSV download option.](https://help.figma.com/hc/article_attachments/29908879009431)

A **Filters**

- Use the **Type** filter to view a specific asset type. Choose between: [**Components**](#h_01JK6GM8VH9RAYEEDSVA5CTYKM)*,* [**Styles**](#h_01JK6J69HG1PV8ME8SBE8VAF1H)*, or* [**Variables**](#h_01JK6J69HGETYEFEE2XWB48JW0)*.*
- Use the **Duration** filter to review analytics for the previous **30**, **60**, or **90** days, or **last year** (a rolling 12 months).

B **Insertions**

A graph of insertions for the selected time period (duration) and asset type.

A component is considered inserted when somebody:

- Copies an instance and pastes it into the file
- Duplicates a component instance within a file
- Drags a component from the **Assets** panel into a file
- [Swaps an instance](https://help.figma.com/hc/en-us/articles/360039150413.html)
- Adds content to a slot within an instance

A style or variable is considered inserted when somebody:

- Copies content that contains a style or variable and pastes it into a file
- When content that uses styles or variables is duplicated within a file
- When a [style](https://help.figma.com/hc/en-us/articles/360040316193) or [variable](https://help.figma.com/hc/en-us/articles/15343107263511) is applied in a file

**Note**: Figma plots the graph to the end of the current week. The end of the week will depend on your geographic location. For example: Figma displays Saturday as the last day of the week in North America and Sunday for people in Europe. You can hover over a dot to view the date and total number of component insertions. The component insertion chart is coded as follows:

- Current data is blue
- Unavailable data is grey
- Comparison data is black
- A dashed line indicates an incomplete week

C **Compare with**

You can compare component insertions between two libraries. This is useful to:

- Track adoption of a new library or compare between a new and old design system
- Compare how libraries are used across different operating systems
- Measure work between products or brands

D **Top teams**

Teams using the library, including the total number of insertions for each team, as well as each team’s percentage of component insertions relative to the total.

E **Download CSV**

If there are more than five teams using a library, **Download CSV** will appear. This gives you the option to export the team data for further review. If there are less than five teams using a library and you want to export the team data, you can copy and paste it from the modal into a spreadsheet or document.

F **Statistics**

Statistics for each asset in the library for the selected time period.

- Click the name of each column to sort the data by ascending or descending values
- Figma logs a detach any time someone uses the [**Detach instance**](https://help.figma.com/hc/en-us/articles/360038665754) setting to break the connection between the instance and the main component. For styles and variables, detaches are logged whenever someone uses the corresponding **Detach** button.

**A few things to note about the data:**

- Library analytics don’t track component usage within other people’s draft files.
- Nested components won’t count as insertions.
- If a style or variable is used by an inserted component, only the component is counted.
- If a variable is used by an inserted style, only the style is counted.
- Figma ignores the initial insertions from duplicating a file.
- Library analytics track up to one year of historical data. Tracking for styles and variables started on October 10, 2024.

## View statistics and usage for a specific asset

In the **Analytics** tab, you can use the **Type** dropdown to filter by asset type to view analytics on the asset type. At the bottom of this view is a statistics section, which contains a list of specific assets for the selected type, along with accompanying statistics. For each specific asset, you can select it to drill down view its usage data.

### Components and component sets

![Component statistics table showing names, variants, total instances, inserts, and detaches for the last 30 days.](https://help.figma.com/hc/article_attachments/29908838680471)

When you set the **Type** filter to **Components** in the **Analytics** tab, you’ll see analytics for both components and component sets in the selected library.

In the **Component statistics** section. This section includes both components and component sets. The number of variants in a component set is shown in the **Variants** column.

In this section, you can select a specific component or component set to drill down and view its usage data.

**Note**: Slots behave similarly to nested instances in library analytics—if a component containing a slot is inserted, the slot itself is not explicitly counted, but the component it belongs to is. However, when inserting content into a slot within an instance, the component is counted as an insertion. Learn more about [what counts as an insertion](https://help.figma.com/hc/articles/360039238353#insertion).

Usage view for a component

![Library analytics showing instances usage, with a file list including names, teams, and modification dates.](https://help.figma.com/hc/article_attachments/29908879014167)

- A Aggregate information about the component:
  - **Description:** A description of the component.
  - **Total:** Total number of instances of this component in your organization.
  - **Used by**: Total number of teams that use this component.
  - **Used in**: Number of files that use instances of this component.
- B

  A table of files using the component. You can only see component usage for files in teams that are open to anyone in the organization, or in teams set to **Only those invited** that you have access to.

  - The files where the component or variant is used.
  - The team containing the file where the component or variant is used.
  - The number of instances of the component or variant in the file.
  - When the file was last modified

Usage view for a component set and its variants

![Library analytics modal displaying component details: total instances, teams using it, files used in, and variant list with usage data.](https://help.figma.com/hc/article_attachments/29908838683671)

- A Aggregate information about the component set:
  - **Description:** A description of the component set. You can add a [description to the component set](https://help.figma.com/hc/en-us/articles/7938814091287), as well as any variants in that component set.
  - **Total:** Total number of instances of all variants in the component set.
  - **Used by**: Total number of teams that use variants from the component set.
  - **Used in**: Number of files that use instances of variants in the component set.
- B A table of variants included in the component set:
  - **Instances:** The current total number of variant instances in files. This gives you a current snapshot of the component's usage, rather than its historical usage over time.
  - **Inserts**: The number of times the variant has been inserted into any file in the last 30 days. This includes instances that have since been deleted, and is most useful for understanding historical usage of a component over time.
  - **Detaches:** The number of times someone has [detached](https://help.figma.com/hc/en-us/articles/360038665754) the variant instance from the component set in the last 30 days.
- C Click any variant in the list to view analytics for that specific component. See above for “Usage view for component."

### Styles

![Style statistics table showing style names with total instances, inserts, and detaches over 30 days in a Figma library.](https://help.figma.com/hc/article_attachments/29908838685335)

When you set the **Type** filter to **Styles** in the **Analytics** tab, you’ll see analytics for styles in the selected library.

In the **Style statistics** section, click on the desired style to drill down and view its usage data.

Usage view for a style

![Library analytics panel displaying an style's usage details.](https://help.figma.com/hc/article_attachments/29908879020183)

- A Aggregate information about the style:
  - **Description:** A description of the style.
  - **Total:** Total number of instances of this style in your organization.
  - **Used by**: Total number of teams that use this style.
  - **Used in**: Number of files that use instances of this style.
- B

  A table of files using the style. You can only see style usage for files in teams that are open to anyone in the organization, or in teams set to **Only those invited** that you have access to.

  - The files where the style is used.
  - The team containing the file where the style is used.
  - The number of instances of the style in the file.
  - When the file was last modified.

### Variables and modes

![Table showing variable analytics in Figma, with columns for name, collection, total instances, inserts, and detaches over 30 days.](https://help.figma.com/hc/article_attachments/29908838689047)

When you set the **Type** filter to **Variables** in the **Analytics** tab, you’ll see analytics for variables.

The table at the bottom contains statistics on variables and modes. You can select the relevant tab to view more.

Variables tab Modes tab

The **Overview** tab includes a summary of information relating to the library.

![Analytics panel showing variable insertions over 30 days, top teams, and detailed variable statistics with options to filter data.](https://help.figma.com/hc/article_attachments/29908838690071)

- A

  A table list of variables in the design system. The columns include the variable’s name, the collection to which it belongs, and other standard statistics. Learn more about which statistics are included in the [analytics tab](anchor link).
- B Filter variables by **Collection**.
- C Click on the desired variable to drill down and view its usage data.

Usage view for a variable

![Library analytics panel showing total instances, teams using a component, and a table of files with modification details.](https://help.figma.com/hc/article_attachments/29908838691479)

- A Aggregate information about the variable:
  - **Description:** A description of the variable.
  - **Total:** Total number of instances of this variable in your organization.
  - **Used by:** Total number of teams that use this variable.
  - **Used in:** Number of files that use instances of this variable.
- B

  A table of files using the variable. You can only see variable usage for files in teams that are open to anyone in the organization, or in teams set to **Only those invited** that you have access to.

  - The files where the variable is used.
  - The team containing the file where the variable is used.
  - The number of instances of the variable in the file.
  - When the file was last modified.

![Analytics interface showing variable insertions graph over time, top teams with insertion percentages, and modes list with instances.](https://help.figma.com/hc/article_attachments/29908879030935)

- A

  The **Modes** list includes the mode’s name, the collection to which it belongs, and the number of instances. Learn more about which statistics are included in the [analytics tab](anchor link).
- B Filter modes by **Collection**.

**Note**: Variables modes does not include a usage view, so you won’t be able to drill down to see more details.

## Library Analytics API

The Library Analytics API, part of the Figma REST API, lets you fetch analytics data for your library usage. The API provides similar information to the in-product library analytics feature, but in a format that you can use to do more fine-grained, custom analysis.

Note: The Library Analytics API is available on the Enterprise plan only.

For more information about the Library Analytics API, check out the [Figma REST API documentation](https://www.figma.com/developers/api#library-analytics).
