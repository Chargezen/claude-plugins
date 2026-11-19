---
name: marketing-report
description: A read-only SmartyTap marketing report in Chargezen for a period — how email, text and WhatsApp did (delivered, opened, clicked, unsubscribed, credited orders and revenue) against the period before, then the campaigns and flows behind those numbers — with subscriber growth, text deliverability and plan usage when they ask. Use for a monthly marketing report, "how did email and text do last month", or comparing one period with the one before.
argument-hint: "[days, default 30]"
---

# Marketing report

Period: the last $ARGUMENTS days, ending today (use 30 if no number was given). The report tools take days (`YYYY-MM-DD`) in the store's time zone, at most 366 days apart; each result states the range it used. Say which period you used.

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; change nothing.

## 1. Overview first

`chargezen.smartytap_reports.overview.v1` with `start_date` and `end_date`: for each channel and for all together, recipients, delivered, opened, clicked, unsubscribed, credited orders and revenue and the rates, each with its change against the previous period of the same length; what texts took off the text credit balance; WhatsApp results; and the same figures by day.

- Sends count on the day they were sent and orders on the day they were placed, so some of a period's revenue can come from sends made before it. Say so once.
- Test sends and opt-in confirmations aren't counted.
- Leave `attribution` out: the workspace's own windows apply. Pass it only when the merchant asks how the numbers would look with other windows, and say that's what you did.

## 2. Then the campaigns and flows behind it

For the same range, run these together and follow `next_cursor` while `has_more` is true:

- `chargezen.smartytap_reports.campaigns.v1`: each one-off campaign that sent in the range or had orders credited to it, with its results in the range;
- `chargezen.smartytap_reports.flows.v1`: the same for flows. A deleted flow that sent keeps its row, named "Deleted flow: …".

## 3. Only when they ask

- **Subscriber growth:** `chargezen.smartytap_reports.subscriber_growth.v1`: people who subscribed and unsubscribed per channel, by day, and where they joined or left. It counts consent changes, not the growth of one list or segment.
- **Why texts didn't arrive:** `chargezen.smartytap_reports.text_deliverability.v1`: sent, delivered, didn't arrive, waiting and not sent, the reasons in plain words, and each sending number's figures. It covers texts only.
- **Store events** such as revenue by day from placed orders, or add-to-carts: `/event-metrics`. Those are the storefront's recorded events, not revenue credited to messages; don't mix the two in one figure.
- **Plan usage:** `chargezen.smartytap_usage.get.v1`: contacts against the plan's limit, marketing emails sent this calendar month against the monthly limit and when it resets, and the text credit balance. It's today's position, not the period's; `plan_limits` null means the plan sets no limit.

## 4. Write the report

Lead with **three takeaways**, each one line with the number and its change (in the shape of "Email revenue rose 18% to $X while texts held steady"). Then:

- a short table per channel: delivered, open rate, click rate, orders, revenue, and the change against the period before;
- the top five campaigns and the top five flows by revenue;
- one line on anything worrying: unsubscribes climbing, a falling delivery rate, text spend rising faster than revenue.

A figure a channel doesn't report (opens for texts, orders while attribution is off) is null: leave it blank and say why, never fill it in. Plain words, the period stated, no IDs.

Where the assistant shows interactive views, a campaign's or a flow's report opens as one when you call it; it presents the same figures, so the written report still states every number, and never tell the merchant to open the admin to see them.

End with one offer: look at a flow that's slipping step by step for the same days (`/flow-results`), dig into campaigns (`/campaign-results`), or build the next campaign on what worked (`/campaign`).
