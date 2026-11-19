---
name: knowledge-setup
description: Load what the merchant's Chargezen agents know — read the store's website into knowledge, then write the FAQs and policies customers ask about most (shipping, returns, refunds, subscriptions, contact) from the store's real settings and the merchant's answers, saved as drafts and published on the merchant's OK, and tidy entries that are out of date or duplicated. Use for a new workspace, before turning on a support agent, after a website or policy change, or when they ask what their agents know.
argument-hint: "[website address, or a topic]"
---

# Knowledge setup

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person approves a step. To fill gaps found in real customer conversations, use `/knowledge-gaps` instead.

## 1. What's there

1. `chargezen.knowledge.list_entries.v1`: every entry in every status, newest change first, with its kind (FAQ, Q&A, article, crawled page, store policy, document), its status and where it came from. Follow `next_page` until you have them all or have enough to judge.
2. `chargezen.knowledge.list_website_crawls.v1`: website crawls, whether each finished and how many pages it saved.
3. `chargezen.workspace_brand.get.v1` for the store's website address.

Tell them in two lines what agents know now (published entries by kind) and what's obviously missing.

## 2. Read the website

If the website was never crawled, or the last crawl failed:

1. Agree the address (the store's home page, or its sitemap) and any sections to skip, such as `/blogs/*`. Say that each page saved is published at once, agents start using it, and it re-imports daily when the page changes.
2. On their OK, `chargezen.knowledge.start_website_crawl.v1` with a fresh `operation_id` (kept on a retry), `crawl_mode: "sitemap"` for a sitemap address and `"crawl"` otherwise.
3. It runs in the background: check it with `chargezen.knowledge.list_website_crawls.v1`. When it finishes, say how many pages were saved and which failed. Pages behind a sign-in aren't read.

## 3. Write the answers customers need

Check each topic with `chargezen.knowledge.search.v1` (two phrasings): shipping times and costs, countries shipped to, order tracking, returns and exchanges, refunds, damaged or wrong items, cancelling or changing an order, discount codes, subscriptions (skip, pause, cancel), loyalty points, payment methods, and how to reach a person. Add topics the merchant names.

For each one that isn't answered, draft a short answer from real facts only:

- shipping zones and rates from `chargezen.shopify_shipping_zones.list.v1`;
- the loyalty program from `chargezen.admin_rewards.get_program.v1`;
- pages the crawl saved (`chargezen.knowledge.read.v1`);
- the merchant's own words.

Anything no tool gives (a return window, who pays return postage) becomes a clear blank, such as "[number] days", for the merchant to fill in. Never invent a policy.

Show the drafts together and choose the kind of each with them: a question shoppers browse becomes an FAQ (shown in the storefront chat's FAQ section once published), one asked many ways a Q&A with its other phrasings, and a full policy an article.

## 4. Save as drafts, publish on their OK

1. Save each approved draft with `chargezen.knowledge.save_faq.v1`, `chargezen.knowledge.save_qna.v1` or `chargezen.knowledge.save_entry.v1`, a fresh `operation_id` each, and always `status: "draft"`, since new entries are published by default.
2. Ask: "Publish these? Agents use them in their answers right away, and FAQs appear in the storefront chat." On a yes, save each again with its `knowledge_entry_id` and `status: "published"`.

## 5. Tidy what's there

From step 1, point out entries that disagree with live settings or with each other, near-duplicates, and drafts never published. For each, propose the fix: edit it (only the fields that change; editing a published entry changes agents' answers at once), archive it (`status: "archived"`, kept but not used), or delete it. `chargezen.knowledge.delete_entry.v1` can't be undone: only on an explicit OK naming that entry.

End with what agents know now, what's still a draft, and the next step: `/support-agent` to put an agent to work, or `/knowledge-gaps` after a few weeks of real conversations.
