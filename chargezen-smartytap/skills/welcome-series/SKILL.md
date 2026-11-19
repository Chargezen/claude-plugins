---
name: welcome-series
description: Build a SmartyTap welcome series in Chargezen — a flow that greets each new email or text subscriber when they join a list, with a first message right away and a follow-up a few days later — saved as a draft, previewed, and turned on only when the merchant says so. Use when they want to welcome new subscribers, set up a welcome email or text, or finish the SMS welcome series every workspace starts with.
argument-hint: "[list or channel, offer]"
---

# Welcome series

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. See what's there

1. `chargezen.workflows.list.v1`, then `chargezen.workflows.get.v1` on any flow whose trigger is `smartytap.audience.subscribed`. Every workspace starts with an **SMS welcome series** draft. If a welcome flow exists, offer to finish or improve it rather than add a second one, so nobody gets welcomed twice.
2. `chargezen.workflows.authoring_options.v1`: the lists, senders, personalization, starter designs (Welcome, Product launch) and whether texts can send yet (`sms.ready`; if not, say what's missing and build email only for now).

## 2. Agree the plan

Propose this, then adjust to what they say:

1. **Trigger:** Subscribed to a list (`smartytap.audience.subscribed`). Filter on `list_name` or `list_id` for one list, and on `channel` (`email` or `sms`) when the email and text welcomes differ.
2. **Leave out people who already know the store:** a `source` filter `not_in` `import`, `shopify_sync`, `teammate`, as Chargezen's own welcome flows do. Imported customers aren't new; welcoming them reads oddly.
3. **Right away:** an email from the Welcome starter design ("Welcome to {{ shop.name }}"): who you are, what to expect, one button to the best sellers. For text joins, a short text instead or as well.
4. **Wait 3 days**, then a second email (Product launch starter, "Our customers' favorites") or a second text.
5. **Re-entry:** once per person (`none`).

An offer must be real: a discount code that already exists in their store, named exactly. This connection can't check codes, so ask them to confirm it. Never invent one.

## 3. Build it as a draft

1. **Start from the library:** `chargezen.workflows.list_templates.v1` lists the flow library; its Welcome series (`welcome_series`) has the plan above: a welcome email right away, a text for text joins, then a bestsellers email, leaving out imported and synced people. `chargezen.workflows.create_from_template.v1` with that `template_key` and a new `operation_id` creates it as a Draft that sends nothing, each email started from a starter design with the template's subject and preview text. Keep that `operation_id` for any retry: a new one makes a second flow. (To finish the SMS welcome series draft the workspace already has, skip this and edit that flow.)
2. `chargezen.workflows.get.v1` on the Draft, then change it to the agreed plan: the trigger's list or channel filter, the wait, a step added or removed with `chargezen.workflows.update.v2` (from the revision you read), or only the texts with `chargezen.workflows.update_messages.v2`. A plan the library doesn't fit is built with `chargezen.workflows.create.v2` (`status: "draft"`, a new `operation_id`) instead.
3. Write each email at its address in `email_documents` with `chargezen.email_documents.apply_ops.v1`: subject under 50 characters, preview text, short body, one button, the unsubscribe link and mailing address. Use only tokens the options list, with a fallback for first names (`{{ profile.first_name | default: "friend" }}`).
4. Texts: the store name first, under 160 characters where you can, one link. Check each with `chargezen.workflows.preview_sms.v1` (trigger `smartytap.audience.subscribed`); the brand prefix and opt-out footer are added for you.
5. `chargezen.workflows.preview_email.v2` for each email and `chargezen.workflows.check.v1` for the whole flow. Show the person every message with its timing and who it reaches.
6. Offer a test of each email and text to them: `chargezen.workflows.send_test.v1` with the step and a new `operation_id`. It goes to them only (or the one address or number they give), filled with sample data; a test text costs credits like any text.

## 4. Turn it on

Only when they say so: `chargezen.workflows.activate.v1`. If it lists something to fix, fix it and show them again. From then on each new subscriber gets it; people who joined before today don't. For them, offer a one-off `/campaign` instead.
