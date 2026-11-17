# Chargezen for Claude

Run your online brand, DTC Shopify store, blog or med spa from Claude with Chargezen: Concierge, Subscriptions, CheckoutOS, SmartyTap and Spark! through one connection, plus skills that do whole jobs the safe way.

## Requirements

- A Chargezen workspace (new? Claude can start your signup when you connect)
- A Chargezen teammate role for the products you want Claude to use

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen@chargezen
```

Then run `/mcp`, choose `chargezen` and sign in. You'll sign in to Chargezen, pick your workspaces and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Settings → Connected AI assistants**. Full guide: https://chargezen.com/mcp

## What's included

| Part | What it does |
|---|---|
| `chargezen` MCP server | Connects to `https://mcp.chargezen.com/mcp`, every Chargezen product |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/weekly-brief [days]` | Read-only: shipping, best sellers and stock, subscriptions, customers waiting, campaigns and creator commissions, then the three things that need you |
| `/inbox-triage [count]` | Works through customers waiting on a reply, oldest first: checks their real order and subscription, drafts a reply for you to approve, then sends, assigns, tags or closes |
| `/campaign <brief>` | Builds an email, text or WhatsApp campaign as a draft from a short brief, fixes what Review flags, counts who gets it and what texts cost, sends you a test, and launches when you say so |
| `/win-back [offer]` | Sizes what cancellations cost you, then builds a flow that starts when a subscription is canceled: an email, then a text, with your offer, stopping for anyone who comes back |
| `/payment-recovery` | Builds a flow for failed renewal payments: a kind email and text with a secure link to update the card, plus an alert to your team when retries run out |
| `/subscribe-and-save <product>` | Sets up delivery options and a subscriber discount for a product, shows you exactly what shoppers will see, and creates it in Shopify on your OK |
| `/loyalty-review` | Reviews how customers earn and redeem points, tiers, referrals and rewards emails against real activity, recommends up to three changes and makes the ones you approve |
| `/creator-review [days]` | Read-only: your top creators, what you owe them, whether your balance covers it, refunds that took commission back, and applications waiting on you |
| `/subscription-help <customer> [request]` | Any request about one customer's subscription: skip, pause, resume, reschedule, frequency, quantity, swap, address, discount, card link or cancel. Shows what changes and what the customer is told, then acts on your OK |
| `/next-order <customer>` | Shows what their upcoming orders hold and changes the next one only: an item's quantity, a one-time add-on, a skipped order brought back, or shipping it now |
| `/new-subscription <customer> <product>` | Starts a subscription on the customer's saved card from a priced plan, with quantity, first billing date and an optional discount, after you confirm the summary |
| `/cancellations [days]` | Read-only: who canceled and what it cost, the customers worth a personal note, the reasons they gave, and what to do next |

Claude asks before anything reaches your customers or changes your store.

## Try

- `/weekly-brief`
- `/win-back 20% off your next order`
- `/campaign Holiday bundle to the VIP list, Friday 9am`
- "Which orders from the last week haven't shipped?"
- "Skip Jane Cooper's next subscription order."
