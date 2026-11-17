---
name: invoice
description: Find an order's invoice in Chargezen, get its PDF, or email it to the customer or another address the merchant approves — creating the invoice if the order doesn't have one yet. Use when a customer asks for an invoice or receipt, or the merchant needs a copy for accounting.
argument-hint: "<customer, order number or invoice number> [email to send it to]"
---

# Invoice

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

1. **Find it:** `admin_invoices.list` with the invoice number, order name, customer name or email. If it's not there, the order may not have an invoice yet: `admin_shopify_orders.search` to find the order (confirm it by date and total).
2. **Show it:** `admin_invoices.get` for an existing invoice: number, order, date, total, and whether and when it was emailed.
3. **PDF:** `admin_invoices.pdf` returns the saved document. Tell the merchant where it is, or attach it if this assistant can.
4. **Email it:** confirm the recipient address with the merchant (the customer's own email by default; never guess another). On a yes, `admin_invoices.send` with the order's exact `order_gid`, that `recipient_email` and a new `operation_id`. It creates the invoice if needed and emails it. A new `operation_id` sends it again, so reuse the same one only to retry the same send.
5. Report what the send receipt says, then check `admin_invoices.get` for the latest delivery status. Don't claim it was delivered until it says so.

An invoice's amounts can't be changed once created; for a correction, the order itself has to change in Shopify.
