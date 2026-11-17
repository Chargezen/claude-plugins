# Chargezen Subscriptions for Claude

Run Shopify subscriptions from Claude with Chargezen: find and change customers' subscriptions, set up subscribe-and-save plans, read new and canceled subscriptions, invoices and loyalty.

## Requirements

- A Chargezen workspace with Subscriptions (new? you can create an account when you connect)
- A Chargezen teammate role that can use Subscriptions

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen-subscriptions@chargezen
```

Then run `/mcp`, choose `chargezen-subscriptions` and sign in. You'll sign in to Chargezen, pick your workspaces and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Settings → Connected AI assistants**. Full guide: https://chargezen.com/mcp

Want every Chargezen product in one connection, plus the weekly brief, win-back and failed-payment skills? Install `chargezen@chargezen` instead.

## What Claude can do

Find a customer's subscriptions and pause, skip, swap, reschedule, change quantity, frequency or address, apply a discount, send a card-update link or cancel; create subscriptions and subscribe-and-save plans; read the new and canceled subscriptions report and invoices; run loyalty points and rewards.

## What's included

| Part | What it does |
|---|---|
| `chargezen-subscriptions` MCP server | Connects to `https://mcp.chargezen.com/mcp/subscriptions`, only Subscriptions's tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/subscribe-and-save <product>` | Sets up delivery options and a subscriber discount for a product, shows you exactly what shoppers will see, and creates it in Shopify on your OK |
| `/loyalty-review` | Reviews how customers earn and redeem points, tiers, referrals and rewards emails against real activity, recommends up to three changes and makes the ones you approve |
| `/subscription-help <customer> [request]` | Any request about one customer's subscription: skip, pause, resume, reschedule, frequency, quantity, swap, address, discount, card link or cancel. Shows what changes and what the customer is told, then acts on your OK |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- "Skip Jane Cooper's next coffee delivery."
- "Who canceled last month, and how much monthly revenue went with them?"
- `/subscribe-and-save Cold brew, 15% off`
