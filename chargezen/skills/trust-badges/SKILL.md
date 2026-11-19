---
name: trust-badges
description: Add trust badges to the Shopify checkout with Chargezen CheckoutOS — secure payment, free shipping, easy returns, ratings, made-in or guarantee badges, with icons and short lines — shown to everyone or only to some carts (first-time customers, big orders, certain products or countries), saved as a draft, previewed and turned on only on the merchant's OK. Use when someone wants to reassure shoppers at checkout or reduce checkout drop-off.
argument-hint: "[what to reassure about]"
---

# Trust badges

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

1. **Placement:** `chargezen.checkout_extensions.discover.v1`; if the trust badge block isn't `placed`, give the merchant the checkout editor link.
2. **What exists:** `chargezen.trust_badges.list.v1`, so you don't add a second set the same shoppers see.
3. **Write the badges.** Three is the sweet spot. Each one is an icon (lock, store, delivery, star, return, cart), a short title and an optional line. Only promise what the store really offers: ask the merchant for their free-shipping threshold and their returns window rather than guessing. Good defaults:
   - lock: "Secure checkout", "Encrypted payment"
   - return: "30-day returns", "Not happy? Send it back"
   - delivery: "Ships in 1–2 days"
   Shopify sets the fonts and colors; pick a tone per icon and a layout (small or large icon stack, or horizontal).
4. **Who sees them:** everyone, or rules such as first-time customers, subtotal over an amount (reassurance matters most on big orders), certain products or shipping countries.
5. Save the draft (`chargezen.trust_badges.create.v1` with a new `operation_id`), `chargezen.trust_badges.preview.v1`, and show the merchant exactly what shoppers will read.
6. On a clear yes, `chargezen.trust_badges.activate.v1`.
