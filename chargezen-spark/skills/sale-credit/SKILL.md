---
name: sale-credit
description: Read-only check of whether a sale was credited to a Spark! partner in Chargezen, and why — which partner, through a tracked link or a discount code, what commission it earned, its status, any refund that took commission back, and the payout it's in — or, when no credit is found, the program settings that explain why. Use when a creator says a sale wasn't credited, asks where a commission went, or a merchant asks which partner gets credit for an order.
argument-hint: "<order number, partner name or date>"
---

# Sale credit check

The question: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; Spark! tools here don't add, move or remove credit.

## 1. Find the credited order

Credited orders come from `chargezen.admin_spark_referred_orders.list.v1`. Narrow it with what you know:

- **a partner:** `chargezen.admin_spark_partners.list.v1` with `query` (name, email or company), then `partner_id`;
- **a date:** `from` and `to` around it (credit time is when the order was credited, usually right after purchase);
- **an order number:** read the matching pages and compare `shopify_order_id` (or `stripe_invoice_number` for a Stripe payment). Ask for the date or partner if the list is long.

Read every page you need (`pagination.total_pages`).

## 2. Explain it

If you find it, `chargezen.admin_spark_referred_orders.get.v1`:

- which partner, and how: `attribution_source` (`affiliate_track` or `click_token` is a tracked link, `promo_code` a discount code), with the link or code;
- commission earned now and originally, and the commission status (`pending`, `processed`, `paid`, `in_dispute`, `revoked`);
- refunds: `refunded_commission` and the adjustments, applied or still open;
- the payout it's in, if any: `chargezen.admin_spark_partner_payouts.get.v1` for its status and payment date.

The rate and discount saved on the order are raw values without a percentage or fixed type; don't present them as money.

## 3. If there's no credit

Say plainly no credited order was found for what you searched, and what you searched. Then read `chargezen.admin_spark_partner_settings.get.v1` and give the settings that commonly explain it, without claiming which one applied: the attribution window (`cookie_duration_days`), whether self-referrals earn (`allow_self_referral`), and, for the partner, `chargezen.admin_spark_partners.get.v1` for whether they're `active` and which links and codes they have. These records can't show clicks for one shopper or Shopify payment state.

## 4. Answer

Lead with yes or no and one line on why. Then the detail above. If a credit needs fixing, Chargezen's Spark! admin is where the team reviews orders: give the page with `chargezen.admin_spark_partner_app.guide.v1` (`orders`). Don't promise a change.
