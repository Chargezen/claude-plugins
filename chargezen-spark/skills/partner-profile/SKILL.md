---
name: partner-profile
description: A read-only deep dive on one Spark! partner in Chargezen — their status, tracked links and discount codes with the commission on each, clicks, orders, sales and commission to date, recent credited orders, refunds and clawbacks, and their payouts — ending with a plain summary and suggestions. Use when they ask how a particular creator or affiliate is doing, before a call with a partner, or when deciding a partner's rate.
argument-hint: "<partner name or email>"
---

# Partner profile

Partner: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Use only reads.**

## 1. Gather

1. `chargezen.admin_spark_partners.list.v1` with `query`. If several match, ask which one.
2. `chargezen.admin_spark_partners.get.v1` with their `record_id`: membership status, links (each with destination and commission profile), lifetime clicks, unique clicks, QR scans, orders, sales and commission, refund totals and clawbacks (`refund_clawback_open`, `negative_balance`), and payouts.
3. `chargezen.admin_spark_referred_orders.list.v1` with `partner_id` for the last 90 days (every page): orders and commission by month, refunds, disputed or revoked commission.
4. For each commission profile on their links, `chargezen.admin_spark_commission_profiles.get.v1`: rate and customer discount.
5. `chargezen.admin_spark_partner_payouts.list.v1` with `partner_id`: what's been paid, what's waiting.

Lifetime commission leaves out revoked orders; lifetime order counts and sales keep them. Everything is for this workspace only, even if the creator works with other brands.

## 2. Report

- **One-line verdict:** e.g. "Growing: 34 orders in 90 days, up from 12, earning 15% on a tracked link."
- **Numbers:** orders and sales by month for the last three months; clicks to orders (orders ÷ unique clicks) for their lifetime, as a rough conversion.
- **Links and rates:** each link or code, its commission and customer discount.
- **Money:** paid to date, waiting, and any open clawback they'll owe from refunds.
- **Flags:** high refund share, disputed commissions, a negative balance, a link with no commission profile, suspended or pending status.

Suggest one or two things grounded in the numbers, such as a better rate for a fast grower or a check on a partner with many refunds. Rate changes, approval and suspension are done in the Spark! admin's **Partner detail** page (`chargezen.admin_spark_partner_app.guide.v1` with `partner_detail`); say where, never that you'll do it.
