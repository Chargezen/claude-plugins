---
name: segment
description: Build, read or change a SmartyTap segment in Chargezen — a live audience such as VIPs, repeat buyers, people who haven't opened in 90 days, subscribers of a product or survey answerers — from the conditions the segment editor offers, counted with sample names before it's saved, and saved only on the merchant's OK. Reads an existing segment's rules and changes only the one asked for, copies a segment to try a variant, and builds an "unengaged" segment to leave out of campaigns. Use when they want to target, define, check or change an audience.
argument-hint: "<who should be in it>"
---

# Segment

Who: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

A segment is live: whoever matches its conditions is in it, recounted as people change, so campaigns and flows reach whoever matches when they send. Being in a segment never means someone agreed to marketing; sending still checks consent. A **list** is different: a fixed group of people put on it by hand or import (`/list-import`).

## 1. Check what exists

`chargezen.smartytap_segments.list.v1` lists the segments with how many people each matched when last counted (`counted_at`; not live), and `chargezen.smartytap_lists.list.v1` the lists. If one already fits, say so and count it instead of building a near-copy.

## Change an existing segment

1. `chargezen.smartytap_segments.list.v1` to find it, then `chargezen.smartytap_segments.get.v1`: its name, description, whether it's active and its conditions, in exactly the shape `chargezen.smartytap_segments.save.v2` takes. Tell the person its rules in plain words.
2. Change **only the rule they asked for** (such as the spend threshold from $300 to $500) and keep every other value as `chargezen.smartytap_segments.get.v1` returned it.
3. `chargezen.smartytap_segments.preview.v1` with the changed conditions: the count now and up to five people. Show the count before and after.
4. On their OK: `chargezen.smartytap_segments.save.v2` with the segment's id as `segment_id`, everything else unchanged, and a new `operation_id`. Campaigns and flows already using it reach the new audience from their next send; say so first.

**To try a variant** without touching the original: `chargezen.smartytap_segments.duplicate.v1` (new `operation_id`) makes "<name> (Copy)" with the same conditions, returned in the shape `chargezen.smartytap_segments.save.v2` takes; rename it and change its rule there. If the original is active, campaigns and flows can choose the copy at once.

## 2. Turn the brief into conditions

1. `chargezen.smartytap_segments.fields.v1`: each field the segment editor can test, its operators, and this workspace's own options (custom properties, tracked events, order activity, matching orders and subscriptions, lists). Use only fields and values listed there.
2. Common audiences, when the fields offer what they need:
   - **VIPs:** total spent or order count above a level the merchant names;
   - **Lapsed buyers:** placed an order before, none in the last N days;
   - **Unengaged:** no email opened or clicked in 90–180 days;
   - **Product buyers or subscribers:** matching orders or subscriptions for a product;
   - **Survey answers:** a contact property a survey saved (such as `heard_about_us`).
3. `chargezen.smartytap_segments.preview.v1` with the conditions: the count now and up to five people by name. If it's refused, fix what it names. If the count looks wrong (zero, or everyone), say so and adjust before going on.

Show the person, in plain words, who's in it ("customers who spent over $300 and ordered in the last year"), the count and the sample names.

## 3. Save

On their OK: `chargezen.smartytap_segments.save.v2` with a name that says who's in it, a short description, `active: true` and a new `operation_id`. Saving an existing segment replaces its whole set of conditions, which is why changes start from `chargezen.smartytap_segments.get.v1` (above).

## 4. Use it

- Target a campaign with it (`/campaign`), or exclude it from one: an unengaged segment in a campaign's **exclude** keeps sends to people who still read, which protects deliverability.
- Start a flow when someone joins it: the **Joined a segment** trigger (`smartytap.segment.entered`), for example a thank-you when someone becomes a VIP.
- A segment no longer wanted can be saved with `active: false` so campaigns and flows can't choose it, or deleted on the merchant's OK (`/audience-cleanup`; deleting never removes the people).
- "Who is in it?" is a count and up to five names from `chargezen.smartytap_segments.preview.v1`; a segment's full membership can't be listed through these tools.
