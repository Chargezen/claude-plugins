---
name: spark-help
description: Answer "how do I…" questions about the Spark! admin in Chargezen — inviting or approving partners, creating or editing a commission profile, recording a deposit, marking a payout paid, program settings, partner notifications, the partner portal pages and analytics — with the exact page and controls, using the workspace's real settings where they matter. Also explains to a member who wants brand deals for themselves where creators sign up. Use when someone asks how to do something in Spark! or what a Spark! page does.
argument-hint: "<what they want to do>"
---

# Spark! help

The question: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Use only reads.** This connection can't change anything in Spark!; it tells the person where and how.

## 1. Pick the page

`admin_spark_partner_app.guide` with the `layout_key` that fits:

| They want to | layout_key |
|---|---|
| see the program at a glance | `overview` |
| find partners | `partners` |
| approve, suspend, see links or mark a payout paid | `partner_detail` |
| invite a partner | `invite` |
| see or change commission rates and discounts | `commission_profiles`, `commission_profile_create`, `commission_profile_edit` |
| review credited orders | `orders` |
| see payout history | `payouts` |
| add funds, see the balance | `finance` |
| click and sales charts | `analytics` |
| partner sign-up and landing pages | `customize` |
| emails partners get | `notifications` |
| connect another app | `integrations` |
| approval, payout minimum, attribution window, self-referrals | `settings` |
| get brand deals for themselves as a creator | `for_creators` |

Read more than one if the job spans pages (inviting someone onto a specific rate is `invite` plus `commission_profiles`).

## 2. Add the real values

Where the answer depends on what's set up, read it: `admin_spark_partner_settings.get` for approval, minimum payout and frequency; `admin_spark_commission_profiles.list` for the profiles they can choose; `admin_spark_partners.list` to find the partner they mean.

## 3. Answer

Give the page (its route from the guide), then the steps as a short numbered list in plain words, and what will happen when they save (for example, an invited partner starts as pending unless auto-approval is on). Only describe controls the guide names; if it doesn't cover the request, say so rather than guessing, and suggest Chargezen support. Offer to check the result afterwards with a read, such as `/partner-profile`.
