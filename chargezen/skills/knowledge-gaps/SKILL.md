---
name: knowledge-gaps
description: Find the customer questions the merchant's Chargezen knowledge doesn't answer — search recent conversations for what customers asked, check each question against the published knowledge, and draft the missing answers from the store's real policies, shipping settings and past replies, ready to add in Concierge's Knowledge page. Use when the agent gives vague answers, hands over too often, before turning on a support agent, or when they ask what their FAQ is missing.
argument-hint: "[days, default 30, or a topic]"
---

# Knowledge gaps

Period or topic: $ARGUMENTS (the last 30 days if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only.** This connection can read knowledge but can't add or edit it; you'll hand the person drafts to add themselves.

## 1. Collect the questions

1. **Topics to try:** start with what customers of a store usually ask: shipping times and costs, international shipping, order tracking, returns and exchanges, refunds, damaged or wrong items, cancelling an order, changing an address, discount codes, sizing, ingredients or materials, stock and restocks, subscriptions (skip, pause, cancel), loyalty points, payment methods, and contacting a person. Add anything the person named.
2. **Find them:** `history.search` for each topic with `since` set to the period, using the words customers would write (for example "where is my order", "tracking number", "hasn't arrived"). Keep matches with `sender: "customer"`; read around one with `history.read` to see the whole question and how it was answered.
3. **Handovers:** `inbox.list` with `status: "handoff_queue"` and `inbox.get` on a few: a question the agent couldn't answer is often a gap.

Search returns the best matches, not every one; record "seen in N conversations read", never a total.

## 2. Check each question against knowledge

For each distinct question, `knowledge.search` with two or three phrasings, then `knowledge.read` on the best entry when the excerpt doesn't settle it. Sort each question into:

- **Answered:** an entry says it clearly.
- **Partly answered or out of date:** an entry touches it but leaves out what customers asked, or disagrees with what the team told customers or with live settings.
- **Not answered:** nothing in knowledge.

## 3. Draft the missing answers

For each gap, ranked by how often it came up, draft a short answer (two to five sentences) built only from real facts:

- what the team already told customers, from the conversations you read;
- shipping zones and rates from `shopify_shipping_zones.list` for shipping questions;
- the loyalty program from `admin_rewards.get_program` for points questions;
- existing team answers from `saved_replies.search`.

When no tool gives the fact (a return window, a refund rule), write the draft with a clear blank, such as "[number] days", and ask the person to fill it in. Never invent a policy.

## 4. Report

Lead with the count of questions checked and how many are gaps. Then the gaps, most common first: the question in a customer's words, how often you saw it, and the draft answer. Then answers that look out of date, with what disagrees.

To add them: in Chargezen open **Concierge → Knowledge** and add each as an FAQ or Q&A entry (or upload a document or import a page from the store's website). Agents and Concierge use an entry once it is published. Offer to recheck with `/knowledge-gaps` afterwards, or to update an agent's instructions with `/agent-tuning`.
