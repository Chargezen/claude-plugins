---
name: checkoutos
description: Use when the user wants to create, change, audit or improve their Shopify checkout with Chargezen CheckoutOS — checkout upsells, post-purchase offers and funnels, A/B experiments, discount functions, cart transforms, checkout validations, trust badges, thank-you texts, address verification, gift-card designs or checkout branding — or asks how their upsells are performing.
---

# Chargezen CheckoutOS

Follow the `chargezen` skill for how to reach the tools and the rules every change follows. This skill adds what's particular to the checkout. If a call says CheckoutOS access is missing, tell the merchant they need CheckoutOS on their Chargezen workspace and a teammate role that can manage it.

Every CheckoutOS job has its own command: `/checkout-upsell`, `/post-purchase`, `/volume-discount`, `/bundle`, `/checkout-rules`, `/trust-badges`, `/thank-you-page`, `/checkout-widgets`, `/checkout-branding`, `/gift-card-design`, `/upsell-experiment` and `/checkout-audit`.

## The order that works

1. **Confirm the block is on the checkout.** Run `chargezen.checkout_extensions.discover.v1`. If the block for the surface you're working on isn't `placed`, give the merchant the checkout editor link it returns and ask them to add the Chargezen block. Nothing you configure reaches shoppers until they do.
2. **Read what exists first.** List and get the current campaigns or offers, their status and priority. Read `chargezen.checkout_extensions.triggers.v1` before writing targeting rules.
3. **Select real records.** Products come from `chargezen.products.search.v1`, collections from `chargezen.products.search_collections.v1`, customers from `chargezen.customers.search.v1`. Pass each selection through unchanged.
4. **Save a draft.** Create with a fresh `operation_id` UUID and keep the same UUID and inputs if you retry. Use the family's preview tool where one exists and show the merchant what shoppers will see.
5. **Go live only when the merchant says so.** Activating or publishing changes their live checkout and may republish a Shopify discount. After it, check the publication result in the response and report any error plainly.

## Optimizing

Start from data, not taste:

- Read `chargezen.upsell_analytics.get.v1` for an explicit window (with timezone offsets; 30 days is a sensible default) and `chargezen.post_purchase_upsells.funnels.v1` for post-purchase.
- Compare offers on conversion (shown → accepted/purchased) and revenue per view, not raw revenue alone. Call out offers with too few views to judge.
- Pick the one change most likely to move the weakest high-traffic offer: the product offered, the discount depth, the trigger audience, the layout or the copy.
- Prefer testing over editing a working offer in place: duplicate it (`chargezen.checkout_extensions.duplicate.v1`), change one thing, then start an experiment with `chargezen.upsell_experiments.create.v1`. The merchant chooses the challenger percentage.
- Tell the merchant when to come back to read the result, and end experiments with `chargezen.upsell_experiments.end.v1` once there's a clear winner.

Never invent performance numbers; if analytics returns nothing for the window, say so.
