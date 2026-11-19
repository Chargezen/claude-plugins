---
name: checkout-rules
description: Stop checkouts that would cause problems, with Chargezen CheckoutOS validation rules — block shipping certain products to certain countries or states, limit where subscriptions can ship, cap order weight per destination, keep company and address lines short enough for the carrier's label, or block specific customers by email or tag — each with the message shoppers see, saved as a draft and turned on only on the merchant's OK. Use when someone has shipping restrictions, carrier label errors, overweight orders, or customers they must stop ordering.
argument-hint: "<what to stop> [where]"
---

# Checkout rules

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

A rule that's on **blocks the shopper from paying** until they change their cart or address. Get each one right before it goes live: a too-broad rule loses real orders.

## 1. What's on now

`chargezen.checkout_validations.list.v1` and `chargezen.checkout_validations.provider_status.v1`: which rules are on, their order, and whether Shopify's validation is actually enabled.

## 2. Pick the rule

| They want to stop | Rule type | What it needs |
|---|---|---|
| Certain products shipping to certain countries or states (restricted ingredients, licensing) | `variant_geo_restriction` | The variants (`chargezen.products.search.v1`) and the country or state codes |
| Subscriptions shipping outside the countries they serve | `subscription_geo_restriction` | Allowed countries; optional exceptions for existing EU customers or customer tags |
| Orders over a weight per destination | `weight_limit` | Country or state codes and a maximum in pounds |
| Wrong weights on some variants for those limits | `variant_weight_override` | Each variant's weight in pounds |
| Address or company lines too long for the carrier label | `address_length` | Maximum characters |
| Specific customers ordering | `blocked_customer` | Emails or customer tags |

Write the **message shoppers see** for each rule in plain words with what to do next: "We can't ship Kava Calm to Germany. Remove it to continue, or ship to another address." For a blocked customer, keep it neutral and point to support; never accuse.

## 3. Check, then turn on

1. Save the draft (`chargezen.checkout_validations.create.v1` with a new `operation_id`), and set its place in the order with `chargezen.checkout_validations.reorder.v1` if several rules apply to the same checkout.
2. `chargezen.checkout_validations.preview.v1` shows the compiled active rules in the order they're checked. Walk the merchant through one checkout that's blocked and one that isn't.
3. On a clear yes, `chargezen.checkout_validations.activate.v1`. It publishes in the background, so read `chargezen.checkout_validations.provider_status.v1` and confirm the rule is in Shopify and validation is enabled. If it isn't yet, `chargezen.checkout_validations.publish.v1` and read again. Report what Shopify says.

To lift a rule: `chargezen.checkout_validations.deactivate.v1` (with no active rules left, validation turns off).
