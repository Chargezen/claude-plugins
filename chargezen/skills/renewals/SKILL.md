---
name: renewals
description: Read-only preview of the subscriptions in Chargezen that renew in the coming days — how many orders, what's in them, roughly what they'll bring in, which products need stock, and anything that needs a look first — so the merchant can plan packing and inventory. Use when someone asks what's renewing this week, what to pack, or what stock they need for upcoming subscription orders.
argument-hint: "[days, default 7]"
---

# Renewals

Window: today through the next $ARGUMENTS days (7 if no number was given), in the store's time zone.

Follow the `chargezen` skill for how to reach the tools. **Use only reads.**

1. `chargezen.admin_customer_subscriptions.find.v1` with `statuses: ["ACTIVE"]`, `next_charge_from` and `next_charge_to` for the window, `sort: "next_charge"`. Page through every result.
2. Add up per day and per product: how many orders, how many units, and the recurring total by currency (from each subscription's stored price; say it's before shipping and taxes).
3. If this connection has `chargezen.shopify_reports.inventory.v1` (the full Chargezen and Concierge addresses do; Subscriptions alone doesn't), check stock for the products with the most units and flag any where available stock is below the units renewing. Otherwise list the units so the merchant can check stock themselves.
4. Note anything to check before the charge runs: a subscription whose products no longer exist or are unavailable.

## Report

Lead with the total orders and recurring revenue in the window, then a short day-by-day table, then the packing list (product, units), then stock warnings. Offer the next useful step: skip or delay the affected orders through `/subscription-help`, or swap an out-of-stock product with `/product-swap`.
