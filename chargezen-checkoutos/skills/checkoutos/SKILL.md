---
name: checkoutos
description: Use when the user wants to create, change, audit or improve their Shopify checkout with Chargezen CheckoutOS — checkout upsells, post-purchase offers and funnels, A/B experiments, discount functions, cart transforms, checkout validations, trust badges, thank-you texts, address verification, gift-card designs or checkout branding — or asks how their upsells are performing.
---

# Chargezen CheckoutOS

The `chargezen-checkoutos` MCP server acts for the merchant who connected it, on their Shopify store. Chargezen enforces their permissions and plan; don't check those yourself. If a call says CheckoutOS access is missing, tell the merchant they need CheckoutOS on their Chargezen workspace and an admin role that can manage it.

## How to reach the tools

Only discovery is loaded directly. List what this connection can do with `chargezen.tools.index.v1`, read the contracts you need with `chargezen.tools.describe.v1`, then run reads through `chargezen.tools.call_read.v1` and changes through `chargezen.tools.call_write.v1`. Each tool's description and schema are the contract: follow them rather than guessing field shapes.

## The order that works

1. **Confirm the block is on the checkout.** Run `checkout_extensions.discover`. If the block for the surface you're working on isn't `placed`, give the merchant the checkout editor link it returns and ask them to add the Chargezen block. Nothing you configure reaches shoppers until they do.
2. **Read what exists first.** List and get the current campaigns or offers, their status and priority. Read `checkout_extensions.triggers` before writing targeting rules.
3. **Select real records.** Products come from `products.search`, collections from `products.search_collections`, customers from `customers.search`. Pass each selection through unchanged.
4. **Save a draft.** Create with a fresh `operation_id` UUID and keep the same UUID and inputs if you retry. Use the family's preview tool where one exists and show the merchant what shoppers will see.
5. **Go live only when the merchant says so.** Activating or publishing changes their live checkout and may republish a Shopify discount. After it, check the publication result in the response and report any error plainly.

## Optimizing

Start from data, not taste:

- Read `upsell_analytics.get` for an explicit window (with timezone offsets; 30 days is a sensible default) and `post_purchase_upsells.funnels` for post-purchase.
- Compare offers on conversion (shown → accepted/purchased) and revenue per view, not raw revenue alone. Call out offers with too few views to judge.
- Pick the one change most likely to move the weakest high-traffic offer: the product offered, the discount depth, the trigger audience, the layout or the copy.
- Prefer testing over editing a working offer in place: duplicate it (`checkout_extensions.duplicate`), change one thing, then start an experiment with `upsell_experiments.create`. The merchant chooses the challenger percentage.
- Tell the merchant when to come back to read the result, and end experiments with `upsell_experiments.end` once there's a clear winner.

Never invent performance numbers; if analytics returns nothing for the window, say so.
