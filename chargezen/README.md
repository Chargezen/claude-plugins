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
| `/renewals [days]` | Read-only: orders renewing in the coming days with a packing list, recurring revenue and stock warnings |
| `/product-swap <old> [new]` | Moves every active subscriber of a product onto a replacement after you approve the batch, skipping and reporting any that can't be swapped |
| `/plan-audit` | Read-only review of every subscription plan: options, discounts, where it shows and which products carry it, with the gaps worth fixing |
| `/invoice <customer or order>` | Finds an invoice, gets its PDF, or emails it to an address you approve, creating it if the order has none |
| `/points <customer>` | Looks up a customer's points, tier and rewards, and adds, deducts, redeems or undoes points on your OK |
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

Claude asks before anything reaches your customers or changes your store.

## Try

- `/weekly-brief`
- `/win-back 20% off your next order`
- `/campaign Holiday bundle to the VIP list, Friday 9am`
- "Which orders from the last week haven't shipped?"
- "Skip Jane Cooper's next subscription order."
