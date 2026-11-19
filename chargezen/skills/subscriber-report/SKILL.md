---
name: subscriber-report
description: A read-only picture of the merchant's subscribers in Chargezen — how many active and paused subscriptions there are, the recurring revenue they carry, which products and delivery frequencies are most popular, new versus canceled over a period, and failed payments — ending with what stands out. Use when they ask how many subscribers they have, their subscription revenue, top subscription products, or for a subscription overview or monthly subscription report.
argument-hint: "[days for new vs canceled, default 30]"
---

# Subscriber report

Period for new and canceled: the last $ARGUMENTS days (30 if no number was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads.** Covers subscriptions that run on Chargezen (Shopify); say that Recharge and Stripe-backed subscriptions aren't counted in the base.

## 1. Gather

1. **The base:** `chargezen.admin_customer_subscriptions.find.v1` with `statuses: ["ACTIVE"]`, every page, then `statuses: ["PAUSED"]`. From each subscription's stored products, price and cadence, total:
   - active and paused counts;
   - recurring revenue per order, and per month by converting each cadence (weekly × 52 ÷ 12, every two months ÷ 2, and so on), by currency;
   - subscriptions and units per product, and how many are on each delivery frequency.
   For a very large base, say how many pages you read if you stop early.
2. **Movement:** `chargezen.subscription_reports.movement.v1` for the period and the same length before it, `sources: ["chargezen"]`: new and canceled counts and the monthly revenue of each. Don't compute a churn rate or net figure; the report says it isn't the source for those.
3. **At risk:** `chargezen.admin_subscriptions.failed_payments.v1` (retrying, first page) for how many renewals are failing now.
4. **Coming up:** `chargezen.admin_customer_subscriptions.find.v1` with `statuses: ["ACTIVE"]` and next charge in the next 7 days: how many renew this week.

These are Chargezen's stored snapshots, not live Shopify state, and prices are before shipping and tax.

## 2. Report

- **Headline:** active subscriptions, monthly recurring revenue, paused count, and new versus canceled this period against the one before.
- **Top products:** up to eight, with subscriptions and monthly revenue each.
- **Frequencies:** the split by delivery frequency.
- **Watch:** failing payments now, a high paused share, a product carrying most of the revenue.

Then two or three suggestions grounded in the numbers, pointing to the skill that does it: `/cancellations` for why people left, `/failed-payments` to chase failing cards, `/renewals` for this week's packing list, `/plan-audit` to review plans and discounts.
