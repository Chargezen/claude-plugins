# Chargezen for Claude

Run your Shopify brand from Claude with Chargezen: Concierge, Subscriptions, CheckoutOS, SmartyTap and Spark! through one connection, plus skills that do whole jobs the safe way.

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

Claude asks before anything reaches your customers or changes your store.

## Try

- `/weekly-brief`
- "Which orders from the last week haven't shipped?"
- "Skip Jane Cooper's next subscription order."
