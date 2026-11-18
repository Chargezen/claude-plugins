---
name: partner-health
description: A read-only health check of the Spark! partner program in Chargezen — applications waiting, active partners with no sales, partners who have gone quiet, partners with unusually high refunds, disputes or revoked commission, links with no commission, and settings worth a second look (approval, attribution window, self-referrals, minimum payout, default commission) — ending with a ranked list of fixes and where to make them. Use for a program audit, when they ask which partners are inactive, or whether anything looks off in the affiliate program.
argument-hint: "[days, default 90]"
---

# Partner program health

Window: the last $ARGUMENTS days (90 if no number was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads.**

## 1. Gather

1. `admin_spark_partners.list` for each status: `pending`, `active`, `suspended`. Note how long pending applications have waited (`joined_at`).
2. `admin_spark_referred_orders.list` for the window, every page. Per partner: orders, sales, commission, refunded orders, and `in_dispute` or `revoked` commission.
3. `admin_spark_partner_settings.get`: auto-approval, default commission, minimum payout and frequency, attribution window (`cookie_duration_days`), self-referrals, tax info.
4. For flagged partners only, `admin_spark_partners.get`: links and their profiles, clicks, refund clawbacks and negative balance.

## 2. What to flag

- **Waiting on you:** pending applications, oldest first (unless auto-approval is on).
- **No sales:** active partners with no credited order in the window; those who joined more than 30 days ago are worth a nudge.
- **Gone quiet:** partners with sales earlier in the window and none in the last 30 days.
- **Unusual patterns:** a partner whose refunded share of orders is well above the program's, many disputed or revoked commissions, a negative balance, or many orders with very few clicks. Say these are worth a look, not proof of abuse; these records don't show who the buyer was.
- **Set-up gaps:** links with no commission profile, no default profile, no saved settings at all.
- **Settings to question:** self-referrals allowed, a very short or very long attribution window, no minimum payout, tax info not required if they pay partners who need tax forms.

## 3. Report

Lead with the three fixes that matter most, each one line with the number behind it. Then one line each for the other findings, and a count of partners by status.

All changes are made in the Spark! admin: approving or suspending on **Partner detail**, rates on **Commission Profiles**, the rest on **Settings**. Use `admin_spark_partner_app.guide` for the exact page and controls. Offer `/partner-profile` for any partner you flagged.
