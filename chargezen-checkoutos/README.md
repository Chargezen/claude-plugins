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

Then run `/mcp`, choose `chargezen-checkoutos` and sign in. You'll sign in to Chargezen, pick your workspace and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Connected accounts** in your account menu and click **Disconnect**. Full guide: https://chargezen.com/docs/checkoutos/api/mcp

## What's included

| Part | What it does |
|---|---|
| `chargezen-checkoutos` MCP server | Connects to `https://mcp.chargezen.com/mcp/checkoutos` |
| `chargezen` and `checkoutos` skills | Teaches Claude the safe order (placement → read → draft → preview → go live) and how to optimize from data |
| `/checkout-upsell <offer>` | Adds a product upsell inside checkout: products, discount, who sees it and the layout, live on your OK |
| `/post-purchase <offer>` | Builds a one-click offer or a funnel of up to three steps after payment, checks who it shows to against a real order, then publishes or schedules it |
| `/volume-discount <deal>` | Quantity breaks, automatic product, order or shipping discounts, subscriber-only deals and campaign-link discounts, with the price math shown first |
| `/bundle <bundle>` | Bundles and kits: a bundle product that ships as its parts, or parts merged into one bundle line at a bundle price |
| `/checkout-rules <what to stop>` | Blocks checkouts that would cause trouble: products or subscriptions shipping where they can't, overweight orders, label-breaking addresses, blocked customers |
| `/trust-badges` | Adds secure-payment, shipping and returns badges to checkout, only promising what your store offers |
| `/thank-you-page` | A message after purchase for some or all orders, and an address check that catches typos before they ship |
| `/checkout-widgets <widget>` | Reviews, a rewards progress bar, live chat, gift-message checkboxes, an image banner or a subscribe-and-save upgrade in checkout |
| `/checkout-branding` | Matches checkout to your brand: colors, buttons, fonts, corners and logo, tried on a draft first (Shopify Plus) |
| `/gift-card-design` | Designs your gift card and its purchase form from a template or a copy |
| `/upsell-experiment <offer>` | Sets up an A/B test on one offer |
| `/checkout-audit [days]` | Read-only audit of your checkout with a ranked list of fixes |
| `/upsell-results [days]` | How every checkout and post-purchase offer, funnel and A/B test performed, then picks the winner and ends a finished test on your OK |
| `/checkout-chat [count]` | Answers shoppers chatting from checkout, quickest first, with drafts you approve before they're sent |

Claude asks before changing anything that shoppers will see.

## Try

- "Add a 10% off coffee upsell at checkout for carts with anything from Breakfast"
- "Which of my upsells is underperforming this month?"
- `/post-purchase a second bottle at 25% off for first-time customers`
- `/volume-discount buy 2 save 10%, buy 3 save 15% on all coffee`
- `/checkout-rules stop Kava Calm shipping to Germany`
- `/checkout-audit 60`
- `/upsell-results 30`
- "Who's waiting in checkout chat?"
