---
name: upsell-experiment
description: Set up an A/B test on one of the merchant's checkout or post-purchase upsells in Chargezen CheckoutOS.
argument-hint: "<offer name or ID> [what to change]"
---

# Upsell experiment

The merchant wants to test: $ARGUMENTS

Follow the `checkoutos` skill for how to reach the tools.

1. Find the offer (checkout upsells or post-purchase offers) and read its configuration and its recent performance from `upsell_analytics.get`.
2. Agree on **one** change to test. If the merchant didn't name one, propose the change most likely to lift conversion and say why.
3. Make the challenger: duplicate the offer (`checkout_extensions.duplicate` for checkout upsells, `post_purchase_upsells.copy` for post-purchase) and apply the change to the copy. Leave the original untouched.
4. Show the merchant both versions side by side and ask what share of shoppers should see the challenger. Don't pick it for them.
5. Only after they confirm, start it with `upsell_experiments.create`. Tell them it starts immediately and that the challenger is shown even while it's a draft.
6. Suggest when to check the result, and offer to read it and end the test then.
