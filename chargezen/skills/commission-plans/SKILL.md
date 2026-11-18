---
name: commission-plans
description: Read-only review of the Spark! commission profiles in Chargezen — each tracked-link and discount-code profile's commission rate, the customer discount it gives, limits and schedule, which partners are on it, the program's default profile, and what each profile actually earned — with the gaps worth fixing and where to change them in the Spark! admin. Use when they ask what rates creators get, who is on which plan, whether a rate is too high or low, or before changing commission.
argument-hint: "[profile, discount code or partner, or all]"
---

# Commission plans

Focus: $ARGUMENTS (every profile if nothing was named).

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; Spark! tools here don't create or edit a profile.

## 1. Gather

1. `admin_spark_commission_profiles.list` (with `query` for a named profile or code): every profile, its type (`automatic_tracking` is a tracked link, `discount_code` a code), commission rate and type (percentage or fixed), and customer discount.
2. `admin_spark_commission_profiles.get` for each: the full terms (minimum purchase, one use per customer, usage and recurring-order limits, start and end dates, which discounts it combines with) and `assigned_partners`.
3. `admin_spark_partner_settings.get`: the default profile new partners get.
4. For a named partner: `admin_spark_partners.list` with `query`, then `admin_spark_partners.get` for their links and the profile on each.
5. **What it earned:** `admin_spark_referred_orders.list` for the last 90 days (every page), then `admin_spark_referred_orders.get` on a sample to see which profile each order was credited under (`commission_profile_id`). Group sales and commission by profile where the sample allows; say it's a sample if you didn't read every order.

Rates are saved configuration. Past commission comes from each order's saved facts, not today's rate. A saved discount doesn't prove the Shopify code is live.

## 2. Look for

- profiles with no partners on them, or partners whose links have no profile;
- a default profile that's missing (`default_commission_profile` null) or no default at all;
- profiles past their end date that partners still sit on;
- the same kind of partner on very different rates, with no reason in the numbers;
- a high customer discount plus a high commission on the same profile (paying twice for one sale);
- recurring-order commission with no limit on a subscription product, if that's not intended.

## 3. Report

A short table: profile, type, commission, customer discount, partners on it, sales and commission in the last 90 days. Then up to three findings, each with the number behind it and the suggested change.

Changes are made in the Spark! admin. Use `admin_spark_partner_app.guide` with `commission_profile_edit`, `commission_profile_create` or `settings` and give the page and the controls to use. Say that a new rate applies to orders credited after the change; past commission stays as recorded.
