---
기술지원명: What’s the difference between workspaces and billing groups?
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: What’s the difference between workspaces and billing groups?
출처링크: https://help.figma.com/hc/en-us/articles/19202489035543-What-s-the-difference-between-workspaces-and-billing-groups
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

In December 2023, we moved billing management out of workspaces and into a new feature called **billing groups**.

Billing groups are for **accounting** and organizing people by cost center. Workspaces are for **collaboration** and organizing work by departments, product areas, or other categories.

Billing groups Workspaces

**Billing groups** build confidence over billing decisions:

- Route upgrade requests and licensing decisions to the relevant decision makers
- Simplify internal accounting by sorting users into cost centers

**Workspaces** enable better collaboration and offer granular content policies:

- Help teams find relevant files in an organized space
- Curate libraries for members to use
- Customize access and plugins for different areas of the business

**Note**: If your organization used workspaces before billing groups launched, we’ve automatically created billing groups for you. Your billing groups have the same names, admins, and members as your current workspaces. From here, you can modify each [billing group](https://help.figma.com/hc/en-us/articles/19100486415255) and [workspace](https://help.figma.com/hc/en-us/articles/7096698154519) to best match your organization’s needs.

## Who can manage workspaces and billing groups?

With the launch of billing groups, there are now four types of admins in a Figma organization:

- **Organization admins** have the highest level of permission for [managing a Figma organization](https://help.figma.com/hc/en-us/articles/360039829474). They can typically do everything a billing group admin or workspace admin can do, as well as managing the highest-level settings in the organization.
- **Billing group admins** sort people in an organization according to internal budget sources and [manage their paid seat status](https://help.figma.com/hc/en-us/articles/19100486415255).
- **Workspace admins** [manage teams and resources in their workspaces](https://help.figma.com/hc/en-us/articles/7096698154519).
- **Team admins** [manage aspects of individual teams](https://help.figma.com/hc/en-us/articles/360053463173), like people, resources, and access to the team.

Below, you can see how each role can manage different aspects of billing groups and workspaces. Team admins can’t manage billing groups or workspaces, so they’ve been excluded from the table.

**Note**: A person can take on multiple admin roles in Figma. For example, someone can be both a billing group admin and a workspace admin and manage multiple billing groups and workspaces.

### Manage billing groups

|  | Organization admins | Workspace admins | Billing group admins |
| --- | --- | --- | --- |
| Create and delete billing groups | ✓ | X | X |
| Add or remove billing group admins | ✓ | X | X |
| Rename a billing group | ✓ | X | X |
| Assign or unassign users from a billing group | ✓ | X | Billing groups they manage |
| Move users between billing groups | ✓ | X | Billing groups they manage |

### Manage workspaces

|  | Organization admins | Workspace admins | Billing group admins |
| --- | --- | --- | --- |
| Create and delete workspaces | ✓ | X | X |
| Add or remove workspace admins | ✓ | X | X |
| Rename a workspace | ✓ | X | X |
| Assign or unassign users from a workspace | ✓ | Workspaces they manage | X |
| Move users between workspaces | ✓ | Workspaces they manage | X |
| Assign or unassign teams from a workspace | ✓ | Workspaces they manage | X |
| Move teams between workspaces | ✓ | Workspaces they manage | X |
| Enable or disable the workspace selector | ✓ | X | X |
| Customize a workspace’s header color | ✓ | Workspaces they manage | X |
| Customize a workspace’s icon | ✓ | Workspaces they manage | X |
| Edit a workspace’s description | ✓ | Workspaces they manage | X |

### Add and remove users from the organization

|  | Organization admins | Workspace admins | Billing group admins |
| --- | --- | --- | --- |
| Invite users to the organization | ✓ | Invited users join the workspace they are invited from | Invited users join their billing group |
| Remove users from the org | ✓ | Users in workspaces they manage | Billing groups they manage |

### Billing

|  | Organization admins | Workspace admins | Billing group admins |
| --- | --- | --- | --- |
| Upgrade or downgrade users’ seats | ✓ | X | Billing groups they manage |
| Manage seat requests | Requests from users who are Unassigned | X | Billing groups they manage |

### Content management

|  | Organization admins | Workspace admins | Billing group admins |
| --- | --- | --- | --- |
| Manage teams | Any visible teams | Visible teams in workspaces they manage | X |
| Approve guest requests\* | For requests to content outside a workspace | For requests to content in workspaces they manage | X |
| Invite new guests\* | ✓ | Guest automatically joins their workspace | X |
| Approve a plugin for the organization | ✓ | X | X |
| Approve a plugin for a workspace | ✓ | X | X |
| Set link sharing controls for the organization | ✓ | X | X |
| Set link sharing controls for a workspace | ✓ | X | X |
| Set default teams for a workspace | X | ✓ | X |
| Enable libraries by default for all files in the organization | ✓ | X | X |
| Enable libraries by default for all files in a workspace | ✓ | Workspaces they manage | X |
| Set default modes for a workspace | ✓ | Workspaces they manage | X |

\*Only applicable if [guest access is restricted](https://help.figma.com/hc/en-us/articles/4410793238167.html).
