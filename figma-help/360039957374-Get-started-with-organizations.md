---
기술지원명: Get started with organizations
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: Get started with organizations
출처링크: https://help.figma.com/hc/en-us/articles/360039957374-Get-started-with-organizations
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you start

Who can use this feature

Supported on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Organizations go beyond the set up of individual teams. They're fantastic for established or growing businesses that need to share resources across a number of teams.

## Plan-specific features

There are two organization plans: Organization and Enterprise. Your organization account will look mostly the same on both plans, with a few differences that we'll cover in this article. [**Explore your organization account →**](https://help.figma.com/hc/en-us/articles/360040450193)

One of the biggest differences is your team hierarchy. The Enterprise plan supports [workspaces](#workspaces), which add another layer of structure within an organization. Check out the diagrams below to see how workspaces impact your organization.

![Organization plan shows organization, teams, projects, and files](https://help.figma.com/hc/article_attachments/28566267159191)

![Enterprise plan shows organization, workspaces, teams, projects, and files](https://help.figma.com/hc/article_attachments/28566267162391)

Another difference is what features you can use:

|  |  |  |
| --- | --- | --- |
| **Feature** | **Organization plan** | **Enterprise plan** |
| [Custom fonts](https://help.figma.com/hc/en-us/articles/360039956774) | ✓ | ✓ |
| [Share organization-wide libraries](https://help.figma.com/hc/en-us/articles/360040529593) | ✓ | ✓ |
| [Track library analytics](https://help.figma.com/hc/en-us/articles/360039238353) | ✓ | ✓ |
| [Create and merge branches](https://help.figma.com/hc/en-us/articles/360063144053) | ✓ | ✓ |
| [View organization activity logs](https://help.figma.com/hc/en-us/articles/360040449533) | ✓ | ✓ |
| [Registered domains and domain capture](https://help.figma.com/hc/en-us/articles/360045953273) | ✓ | ✓ |
| [Authenticate members using SAML SSO](https://help.figma.com/hc/en-us/articles/360040532333) | ✓ | ✓ |
| [Provision users with SCIM](https://help.figma.com/hc/en-us/articles/360048514653) | ✓ | ✓ |
| [Set seat types with SCIM](https://help.figma.com/hc/en-us/articles/360048787534) | ✕ | ✓ |
| [Create workspaces](https://help.figma.com/hc/en-us/articles/4409612431383) | ✕ | ✓ |
| [Restrict guest access](https://help.figma.com/hc/en-us/articles/4410793238167) | ✕ | ✓ |
| [Access activity log API](https://www.figma.com/developers/api#activity_logs) | ✕ | ✓ |
| [Manage team creation](https://help.figma.com/hc/en-us/articles/10386065399319-Manage-who-can-create-a-team-in-an-organization) | ✕ | ✓ |
| [Restrict access to external content](https://help.figma.com/hc/en-us/articles/12080587805719) | ✕ | ✓ |

## Workspaces

If you're on the Enterprise plan, your organization will have workspaces! [Workspaces](https://help.figma.com/hc/en-us/articles/4409676189207) are collections of teams, people, and resources. They add another layer of structure within organizations.

Workspaces could be different teams, departments, cost centers, or business units within your organization.

You can only be assigned to one workspace at a time. When you are assigned to a workspace, you'll be added to any [default teams](https://help.figma.com/hc/en-us/articles/4419450594455). You can view and join teams outside your workspace. As well as browse and access libraries in other workspaces.

Organization admins create workspaces and assign dedicated admins to each workspace. They can then assign both teams and members (including guests) to workspaces. You might see a workspace selector when you join the organization, asking you to [select your workspace](https://help.figma.com/hc/en-us/articles/4409603173143).

## Teams

On team plans, you have to be invited to a team before you can access it in your account. In an organization, you can [view all teams in the organization](https://help.figma.com/hc/en-us/articles/360039957674) and join the ones relevant to you.

You can also [create as many teams as you need](https://help.figma.com/hc/en-us/articles/360040450293) within an organization. You can map teams to your company's hierarchy, or create cross-functional teams for company-wide projects.

Members of the organization can find and access teams that are open to that organization. They can also request to join any other visible teams.

Teams in organizations also have access to extra features, like [library analytics](https://help.figma.com/hc/en-us/articles/360039238353), which allows you to track component, style, and variable usage across teams.

## Other resources

You can share organization-specific resources with other members of your team. This includes style and component libraries, custom fonts, and private organization plugins.

- [Upload brand-specific fonts](https://help.figma.com/hc/en-us/articles/360039956774) and share them with members across your organization.
- [Share organization files](https://help.figma.com/hc/en-us/articles/360040044834) with peace of mind with organization-specific link sharing settings.
- View and install [private organization plugins](https://help.figma.com/hc/en-us/articles/4404228629655)

**[Access organization resources →](https://help.figma.com/hc/en-us/articles/360052679454)**

## Members and guests

Everyone in an organization has an **account type**. A person's account type determines what they can access within the organization.

This includes organization-wide resources, like teams, libraries, plugins, and widgets. It also includes features and functionality, like branching, library analytics, and shared fonts.

Members are people in the organization that have an email address that matches any of the [organization's domains](https://help.figma.com/hc/en-us/articles/360045953273). Members can access teams, libraries, and other resources shared within the organization.

Twigma has the `twigma.com` and `dev.twigma.com` domains registered to their organization. Anyone that joins the organization with a Twigma email address (`name@twigma.com` or `name@dev.twigma.com`) is a member.

Guests are external users with email addresses that don't match any of the organization's domains. They could be contractors, agencies, clients, or external collaborators. Guests have limited access to the organization. They can only resources to which they're invited. They can't browse organization teams or access shared resources like fonts, plugins, or library analytics.

Twigma has the `twigma.com` domain registered to their organization. They work with an agency called DsgnSystm who they invite to a specific team in the organization. As collaborators from the agency only have `dsgnsystm.com` emails, not `twigma.com` emails, they are guests. They can't access any teams or resources outside the team they’re invited to.

[**Members versus guests →**](https://help.figma.com/hc/en-us/articles/4420557314967)

## Seat type

Figma has multiple products: Figma Design, FigJam, Dev Mode, and Figma Slides.

You assign a single seat for each user in your organization, and the seat type determines which products they have access to.

[Learn more about managing seats in Figma](https://help.figma.com/hc/en-us/articles/360039960434).

## Organization admins

[Admins](https://help.figma.com/hc/en-us/articles/4420557724439) are members that have extra administrative rights within an organization. There are two types of admins in an organization: organization admins and workspace admins.

**Organization admins** manage all aspects of the organization. This includes everything from members and resources, to billing and other organization-wide settings.

**Workspace admins** (Enterprise plan only) manage their specific workspace(s). They can manage seats for workspace members, set and assign default teams, and help with billing true-ups.

### Admin settings

Organization admins can access the organization's admin settings. They can adjust members, view teams, monitor activity, manage billing, and configure security settings.

**📖 [Guide to organization admin →](https://help.figma.com/hc/en-us/articles/360039829474)**

### Teams

Organization admins don't have the ability to manage teams in the organization. You need to be a team admin to manage a team. Organization admins can view a list of all teams.

Organization admins can claim ownership of empty teams, and perform limited bulk actions.

- [Manage organization teams](https://help.figma.com/hc/en-us/articles/360053463173)
- [Manage drafts of deleted members](https://help.figma.com/hc/en-us/articles/4420549259799)
- [Claim ownership of projects](https://help.figma.com/hc/en-us/articles/360044267954)

### Billing

When you sign up for a Figma plan, you purchase a number of seats for your annual subscription term.

You can purchase any number of Full, Dev, or Collab seats. View seats are free and do not need to be purchased.

[Learn more about managing billing on the Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328293).

### SAML SSO

Organizations that need enhanced security requirements can configure SAML SSO in Figma. Get started with our [Guide to SAML SSO in Figma →](https://help.figma.com/hc/en-us/articles/360040532333)

- **Security Assertion Markup Language (SAML)** is a security standard for logging into applications.
- **Single Sign On (SSO)** allows users to log into many applications or websites via one set of login details.

You can set up SAML SSO with one of our dedicated providers:

- [SAML SSO with Okta](https://help.figma.com/hc/en-us/articles/360040532353)
- [SAML SSO with OneLogin](https://help.figma.com/hc/en-us/articles/360040533373)
- [SAML SSO with Microsoft Entra ID](https://help.figma.com/hc/en-us/articles/360040532413)
- [Set up SAML SSO for AD FS](https://help.figma.com/hc/en-us/articles/360048269533)

If your provider isn't listed above, you can set up a custom SAML SSO configuration:

- [Set up a custom SAML configuration](https://help.figma.com/hc/en-us/articles/360040047774)
- [Set up automatic provisioning via SCIM](https://help.figma.com/hc/en-us/articles/360048514653)
