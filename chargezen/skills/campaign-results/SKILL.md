---
name: campaign-results
description: A read-only review of SmartyTap campaign results in Chargezen over a period — what was delivered, opened, clicked and unsubscribed, the orders and revenue credited, how email, text and WhatsApp compared, which A/B versions won — ending with what worked, what didn't and three things to do next. Use when they ask how their campaigns did, which campaign made the most, or for a monthly marketing report.
argument-hint: "[days, default 30]"
---

# Campaign results

Period: the last $ARGUMENTS days, ending now (use 30 if no number was given). Work out the start and end as timestamps with an explicit UTC offset and use the store's time zone (`smartytap_campaigns.authoring_options` names it) once you know it.

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; change nothing.

## 1. Gather

1. `smartytap_campaigns.list` with `launched_from` and `launched_to` set to the period; follow `next_page` until it's done. Campaigns never launched are left out.
2. `smartytap_campaigns.report` for each (run them together). Per campaign and per message: accepted, delivered, opened, clicked, replied, bounced, unsubscribed, orders and revenue credited, conversion rate, and A/B versions with the winner.
3. Note the attribution window the report describes (for example, orders within 5 days of a click), and say it once in the review.

A figure a channel doesn't report (opens for texts) is null with a reason; don't fill it in. Flows (automations) aren't campaigns and aren't in these results.

## 2. Work it out

From the counts, work out per campaign: open rate and click rate (of delivered), unsubscribe rate, revenue per message delivered. Say these are worked out from the report's counts.

Look for:
- **Best and worst** by revenue and by clicks, and what they had in common (channel, day and time, audience, offer, subject style);
- **Channels:** email against text against WhatsApp on clicks and revenue per message;
- **Warning signs:** unsubscribes or bounces well above the others, high delivery with almost no clicks, audiences sent to very often;
- **A/B tests:** which versions won and by how much.

## 3. Write the review

Lead with **three takeaways**, each one line with the number behind it (in the shape of "Texts earned more per message than emails: $X against $Y"). Then the top five campaigns in a short table (name, sent, delivered, clicks, orders, revenue), and one line on anything worrying. Plain words, the period stated, no IDs.

End with one offer: draft the next campaign built on what worked (`/campaign`), plan next month (`/marketing-calendar`), or build an unengaged segment to leave out if unsubscribes are climbing (`/segment`).
