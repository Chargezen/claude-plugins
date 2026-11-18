---
name: saved-reply-review
description: A read-only review of the merchant's saved replies in the Chargezen inbox — checks each one against the store's knowledge, live shipping settings and loyalty program, and flags stale facts, broken or unfilled placeholders, near-duplicates and common customer questions with no saved reply — then drafts the corrected or new wording for the team to update. Use when they want their saved replies or macros cleaned up, checked for out-of-date policies, or filled in for common questions.
argument-hint: "[channel: sms, chat or email] [topic]"
---

# Saved reply review

Focus: $ARGUMENTS (every saved reply on every channel if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only.** This connection can read saved replies but can't create, edit or delete them; you'll hand the team the new wording to update in Chargezen.

## 1. Gather

1. `saved_replies.search` with no query (add `channel` if they named one): each reply's name, shortcut, category, content and placeholders (`variables`). It lists the shared replies and the connected teammate's own.
2. Facts to check them against:
   - `knowledge.search` (and `knowledge.read` for the full entry) on each policy a reply states: returns, refunds, shipping times, cancellations, subscriptions;
   - `shopify_shipping_zones.list` for any shipping price, country or free-shipping threshold;
   - `admin_rewards.get_program` for points, tiers and rewards.
3. What customers ask: `history.search` for the last 30 days on the usual topics (where is my order, returns, refunds, discount code, cancel, change address, sizing), keeping customer messages, to find common questions without a saved reply.

## 2. What to flag

- **Stale or wrong facts:** a return window, price, threshold, country or points rule that disagrees with knowledge or live settings. Quote both.
- **Placeholders:** a `{{…}}` placeholder in the content that isn't listed in `variables`, one spelled differently from the others, or a reply that can only be sent after editing by hand.
- **Near-duplicates:** two replies for the same question with different answers.
- **Channel fit:** a text reply far over 300 characters, or an email reply with no greeting or sign-off.
- **Tone:** cold, blaming or jargon-heavy wording.
- **Missing replies:** questions that came up often in conversations with no saved reply.

## 3. Report

Lead with the count reviewed and the three fixes that matter most. Then one line per reply that needs a change: its name or shortcut, what's wrong and the corrected wording in full. Then drafts for the missing replies, with placeholders written the way the existing replies write them.

The team updates saved replies in Chargezen. Offer to fix the knowledge behind a wrong answer with `/knowledge-gaps`, or to use the corrected wording right away while working the inbox with `/inbox-triage`.
