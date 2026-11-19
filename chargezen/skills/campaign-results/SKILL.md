---
name: campaign-results
description: A read-only review of SmartyTap one-off campaign results in Chargezen over a period — what was delivered, opened, clicked and unsubscribed, the orders and revenue credited, how email, text and WhatsApp compared, which A/B versions won — ending with what worked, what didn't and three things to do next. Use when they ask how their campaigns did, which campaign made the most, or to compare several campaigns.
argument-hint: "[days, default 30]"
---

# Campaign results

Period: the last $ARGUMENTS days, ending today (use 30 if no number was given). The report tool takes days (`YYYY-MM-DD`) in the store's time zone, at most 366 days apart.

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; change nothing.

## 1. Gather

1. `chargezen.smartytap_reports.campaigns.v1` with `start_date` and `end_date`, following `next_cursor` while `has_more` is true: every one-off campaign that sent in the period or had orders placed in it credited to it, with recipients, delivered, opened, clicked, unsubscribed, credited orders and revenue, the rates and what its texts cost, all in one call. Sends count on the day they were sent and orders on the day they were placed. This is the table for several campaigns.
2. `chargezen.smartytap_campaigns.report.v1` only for the campaigns you need to open up (the best and the worst, and any with an A/B test): one campaign's figures all time, per message and per A/B version with the winner. Say these are all time when you show them beside the period's table. Where the assistant shows interactive views, this report opens as one; it presents the same figures, so still state them in words and never tell the merchant to open the admin to see them.
3. Note the attribution window the results describe (for example, orders within 5 days of a click), and say it once in the review.

**Campaigns with one tag** ("how did everything tagged Black Friday do?"): `chargezen.smartytap_campaigns.list.v1` with `tag` (exact; `message_tag` is the tag on a message, and `query` only searches names), then pick those campaigns' rows from the table or open each with `chargezen.smartytap_campaigns.report.v1`.

A figure a channel doesn't report (opens for texts) is null with a reason; don't fill it in. Flows (automations) aren't campaigns and aren't in these results; `/flow-results` covers them.

## 2. Work it out

Use the rates the table returns; work out only what it doesn't give, such as revenue per message delivered, and say that one is worked out from the counts.

Look for:
- **Best and worst** by revenue and by clicks, and what they had in common (channel, day and time, audience, offer, subject style);
- **Channels:** email against text against WhatsApp on clicks and revenue per message;
- **Warning signs:** unsubscribes or bounces well above the others, high delivery with almost no clicks, audiences sent to very often;
- **A/B tests:** which versions won and by how much.

## 3. Write the review

Lead with **three takeaways**, each one line with the number behind it (in the shape of "Texts earned more per message than emails: $X against $Y"). Then the top five campaigns in a short table (name, sent, delivered, clicks, orders, revenue), and one line on anything worrying. Plain words, the period stated, no IDs.

End with one offer: draft the next campaign built on what worked (`/campaign`), plan next month (`/marketing-calendar`), or build an unengaged segment to leave out if unsubscribes are climbing (`/segment`).
