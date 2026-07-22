---
기술지원명: Troubleshoot in Figma Make
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Troubleshoot in Figma Make
출처링크: https://help.figma.com/hc/en-us/articles/31304610458647-Troubleshoot-in-Figma-Make
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Figma Make is available for [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on paid plans.

You can try Figma Make on other seats and plans.

When you’re working in Figma Make, you may sometimes encounter [error messages](#h_01JTF1ZXPA25V3DMYRB0PBDC53) or [issues](#h_01JTF1ZXPA2ZBYJBQ30H56M6JR).

## Error messages

Here’s are the error messages that you may run into and what they mean. The error messages are organized alphabetically to make referencing easier, not in terms of how often you might experience the error.

| Error message | Reason | How to fix the error |
| --- | --- | --- |
| Attachments are too large. | The images attached to the prompt are too large to process. | Reduce the size and resolution of the image and [try attaching it again](https://help.figma.com/hc/en-us/articles/31304529835671#h_01JTF3AP5Z9S0RFX9E9N7DD963). |
| Attachment failed. Try a different frame. | We weren’t able to convert the design to be usable in Figma Make. | Occasionally, depending on the complexity and content of a design, we’re not able to convert it to a usable format for Figma Make. When this happens, try [separating out the parts of the design into simpler, smaller frames](https://help.figma.com/hc/en-us/articles/31304529835671#h_01JTF3AP5ZBWVFQ60GZP02TT0E) and attach those instead. |
| Connection interrupted... Please try again. | A network error has caused the operation to fail. | This is usually related to an unstable connection to Figma. Wait for a short time and then try prompting again. |
| Couldn't connect. | There is no internet connectivity. | Ensure that you’re connected to the internet and then try your prompt again. |
| Designs are too large to upload. Try adding screens separately. | The size of the frame or component that was used is too large in terms of width and height. | The design you attached to the prompt was too large in size. Instead of attaching the whole frame or component, select parts of the design that you want to add to prompts one at a time. You can also try splitting the design into [multiple, smaller frames](https://help.figma.com/hc/en-us/articles/31304529835671#h_01JTF3AP5ZBWVFQ60GZP02TT0E). |
| Limit reached for this feature until <date>. | The prompt limit for the user has been reached. | When the limit resets at the given date, continue prompting. |
| Make sure your design is in a frame, then try again. | A design that’s not in a frame and isn’t a component was pasted into the prompt box of the AI chat. | In the Figma Design file where you copied the design, make sure your selection is in [a frame](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma-Design). You can also right-click your selection and select **Frame selection** from the menu. |
| Please try a different input. | The prompt was flagged by automated moderation and blocked. | This occurs when the model detects prompts that potentially contain unsafe or harmful content. Try rewording your prompt. |
| Project too large, try deleting some files | The project contains very large files that are exceeding size limits. | This occurs when one or more files in the project are exceeding the 1MB size limit, which prevents the AI chat in Figma Make from working correctly.  To resolve the issue, look for files that are too large, indicated by the warning symbol next to the filename.  Warning icon next to a file called example-bad-file.tsx indicating the file exceeds the 1MB size limit.  Shorten or delete the problem files.  Once the problem files are fixed or removed, you can prompt Figma Make to resolve any issues introduced by shortening the files. |
| Rate limit exceeded. | Too many prompts have been sent in a short period of time and the rate limit has been exceeded.    This error isn't related to [usage limits](https://help.figma.com/hc/en-us/articles/31722591905559-Figma-Make-FAQs#h_01JTE4M55F6PVQ9ZRTDR5P1WVG). | Wait for a short time and then try your prompt again. |
| Some frames are too big, so they were converted to images. | The design you attached or pasted into the prompt box was too big. | Figma Make automatically converts the attached design into an image instead. If you'd prefer to use the design version, try attaching smaller frames within the design, rather than the whole design itself. Try adding the smaller frames [one prompt at a time](https://help.figma.com/hc/en-us/articles/31304529835671-Attach-designs-and-images-to-a-prompt#h_01JTF3AP5ZBWVFQ60GZP02TT0E). |
| Something went wrong... Try again in a minute. | The operation has failed for an unknown reason. | Due to the generative nature of Figma Make and AI models, occasionally a prompt will fail for an unknown reason. Wait for a short while and then try your prompt again. If you have a file where you repeatedly have this error, try duplicating the file and start prompting again in the copy. If the error is persistent, you can also [report it as a bug](#h_01JTF1ZXPASJGQ4X05T92GSAQZ). |
| Try again, with fewer inputs. | The selection that was pasted into the AI chat or the selection you pointed to with the edit tool is too large. | When you paste content into the AI chat, it’s converted into a format the model can use. Selections that contain a large amount of layers, text, images, and other design elements can cause the prompt to become too long. Try your prompt again with a smaller selection of content. |
| Try pasting a frame instead of a URL. | A URL for a Figma file was pasted into the prompt box of the AI chat. | Either [attach the design](https://help.figma.com/hc/en-us/articles/31304529835671) or component to the prompt, or copy and paste a design in the file directly into the prompt box of the AI chat. |
| You can add up to 3 attachments to each message. | More than three designs or images were attached to a prompt. | Split your prompt into multiple prompts, and attach fewer designs or images to each of those prompts. |

## Other issues

You may occasionally encounter issues that don’t result in an error message, such as:

- The model won’t stop thinking and no code is generated
- Prompting doesn’t result in any change to the functional prototype or web app
- The [Point and edit tool](https://help.figma.com/hc/en-us/articles/31304485164695-Create-and-edit-a-functional-prototype-or-web-app#h_01JTEVBJ0527WJSQ40FDX87CRH) doesn’t make changes when selecting elements

If you’re not seeing any change in the functional prototype or web app, click  **Refresh preview** at the top of the preview. Check if the changes to your functional prototype or web app are now visible.

If refreshing the preview doesn’t resolve the issue, try refreshing the page and then prompt the model again. You can also duplicate the Figma Make file and start prompting again in the copy.

If the file is unresponsive because its preview is causing performance problems, open the file from the file browser, right-click it, and select **Open with preview disabled**. You can also add `&disablepreview` to the file URL. With the preview disabled, you can restore a previous version or ask Figma Make to diagnose and improve the generated code.

If the AI's responses feel inconsistent or off-track—for example, it's not following new instructions or output quality has degraded after many prompts—try [clearing your chat context](https://help.figma.com/hc/en-us/articles/39893099629975). This resets the AI's memory for the current file.

If [Point and edit](https://help.figma.com/hc/en-us/articles/31304485164695-Create-and-edit-a-functional-prototype-or-web-app#h_01JTEVBJ0527WJSQ40FDX87CRH) doesn’t make changes when selecting elements, check which UI framework your project is using. Point and edit works with projects built using Tailwind CSS and shadcn/ui. It doesn’t currently support other component libraries, such as Material UI.

If your project uses an unsupported library, try one of the following:

- Switch to Tailwind and shadcn/ui components
- Describe your changes in the AI chat instead of using Point and edit
- Duplicate the file and regenerate the app using a supported framework

If the problem persists, report the issue as a bug.

## Report bugs and problems

If you have persistent errors or bugs in a file, follow the steps to [submit a bug report](https://help.figma.com/hc/en-us/articles/360041468234-Submit-a-bug-report). In your report, include an image or a short video of the problem that you’re encountering. A brief explanation of the action you were attempting in Figma Make is also helpful.
