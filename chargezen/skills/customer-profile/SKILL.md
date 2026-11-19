---
name: customer-profile
description: Everything about one customer in Chargezen on one page — who they are, their recent orders and what hasn't shipped, every conversation with the store across text, email, WhatsApp and chat, what the team has promised them, and their loyalty points and tier — so the merchant can answer or help them without opening five screens. Use when they ask "who is this customer", want a customer's history before replying, or are handling a complaint or VIP.
argument-hint: "<email, phone, order number or name>"
---

# Customer profile

Customer: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person asks for something.

## 1. Find them

`chargezen.customers.search.v1` with what was given. If several match, or the stored address doesn't fit what the person knows, show the candidates and ask. Keep the exact `customer_ref`; its `id` is also the customer's ID for the inbox.

## 2. Gather

Run these together:

1. **Orders:** `chargezen.admin_shopify_orders.search.v1` with the `customer_ref`: their 15 newest saved orders. For the latest, and any that aren't fulfilled, `chargezen.admin_shopify_orders.get.v1` for items, totals, status and tracking.
2. **Open conversations:** `chargezen.inbox.list.v1` with `status: "all"` and `customer_uuid` set to the customer's ID: each conversation's channel, who's handling it, who it's assigned to and the latest message. `chargezen.inbox.get.v1` on any that are open or waiting.
3. **What was said before:** `chargezen.history.search.v1` with their order numbers, and with words from the complaint or request the person mentioned. Read around anything a teammate or agent promised (a refund, a replacement, a callback) with `chargezen.history.read.v1`.
4. **Loyalty:** `chargezen.admin_rewards.get_customer.v1`: points balance, tier, points about to expire and rewards issued.
5. **Marketing** (full Chargezen connection only): `chargezen.contacts.search.v1`, then `chargezen.contacts.get.v1` for their consent per channel, lists, custom properties and the timeline of what SmartyTap sent them.

Subscriptions aren't on this connection; if the person asks about them, say the full Chargezen connector can check.

## 3. Report

Lead with a two-line summary: who they are (first order date, number of orders, total spent where the orders show it, tier) and what's going on right now (an order not shipped, a conversation waiting, a promise not yet kept).

Then short sections: recent orders (up to five, with status), conversations (open first), promises found in past messages with their dates, and loyalty. Messages show what was said, not whether it was done: check orders before saying a promise was kept.

End with the most useful next step: reply to their waiting conversation (`/inbox-triage` or `/order-status`), or add goodwill points (`/points`).
