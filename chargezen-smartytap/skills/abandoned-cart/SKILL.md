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

Start with abandoned checkout if they have none: it is closest to a sale. `chargezen.workflows.list.v1` first; if a flow already uses that trigger, read it with `chargezen.workflows.get.v1` and offer to improve it instead.

## 2. Settings that matter

- **Stop when they buy:** profile filter history `placed_order` equals 0 `since_flow_start`. Profile filters are checked before every step, so a shopper who orders leaves the flow.
- **Re-entry:** `after_period` of 30 days, so a regular browser isn't emailed every visit.
- **Smart sending** stays on (the default) so they aren't also hit by a campaign the same day.
- These flows send marketing only: people need email or text consent.
- **Personalization:** the checkout and cart triggers fill `{{ event.checkout_url }}`, the cart or checkout total and each item (`{{ item.title }}`, `{{ item.image_url }}`, `{{ item.url }}`); browse fills `{{ product.title }}` and `{{ product.url }}`. Texts can use only the trigger's `sms_tokens`. Use only tokens `chargezen.workflows.authoring_options.v1` lists for that trigger.
- **Offer:** better saved for the second message, if at all. It must be a code that exists in their store, named exactly; this connection can't check codes, so ask.

## 3. Build it as a draft

1. `chargezen.workflows.authoring_options.v1` for senders and whether texts can send. If texts aren't ready, the flow can still be built; say which setup step is left and that its text steps won't send until then.
2. **Start from the library:** `chargezen.workflows.list_templates.v1`, then `chargezen.workflows.create_from_template.v1` with the matching `template_key` (`abandoned_checkout`, `abandoned_cart` or `browse_abandonment`) and a new `operation_id`. Each comes with the timing, stop rule and re-entry above, an email started from the Abandoned cart or Browse abandonment starter, and a text where the table has one. It's a Draft that sends nothing. Keep that `operation_id` for any retry: a new one makes a second flow.
3. `chargezen.workflows.get.v1` on the Draft; change what the merchant wants different (a wait, an offer step, dropping the text) with `chargezen.workflows.update.v2` from the revision you read, or only the texts with `chargezen.workflows.update_messages.v2`.
4. Write each email with `chargezen.email_documents.apply_ops.v1` at its address in `email_documents`: a subject like "You left something at checkout", the items, one button back to checkout, the unsubscribe link and mailing address.
5. Check texts with `chargezen.workflows.preview_sms.v1` (passing the flow's trigger), emails with `chargezen.workflows.preview_email.v2`, and the whole flow with `chargezen.workflows.check.v1`. Show the person each message, its timing and the stop rule.
6. Offer a test of each email and text to them: `chargezen.workflows.send_test.v1` with the step and a new `operation_id`, filled with a sample checkout and its items. It goes to them only; a test text costs credits like any text.

## 4. Turn it on

Only when they say so: `chargezen.workflows.activate.v1`. It reaches shoppers from now on. Offer to build the next of the three, then a check after two weeks with `/flow-health`.
