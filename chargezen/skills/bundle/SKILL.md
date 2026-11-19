---
name: bundle
description: Create a product bundle at the Shopify checkout with Chargezen CheckoutOS cart transforms — sell a bundle product that expands into its parts for fulfillment, merge items bought together into one bundle line at a bundle price, or change how a product shows or is priced in the cart — saved as a draft, previewed, and activated only on the merchant's OK. Use when someone wants a bundle, a kit, a "buy these together" price, or a gift set.
argument-hint: "<the bundle> [price]"
---

# Bundle

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

## 1. Check what the store supports

1. `chargezen.cart_transforms.capabilities.v1`: merge and expand work on every plan; changing a line's price or look (`update`) needs Shopify Plus or a development store. If the plan lookup fails, that alone isn't proof it's unsupported.
2. `chargezen.cart_transforms.list.v1` so you don't duplicate a bundle.
3. Bundles apply to **one-time purchases only**; subscription lines and renewals are never transformed. Say so if they sell the parts on subscription.

## 2. Pick the kind

| They want | Rule |
|---|---|
| A bundle product shoppers buy as one item, shipped as its parts ("Starter kit" = cleanser + serum + cream) | `expand`: the bundle variant, its component variants and quantities; price by a percentage off the parts or fixed prices per component |
| Shoppers who add the parts get them combined into a bundle line at a bundle price | `merge`: the component variants and quantities, the bundle title and image, and the percentage off |
| Change one product's price or title in the cart (Plus) | `update` with a fixed price per unit |

Pick every product and variant with `chargezen.products.search.v1`; use the Shopify variant IDs it returns.

## 3. Preview and activate

1. Save the draft (`chargezen.cart_transforms.create.v1` with a new `operation_id`).
2. `chargezen.cart_transforms.preview.v1`, then show what the cart line will look like and the price math at today's prices: parts total, bundle price, saving.
3. Remind them that stock is tracked on the parts, so an expand bundle sells out when a part does.
4. On a clear yes, `chargezen.cart_transforms.activate.v1`, then `chargezen.cart_transforms.provider_status.v1` to confirm it's live in Shopify.
