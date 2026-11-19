---
name: checkout-branding
description: Style the Shopify checkout to match the brand with Chargezen CheckoutOS — colors, buttons, fonts and sizes, corners, form fields, header and logo, and the order summary — saved first, tried on a draft checkout profile, and applied to the live checkout only on the merchant's OK. Needs Shopify Plus or a development store. Use when someone says checkout doesn't look like their store, or wants to change checkout colors, fonts or buttons.
argument-hint: "[what to change]"
---

# Checkout branding

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

## 1. Profiles and what's set

1. `chargezen.checkout_branding.discover.v1` (follow `next_cursor` to the end). Branding needs Shopify Plus or a development store; if the result says otherwise, stop and explain.
2. Profiles are **published** (the live checkout) or **draft** (previewed in Shopify's checkout editor). `chargezen.checkout_branding.get.v1` the one they mean and describe what's set now in plain words.

## 2. Decide the look

Ask for their brand colors and fonts, or read them from their store and confirm. Then agree, in plain words:

- **Colors:** brand and accent, and the two color schemes (main area and order summary): background, text, buttons and their hover, form controls.
- **Buttons:** filled or outlined, corner shape, padding, text case and weight.
- **Type:** primary and secondary fonts (Shopify fonts or ones already uploaded), base size and heading sizes.
- **Corners and fields:** small, base, large or none; field borders and label position.
- **Header:** logo alignment and width.

Keep text readable: dark text on light backgrounds (or the reverse) and buttons that stand out from the page. Flag any color pair that's hard to read.

## 3. Try it, then go live

1. `chargezen.checkout_branding.save.v1` the complete decision on a **draft** profile if they have one, then `chargezen.checkout_branding.apply.v1` it. Applying to a draft changes only its editor preview: ask them to open it in Shopify's checkout editor and look.
2. When they're happy, save the same decision on the published profile and, on a clear yes, `chargezen.checkout_branding.apply.v1` it. That changes the live checkout immediately.
3. `chargezen.checkout_branding.get.v1` to confirm what Shopify now has, and report any error. If Shopify didn't answer, read before retrying.
