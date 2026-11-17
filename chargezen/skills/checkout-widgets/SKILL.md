---
name: checkout-widgets
description: Add a widget to the Shopify checkout with Chargezen CheckoutOS — customer reviews, a rewards progress bar, live chat, gift-message and delivery-instruction checkboxes, an image banner, or line-item controls that let shoppers change variant or quantity, remove upsells or upgrade to a subscription — saved as a draft and published only on the merchant's OK. Use when someone wants social proof, a gift note, a chat button, a promo banner, or a subscribe-and-save upgrade inside checkout.
argument-hint: "<widget> [details]"
---

# Checkout widgets

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

1. **Placement:** `checkout_extensions.discover`; the block for this widget must be `placed`. Give the merchant the editor link if not.
2. **What exists:** `checkout_widgets.list` for this type. Reviews, rewards bar, live chat and cart controls show **one** campaign at a time; order notes and banners can run several (each placed block names the campaign it shows).
3. **Build it:**

| Widget | Good defaults |
|---|---|
| **Reviews** | Two or three real reviews with the reviewer's name and a "Verified buyer" badge. Use only reviews the merchant gives you or that exist; never write one |
| **Rewards bar** | Progress by subtotal toward their reward goal; "{AMOUNT} away from your reward" and "You've unlocked it!". Check the real reward with `admin_rewards.get_program` |
| **Live chat** | A short button ("Questions? Chat with us") and a welcome line using {first_name}, in the brand's colors. Publishing it turns the checkout chat channel on, so someone must answer it; chats land in the Chargezen inbox, and Claude can read and answer them there |
| **Order note** | Up to five checkboxes such as "This is a gift" with a gift-message box (set a character limit), or "Leave at the door". Save to the order note, or to order attributes if their fulfillment app reads those |
| **Banner** | An https image (from Shopify Files), alt text, a width up to 600px and an optional link |
| **Cart controls** | Variant and quantity changes, remove for upsells only, and a "Subscribe and save" upgrade button that switches a line to its first subscription plan. Lines only change where Shopify allows edits |

4. Save the draft (`checkout_widgets.save` with a new `operation_id`) and describe exactly what shoppers will see.
5. On a clear yes, `checkout_widgets.status` to `active`. If another campaign of that type is live, the call names it: ask whether to replace it, then repeat with `replace_live: true` only on their yes. Editing a widget that's already active changes checkout right away, so confirm edits too.
