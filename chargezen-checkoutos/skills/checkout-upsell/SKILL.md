---
name: checkout-upsell
description: Add or change a product upsell inside the Shopify checkout with Chargezen CheckoutOS — which products to offer, the discount, who sees it (cart contents, subtotal, country, language, subscribers), the layout and the copy — saved as a draft, shown to the merchant, and turned on only on their OK. Use when someone wants to offer an add-on, a "complete the routine" product or a subscribe option at checkout.
argument-hint: "<what to offer> [to whom, discount]"
---

# Checkout upsell

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

## 1. Check the checkout first

1. `checkout_extensions.discover`: if the checkout upsell block isn't `placed`, give the merchant the checkout editor link and ask them to add the Chargezen upsell block. Nothing shows until they do.
2. `checkout_upsells.list` with each campaign's status and priority. Checkout shows only the **first** active campaign, in priority order, whose rules match, so a new campaign for the same shoppers as an existing one needs a priority decision. If one already does what they ask, offer to edit it instead.
3. `checkout_extensions.triggers` for the conditions checkout can check.

## 2. Build the offer

- **Products:** `products.search`; pass each `product_selection` unchanged. Suggest what pairs with what's in the cart (a refill with the device, the matching conditioner), not the store's best seller by default. Products are offered at quantity one; `purchase_options: "buyer_choice"` lets the shopper pick one-time or a subscription plan the product has.
- **Discount:** none, a percentage or a fixed amount per product. 10–20% is common for add-ons. With `skip_discount_if_discounted` on, shoppers who already have a code get the offer at full price; suggest it when margins are thin.
- **Who sees it:** "everyone", or conditions such as cart contains a product or collection, subtotal above or below an amount, quantity, shipping country, language, or subscription in the cart. First-time-customer targeting isn't available at checkout; it is for post-purchase (`/post-purchase`).
- **Layout:** one product (`SingleProductupsells`), a stack, a carousel or checkboxes. Keep `hide_if_in_cart` on so nobody is offered what they're already buying, and `hide_out_of_stock` on.
- **Copy:** a short title ("Complete your routine"), an accept label ("Add"), and optional blocks: a badge, a review quote, a short timer only if the offer genuinely ends.

## 3. Show, save, go live

1. Show the merchant what a matching shopper will see: title, each product with its price before and after the discount, the button, and who it shows to in one plain sentence.
2. Save it as a draft (`checkout_upsells.save` with a new `operation_id`).
3. If another active campaign targets the same shoppers, agree the order and set it with `checkout_upsells.priority`.
4. On a clear yes, `checkout_upsells.status` to `active`. This republishes the shared upsell discount in Shopify: read the publication result and report any error.

Offer next: an A/B test against a variant (`/upsell-experiment`), and a check on its numbers after a week or two.
