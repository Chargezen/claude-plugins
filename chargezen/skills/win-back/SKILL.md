---
name: win-back
description: Bring back subscribers who cancel. Reads who canceled recently and what they were worth, then builds a Chargezen flow that starts when a subscription is canceled — a well-timed email, then a text, with an offer the merchant chooses — stopping for anyone who comes back. Saved as a draft and turned on only when the merchant says so. Use when they ask about win-backs, getting canceled subscribers back, or reducing cancellations.
argument-hint: "[offer, e.g. 20% off the next order]"
---

# Win-back

Offer, if given: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Size the problem

`chargezen.subscription_reports.movement.v1` for the last 30 and the last 90 days (`sources: ["chargezen"]`). Tell the person how many subscribers canceled, the monthly revenue that went with them, and the three highest-spending customers who left with the reasons they gave (`cancellation_reasons`; say so when none was recorded). Keep each one's `customer_ref` for step 4. This is the case for the flow; keep it to three lines.

Then `chargezen.workflows.list.v1` to check for a win-back flow already. If one exists, read it (`chargezen.workflows.get.v1`) and offer to improve it instead of adding a second.

## 2. Agree the plan

Propose this, then adjust to what they say:

1. **Trigger:** Subscription cancelled (`subscription.cancelled`). Leave out cancellations made by the team in the Shopify admin if they want (filter `changed_in_shopify_admin` is false).
2. **Wait 3 days.** Right after canceling is too soon.
3. **Email:** "We saved your spot", from the Win-back starter design. What they loved, what's new, the offer, one button to restart. `{{ customer.portal_link }}` takes them to their account.
4. **Split:** anyone who placed an order since the flow started leaves here.
5. **Wait 7 days**, then a **text** (only if texts are ready and they agreed to texts): one line, the offer, the link.
6. **Re-entry:** once per customer (`none`), so nobody gets it twice.

The offer must be real. In an email, give each person their own code: set the coupon block to `couponSource: {type: "unique"}` with the offer (percent or amount off, an optional minimum order and an optional number of days it works) through `chargezen.email_documents.apply_ops.v1`. State only the offer; never ask for or upload a list of codes. Chargezen makes each recipient's single-use Shopify code when the email sends, so say plainly that turning the flow on (or launching a campaign) creates real discount codes on the store, and for a campaign confirm the number from `chargezen.smartytap_campaigns.preview_audience.v1` first. It needs a connected Shopify store. Texts can't carry a unique code: for a text, use a code the store already has in Shopify, named exactly, or no discount and a reason to come back instead. Never invent a code. If a win-back campaign later pauses with `discount_codes` in `chargezen.smartytap_campaigns.get.v1`: when Shopify didn't finish the codes (`unfinished`), resume it with `chargezen.smartytap_campaigns.resume.v1`; when Shopify refused them (`refused`), relay Shopify's reason, change the coupon block's offer with `chargezen.email_documents.apply_ops.v1` and publish it with `chargezen.smartytap_campaigns.publish_scheduled_edit.v1`. An offer changed after launch gives the unsent emails new codes.

## 3. Build it as a draft

1. `chargezen.workflows.authoring_options.v1` for the trigger, steps, senders, templates, personalization and whether texts can send.
2. `chargezen.workflows.create.v2` with `status: "draft"` and a new `operation_id`.
3. Write each email at the address in the result's `email_documents` with `chargezen.email_documents.apply_ops.v1`: subject under 50 characters, short body, one button, unsubscribe link and mailing address.
4. `chargezen.workflows.preview_email.v2` and `chargezen.workflows.preview_sms.v1`; show the person both, with the timing.

## 4. Turn it on

Only when they say so: `chargezen.workflows.activate.v1`. From then on, each cancellation starts it.

It doesn't reach people who canceled before today on its own. For those, start this same flow by hand: for each customer they pick from step 1, find their cancelled subscription with `chargezen.admin_customer_subscriptions.search.v1` (their `customer_ref`), then `chargezen.workflows.trigger.v1` with `customer_id` set to the `customer_ref.id` and that `subscription_ref` (a new `operation_id` each), one at a time, each on their OK. It is refused if that subscription isn't cancelled any more. A `null` result means the flow's filters or re-entry kept that customer out; say so. Who cancelled isn't known for these, so a filter on `changed_in_shopify_admin` keeps everyone out: leave that filter off if they want to reach past cancellations.
