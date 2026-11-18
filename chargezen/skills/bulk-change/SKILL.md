---
name: bulk-change
description: Make the same change to many subscriptions in Chargezen at once — push back or skip everyone's next order of a product during a stock-out, move renewals off a holiday, pause a group until a date, change how often they ship, apply a discount code, or cancel a set — by finding exactly who matches, showing the list and what each customer is told, then changing each one only after one approval for the batch. Use when they want to change all subscriptions of a product, everyone renewing on certain days, or every paused or active subscriber. For swapping a product on every subscription, use /product-swap.
argument-hint: "<who> <change>"
---

# Bulk change

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. Covers subscriptions that run on Chargezen (Shopify); Recharge and Stripe-backed ones aren't found here. To replace one product with another, use `/product-swap` instead.

## 1. Find who matches

`admin_customer_subscriptions.find` with the filters that fit, all of which must match:

- a product: `products.search`, then its `product_selection.product_id`;
- a status: `statuses` (`ACTIVE`, `PAUSED`; most changes need `ACTIVE`);
- renewing on certain days: `next_charge_from` and `next_charge_to` (store time zone), with `sort: "next_charge"`.

Read every page. Leave out any with a null `customer_ref`; they can't be changed here, so count them separately. Tell the person how many match and show the first ten (customer, product, next charge, price).

## 2. Agree the change

One change for the whole batch:

| Change | Tool | What to settle |
|---|---|---|
| Move the next order to a date | `admin_customer_subscriptions.reschedule_next_charge` | the date (or "two weeks later than each one's current date") |
| Skip the next order | `admin_customer_subscriptions.skip_next` | uses each subscription's own next charge date from the same result |
| Pause | `admin_customer_subscriptions.pause` | until a date (`resume_on`) or until resumed |
| How often it ships | `admin_customer_subscriptions.update_frequency` | interval and count |
| Discount code | `admin_customer_subscriptions.apply_discount` | the exact code they give; never suggest one |
| Cancel | `admin_customer_subscriptions.cancel` | that it can't be undone here |

Say what each customer gets: skip and pause send the store's skipped-order or paused email and text, as the store's notifications are set up. For the other changes, read the tool's description and say what it states; if it says nothing, tell the person you can't confirm from here whether customers are told.

## 3. Approve once, change each

Get one clear yes on: who (the count), the change, and what customers are told. Then go one subscription at a time, passing `customer_ref` and `subscription_ref` unchanged (and, for skip, that item's `next_charge_at`). If a call returns `CONFIRMATION_REQUIRED`, repeat it with its `confirmation_token` only because it's exactly the change they approved for the batch.

If one fails (not active any more, a code Shopify refuses), skip it, note why and carry on. Don't retry a different way without asking.

## 4. Report

Changed, skipped with reasons, and left out (not changeable here). Offer to read them back with `find` to confirm the new dates.
