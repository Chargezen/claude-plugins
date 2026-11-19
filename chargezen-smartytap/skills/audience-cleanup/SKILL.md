---
name: audience-cleanup
description: Tidy SmartyTap segments, lists and contacts in Chargezen — list segments and lists with how many people each holds, find test, empty, duplicate and unused ones, delete only the ones the merchant confirms by name, take people off a list, see who is in a segment, merge two profiles of the same person, and delete a contact on request. Explains that deleting a segment or list never removes people or their consent, and handles one still used by a scheduled campaign. Use for "delete the test segments and lists", cleaning up audiences, "who is in this segment", "take these people off the list", "merge these duplicates" or "delete this contact".
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

## 2. Who is in a segment or a list

- **A segment:** `chargezen.smartytap_segments.members.v1` pages through everyone it matches right now, with name, email, phone and text consent, and `total`. It's worked out live, so two pages read minutes apart may not line up; being in a segment isn't consent (sending still checks it). It brings customers' personal data into the conversation: list only as many people as the question needs, and for a count alone use `chargezen.smartytap_segments.get.v1`.
- **A list:** `chargezen.smartytap_lists.members.v1` pages through everyone on it.

## 3. Delete, one confirmed name at a time

Ask the merchant to confirm each one by its exact name ("Delete the segment *Test VIP copy*?"), then delete only that one:

- a segment: `chargezen.smartytap_segments.delete.v1`. A "Joined a segment" flow started by it stops starting anyone; a draft campaign that names it needs another audience before it can send.
- a list: `chargezen.smartytap_lists.delete.v1`. Sign-up forms, its subscribe page, text keywords and other sign-ups that put people on it keep collecting sign-ups but no longer add anyone to it; a draft campaign that names it needs another audience.

Say these effects in one line before asking. Neither can be restored.

**Refused with `SEGMENT_IN_USE` or `LIST_IN_USE`:** a scheduled campaign still sends to it, and nothing changed. Name the campaigns the refusal lists and offer two ways on: leave it, or take those campaigns off the schedule first with `chargezen.smartytap_campaigns.unschedule.v1` (each goes back to a draft and sends nothing until it's launched again), then delete. Unscheduling is its own yes; ask for it separately.

**Take people off a list** (a hand-made or imported one; a list built from conditions can't lose people by hand): find their `contact_id` with `chargezen.smartytap_lists.members.v1` or `chargezen.contacts.search.v1`, say who and from which list, and on their yes call `chargezen.smartytap_lists.remove_contacts.v1`. It unsubscribes nobody and changes no one's consent: campaigns to the list and segments built on it leave them out from now on, and a flow for people *not* on the list can start for them. If they want someone to stop getting marketing, that's an unsubscribe (`/list-import`), not this. Anyone reported in `not_on_contact_ids` wasn't on the list. `chargezen.smartytap_lists.add_contacts.v1` puts people back.

**Delete a contact**, only when the merchant asks for that person to be deleted: find them with `chargezen.contacts.search.v1` and confirm it's the right person by name and email or phone (with duplicates, say which one). Before asking, say in plain words what happens: their SmartyTap profile, list memberships and back-in-stock requests go and it can't be undone, but their conversations and messages, report figures and unsubscribes stay, so an address that unsubscribed stays unsubscribed. It is **not a full legal erasure** of everything about the person, and someone who is also a store customer still shows in People, can still get campaigns as that customer, and gets a contact again with their next Shopify change. On their yes, `chargezen.contacts.delete.v1`. Never delete a contact to stop their marketing: unsubscribe them instead.

**Merge two profiles of the same person** (a duplicate contact): find both with `chargezen.contacts.search.v1` and show them side by side (name, phones, emails, consent, lists). Ask which one to keep; it becomes `keep_contact_id`, the other `duplicate_contact_id`. Before asking, say in plain words:

- it **can't be undone**, and the duplicate stops being a contact (its id no longer works);
- the kept contact keeps its own name, main phone, main email and custom property values, and takes the duplicate's only where it has none; it gains the duplicate's other phones and emails, tags and lists, and its conversations and texts;
- on each channel the stricter consent stays, so **an unsubscribe on either profile stays in force**; nobody is subscribed by the merge;
- only SmartyTap contacts merge: **Shopify customers are not merged** or changed, and the duplicate's store customer stays a separate customer.

On their yes, `chargezen.contacts.merge.v1`. Merging the same pair again changes nothing. Merge, don't delete, when both profiles belong to one person.

A segment the merchant isn't sure about can be kept but hidden from campaigns and flows instead: save it with `active: false` (`/segment`).

## 4. Report

List what was deleted, what was kept and why, and anything refused with the campaigns that hold it. List anyone taken off a list, merged or deleted as a contact. Remind them once that deleting a segment or list kept all its people.
