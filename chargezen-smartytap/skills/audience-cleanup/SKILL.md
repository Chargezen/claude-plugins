---
name: audience-cleanup
description: Tidy SmartyTap segments and lists in Chargezen — list them with how many people each holds, find test, empty, duplicate and unused ones, and delete only the ones the merchant confirms by name, one at a time. Explains that deleting never removes people or their consent, and handles one still used by a scheduled campaign. Use for "delete the test segments and lists", cleaning up audiences, or "who is in this segment".
argument-hint: "[what to clean up]"
---

# Audience cleanup

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Read only** until the merchant confirms a delete by name.

A segment is dynamic (whoever matches its conditions), a list is static (people added, imported or signed up). Neither is consent. **Deleting a segment or a list never deletes the people in it, their consent or their other lists.** Say this before the first delete.

## 1. See what there is

Run together, following `next_cursor` or the next page until done:

- `chargezen.smartytap_segments.list.v1`: each segment, newest first, with `customer_count` as of `counted_at`. That count is from the last time it was counted, not live; say so. For a live count of one segment, read its conditions with `chargezen.smartytap_segments.get.v1` and count them now with `chargezen.smartytap_segments.preview.v1`.
- `chargezen.smartytap_lists.list.v1`: each list with how many people are on it.

Group what you find for the merchant: **looks like a test** (test, QA, copy, demo in the name), **empty**, **near-duplicates** (same name with "(Copy)", or the same conditions), **inactive**, and the rest. Don't guess that a list or segment is unused from its name alone.

## 2. Who is in a segment

"Who is in this segment?" is answered with a count and a sample: `chargezen.smartytap_segments.get.v1` for its conditions, then `chargezen.smartytap_segments.preview.v1` with those conditions returns the number who match right now and up to five of them. The full membership of a segment can't be listed through these tools. For a list, `chargezen.smartytap_lists.members.v1` pages through everyone on it.

## 3. Delete, one confirmed name at a time

Ask the merchant to confirm each one by its exact name ("Delete the segment *Test VIP copy*?"), then delete only that one:

- a segment: `chargezen.smartytap_segments.delete.v1`. A "Joined a segment" flow started by it stops starting anyone; a draft campaign that names it needs another audience before it can send.
- a list: `chargezen.smartytap_lists.delete.v1`. Sign-up forms, its subscribe page, text keywords and other sign-ups that put people on it keep collecting sign-ups but no longer add anyone to it; a draft campaign that names it needs another audience.

Say these effects in one line before asking. Neither can be restored.

**Refused with `SEGMENT_IN_USE` or `LIST_IN_USE`:** a scheduled campaign still sends to it, and nothing changed. Name the campaigns the refusal lists and offer two ways on: leave it, or take those campaigns off the schedule first with `chargezen.smartytap_campaigns.unschedule.v1` (each goes back to a draft and sends nothing until it's launched again), then delete. Unscheduling is its own yes; ask for it separately.

A segment the merchant isn't sure about can be kept but hidden from campaigns and flows instead: save it with `active: false` (`/segment`).

## 4. Report

List what was deleted, what was kept and why, and anything refused with the campaigns that hold it. Remind them once that the people are all still there.
