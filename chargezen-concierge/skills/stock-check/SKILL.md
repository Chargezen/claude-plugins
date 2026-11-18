---
name: stock-check
description: A read-only stock and sales check for the merchant's Shopify store through Chargezen — best sellers by SKU for a period, live inventory for each across locations, how many days of stock are left at the recent selling rate, and a suggested reorder quantity — so they know what to restock first. Use when they ask what's selling, what's running low, what to reorder, or how much stock a product has.
argument-hint: "[days of sales, default 30] [product or SKU] [days of cover wanted, default 30]"
---

# Stock check

Request: $ARGUMENTS (30 days of sales, the top 15 SKUs and 30 days of cover wanted, if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Read only.** Use timestamps with a UTC offset and say which period you used.

## 1. What sold

`shopify_reports.sales_by_sku` for the period (all SKUs, or the ones they named; for a product name, `products.search` first to find its variants and SKUs). Rank SKUs by units sold. Keep in mind:

- units include cancelled, refunded and test orders, and gross sales are before discounts and refunds; say so if you show revenue;
- each currency is reported separately; don't add them together;
- items without a SKU come back unattributed and can't be matched to stock.

## 2. What's in stock

`shopify_reports.inventory` with `filters: { skus: [...] }` for the top SKUs (and any they named). For each SKU add up `available` across active locations, and note `incoming` and `committed`. Inventory that isn't tracked has no reliable count: say "not tracked" rather than zero. `shopify_locations.list` names the locations.

## 3. Work it out

For each SKU, show your working:

- **Daily rate** = units sold ÷ days in the period.
- **Days left** = available ÷ daily rate (blank when nothing sold).
- **Suggested reorder** = (daily rate × days of cover wanted) − available − incoming, rounded up; none when that's zero or less.

This is a simple average of past sales; it doesn't know about launches, seasons, promotions or supplier lead times. Ask about lead time and add it to the days of cover if they give one.

## 4. Report

Lead with what to reorder first: the SKUs with the fewest days left, each one line with available, days left and the suggested quantity. Then the best sellers that are fine, and slow movers holding a lot of stock (many available, few sold). No tables longer than 15 rows.

This connection can't change stock or place purchase orders. Offer next steps: re-run for one product or location, find the customers who asked about a product that's out (`history.search` for its name), or answer them with `/inbox-triage`.
