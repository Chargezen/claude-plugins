---
name: flow-health
description: A read-only check of every SmartyTap flow (automation) in Chargezen — which are on and which are still drafts, emails with a missing subject or broken personalization, texts with content errors, WhatsApp templates Meta hasn't approved, senders, lists or segments that no longer exist, flows that would message the same person twice, runs that stopped and why, and missing journeys such as a welcome or abandoned-checkout flow — ending with a ranked list of fixes. Use when they ask whether their flows are working, why someone didn't get a flow's message, for a flow audit, or before a busy season.
argument-hint: "[flow name, or all]"
---

# Flow health check

Check: $ARGUMENTS (every flow if nothing was named).

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person picks a fix.

## 1. Gather

1. `chargezen.workflows.list.v1`: each flow's status (`active`, `paused` or `draft`) and trigger; narrow with `status` or `query` when they named one.
2. `chargezen.workflows.authoring_options.v1`: senders, lists, segments, live survey questions and whether texts can send (`sms.ready`).
3. For each flow (active ones first), `chargezen.workflows.get.v1`, then:
   - each email step: `chargezen.workflows.preview_email.v2`. Note its errors, warnings and checks (a missing subject, personalization written wrongly, custom fonts), and read the email with `chargezen.email_documents.get.v1` when you need to see whether it has an unsubscribe link and mailing address;
   - each text step: `chargezen.workflows.preview_sms.v1` with its body and the flow's trigger. Note content errors, `unknown_tokens` the trigger can't fill, and the segment count (long texts cost more credits);
   - each WhatsApp step: `chargezen.smartytap_whatsapp_templates.get.v1` for Meta's status;
   - senders, lists, segments and survey questions the flow names that are missing from the options.
4. `chargezen.workflows.check.v1` on each flow, drafts included: every step in order with whether it's configured and what it will do, and each configuration problem with the step it's on. It runs no one through the flow and sends nothing. `chargezen.workflows.activate.v1` makes further checks of its own (such as each email being written), so a clean check isn't a promise it will turn on.
5. `chargezen.workflows.list_runs.v1` with the `flow_id` of each active flow: recent runs, newest first, with their status, the step each is at or waiting on, and for one that stopped, why (`error_message`: the flow turned off or deleted, a Split path removed, no longer matching the flow's profile filters) and each step it reached with what happened there (step summaries). Runs don't say who the person is. This answers "why didn't they get the second email?" for the run in question.
6. `chargezen.workflows.report.v1` for a flow's results by step, all time (there is no date range); `/flow-results` covers results in depth.

## 2. What to flag

- **Active and broken:** an email or text with errors, a sender that's gone, a WhatsApp template that's rejected or paused, texts while `sms.ready` is false, problems `chargezen.workflows.check.v1` lists, or recent runs stopping with an error. Customers are missing messages now.
- **Overlap:** two active flows on the same trigger for the same people (two welcome series, two abandoned-checkout flows).
- **No stop rule:** a reminder (cart, checkout, browse, win-back) without a profile filter history `placed_order` equals 0 `since_flow_start`, so people who bought still get nudged.
- **Re-entry:** storefront flows set to `allow` (a regular browser gets emailed every visit; 30 days is recommended), or a flow meant to run every time set to `none`.
- **Drafts left behind:** finished-looking drafts that were never turned on, such as the SMS welcome series every workspace starts with.
- **Missing journeys:** no flow on `smartytap.audience.subscribed` (welcome), `chargezen.pixel.checkout_started` (abandoned checkout), `catalog.back_in_stock` or `shopify.orders.fulfilled` (thank-you).

## 3. Report

Lead with the three fixes that matter most, each one line: the flow, what's wrong, what it costs (customers missing a message, or getting two), and the fix. Then one short line per flow: name, on or off, and "looks fine" or the issue. No tables longer than ten rows.

Offer to fix what they choose: an email with `chargezen.email_documents.apply_ops.v1`, texts with `chargezen.workflows.update_messages.v2`, structure with `chargezen.workflows.update.v2` (read the flow's revision first), then `chargezen.workflows.check.v1` again and a test of a changed step to the person with `chargezen.workflows.send_test.v1` (new `operation_id`; it sends to them only and a text costs credits like any text). Turn a duplicate off with `chargezen.workflows.deactivate.v1`; delete an old test flow with `chargezen.workflows.delete.v1` only when they confirm it by name (it can't be restored, and anyone in it leaves it; Chargezen's default flows are refused, so turn those off instead). Or build a missing journey (`/welcome-series`, `/abandoned-cart`, `/back-in-stock`, `/order-follow-up`). Changing an active flow changes what customers get from that moment, and turning one off cancels the people waiting in it: say so and wait for a yes.
