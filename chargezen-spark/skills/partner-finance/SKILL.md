---
name: partner-finance
description: A read-only reconciliation of the Spark! partner-program money in Chargezen for a period — deposits in, payouts out, fees and adjustments in the ledger, pending and failed deposits, and whether the recorded balance agrees with them — flagging anything that doesn't add up. Use for month-end or accounting, when the balance looks wrong, or when they ask where the program's money went.
argument-hint: "[month, or days, default last calendar month]"
---

# Partner finance

Period: $ARGUMENTS (a month name, a number of days, or last calendar month if nothing was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; nothing here creates, refunds or cancels a deposit or payout.

## 1. Gather

1. **Balance now:** `admin_spark_partner_finance.get_balance`: available, reserved, pending deposits, total deposited, total paid out, committed payouts, last deposit and payout dates.
2. **Ledger:** `admin_spark_partner_finance.list_transactions` with `start_date` and `end_date` for the period, every page. Total by `transaction_type` (`deposit`, `payout`, `fee`, `adjustment`, `refund` of a deposit, `reservation`, `release`). Note the running balance at the start and end of the period.
3. **Deposits:** `admin_spark_partner_finance.list_deposits`, enough pages to cover the period: gross, fee and net, status, method.
4. **Payouts:** `admin_spark_partner_payouts.list` with `status: "paid"` covering the period, and `failed`.

These are Chargezen's records, not a bank statement. A paid payout means a teammate recorded the payment; it isn't bank confirmation.

## 2. Reconcile

- **Opening balance + deposits − payouts − fees ± adjustments = closing balance?** Use the ledger's running balance. Show the sum and any gap.
- **Deposits:** each completed deposit in the period should have a `deposit` ledger entry. List completed deposits with no matching entry, and pending ones (not available yet). Name failed, refunded or cancelled deposits.
- **Payouts:** each payout marked paid in the period should have a `payout` ledger entry with its `payout_id`. List any without one, and ledger payouts with no paid payout.
- **Fees:** total processing fees taken from deposits.

## 3. Report

Lead with one line: money in, money out, closing balance, and "reconciles" or the gap. Then a short summary by type and a list of mismatches (date, amount, what's missing). Keep amounts in the balance's currency.

If something needs correcting, the team records a deposit on **Partner Finance** and marks payouts on **Partner detail** in the Spark! admin (`admin_spark_partner_app.guide` with `finance` or `partner_detail`). Suggest the person check bank statements for any gap rather than guessing the cause.
