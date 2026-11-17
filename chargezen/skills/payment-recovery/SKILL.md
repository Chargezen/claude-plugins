---
name: payment-recovery
description: Recover subscription renewals whose payment failed. Checks the merchant's existing Chargezen flows, then builds one that starts when a renewal payment fails — a friendly email and text with a secure link to update the card, a reminder before the last retry, and an alert to the team when retries run out — as a draft, turned on only when they say so. Use when they ask about failed payments, declined cards, dunning or involuntary cancellations.
---

# Payment recovery

Follow the `chargezen` skill for how to reach the tools.

## 1. See what's there

`workflows.list`, then `workflows.get` on any flow whose trigger is a payment event (`subscription.payment_failed_first_attempt`, `payment_retrying`, `payment_last_attempt`, `payment_method_problem`). If one already covers failed payments, read it to the person and offer to improve it rather than adding a second; two flows would message customers twice.

## 2. Agree the plan

Propose, then adjust:

1. **Trigger:** Renewal payment failed (`subscription.payment_failed_first_attempt`).
2. **Email right away:** "Your order is on hold." Plain and kind: the payment didn't go through, nothing is lost, update the card in a minute. One button to `{{ customer.portal_link }}`. No blame, no card details.
3. **Wait 2 days**, then a **text** (only if texts are ready and they agree): one line and the link.
4. **A second flow** on Payment retries ended (`subscription.payment_last_attempt`): an **internal alert** to the team with the customer and subscription, so someone can reach out personally.

Optional, if they want: a flow on Payment method problem (`subscription.payment_method_problem`), for a card that's about to expire, so customers fix it before a renewal fails.

## 3. Build it as a draft

1. `workflows.authoring_options` for triggers, steps, senders, templates, personalization and whether texts can send. Ask who should get the internal alert. A new alert address gets a confirmation email first and receives alerts only after it confirms; tell the person so they watch for it.
2. `workflows.create` with `status: "draft"` and a new `operation_id` for each flow.
3. Write each email with `email_documents.apply_ops` at the address in `email_documents`: subject under 50 characters, two or three short sentences, one button, unsubscribe link and mailing address.
4. `workflows.preview_email` and `workflows.preview_sms`; show the person everything a customer would get, in order, with the timing.

## 4. Turn it on

Only when they say so: `workflows.activate` for each flow. Say it starts with the next failed renewal. For a customer whose payment already failed, offer `admin_customer_subscriptions.request_payment_method_update`, which emails them a secure link, one customer at a time on their OK.
