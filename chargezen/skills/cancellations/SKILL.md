---
name: cancellations
description: Read-only look at who canceled their subscription in Chargezen over a period and what it cost — new versus canceled subscriptions, monthly revenue lost, the customers who left with their order history and spend, and the reasons they gave — ending with what to do about it. Use when someone asks who canceled, why customers leave, or how subscriptions are trending.
argument-hint: "[days, default 30]"
---

# Cancellations

Period: the last $ARGUMENTS days, ending now (30 if no number was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; change nothing.

1. `subscription_reports.movement` for the period and for the same length before it, `sources: ["chargezen"]`. It reports new and canceled counts, the monthly revenue of each, and the canceled customers with their order count and spend; where it returns a `customer_ref` and the reasons they gave, use them.
2. Don't compute a churn rate or net figure; the report says it isn't the source for those.
3. For the top five customers by spend who left, `admin_customer_subscriptions.search` with their `customer_ref` shows what they were subscribed to and when it ended.

## Report

- One line: canceled versus new this period, and versus the period before.
- Monthly revenue that left, by currency.
- The customers worth a personal note: name, orders, spend, what they had, and their reason if given.
- Patterns in the reasons, if there are any (price, too much product, quality, moving), each with a count.
- Two or three next steps grounded in the above: a win-back message (the `/win-back` skill, in the full Chargezen plugin), offering "ship less often" or "skip" earlier, or a plan change.
