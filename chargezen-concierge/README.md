# Chargezen Concierge for Claude

Work your Chargezen inbox and hand jobs to Concierge, your digital employees, from Claude: customer conversations on every channel, orders and shipping, reports, knowledge and loyalty.

## Requirements

- A Chargezen workspace with Concierge (new? you can create an account when you connect)
- A Chargezen teammate role that can use Concierge

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen-concierge@chargezen
```

Then run `/mcp`, choose `chargezen-concierge` and sign in. You'll sign in to Chargezen, pick your workspaces and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Settings → Connected AI assistants**. Full guide: https://chargezen.com/mcp

Want every Chargezen product in one connection, plus the weekly brief, win-back and failed-payment skills? Install `chargezen@chargezen` instead.

## What Claude can do

Read and reply to inbox conversations on text, email, WhatsApp and chat, assign, tag and close them; hand Concierge a job and get its reply; look up orders, shipping, stock and sales reports; search workspace knowledge and media; run loyalty points and rewards.

## What's included

| Part | What it does |
|---|---|
| `chargezen-concierge` MCP server | Connects to `https://mcp.chargezen.com/mcp/concierge`, only Concierge's tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/inbox-triage [count]` | Works through customers waiting on a reply, oldest first: checks their real order, drafts a reply for you to approve, then sends, assigns, tags or closes |
| `/loyalty-review` | Reviews how customers earn and redeem points, tiers, referrals and rewards emails against real activity, recommends up to three changes and makes the ones you approve |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- "Which conversations are waiting on a reply, on every channel?"
- "Ask Concierge to sum up last week's customer conversations."
- "Which orders from the last week haven't shipped?"
