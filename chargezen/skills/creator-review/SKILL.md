---
name: creator-review
description: Read-only review of the merchant's Spark! creator and affiliate program in Chargezen — who drives sales, what's owed, whether the balance covers it, refunds that clawed back commission, and partners waiting for approval — with clear next steps. Use when they ask which creators perform, what they owe creators, whether payouts are covered, or how the partner program is doing.
argument-hint: "[days, default 30]"
---

# Creator review

Period: the last $ARGUMENTS days (30 if no number was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; Spark!'s tools here don't change anything. Payouts, approvals and commission changes happen in Chargezen; point the person there.

## Gather

1. **Partners:** `admin_spark_partners.list` with `status: "active"`, and again with `status: "pending"` for applications waiting on them.
2. **Sales credited to partners:** `admin_spark_referred_orders.list`, newest first, page by page until the attributions are older than the period. Total each partner's credited orders and earnings in the period, and note orders with a refund impact or a `revoked` or `in_dispute` commission.
3. **Money:** `admin_spark_partner_finance.get_balance`: available balance, pending deposits, net pending commissions and committed payouts. Pending deposits aren't available yet.
4. **Payouts:** `admin_spark_partner_payouts.list` for recent and upcoming payouts.
5. **Rates, if a partner stands out:** `admin_spark_partners.get` and `admin_spark_commission_profiles.get` for their commission terms.

Amounts are in the workspace's currency. Attribution here is Chargezen's record of credited orders, not live Shopify payment state; say so if someone asks about a specific payment.

## Report

Lead with three lines:

- **Top creators:** the top three by credited orders in the period, with what each earned.
- **Money:** whether the available balance covers net pending commissions plus committed payouts, and by how much it's short or over.
- **Needs you:** pending applications, disputed or revoked commissions, refunds that took commission back.

Then a short table of the top ten partners (name, credited orders, earned, commission status) and one or two suggestions grounded in the numbers, such as a better rate for a creator who's growing fast, or a deposit before the next payout. End by offering the next read they might want.
