# Chargezen Spark! for Claude

Run reports on your Spark! creator and affiliate program from Claude with Chargezen: partner leaderboards and monthly reports, payout prep and funding checks, commission plans, sale-credit checks, finance reconciliation and program health. Read-only.

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

Read partners and applications, credited orders and commissions, commission profiles, payouts, deposits, the finance ledger and balance, program settings, and a guide to every Spark! admin page. Spark! tools only read; payouts, approvals and rate changes happen in the Spark! admin, and Claude tells you exactly where.

## What's included

| Part | What it does |
|---|---|
| `chargezen-spark` MCP server | Connects to `https://mcp.chargezen.com/mcp/spark`, only Spark!'s tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/creator-review [days]` | Read-only: your top creators, what you owe them, whether your balance covers it, refunds that took commission back, and applications waiting on you |
| `/partner-report [month or days]` | A shareable monthly or period report: every partner's credited orders, sales and commission ranked and compared with the period before, new partners, refunds and payouts made |
| `/payout-prep [partner]` | What each partner is owed, payouts waiting or failed, who's under the minimum, refund deductions, and whether your balance covers it, with where to mark payouts paid |
| `/commission-plans [profile or partner]` | Every commission profile's rate, customer discount, limits and schedule, who's on it and what it earned, with the gaps worth fixing |
| `/sale-credit <order, partner or date>` | Did this sale get credited? Which partner, by link or code, the commission, its status, refunds and payout, or the settings that explain a missing credit |
| `/partner-profile <partner>` | One partner in depth: links and rates, clicks, orders and sales by month, refunds and clawbacks, payouts, with suggestions |
| `/partner-finance [month or days]` | Month-end reconciliation: deposits, payouts, fees and adjustments against the recorded balance, flagging anything that doesn't add up |
| `/partner-health [days]` | Program check: applications waiting, partners with no sales or gone quiet, unusual refund or dispute patterns, set-up gaps and settings worth a second look |
| `/spark-help <question>` | How to do something in the Spark! admin, with the exact page and steps, using your real settings |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- "Which creators drove the most sales last month?"
- "Does our balance cover pending commissions?"
- `/creator-review 30`
- `/partner-report October`
- "Did order 1042 get credited to Maya?"
- `/payout-prep`
- "How do I invite a creator on the 20% plan?"
