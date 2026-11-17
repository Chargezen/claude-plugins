---
name: volume-discount
description: Create an automatic discount at the Shopify checkout with Chargezen CheckoutOS — quantity breaks ("buy 2 save 10%, buy 3 save 15%"), a product or order discount, free or capped shipping, a discount that only applies to one-time buyers or subscribers, or one that turns on for visitors from a campaign link — saved as a draft, previewed, and published to Shopify only on the merchant's OK. Use when someone asks for tiered pricing, bulk discounts, free shipping over a threshold, an automatic sale or a discount for a specific traffic source.
argument-hint: "<the deal> [products, dates]"
---

# Volume and automatic discounts

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

## 1. What exists

`discount_functions.list`, then `get` any that cover the same products, so the new one doesn't stack by accident. Check how existing ones combine with product, order and shipping discounts.

## 2. Shape the deal

Pick the type that matches what they said:

| They want | Set up |
|---|---|
| Buy more, save more | `product` discount with volume tiers: each tier a minimum quantity and its percentage or amount. `progressive` gives each tier's rate to the units in that band; `uniform` gives the whole line the highest tier reached. Uniform is easier for shoppers to understand |
| Money off certain products | `product` discount, specific products and variants (`products.search`) |
| Money off the whole order | `order` discount |
| Free or cheaper shipping | `shipping` discount, optionally limited to countries or to rates under a maximum cost |
| Only subscribers, or only one-time buyers | `purchase_type` |
| Only visitors from a campaign or influencer link | `trigger_type: "utm_source"` with the source value |
| A sale with dates | `starts_at` and `ends_at` with time zone |

Not supported here: collections (pick the products), minimum purchase amounts, customer eligibility, usage limits and discount codes. Say so and suggest Shopify's own discounts for those.

Agree how it **combines** with other product, order and shipping discounts. Stacking a volume discount with a sitewide sale can cost more than intended.

## 3. Preview and publish

1. Save the draft (`discount_functions.create` with a new `operation_id`).
2. `discount_functions.preview`, then show a worked example at real prices: "2 bottles: $48 → $43.20; 3 bottles: $72 → $61.20", plus who gets it and when.
3. On a clear yes, `discount_functions.activate`. Then `discount_functions.provider_status` to confirm Shopify has it live, and report any error plainly.

To end it later: `discount_functions.deactivate`.
