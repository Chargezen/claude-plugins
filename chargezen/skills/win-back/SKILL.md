---
name: win-back
description: Bring back subscribers who cancel. Reads who canceled recently and what they were worth, then builds a Chargezen flow that starts when a subscription is canceled — a well-timed email, then a text, with an offer the merchant chooses — stopping for anyone who comes back. Saved as a draft and turned on only when the merchant says so. Use when they ask about win-backs, getting canceled subscribers back, or reducing cancellations.
argument-hint: "[offer, e.g. 20% off the next order]"
---

# Win-back

Offer, if given: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Size the problem

`subscription_reports.movement` for the last 30 and the last 90 days (`sources: ["chargezen"]`). Tell the person how many subscribers canceled, the monthly revenue that went with them, and the three highest-spending customers who left. This is the case for the flow; keep it to three lines.

Then `workflows.list` to check for a win-back flow already. If one exists, read it (`workflows.get`) and offer to improve it instead of adding a second.

## 2. Agree the plan

Propose this, then adjust to what they say:

1. **Trigger:** Subscription cancelled (`subscription.cancelled`). Leave out cancellations made by the team in the Shopify admin if they want (filter `changed_in_shopify_admin` is false).
2. **Wait 3 days.** Right after canceling is too soon.
3. **Email:** "We saved your spot", from the Win-back starter design. What they loved, what's new, the offer, one button to restart. `{{ customer.portal_link }}` takes them to their account.
4. **Split:** anyone who placed an order since the flow started leaves here.
5. **Wait 7 days**, then a **text** (only if texts are ready and they agreed to texts): one line, the offer, the link.
6. **Re-entry:** once per customer (`none`), so nobody gets it twice.

The offer must be real: a discount code they already have in Shopify, named exactly. If they don't have one, ask them to create it, or make the flow with no discount and a reason to come back instead. Never invent a code.

## 3. Build it as a draft

1. `workflows.authoring_options` for the trigger, steps, senders, templates, personalization and whether texts can send.
2. `workflows.create` with `status: "draft"` and a new `operation_id`.
3. Write each email at the address in the result's `email_documents` with `email_documents.apply_ops`: subject under 50 characters, short body, one button, unsubscribe link and mailing address.
4. `workflows.preview_email` and `workflows.preview_sms`; show the person both, with the timing.

## 4. Turn it on

Only when they say so: `workflows.activate`. From then on, each cancellation starts it.

It doesn't reach people who canceled before today. For those, offer a second flow with the same email and text whose trigger is Started by hand (`workflows.manual`), built and activated the same way. Then, for each customer they pick from step 1, find them with `customers.search` and start it with `workflows.trigger` (a new `operation_id` each), one at a time, each on their OK. A `null` result means the flow's filters or re-entry kept that customer out; say so.
