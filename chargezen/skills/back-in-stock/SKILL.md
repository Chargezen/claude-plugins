---
name: back-in-stock
description: Build a SmartyTap back-in-stock flow in Chargezen that emails and texts each shopper who asked to hear about a product the moment it's available again — saved as a draft, previewed, and turned on only on the merchant's OK. Use when they want back-in-stock or restock alerts.
argument-hint: "[products, if only some]"
---

# Back in stock

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Check what's there

1. `chargezen.workflows.list.v1`: if a flow already uses Back in stock (`catalog.back_in_stock`), read it with `chargezen.workflows.get.v1` and offer to improve it instead. Two would alert the same shopper twice.
2. `chargezen.workflows.authoring_options.v1` for senders, the Back in stock starter design and whether texts can send.

The flow starts for each shopper who asked, on the store's back-in-stock sign-up, to hear about a variant, once that variant has stock again. Without the sign-up on the store, nobody enters; if the merchant isn't sure it's there, tell them to check it in SmartyTap.

## 2. Agree the plan

1. **Trigger:** Back in stock. To cover only some products, filter on `product_title`, `product_id` or `variant_id` (`chargezen.products.search.v1` finds the real ones). Optionally `inventory_quantity` at least a number, so a single returned unit doesn't alert a long waiting list.
2. **Right away:** an email from the Back in stock starter ("{{ product.title }} is back"), the product image, one button to `{{ product.url }}`.
3. **And a text** when texts are ready: "Good news: {{ product.title }} is back in stock at {{ organization.name }}. {{ product.url }}"
4. **Purpose:** `transactional` for both. The shopper asked for this alert, which is how Chargezen's own template sets it. Keep the words to the alert: no unrelated promotion.
5. **Re-entry:** `allow`, so someone who asks about another product later is told again.

## 3. Build, check, turn on

1. **Start from the library:** `chargezen.workflows.list_templates.v1`, then `chargezen.workflows.create_from_template.v1` with `template_key` `back_in_stock` and a new `operation_id`: the trigger, an email from the Back in stock starter and a transactional text, as a Draft that sends nothing. Keep that `operation_id` for any retry: a new one makes a second flow.
2. `chargezen.workflows.get.v1` on the Draft; add the product or stock filters agreed above with `chargezen.workflows.update.v2` from the revision you read, and change the text with `chargezen.workflows.update_messages.v2` if the wording differs.
3. Write the email with `chargezen.email_documents.apply_ops.v1` at its address in `email_documents`; check the text with `chargezen.workflows.preview_sms.v1` (trigger `catalog.back_in_stock`), the email with `chargezen.workflows.preview_email.v2` and the flow with `chargezen.workflows.check.v1`.
4. Show the person both messages and which products they cover, and offer a test of each to them with `chargezen.workflows.send_test.v1` (new `operation_id`; to them only, a test text costs credits like any text).
5. Only when they say so: `chargezen.workflows.activate.v1`.
