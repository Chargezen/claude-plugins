---
name: order-status
description: Answer "where is my order" for one customer in Chargezen — find the order by number, email, phone or name, read its live Shopify status, fulfillment orders, holds and tracking, explain in plain words where it is and what happens next, and draft a reply for the merchant to approve before it goes to the customer in their inbox conversation. Use when a customer asks where their order is, when it will ship, or for tracking, or when the merchant wants to check one order.
argument-hint: "<order number, email, phone or customer name>"
---

# Order status

Looking up: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Find the order

- **An order number:** `admin_shopify_orders.search` with `order_number` exactly as given, store prefix included.
- **An email, phone or name:** `customers.search`, confirm the right person (ask if several match or the address differs), then `admin_shopify_orders.search` with their `customer_ref`. It returns their 15 newest saved orders; ask which one if it isn't clear.
- **From the inbox:** the customer's details are on the conversation (`inbox.get`).

## 2. Read where it is

1. `admin_shopify_orders.get` with the order's exact ID: the live Shopify view with items, payment and fulfillment status, shipping address, tags and tracking.
2. `admin_shopify_fulfillment_orders.search` with that `order_id`, then `admin_shopify_fulfillment_orders.get` on any that are still open: which location is sending it, holds (and their reason), and items still to ship.

Work out the plain answer:

| What the tools show | Tell them |
|---|---|
| Fulfilled, with tracking | It shipped on <date> with <carrier>; the tracking link. Shopify's records don't confirm delivery. |
| Partly fulfilled | What shipped (with tracking) and what's still to come |
| Open or in progress, no hold | It's being prepared at <location>; ordered <date> |
| On hold | It's paused (say why only if the hold reason is customer-safe, such as an address check); flag it to the merchant |
| Fulfillment request rejected or cancellation requested | Something went wrong with the warehouse; this needs the merchant |
| Cancelled or refunded | It was cancelled on <date>; refunds follow the payment status |

Never promise a delivery date: these tools don't predict delivery. If the address looks wrong or incomplete, tell the merchant before replying.

## 3. Draft the reply

Greet the customer by first name, give the answer above with real dates and the tracking link, and say what happens next. Keep texts under 300 characters. Show the merchant the facts you checked and the draft; offer send, edit or skip.

## 4. Act on their OK

- **Reply in an existing conversation:** `inbox.reply` with a new `operation_id` and the approved words exactly. It can't be unsent.
- **No conversation yet:** `inbox.compose` by text or email to the address on the order, with the approved words.
- **It needs a change** (cancel, a new shipment, a hold released, a refund or return): this connection can't do those directly. Offer to hand it to Concierge with `/ask-concierge`, which asks the merchant to approve before it acts, or to assign the conversation to a teammate (`inbox.assignable_teammates`, `inbox.assign`).

Report what was sent and anything left for a teammate.
