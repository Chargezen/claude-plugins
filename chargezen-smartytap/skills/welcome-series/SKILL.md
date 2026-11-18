---
name: welcome-series
description: Build a SmartyTap welcome series in Chargezen — a flow that greets each new email or text subscriber when they join a list, with a first message right away and a follow-up a few days later — saved as a draft, previewed, and turned on only when the merchant says so. Use when they want to welcome new subscribers, set up a welcome email or text, or finish the SMS welcome series every workspace starts with.
argument-hint: "[list or channel, offer]"
---

# Welcome series

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. See what's there

1. `workflows.list`, then `workflows.get` on any flow whose trigger is `smartytap.audience.subscribed`. Every workspace starts with an **SMS welcome series** draft. If a welcome flow exists, offer to finish or improve it rather than add a second one, so nobody gets welcomed twice.
2. `workflows.authoring_options`: the lists, senders, personalization, starter designs (Welcome, Product launch) and whether texts can send yet (`sms.ready`; if not, say what's missing and build email only for now).

## 2. Agree the plan

Propose this, then adjust to what they say:

1. **Trigger:** Subscribed to a list (`smartytap.audience.subscribed`). Filter on `list_name` or `list_id` for one list, and on `channel` (`email` or `sms`) when the email and text welcomes differ.
2. **Leave out people who already know the store:** a `source` filter `not_in` `import`, `shopify_sync`, `teammate`, as Chargezen's own welcome flows do. Imported customers aren't new; welcoming them reads oddly.
3. **Right away:** an email from the Welcome starter design ("Welcome to {{ shop.name }}"): who you are, what to expect, one button to the best sellers. For text joins, a short text instead or as well.
4. **Wait 3 days**, then a second email (Product launch starter, "Our customers' favorites") or a second text.
5. **Re-entry:** once per person (`none`).

An offer must be real: a discount code that already exists in their store, named exactly. This connection can't check codes, so ask them to confirm it. Never invent one.

## 3. Build it as a draft

1. `workflows.create` with `status: "draft"` and a new `operation_id` (describe it on its own first; its schema is large).
2. Write each email at its address in the result's `email_documents` with `email_documents.apply_ops`: subject under 50 characters, preview text, short body, one button, the unsubscribe link and mailing address. Use only tokens the options list, with a fallback for first names (`{{ profile.first_name | default: "friend" }}`).
3. Texts: the store name first, under 160 characters where you can, one link. Check each with `workflows.preview_sms` (trigger `smartytap.audience.subscribed`); the brand prefix and opt-out footer are added for you.
4. `workflows.preview_email` for each email. Show the person every message with its timing and who it reaches.

## 4. Turn it on

Only when they say so: `workflows.activate`. If it lists something to fix, fix it and show them again. From then on each new subscriber gets it; people who joined before today don't. For them, offer a one-off `/campaign` instead.
