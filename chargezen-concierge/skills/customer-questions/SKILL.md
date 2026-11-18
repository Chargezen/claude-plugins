---
name: customer-questions
description: A read-only digest of what the merchant's customers have been writing about across texts, email, WhatsApp and web chat in Chargezen — the main themes, complaints, product questions and requests, each with real example quotes and the orders or products behind them — ending with what to fix or answer better. Use when they ask what customers are asking about, what people are complaining about this week, or for voice-of-customer insight.
argument-hint: "[days, default 7, or a topic or product]"
---

# Customer questions

Period or focus: $ARGUMENTS (the last 7 days if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only**; change nothing. Work out the period as timestamps with a UTC offset and say which you used.

## 1. See what came in

1. **Recent conversations:** `inbox.list` with `status: "all"`, a page of 50, most recent activity first. Keep paging while `last_message_at` is inside the period, up to 200 conversations. Each row's latest message preview, channel and handling (`ai`, `handoff_pending`, `human`) gives a first sketch.
2. **Group them** into themes from the previews: where is my order, returns and refunds, damaged or wrong item, product questions (size, ingredients, compatibility), stock and restocks, discount codes and pricing, subscriptions, loyalty points, account and login, shipping costs and countries, praise. Add themes the previews suggest.
3. **Read deeper:** for each of the biggest themes, `inbox.get` on two or three conversations to see what customers actually asked and how it ended.

## 2. Dig into each theme

- `history.search` with the customers' own words for the theme (for example "arrived broken", "smaller than expected", "still waiting") and `since` set to the period, to find more examples across channels. Keep matches with `sender: "customer"`; read around one with `history.read` when needed.
- For a product that keeps coming up, `products.search` to name it exactly, and `shopify_reports.sales_by_sku` for the period to set the complaints against how many sold.
- For shipping themes, `shopify_reports.fulfillment_status` for the period, to see whether there's a real backlog behind the questions.

Search results are the best matches, not every one, and the inbox sample is what you paged through. Report "N of the M conversations read", never a total or a percentage of all customers.

## 3. Report

Lead with the three themes that matter most, ranked by how often they came up and how upset customers were. For each: one line on what customers are saying, one or two short quotes (no names, emails or phone numbers), how many of the conversations read mention it, and the likely cause where a tool showed one (a delayed batch, a product description that's unclear).

Then a short list of the other themes, one line each, and anything customers praised.

End with one or two next steps you can do, such as drafting knowledge answers for the questions that keep coming back (`/knowledge-gaps`), teaching the support agent to handle a theme (`/agent-tuning`), or answering the customers still waiting (`/inbox-triage`).
