---
name: knowledge-gaps
description: Find the customer questions the merchant's Chargezen knowledge doesn't answer — search recent conversations for what customers asked, check each question against the published knowledge, draft the missing answers from the store's real policies, shipping settings and past replies, then save them as drafts and publish the ones the merchant approves. Use when the agent gives vague answers, hands over too often, before turning on a support agent, or when they ask what their FAQ is missing.
argument-hint: "[days, default 30, or a topic]"
---

# Knowledge gaps

Period or topic: $ARGUMENTS (the last 30 days if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person approves the answers to save.

## 1. Collect the questions

1. **Topics to try:** start with what customers of a store usually ask: shipping times and costs, international shipping, order tracking, returns and exchanges, refunds, damaged or wrong items, cancelling an order, changing an address, discount codes, sizing, ingredients or materials, stock and restocks, subscriptions (skip, pause, cancel), loyalty points, payment methods, and contacting a person. Add anything the person named.
2. **Find them:** `history.search` for each topic with `since` set to the period, using the words customers would write (for example "where is my order", "tracking number", "hasn't arrived"). Keep matches with `sender: "customer"`; read around one with `history.read` to see the whole question and how it was answered.
3. **Handovers:** `inbox.list` with `status: "handoff_queue"` and `inbox.get` on a few: a question the agent couldn't answer is often a gap.
4. **Gaps Chargezen already noticed:** `knowledge.list_content_gaps` with `status: "open"` and `days_back` set to the period: similar questions grouped, how often each came up, how the agent responded, and any suggested draft.

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

## 5. Save the answers they approve

1. Ask which drafts to save, and have them fill every blank first.
2. Save each as a **draft**, so no customer sees it yet: a common question shoppers could browse becomes an FAQ (`knowledge.save_faq`, shown in the storefront chat's FAQ section once published), one with several phrasings a Q&A (`knowledge.save_qna`, with the other ways customers ask it), and a longer policy an article (`knowledge.save_entry`). Always pass `status: "draft"`, since new entries are published by default, and a fresh `operation_id` for each, kept on a retry.
3. For an out-of-date entry, show the old and new wording side by side. Editing a published entry changes agents' answers at once, so save it only on their OK.
4. Read the drafts back in one short list, then ask: "Publish these? Agents start using them in their answers right away, and FAQs appear in the storefront chat." On a yes, save each again with its `knowledge_entry_id` and `status: "published"`.

Say what was saved, what's live and what's still a draft. Offer to recheck with `/knowledge-gaps` after a few weeks, or to update an agent's instructions with `/agent-tuning`.
