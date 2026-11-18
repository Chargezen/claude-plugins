---
name: segment
description: Build or change a SmartyTap segment in Chargezen — a live audience such as VIPs, repeat buyers, people who haven't opened in 90 days, subscribers of a product or survey answerers — from the conditions the segment editor offers, counted with sample names before it's saved, and saved only on the merchant's OK. Also builds an "unengaged" segment to leave out of campaigns. Use when they want to target, define or clean up an audience.
argument-hint: "<who should be in it>"
---

# Segment

Who: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

A segment is live: whoever matches its conditions is in it, recounted as people change, so campaigns and flows reach whoever matches when they send. Being in a segment never means someone agreed to marketing; sending still checks consent. A **list** is different: a fixed group of people put on it by hand or import (`/list-import`).

## 1. Check what exists

`smartytap_campaigns.authoring_options` lists the segments and lists. If one already fits, say so and count it instead of building a near-copy. To change an existing segment, its id goes in `segment_id`.

## 2. Turn the brief into conditions

1. `smartytap_segments.fields`: each field the segment editor can test, its operators, and this workspace's own options (custom properties, tracked events, order activity, matching orders and subscriptions, lists). Use only fields and values listed there.
2. Common audiences, when the fields offer what they need:
   - **VIPs:** total spent or order count above a level the merchant names;
   - **Lapsed buyers:** placed an order before, none in the last N days;
   - **Unengaged:** no email opened or clicked in 90–180 days;
   - **Product buyers or subscribers:** matching orders or subscriptions for a product;
   - **Survey answers:** a contact property a survey saved (such as `heard_about_us`).
3. `smartytap_segments.preview` with the conditions: the count now and up to five people by name. If it's refused, fix what it names. If the count looks wrong (zero, or everyone), say so and adjust before going on.

Show the person, in plain words, who's in it ("customers who spent over $300 and ordered in the last year"), the count and the sample names.

## 3. Save

On their OK: `smartytap_segments.save` with a name that says who's in it, a short description, `active: true` and a new `operation_id`. Editing replaces the whole set of conditions; campaigns and flows already using it reach the new audience from their next send, so say so first.

## 4. Use it

- Target a campaign with it (`/campaign`), or exclude it from one: an unengaged segment in a campaign's **exclude** keeps sends to people who still read, which protects deliverability.
- Start a flow when someone joins it: the **Joined a segment** trigger (`smartytap.segment.entered`), for example a thank-you when someone becomes a VIP.
- Segments and lists can't be deleted through these tools. A segment no longer wanted can be saved with `active: false` so campaigns and flows can't choose it.
