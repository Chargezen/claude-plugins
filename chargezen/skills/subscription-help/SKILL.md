---
name: subscription-help
description: Handle any request about one customer's subscription in Chargezen — skip, pause, resume, cancel, change the next charge date, how often it ships, quantity, a product swap, the delivery address, a discount code, or a link to update their card. Finds the customer and the right subscription, shows what will change and what the customer will be told, and acts only on the merchant's OK. Use whenever someone names a customer and wants something done to their subscription.
argument-hint: "<customer name, email or phone> [what they want]"
---

# Subscription help

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. These tools cover subscriptions that run on Chargezen (Shopify); for one on Recharge or Stripe, say it has to be changed there.

## 1. Find the right subscription

1. `customers.search` with what you were given. If several people match, show name, email and stored address and ask which one.
2. `admin_customer_subscriptions.search` for that customer (every status, so paused and canceled ones show too). If there's more than one, list them (products, how often, next charge, status) and ask which.
3. `admin_customer_subscriptions.get.v2` for the one chosen: products, price, cadence, next charge, address and card on file. Keep its `customer_ref`, `subscription_ref` and `next_charge_at` exactly as returned.

## 2. Say what will happen, then act on the OK

Before every change, tell the person in one or two lines: what changes, from what to what, and that **the customer gets the store's email or text about it** (as the store's notifications are set up). Then wait for a yes.

| They want | Tool | Watch for |
|---|---|---|
| Skip the next order | `skip_next` with the same `next_charge_at` | Only the very next charge. To bring it back: `restore_skipped_order` |
| Move the next charge | `reschedule_next_charge` | Needs an exact date. "Early March" isn't one: ask for the day |
| Pause | `pause` | Ask whether it should resume on a date (`resume_on`, an exact day) or stay paused |
| Resume | `resume` | |
| Ship the next order now | `order_now.v2` | **Charges their saved card right away.** Say the amount and get a clear yes. If it returns `ORDER_NOW_PROCESSING`, repeat the identical call a few seconds later; if it needs bank approval, share the link it returns |
| Change how often | `update_frequency` | Billing and delivery move together |
| Change quantity, or remove an item from every order | `update_quantity` / `remove_item` | For the next order only, use `/next-order` |
| Swap a product | `list_swap_options`, then `swap_product` | Show the replacements with price and stock; pass the result back unchanged |
| New delivery address | `update_shipping_address` | Read the full address back first |
| Add a discount code | `apply_discount` | The code must already exist in Shopify |
| New card | `request_payment_method_update` | Emails the customer a secure link. Never take card details in the chat |
| Cancel | `cancel` | See below |

## 3. Before canceling

Canceling is immediate, and the customer gets the store's cancellation email and text; there's no silent cancel. If the person hasn't said the customer insists, offer the alternatives in one line: skip the next order, pause until a date, ship less often, or swap the product. Cancel only on a clear yes.

## 4. Confirm

Report what changed with the new next charge date and status the tool returned, and offer a short reply the merchant can send the customer. If anything returned an error, say what it means in plain words and what to try instead.
