---
name: plan-audit
description: Review every subscription plan in Chargezen — each group's delivery options, discounts, where it shows (store, customer portal) and which products carry it — and point out what's missing or inconsistent, such as products with no subscription option, plans hidden from the store, uneven discounts or switched-off groups. Read-only; offers fixes. Use when someone asks whether their subscription offers are set up right or what plans they have.
---

# Plan audit

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; offer changes at the end.

## Gather

1. `admin_selling_plan_groups.list` for every group (active or not).
2. `admin_selling_plan_groups.get` for each: its delivery options (billing and delivery cadence), each option's price adjustment, any minimum or maximum number of orders, the channels it shows on (online store, customer portal, subscription detail, contract import) and the products and variants it holds.
3. `products.search` for the store's best sellers (or the products the merchant names) and read each one's `purchase_options` to see which plans shoppers can actually choose.

## What to look for

- products people subscribe to, or best sellers, with **no subscription option** shoppers can choose;
- groups that are **switched off** or **hidden from the online store** while still holding products;
- the **same cadence priced differently** across groups, or discounts that don't reward longer gaps the way the merchant intends;
- options with a **minimum commitment** the merchant may not remember setting;
- duplicate groups offering the same thing.

## Report

A short table of the groups (name, options, discount, where it shows, product count), then the findings ranked by how many shoppers they affect, each with the fix. Offer to make a fix: a new plan through `/subscribe-and-save`, or a change the merchant makes in Chargezen's plan editor (these tools create plans but don't edit existing groups).
