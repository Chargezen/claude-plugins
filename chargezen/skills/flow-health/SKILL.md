---
name: flow-health
description: A read-only check of every SmartyTap flow (automation) in Chargezen — which are on and which are still drafts, emails with a missing subject or broken personalization, texts with content errors, WhatsApp templates Meta hasn't approved, senders, lists or segments that no longer exist, flows that would message the same person twice, and missing journeys such as a welcome or abandoned-checkout flow — ending with a ranked list of fixes. Use when they ask whether their flows are working, for a flow audit, or before a busy season.
argument-hint: "[flow name, or all]"
---

# Flow health check

Check: $ARGUMENTS (every flow if nothing was named).

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person picks a fix.

## 1. Gather

1. `workflows.list`: each flow's status (`active` or `draft`) and trigger.
2. `workflows.authoring_options`: senders, lists, segments, live survey questions and whether texts can send (`sms.ready`).
3. For each flow (active ones first), `workflows.get`, then:
   - each email step: `workflows.preview_email`. Note its errors, warnings and checks (a missing subject, personalization written wrongly, custom fonts), and read the email with `email_documents.get` when you need to see whether it has an unsubscribe link and mailing address;
   - each text step: `workflows.preview_sms` with its body and the flow's trigger. Note content errors, `unknown_tokens` the trigger can't fill, and the segment count (long texts cost more credits);
   - each WhatsApp step: `smartytap_whatsapp_templates.get` for Meta's status;
   - senders, lists, segments and survey questions the flow names that are missing from the options.

These tools don't report how many people entered a flow, how many runs failed or what a flow earned. Say so, rather than guessing.

## 2. What to flag

- **Active and broken:** an email or text with errors, a sender that's gone, a WhatsApp template that's rejected or paused, texts while `sms.ready` is false. Customers are missing messages now.
- **Overlap:** two active flows on the same trigger for the same people (two welcome series, two abandoned-checkout flows).
- **No stop rule:** a reminder (cart, checkout, browse, win-back) without a profile filter history `placed_order` equals 0 `since_flow_start`, so people who bought still get nudged.
- **Re-entry:** storefront flows set to `allow` (a regular browser gets emailed every visit; 30 days is recommended), or a flow meant to run every time set to `none`.
- **Drafts left behind:** finished-looking drafts that were never turned on, such as the SMS welcome series every workspace starts with.
- **Missing journeys:** no flow on `smartytap.audience.subscribed` (welcome), `chargezen.pixel.checkout_started` (abandoned checkout), `catalog.back_in_stock` or `shopify.orders.fulfilled` (thank-you).

## 3. Report

Lead with the three fixes that matter most, each one line: the flow, what's wrong, what it costs (customers missing a message, or getting two), and the fix. Then one short line per flow: name, on or off, and "looks fine" or the issue. No tables longer than ten rows.

Offer to fix what they choose: an email with `email_documents.apply_ops`, texts with `workflows.update_messages`, structure with `workflows.update` (read the flow's revision first), turning a duplicate off with `workflows.deactivate`, or building a missing journey (`/welcome-series`, `/abandoned-cart`, `/back-in-stock`, `/order-follow-up`). Changing an active flow changes what customers get from that moment, and turning one off cancels the people waiting in it: say so and wait for a yes.
