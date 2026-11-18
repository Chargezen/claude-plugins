---
name: abandoned-cart
description: Build SmartyTap recovery flows in Chargezen for shoppers who started checkout, added to cart or looked at a product and didn't buy — a timed email, then a text, with their items and a link back, stopping as soon as they order — saved as drafts, previewed, and turned on only on the merchant's OK. Use for abandoned checkout, abandoned cart or browse abandonment messages.
argument-hint: "[checkout | cart | browse] [offer]"
---

# Abandoned cart and checkout

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Pick the flow

Three triggers, from the store's Chargezen pixel. Only shoppers the store has identified (a known email or phone) enter; anonymous visitors never do.

| Flow | Trigger | Timing Chargezen recommends |
|---|---|---|
| Abandoned checkout | Checkout Started (`chargezen.pixel.checkout_started`) | wait 1 hour, email; wait 23 hours, text |
| Abandoned cart | Added to Cart (`chargezen.pixel.added_to_cart`) | wait 4 hours, email; wait 20 hours, text |
| Browse abandonment | Viewed Product (`chargezen.pixel.product_viewed`) | wait 2 hours, one email |

Start with abandoned checkout if they have none: it is closest to a sale. `workflows.list` first; if a flow already uses that trigger, read it with `workflows.get` and offer to improve it instead.

## 2. Settings that matter

- **Stop when they buy:** profile filter history `placed_order` equals 0 `since_flow_start`. Profile filters are checked before every step, so a shopper who orders leaves the flow.
- **Re-entry:** `after_period` of 30 days, so a regular browser isn't emailed every visit.
- **Smart sending** stays on (the default) so they aren't also hit by a campaign the same day.
- These flows send marketing only: people need email or text consent.
- **Personalization:** the checkout and cart triggers fill `{{ event.checkout_url }}`, the cart or checkout total and each item (`{{ item.title }}`, `{{ item.image_url }}`, `{{ item.url }}`); browse fills `{{ product.title }}` and `{{ product.url }}`. Texts can use only the trigger's `sms_tokens`. Use only tokens `workflows.authoring_options` lists for that trigger.
- **Offer:** better saved for the second message, if at all. It must be a code that exists in their store, named exactly; this connection can't check codes, so ask.

## 3. Build it as a draft

1. `workflows.authoring_options` for senders, starter designs (Abandoned cart, Browse abandonment) and whether texts can send. If texts aren't ready, build email only and say what setup step is left.
2. `workflows.create` with `status: "draft"` and a new `operation_id`. Start emails from the Abandoned cart or Browse abandonment starter.
3. Write each email with `email_documents.apply_ops` at its address in `email_documents`: a subject like "You left something at checkout", the items, one button back to checkout, the unsubscribe link and mailing address.
4. Check texts with `workflows.preview_sms` (passing the flow's trigger) and emails with `workflows.preview_email`. Show the person each message, its timing and the stop rule.

## 4. Turn it on

Only when they say so: `workflows.activate`. It reaches shoppers from now on. Offer to build the next of the three, then a check after two weeks with `/flow-health`.
