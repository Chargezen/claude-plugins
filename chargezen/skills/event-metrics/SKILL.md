---
name: event-metrics
description: A read-only look at the events a store's storefront recorded in Chargezen SmartyTap — placed orders, product views, add-to-carts, launcher activity or a custom event — counted, counted by person or added up by day over a period, split by one property such as currency or state, and narrowed to a saved segment. Use for "revenue by day from orders this month", "how many people added to cart last week", "orders from people in Ohio who clicked last month", or any question about one tracked event over time.
argument-hint: "<the question> [days, default 30]"
---

# Event metrics

The question: $ARGUMENTS. The period is the number of days given, ending today (30 if no number was given).

Follow the `chargezen` skill for how to reach the tools. **Use only reads**, except saving a segment when the question is about a group of people (step 3), and only on the merchant's OK.

These are the events the storefront's pixels and launcher recorded, as SmartyTap › Analytics › Events shows them. They are not the email, text and WhatsApp results: for revenue credited to messages, use `chargezen.smartytap_reports.overview.v1`, `chargezen.smartytap_reports.campaigns.v1` or `chargezen.smartytap_reports.flows.v1` (`/marketing-report`) instead.

## 1. See which events there are

`chargezen.smartytap_events.list_metrics.v1` with `start_date` and `end_date` (days in the store's time zone, at most 366 days apart): each event's `event_type` and `source`, and the properties it carries with their paths and types (such as the number `["total"]` and the text `["currency"]` on `checkout_completed`). Use only events, sources and paths listed there; private keys such as email and phone aren't offered.

## 2. Ask the question

`chargezen.smartytap_events.query.v1` with the same days, the `event_type` and a `measure`:

- `events`: how many times it happened;
- `people`: how many people did it (once per customer when a visitor was linked to one, else once per visitor);
- `sum` with `value_property`: adds up a number the event records.

`group_by` splits the figures by one text, number or yes-no property (such as `["currency"]` or `["shipping_address", "province_code"]`); each series comes back with its total and its figures by day, biggest total first.

**Revenue by day from placed orders:** event `checkout_completed`, measure `sum`, `value_property` `["total"]`, `group_by` `["currency"]`.

- `checkout_completed` is an order completed in the online store's checkout. Subscription renewals, point-of-sale and draft orders aren't in it: say so whenever you call it orders or revenue.
- Sums add the amounts as recorded, in the currency each checkout used, **without converting**. Split by currency and report each currency on its own; never add two currencies together.

## 3. A question about a group of people

The query can't filter on a property's value or combine two events. For "orders from people in Ohio who clicked last month", describe the people as a segment and pass its id:

1. Look for one that already fits with `chargezen.smartytap_segments.list.v1`.
2. Otherwise build it as `/segment` does (`chargezen.smartytap_segments.fields.v1`, then `chargezen.smartytap_segments.preview.v1` to count it) and, on the merchant's OK, save it with `chargezen.smartytap_segments.save.v2` (a new `operation_id`).
3. `chargezen.smartytap_events.query.v1` with that `segment_id`.

The segment is who matches it **now**, not who matched on each day, and only people linked to a customer can match one. Say both.

## 4. What it can't answer

It returns totals only: never a list of people or of single events. It can't compare two periods in one call (run it twice with the same length and say which days each covers), combine two events, or filter on a value. If the merchant needs one of those, say so plainly.

## 5. Write it

Lead with the answer in one line, with the period and what the event covers ("Online-store orders brought in $12,400 in the last 30 days, all in USD"). Then the figures by day or by group in a short table (at most 31 rows; group longer periods of `events` or `sum` by week and say you did; never add up daily `people` figures, because someone active on several days counts once in the range's `total`), and one line on anything striking. Plain words, no IDs. Every figure comes from the result.

End with one offer: compare with the period before, split by another property, or turn the group into a campaign audience (`/campaign`).
