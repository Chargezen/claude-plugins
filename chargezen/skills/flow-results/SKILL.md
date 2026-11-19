---
name: flow-results
description: A read-only review of how SmartyTap flows (automations) in Chargezen performed — every flow that sent in a period with its delivered, opened, clicked, unsubscribed, credited orders and revenue, then, for the flows that matter, each email, text and WhatsApp step's results to find the weakest step — ending with what to fix. Use when they ask how their flows are doing, which flow makes the most, or which email in a flow is weakest.
argument-hint: "[days, default 30] [flow name]"
---

# Flow results

The request: $ARGUMENTS. The period is the number of days given, ending today (30 if no number was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads**; change nothing.

## 1. Flows for the period

`chargezen.smartytap_reports.flows.v1` with `start_date` and `end_date` (days in the store's time zone, at most 366 days apart), following `next_cursor` while `has_more` is true: each flow that sent in the range or had orders credited to it, with recipients, delivered, opened, clicked, unsubscribed, credited orders and revenue and the rates in that range. Sends count on the day they were sent and orders on the day they were placed. A deleted flow keeps its row ("Deleted flow: …") with no `flow_id`.

If they named a flow, find it here, or by name with `chargezen.workflows.list.v1` when it didn't send in the period (say so: a flow that sent nothing earned nothing).

## 2. Step by step for the flows that matter

For the named flow, or the two or three with the most revenue or the most recipients, `chargezen.workflows.report.v1` with its `flow_id`. It returns the flow's totals and one row per email, text and WhatsApp step: recipients, delivered, opened, clicked, unsubscribed, credited orders and revenue and the rates; a survey step adds how many answered; a removed step keeps its row while it has sends.

**These step figures are all time, since the flow first sent; there is no date range.** Say so whenever you show them next to the period's figures, and don't subtract one from the other.

Match each row to its step in the flow with `chargezen.workflows.get.v1` (`node_id`) when you need the step's place, wait or content.

## 3. Find the weakest step

Compare the steps of one flow with each other, not with other flows:

- **Opens drop sharply at one email:** its subject or preview text, or the wait before it;
- **Opens fine, clicks low:** the email's content, its button or its offer;
- **Unsubscribes jump at one step:** too many messages too close together, or one that reads as off-topic;
- **A text with clicks but no orders:** the link or the landing page;
- **A late step with almost no recipients:** most people leave before it (they ordered, or a filter stopped them); that can be working as intended.

## 4. Write it

Lead with the flows ranked by revenue in the period (name, recipients, click rate, orders, revenue), then for each flow you opened, its steps in order with one line each and the weakest one named with the number behind it. Plain words, no IDs.

End with one offer: rewrite the weakest email (`chargezen.email_documents.apply_ops.v1` at its document address, then `chargezen.workflows.send_test.v1` to see it), change a wait or a text (`/flow-health` has the steps), or see where people stopped with `chargezen.workflows.list_runs.v1`. Changing an active flow changes what customers get from that moment: ask first.
