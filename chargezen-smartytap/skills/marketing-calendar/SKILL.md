---
name: marketing-calendar
description: Plan a month of SmartyTap campaigns in Chargezen from what has worked before — dates, audiences, channels and offers around the merchant's launches, sales and holidays, spaced so nobody is over-messaged and checked against flows already running — then draft each campaign on the campaign calendar for the merchant to review. Nothing is scheduled or sent until they launch each one. Use for a marketing calendar, a monthly or holiday promo plan, or "what should we send next month?".
argument-hint: "[month] [launches, sales, goals]"
---

# Marketing calendar

The request: $ARGUMENTS (next month if none was named).

Follow the `chargezen` skill for how to reach the tools.

## 1. Learn from what's there

1. **Past results:** `smartytap_campaigns.list` launched in the last 90 days, then `report` on each: which channels, days, times, audiences and offers earned clicks and orders, and which drew unsubscribes.
2. **Already planned:** `smartytap_campaigns.list` with status `scheduled` and `draft`, so the plan builds on them rather than doubling up.
3. **Always-on flows:** `workflows.list` (welcome, abandoned cart, win-back…). A campaign doesn't need to do their job.
4. **Audiences and setup:** `smartytap_campaigns.authoring_options` for lists, segments, senders, time zone and whether texts can send.

## 2. Ask for what only they know

In one message: launches, restocks or sales in the month with real dates; the offer for each (a real discount code from their store, named exactly; this connection can't check codes); anything they don't want to send. Add the dates that matter for their market and audience (holidays, seasonal moments) and say which you picked.

## 3. Propose the plan

A short table: date and local time, name, goal, audience, channel, offer, one line on the idea. Rules of thumb:

- One or two emails a week to the main list; texts for the moments that matter most (launch day, last chance), not every send.
- Leave a day or two between sends to the same people. Smart sending also skips people messaged in the last 16 hours (email) or 24 hours (texts).
- Send at the days and times that did best in step 1; say what that was.
- Give VIPs or subscribers early access before the main list when there's a launch or sale.
- Leave out an unengaged segment from the bigger sends, if there is one.

Adjust it with them until they're happy.

## 4. Draft the campaigns

For each agreed row, on their OK: `smartytap_campaigns.create` with a new `operation_id`, the audience, the send time (`schedule_once` at the local date and time), the goal, a tag for the month and a `calendar_color`, so they show together on SmartyTap's campaign calendar. Write a first version of each email with `email_documents.apply_ops` and each text in the definition, following `/campaign`.

They stay **drafts**: a send time on a draft sends nothing. Tell the person so plainly. Each one goes out only when it's launched, one at a time, after `review` and `preview_audience` show who gets it and what texts cost, and they say yes (`/campaign` steps 3 and 4).

End with the list of drafts and their dates, and offer to finish and launch the first one.
