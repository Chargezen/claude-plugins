---
name: subscription-help
description: Handle any request about one customer's subscription in Chargezen — skip, pause, resume, cancel, change the next charge date, how often it ships, quantity, a product swap, the delivery address, a discount code, or a link to update their card. Finds the customer and the right subscription, shows what will change and what the customer will be told, and acts only on the merchant's OK. Use whenever someone names a customer and wants something done to their subscription.
argument-hint: "<customer name, email or phone> [what they want]"
---

# Subscription help

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. These tools cover subscriptions that run on Chargezen (Shopify); for one on Recharge or Stripe, say it has to be changed there.

## 1. Find the right subscription

1. `chargezen.customers.search.v1` with what you were given. If several people match, show name, email and stored address and ask which one.
2. `chargezen.admin_customer_subscriptions.search.v1` for that customer (every status, so paused and canceled ones show too). If there's more than one, list them (products, how often, next charge, status) and ask which.
3. `chargezen.admin_customer_subscriptions.get.v2` for the one chosen: products, price, cadence, next charge, address and card on file. Keep its `customer_ref`, `subscription_ref` and `next_charge_at` exactly as returned.

## 2. Say what will happen, then act on the OK

Before every change, tell the person in one or two lines: what changes, from what to what, and that **the customer gets the store's email or text about it** (as the store's notifications are set up). Then wait for a yes.

| They want | Tool | Watch for |
|---|---|---|
| Skip the next order | `chargezen.admin_customer_subscriptions.skip_next.v1` with the same `next_charge_at` | Only the very next charge. To bring it back: `chargezen.admin_customer_subscriptions.restore_skipped_order.v1` |
| Move the next charge | `chargezen.admin_customer_subscriptions.reschedule_next_charge.v1` | Needs an exact date. "Early March" isn't one: ask for the day |
| Pause | `chargezen.admin_customer_subscriptions.pause.v1` | Ask whether it should resume on a date (`resume_on`, an exact day) or stay paused |
| Resume | `chargezen.admin_customer_subscriptions.resume.v1` | |
| Ship the next order now | `chargezen.admin_customer_subscriptions.order_now.v2` | **Charges their saved card right away.** Say the amount and get a clear yes. If it returns `ORDER_NOW_PROCESSING`, repeat the identical call a few seconds later; if it needs bank approval, share the link it returns |
| Change how often | `chargezen.admin_customer_subscriptions.update_frequency.v1` | Billing and delivery move together |
| Change quantity, or remove an item from every order | `chargezen.admin_customer_subscriptions.update_quantity.v1` / `chargezen.admin_customer_subscriptions.remove_item.v1` | For the next order only, use `/next-order` |
| Swap a product | `chargezen.admin_customer_subscriptions.list_swap_options.v1`, then `chargezen.admin_customer_subscriptions.swap_product.v1` | Show the replacements with price and stock; pass the result back unchanged |
| New delivery address | `chargezen.admin_customer_subscriptions.update_shipping_address.v1` | Read the full address back first |
| Add a discount code | `chargezen.admin_customer_subscriptions.apply_discount.v1` | The code must already exist in Shopify |
| New card | `chargezen.admin_customer_subscriptions.request_payment_method_update.v1` | Emails the customer a secure link. Never take card details in the chat |
| Cancel | `chargezen.admin_customer_subscriptions.cancel.v1` | See below |

## 3. Before canceling

Canceling is immediate, and the customer gets the store's cancellation email and text; there's no silent cancel. If the person hasn't said the customer insists, offer the alternatives in one line: skip the next order, pause until a date, ship less often, or swap the product. Cancel only on a clear yes.

## 4. Confirm

Report what changed with the new next charge date and status the tool returned, and offer a short reply the merchant can send the customer. If anything returned an error, say what it means in plain words and what to try instead.
