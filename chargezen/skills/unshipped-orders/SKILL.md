---
name: unshipped-orders
description: A read-only check of orders that haven't shipped in the merchant's Shopify store through Chargezen — a fulfillment status count for the period, then the orders waiting longest, on hold, rejected by the warehouse or with a cancellation requested, by location — ending with what to do about each, and optional delay notes to customers on the merchant's OK. Use when they ask which orders haven't shipped, what's late or stuck, or for a fulfillment report.
argument-hint: "[days, default 14] [late after N days, default 3]"
---

# Unshipped orders

Period and threshold: $ARGUMENTS (orders from the last 14 days, late when still unshipped after 3 days, if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person asks for customer notes. Use timestamps with a UTC offset; once a report names the store's time zone, use its midnight and say which period you used.

## 1. The overall picture

`shopify_reports.fulfillment_status` for fulfillment orders created in the period: counts of fulfillment orders, items and remaining quantity for each status and warehouse request status. Statuses are what they are now, not at the end of the period. If `not_visible_categories` is set, name those locations as not checked wherever you give a count.

`shopify_locations.list` (all pages) to name locations.

## 2. The orders that need attention

Use `admin_shopify_fulfillment_orders.search` with `filters` (`time_field: "created_at"`, the period), reading every page (`next_cursor`) before treating a list as complete:

1. **On hold:** `status: "ON_HOLD"`. Note the hold reason from `admin_shopify_fulfillment_orders.get`.
2. **Rejected or stuck at the warehouse:** `request_status: "REJECTED"`, then `"CANCELLATION_REQUESTED"`.
3. **Late:** `status: "OPEN"` and `"IN_PROGRESS"` created more than the threshold ago (set `to` to now minus the threshold).
4. **Incomplete:** `status: "INCOMPLETE"`.

Add `location_id` to look at one warehouse. For each order you'll name, `admin_shopify_orders.get` for the order number, customer, date, items and whether it's paid. Read at most 25 orders in detail; above that, give counts by location and status and list the oldest.

## 3. Report

Lead with the headline: how many orders are unshipped, how many are late, and the oldest wait. Then a short list per group (on hold, rejected, late), oldest first: order number, customer first name, days waiting, location, and the likely fix:

- **On hold:** release it once the reason is sorted (an address check, a fraud review, payment pending).
- **Rejected by the warehouse:** resend the request or move it to another location.
- **Late at one location:** the location is behind; consider moving orders.

These tools read only; releasing holds, rerouting or creating fulfillments need a change. Offer to hand that to Concierge with `/ask-concierge`, which asks before it acts.

## 4. Delay notes, on their OK

If they want customers told, draft one short message per customer (or one template with each order's real details filled in): an apology, that the order is on its way soon, no delivery date promised. Show the drafts together. On a yes:

- in a customer's existing conversation, `inbox.reply`;
- otherwise `inbox.compose` by email or text to the contact on the order.

Each with a new `operation_id` and the approved words. Texts to people who opted out aren't sent; report who got a note and who didn't.
