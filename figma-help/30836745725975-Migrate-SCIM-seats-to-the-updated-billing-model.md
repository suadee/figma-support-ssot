---
기술지원명: Migrate SCIM seats to the updated billing model
카테고리: 계약
작성자: Figma
승인자: (승인 대기)
출처: Migrate SCIM seats to the updated billing model
출처링크: https://help.figma.com/hc/en-us/articles/30836745725975-Migrate-SCIM-seats-to-the-updated-billing-model
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

In March 2025, Figma introduced updates to how seats and other billing features work.

[Learn more about the transition to the updated billing model](https://help.figma.com/hc/en-us/articles/27468498501527).

If you've previously managed seats for your organization with SCIM and want to continue doing so, you may need to take some steps to ensure your SCIM user configuration works correctly with the updated billing model.

## Old method of user configuration

Previously, when you used SCIM to explicitly assign users seats in Figma, you would set the following permissions:

- `figmaPermission`
- `devModePermission`
- `figjamPermission`

While best practice was to assign values to each of the attributes, it wasn't required. You could exclude unused permissions, or set the value of a permission to null.

Now, so Figma can correctly map your SCIM configuration to the seat types in the updated billing model, you need to do one of the following:

- [Configure SCIM so your users can be assigned to the new seat types](#h_01JPXAND3S8QNF6ZDF7FG4ZZ9Q): Full, Dev, Collab, and View. This is the recommended method.
- [Modify your existing SCIM configuration](#h_01JPXBB7BAQRERW8PS2S73NKCA) so Figma can correctly map users to the updated seat types. This method will only work until March 2026, at which point you need to ensure your users are directly assigned to the new seat types.

## Use the new seat types (best practice)

The best way to ensure you can continue to manage your SCIM users as normal, including upgrading and downgrading, is to migrate to the new seat types. See [Manage Seats via SCIM](https://help.figma.com/hc/en-us/articles/360048787534) for information about how to update your SCIM configuration to handle the new seat types.

## Modify your existing configuration

Note: You have until March 2026 to update your SCIM configuration to use the new seat types.

To continue managing users with your existing SCIM configuration, such as being able to downgrade users, you need to make two updates:

1. Ensure that all users have the following three permissions: `figmaPermission`, `devModePermission`, and `figjamPermission`.
2. Ensure that each permission is set to one of the following values: `full` or `viewerRestricted`.

When your SCIM users are configured in this way, it will ensure that Figma is able to correctly map the users to the new seat types. However, this method will no longer work after March 2026.

Note: If you're having issues migrating your existing SCIM configuration, reach out to your account manager, or follow the steps in [Get help with Figma](https://help.figma.com/hc/en-us/articles/360041057214).
