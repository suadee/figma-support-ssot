---
기술지원명: Use your design system package in Make kits
카테고리: 개발
작성자: Figma
승인자: (승인 대기)
출처: Use your design system package in Make kits
출처링크: https://help.figma.com/hc/en-us/articles/35946832653975-Use-your-design-system-package-in-Make-kits
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Figma Make is available for [Full seats](https://help.figma.com/hc/en-us/articles/360039960434) on paid plans.

Any Figma Make user in any plan can use design system packages available on [the public npm registry](https://www.npmjs.com/).

Any Figma Make user in a paid plan can publish private design system packages and use them in Figma Make.

With Make kits, you can bring your production-ready React design system into Figma Make to build high-fidelity prototypes that use the exact same code as your production apps. This lets you prototype, test, and ship using one consistent source of truth.

## Why use a design system package

Many mature product teams already have a design system implemented in their codebase. By adding that system to Figma Make, you can:

- Use your fully interactive, production-ready components directly in prototypes
- Keep design and engineering in sync by using the same design system implementation in both Figma Make and production
- Deploy your Figma Make to production, using your production design system, using the [Figma MCP Server](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)

## Code frameworks supported by Figma Make

Make kits currently only support codebases that are written in React. Here are three of the most common approaches to using design system packages in Figma Make:

- **Use a npm package currently on the npm registry:** The [npm public registry](https://www.npmjs.com/) is a collection of software packages that helps users install various tools and codebases into their applications. Figma Make now supports design systems that have packages published on the npm registry.
- **Publish your own public package on the registry:** Similarly, you can choose to [publish your design system code](https://docs.npmjs.com/creating-and-publishing-unscoped-public-packages) as a publicly-available npm package.
- **Use your private code package:** Figma provides organizations a private registry for publishing npm packages. This allows you to restrict access of your design system to users in your organization.

The team that builds and manages your design system package is best placed to help prepare your package. For private packages, an organization admin must help set up and manage scopes in order for you to publish to the organization’s private npm registry.

## Creating guidelines

Guidelines are critical for ensuring Figma Make can use your design package for high quality, reliable output.

When you’re assembling your Make kit, Figma Make can generate the guidelines for your package automatically. If you prefer, you can also manually write your own guidelines. We recommend letting Figma Make generate the guidelines and then reviewing the result.

See [Get started with Make kits](https://help.figma.com/hc/en-us/articles/39241689698839) to learn about generating guidelines for your Make kits.

See [Write design system guidelines for Make kits](https://developers.figma.com/docs/code/write-design-system-guidelines/) in our developer documentation for best practices.

## Assemble your Make kit

When you're ready to get started:

1. Follow the steps in our [developer documentation](https://developers.figma.com/docs/code/bring-your-design-system-package/) to upload your package to Figma. You'll need to work with an organization admin during this process. Only org admins can manage scopes for your organization's private registry. See the developer documentation for more information.
2. Follow the steps in [Get started with Make kits](https://help.figma.com/hc/en-us/articles/39241689698839)  to finish assembling your Make kit.

Once you've assembled a Make kit that contains your design package, your teammates will be able to use the Make kit throughout Figma Make.
