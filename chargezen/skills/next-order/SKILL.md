---
name: next-order
description: Show what a customer's upcoming subscription orders will contain in Chargezen and change the next one only — set how many of an item it gets, take out a one-time add-on, bring back an order they skipped, or ship it now — without touching later orders. Use when someone asks what's in a customer's next box or wants just that order changed.
argument-hint: "<customer> [what to change on the next order]"
---

# Next order

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. Covers subscriptions that run on Chargezen (Shopify).

1. **Find it:** `customers.search`, then `admin_customer_subscriptions.search`; ask which subscription if there's more than one.
2. **Read the orders:** `admin_customer_subscriptions.upcoming_orders`. Show the next few orders by date with what each holds: recurring items, items for that order only, and any quantity that differs from usual. List skipped orders separately.
3. **Change the next order only**, on the merchant's OK:
   - quantity of an item on that order: `change_next_order_item` with `remove: false` and the new quantity;
   - take out an item that's on that order only: `change_next_order_item` with `remove: true`;
   - bind `scheduled_at`, `cycle_index` and `line_id` from the same `upcoming_orders` result, unchanged.

   A recurring item can't be taken out of one order: offer to skip the order or set its quantity instead. The only item on an order can't be removed.
4. **Bring back a skipped order:** `restore_skipped_order`.
5. **Ship it now:** `order_now.v2` charges the saved card immediately and places the order; follow the `/subscription-help` rules for it.
6. Read `upcoming_orders` again and show the next order as it now stands.

To change every future order instead, use `update_quantity`, `remove_item` or `/subscription-help`.
