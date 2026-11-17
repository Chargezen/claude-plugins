---
name: post-purchase
description: Build a one-click post-purchase offer or a short funnel in Chargezen CheckoutOS — shown after payment, before the thank-you page, added to the order on the shopper's saved payment with no re-entry — choosing the product (a specific one or from their cart), the discount, who sees it, the copy and what follows a yes or a no, checking the rules against a real order, and publishing or scheduling only on the merchant's OK. Use when someone wants a post-purchase upsell, a one-click add-on, a subscription upgrade after checkout, or a funnel.
argument-hint: "<what to offer> [to whom, discount]"
---

# Post-purchase offer

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

A shopper who accepts gets the item added to their order and is **charged on their original payment method** right away. Say this plainly when you show the offer.

## 1. What's there

1. `checkout_extensions.discover`: the post-purchase block must be set up; if not, give the merchant the link.
2. `post_purchase_upsells.funnels` for the last 30 days: live offers, which start a funnel, their priority and how they convert. Don't build a second starting offer for the same shoppers without agreeing which one wins (higher `offer_priority` is considered first).
3. `post_purchase_upsells.discover` for the templates. Pick one that fits the offer (a single product, a subscription upgrade).

## 2. Design it

- **Product:** a specific product (`products.search`, then its Shopify variant ID), or the most or least expensive item in their cart ("get another at 25% off" works well for consumables). To offer a subscription, the variant needs a real selling plan: its `purchase_options` from `products.search` name the plans it has. A product with none needs a plan first (`/subscribe-and-save`).
- **Discount:** post-purchase offers convert on a clear deal: 15–30% is typical, shown as the price before and after.
- **Who sees it:** everyone, or rules on what they bought, subtotal, quantity, country, first-time customers, customer tags, order count, currency, language, a random share of orders, or a date window. Collection and discount-code rules don't work after purchase; use products, tags or types instead.
- **Funnel:** up to three steps. Set what follows a yes (`accepted_next_upsell_setting_id`) and a no (`declined_next_upsell_setting_id`), for example a cheaper downsell after a no. Each offer shows at most once per order.
- **Copy:** a headline that names the deal ("One-time offer: add a second bottle for 25% off"), a line on why it pairs with what they bought, and optional blocks such as a review or an FAQ. Use a timer only if the offer really ends with the page.

## 3. Check, save, publish

1. Save each step as a draft (`post_purchase_upsells.save` with the template and a new `operation_id`), then link the steps by editing the first.
2. Prove the targeting: `post_purchase_upsells.check_trigger` with the saved rules and one or two real recent orders the merchant knows, one that should match and one that shouldn't. Report what matched and why. Shopify can still skip post-purchase pages for some orders (some payment methods), so say so.
3. Show the merchant the whole funnel: each step's product, price before and after, copy, and what happens on yes and no.
4. On a clear yes, `post_purchase_upsells.publish` with `live`, or `scheduled` with a start and optional end (with time zone) for a sale period.

Offer next: read its funnel numbers in a week (`/checkout-audit`) or test a variant (`/upsell-experiment`).
