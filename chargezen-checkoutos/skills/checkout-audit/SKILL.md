---
name: checkout-audit
description: Audit the merchant's Shopify checkout in Chargezen CheckoutOS and recommend the highest-impact fixes. Read-only.
argument-hint: "[days, default 30]"
---

# Checkout audit

Audit window: the last $ARGUMENTS days (use 30 if no number was given).

Use only reads (`chargezen.tools.call_read.v1`); change nothing. Follow the `checkoutos` skill for how to reach the tools.

1. **Placement:** `checkout_extensions.discover` — which Chargezen blocks are placed, editor-only, not seen recently or never seen.
2. **What's live:** checkout upsells (with priority order), post-purchase offers and funnels, running experiments, discount functions, cart transforms, validations, trust badges, texts and branding.
3. **Performance:** `upsell_analytics.get` and `post_purchase_upsells.funnels` for the window.
4. **Report** as a short ranked list. For each finding give what you saw, why it matters to revenue or conversion, and the specific fix. Typical findings:
   - an active offer whose block isn't placed
   - several active campaigns where a lower-priority one never gets served
   - offers with many views and low conversion
   - offers discounting products shoppers already buy at full price
   - no post-purchase offer at all
   - experiments running past a clear result

End by offering to make the top fix as a draft.
