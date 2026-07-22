---
기술지원명: Record a performance profile
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Record a performance profile
출처링크: https://help.figma.com/hc/en-us/articles/360041468414-Record-a-performance-profile
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

**When:** If you are experiencing performance issues, like slowness and lagging, in the **Figma desktop app**.

**What:** Use the developer tools to record yourself performing the affected actions.

**Why:** Recording a performance profile will help us to identify how Figma is performing.

Before you relaunch the app and record a performance profile, completely quit the Figma desktop app.

1. Launch the Figma Desktop app
2. Click Help in the menu bar then select **Troubleshooting**
3. Select **Toggle Web App Developer Tools**
4. This will open a Developer Tools window above the Figma app. Select the **Performance** tab from the options:

   ![Developer Tools window open with Performance tab selected, instructing to start recording with button or Command+E shortcut.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d7731df2c7d3a7e9ae0f1fc/file-80u44WeRhx.png)
5. Click the **Record** button in the top left corner of the window:

   ![Developer Tools window open with Performance tab highlighted, showing instructions to record actions using the record button in the top left corner.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d7731e72c7d3a7e9ae0f1fd/file-vwaIFMZFui.png)
6. A progress dialog will indicate that a profile is being recorded:

   ![Chrome DevTools Performance tab showing recording in progress for profiling Figma actions, with a "Stop" button highlighted.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d7731ef04286364bc8ee9b9/file-jZq0SJgqo3.png)
7. You can now go back to the Figma app and perform any of the specific actions you're having issues with.
8. When you're finished, return to the Developer Tools window and click the **Stop** button to end the profile:

   ![Stop button highlighted in Chrome Developer Tools' Performance tab during Figma performance profiling. Press it to stop the recording.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d7731f404286364bc8ee9ba/file-kQm7AuQaHC.png)
9. The Console will now show you a detailed view of the profile. You can even scroll through the timeline at the top to view a screenshot of each action:

   ![Developer Tools window with Performance tab, showing timeline data and Figma interface to diagnose app performance issues.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d7732022c7d3a7e9ae0f200/file-zRBPof75YD.png)
10. Right-click in the console and select **Save profile**. This will download a copy of the Performance Profile to your computer.

    ![Developer Tools window showing a performance profile timeline, option to save or load profile highlighted.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d7731fb04286364bc8ee9bb/file-YXqDTY21my.png)
11. You can then attach the saved File to your Figma Support conversation.

**Tip!** You can also use the keyboard shortcuts to **start** and **stop** the profiling process.

**Mac:** `Command` `E` **Windows**:  `Ctrl` `E`

**Need to submit a bug report?** [Head to our Support Hub to get started](https://help.figma.com/hc/en-us/requests/new).
