---
name: weekly-brief
description: A read-only brief on the merchant's Chargezen workspace for a recent period — orders that haven't shipped, best sellers and their stock, new and canceled subscriptions, customers waiting on a reply, campaign results and creator commissions — ending with the three things that need them most. Use when they ask what needs their attention, how last week went, or for a weekly or Monday summary.
argument-hint: "[days, default 7]"
---

# Weekly brief

Period: the last $ARGUMENTS days, ending now (use 7 if no number was given). Work out the start and end as timestamps with an explicit UTC offset and use the same period everywhere. Reports name the store's time zone in `scope.timezone`; once you know it, use its midnight for the start and end. Until then use UTC and say so.

Follow the `chargezen` skill for how to reach the tools. **Use only tools that read**; change nothing. Skip any part whose tools this connection doesn't have, and say which parts you skipped and why, in one line at the end. The Concierge connection covers shipping, sales and stock, and customers waiting; subscriptions, campaigns and creators need the full Chargezen connection.

## Gather

Run the independent reads together.

1. **Shipping:** `chargezen.shopify_reports.fulfillment_status.v1` for fulfillment orders created in the period. Count what's still open (status not closed or cancelled, remaining quantity above 0). If `not_visible_categories` is set, say those locations weren't checked.
2. **Sales and stock:** `chargezen.shopify_reports.sales_by_sku.v1` for the period. Take the five SKUs with the most units, then `chargezen.shopify_reports.inventory.v1` for those SKUs and report what's available across active locations. Sales are gross line-item sales before discounts and refunds; say so if you give a revenue figure.
3. **Subscriptions** (full Chargezen connection): `chargezen.subscription_reports.movement.v1` for the period with `sources: ["chargezen"]`: new and canceled counts (restarts aren't tracked), and the canceled customers with their order count, spend and the reasons they gave (`cancellation_reasons`). Don't turn it into a churn rate or net figure; the tool says not to.
4. **Customers waiting:** `chargezen.inbox.list.v1` with `status: "handoff_queue"` (waiting for a teammate), then `status: "open"` with `assigned: "unassigned"`. Note how many are waiting and the oldest.
5. **Campaigns** (full Chargezen connection): `chargezen.smartytap_reports.campaigns.v1` for the period (it takes days in the store's time zone): each campaign that sent with its delivered, opened, clicked, orders and revenue credited, in one call.
6. **Creators** (full Chargezen connection): `chargezen.admin_spark_partner_finance.get_balance.v1`. Compare `available_balance` with `pending_commissions_net` plus `committed_payouts`, all in the balance's currency.

## Write the brief

An area with nothing in the period gets one line saying so ("No new or canceled subscriptions this week"); quiet is good news, not an error.

Lead with **three things that need them**, ranked by money or customers at stake, each one line with the number behind it and the fix you can do next. Typical ones:

- orders waiting to ship longer than usual
- a best seller with little stock left
- high-spending customers who canceled (name the top two and the reasons they gave)
- customers waiting on a reply, with the oldest wait
- a creator balance that doesn't cover what's owed
- a campaign with many deliveries and few clicks

Then a short section for each area you read, two to four lines each, plain words, real numbers with the period stated. No tool names, IDs or tables longer than five rows.

End with one offer: the most useful next step you can take for them, such as drafting replies to the customers who are waiting or a win-back message for the customers who canceled.
