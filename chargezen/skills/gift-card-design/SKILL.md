---
name: gift-card-design
description: Design how the store's gift cards look and what the purchase form asks for, with Chargezen CheckoutOS — template, colors and fonts, labels for the amount, recipient, delivery date and gift note, extra text and buttons, and images already in the workspace — starting from a template or a copy of an existing design. Use when someone wants to create or restyle their gift card or its form. Designs don't issue gift cards or charge anyone.
argument-hint: "[style or occasion]"
---

# Gift card design

The request: $ARGUMENTS

Follow the `chargezen` and `checkoutos` skills for how to reach the tools.

These tools design the gift card and its form. They don't issue gift cards, set values or charge anyone.

1. **Start point:** `gift_card_designs.list` for the store's designs. For a seasonal version of one, `gift_card_designs.copy` it. For a new one, `gift_card_designs.discover` and pick a template, which comes with complete editable defaults.
2. **Design it** with the merchant:
   - colors for the background, borders, title, text, labels, toggles and button, matching their brand;
   - the font and corner radius;
   - labels in their voice: "Amount", "Who's it for?", "Their email", "When should it arrive?", "Add a note";
   - extra blocks in order: a headline, a paragraph, a checkbox, a spacer or a button;
   - images: reuse the gift card or background image from a saved design (the full `chargezen` connection can also use the workspace's media library). New images are uploaded in Chargezen's design editor; say so if they need one.
3. Save it (`gift_card_designs.save` with a new `operation_id` for a new design, or its `design_id` to edit). Blocks are a complete replacement, so send every block they want to keep.
4. Describe the finished card and form in a few lines. On their OK, mark it live with `gift_card_designs.status`. That marks it ready in Chargezen; where it appears depends on the gift card block placed on their store.
