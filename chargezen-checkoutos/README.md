# Chargezen CheckoutOS for Claude

Build and optimize your Shopify checkout from Claude: checkout and post-purchase upsells, A/B experiments, discount functions, cart transforms, checkout validations, trust badges, thank-you texts, address verification, gift-card designs and checkout branding.

## Requirements

- A Chargezen workspace with CheckoutOS, connected to your Shopify store
- A Chargezen teammate role that can manage CheckoutOS

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen-checkoutos@chargezen
```

Then run `/mcp`, choose `chargezen-checkoutos` and sign in. You'll sign in to Chargezen, pick your workspace and approve what Claude may do. You can revoke access at any time from Chargezen.

## What's included

| Part | What it does |
|---|---|
| `chargezen-checkoutos` MCP server | Connects to `https://mcp.chargezen.com/mcp/checkoutos` |
| `checkoutos` skill | Teaches Claude the safe order (placement → read → draft → preview → go live) and how to optimize from data |
| `/checkout-audit [days]` | Read-only audit of your checkout with a ranked list of fixes |
| `/upsell-experiment <offer>` | Sets up an A/B test on one offer |

Claude asks before changing anything that shoppers will see.

## Try

- "Add a 10% off coffee upsell at checkout for carts with anything from Breakfast"
- "Which of my upsells is underperforming this month?"
- `/checkout-audit 60`
