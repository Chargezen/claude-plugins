---
name: order-tag-flow
description: Build a Chargezen flow that runs each time an order gets a tag in Shopify — email or text the customer, alert the team, hold the order from shipping, or tag it again — saved as a draft, previewed, and turned on only on the merchant's OK. Use for "when an order is tagged X, message the customer", wholesale or VIP order handling, fraud-review holds or custom order notices.
argument-hint: "<tag> <what should happen>"
---

# Order tag flow

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Pin down the tag and the action

- **The tag**, spelled exactly as it is in Shopify. Tags are matched as written.
- **Which trigger:**
  - Order tags added (`shopify.orders.tags_added`) with an `added_tags` filter (`includes_any`) runs once, at the moment the tag is added. This is the usual choice.
  - Order created or updated (`shopify.orders.updated`) with a `tags` filter runs for any order that has the tag, every time the order changes. Use it only with re-entry set so customers aren't messaged repeatedly.
- **What happens**, from the steps the options list for orders: email the customer, text the customer, **Internal alert** (emails confirmed team addresses; a new address must confirm first), **Hold fulfillment** (Shopify hold with a reason and note, so it doesn't ship), add or remove order tags, a **Webhook** (needs the teammate's two-factor sign-in to turn on), and **Split** for different paths, such as by `total_price` or `shipping_zip`.

`workflows.list` first: if a flow already watches that tag, read it with `workflows.get` and change it instead.

## 2. Build it as a draft

1. `workflows.authoring_options` for senders, the order tokens (`{{ order.name }}`, `{{ order.total_price }}`, `{{ order.tags }}`) and whether texts can send.
2. Message `purpose`: `transactional` when it's about this order (a status update, a delay, instructions), `marketing` if it promotes anything. Transactional skips the marketing opt-in; opted-out customers get neither.
3. `workflows.create` with `status: "draft"` and a new `operation_id`. Write each email with `email_documents.apply_ops` at its address in `email_documents`.
4. `workflows.preview_email` and `workflows.preview_sms` with trigger `shopify.orders.tags_added`.

## 3. Show and turn on

Show the person, in plain words: "When an order gets the tag *X*, …", each message, any hold or tag change, and who gets alerts. Only when they say so: `workflows.activate`. Orders tagged before then don't run it. Remind them that a hold stays until someone releases it in Shopify.
