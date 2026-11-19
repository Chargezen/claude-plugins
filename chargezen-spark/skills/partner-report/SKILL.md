---
name: partner-report
description: A read-only Spark! partner report for a month or any period in Chargezen — credited orders, sales and commission for every partner, ranked, compared with the period before, with new partners, refunds that took commission back and payouts made — written so it can be shared with the team. Use when they ask for a monthly affiliate report, a creator leaderboard, who sold the most, or how the partner program did last month.
argument-hint: "[month, or days, default last calendar month]"
---

# Partner report

Period: $ARGUMENTS (a month name, a number of days, or last calendar month if nothing was given). Use the same length right before it as the comparison period.

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; Spark! tools here don't change anything.

## 1. Gather

1. **Credited orders:** `chargezen.admin_spark_referred_orders.list.v1` with `from` and `to` for the period (`to` is exclusive), reading every page (`pagination.total_pages`). Do the same for the comparison period.
2. **Per partner**, from those orders: credited orders, sales (`order_total`), commission earned (`earned_commission`), refunded orders (`is_refunded`) and commission taken back (`refunded_commission`), and orders whose commission is `in_dispute` or `revoked`.
3. **New partners:** `chargezen.admin_spark_partners.list.v1` with `status: "active"`; count those whose `joined_at` falls in the period, and how many of them already have a credited order.
4. **Payouts:** `chargezen.admin_spark_partner_payouts.list.v1` (newest first, enough pages to cover the period): payouts marked `paid` in the period and their total, plus any `failed`.

Amounts are in the workspace's currency (the `currency` on each result). These are Chargezen's records of credited orders, not live Shopify payments; say so once.

## 2. Write the report

- **Headline, three lines:** total credited orders, sales and commission for the period with the change against the period before; how many partners made at least one sale; commission paid out.
- **Leaderboard:** the top ten partners by sales (name, orders, sales, commission, change from the period before). Name anyone new in the top ten and anyone who dropped out of it.
- **Worth a look:** refunds that took commission back, disputed or revoked commissions, new partners with no sale yet.
- **Commission as a share of sales**, overall, if both figures are there.

No tool names or IDs. Keep it to one screen so it can be pasted into a team channel. Offer a next read: one partner in depth (`/partner-profile`), what's due at the next payout (`/payout-prep`), or the rates behind the top earners (`/commission-plans`).
