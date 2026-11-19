---
name: product-swap
description: Move every active subscriber of one product onto a replacement in Chargezen — for a discontinued product, a sold-out flavor or a new version — by finding everyone subscribed to it, showing the replacement with its price and stock, and swapping each subscription only after the merchant approves the whole batch. Use when a product is discontinued, out of stock for a while, or being replaced.
argument-hint: "<product being replaced> [replacement]"
---

# Product swap

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. Covers subscriptions that run on Chargezen (Shopify).

## 1. Who has it

1. `chargezen.products.search.v1` for the product being replaced; keep its `product_selection.product_id`.
2. `chargezen.admin_customer_subscriptions.find.v1` with that `product_id` and `statuses: ["ACTIVE", "PAUSED"]`. Page through all of them. Tell the merchant how many active and paused subscriptions have it, and how many units renew in the next 30 days.

## 2. What it becomes

For the first subscription, `chargezen.admin_customer_subscriptions.list_swap_options.v1` and find the replacement the merchant named among that item's replacements. Show it with its recurring price, stock and whether it's for sale, and the price difference per order.

If the replacement isn't offered as a swap for this product, say so: it has to be added as a swap option in Chargezen first. If the price changes, make sure the merchant is fine with every subscriber paying the new price from their next order.

## 3. Approve once, swap each

Get one clear yes for the batch: the product, the replacement, the price per order, how many subscriptions, and that **each customer gets the store's product-swap email and text** (as the store's notifications are set up).

Then for each subscription, one at a time:
1. `chargezen.admin_customer_subscriptions.list_swap_options.v1` for that subscription (each subscription's result is its own);
2. `chargezen.admin_customer_subscriptions.swap_product.v1` with that result's `subscription` object unchanged and the line and replacement indexes for this product and replacement.

If one fails (price or stock changed, or the replacement isn't offered for it), skip it, note why, and carry on. Report at the end: swapped, skipped with reasons, and any paused subscriptions left as they were if the merchant chose to leave them.
