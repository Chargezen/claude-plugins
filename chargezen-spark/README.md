# Chargezen Spark! for Claude

Review your Spark! creator and affiliate program from Claude with Chargezen: partners, credited orders, commissions, payouts and your program balance. Read-only.

## Requirements

- A Chargezen workspace with Spark! (new? you can create an account when you connect)
- A Chargezen teammate role that can use Spark!

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen-spark@chargezen
```

Then run `/mcp`, choose `chargezen-spark` and sign in. You'll sign in to Chargezen, pick your workspaces and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Settings → Connected AI assistants**. Full guide: https://chargezen.com/mcp

Want every Chargezen product in one connection, plus the weekly brief, win-back and failed-payment skills? Install `chargezen@chargezen` instead.

## What Claude can do

Read partners and applications, credited orders and commissions, commission profiles, payouts, deposits and the program's finance balance. Spark! tools only read; payouts, approvals and rate changes happen in Chargezen.

## What's included

| Part | What it does |
|---|---|
| `chargezen-spark` MCP server | Connects to `https://mcp.chargezen.com/mcp/spark`, only Spark!'s tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/creator-review [days]` | Read-only: your top creators, what you owe them, whether your balance covers it, refunds that took commission back, and applications waiting on you |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- "Which creators drove the most sales last month?"
- "Does our balance cover pending commissions?"
- `/creator-review 30`
