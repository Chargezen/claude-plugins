---
name: new-subscription
description: Start a subscription in Chargezen for an existing customer on the card they already have saved — the product and variant, a priced plan (how often it ships and its discount), quantity, first billing date and an optional extra discount — confirmed with the merchant before it's created. Use when someone wants to sign a customer up, set up a subscription by phone or email, or comp a free subscription.
argument-hint: "<customer> <product> [how often, quantity, first billing date]"
---

# New subscription

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Select exactly

1. **Customer:** `customers.search`. Confirm the right person by email and address. If they don't exist yet and the merchant wants to add them, `customers.create`.
2. **Product:** `products.search`; pick the exact variant (size, flavor). Keep its `product_selection` as returned.
3. **Plan:** `admin_subscription_plans.list` with that `product_selection`. Each `subscription_selections` entry is a priced plan for this variant. Show the options as the customer would read them ("Every 4 weeks, 15% off: $25.50 per order") and pick the one the merchant asked for. Pass the chosen `subscription_selection` on unchanged; never assemble it from separate results. If none fits, offer `/subscribe-and-save` to create the plan first.

## 2. Settle the details

Ask only for what's missing:
- **quantity** per delivery;
- **first billing date**, an exact day (never pick one yourself);
- an optional **extra discount**, percentage or fixed amount (100% makes it free);
- the **delivery address**, if not the customer's default.

## 3. Confirm, then create

Show one summary: customer, product, plan, quantity, price per order after discounts, first billing date, address, and that it uses the card the customer already has saved, with nothing charged today. On a yes, `admin_customer_subscriptions.create.v2` with a new `operation_id` (keep it, with the same inputs, for any retry).

- `SUBSCRIPTION_PAYMENT_METHOD_REQUIRED`: the customer has no saved card. They need to add one through the store; never take card details in the chat.
- Follow `admin_customer_subscriptions.get_creation` with the returned `subscription_contract_id` until it gives the local reference, then report the actual next billing date it read back (Shopify may adjust it).
