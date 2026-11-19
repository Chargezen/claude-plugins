---
name: order-follow-up
description: Build a SmartyTap flow in Chargezen that follows up after an order ships — a thank-you a few days after fulfillment, then a request for a review or a quick rating — with an optional different path for first-time and repeat customers, saved as a draft, previewed, and turned on only on the merchant's OK. Use for thank-you emails, review requests, "how's your order?" texts or a post-delivery check-in. (For an offer inside checkout or right after payment, that's CheckoutOS's `/post-purchase`.)
argument-hint: "[review link or survey, timing]"
---

# Order follow-up

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Check what's there

1. `chargezen.workflows.list.v1`: look for flows on Order fulfilled (`shopify.orders.fulfilled`) or Order paid. If one already thanks customers, read it with `chargezen.workflows.get.v1` and offer to add to it rather than send two.
2. `chargezen.workflows.authoring_options.v1` for senders, starter designs (VIP thank-you, Order shipped), live survey questions and whether texts can send.

There is no "delivered" event: the flow starts when the order is fulfilled, so the wait covers shipping time. Ask how long their orders usually take to arrive.

## 2. Agree the plan

Propose this, then adjust:

1. **Trigger:** Order fulfilled. Filter on `skus`, `tags` or `total_price` if only some orders should get it. Re-entry `allow` (every order) or `after_period` (say 60 days) so frequent buyers aren't asked every time.
2. **Wait** shipping time plus a couple of days (Chargezen's own thank-you flow waits 7 days).
3. **Optional Split:** first-time customers (profile filter `total_orders` equals 1, or history `placed_order`) get a warmer welcome-style thank-you; repeat customers a shorter note.
4. **Thank-you email** (VIP thank-you starter): thanks, how to get the most from the product, a contact for problems.
5. **Wait 5–7 days**, then the **review ask**, one of:
   - a link to their review page: they give the exact link; never make one up;
   - a 0-10 or 1-5 rating on a SmartyTap survey: build it with `/survey` first, then link its page, or use an **Ask by text** step (`ask_text`) that texts the question and follows each answer (for example, a thank-you to a 9 or 10 asking for a public review, and an alert to the team for a low score with an **Internal alert** step).

Order follow-ups to people who haven't agreed to marketing should stay about the order (`purpose: "transactional"`). A review request with a promotion or a coupon is marketing: mark it `marketing`.

## 3. Build, check, turn on

1. `chargezen.workflows.create.v2` with `status: "draft"` and a new `operation_id`.
2. Write each email with `chargezen.email_documents.apply_ops.v1` at its address in `email_documents`, using the trigger's order tokens (`{{ order.name }}`) and `{{ profile.first_name }}` with a fallback.
3. `chargezen.workflows.preview_email.v2` and `chargezen.workflows.preview_sms.v1` (trigger `shopify.orders.fulfilled`). Show the whole path with its timing.
4. Only when they say so: `chargezen.workflows.activate.v1`. Orders fulfilled before then don't get it.
