---
name: subscribe-and-save
description: Set up a subscribe-and-save offer for one or more products in Chargezen — delivery options (for example every 2, 4 or 6 weeks), the subscriber discount and where customers see it — checking what's already there, showing the merchant exactly what shoppers will see, and creating it in Shopify only on their OK. Use when they want to sell a product on subscription, add delivery options, or change the subscriber discount on new plans.
argument-hint: "<product> [discount, delivery options]"
---

# Subscribe and save

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. Saving a plan changes the purchase options shoppers see on the product, so nothing is created until the person agrees to the exact plan.

## 1. Find the product and what it already has

1. `chargezen.products.search.v1` for the product. Keep its `product_record_id` exactly as returned; never substitute a Shopify ID.
2. Each variant's `purchase_options` lists the plans shoppers can already buy it with. If any names a plan, find that group in `chargezen.admin_selling_plan_groups.list.v1` (its `shopify_id` equals the `plan_ref`'s `selling_plan_group_id`) and `chargezen.admin_selling_plan_groups.get.v1` its `record_id`. Show it and ask whether they want another option in it or a separate plan; don't create a duplicate by accident.
3. If they say they had a plan before that shoppers can't see, `chargezen.admin_selling_plan_groups.list.v1` with `active: false` and offer to reuse it rather than create a new one.

## 2. Propose the plan

Suggest a starting point, then adjust to what they say:

- **Name customers see:** "Subscribe and save". **Selector title:** "Delivery".
- **Delivery options:** every 2, 4 and 6 weeks for consumables someone uses up monthly; every 1 and 2 months for slower ones. Billing matches delivery unless they want prepaid.
- **Discount:** 10% to 15% off each order is common; make it the same across options unless they want to reward longer gaps. Use exact decimals.
- **Where it shows:** online store, customer portal and subscription detail on; contract import off unless they're importing.
- **Commitment:** none by default. A minimum number of orders only if they ask.

Show it as shoppers will read it: the selector title, each option's label ("Every 4 weeks, save 15%") and the price per order at the product's current price.

## 3. Create it

On their OK, `chargezen.admin_selling_plan_groups.create.v2` with a new `operation_id`, `plan_type: "fixed_price"`, every option's full configuration and the product in `catalog_assignments`. Keep the same `operation_id` and configuration if you retry.

Read the result: it can be `saved`, `partial` or `outcome_unknown`. Report exactly what was confirmed. Never send an `outcome_unknown` creation again; read the group with `chargezen.admin_selling_plan_groups.get.v1` and tell the person what's there.

## 4. Check it

`chargezen.admin_subscription_plans.list.v1` with the new group and the product, to confirm the priced options shoppers get. Then suggest they open the product page on their store to see the new options as a shopper would.
