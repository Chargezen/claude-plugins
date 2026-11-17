---
name: chargezen
description: Use whenever the user wants to look something up or get something done in their Chargezen workspace — customers, orders, stock, subscriptions, the inbox, email and text campaigns, flows (automations), loyalty points and rewards, Spark! creators and payouts, checkout offers, or handing a job to Concierge. Covers how to reach Chargezen's tools, the safe order for changes, and the rules every other Chargezen skill follows.
---

# Chargezen

The `chargezen` MCP server acts for the teammate who connected it, in the workspaces they picked when they pressed Allow. Chargezen checks their permissions and plan on every call; don't check those yourself. If a call says access is missing, tell them which product or permission they need and stop.

## Reach the tools

Only a few tools are loaded directly. List everything this connection can do with `chargezen.tools.index.v1` (narrow it with `namespaces` or `query`), read the contracts you need with `chargezen.tools.describe.v1`, then run reads through `chargezen.tools.call_read.v1` and changes through `chargezen.tools.call_write.v1`. Each tool's description and schema are the contract: follow them rather than guessing field shapes.

- **Which workspace:** when the connection reaches more than one, `chargezen.connection.get_profile.v1` lists them. Ask which brand the person means unless it's clear, and pass that `workspace` on every call.
- **Pick real records.** Customers come from `customers.search`, products from `products.search`, collections from `products.search_collections`, lists and segments from the authoring-options tools. Pass every reference through exactly as it came back.
- **Dates:** reports take explicit timestamps with a UTC offset. Say which period you used.

## The safe order for any change

1. **Read first.** Look at what exists before you add to it, so you don't create a duplicate.
2. **Draft.** Campaigns, flows, offers and rules are created as drafts that customers don't see. Use the `operation_id` a tool asks for: a fresh UUID, kept with the same inputs on any retry.
3. **Show it.** Use the family's preview tool where there is one (`preview`, `preview_audience`, `review`), and tell the person in plain words what customers will see, who gets it and what it costs.
4. **Go live only when they say so.** Launching, activating, publishing, sending, cancelling and deleting change what customers see or get. Ask in one plain sentence and wait for a yes. If a call returns `CONFIRMATION_REQUIRED`, repeat the identical call with its `confirmation_token` only after they agree.
5. **Report what happened**, including anything the result says failed.

## Hard rules

- Never send a customer anything (email, text, WhatsApp, inbox reply) without the person's OK on the exact words.
- Never ask for, read out or type passwords, sign-in codes or card details.
- Never get around a confirmation, a review hold, a plan limit or a rate limit.
- Never invent numbers. Every figure you report comes from a tool result; say when a result is incomplete (`complete: false`, `has_more: true`, `not_visible_categories`, `unavailable`).
- Direct subscription tools cover subscriptions that run on Chargezen. Subscriptions still on Recharge or Stripe aren't included: say so when it matters.

## Talking to the person

Write like a helpful teammate: short sentences, plain words, no tool names, IDs or JSON unless they ask. Lead with the answer, then the detail. End with one clear next step you can do for them.

## Other Chargezen skills

`/weekly-brief`, `/inbox-triage`, `/campaign`, `/win-back`, `/payment-recovery`, `/subscribe-and-save` and `/loyalty-review` each do one whole job and follow this skill.
