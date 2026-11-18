---
name: payout-prep
description: Read-only Spark! payout preparation in Chargezen — what each partner is owed, which payouts are waiting or processing, who is under the minimum payout, refund deductions, and whether the program balance covers it all, with a funding warning and where to mark payouts paid in the Spark! admin. Use before paying creators, when they ask what they owe partners, whether they have enough funds for payouts, or why a partner hasn't been paid.
argument-hint: "[partner name, or all]"
---

# Payout prep

Scope: $ARGUMENTS (every partner if nothing was named).

Follow the `chargezen` skill for how to reach the tools. **Use only reads.** Spark! tools here don't pay anyone or change a payout; payments are made outside Chargezen and then marked paid in the Spark! admin.

## 1. Gather

1. **Rules:** `admin_spark_partner_settings.get`: minimum payout (`minimum_payout_amount`) and how often payouts run (`payout_frequency`). If `settings` is null, the program has no saved settings; say so.
2. **Money:** `admin_spark_partner_finance.get_balance`: `available_balance`, `pending_deposits`, `pending_commissions_net` (commission not yet in a payout, after open refund adjustments) and `committed_payouts` (payouts pending or processing).
3. **Payouts waiting:** `admin_spark_partner_payouts.list` with `status: "pending"`, then `"processing"`, then `"failed"`, every page. For a named partner, add `partner_id` (from `admin_spark_partners.list` with `query`). Read `admin_spark_partner_payouts.get` for each waiting payout over a size worth checking, or for the named partner: the orders in it and any adjustments (refund deductions).
4. **Owed but not in a payout yet:** `admin_spark_referred_orders.list` with `commission_status: "pending"` and again `"processed"`, every page; orders with no `payout_id` are still to be batched. Total them per partner.

## 2. Check

- **Covered?** Compare `available_balance` with `committed_payouts` plus `pending_commissions_net`. Pending deposits aren't available yet: show them separately ("covered once the pending deposit lands").
- **Under the minimum:** partners whose unpaid total is below the minimum payout; they roll over to a later payout.
- **Failed payouts:** name the partner and amount; they still need paying.
- **Deductions:** payouts with refund adjustments, so the partner isn't surprised by a lower amount.
- **In dispute:** orders with `in_dispute` commission aren't ready to pay.

## 3. Report

Lead with one line: total due now, the balance, and covered or short by how much. Then a short table (partner, in waiting payouts, not yet batched, deductions, status) of at most fifteen rows, largest first.

Then the next step, in the admin (use `admin_spark_partner_app.guide` with `partner_detail` and `finance` for the exact pages): add funds on **Partner Finance** if short, and after paying a partner outside Chargezen, open their **Partner detail** and use **Mark payout as paid** with the date and transaction reference. Paying early or below the minimum asks for an extra confirmation there. Never suggest Claude can pay or mark a payout.
