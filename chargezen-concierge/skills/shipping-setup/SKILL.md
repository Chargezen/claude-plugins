---
name: shipping-setup
description: A read-only review of the merchant's live Shopify shipping setup through Chargezen — where the store ships, zones and rates by shipping profile, free-shipping thresholds, carrier-calculated rates and fulfillment locations — checked against what customers ask and what knowledge promises, ending with the gaps worth fixing. Also answers one question such as "do we ship to Canada and what does it cost". Use when they ask about shipping countries, rates or free shipping, or want their shipping setup checked.
argument-hint: "[country or region, or review]"
---

# Shipping setup

Request: $ARGUMENTS (a full review if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only.** Shipping is changed in Shopify; this connection can't change it.

## One destination

For "do we ship to X": `shopify_shipping_zones.list` with `destination` (`country` as a two-letter code, plus `province` when they named one). An empty list means the store doesn't ship there. Otherwise give each rate: its name as shoppers see it, its price, any order price or weight limits (such as free over an amount), and note that a carrier- or app-calculated rate has no fixed price because it's worked out at checkout. If a zone belongs to a product-specific profile, say which products it applies to. Then stop, or offer the full review.

## Full review

1. **Zones and rates:** `shopify_shipping_zones.list` with no destination: every zone, its profile (general or product-specific), countries and rates.
2. **Locations:** `shopify_locations.list` (all pages): where orders ship from.
3. **What customers expect:** `knowledge.search` for shipping times, costs, free shipping and international shipping, and `saved_replies.search` for "shipping". `history.search` for the last 30 days with words like "ship to", "shipping cost", "international", "customs", from customers.

## What to flag

- **Promises that don't match:** knowledge or a saved reply says free shipping over an amount, a country, or a price that the live rates don't have.
- **Countries customers ask about** that no zone covers.
- **Zones without rates**: a zone with no active rates offers no shipping there.
- **Gaps between profiles:** a product-specific profile that covers fewer countries than the general one, so some products can't ship where others can.
- **Rest of world:** whether it exists and what it costs.
- **No free-shipping threshold** where they think there is one, or thresholds that differ between zones without reason.

These tools don't cover local delivery, pickup, taxes or duties, or quote an exact cart price; say so if it comes up.

## Report

Lead with up to three fixes, each one line: what's wrong, who it affects and where to fix it (Shopify's shipping settings for rates and zones; **Concierge → Knowledge** or the saved reply for wrong promises). Then one line per zone: countries, rates and thresholds. Offer to draft corrected knowledge answers (`/knowledge-gaps`) or saved replies (`/saved-reply-review`).
