---
기술지원명: Test your prototypes with UserTesting
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Test your prototypes with UserTesting
출처링크: https://help.figma.com/hc/en-us/articles/19790203466263-Test-your-prototypes-with-UserTesting
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

[UserTesting](http://usertesting.com/) provides videos of users giving real-time feedback as they explore your website, mobile app, prototype, and more. UserTesting allows you to collect feedback on your Figma prototypes and generate actionable insight from your target audience. Additionally, you can embed and watch UserTesting clips and session videos with the [UserTesting integration for FigJam](https://help.usertesting.com/hc/en-us/articles/15335069260180).

Use UserTesting to:

- Evaluate a design using a prototype test, live site test, or navigation test
- Collect feedback when building your website or mobile app
- Run benchmark tests to evaluate design or experiences over time or against a competitor
- Compare feedback on designs with A/B tests and preference tests
- Create omnichannel studies spanning across multiple modes of interaction
- Share clips and highlight reels of the most relevant contributor feedback

Check out the [quick start guide](https://help.usertesting.com/hc/en-us/sections/360003875732-Quick-Start-Guide-Test) or learn more about [getting started with UserTesting](https://www.usertesting.com/start-here) →

## Test your Figma prototype

You can test your Figma prototype by using its share link.

### Edit share settings for a prototype in Figma

1. From your design file, select  **Present** in the toolbar.
2. Once you’re in presentation view, click **Share prototype** in the toolbar.
3. From the **Share prototype** modal, update the access setting to **Anyone**.
4. Click  **Can view** to update the permission setting.

   [Learn more about managing public link sharing and open sessions →](https://help.figma.com/hc/en-us/articles/5726756336791-Manage-public-link-sharing-and-open-sessions)
5. Click **Options** in the toolbar to set how you want contributors to view the prototype.

   - Desktop prototypes: Use **Fit width**
   - Mobile prototypes: Use **Fit to screen**
6. To avoid confusing contributors not familiar with prototypes, deselect these options:

   - Show hotspot hints on click
   - Show sidebar
   - Show Figma UI
7. From the **Share prototype** modal, click **Copy link** to copy the prototype’s URL to your clipboard.

**Note:** Remember that changing any of the prototype options will modify the URL.  
[Learn more about sharing files and prototypes in Figma →](https://help.figma.com/hc/en-us/articles/360040531773-Share-files-and-prototypes#h_01HENVJ93EDPD5MBNYP1JSW7BJ).

### Set up your test in UserTesting

1. Click **Create test** from the toolbar, then select **Create a test** from the dropdown menu.![UserTesting interface showing "Create a test" dropdown in workspace for initiating a new test session.](https://help.figma.com/hc/article_attachments/19823470144151)
2. Select **Prototype**.
3. Select **Build audience** then **Select audience** to customize your audience. Select test contributors from the UserTesting Contributor Network or your own.![Setup screen in UserTesting for selecting contributor devices and network options for a test.](https://help.figma.com/hc/article_attachments/19823491730711)
4. Select **Build test plan** to include necessary context for your testing scenario. You can also adjust settings for the starting URL where contributors will start the test.![Starting instructions panel in UserTesting showing fields for Starting URL and Scenario setup for mobile prototype testing.](https://help.figma.com/hc/article_attachments/19823470169111)

   **Note:** For mobile, select the native browser requirement.
5. Under Test plan, drag and drop a URL task from the Assets menu on the right.
6. Paste your Figma prototype link in the **URL** field.![UserTesting interface showing a test plan setup with a URL entry for launching a Figma prototype task.](https://help.figma.com/hc/article_attachments/19823470175895)
7. You can add as many tasks as you need after the URL asset. You do not need to specify the URL for every task; contributors will complete the tasks at that URL unless you specify a new URL.
8. Use **Preview test plan** to review the flow of the tasks from the contributor’s perspective.
9. Click **Done,** then **Launch test**.

   **Tip:** Preview your prototype in an incognito window to ensure that everyone can access it.

## Best practices for testing Figma prototypes

- **Set expectations:** Let contributors know that they will be interacting with a prototype that is not a fully functional site. Not all links are functional, and the prototype may be slow to load. This can be done in the **Scenario** section of your test plan.
- **Optimize your prototype:** Not all contributors have high-speed internet and can experience slow load times. A large, heavyweight prototype takes longer to load and can lead to contributors abandoning the test. Consider breaking up testing between prototypes or reducing the size of files.
- **Create a dedicated testing file:** Duplicate the Figma file containing the designs you want to test. In this newly created file, remove any pages, frames, assets, images, and elements not relevant to testing to ensure a clean and lightweight testing file.
- **Set checkpoints:** For large, complex prototypes, help the user begin each stage for your test in the right place. Figma supports [multiple flow starting points](https://help.figma.com/hc/en-us/articles/360039823894-Set-prototype-device-and-starting-point#Starting_point) to achieve this.
- **Compress images:** Before uploading them to Figma, consider compressing PNGs that may result in large file sizes. One option to try is [Downsize](https://www.figma.com/community/plugin/869495400795251845/Downsize), a Figma plugin for compressing images.
- **Use Smart Animate sparingly:** Limit the use of Smart Animate whenever possible to decrease loading time. Opt to use simpler transitions that require less RAM.
- **Share your test securely:** You can [require your contributors to sign your company’s NDA](https://help.usertesting.com/hc/en-us/articles/115003378392-Can-I-Require-Test-Contributors-to-Sign-an-NDA-) before accepting your test if additional confidentiality is required.

## Share results with UserTesting for FigJam

After conducting your test, bring your results to life by embedding UserTesting clips, sessions, and highlight reels directly in your FigJam boards.

Check out the [UserTesting and FigJam integration](https://help.figma.com/hc/en-us/articles/14046761881623-Add-insights-with-UserTesting) as well as UserTesting’s [FigJam template](https://www.figma.com/community/file/1251228117769065674) to get started.

[Learn more about prototyping in Figma →](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma)
