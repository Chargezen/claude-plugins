# Chargezen Concierge for Claude

Work your Chargezen inbox and set up Concierge, your digital employees, from Claude: customer conversations on every channel, the agents that answer them, orders and shipping, stock, knowledge and loyalty.

## Requirements

- A Chargezen workspace with Concierge (new? you can create an account when you connect)
- A Chargezen teammate role that can use Concierge

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen-concierge@chargezen
```

Then run `/mcp`, choose `chargezen-concierge` and sign in. You'll sign in to Chargezen, pick your workspaces and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Settings → Connected AI assistants**. Full guide: https://chargezen.com/mcp

Want every Chargezen product in one connection, plus subscription, campaign, win-back and failed-payment skills? Install `chargezen@chargezen` instead.

## What Claude can do

Read and reply to inbox conversations on text, email, WhatsApp and chat, assign, tag and close them; set up the channels customers reach you on (storefront chat launcher, texting numbers, email mailboxes and domains, WhatsApp, phone numbers), business hours and handoff alerts; set up and tune the agents that answer your customers; build and edit workspace knowledge, saved replies and website crawls; search past conversations and workspace knowledge and media; look up orders, shipping, stock and sales reports; run loyalty points and rewards.

## What's included

| Part | What it does |
|---|---|
| `chargezen-concierge` MCP server | Connects to `https://mcp.chargezen.com/mcp/concierge`, only Concierge's tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/inbox-triage [count]` | Works through customers waiting on a reply, oldest first: checks their real order, drafts a reply for you to approve, then sends, assigns, tags or closes |
| `/order-status <order or customer>` | Answers "where is my order": live status, holds and tracking in plain words, and a reply for you to approve |
| `/customer-profile <customer>` | One customer on one page: orders, every conversation, what the team promised them, and their points |
| `/support-agent [channels]` | Sets up a customer-facing agent for chat, text, WhatsApp, email or phone: instructions, tools, channels, business hours and handoff alerts, saved as a draft and turned on when you say so |
| `/channel-setup [channels]` | Gets each way customers reach you ready and answered: storefront chat, texts, email, WhatsApp and phone, the agent that answers each, business hours and handoff alerts, and the steps that stay with you |
| `/chat-launcher [change]` | Designs the storefront chat launcher in your brand: teaser, greeting, shortcuts, FAQs, colors and position, saved as a draft and published on your OK |
| `/knowledge-setup [website]` | Loads what your agents know: reads your website, writes the FAQs and policies customers ask about from your real settings, publishes on your OK, and tidies stale entries |
| `/agent-tuning <agent>` | Reads what customers asked an agent and where it handed over, then improves its instructions, tools or reply style on your OK |
| `/agent-health` | Read-only check of every agent and channel: channels not ready or nobody answers, drafts never turned on, missing instructions or tools, no handoff alerts, customers waiting, with a ranked list of fixes |
| `/knowledge-gaps [days]` | Finds customer questions your knowledge doesn't answer, drafts the missing answers from real policies and past replies, saves them as drafts and publishes on your OK |
| `/customer-questions [days]` | Read-only: what customers wrote about this week, the main themes and complaints with example quotes, and what to fix |
| `/saved-reply-review` | Checks saved replies against your knowledge, shipping and loyalty settings, drafts corrected and missing replies, and saves, hides or deletes them on your OK |
| `/unshipped-orders [days]` | Read-only: orders that are late, on hold or rejected by the warehouse, by location, with delay notes to customers on your OK |
| `/stock-check [days]` | Read-only: best sellers, stock left across locations, days of cover and a suggested reorder quantity |
| `/shipping-setup [country]` | Read-only: where you ship, rates and free-shipping thresholds, checked against what customers ask and what your knowledge promises |
| `/weekly-brief [days]` | Read-only: unshipped orders, best sellers and stock, and customers waiting, then the three things that need you |
| `/loyalty-review` | Reviews how customers earn and redeem points, tiers, referrals and rewards emails against real activity, recommends up to three changes and makes the ones you approve |
| `/points <customer>` | Looks up a customer's points, tier and rewards, and adds, deducts, redeems or undoes points on your OK |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- "Which conversations are waiting on a reply, on every channel?"
- "Which orders from the last week haven't shipped?"
- `/support-agent web chat and text, order and shipping questions`
- `/knowledge-gaps 30`
- `/stock-check 30`
