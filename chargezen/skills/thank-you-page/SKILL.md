---
name: thank-you-page
description: Make the most of the Shopify thank-you page with Chargezen CheckoutOS — a message for some or all orders (what happens next, a referral ask, a code for the next order, a note for first-time buyers or subscribers), and an address check that confirms the shipping address or suggests a correction before the order ships — saved as drafts, previewed and turned on only on the merchant's OK. Use when someone wants to say something after purchase, cut failed deliveries, or use the thank-you page better.
argument-hint: "<message or address check> [for whom]"
---

# Thank-you page

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

Start with `chargezen.checkout_extensions.discover.v1`: the thank-you text block and the address check block must each be `placed` for what you build to show. Give the merchant the editor link for any that aren't.

## A message after purchase

1. `chargezen.checkout_texts.list.v1`: every active message whose rules match an order shows, so check what's already there.
2. Write it for the moment: the shopper has just paid. Lead with what happens next, then one ask at most. Ideas that work:
   - first-time buyers: when it ships and how to reach support;
   - subscribers: how to skip or change the next order from their account;
   - big orders: a thank-you and a referral ask;
   - a code for the next order (create the code in Shopify first; never invent one).
3. Pick a style (plain or a banner, with a tone) and who sees it (everyone, first-time customers, subscribers, products, subtotal, country, language). Collection rules aren't available here. A checkbox in the message is for show only; it doesn't record consent.
4. Save the draft (`chargezen.checkout_texts.create.v1` with a new `operation_id`), `chargezen.checkout_texts.preview.v1`, show the exact words, and on a clear yes `chargezen.checkout_texts.activate.v1`.

## An address check

Checks the shipping address on the thank-you page and shows a banner: confirmed, a suggested correction, or a warning that it couldn't be verified. It catches typos before they become returned parcels.

1. `chargezen.address_verifications.list.v1`.
2. Agree who gets it (everyone, or first-time customers and international orders, where most bad addresses come from) and the four banner lines. Keep the "couldn't verify" text calm and actionable: "We couldn't confirm this address. Reply to your confirmation email if it needs a fix."
3. Save the draft (`chargezen.address_verifications.save.v1` with a new `operation_id`), show the lines, and on a clear yes publish it with `chargezen.address_verifications.status.v1`.
